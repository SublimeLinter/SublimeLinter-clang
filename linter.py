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

import shlex
from SublimeLinter.lint import Linter, util


class Clang(Linter):

    """Provides an interface to clang."""

    syntax = ('c', 'c improved', 'c++', 'c++11')
    executable = 'clang'

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
        'include_dirs': [],
        'extra_flags': ""
    }

    base_cmd = (
        'clang -fsyntax-only '
        '-fno-caret-diagnostics -Wall '
    )

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.

        """

        result = self.base_cmd

        if util.get_syntax(self.view) in ['c', 'c improved']:
            result += ' -x c '
        elif util.get_syntax(self.view) in ['c++', 'c++11']:
            result += ' -x c++ '

        settings = self.get_view_settings()
        result += settings.get('extra_flags', '')

        include_dirs = settings.get('include_dirs', [])

        if include_dirs:
            result += ' '.join([' -I ' + shlex.quote(include) for include in include_dirs])

        return result + ' -'
