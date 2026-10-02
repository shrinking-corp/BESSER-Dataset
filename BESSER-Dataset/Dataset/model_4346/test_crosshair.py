from python_code import hutn_ClassObjectSlot

def test_hutn_ClassObjectSlot___init__():
    assert hutn_ClassObjectSlot.__init__(hutn_ClassObjectSlot()) == None

def test_hutn_ClassObjectSlot_getClassObjects():
    assert hutn_ClassObjectSlot.getClassObjects(hutn_ClassObjectSlot()) == None

def test_hutn_ClassObjectSlot_setClassObjects():
    assert hutn_ClassObjectSlot.setClassObjects(hutn_ClassObjectSlot(), '') == None

def test_hutn_ClassObjectSlot_addClassObject():
    assert hutn_ClassObjectSlot.addClassObject(hutn_ClassObjectSlot(), '') == None

from python_code import hutn_ModelElement

def test_hutn_ModelElement___init__():
    assert hutn_ModelElement.__init__(hutn_ModelElement(0, 0), 0, 0) == None

from python_code import hutn_Object

def test_hutn_Object___init__():
    assert hutn_Object.__init__(hutn_Object('', '\x00'), '\x00\x00', '') == None
