# -*- coding: utf-8 -*-

import sqlite3
import sys

from .dao.propriedade_dao import PropriedadeDAO
from .dao.metrica_dao import MetricaDAO


class MetricasAdapter:
    def __init__(self, ctx, dbPath):
        self.dataBasePath = dbPath
        self.ctx = ctx
        self.db = self.openDB()
        self.propriedadeDAO = PropriedadeDAO(ctx=self.ctx, db=self.db)
        self.metricaDAO = MetricaDAO(ctx=self.ctx, db=self.db)

    def openDB(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        try:
            return sqlite3.connect(self.dataBasePath+"/agent.db")
        except Exception as identifier:
            logMSG = "Fail to open DB"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def closeDB(self):
        self.db.close()

    def dumpConfig(self):
        self.propriedadeDAO.dumpConfig()
        self.metricaDAO.dumpConfig()
