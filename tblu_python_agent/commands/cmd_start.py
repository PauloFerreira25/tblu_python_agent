# -*- coding: utf-8 -*-
import sys
import click
import time
from tblu_python_agent.cli import pass_context
# from tblu_python_agent.vo.metric import Metric
from tblu_python_agent.shared_module.shared_module import SharedModule


@click.command('start', short_help='Shows file changes.')
@click.option('-db', '--db', required=False, default='/var/db/tblu', show_default=True, help='Local DataBase directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, allow_dash=False, path_type=None))
@pass_context
def cli(ctx, db):
    extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
    logMSG = "Inputs: db: {}".format(db)
    ctx.log.debug(logMSG, extra=extra)
    ctx.sharedModule = SharedModule(ctx=ctx, dbPath=db)
    ctx.account = ctx.sharedModule.getProperties('account')
    ctx.component = ctx.sharedModule.getProperties('component')
    if ctx.account == None or ctx.component == None:
        raise click.UsageError('Rode o configure atens')
    else:
        ctx.sharedModule.runUpdate()
        ctx.sharedModule.startCrons()
        try:
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            ctx.sharedModule.shutdown()
