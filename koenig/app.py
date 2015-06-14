from thriftpy.thrift import TProcessor

from koenig import koenig_thrift
from koenig.dispatcher import KoenigDispatcher

app = TProcessor(koenig_thrift.KoenigService, KoenigDispatcher())
