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

import re
from SublimeLinter.lint import Linter


OUTPUT_RE = re.compile(
    r'<stdin>:(?P<line>\d+):'
    r'((?P<col>\d*): )?'  # column number, colon and space are only applicable for single line messages
    # several lines of anything followed by
    # either error/warning/note or newline (= irrelevant backtrace content)
    # (lazy quantifiers so we don’t skip what we seek)
    r'(.*?((?P<error>error)|(?P<warning>warning|note)|\r?\n))+?'
    r': (?P<message>.+)',  # match the remaining content of the current line for output
    re.MULTILINE
)


class clangc(Linter):
    cmd = 'clang -fsyntax-only -fno-caret-diagnostics ${args} -'
    defaults = {
        'selector': 'source.c',
        '-Wall': True,
        '-I +': [],
        '-x': 'c'
    }
    regex = OUTPUT_RE
    multiline = True
    on_stderr = None


class clangcplus(Linter):
    cmd = 'clang -fsyntax-only -fno-caret-diagnostics ${args} -'
    defaults = {
        'selector': 'source.c++',
        '-Wall': True,
        '-I +': [],
        '-x': 'c++'
    }
    regex = OUTPUT_RE
    multiline = True
    on_stderr = None
