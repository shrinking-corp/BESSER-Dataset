from python_code import conversation_Event
from python_code import conversation_Projection

def test_conversation_Event___init__():
    assert conversation_Event.__init__(conversation_Event('', conversation_Event=conversation_Projection()), '', conversation_Event=conversation_Projection()) == None


from python_code import conversation_Import

def test_conversation_Import___init__():
    assert conversation_Import.__init__(conversation_Import(''), '') == None

