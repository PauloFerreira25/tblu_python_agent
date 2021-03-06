# -*- coding: utf-8 -*-

import sqlite3
import sys

from ..entity.coleta_entity import SQL_CREATE_TABLE, SQL_INSERT, SQL_SELECT_ALL
from ..entity.coleta_entity import Coleta


class ColetaDAO:
    def __init__(self, ctx, db):
        self.ctx = ctx
        self.db = db
        self.checkDB()

    def checkDB(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        try:
            self.db.cursor().execute(SQL_CREATE_TABLE)
            self.db.commit()
            logMSG = "SQL: {}".format(SQL_CREATE_TABLE)
            self.ctx.log.debug(logMSG, extra=extra)
        except Exception as identifier:
            logMSG = "Fail to check DB"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def insert(self, coleta):
        extra = {"local": __name__,
                 "method": sys._getframe().f_code.co_name}
        try:
            myDict = coleta.__dict__
            qmarks = ', '.join('?' * len(myDict))
            columns = ', '.join(myDict.keys())
            qry = SQL_INSERT % (columns, qmarks)
            logMSG = "SQL: {}, values({})".format(qry, myDict.values())
            self.ctx.log.debug(logMSG, extra=extra)
            self.db.cursor().execute(qry, myDict.values())
            self.db.commit()
        except Exception as identifier:
            logMSG = "Fail to insert"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def getAll(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        try:
            cur = self.db.cursor()
            resultado = []
            for row in cur.execute(SQL_SELECT_ALL):
                resultado.append(Coleta(row))
            cur.close()
            return resultado
        except Exception as identifier:
            logMSG = "Fail to getAll"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def dumpConfig(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        for m in self.getAll():
            logMSG = "DB Coleta - {}".format(m)
            self.ctx.log.debug(logMSG, extra=extra)
