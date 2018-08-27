# -*- coding: utf-8 -*-

SQL_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS metrica (componenteUUID TEXT NOT NULL, metricaUUID TEXT NOT NULL, module TEXT NOT NULL, cron TEXT NOT NULL, parametros TEXT, PRIMARY KEY (componenteUUID, metricaUUID) ) """
SQL_INSERT = "INSERT OR REPLACE INTO metrica (%s) VALUES (%s)"
SQL_SELECT_ALL = """SELECT * FROM metrica"""


class Metrica():

    def __repr__(self):
        retorno = ""+__name__+"("
        for attr, value in self.__dict__.items():
            retorno += attr + ":{},".format(value)
        retorno += ")"
        return retorno

    def fromArray(self, arg):
        self.componenteUUID = arg[0]
        self.metricaUUID = arg[1]
        self.module = arg[2]
        self.cron = arg[3]

    def fromDict(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)

    def getUniq(self):
        return str(self.componenteUUID + "_" + self.metricaUUID)

    def __init__(self, componenteUUID=None, metricaUUID=None, module=None, cron=None):
        if isinstance(componenteUUID, dict):
            self.fromDict(componenteUUID)
        elif isinstance(componenteUUID, list):
            self.fromArray(componenteUUID)
        elif isinstance(componenteUUID, tuple):
            self.fromArray(componenteUUID)
        else:
            self.fromArray([componenteUUID, metricaUUID, module, cron])
