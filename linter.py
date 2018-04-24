#
# linter.py
# Linter for SublimeLinter4, a code checking framework for Sublime Text 3
#
# Written by nirm03
# Copyright (c) 2013 nirm03
#
# License: MIT
#

"""This module exports the Clang plugin class."""

from SublimeLinter.lint import Linter, util


class Clang(Linter):
    """Provides an interface to clang."""

    regex = (
        r'<stdin>:(?P<line>\d+):'
        r'((?P<col>\d*): )?'  # column number, colon and space are only applicable for single line messages
        # several lines of anything followed by
        # either error/warning/note or newline (= irrelevant backtrace content)
        # (lazy quantifiers so we don’t skip what we seek)
        r'(.*?((?P<error>error)|(?P<warning>warning|note)|\r?\n))+?'
        r': (?P<message>.+)'  # match the remaining content of the current line for output
    )

    multiline = True

    defaults = {
        'selector': 'source.c, source.c++',
        '-Wall': True,
        '-I +': [],
        '-x': None
    }

    on_stderr = None

    def cmd(self):
        """Return the command line to execute."""

        cmd = 'clang -fsyntax-only -fno-caret-diagnostics ${args} -'

        settings = self.get_view_settings()

        # If not set by the user apply magic
        if settings['x'] is None:
            syntax = util.get_syntax(self.view)
            if syntax in ['c', 'c improved']:
                settings['x'] = 'c'
            elif syntax in ['c++', 'c++11']:
                settings['x'] = 'c++'

        return cmd
