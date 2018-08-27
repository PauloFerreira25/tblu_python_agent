# -*- coding: utf-8 -*-
import sys
import click
from uuid import UUID
from tblu_python_agent.cli import pass_context
from tblu_python_agent.shared_module.shared_module import SharedModule


@click.command('configure', short_help='Configure this agent')
@click.option('-a', '--account', required=True, help='Account UUID', type=click.UUID)
@click.option('-c', '--component', required=True, help='component UUID', type=click.UUID)
@click.option('-db', '--db', required=False, default='/var/db/tblu', show_default=True, help='Local DataBase directory. Default: /var/db/tblu', type=click.Path(exists=True, file_okay=False, dir_okay=True, writable=True, readable=True, resolve_path=True, allow_dash=False, path_type=None))
@pass_context
def cli(ctx, account, component, db):
    extra = {"local": __name__, "method": sys._getframe().f_code.co_name}
    logMSG = "Inputs: account: {}, component: {}, db: {}".format(
        account, component, db)
    ctx.log.debug(logMSG, extra=extra)
    if account == component:
        raise click.BadParameter(
            'account and component can not have the same uuid',  param_hint=component)
    ctx.sharedModule = SharedModule(ctx=ctx, dbPath=db)
    ctx.sharedModule.insetProperties(properties='account', value=str(account))
    ctx.sharedModule.insetProperties(
        properties='component', value=str(component))
    ctx.sharedModule.createDefaultMetrics(str(component=component))
    if ctx.debug:
        ctx.sharedModule.dumpConfig()
    ctx.sharedModule.closeDB()
