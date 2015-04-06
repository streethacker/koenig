## Koenig

Bundle of APIs, used to monitor system's operational parameters, namely, __CPU__, __MEMORY__, __DISK__, __NETWORK IO__ and __SYSTEM USERS__ statistic.

Thanks to [__psutil__](https://github.com/giampaolo/psutil), I could managed to keep the APIs simple enough. The whole project will contain 3 parts, Koenig is one of them:

* __Koenig__ is a bundle of data service APIs, running as a server in the whole system;

* __Agera__ is a bundle of web APIs, which implemented by [__Flask__](https://github.com/mitsuhiko/flask), running as a client;

* __Wheels__ is a fore-end project, mostly implemented by __Angular JS__;

Apart from __psutil__, another important open source library is [__thriftpy__](https://github.com/eleme/thriftpy). __Thriftpy__ is a pure python implementation of __Apache Thrift__ in a pythonic way, which is open sourced by [__Eleme__](http://v5.ele.me/).


## Quick Start


### Installation

Install as developer

```
$ make develop
```

Install as package

```
$ make install
```

More options

```
$ make help
```

### Development

Run server

```
$ k-server
```

Several APIs need to run with `sudo`, otherwise  __ACCESS_DENIED__  exception would be raised. Therefore, maybe you should run the server with `sudo` specified

```
$ sudo k-server
```

Run client

```
$ k-client
```
