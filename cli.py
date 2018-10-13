#!/usr/bin/env python


"""
Commandline tool for interacting with library
"""
import click

from mymusiclib import __version__
from mymusiclib.scales import MajorScale


@click.version_option(__version__)
@click.command()
@click.option("--major", help="key for which you want major scale")
def client(major):
    try:
        key = major
        if len(key) == 3 and key.endswith('sh'):
            key = key.replace('sh', '#')
        res = MajorScale().key(key)
        formatted = [click.style(res[0], bg='red', fg='white'),
                     ','.join(res[1:3]),
                     click.style(res[3], bg='blue', fg='white'),
                     click.style(res[4], bg='green', fg='white'),
                     ','.join(res[5:7]),
                     click.style(res[7], bg='red', fg='white')]

        click.echo(','.join(formatted))
    except TypeError:
        click.echo("Must pass in Key like 'C'")


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    client()
