from python_code import viewers_ListViewerElement
from python_code import viewers_ListViewerInput

def test_viewers_ListViewerElement___init__():
    assert viewers_ListViewerElement.__init__(viewers_ListViewerElement('', viewers_ListViewerElement=viewers_ListViewerInput()), '', viewers_ListViewerElement=viewers_ListViewerInput()) == None


from python_code import viewers_TableViewerElement
from python_code import viewers_TableViewerInput

def test_viewers_TableViewerElement___init__():
    assert viewers_TableViewerElement.__init__(viewers_TableViewerElement('', '\x00', viewers_TableViewerElement=viewers_TableViewerInput()), '\x00\x00', '', viewers_TableViewerElement=viewers_TableViewerInput()) == None

