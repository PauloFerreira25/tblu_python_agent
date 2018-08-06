# -*- coding: utf-8 -*-
import sys
import click
import time
from tblu_python_agent.cli import pass_context
from tblu_python_agent.vo.metric import Metric


@click.command('start', short_help='Shows file changes.')
@click.option('-db', '--db', required=False, default='/var/db/tblu', show_default=True, help='Local DataBase directory', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, allow_dash=False, path_type=None))
@pass_context
def cli(ctx, db):
    ctx.db.init(ctx=ctx, dbPath=db)
    ctx.account = ctx.db.getProperties('account')
    ctx.equipment = ctx.db.getProperties('equipment')
    if ctx.account == None or ctx.equipment == None:
        raise click.UsageError('Rode o configure atens')
    else:
        ctx.cron.init(ctx=ctx)
        metricas = ctx.db.getMetrics()
        print(metricas)
        # a = Metric('a', '* * * * *')
        # b = Metric('b', '* * * * *')
        for metrica in metricas:
            ctx.cron.add(metrica)
        try:
            # This is here to simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            ctx.db.closeDB()
            ctx.cron.shutdown()
