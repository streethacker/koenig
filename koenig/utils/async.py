# -*- coding: utf-8 -*-

import celery
import functools

import logging

from koenig.client import make_client

from koenig.settings import (
    CELERY_BROKER,
    CELERY_CONFIG,
)


logger = logging.getLogger(__name__)


broker = 'amqp://{user}:{password}@{host}:{port}/koenig'.\
    format(**CELERY_BROKER)
app = celery.Celery(broker=broker)
app.conf.update(**CELERY_CONFIG)


MAX_RETRIES = 720
RETRY_WAIT = 5


@app.task(max_retries=MAX_RETRIES, bind=True)
def async_api(self, slug, api_name, *args, **kwargs):
    def retry_exc(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                max_retries = kwargs.get('max_retries', MAX_RETRIES)
                retry_wait = kwargs.get('retry_wait', RETRY_WAIT)
                self.retry(
                    exc=e, countdown=retry_wait, max_retries=max_retries)
        return wrapper

    def run_api(api_name, *args):
        with make_client() as c:
            getattr(c, api_name)(*args)

    retry_exc(run_api)(api_name, *args)


def send_task(service_slug, api_name, *args, **kwargs):
    kwargs.setdefault('queue', '{}_queue'.format(service_slug))
    r = async_api.si(service_slug, api_name, *args).apply_async(**kwargs)
    return r
