import sys
from ..enviar_dados_adapter import enviaDados
# try:
# modulo = __import__(metric.module, None, None, ['cron_run'])
#         except ImportError:
#             installer = ['install', '-U', '--user', metric.module]
#             try:
#                 import pip
#                 pip.main(installer)  # pip old
#             except AttributeError:
#                 try:
#                     from pip._internal import main  # pip new
#                     main(installer)
#                 except AttributeError as e1:
#                     raise


def cron_run(ctx, metric):
    extra = {"local": __name__,
             "method": sys._getframe().f_code.co_name}
    try:
        modulo = __import__(metric.module, None, None, ['cron_run'])
        logMSG = "Cron Run: {}".format(metric)
        ctx.log.debug(logMSG, extra=extra)
        resultado = modulo.cron_run(ctx, metric)
        enviaDados(ctx, metric, resultado)
    except Exception as identifier:
        logMSG = "Fail to Run Cron:{}".format(metric.getUniq())
        ctx.log.exception(logMSG, error=identifier, extra=extra)
