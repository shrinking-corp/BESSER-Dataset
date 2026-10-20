from python_code import petrinet_TracedPlace
from python_code import trace_States_Place_tokens_State

def test_trace_States_Place_tokens_State___init__():
    assert trace_States_Place_tokens_State.__init__(trace_States_Place_tokens_State(0, place_tokens_States=set(), tokensTrace=petrinet_TracedPlace()), 0, place_tokens_States=set(), tokensTrace=petrinet_TracedPlace()) == None


from python_code import petrinet_trace_Place
from python_code import trace_petrinet_TracedPlace

def test_trace_petrinet_TracedPlace___init__():
    assert trace_petrinet_TracedPlace.__init__(trace_petrinet_TracedPlace(0, '\x00', trace_petrinet_TracedPlace=petrinet_trace_Place(), parent=set()), 0, '', trace_petrinet_TracedPlace=petrinet_trace_Place(), parent=set()) == None

