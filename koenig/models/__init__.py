# -*- coding: utf-8 -*-

import functools
import logging

from sqlalchemy import (
    create_engine,
    func,
    Column,
    DateTime,
    Integer,
    Numeric,
)

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)

from sqlalchemy.exc import (
    SQLAlchemyError,
)

from koenig.exc import (
    raise_system_exc,
    KoenigErrorCode,
)

from koenig.settings import (
    MYSQL_SETTINGS,
)

logger = logging.getLogger(__name__)

####################
# Session maker
####################
master_url = ("mysql+pymysql://{user}:{passwd}@{host}:{port}/{database}"
              "?charset=utf8".format(**MYSQL_SETTINGS))
mysql_engine = create_engine(
    master_url,
    pool_size=10,
    max_overflow=-1,
    pool_recycle=3600)

DBSession = scoped_session(sessionmaker(bind=mysql_engine, autoflush=False))

session = DBSession()

###################
# Table Declare
###################
from sqlalchemy.ext.declarative import declarative_base
DeclarativeBase = declarative_base()


class TimestampMixin(object):
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class RuntimeProfile(DeclarativeBase, TimestampMixin):

    __tablename__ = 'tb_koenig_runtime_profile'

    id = Column(Integer, primary_key=True)
    cpu_percent = Column(Numeric(2, 1), default=0)
    mem_percent = Column(Numeric(2, 1), default=0)
    profile_ts = Column(DateTime, default=0)

    @classmethod
    def new(clazz, **kwargs):
        profile = RuntimeProfile()
        for key, val in kwargs.iteritems():
            setattr(profile, key, val)

        DBSession().add(profile)
        DBSession().flush()

    @classmethod
    def get_by_ts(clazz, start_ts, end_ts):
        return DBSession().query(RuntimeProfile).\
            filter(RuntimeProfile.profile_ts >= start_ts).\
            filter(RuntimeProfile.profile_ts < end_ts).\
            all()


def gen_commit_deco(DBSession, raise_exc, error_code):
    def wrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            session = DBSession()
            try:
                session.flush()
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise_exc(error_code, repr(e))
            finally:
                session.close()
            return result
        return wrapper
    return wrap

db_commit = gen_commit_deco(
    DBSession,
    raise_system_exc,
    KoenigErrorCode.DATABASE_ERROR)
