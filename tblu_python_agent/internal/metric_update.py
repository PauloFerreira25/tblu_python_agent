import sys


def cron_run(ctx, metric):
    extra = {"local": __name__,
             "method": sys._getframe().f_code.co_name}
    logMSG = "Metric Update: {}".format(metric)
    ctx.log.debug(logMSG, extra=extra)
