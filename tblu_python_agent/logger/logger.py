# -*- coding: utf-8 -*-
import logging


class Logger():

    def __init__(self, logger):
        self.logger = logger

    def getLogLevel(self, x):
        return {
            '1': logging.INFO,
            '2': logging.DEBUG,
            '3': logging.DEBUG,
        }.get(x, logging.ERROR)

    def setLevel(self, level):
        self.logger.setLevel(self.getLogLevel(level))

    def messageFormater(self, msg, *args, **kwargs):
        if 'extra' in kwargs:
            if 'method' in kwargs['extra']:
                t = '['+kwargs['extra']['method']+'] ' + msg
                msg = t
            if 'local' in kwargs['extra']:
                t = '['+kwargs['extra']['local']+'] ' + msg
                msg = t
        return msg

    def debug(self, msg, *args, **kwargs):
        self.log(logging.DEBUG, msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.log(logging.INFO, msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.log(logging.WARNING, msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.log(logging.CRITICAL, msg, *args, **kwargs)

    def exception(self, msg, error, *args, **kwargs):
        self.log(logging.ERROR, msg, *args, **kwargs)
        self.logger.exception(error)

    def log(self, level, msg, *args, **kwargs):
        msgF = self.messageFormater(msg, *args, **kwargs)
        self.logger.log(level, msgF, *args, **kwargs)
