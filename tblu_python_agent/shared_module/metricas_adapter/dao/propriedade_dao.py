# -*- coding: utf-8 -*-

import sqlite3
import sys
SQL_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS config (properties TEXT UNIQUE, value TEXT)"""
SQL_INSERT = """INSERT OR REPLACE INTO config(properties, value) VALUES(?,?)"""
SQL_SELECT_ALL = """SELECT properties, value FROM config"""
SQL_SELECT_ONE = """SELECT value FROM config WHERE properties == ? LIMIT 1"""


class PropriedadeDAO:
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

    def insert(self, properties, value):
        extra = {"local": __name__,
                 "method": sys._getframe().f_code.co_name}
        try:
            self.db.cursor().execute(SQL_INSERT, (properties, value))
            self.db.commit()
        except Exception as identifier:
            logMSG = "Fail to insert"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def getProperties(self, properties):
        extra = {"local": __name__,
                 "method": sys._getframe().f_code.co_name}
        try:
            cur = self.db.cursor()
            logMSG = "SQL: {}".format(SQL_SELECT_ONE)
            self.ctx.log.debug(logMSG, extra=extra)
            p = cur.execute(SQL_SELECT_ONE, [properties]).fetchone()
            logMSG = "SQL OPTIONS: {}, RESULT: {}".format(properties, p)
            self.ctx.log.debug(logMSG, extra=extra)
            cur.close()
            if p == None:
                return None
            else:
                return p[0]
        except Exception as identifier:
            logMSG = "Fail to getProperties"
            self.ctx.log.exception(logMSG, identifier, extra=extra)
            raise identifier

    def dumpConfig(self):
        extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
        cur = self.db.cursor()
        for row in cur.execute(SQL_SELECT_ALL):
            logMSG = "DB CONFIG - properties({})/value({})".format(
                row[0], row[1])
            self.ctx.log.debug(logMSG, extra=extra)
        cur.close()
