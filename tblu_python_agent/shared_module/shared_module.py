# -*- coding: utf-8 -*-

from .metricas_adapter.metricas_adapter import MetricasAdapter
from .coletas_adapter.coletas_adapter import ColetasAdapter
from .metricas_padrao import MetricasPadrao
from .cron_controller.cron_controller import CronController


class SharedModule:
    def __init__(self, ctx, dbPath):
        self.ctx = ctx
        self.cronController = CronController(ctx=ctx)
        self.metricasAdapter = MetricasAdapter(ctx=ctx, dbPath=dbPath)
        self.coletasAdapter = ColetasAdapter(ctx=ctx, dbPath=dbPath)
        # self.tempDataAdapter = TempDataAdapter(ctx=ctx, dbPath=dbPath)

    def insetProperties(self, properties, value):
        return self.metricasAdapter.propriedadeDAO.insert(properties=properties, value=value)

    def dumpConfig(self):
        self.metricasAdapter.dumpConfig()
        self.coletasAdapter.dumpConfig()

    def closeDB(self):
        self.metricasAdapter.closeDB()
        self.coletasAdapter.closeDB()

    def shutdown(self):
        self.closeDB()

    def getProperties(self, properties):
        return self.metricasAdapter.propriedadeDAO.getProperties(properties=properties)

    def createDefaultMetrics(self, component):
        metricas = MetricasPadrao(component=component)
        for m in metricas.getAll():
            self.metricasAdapter.metricaDAO.insert(m)

    def runUpdate(self):
        metricas = MetricasPadrao(component=self.ctx.component)
        self.cronController.tick(metricas.getUpdate())

    def startCrons(self):
        for m in self.metricasAdapter.metricaDAO.getAll():
            self.cronController.add(m)

    def insertColeta(self, coleta):
        return self.coletasAdapter.coletaDAO.insert(coleta=coleta)
