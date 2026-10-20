from python_code import BorderPane
from python_code import Button
from python_code import HBox
from python_code import Label
from python_code import VBox
from python_code import connect_four_gui_StartMenu

def test_connect_four_gui_StartMenu___init__():
    assert connect_four_gui_StartMenu.__init__(connect_four_gui_StartMenu('', Label(), Button(), HBox(), VBox(), BorderPane()), '', Label(), Button(), HBox(), VBox(), BorderPane()) == None


from python_code import connect_four_gui_Token

def test_connect_four_gui_Token___init__():
    assert connect_four_gui_Token.__init__(connect_four_gui_Token(False, '', '\x00\x00'), False, '', '') == None

