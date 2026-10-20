from python_code import model2_TracedA
from python_code import trace_States_A_a_State

def test_trace_States_A_a_State___init__():
    assert trace_States_A_a_State.__init__(trace_States_A_a_State(0, aTrace=model2_TracedA(), a_a_States=set()), 0, aTrace=model2_TracedA(), a_a_States=set()) == None


from python_code import model2Configuration_TracedB
from python_code import trace_States_B_b_State

def test_trace_States_B_b_State___init__():
    assert trace_States_B_b_State.__init__(trace_States_B_b_State(0, bTrace=model2Configuration_TracedB(), b_b_States=set()), 0, bTrace=model2Configuration_TracedB(), b_b_States=set()) == None

