# -*- coding: utf-8 -*-
import sys
import click
from uuid import UUID
from tblu_python_agent.cli import pass_context


@click.command('configure', short_help='Configure this agent')
@click.option('-a', '--account', required=True, help='Account UUID', type=click.UUID)
@click.option('-e', '--equipment', required=True, help='equipment UUID', type=click.UUID)
@click.option('-db', '--db', required=False, default='/var/db/tblu', show_default=True, help='Local DataBase directory. Default: /var/db/tblu', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, allow_dash=False, path_type=None))
@pass_context
def cli(ctx, account, equipment, db):
    extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
    logMSG = "Inputs: account: {}, equipment: {}, db: {}".format(
        account, equipment, db)
    ctx.log.debug(logMSG, extra=extra)
    if account == equipment:
        raise click.BadParameter(
            'account and equipment can not have the same uuid',  param_hint=equipment)
    ctx.db.init(ctx, db)
    ctx.db.insetProperties('account', str(account))
    ctx.db.insetProperties('equipment', str(equipment))
    if ctx.debug:
        ctx.db.dumpConfig()
    ctx.db.closeDB()
