# -*- coding: utf-8 -*-

import time
import datetime
import logging

from functools import partial
from koenig import koenig_thrift

from koenig.exc import (
    raise_user_exc,
    KoenigErrorCode,
)


logger = logging.getLogger(__name__)


def datetime2utc(dt):
    return int(time.mktime(dt.timetuple()))


def utc2datetime(t):
    return datetime.datetime.fromtimestamp(t)


def __serialize(obj, ttype):
    tobj = ttype()
    for key, val in obj.__dict__.iteritems():
        if key.startswith('_'):
            continue
        if isinstance(val, tuple) and key in ('laddr', 'raddr'):
            val = koenig_thrift.TNetworkAddress(*val)
        setattr(tobj, key, val)

    return tobj


def __serialize_list(obj_list, ttype):

    if not isinstance(obj_list, (list, tuple)):
        raise_user_exc(KoenigErrorCode.PARAMETER_TYPE_INVALID)

    func = partial(__serialize, ttype=ttype)
    return [func(obj) for obj in obj_list]


def __serialize_dict(obj_dict, ttype):

    if not isinstance(obj_dict, dict):
        raise_user_exc(KoenigErrorCode.PARAMETER_TYPE_INVALID)

    func = partial(__serialize, ttype=ttype)
    return {k: func(obj) for k, obj in obj_dict.iteritems()}


def serialize(obj, ttype, _list=False, _map=False):
    if _list:
        return __serialize_list(obj, ttype)
    if _map:
        return __serialize_dict(obj, ttype)
    return __serialize(obj, ttype)
