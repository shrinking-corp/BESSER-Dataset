from enum import Enum
from python_code import TriggerTime
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(TriggerTime.AFTER, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(TriggerTime.AFTER, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(TriggerTime.BEFORE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(TriggerTime.AFTER, 0)

def test_Enum___new___2():
    assert Enum.__new__(TriggerTime.AFTER, 'AFTER') == TriggerTime.AFTER

from python_code import sqls_Enum
from python_code import sqls_EnumElement

def test_sqls_EnumElement___init__():
    assert sqls_EnumElement.__init__(sqls_EnumElement('', '\x00', sqls_EnumElement=sqls_Enum()), '\x00\x00', '', sqls_EnumElement=sqls_Enum()) == None

from python_code import sqls_ResultColumn
from python_code import sqls_SelectList
from python_code import sqls_SqlExpr

def test_sqls_ResultColumn___init__():
    assert sqls_ResultColumn.__init__(sqls_ResultColumn('', sqls_ResultColumn46=sqls_SelectList(), sqls_ResultColumn=sqls_SqlExpr()), '', sqls_ResultColumn46=sqls_SelectList(), sqls_ResultColumn=sqls_SqlExpr()) == None

from python_code import sqls_SqlBinaryExpr
from python_code import sqls_SqlExpr

def test_sqls_SqlBinaryExpr___init__():
    assert sqls_SqlBinaryExpr.__init__(sqls_SqlBinaryExpr('', sqls_SqlBinaryExpr=sqls_SqlExpr(), sqls_SqlBinaryExpr117=sqls_SqlExpr()), '', sqls_SqlBinaryExpr=sqls_SqlExpr(), sqls_SqlBinaryExpr117=sqls_SqlExpr()) == None

from python_code import sqls_SqlNumberLiteral

def test_sqls_SqlNumberLiteral___init__():
    assert sqls_SqlNumberLiteral.__init__(sqls_SqlNumberLiteral(0), 0) == None

from python_code import sqls_SqlParam

def test_sqls_SqlParam___init__():
    assert sqls_SqlParam.__init__(sqls_SqlParam(''), '') == None

from python_code import sqls_SqlStringLiteral

def test_sqls_SqlStringLiteral___init__():
    assert sqls_SqlStringLiteral.__init__(sqls_SqlStringLiteral(''), '') == None
