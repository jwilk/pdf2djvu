# encoding=UTF-8

# Copyright © 2015-2016 Jakub Wilk <jwilk@jwilk.net>
#
# This file is part of pdf2djvu.
#
# pdf2djvu is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# pdf2djvu is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

from tools import (
    case,
    re,
)

class test(case):

    # Bug: https://bitbucket.org/jwilk/pdf2djvu/issues/113

    def test(self):
        r = self.pdf2djvu('--page-title-template', '{label}', quiet=False)
        r.assert_(stderr=re('Warning: Ignoring duplicate page title: x\n'))
        r = self.ls()
        r.assert_(stdout=re(
            r'\n'
            r'\s*1\s+P\s+\d+\s+[\w.]+\s+T=x\n'
            r'\s*2\s+P\s+\d+\s+[\w.]+\n'
            r'\s*3\s+P\s+\d+\s+[\w.]+\n'
        ))

# vim:ts=4 sts=4 sw=4 et
