# -*- coding: utf-8 -*-
import sys

SQL_CREATE_TABLE_METRIC = """CREATE TABLE IF NOT EXISTS metric (\
                                equipamentUUID TEXT NOT NULL, \
                                metricUUID TEXT NOT NULL, \
                                module TEXT NOT NULL, \
                                cron TEXT NOT NULL, \
                                PRIMARY KEY (equipamentUUID, metricUUID) \
                                ) """
SQL_GET_METRICS = """SELECT * FROM metric"""
SQL_INSERT_METRICS = """INSERT OR REPLACE INTO metric(equipamentUUID, metricUUID, module, cron) VALUES(?,?,?,?)"""


def getMetricDefault(equipment):
    return [[equipment, "b514af82-3c4f-4bb5-b1da-a89a0ced5e6f", 'tblu_python_agent.internal.metric_update', '* * * * *']]


class Metric():

    def __repr__(self):
        retorno = ""+__name__+"("
        for attr, value in self.__dict__.items():
            retorno += attr + ":{},".format(value)
        retorno += ")"
        return retorno

    def fromArray(self, arg):
        self.equipamentUUID = arg[0]
        self.metricUUID = arg[1]
        self.module = arg[2]
        self.cron = arg[3]

    def fromDict(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)

    def getUniq(self):
        return str(self.equipamentUUID + "_" + self.metricUUID)

    def __init__(self, equipamentUUID=None, metricUUID=None, module=None, cron=None):
        if isinstance(equipamentUUID, dict):
            self.fromDict(equipamentUUID)
        elif isinstance(equipamentUUID, list):
            self.fromArray(equipamentUUID)
        elif isinstance(equipamentUUID, tuple):
            self.fromArray(equipamentUUID)
        else:
            self.fromArray([equipamentUUID, metricUUID, module, cron])
