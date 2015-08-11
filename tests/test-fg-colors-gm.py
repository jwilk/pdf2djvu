# encoding=UTF-8

# Copyright © 2010-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This package is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.

from common import (
    assert_equal,
    case,
    count_ppm_colors,
)

class test(case):
    '''
    https://bitbucket.org/jwilk/pdf2djvu/issue/47
    fixed in [3d0f55ae5a65]
    '''
    def test(self):
        yield self._test, 1, 2
        yield self._test, 2, 3
        yield self._test, 4, 5
        yield self._test, 255, 241
        yield self._test, 256, 245
        yield self._test, 652, 245

    def _test(self, i, n):
        self.require_feature('GraphicsMagick')
        self.pdf2djvu(
            '--dpi=72',
            '--fg-colors={0}'.format(i)
        ).assert_()
        r = self.decode()
        r.assert_(stdout=None)
        r = self.decode(mode='foreground')
        r.assert_(stdout=None)
        colors = count_ppm_colors(r.stdout)
        assert_equal(len(colors), n)

# vim:ts=4 sts=4 sw=4 et