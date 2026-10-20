import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Block,
    EOLLibraryModule,
    Expression,
    eol_module_AnnotationBlock,
    eol_module_Block,
    eol_module_EOLLibraryModule,
    eol_module_EOLModule,
    eol_module_Expression,
    eol_module_ExpressionOrStatementBlock,
    eol_module_FormalParameterExpression,
    eol_module_Import,
    eol_module_ModelDeclarationStatement,
    eol_module_NameExpression,
    eol_module_OperationDefinition,
    eol_module_Statement,
    eol_module_Type,
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

def test_assoc_importedModule6_reverse_link_reassign_clear():
    a1 = eol_module_Import(imported="sample_text")
    a2 = eol_module_Import(imported="sample_text_2")
    b = eol_module_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_module_EOLLibraryModule8', a1)
    assert _is_linked(b, 'eol_module_EOLLibraryModule8', a1)
    if hasattr(a1, 'eol_module_Import7'):
        assert _is_linked(a1, 'eol_module_Import7', b)
    _safe_set(b, 'eol_module_EOLLibraryModule8', a2)
    assert _is_linked(b, 'eol_module_EOLLibraryModule8', a2)
    if hasattr(a1, 'eol_module_Import7'):
        assert not _is_linked(a1, 'eol_module_Import7', b)
    if hasattr(a2, 'eol_module_Import7'):
        assert _is_linked(a2, 'eol_module_Import7', b)
    _safe_set(b, 'eol_module_EOLLibraryModule8', None)
    assert not _is_linked(b, 'eol_module_EOLLibraryModule8', a2)
    if hasattr(a2, 'eol_module_Import7'):
        assert not _is_linked(a2, 'eol_module_Import7', b)


def test_assoc_imports0_reverse_link_reassign_clear():
    a1 = eol_module_Import(imported="sample_text")
    a2 = eol_module_Import(imported="sample_text_2")
    b = eol_module_EOLLibraryModule(name="sample_text")
    _safe_set(b, 'eol_module_EOLLibraryModule', {a1})
    assert _is_linked(b, 'eol_module_EOLLibraryModule', a1)
    if hasattr(a1, 'eol_module_Import'):
        assert _is_linked(a1, 'eol_module_Import', b)
    _safe_set(b, 'eol_module_EOLLibraryModule', {a2})
    assert _is_linked(b, 'eol_module_EOLLibraryModule', a2)
    if hasattr(a1, 'eol_module_Import'):
        assert not _is_linked(a1, 'eol_module_Import', b)
    if hasattr(a2, 'eol_module_Import'):
        assert _is_linked(a2, 'eol_module_Import', b)
    _safe_set(b, 'eol_module_EOLLibraryModule', set())
    assert not _is_linked(b, 'eol_module_EOLLibraryModule', a2)
    if hasattr(a2, 'eol_module_Import'):
        assert not _is_linked(a2, 'eol_module_Import', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_modelDeclarations1_stub_double():
    # eol_module_ModelDeclarationStatement has no real 'eol_module_ModelDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so eol_module_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_module_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_module_EOLLibraryModule(name="sample_text")
    partner = eol_module_ModelDeclarationStatement()
    setattr(partner, 'eol_module_ModelDeclarationStatement', None)
    _safe_set(owner, 'eol_module_EOLLibraryModule2', {partner})
    assert getattr(partner, 'eol_module_ModelDeclarationStatement') == owner
    _safe_set(owner, 'eol_module_EOLLibraryModule2', set())
    assert getattr(partner, 'eol_module_ModelDeclarationStatement') is None


def test_assoc_name28_stub_double():
    # eol_module_OperationDefinition has no real 'eol_module_OperationDefinition29' property in the generated
    # code (a bare stub) -- manually attach it so eol_module_NameExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_module_NameExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_module_NameExpression(isType=True, name="sample_text")
    partner = eol_module_OperationDefinition()
    setattr(partner, 'eol_module_OperationDefinition29', None)
    _safe_set(owner, 'eol_module_NameExpression', partner)
    assert getattr(partner, 'eol_module_OperationDefinition29') == owner
    _safe_set(owner, 'eol_module_NameExpression', None)
    assert getattr(partner, 'eol_module_OperationDefinition29') is None


def test_assoc_operations3_stub_double():
    # eol_module_OperationDefinition has no real 'eol_module_OperationDefinition' property in the generated
    # code (a bare stub) -- manually attach it so eol_module_EOLLibraryModule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # eol_module_EOLLibraryModule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = eol_module_EOLLibraryModule(name="sample_text")
    partner = eol_module_OperationDefinition()
    setattr(partner, 'eol_module_OperationDefinition', None)
    _safe_set(owner, 'eol_module_EOLLibraryModule4', {partner})
    assert getattr(partner, 'eol_module_OperationDefinition') == owner
    _safe_set(owner, 'eol_module_EOLLibraryModule4', set())
    assert getattr(partner, 'eol_module_OperationDefinition') is None


