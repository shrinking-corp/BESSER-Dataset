from python_code import automaton_Parameter
from python_code import automaton_TypedTransition

def test_automaton_Parameter___init__():
    assert automaton_Parameter.__init__(automaton_Parameter('', 0, Parameter=automaton_TypedTransition(), parameters=automaton_TypedTransition()), '', 0, Parameter=automaton_TypedTransition(), parameters=automaton_TypedTransition()) == None


from python_code import automaton_ParameterBinding
from python_code import automaton_ParameterTable

def test_automaton_ParameterBinding___init__():
    assert automaton_ParameterBinding.__init__(automaton_ParameterBinding('', '\x00', ParameterBinding=automaton_ParameterTable(), parameterBindings=automaton_ParameterTable()), '\x00\x00', '', ParameterBinding=automaton_ParameterTable(), parameterBindings=automaton_ParameterTable()) == None

