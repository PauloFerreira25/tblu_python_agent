# -*- coding: utf-8 -*-
import sys

createTableMetric = """CREATE TABLE IF NOT EXISTS metric (equipamentUUID TEXT UNIQUE, metricUUID TEXT UNIQUE, value TEXT)"""


class Metric():

    def __repr__(self):
        retorno = ""+__name__+"("
        for attr, value in self.__dict__.items():
            retorno += attr + ":{},".format(value)
        retorno += ")"
        return retorno

    def fromArray(self, arg):
        self._key = arg[0]

    def fromDict(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)

    def getUniq(self):
        return str(self._key)

    def __init__(self, _key=None, cron=None):
        if isinstance(_key, dict):
            self.fromDict(_key)
        elif isinstance(_key, list):
            self.fromArray(_key)
        else:
            self._key = _key
            self.cron = cron
