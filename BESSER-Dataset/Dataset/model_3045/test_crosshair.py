from python_code import df_EObject
from python_code import df_Instance

def test_df_Instance___init__():
    assert df_Instance.__init__(df_Instance('', df_Instance6=df_EObject(), df_Instance=set()), '', df_Instance6=df_EObject(), df_Instance=set()) == None


from python_code import df_Action
from python_code import df_Tag

def test_df_Tag___init__():
    assert df_Tag.__init__(df_Tag('', df_Tag=df_Action()), '', df_Tag=df_Action()) == None


from python_code import df_Unit

def test_df_Unit___init__():
    assert df_Unit.__init__(df_Unit('', 0, '', df_Unit=set(), df_Unit2=set()), '', 0, '', df_Unit=set(), df_Unit2=set()) == None

