# -*- coding: utf-8 -*-

import argparse
import importlib


def server():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help="listen host")
    parser.add_argument('--port', help="listen port")
    args = parser.parse_args()

    service_server = importlib.import_module("koenig.server")
    service_server.server(args.host, args.port).serve()


def client():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', help="listen host")
    parser.add_argument('--port', help="listen port")
    args = parser.parse_args()

    service_client = importlib.import_module("koenig")
    with service_client.koenig_client(args.host, args.port) as c:
        c.ping()
        import IPython
        IPython.embed()
