# -*- coding: utf-8 -*-
import sqlite3
import sys
from tblu_python_agent.vo.metric import createTableMetric


class LocalDB():

    def init(self, ctx, dbPath):
        self.dataBasePath = dbPath
        self.ctx = ctx
        self.connAgent = None
        self.openDB()
        self.checkDB()

    def openDB(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        try:
            self.connAgent = sqlite3.connect(self.dataBasePath+"/agent.db")
            self.connTemp = sqlite3.connect(self.dataBasePath+"/temp.db")
            self.connData = sqlite3.connect(self.dataBasePath+"/data.db")
        except Exception as identifier:
            logMSG = "Fail to open DB"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def checkDBAgent(self):
        self.connAgent.cursor().execute(
            """CREATE TABLE IF NOT EXISTS config (properties TEXT UNIQUE, value TEXT)""")
        self.connAgent.commit()

    def checkDBTemp(self):
        self.connTemp.cursor().execute(
            """CREATE TABLE IF NOT EXISTS temp (properties TEXT UNIQUE, value TEXT)""")
        self.connTemp.commit()

    def checkDBData(self):
        self.connData.cursor().execute(createTableMetric)
        self.connData.commit()

    def checkDB(self):
        self.checkDBAgent()
        self.checkDBTemp()
        self.checkDBData()

    def insetProperties(self, properties, value):
        self.connAgent.cursor().execute(
            """INSERT OR REPLACE INTO config(properties, value) VALUES(?,?)""", (
                properties, value))
        self.connAgent.commit()

    def closeDB(self):
        self.connAgent.close()

    def dumpDB(self):
        self.dumpConfig()

    def dumpConfig(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        cur = self.connAgent.cursor()
        for row in cur.execute("""SELECT properties, value FROM config"""):
            # print(row)
            logMSG = "DB CONFIG - properties({})/value({})".format(
                row[0], row[1])
            self.ctx.log.debug(logMSG, extra=extra)
        cur.close()
