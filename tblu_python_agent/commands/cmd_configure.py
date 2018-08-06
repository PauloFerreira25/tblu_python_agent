# -*- coding: utf-8 -*-
import sys
import click
from uuid import UUID
from tblu_python_agent.cli import pass_context


@click.command('configure', short_help='Configure this agent')
@click.option('-a', '--account', required=True, help='Account UUID', type=click.UUID)
@click.option('-s', '--server', required=True, help='Server UUID', type=click.UUID)
@click.option('-db', '--db', required=False, default='/var/db/tblu', show_default=True, help='Local DataBase directory. Default: /var/db/tblu', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, allow_dash=False, path_type=None))
@pass_context
def cli(ctx, account, server, db):
    extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
    logMSG = "Inputs: account: {}, server: {}, db: {}".format(
        account, server, db)
    ctx.log.debug(logMSG, extra=extra)
    if account == server:
        raise click.BadParameter(
            'account and server can not have the same uuid',  param_hint=server)
    ctx.db.init(ctx, db)
    ctx.db.insetProperties('account', str(account))
    ctx.db.insetProperties('server', str(server))
    if ctx.debug:
        ctx.db.dumpConfig()
