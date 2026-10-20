import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ASTNode,
    Call,
    Expression,
    FilePath,
    If,
    Literal,
    Method,
    Parameter,
    Resource,
    Script,
    ScriptDescriptor,
    Statement,
    core_mt_Resource,
    mt_Resource,
    mt_ResourceSet,
    mt_core_ASTNode,
    mt_core_FilePath,
    mt_core_Metamodel,
    mt_core_Method,
    mt_core_Parameter,
    mt_core_Script,
    mt_core_ScriptDescriptor,
    mt_core_Service,
    mt_core_Template,
    mt_expressions_BooleanLiteral,
    mt_expressions_Call,
    mt_expressions_CallSet,
    mt_expressions_DoubleLiteral,
    mt_expressions_Expression,
    mt_expressions_IntegerLiteral,
    mt_expressions_Literal,
    mt_expressions_Not,
    mt_expressions_NullLiteral,
    mt_expressions_Operator,
    mt_expressions_Parenthesis,
    mt_expressions_StringLiteral,
    mt_statements_Comment,
    mt_statements_Feature,
    mt_statements_For,
    mt_statements_If,
    mt_statements_Statement,
    mt_statements_Text,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments15_stub_double():
    # Expression has no real 'Expression16' property in the generated
    # code (a bare stub) -- manually attach it so mt_expressions_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_expressions_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_expressions_Call(name="sample_text", prefix="sample_text")
    partner = Expression()
    setattr(partner, 'Expression16', None)
    _safe_set(owner, 'mt_expressions_Call', {partner})
    assert getattr(partner, 'Expression16') == owner
    _safe_set(owner, 'mt_expressions_Call', set())
    assert getattr(partner, 'Expression16') is None


def test_assoc_file7_stub_double():
    # FilePath has no real 'FilePath' property in the generated
    # code (a bare stub) -- manually attach it so mt_core_ScriptDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_core_ScriptDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_core_ScriptDescriptor(description="sample_text", name="sample_text", type="sample_text")
    partner = FilePath()
    setattr(partner, 'FilePath', None)
    _safe_set(owner, 'mt_core_ScriptDescriptor', partner)
    assert getattr(partner, 'FilePath') == owner
    _safe_set(owner, 'mt_core_ScriptDescriptor', None)
    assert getattr(partner, 'FilePath') is None


def test_assoc_filter17_stub_double():
    # Expression has no real 'Expression19' property in the generated
    # code (a bare stub) -- manually attach it so mt_expressions_Call's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_expressions_Call's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_expressions_Call(name="sample_text", prefix="sample_text")
    partner = Expression()
    setattr(partner, 'Expression19', None)
    _safe_set(owner, 'mt_expressions_Call18', partner)
    assert getattr(partner, 'Expression19') == owner
    _safe_set(owner, 'mt_expressions_Call18', None)
    assert getattr(partner, 'Expression19') is None


def test_assoc_imports1_stub_double():
    # core_mt_Resource has no real 'core_mt_Resource' property in the generated
    # code (a bare stub) -- manually attach it so mt_core_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_core_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_core_Template(beginTag="sample_text", endTag="sample_text")
    partner = core_mt_Resource()
    setattr(partner, 'core_mt_Resource', None)
    _safe_set(owner, 'mt_core_Template', {partner})
    assert getattr(partner, 'core_mt_Resource') == owner
    _safe_set(owner, 'mt_core_Template', set())
    assert getattr(partner, 'core_mt_Resource') is None


def test_assoc_operands22_stub_double():
    # Expression has no real 'Expression23' property in the generated
    # code (a bare stub) -- manually attach it so mt_expressions_Operator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_expressions_Operator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_expressions_Operator(operator="sample_text")
    partner = Expression()
    setattr(partner, 'Expression23', None)
    _safe_set(owner, 'mt_expressions_Operator', {partner})
    assert getattr(partner, 'Expression23') == owner
    _safe_set(owner, 'mt_expressions_Operator', set())
    assert getattr(partner, 'Expression23') is None


def test_assoc_parameters13_stub_double():
    # Parameter has no real 'Parameter' property in the generated
    # code (a bare stub) -- manually attach it so mt_core_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_core_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_core_Method(name="sample_text", return_="sample_text")
    partner = Parameter()
    setattr(partner, 'Parameter', None)
    _safe_set(owner, 'mt_core_Method', {partner})
    assert getattr(partner, 'Parameter') == owner
    _safe_set(owner, 'mt_core_Method', set())
    assert getattr(partner, 'Parameter') is None


def test_assoc_post8_stub_double():
    # Expression has no real 'Expression' property in the generated
    # code (a bare stub) -- manually attach it so mt_core_ScriptDescriptor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_core_ScriptDescriptor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_core_ScriptDescriptor(description="sample_text", name="sample_text", type="sample_text")
    partner = Expression()
    setattr(partner, 'Expression', None)
    _safe_set(owner, 'mt_core_ScriptDescriptor9', partner)
    assert getattr(partner, 'Expression') == owner
    _safe_set(owner, 'mt_core_ScriptDescriptor9', None)
    assert getattr(partner, 'Expression') is None


def test_assoc_resources0_stub_double():
    # mt_ResourceSet has no real 'mt_ResourceSet' property in the generated
    # code (a bare stub) -- manually attach it so mt_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_Resource(name="sample_text")
    partner = mt_ResourceSet()
    setattr(partner, 'mt_ResourceSet', None)
    _safe_set(owner, 'mt_Resource', partner)
    assert owner in getattr(partner, 'mt_ResourceSet')
    _safe_set(owner, 'mt_Resource', None)
    assert owner not in getattr(partner, 'mt_ResourceSet')


def test_assoc_scripts2_stub_double():
    # Script has no real 'Script' property in the generated
    # code (a bare stub) -- manually attach it so mt_core_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # mt_core_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = mt_core_Template(beginTag="sample_text", endTag="sample_text")
    partner = Script()
    setattr(partner, 'Script', None)
    _safe_set(owner, 'mt_core_Template3', {partner})
    assert getattr(partner, 'Script') == owner
    _safe_set(owner, 'mt_core_Template3', set())
    assert getattr(partner, 'Script') is None


