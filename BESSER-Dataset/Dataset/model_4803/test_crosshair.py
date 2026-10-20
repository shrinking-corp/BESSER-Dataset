from python_code import pltest_Child1
from python_code import pltest_Common

def test_pltest_Child1___init__():
    assert pltest_Child1.__init__(pltest_Child1('', pltest_Child1=pltest_Common()), '', pltest_Child1=pltest_Common()) == None


from python_code import pltest_Circle
from python_code import pltest_WhatEver

def test_pltest_Circle___init__():
    assert pltest_Circle.__init__(pltest_Circle('', 0.0, 0.0, pltest_Circle=set(), pltest_Circle5=pltest_WhatEver()), '', 0.0, 0.0, pltest_Circle=set(), pltest_Circle5=pltest_WhatEver()) == None


from python_code import pltest_Numbers

def test_pltest_Numbers___init__():
    assert pltest_Numbers.__init__(pltest_Numbers(0, '', 0.0, 0.0, '', ''), 0, '', 0.0, 0.0, '', '') == None

