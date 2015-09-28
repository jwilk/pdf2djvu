# encoding=UTF-8

# Copyright © 2009-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This file is part of pdfdjvu.
#
# pdf2djvu is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# pdf2djvu is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

import xml.etree.cElementTree as etree

from tools import (
    assert_equal,
    assert_is_none,
    case,
    xml_find_text,
)

class test(case):
    # + fixed in 0.6.0 [d8c60ea6bc37]

    def test_verbatim(self):
        self.pdf2djvu('--verbatim-metadata').assert_()
        xmp = self.extract_xmp()
        assert_is_none(xmp)

    def test_no_verbatim(self):
        self.require_feature('Exiv2')
        self.pdf2djvu().assert_()
        xmp = self.extract_xmp()
        xmp = etree.fromstring(xmp)
        dcformat = xml_find_text(xmp, 'dc:format')
        assert_equal(dcformat, 'image/vnd.djvu')

# vim:ts=4 sts=4 sw=4 et
