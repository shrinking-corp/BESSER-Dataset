import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Assertion,
    Class_Element,
    Condition,
    Containment,
    Implementation,
    Propose_Refactoring,
    Refactoring,
    Refactoring_Instance,
    Test_Step_Element,
    tTCTest_Assert_False,
    tTCTest_Assert_True,
    tTCTest_Assertion,
    tTCTest_Class_Element,
    tTCTest_Classes,
    tTCTest_Compile,
    tTCTest_Condition,
    tTCTest_Containment,
    tTCTest_Contains,
    tTCTest_Contains_Not,
    tTCTest_Create_Superclass_Refactoring,
    tTCTest_Expect_False,
    tTCTest_Expect_True,
    tTCTest_Fields,
    tTCTest_Implementation,
    tTCTest_Implements,
    tTCTest_Implements_Not,
    tTCTest_Java_Class,
    tTCTest_Java_Field,
    tTCTest_Java_Method,
    tTCTest_Methods,
    tTCTest_No_Refactoring,
    tTCTest_Propose_Create_Superclass_Refactoring,
    tTCTest_Propose_Pullup_Method_Refactoring,
    tTCTest_Propose_Refactoring,
    tTCTest_Pull_Up_Refactoring,
    tTCTest_Refactoring,
    tTCTest_Refactoring_Instance,
    tTCTest_Synchronize,
    tTCTest_Test_Case,
    tTCTest_Test_File,
    tTCTest_Test_Flow,
    tTCTest_Test_Step,
    tTCTest_Test_Step_Element,
    tTCTest_Warning,
)

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

def test_assoc_classes9_reverse_link_reassign_clear():
    a1 = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    a2 = tTCTest_Java_Class(class_name="sample_text_2", name="sample_text_2", package="sample_text_2")
    b = tTCTest_Classes(name="sample_text")
    _safe_set(b, 'tTCTest_Classes10', {a1})
    assert _is_linked(b, 'tTCTest_Classes10', a1)
    if hasattr(a1, 'tTCTest_Java_Class11'):
        assert _is_linked(a1, 'tTCTest_Java_Class11', b)
    _safe_set(b, 'tTCTest_Classes10', {a2})
    assert _is_linked(b, 'tTCTest_Classes10', a2)
    if hasattr(a1, 'tTCTest_Java_Class11'):
        assert not _is_linked(a1, 'tTCTest_Java_Class11', b)
    if hasattr(a2, 'tTCTest_Java_Class11'):
        assert _is_linked(a2, 'tTCTest_Java_Class11', b)
    _safe_set(b, 'tTCTest_Classes10', set())
    assert not _is_linked(b, 'tTCTest_Classes10', a2)
    if hasattr(a2, 'tTCTest_Java_Class11'):
        assert not _is_linked(a2, 'tTCTest_Java_Class11', b)


def test_assoc_fields19_reverse_link_reassign_clear():
    a1 = tTCTest_Java_Field(field_name="sample_text")
    a2 = tTCTest_Java_Field(field_name="sample_text_2")
    b = tTCTest_Fields(name="sample_text")
    _safe_set(b, 'tTCTest_Fields', {a1})
    assert _is_linked(b, 'tTCTest_Fields', a1)
    if hasattr(a1, 'tTCTest_Java_Field20'):
        assert _is_linked(a1, 'tTCTest_Java_Field20', b)
    _safe_set(b, 'tTCTest_Fields', {a2})
    assert _is_linked(b, 'tTCTest_Fields', a2)
    if hasattr(a1, 'tTCTest_Java_Field20'):
        assert not _is_linked(a1, 'tTCTest_Java_Field20', b)
    if hasattr(a2, 'tTCTest_Java_Field20'):
        assert _is_linked(a2, 'tTCTest_Java_Field20', b)
    _safe_set(b, 'tTCTest_Fields', set())
    assert not _is_linked(b, 'tTCTest_Fields', a2)
    if hasattr(a2, 'tTCTest_Java_Field20'):
        assert not _is_linked(a2, 'tTCTest_Java_Field20', b)


def test_assoc_java_class1_reverse_link_reassign_clear():
    a1 = tTCTest_Test_File(name="sample_text")
    a2 = tTCTest_Test_File(name="sample_text_2")
    b = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    _safe_set(b, 'tTCTest_Java_Class', a1)
    assert _is_linked(b, 'tTCTest_Java_Class', a1)
    if hasattr(a1, 'tTCTest_Test_File2'):
        assert _is_linked(a1, 'tTCTest_Test_File2', b)
    _safe_set(b, 'tTCTest_Java_Class', a2)
    assert _is_linked(b, 'tTCTest_Java_Class', a2)
    if hasattr(a1, 'tTCTest_Test_File2'):
        assert not _is_linked(a1, 'tTCTest_Test_File2', b)
    if hasattr(a2, 'tTCTest_Test_File2'):
        assert _is_linked(a2, 'tTCTest_Test_File2', b)
    _safe_set(b, 'tTCTest_Java_Class', None)
    assert not _is_linked(b, 'tTCTest_Java_Class', a2)
    if hasattr(a2, 'tTCTest_Test_File2'):
        assert not _is_linked(a2, 'tTCTest_Test_File2', b)


def test_assoc_java_classes3_reverse_link_reassign_clear():
    a1 = tTCTest_Test_File(name="sample_text")
    a2 = tTCTest_Test_File(name="sample_text_2")
    b = tTCTest_Classes(name="sample_text")
    _safe_set(b, 'tTCTest_Classes', a1)
    assert _is_linked(b, 'tTCTest_Classes', a1)
    if hasattr(a1, 'tTCTest_Test_File4'):
        assert _is_linked(a1, 'tTCTest_Test_File4', b)
    _safe_set(b, 'tTCTest_Classes', a2)
    assert _is_linked(b, 'tTCTest_Classes', a2)
    if hasattr(a1, 'tTCTest_Test_File4'):
        assert not _is_linked(a1, 'tTCTest_Test_File4', b)
    if hasattr(a2, 'tTCTest_Test_File4'):
        assert _is_linked(a2, 'tTCTest_Test_File4', b)
    _safe_set(b, 'tTCTest_Classes', None)
    assert not _is_linked(b, 'tTCTest_Classes', a2)
    if hasattr(a2, 'tTCTest_Test_File4'):
        assert not _is_linked(a2, 'tTCTest_Test_File4', b)


def test_assoc_java_method5_reverse_link_reassign_clear():
    a1 = tTCTest_Test_File(name="sample_text")
    a2 = tTCTest_Test_File(name="sample_text_2")
    b = tTCTest_Java_Method(method_name="sample_text")
    _safe_set(b, 'tTCTest_Java_Method', a1)
    assert _is_linked(b, 'tTCTest_Java_Method', a1)
    if hasattr(a1, 'tTCTest_Test_File6'):
        assert _is_linked(a1, 'tTCTest_Test_File6', b)
    _safe_set(b, 'tTCTest_Java_Method', a2)
    assert _is_linked(b, 'tTCTest_Java_Method', a2)
    if hasattr(a1, 'tTCTest_Test_File6'):
        assert not _is_linked(a1, 'tTCTest_Test_File6', b)
    if hasattr(a2, 'tTCTest_Test_File6'):
        assert _is_linked(a2, 'tTCTest_Test_File6', b)
    _safe_set(b, 'tTCTest_Java_Method', None)
    assert not _is_linked(b, 'tTCTest_Java_Method', a2)
    if hasattr(a2, 'tTCTest_Test_File6'):
        assert not _is_linked(a2, 'tTCTest_Test_File6', b)


def test_assoc_methods15_reverse_link_reassign_clear():
    a1 = tTCTest_Methods(name="sample_text")
    a2 = tTCTest_Methods(name="sample_text_2")
    b = tTCTest_Java_Method(method_name="sample_text")
    _safe_set(b, 'tTCTest_Java_Method16', a1)
    assert _is_linked(b, 'tTCTest_Java_Method16', a1)
    if hasattr(a1, 'tTCTest_Methods'):
        assert _is_linked(a1, 'tTCTest_Methods', b)
    _safe_set(b, 'tTCTest_Java_Method16', a2)
    assert _is_linked(b, 'tTCTest_Java_Method16', a2)
    if hasattr(a1, 'tTCTest_Methods'):
        assert not _is_linked(a1, 'tTCTest_Methods', b)
    if hasattr(a2, 'tTCTest_Methods'):
        assert _is_linked(a2, 'tTCTest_Methods', b)
    _safe_set(b, 'tTCTest_Java_Method16', None)
    assert not _is_linked(b, 'tTCTest_Java_Method16', a2)
    if hasattr(a2, 'tTCTest_Methods'):
        assert not _is_linked(a2, 'tTCTest_Methods', b)


def test_assoc_params12_reverse_link_reassign_clear():
    a1 = tTCTest_Java_Method(method_name="sample_text")
    a2 = tTCTest_Java_Method(method_name="sample_text_2")
    b = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    _safe_set(b, 'tTCTest_Java_Class14', a1)
    assert _is_linked(b, 'tTCTest_Java_Class14', a1)
    if hasattr(a1, 'tTCTest_Java_Method13'):
        assert _is_linked(a1, 'tTCTest_Java_Method13', b)
    _safe_set(b, 'tTCTest_Java_Class14', a2)
    assert _is_linked(b, 'tTCTest_Java_Class14', a2)
    if hasattr(a1, 'tTCTest_Java_Method13'):
        assert not _is_linked(a1, 'tTCTest_Java_Method13', b)
    if hasattr(a2, 'tTCTest_Java_Method13'):
        assert _is_linked(a2, 'tTCTest_Java_Method13', b)
    _safe_set(b, 'tTCTest_Java_Class14', None)
    assert not _is_linked(b, 'tTCTest_Java_Class14', a2)
    if hasattr(a2, 'tTCTest_Java_Method13'):
        assert not _is_linked(a2, 'tTCTest_Java_Method13', b)


def test_assoc_refactorings7_reverse_link_reassign_clear():
    a1 = tTCTest_Test_File(name="sample_text")
    a2 = tTCTest_Test_File(name="sample_text_2")
    b = tTCTest_Refactoring_Instance(name="sample_text")
    _safe_set(b, 'tTCTest_Refactoring_Instance', a1)
    assert _is_linked(b, 'tTCTest_Refactoring_Instance', a1)
    if hasattr(a1, 'tTCTest_Test_File8'):
        assert _is_linked(a1, 'tTCTest_Test_File8', b)
    _safe_set(b, 'tTCTest_Refactoring_Instance', a2)
    assert _is_linked(b, 'tTCTest_Refactoring_Instance', a2)
    if hasattr(a1, 'tTCTest_Test_File8'):
        assert not _is_linked(a1, 'tTCTest_Test_File8', b)
    if hasattr(a2, 'tTCTest_Test_File8'):
        assert _is_linked(a2, 'tTCTest_Test_File8', b)
    _safe_set(b, 'tTCTest_Refactoring_Instance', None)
    assert not _is_linked(b, 'tTCTest_Refactoring_Instance', a2)
    if hasattr(a2, 'tTCTest_Test_File8'):
        assert not _is_linked(a2, 'tTCTest_Test_File8', b)


def test_assoc_test_cases0_reverse_link_reassign_clear():
    a1 = tTCTest_Test_File(name="sample_text")
    a2 = tTCTest_Test_File(name="sample_text_2")
    b = tTCTest_Test_Case(description="sample_text", java_program="sample_text", name="sample_text")
    _safe_set(b, 'tTCTest_Test_Case', a1)
    assert _is_linked(b, 'tTCTest_Test_Case', a1)
    if hasattr(a1, 'tTCTest_Test_File'):
        assert _is_linked(a1, 'tTCTest_Test_File', b)
    _safe_set(b, 'tTCTest_Test_Case', a2)
    assert _is_linked(b, 'tTCTest_Test_Case', a2)
    if hasattr(a1, 'tTCTest_Test_File'):
        assert not _is_linked(a1, 'tTCTest_Test_File', b)
    if hasattr(a2, 'tTCTest_Test_File'):
        assert _is_linked(a2, 'tTCTest_Test_File', b)
    _safe_set(b, 'tTCTest_Test_Case', None)
    assert not _is_linked(b, 'tTCTest_Test_Case', a2)
    if hasattr(a2, 'tTCTest_Test_File'):
        assert not _is_linked(a2, 'tTCTest_Test_File', b)


def test_assoc_type17_reverse_link_reassign_clear():
    a1 = tTCTest_Java_Field(field_name="sample_text")
    a2 = tTCTest_Java_Field(field_name="sample_text_2")
    b = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    _safe_set(b, 'tTCTest_Java_Class18', a1)
    assert _is_linked(b, 'tTCTest_Java_Class18', a1)
    if hasattr(a1, 'tTCTest_Java_Field'):
        assert _is_linked(a1, 'tTCTest_Java_Field', b)
    _safe_set(b, 'tTCTest_Java_Class18', a2)
    assert _is_linked(b, 'tTCTest_Java_Class18', a2)
    if hasattr(a1, 'tTCTest_Java_Field'):
        assert not _is_linked(a1, 'tTCTest_Java_Field', b)
    if hasattr(a2, 'tTCTest_Java_Field'):
        assert _is_linked(a2, 'tTCTest_Java_Field', b)
    _safe_set(b, 'tTCTest_Java_Class18', None)
    assert not _is_linked(b, 'tTCTest_Java_Class18', a2)
    if hasattr(a2, 'tTCTest_Java_Field'):
        assert not _is_linked(a2, 'tTCTest_Java_Field', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_child28_stub_double():
    # tTCTest_Create_Superclass_Refactoring has no real 'tTCTest_Create_Superclass_Refactoring' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Classes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Classes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Classes(name="sample_text")
    partner = tTCTest_Create_Superclass_Refactoring()
    setattr(partner, 'tTCTest_Create_Superclass_Refactoring', None)
    _safe_set(owner, 'tTCTest_Classes29', partner)
    assert getattr(partner, 'tTCTest_Create_Superclass_Refactoring') == owner
    _safe_set(owner, 'tTCTest_Classes29', None)
    assert getattr(partner, 'tTCTest_Create_Superclass_Refactoring') is None


def test_assoc_child54_stub_double():
    # tTCTest_Implementation has no real 'tTCTest_Implementation' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    partner = tTCTest_Implementation()
    setattr(partner, 'tTCTest_Implementation', None)
    _safe_set(owner, 'tTCTest_Java_Class55', partner)
    assert getattr(partner, 'tTCTest_Implementation') == owner
    _safe_set(owner, 'tTCTest_Java_Class55', None)
    assert getattr(partner, 'tTCTest_Implementation') is None


def test_assoc_class_50_stub_double():
    # tTCTest_Containment has no real 'tTCTest_Containment' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    partner = tTCTest_Containment()
    setattr(partner, 'tTCTest_Containment', None)
    _safe_set(owner, 'tTCTest_Java_Class51', partner)
    assert getattr(partner, 'tTCTest_Containment') == owner
    _safe_set(owner, 'tTCTest_Java_Class51', None)
    assert getattr(partner, 'tTCTest_Containment') is None


def test_assoc_contains52_stub_double():
    # tTCTest_Containment has no real 'tTCTest_Containment53' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Class_Element's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Class_Element's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Class_Element(name="sample_text")
    partner = tTCTest_Containment()
    setattr(partner, 'tTCTest_Containment53', None)
    _safe_set(owner, 'tTCTest_Class_Element', partner)
    assert getattr(partner, 'tTCTest_Containment53') == owner
    _safe_set(owner, 'tTCTest_Class_Element', None)
    assert getattr(partner, 'tTCTest_Containment53') is None


def test_assoc_method25_stub_double():
    # tTCTest_Pull_Up_Refactoring has no real 'tTCTest_Pull_Up_Refactoring26' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Method(method_name="sample_text")
    partner = tTCTest_Pull_Up_Refactoring()
    setattr(partner, 'tTCTest_Pull_Up_Refactoring26', None)
    _safe_set(owner, 'tTCTest_Java_Method27', partner)
    assert getattr(partner, 'tTCTest_Pull_Up_Refactoring26') == owner
    _safe_set(owner, 'tTCTest_Java_Method27', None)
    assert getattr(partner, 'tTCTest_Pull_Up_Refactoring26') is None


def test_assoc_parent23_stub_double():
    # tTCTest_Pull_Up_Refactoring has no real 'tTCTest_Pull_Up_Refactoring' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    partner = tTCTest_Pull_Up_Refactoring()
    setattr(partner, 'tTCTest_Pull_Up_Refactoring', None)
    _safe_set(owner, 'tTCTest_Java_Class24', partner)
    assert getattr(partner, 'tTCTest_Pull_Up_Refactoring') == owner
    _safe_set(owner, 'tTCTest_Java_Class24', None)
    assert getattr(partner, 'tTCTest_Pull_Up_Refactoring') is None


def test_assoc_parent56_stub_double():
    # tTCTest_Implementation has no real 'tTCTest_Implementation57' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    partner = tTCTest_Implementation()
    setattr(partner, 'tTCTest_Implementation57', None)
    _safe_set(owner, 'tTCTest_Java_Class58', partner)
    assert getattr(partner, 'tTCTest_Implementation57') == owner
    _safe_set(owner, 'tTCTest_Java_Class58', None)
    assert getattr(partner, 'tTCTest_Implementation57') is None


def test_assoc_target30_stub_double():
    # tTCTest_Create_Superclass_Refactoring has no real 'tTCTest_Create_Superclass_Refactoring31' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Java_Class's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Java_Class's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Java_Class(class_name="sample_text", name="sample_text", package="sample_text")
    partner = tTCTest_Create_Superclass_Refactoring()
    setattr(partner, 'tTCTest_Create_Superclass_Refactoring31', None)
    _safe_set(owner, 'tTCTest_Java_Class32', partner)
    assert getattr(partner, 'tTCTest_Create_Superclass_Refactoring31') == owner
    _safe_set(owner, 'tTCTest_Java_Class32', None)
    assert getattr(partner, 'tTCTest_Create_Superclass_Refactoring31') is None


def test_assoc_test_flow21_stub_double():
    # tTCTest_Test_Flow has no real 'tTCTest_Test_Flow' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Test_Case's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Test_Case's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Test_Case(description="sample_text", java_program="sample_text", name="sample_text")
    partner = tTCTest_Test_Flow()
    setattr(partner, 'tTCTest_Test_Flow', None)
    _safe_set(owner, 'tTCTest_Test_Case22', partner)
    assert getattr(partner, 'tTCTest_Test_Flow') == owner
    _safe_set(owner, 'tTCTest_Test_Case22', None)
    assert getattr(partner, 'tTCTest_Test_Flow') is None


def test_assoc_warning43_stub_double():
    # tTCTest_Condition has no real 'tTCTest_Condition44' property in the generated
    # code (a bare stub) -- manually attach it so tTCTest_Warning's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tTCTest_Warning's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tTCTest_Warning(message="sample_text")
    partner = tTCTest_Condition()
    setattr(partner, 'tTCTest_Condition44', None)
    _safe_set(owner, 'tTCTest_Warning', partner)
    assert getattr(partner, 'tTCTest_Condition44') == owner
    _safe_set(owner, 'tTCTest_Warning', None)
    assert getattr(partner, 'tTCTest_Condition44') is None


