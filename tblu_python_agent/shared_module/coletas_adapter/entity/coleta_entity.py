# -*- coding: utf-8 -*-

SQL_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS coleta (componenteUUID TEXT NOT NULL, metricaUUID TEXT NOT NULL, accountUUID TEXT NOT NULL, dataColeta TEXT NOT NULL, coleta TEXT NULL, PRIMARY KEY (componenteUUID, metricaUUID, accountUUID, dataColeta) ) """
SQL_INSERT = "INSERT INTO coleta (%s) VALUES (%s)"
SQL_SELECT_ALL = """SELECT * FROM coleta"""


class Coleta():

    def __repr__(self):
        retorno = ""+__name__+"("
        for attr, value in self.__dict__.items():
            retorno += attr + ":{},".format(value)
        retorno += ")"
        return retorno

    def fromArray(self, arg):
        self.componenteUUID = arg[0]
        self.metricaUUID = arg[1]
        self.accountUUID = arg[2]
        self.dataColeta = arg[3]
        self.coleta = arg[4]

    def fromDict(self, data):
        for attr, value in data.items():
            setattr(self, attr, value)

    def __init__(self, componenteUUID=None, metricaUUID=None, accountUUID=None, dataColeta=None, coleta=None):
        if isinstance(componenteUUID, dict):
            self.fromDict(componenteUUID)
        elif isinstance(componenteUUID, list):
            self.fromArray(componenteUUID)
        elif isinstance(componenteUUID, tuple):
            self.fromArray(componenteUUID)
        else:
            self.fromArray([componenteUUID, metricaUUID,
                            accountUUID, dataColeta, coleta])
