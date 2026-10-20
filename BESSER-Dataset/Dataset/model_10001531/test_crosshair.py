from python_code import Controller_EventManager

def test_Controller_EventManager___init__():
    assert Controller_EventManager.__init__(Controller_EventManager('', False, controller26=set(), event_union_28=set()), '', True, controller26=set(), event_union_28=set()) == None


from python_code import AbstractBehavior
from python_code import AbstractProperty
from python_code import Entity

def test_Entity___init__():
    assert Entity.__init__(Entity(AbstractProperty(), AbstractBehavior(), abstractProperty34=set(), abstractBehavior36=set()), AbstractProperty(), AbstractBehavior(), abstractProperty34=set(), abstractBehavior36=set()) == None


from python_code import Model_Chunk
from python_code import Model_Tile

def test_Model_Tile___init__():
    assert Model_Tile.__init__(Model_Tile(0, 0, 0, '', chunk3=Model_Chunk()), 0, 0, 0, '', chunk3=Model_Chunk()) == None


from python_code import Table2

def test_Table2___init__():
    assert Table2.__init__(Table2(''), '') == None


from python_code import Table3

def test_Table3___init__():
    assert Table3.__init__(Table3(''), '') == None


from python_code import Model_World
from python_code import View_Renderer_Interface
from python_code import View_SDLCamera
from python_code import View_SDLRenderer
from python_code import View_SDLTexture
from python_code import View_View

def test_View_SDLRenderer___init__():
    assert View_SDLRenderer.__init__(View_SDLRenderer(View_View(Model_World(), View_Renderer_Interface(), controller25=set(), world7=Model_World(), renderer10=View_Renderer_Interface(), camera19=View_SDLCamera()), View_SDLTexture(), View_SDLCamera(), '', '', sDLCamera20=View_SDLCamera(), renderer15=View_Renderer_Interface(), sDLTexture16=set()), View_View(Model_World(), View_Renderer_Interface(), controller25=set(), world7=Model_World(), renderer10=View_Renderer_Interface(), camera19=View_SDLCamera()), View_SDLTexture(), View_SDLCamera(), '', '', sDLCamera20=View_SDLCamera(), renderer15=View_Renderer_Interface(), sDLTexture16=set()) == None


from python_code import Model_World
from python_code import View_Renderer_Interface
from python_code import View_SDLCamera
from python_code import View_View

def test_View_View___init__():
    assert View_View.__init__(View_View(Model_World(), View_Renderer_Interface(), controller25=set(), world7=Model_World(), renderer10=View_Renderer_Interface(), camera19=View_SDLCamera()), Model_World(), View_Renderer_Interface(), controller25=set(), world7=Model_World(), renderer10=View_Renderer_Interface(), camera19=View_SDLCamera()) == None


from python_code import trans_Table

def test_trans_Table___init__():
    assert trans_Table.__init__(trans_Table('', '\x00'), '\x00\x00', '') == None

