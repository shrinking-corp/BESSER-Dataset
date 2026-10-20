from python_code import ric_Button

def test_ric_Button___init__():
    assert ric_Button.__init__(ric_Button('', False, '\x00\x00'), '', False, '') == None


from python_code import ric_ClassifiableComponent

def test_ric_ClassifiableComponent___init__():
    assert ric_ClassifiableComponent.__init__(ric_ClassifiableComponent(''), '') == None


from python_code import ric_Datepicker

def test_ric_Datepicker___init__():
    assert ric_Datepicker.__init__(ric_Datepicker(False, '', '', 0, False, False, False, False), False, '', '', 0, False, False, False, False) == None


from python_code import ric_Heading

def test_ric_Heading___init__():
    assert ric_Heading.__init__(ric_Heading(''), '') == None


from python_code import ric_IdentifiableComponent

def test_ric_IdentifiableComponent___init__():
    assert ric_IdentifiableComponent.__init__(ric_IdentifiableComponent(''), '') == None


from python_code import ric_Image
from python_code import ric_Logo

def test_ric_Image___init__():
    assert ric_Image.__init__(ric_Image('', '\x00', ric_Image=ric_Logo()), '\x00\x00', '', ric_Image=ric_Logo()) == None


from python_code import ric_InputFile

def test_ric_InputFile___init__():
    assert ric_InputFile.__init__(ric_InputFile(0, 0, False), 0, 0, False) == None


from python_code import ric_MessageDialog

def test_ric_MessageDialog___init__():
    assert ric_MessageDialog.__init__(ric_MessageDialog(False, False, 0, 0, 0, 0, 0, 0, '\x00', '', False, ric_MessageDialog=set()), False, True, 0, 0, 0, 0, 0, 0, '', '', False, ric_MessageDialog=set()) == None


from python_code import ric_OrderedList

def test_ric_OrderedList___init__():
    assert ric_OrderedList.__init__(ric_OrderedList('', ric_OrderedList=set()), '', ric_OrderedList=set()) == None


from python_code import ric_Paragraph

def test_ric_Paragraph___init__():
    assert ric_Paragraph.__init__(ric_Paragraph(''), '') == None


from python_code import ric_AccordionPanel
from python_code import ric_Section

def test_ric_Section___init__():
    assert ric_Section.__init__(ric_Section('', ric_Section=ric_AccordionPanel(), ric_Section80=set(), ric_Section83=set(), ric_Section86=set(), ric_Section89=set(), ric_Section92=set(), ric_Section95=set(), ric_Section98=set()), '', ric_Section=ric_AccordionPanel(), ric_Section80=set(), ric_Section83=set(), ric_Section86=set(), ric_Section89=set(), ric_Section92=set(), ric_Section95=set(), ric_Section98=set()) == None


from python_code import ric_Select

def test_ric_Select___init__():
    assert ric_Select.__init__(ric_Select(0, False, ric_Select=set()), 0, False, ric_Select=set()) == None


from python_code import ric_Span

def test_ric_Span___init__():
    assert ric_Span.__init__(ric_Span(''), '') == None


from python_code import ric_TextArea

def test_ric_TextArea___init__():
    assert ric_TextArea.__init__(ric_TextArea(0, 0, False), 0, 0, False) == None


from python_code import ric_TextField

def test_ric_TextField___init__():
    assert ric_TextField.__init__(ric_TextField(0, 0, False, False), 0, 0, False, True) == None


from python_code import ric_UnorderedList

def test_ric_UnorderedList___init__():
    assert ric_UnorderedList.__init__(ric_UnorderedList('', ric_UnorderedList=set()), '', ric_UnorderedList=set()) == None

