from python_code import mundo_Ave

def test_mundo_Ave___init__():
    assert mundo_Ave.__init__(mundo_Ave('', '', '\x00\x00'), '', '', '') == None

from python_code import mundo_Galloanserae

def test_mundo_Galloanserae___init__():
    assert mundo_Galloanserae.__init__(mundo_Galloanserae('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import mundo_Neoaves

def test_mundo_Neoaves___init__():
    assert mundo_Neoaves.__init__(mundo_Neoaves('', '\x00'), '\x00\x00', '') == None

from python_code import mundo_Neognato

def test_mundo_Neognato___init__():
    assert mundo_Neognato.__init__(mundo_Neognato('', '\x00'), '\x00\x00', '') == None

from python_code import mundo_Neornithe

def test_mundo_Neornithe___init__():
    assert mundo_Neornithe.__init__(mundo_Neornithe('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None

from python_code import mundo_Paleognato

def test_mundo_Paleognato___init__():
    assert mundo_Paleognato.__init__(mundo_Paleognato(''), '') == None

from python_code import mundo_Ratite

def test_mundo_Ratite___init__():
    assert mundo_Ratite.__init__(mundo_Ratite(True), False) == None

from python_code import mundo_Tinamues

def test_mundo_Tinamues___init__():
    assert mundo_Tinamues.__init__(mundo_Tinamues(''), '') == None
