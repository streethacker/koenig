# -*- coding: utf-8 -*-

###############
# MYSQL
###############

MYSQL_SETTINGS = {
    'user': 'root',
    'passwd': 'root',
    'host': 'localhost',
    'port': 3306,
    'database': 'koenig',
}


##############
# THRIFT
##############

KOENIG_THRIFT_SETTINGS = {
    'host': 'localhost',
    'port': 27028,
}


##############
# LOGGING
##############

LOGGING_SETTINGS = {
    'version': 1,

    'disable_existing_loggers': False,

    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },

    'loggers': {
        'koenig': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        }
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'general',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': '/var/log/koenig/koenig.log',
        },
    },

    'formatters': {
        'general': {
            'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                      ' %(message)s'
        },
        'detail': {
            'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                      '[%(pathname)s: %(lineno)d]'
                      ' %(message)s',
        },
    }
}
