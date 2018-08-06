# -*- coding: utf-8 -*-
import sys

from datetime import datetime
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.base import STATE_RUNNING
from apscheduler.triggers.cron import CronTrigger
import logging
import click_log
log1 = click_log.basic_config('apscheduler.executors.default')
log2 = click_log.basic_config('apscheduler.scheduler')


class Cron():

    def init(self, ctx):
        self.ctx = ctx
        log1.setLevel(ctx.logLevel)
        log2.setLevel(ctx.logLevel)
        self.executors = {
            'default': ThreadPoolExecutor(20),
            'processpool': ProcessPoolExecutor(5)
        }
        self.job_defaults = {
            'coalesce': False,
            'max_instances': 1
        }
        self.scheduler = BackgroundScheduler(executors=self.executors,
                                             job_defaults=self.job_defaults)
        self.start()

    def tick(self, metric):
        try:
            extra = {"local": __name__,
                     "method": sys._getframe().f_code.co_name}
            logMSG = "Tick!{}, The time is: {}".format(metric, datetime.now())
            self.ctx.log.debug(logMSG, extra=extra)
            if(metric._key == 'a'):
                time.sleep(150)
                logMSG = "Tick2!{}, The time is: {}".format(
                    metric, datetime.now())
                self.ctx.log.debug(logMSG, extra=extra)
            else:
                logMSG = "Tick2!{}, The time is: {}".format(
                    metric, datetime.now())
                self.ctx.log.debug(logMSG, extra=extra)
        except Exception as identifier:
            logMSG = "Fail to Tick"
            self.ctx.log.exception(logMSG, error=identifier, extra=extra)
            raise

    def start(self):
        try:
            extra = {"local": __name__,
                     "method": sys._getframe().f_code.co_name}
            if self.scheduler.state != STATE_RUNNING:
                logMSG = "Scheduler Start".format()
                self.ctx.log.debug(logMSG, extra=extra)
                self.scheduler.start()
        except Exception as identifier:
            logMSG = "Fail to Start Cron"
            self.ctx.log.exception(logMSG, error=identifier, extra=extra)
            raise

    def add(self, metric):
        try:
            extra = {"local": __name__,
                     "method": sys._getframe().f_code.co_name}
            self.scheduler.add_job(self.tick,
                                   CronTrigger.from_crontab(metric.cron),
                                   args=[metric],
                                   seconds=3,
                                   id=metric.getUniq(), jitter=120, replace_existing=True)
            logMSG = "ADD - UNIQ {} - {}".format(metric.getUniq(), metric)
            self.ctx.log.debug(logMSG, extra=extra)
        except Exception as identifier:
            logMSG = "Fail to ADD in Cron"
            self.ctx.log.exception(logMSG, error=identifier, extra=extra)
            raise

    def shutdown(self):
        self.scheduler.shutdown()
