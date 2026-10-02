from python_code import problog_Atom

def test_problog_Atom___init__():
    assert problog_Atom.__init__(problog_Atom(''), '') == None

from python_code import problog_Cheat

def test_problog_Cheat___init__():
    assert problog_Cheat.__init__(problog_Cheat(''), '') == None

from python_code import problog_Comment

def test_problog_Comment___init__():
    assert problog_Comment.__init__(problog_Comment(''), '') == None

from python_code import problog_Evidence

def test_problog_Evidence___init__():
    assert problog_Evidence.__init__(problog_Evidence(''), '') == None

from python_code import problog_ImportLibrary

def test_problog_ImportLibrary___init__():
    assert problog_ImportLibrary.__init__(problog_ImportLibrary(''), '') == None

from python_code import problog_ProbabilityFraction

def test_problog_ProbabilityFraction___init__():
    assert problog_ProbabilityFraction.__init__(problog_ProbabilityFraction(0, 0), 0, 0) == None

from python_code import problog_ProbabilityLiteral

def test_problog_ProbabilityLiteral___init__():
    assert problog_ProbabilityLiteral.__init__(problog_ProbabilityLiteral(0.0), 0.0) == None

from python_code import problog_ProbLogProgram
from python_code import problog_Term
from python_code import problog_TermInstance

def test_problog_Term___init__():
    assert problog_Term.__init__(problog_Term('', 0, problog_Term=problog_ProbLogProgram(), problog_Term16=problog_TermInstance()), '', 0, problog_Term=problog_ProbLogProgram(), problog_Term16=problog_TermInstance()) == None

from python_code import problog_Variable

def test_problog_Variable___init__():
    assert problog_Variable.__init__(problog_Variable(''), '') == None
