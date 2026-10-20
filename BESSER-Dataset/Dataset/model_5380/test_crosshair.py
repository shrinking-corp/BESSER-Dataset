from python_code import html_ColumnOption
from python_code import html_SelectComplex

def test_html_ColumnOption___init__():
    assert html_ColumnOption.__init__(html_ColumnOption('', 0, html_ColumnOption=html_SelectComplex()), '', 0, html_ColumnOption=html_SelectComplex()) == None


from python_code import html_Container

def test_html_Container___init__():
    assert html_Container.__init__(html_Container('', html_Container=set()), '', html_Container=set()) == None


from python_code import html_Input

def test_html_Input___init__():
    assert html_Input.__init__(html_Input(False, '', 0, 0, 0, 0), False, '', 0, 0, 0, 0) == None


from python_code import html_Select

def test_html_Select___init__():
    assert html_Select.__init__(html_Select('', html_Select=set()), '', html_Select=set()) == None


from python_code import html_SelectionList

def test_html_SelectionList___init__():
    assert html_SelectionList.__init__(html_SelectionList(True), False) == None

