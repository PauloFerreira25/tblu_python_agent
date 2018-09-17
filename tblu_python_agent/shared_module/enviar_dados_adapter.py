import sys
import requests
from .coletas_adapter.entity.coleta_entity import Coleta
import time
import json


def enviaDados(ctx, metric, resultado):
    extra = {"local": __name__,
             "method": sys._getframe().f_code.co_name}
    try:
        logMSG = "Envia Dados: {}".format(metric.getUniq())
        ctx.log.debug(logMSG, extra=extra)
        millis = int(round(time.time() * 1000))
        c = Coleta(componenteUUID=metric.componenteUUID, metricaUUID=metric.metricaUUID,
                   accountUUID=ctx.account,
                   dataColeta=millis, coleta=resultado)
        data = c.__dict__
        url = ctx.baseAPI + '/coleta'
        requests.post(url, json=data)
    except Exception:
        ctx.sharedModule.insertColeta(c)
