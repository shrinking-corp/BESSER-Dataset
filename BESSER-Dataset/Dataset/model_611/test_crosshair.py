from python_code import appBuilderDSL_AbstractElement
from python_code import appBuilderDSL_AppBuilder

def test_appBuilderDSL_AbstractElement___init__():
    assert appBuilderDSL_AbstractElement.__init__(appBuilderDSL_AbstractElement('', appBuilderDSL_AbstractElement=appBuilderDSL_AppBuilder()), '', appBuilderDSL_AbstractElement=appBuilderDSL_AppBuilder()) == None


from python_code import appBuilderDSL_Button
from python_code import appBuilderDSL_Value

def test_appBuilderDSL_Button___init__():
    assert appBuilderDSL_Button.__init__(appBuilderDSL_Button('', appBuilderDSL_Button=appBuilderDSL_Value(), appBuilderDSL_Button99=appBuilderDSL_Value()), '', appBuilderDSL_Button=appBuilderDSL_Value(), appBuilderDSL_Button99=appBuilderDSL_Value()) == None


from python_code import appBuilderDSL_Control
from python_code import appBuilderDSL_ControlValue

def test_appBuilderDSL_ControlValue___init__():
    assert appBuilderDSL_ControlValue.__init__(appBuilderDSL_ControlValue('', appBuilderDSL_ControlValue=appBuilderDSL_Control()), '', appBuilderDSL_ControlValue=appBuilderDSL_Control()) == None


from python_code import appBuilderDSL_Control
from python_code import appBuilderDSL_DataBinding
from python_code import appBuilderDSL_InitAction

def test_appBuilderDSL_DataBinding___init__():
    assert appBuilderDSL_DataBinding.__init__(appBuilderDSL_DataBinding('', appBuilderDSL_DataBinding=appBuilderDSL_InitAction(), appBuilderDSL_DataBinding50=appBuilderDSL_Control()), '', appBuilderDSL_DataBinding=appBuilderDSL_InitAction(), appBuilderDSL_DataBinding50=appBuilderDSL_Control()) == None


from python_code import appBuilderDSL_EnumDataBinding

def test_appBuilderDSL_EnumDataBinding___init__():
    assert appBuilderDSL_EnumDataBinding.__init__(appBuilderDSL_EnumDataBinding(''), '') == None


from python_code import appBuilderDSL_GridLayout

def test_appBuilderDSL_GridLayout___init__():
    assert appBuilderDSL_GridLayout.__init__(appBuilderDSL_GridLayout(0), 0) == None


from python_code import appBuilderDSL_Import

def test_appBuilderDSL_Import___init__():
    assert appBuilderDSL_Import.__init__(appBuilderDSL_Import(''), '') == None


from python_code import appBuilderDSL_InstanceService

def test_appBuilderDSL_InstanceService___init__():
    assert appBuilderDSL_InstanceService.__init__(appBuilderDSL_InstanceService(''), '') == None


from python_code import appBuilderDSL_Label
from python_code import appBuilderDSL_Value

def test_appBuilderDSL_Label___init__():
    assert appBuilderDSL_Label.__init__(appBuilderDSL_Label('', appBuilderDSL_Label=appBuilderDSL_Value()), '', appBuilderDSL_Label=appBuilderDSL_Value()) == None


from python_code import appBuilderDSL_CompositeScreen
from python_code import appBuilderDSL_Layout
from python_code import appBuilderDSL_View

def test_appBuilderDSL_Layout___init__():
    assert appBuilderDSL_Layout.__init__(appBuilderDSL_Layout('', appBuilderDSL_Layout=appBuilderDSL_View(), appBuilderDSL_Layout79=set(), appBuilderDSL_Layout104=appBuilderDSL_CompositeScreen()), '', appBuilderDSL_Layout=appBuilderDSL_View(), appBuilderDSL_Layout79=set(), appBuilderDSL_Layout104=appBuilderDSL_CompositeScreen()) == None


from python_code import appBuilderDSL_List
from python_code import appBuilderDSL_Value

def test_appBuilderDSL_List___init__():
    assert appBuilderDSL_List.__init__(appBuilderDSL_List('', appBuilderDSL_List=appBuilderDSL_Value(), appBuilderDSL_List85=appBuilderDSL_Value(), appBuilderDSL_List88=appBuilderDSL_Value()), '', appBuilderDSL_List=appBuilderDSL_Value(), appBuilderDSL_List85=appBuilderDSL_Value(), appBuilderDSL_List88=appBuilderDSL_Value()) == None


from python_code import appBuilderDSL_RestCall

def test_appBuilderDSL_RestCall___init__():
    assert appBuilderDSL_RestCall.__init__(appBuilderDSL_RestCall(''), '') == None


from python_code import appBuilderDSL_SimpleConditionExpression

def test_appBuilderDSL_SimpleConditionExpression___init__():
    assert appBuilderDSL_SimpleConditionExpression.__init__(appBuilderDSL_SimpleConditionExpression(''), '') == None


from python_code import appBuilderDSL_Text
from python_code import appBuilderDSL_Value

def test_appBuilderDSL_Text___init__():
    assert appBuilderDSL_Text.__init__(appBuilderDSL_Text('', appBuilderDSL_Text=appBuilderDSL_Value(), appBuilderDSL_Text94=appBuilderDSL_Value()), '', appBuilderDSL_Text=appBuilderDSL_Value(), appBuilderDSL_Text94=appBuilderDSL_Value()) == None


from python_code import appBuilderDSL_UiAction

def test_appBuilderDSL_UiAction___init__():
    assert appBuilderDSL_UiAction.__init__(appBuilderDSL_UiAction('', appBuilderDSL_UiAction=set()), '', appBuilderDSL_UiAction=set()) == None


from python_code import appBuilderDSL_Action
from python_code import appBuilderDSL_Control
from python_code import appBuilderDSL_InitAction
from python_code import appBuilderDSL_UiListenerBinding

def test_appBuilderDSL_UiListenerBinding___init__():
    assert appBuilderDSL_UiListenerBinding.__init__(appBuilderDSL_UiListenerBinding('', appBuilderDSL_UiListenerBinding=appBuilderDSL_InitAction(), appBuilderDSL_UiListenerBinding44=appBuilderDSL_Action(), appBuilderDSL_UiListenerBinding47=appBuilderDSL_Control()), '', appBuilderDSL_UiListenerBinding=appBuilderDSL_InitAction(), appBuilderDSL_UiListenerBinding44=appBuilderDSL_Action(), appBuilderDSL_UiListenerBinding47=appBuilderDSL_Control()) == None

