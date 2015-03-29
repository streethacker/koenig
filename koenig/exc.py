# -*- coding: utf-8 -*-

from koenig import (
    koenig_thrift,
)


KoenigErrorCode = koenig_thrift.KoenigErrorCode
KoenigUserException = koenig_thrift.KoenigUserException
KoenigSystemException = koenig_thrift.KoenigSystemException

TRANSLATIONS = {
    KoenigErrorCode.ACCESS_DENIED: u'需要sudo权限',
    KoenigErrorCode.PLATFORM_NOT_SUPPORT: u'不支持的系统调用',
    KoenigErrorCode.PROCESS_NOT_FOUND: u'指定的pid未找到',
    KoenigErrorCode.UNKNOWN_ERROR: u'未知的系统错误',
}


def raise_user_exc(code, message=None):
    raise KoenigUserException(
        code,
        KoenigErrorCode._VALUES_TO_NAMES[code],
        message or TRANSLATIONS[code]
    )


def raise_system_exc(code, message=None):
    raise KoenigSystemException(
        code,
        KoenigErrorCode._VALUES_TO_NAMES[code],
        message or TRANSLATIONS[code]
    )
