# -*- coding: utf-8 -*-

from functools import (
    partial,
)

from koenig import (
    koenig_thrift,
)


def serialize_to_ttype(obj, ttype):
    tobj = ttype()
    for key, val in obj.__dict__.iteritems():
        if isinstance(val, tuple):
            val = koenig_thrift.TNetworkAddress(*val)
        setattr(tobj, key, val)

    return tobj


def serialize_to_ttype_list(obj_list, ttype):
    serialize = partial(serialize_to_ttype, ttype=ttype)

    result = [serialize(obj) for obj in obj_list]
    return result


def serialize_to_ttype_dict(obj_dict, ttype):
    serialize = partial(serialize_to_ttype, ttype=ttype)

    result = {k: serialize(obj) for k, obj in obj_dict.iteritems()}
    return result
