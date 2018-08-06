# -*- coding: utf-8 -*-
import os
import sys
import click

"""Log"""
import logging
import click_log
logger = click_log.basic_config(__name__)

from .logger.logger import Logger
from .database.database import LocalDB
from .cron.cron import Cron

CONTEXT_SETTINGS = dict(auto_envvar_prefix='COMPLEX')


class Context(object):

    def __init__(self):
        self.debug = False
        self.logLevel = 0
        self.log = Logger(logger)
        self.db = LocalDB()
        self.cron = Cron()


pass_context = click.make_pass_decorator(Context, ensure=True)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'commands'))


class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and \
               filename.startswith('cmd_'):
                rv.append(filename[4:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
                fileImport = 'tblu_python_agent.commands.cmd_' + name
            mod = __import__(fileImport,
                             None, None, ['cli'])
        except ImportError:
            return
        return mod.cli


@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
# @click.option('--home', type=click.Path(exists=True, file_okay=False,
#                                         resolve_path=True),
#   help = 'Changes the folder to operate on.')
@click.option('-v', '--verbose', default=0, count=True,
              help='Enables verbose mode.')
@pass_context
def cli(ctx, verbose):
    """TBLu Agent Command Line"""
    ctx.log.setLevel(str(verbose))
    ctx.logLevel = ctx.log.getLogLevel(str(verbose))
    if verbose >= 2:
        ctx.debug = True

    # if home is not None:
    #     ctx.home = home


# if __name__ == "__main__":
#     cli()
