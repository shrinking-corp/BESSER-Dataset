from python_code import DocBook_Para
from python_code import DocBook_Section

def test_DocBook_Para___init__():
    assert DocBook_Para.__init__(DocBook_Para('', Para=DocBook_Section(), paras=DocBook_Section()), '', Para=DocBook_Section(), paras=DocBook_Section()) == None


from python_code import DocBook_TitledElement

def test_DocBook_TitledElement___init__():
    assert DocBook_TitledElement.__init__(DocBook_TitledElement(''), '') == None

