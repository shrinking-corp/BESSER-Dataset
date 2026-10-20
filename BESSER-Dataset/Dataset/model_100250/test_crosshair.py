from python_code import stylesheets_EmbeddedStyleSheet

def test_stylesheets_EmbeddedStyleSheet___init__():
    assert stylesheets_EmbeddedStyleSheet.__init__(stylesheets_EmbeddedStyleSheet('', '\x00'), '\x00\x00', '') == None


from python_code import stylesheets_StyleSheetReference

def test_stylesheets_StyleSheetReference___init__():
    assert stylesheets_StyleSheetReference.__init__(stylesheets_StyleSheetReference(''), '') == None


from python_code import stylesheets_Theme
from python_code import stylesheets_WorkspaceThemes

def test_stylesheets_Theme___init__():
    assert stylesheets_Theme.__init__(stylesheets_Theme('', '', '', stylesheets_Theme3=set(), stylesheets_Theme=stylesheets_WorkspaceThemes()), '', '', '', stylesheets_Theme3=set(), stylesheets_Theme=stylesheets_WorkspaceThemes()) == None

