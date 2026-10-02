from enum import Enum
from python_code import PseudostateKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(PseudostateKind.initial, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(PseudostateKind.initial, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(PseudostateKind.initial, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(PseudostateKind.initial, 0)

def test_Enum___new___2():
    assert Enum.__new__(PseudostateKind.initial, 'initial') == PseudostateKind.initial

from python_code import fsmcore_Constraint
from python_code import fsmcore_Transition

def test_fsmcore_Constraint___init__():
    assert fsmcore_Constraint.__init__(fsmcore_Constraint(fsmcore_Constraint=fsmcore_Transition()), fsmcore_Constraint=fsmcore_Transition()) == None

def test_fsmcore_Constraint_evalConstraint():
    assert fsmcore_Constraint.evalConstraint(fsmcore_Constraint(fsmcore_Constraint=fsmcore_Transition()), '') == None

from python_code import fsmcore_NamedElement

def test_fsmcore_NamedElement___init__():
    assert fsmcore_NamedElement.__init__(fsmcore_NamedElement(''), '') == None

from python_code import fsmcore_Program
from python_code import fsmcore_State

def test_fsmcore_Program___init__():
    assert fsmcore_Program.__init__(fsmcore_Program(fsmcore_Program=fsmcore_State(), fsmcore_Program11=fsmcore_State(), fsmcore_Program14=fsmcore_State(), fsmcore_Program24=set()), fsmcore_Program=fsmcore_State(), fsmcore_Program11=fsmcore_State(), fsmcore_Program14=fsmcore_State(), fsmcore_Program24=set()) == None

def test_fsmcore_Program_eval():
    assert fsmcore_Program.eval(fsmcore_Program(fsmcore_Program=fsmcore_State(), fsmcore_Program11=fsmcore_State(), fsmcore_Program14=fsmcore_State(), fsmcore_Program24=set()), 0) == None

from python_code import fsmcore_Pseudostate

def test_fsmcore_Pseudostate___init__():
    assert fsmcore_Pseudostate.__init__(fsmcore_Pseudostate(''), '') == None

from python_code import fsmcore_Transition
from python_code import fsmcore_Trigger

def test_fsmcore_Trigger___init__():
    assert fsmcore_Trigger.__init__(fsmcore_Trigger(True, fsmcore_Trigger=fsmcore_Transition()), False, fsmcore_Trigger=fsmcore_Transition()) == None
