from python_code import swt_AbstractList

def test_swt_AbstractList___init__():
    assert swt_AbstractList.__init__(swt_AbstractList('', 0), '', 0) == None


from python_code import swt_AbstractMenu

def test_swt_AbstractMenu___init__():
    assert swt_AbstractMenu.__init__(swt_AbstractMenu('', False, False, swt_AbstractMenu=set()), '', False, True, swt_AbstractMenu=set()) == None


from python_code import swt_Browser

def test_swt_Browser___init__():
    assert swt_Browser.__init__(swt_Browser(False, '', '\x00\x00'), False, '', '') == None


from python_code import swt_Combo

def test_swt_Combo___init__():
    assert swt_Combo.__init__(swt_Combo('', 0), '', 0) == None


from python_code import swt_DateTime

def test_swt_DateTime___init__():
    assert swt_DateTime.__init__(swt_DateTime(0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0) == None


from python_code import swt_Decorations
from python_code import swt_MenuBar

def test_swt_Decorations___init__():
    assert swt_Decorations.__init__(swt_Decorations(False, False, parent=swt_MenuBar(), Decorations=swt_MenuBar()), False, False, parent=swt_MenuBar(), Decorations=swt_MenuBar()) == None


from python_code import swt_FillLayout

def test_swt_FillLayout___init__():
    assert swt_FillLayout.__init__(swt_FillLayout('\x00\x00', 0, 0, 0), '', 0, 0, 0) == None


from python_code import swt_FormLayout

def test_swt_FormLayout___init__():
    assert swt_FormLayout.__init__(swt_FormLayout(0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0, 0) == None


from python_code import swt_GridData

def test_swt_GridData___init__():
    assert swt_GridData.__init__(swt_GridData('', '', 0, 0, 0, 0, 0, 0, False, False, 0, 0, False), '', '', 0, 0, 0, 0, 0, 0, True, False, 0, 0, True) == None


from python_code import swt_GridLayout

def test_swt_GridLayout___init__():
    assert swt_GridLayout.__init__(swt_GridLayout(0, False, 0, 0, 0, 0, 0, 0, 0, 0), 0, False, 0, 0, 0, 0, 0, 0, 0, 0) == None


from python_code import swt_Group

def test_swt_Group___init__():
    assert swt_Group.__init__(swt_Group(''), '') == None


from python_code import swt_IntervalControl

def test_swt_IntervalControl___init__():
    assert swt_IntervalControl.__init__(swt_IntervalControl(0, 0, 0), 0, 0, 0) == None


from python_code import swt_IntervalSelector

def test_swt_IntervalSelector___init__():
    assert swt_IntervalSelector.__init__(swt_IntervalSelector('', 0, 0), '\x00', 0, 0) == None


from python_code import swt_Labeled

def test_swt_Labeled___init__():
    assert swt_Labeled.__init__(swt_Labeled('', '\x00'), '\x00\x00', '') == None


from python_code import swt_LineAttributes

def test_swt_LineAttributes___init__():
    assert swt_LineAttributes.__init__(swt_LineAttributes(0.0, '', '', '', 0.0, 0.0, 0.0), 0.0, '', '', '\x00', 0.0, 0.0, 0.0) == None


from python_code import swt_List

def test_swt_List___init__():
    assert swt_List.__init__(swt_List('', 0, '\x00\x00'), '', 0, '') == None


from python_code import swt_ProgressBar

def test_swt_ProgressBar___init__():
    assert swt_ProgressBar.__init__(swt_ProgressBar(''), '') == None


from python_code import swt_RGBColor

def test_swt_RGBColor___init__():
    assert swt_RGBColor.__init__(swt_RGBColor(0, 0, 0), 0, 0, 0) == None


from python_code import swt_RowData

def test_swt_RowData___init__():
    assert swt_RowData.__init__(swt_RowData(0, 0, False), 0, 0, False) == None


from python_code import swt_RowLayout

def test_swt_RowLayout___init__():
    assert swt_RowLayout.__init__(swt_RowLayout(0, False, False, False, False, False, 0, 0, 0, 0, '', 0, 0), 0, True, False, False, True, False, 0, 0, 0, 0, '', 0, 0) == None


from python_code import swt_Separator

def test_swt_Separator___init__():
    assert swt_Separator.__init__(swt_Separator(''), '') == None


from python_code import swt_Slider

def test_swt_Slider___init__():
    assert swt_Slider.__init__(swt_Slider(0), 0) == None


from python_code import swt_Spinner

def test_swt_Spinner___init__():
    assert swt_Spinner.__init__(swt_Spinner(0, 0), 0, 0) == None


from python_code import swt_SystemColor

def test_swt_SystemColor___init__():
    assert swt_SystemColor.__init__(swt_SystemColor(''), '') == None


from python_code import swt_Text

def test_swt_Text___init__():
    assert swt_Text.__init__(swt_Text(0, '', '', '', '\x00', False, '', 0, 0), 0, '', '', '', '', False, '', 0, 0) == None


from python_code import swt_Viewer

def test_swt_Viewer___init__():
    assert swt_Viewer.__init__(swt_Viewer(''), '') == None


from python_code import swt_Widget

def test_swt_Widget___init__():
    assert swt_Widget.__init__(swt_Widget(0), 0) == None

