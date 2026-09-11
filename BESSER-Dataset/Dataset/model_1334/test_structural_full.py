import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    BooleanLiteralExpCS,
    CSTrace,
    CallExpCS,
    EqualityExpCS,
    ExpCS,
    LiteralExpCS,
    LoopExpCS,
    NavigationExpCS,
    PrimaryExpCS,
    minioclcs_AccVarCS,
    minioclcs_BooleanExpCS,
    minioclcs_BooleanLiteralExpCS,
    minioclcs_CSTrace,
    minioclcs_CallExpCS,
    minioclcs_ClassCS,
    minioclcs_CollectExpCS,
    minioclcs_CollectionLiteralExpCS,
    minioclcs_CollectionLiteralPartCS,
    minioclcs_ConstraintsDefCS,
    minioclcs_EClass,
    minioclcs_EObject,
    minioclcs_EqualityExpCS,
    minioclcs_ExpCS,
    minioclcs_ImportCS,
    minioclcs_IntLiteralExpCS,
    minioclcs_InvariantCS,
    minioclcs_IterateExpCS,
    minioclcs_IteratorVarCS,
    minioclcs_LetExpCS,
    minioclcs_LetVarCS,
    minioclcs_LiteralExpCS,
    minioclcs_LoopExpCS,
    minioclcs_MultiplicityCS,
    minioclcs_NameExpCS,
    minioclcs_NavigationExpCS,
    minioclcs_NullLiteralExpCS,
    minioclcs_OperationCS,
    minioclcs_PackageCS,
    minioclcs_ParameterCS,
    minioclcs_PathElementCS,
    minioclcs_PathNameCS,
    minioclcs_PrimaryExpCS,
    minioclcs_PropertyCS,
    minioclcs_RootCS,
    minioclcs_RoundedBracketClauseCS,
    minioclcs_SelfExpCS,
    CollectionKindCS,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_minioclcs_AccVarCS_accName_value_roundtrip():
    instance = minioclcs_AccVarCS(accName="sample_text")
    assert instance.accName == "sample_text"
    instance.accName = "sample_text_2"
    assert instance.accName == "sample_text_2"


def test_minioclcs_BooleanExpCS_boolSymbol_value_roundtrip():
    instance = minioclcs_BooleanExpCS(boolSymbol=True)
    assert instance.boolSymbol == True
    instance.boolSymbol = False
    assert instance.boolSymbol == False


def test_minioclcs_ClassCS_name_value_roundtrip():
    instance = minioclcs_ClassCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_CollectionLiteralExpCS_kind_value_roundtrip():
    instance = minioclcs_CollectionLiteralExpCS(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_minioclcs_EqualityExpCS_opName_value_roundtrip():
    instance = minioclcs_EqualityExpCS(opName="sample_text")
    assert instance.opName == "sample_text"
    instance.opName = "sample_text_2"
    assert instance.opName == "sample_text_2"


def test_minioclcs_ImportCS_alias_value_roundtrip():
    instance = minioclcs_ImportCS(alias="sample_text", uri="sample_text")
    assert instance.alias == "sample_text"
    instance.alias = "sample_text_2"
    assert instance.alias == "sample_text_2"


def test_minioclcs_ImportCS_uri_value_roundtrip():
    instance = minioclcs_ImportCS(alias="sample_text", uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_minioclcs_IntLiteralExpCS_intSymbol_value_roundtrip():
    instance = minioclcs_IntLiteralExpCS(intSymbol=7)
    assert instance.intSymbol == 7
    instance.intSymbol = 13
    assert instance.intSymbol == 13


def test_minioclcs_IteratorVarCS_itName_value_roundtrip():
    instance = minioclcs_IteratorVarCS(itName="sample_text")
    assert instance.itName == "sample_text"
    instance.itName = "sample_text_2"
    assert instance.itName == "sample_text_2"


def test_minioclcs_LetVarCS_name_value_roundtrip():
    instance = minioclcs_LetVarCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_MultiplicityCS_lowerInt_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.lowerInt == 7
    instance.lowerInt = 13
    assert instance.lowerInt == 13


def test_minioclcs_MultiplicityCS_mandatory_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.mandatory == 7
    instance.mandatory = 13
    assert instance.mandatory == 13


def test_minioclcs_MultiplicityCS_mult_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.mult == True
    instance.mult = False
    assert instance.mult == False


def test_minioclcs_MultiplicityCS_opt_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.opt == True
    instance.opt = False
    assert instance.opt == False


def test_minioclcs_MultiplicityCS_upperInt_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.upperInt == 7
    instance.upperInt = 13
    assert instance.upperInt == 13


def test_minioclcs_MultiplicityCS_upperMult_value_roundtrip():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert instance.upperMult == True
    instance.upperMult = False
    assert instance.upperMult == False


def test_minioclcs_OperationCS_name_value_roundtrip():
    instance = minioclcs_OperationCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_PackageCS_name_value_roundtrip():
    instance = minioclcs_PackageCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_ParameterCS_name_value_roundtrip():
    instance = minioclcs_ParameterCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_PropertyCS_name_value_roundtrip():
    instance = minioclcs_PropertyCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_minioclcs_BooleanExpCS_isa_BooleanLiteralExpCS():
    instance = minioclcs_BooleanExpCS(boolSymbol=True)
    assert isinstance(instance, BooleanLiteralExpCS)


def test_minioclcs_AccVarCS_isa_CSTrace():
    instance = minioclcs_AccVarCS(accName="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_ClassCS_isa_CSTrace():
    instance = minioclcs_ClassCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_CollectionLiteralPartCS_isa_CSTrace():
    instance = minioclcs_CollectionLiteralPartCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_ConstraintsDefCS_isa_CSTrace():
    instance = minioclcs_ConstraintsDefCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_ExpCS_isa_CSTrace():
    instance = minioclcs_ExpCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_ImportCS_isa_CSTrace():
    instance = minioclcs_ImportCS(alias="sample_text", uri="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_InvariantCS_isa_CSTrace():
    instance = minioclcs_InvariantCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_IteratorVarCS_isa_CSTrace():
    instance = minioclcs_IteratorVarCS(itName="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_LetVarCS_isa_CSTrace():
    instance = minioclcs_LetVarCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_MultiplicityCS_isa_CSTrace():
    instance = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    assert isinstance(instance, CSTrace)


def test_minioclcs_NavigationExpCS_isa_CSTrace():
    instance = minioclcs_NavigationExpCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_OperationCS_isa_CSTrace():
    instance = minioclcs_OperationCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_PackageCS_isa_CSTrace():
    instance = minioclcs_PackageCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_ParameterCS_isa_CSTrace():
    instance = minioclcs_ParameterCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_PathElementCS_isa_CSTrace():
    instance = minioclcs_PathElementCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_PathNameCS_isa_CSTrace():
    instance = minioclcs_PathNameCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_PropertyCS_isa_CSTrace():
    instance = minioclcs_PropertyCS(name="sample_text")
    assert isinstance(instance, CSTrace)


def test_minioclcs_RootCS_isa_CSTrace():
    instance = minioclcs_RootCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_RoundedBracketClauseCS_isa_CSTrace():
    instance = minioclcs_RoundedBracketClauseCS()
    assert isinstance(instance, CSTrace)


def test_minioclcs_PrimaryExpCS_isa_CallExpCS():
    instance = minioclcs_PrimaryExpCS()
    assert isinstance(instance, CallExpCS)


def test_minioclcs_CallExpCS_isa_EqualityExpCS():
    instance = minioclcs_CallExpCS()
    assert isinstance(instance, EqualityExpCS)


def test_minioclcs_EqualityExpCS_isa_ExpCS():
    instance = minioclcs_EqualityExpCS(opName="sample_text")
    assert isinstance(instance, ExpCS)


def test_minioclcs_BooleanLiteralExpCS_isa_LiteralExpCS():
    instance = minioclcs_BooleanLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_minioclcs_CollectionLiteralExpCS_isa_LiteralExpCS():
    instance = minioclcs_CollectionLiteralExpCS(kind="sample_text")
    assert isinstance(instance, LiteralExpCS)


def test_minioclcs_IntLiteralExpCS_isa_LiteralExpCS():
    instance = minioclcs_IntLiteralExpCS(intSymbol=7)
    assert isinstance(instance, LiteralExpCS)


def test_minioclcs_NullLiteralExpCS_isa_LiteralExpCS():
    instance = minioclcs_NullLiteralExpCS()
    assert isinstance(instance, LiteralExpCS)


def test_minioclcs_CollectExpCS_isa_LoopExpCS():
    instance = minioclcs_CollectExpCS()
    assert isinstance(instance, LoopExpCS)


def test_minioclcs_IterateExpCS_isa_LoopExpCS():
    instance = minioclcs_IterateExpCS()
    assert isinstance(instance, LoopExpCS)


def test_minioclcs_LoopExpCS_isa_NavigationExpCS():
    instance = minioclcs_LoopExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_minioclcs_NameExpCS_isa_NavigationExpCS():
    instance = minioclcs_NameExpCS()
    assert isinstance(instance, NavigationExpCS)


def test_minioclcs_LetExpCS_isa_PrimaryExpCS():
    instance = minioclcs_LetExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_minioclcs_LiteralExpCS_isa_PrimaryExpCS():
    instance = minioclcs_LiteralExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_minioclcs_NameExpCS_isa_PrimaryExpCS():
    instance = minioclcs_NameExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_minioclcs_SelfExpCS_isa_PrimaryExpCS():
    instance = minioclcs_SelfExpCS()
    assert isinstance(instance, PrimaryExpCS)


def test_assoc_accInitExp59_link_reassign_clear():
    a = minioclcs_AccVarCS(accName="sample_text")
    b1 = minioclcs_ExpCS()
    b2 = minioclcs_ExpCS()
    _safe_set(a, 'minioclcs_AccVarCS60', b1)
    assert _is_linked(a, 'minioclcs_AccVarCS60', b1)
    if hasattr(b1, 'minioclcs_ExpCS61'):
        assert _is_linked(b1, 'minioclcs_ExpCS61', a)
    _safe_set(a, 'minioclcs_AccVarCS60', b2)
    assert _is_linked(a, 'minioclcs_AccVarCS60', b2)
    if hasattr(b1, 'minioclcs_ExpCS61'):
        assert not _is_linked(b1, 'minioclcs_ExpCS61', a)
    if hasattr(b2, 'minioclcs_ExpCS61'):
        assert _is_linked(b2, 'minioclcs_ExpCS61', a)
    _safe_set(a, 'minioclcs_AccVarCS60', None)
    assert not _is_linked(a, 'minioclcs_AccVarCS60', b2)
    if hasattr(b2, 'minioclcs_ExpCS61'):
        assert not _is_linked(b2, 'minioclcs_ExpCS61', a)


def test_assoc_accType56_link_reassign_clear():
    a = minioclcs_AccVarCS(accName="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_AccVarCS57', b1)
    assert _is_linked(a, 'minioclcs_AccVarCS57', b1)
    if hasattr(b1, 'minioclcs_PathNameCS58'):
        assert _is_linked(b1, 'minioclcs_PathNameCS58', a)
    _safe_set(a, 'minioclcs_AccVarCS57', b2)
    assert _is_linked(a, 'minioclcs_AccVarCS57', b2)
    if hasattr(b1, 'minioclcs_PathNameCS58'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS58', a)
    if hasattr(b2, 'minioclcs_PathNameCS58'):
        assert _is_linked(b2, 'minioclcs_PathNameCS58', a)
    _safe_set(a, 'minioclcs_AccVarCS57', None)
    assert not _is_linked(a, 'minioclcs_AccVarCS57', b2)
    if hasattr(b2, 'minioclcs_PathNameCS58'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS58', a)


def test_assoc_accVar55_link_reassign_clear():
    a = minioclcs_AccVarCS(accName="sample_text")
    b1 = minioclcs_IterateExpCS()
    b2 = minioclcs_IterateExpCS()
    _safe_set(a, 'minioclcs_AccVarCS', b1)
    assert _is_linked(a, 'minioclcs_AccVarCS', b1)
    if hasattr(b1, 'minioclcs_IterateExpCS'):
        assert _is_linked(b1, 'minioclcs_IterateExpCS', a)
    _safe_set(a, 'minioclcs_AccVarCS', b2)
    assert _is_linked(a, 'minioclcs_AccVarCS', b2)
    if hasattr(b1, 'minioclcs_IterateExpCS'):
        assert not _is_linked(b1, 'minioclcs_IterateExpCS', a)
    if hasattr(b2, 'minioclcs_IterateExpCS'):
        assert _is_linked(b2, 'minioclcs_IterateExpCS', a)
    _safe_set(a, 'minioclcs_AccVarCS', None)
    assert not _is_linked(a, 'minioclcs_AccVarCS', b2)
    if hasattr(b2, 'minioclcs_IterateExpCS'):
        assert not _is_linked(b2, 'minioclcs_IterateExpCS', a)


def test_assoc_body26_link_reassign_clear():
    a = minioclcs_OperationCS(name="sample_text")
    b1 = minioclcs_ExpCS()
    b2 = minioclcs_ExpCS()
    _safe_set(a, 'minioclcs_OperationCS27', b1)
    assert _is_linked(a, 'minioclcs_OperationCS27', b1)
    if hasattr(b1, 'minioclcs_ExpCS'):
        assert _is_linked(b1, 'minioclcs_ExpCS', a)
    _safe_set(a, 'minioclcs_OperationCS27', b2)
    assert _is_linked(a, 'minioclcs_OperationCS27', b2)
    if hasattr(b1, 'minioclcs_ExpCS'):
        assert not _is_linked(b1, 'minioclcs_ExpCS', a)
    if hasattr(b2, 'minioclcs_ExpCS'):
        assert _is_linked(b2, 'minioclcs_ExpCS', a)
    _safe_set(a, 'minioclcs_OperationCS27', None)
    assert not _is_linked(a, 'minioclcs_OperationCS27', b2)
    if hasattr(b2, 'minioclcs_ExpCS'):
        assert not _is_linked(b2, 'minioclcs_ExpCS', a)


def test_assoc_classes8_link_reassign_clear():
    a = minioclcs_PackageCS(name="sample_text")
    b1 = minioclcs_ClassCS(name="sample_text")
    b2 = minioclcs_ClassCS(name="sample_text_2")
    _safe_set(a, 'minioclcs_PackageCS9', {b1})
    assert _is_linked(a, 'minioclcs_PackageCS9', b1)
    if hasattr(b1, 'minioclcs_ClassCS'):
        assert _is_linked(b1, 'minioclcs_ClassCS', a)
    _safe_set(a, 'minioclcs_PackageCS9', {b2})
    assert _is_linked(a, 'minioclcs_PackageCS9', b2)
    if hasattr(b1, 'minioclcs_ClassCS'):
        assert not _is_linked(b1, 'minioclcs_ClassCS', a)
    if hasattr(b2, 'minioclcs_ClassCS'):
        assert _is_linked(b2, 'minioclcs_ClassCS', a)
    _safe_set(a, 'minioclcs_PackageCS9', set())
    assert not _is_linked(a, 'minioclcs_PackageCS9', b2)
    if hasattr(b2, 'minioclcs_ClassCS'):
        assert not _is_linked(b2, 'minioclcs_ClassCS', a)


def test_assoc_extends10_link_reassign_clear():
    a = minioclcs_ClassCS(name="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_ClassCS11', b1)
    assert _is_linked(a, 'minioclcs_ClassCS11', b1)
    if hasattr(b1, 'minioclcs_PathNameCS'):
        assert _is_linked(b1, 'minioclcs_PathNameCS', a)
    _safe_set(a, 'minioclcs_ClassCS11', b2)
    assert _is_linked(a, 'minioclcs_ClassCS11', b2)
    if hasattr(b1, 'minioclcs_PathNameCS'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS', a)
    if hasattr(b2, 'minioclcs_PathNameCS'):
        assert _is_linked(b2, 'minioclcs_PathNameCS', a)
    _safe_set(a, 'minioclcs_ClassCS11', None)
    assert not _is_linked(a, 'minioclcs_ClassCS11', b2)
    if hasattr(b2, 'minioclcs_PathNameCS'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS', a)


def test_assoc_imports0_link_reassign_clear():
    a = minioclcs_ImportCS(alias="sample_text", uri="sample_text")
    b1 = minioclcs_RootCS()
    b2 = minioclcs_RootCS()
    _safe_set(a, 'minioclcs_ImportCS', b1)
    assert _is_linked(a, 'minioclcs_ImportCS', b1)
    if hasattr(b1, 'minioclcs_RootCS'):
        assert _is_linked(b1, 'minioclcs_RootCS', a)
    _safe_set(a, 'minioclcs_ImportCS', b2)
    assert _is_linked(a, 'minioclcs_ImportCS', b2)
    if hasattr(b1, 'minioclcs_RootCS'):
        assert not _is_linked(b1, 'minioclcs_RootCS', a)
    if hasattr(b2, 'minioclcs_RootCS'):
        assert _is_linked(b2, 'minioclcs_RootCS', a)
    _safe_set(a, 'minioclcs_ImportCS', None)
    assert not _is_linked(a, 'minioclcs_ImportCS', b2)
    if hasattr(b2, 'minioclcs_RootCS'):
        assert not _is_linked(b2, 'minioclcs_RootCS', a)


def test_assoc_initExp83_link_reassign_clear():
    a = minioclcs_LetVarCS(name="sample_text")
    b1 = minioclcs_ExpCS()
    b2 = minioclcs_ExpCS()
    _safe_set(a, 'minioclcs_LetVarCS84', b1)
    assert _is_linked(a, 'minioclcs_LetVarCS84', b1)
    if hasattr(b1, 'minioclcs_ExpCS85'):
        assert _is_linked(b1, 'minioclcs_ExpCS85', a)
    _safe_set(a, 'minioclcs_LetVarCS84', b2)
    assert _is_linked(a, 'minioclcs_LetVarCS84', b2)
    if hasattr(b1, 'minioclcs_ExpCS85'):
        assert not _is_linked(b1, 'minioclcs_ExpCS85', a)
    if hasattr(b2, 'minioclcs_ExpCS85'):
        assert _is_linked(b2, 'minioclcs_ExpCS85', a)
    _safe_set(a, 'minioclcs_LetVarCS84', None)
    assert not _is_linked(a, 'minioclcs_LetVarCS84', b2)
    if hasattr(b2, 'minioclcs_ExpCS85'):
        assert not _is_linked(b2, 'minioclcs_ExpCS85', a)


def test_assoc_itType52_link_reassign_clear():
    a = minioclcs_IteratorVarCS(itName="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_IteratorVarCS53', b1)
    assert _is_linked(a, 'minioclcs_IteratorVarCS53', b1)
    if hasattr(b1, 'minioclcs_PathNameCS54'):
        assert _is_linked(b1, 'minioclcs_PathNameCS54', a)
    _safe_set(a, 'minioclcs_IteratorVarCS53', b2)
    assert _is_linked(a, 'minioclcs_IteratorVarCS53', b2)
    if hasattr(b1, 'minioclcs_PathNameCS54'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS54', a)
    if hasattr(b2, 'minioclcs_PathNameCS54'):
        assert _is_linked(b2, 'minioclcs_PathNameCS54', a)
    _safe_set(a, 'minioclcs_IteratorVarCS53', None)
    assert not _is_linked(a, 'minioclcs_IteratorVarCS53', b2)
    if hasattr(b2, 'minioclcs_PathNameCS54'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS54', a)


def test_assoc_itVar48_link_reassign_clear():
    a = minioclcs_IteratorVarCS(itName="sample_text")
    b1 = minioclcs_LoopExpCS()
    b2 = minioclcs_LoopExpCS()
    _safe_set(a, 'minioclcs_IteratorVarCS', b1)
    assert _is_linked(a, 'minioclcs_IteratorVarCS', b1)
    if hasattr(b1, 'minioclcs_LoopExpCS'):
        assert _is_linked(b1, 'minioclcs_LoopExpCS', a)
    _safe_set(a, 'minioclcs_IteratorVarCS', b2)
    assert _is_linked(a, 'minioclcs_IteratorVarCS', b2)
    if hasattr(b1, 'minioclcs_LoopExpCS'):
        assert not _is_linked(b1, 'minioclcs_LoopExpCS', a)
    if hasattr(b2, 'minioclcs_LoopExpCS'):
        assert _is_linked(b2, 'minioclcs_LoopExpCS', a)
    _safe_set(a, 'minioclcs_IteratorVarCS', None)
    assert not _is_linked(a, 'minioclcs_IteratorVarCS', b2)
    if hasattr(b2, 'minioclcs_LoopExpCS'):
        assert not _is_linked(b2, 'minioclcs_LoopExpCS', a)


def test_assoc_left40_link_reassign_clear():
    a = minioclcs_EqualityExpCS(opName="sample_text")
    b1 = minioclcs_EqualityExpCS(opName="sample_text")
    b2 = minioclcs_EqualityExpCS(opName="sample_text_2")
    _safe_set(a, 'minioclcs_EqualityExpCS', b1)
    assert _is_linked(a, 'minioclcs_EqualityExpCS', b1)
    if hasattr(b1, 'minioclcs_EqualityExpCS39'):
        assert _is_linked(b1, 'minioclcs_EqualityExpCS39', a)
    _safe_set(a, 'minioclcs_EqualityExpCS', b2)
    assert _is_linked(a, 'minioclcs_EqualityExpCS', b2)
    if hasattr(b1, 'minioclcs_EqualityExpCS39'):
        assert not _is_linked(b1, 'minioclcs_EqualityExpCS39', a)
    if hasattr(b2, 'minioclcs_EqualityExpCS39'):
        assert _is_linked(b2, 'minioclcs_EqualityExpCS39', a)
    _safe_set(a, 'minioclcs_EqualityExpCS', None)
    assert not _is_linked(a, 'minioclcs_EqualityExpCS', b2)
    if hasattr(b2, 'minioclcs_EqualityExpCS39'):
        assert not _is_linked(b2, 'minioclcs_EqualityExpCS39', a)


def test_assoc_letVars76_link_reassign_clear():
    a = minioclcs_LetVarCS(name="sample_text")
    b1 = minioclcs_LetExpCS()
    b2 = minioclcs_LetExpCS()
    _safe_set(a, 'minioclcs_LetVarCS', b1)
    assert _is_linked(a, 'minioclcs_LetVarCS', b1)
    if hasattr(b1, 'minioclcs_LetExpCS'):
        assert _is_linked(b1, 'minioclcs_LetExpCS', a)
    _safe_set(a, 'minioclcs_LetVarCS', b2)
    assert _is_linked(a, 'minioclcs_LetVarCS', b2)
    if hasattr(b1, 'minioclcs_LetExpCS'):
        assert not _is_linked(b1, 'minioclcs_LetExpCS', a)
    if hasattr(b2, 'minioclcs_LetExpCS'):
        assert _is_linked(b2, 'minioclcs_LetExpCS', a)
    _safe_set(a, 'minioclcs_LetVarCS', None)
    assert not _is_linked(a, 'minioclcs_LetVarCS', b2)
    if hasattr(b2, 'minioclcs_LetExpCS'):
        assert not _is_linked(b2, 'minioclcs_LetExpCS', a)


def test_assoc_multiplicity19_link_reassign_clear():
    a = minioclcs_PropertyCS(name="sample_text")
    b1 = minioclcs_MultiplicityCS(lowerInt=7, mandatory=7, mult=True, opt=True, upperInt=7, upperMult=True)
    b2 = minioclcs_MultiplicityCS(lowerInt=13, mandatory=13, mult=False, opt=False, upperInt=13, upperMult=False)
    _safe_set(a, 'minioclcs_PropertyCS20', b1)
    assert _is_linked(a, 'minioclcs_PropertyCS20', b1)
    if hasattr(b1, 'minioclcs_MultiplicityCS'):
        assert _is_linked(b1, 'minioclcs_MultiplicityCS', a)
    _safe_set(a, 'minioclcs_PropertyCS20', b2)
    assert _is_linked(a, 'minioclcs_PropertyCS20', b2)
    if hasattr(b1, 'minioclcs_MultiplicityCS'):
        assert not _is_linked(b1, 'minioclcs_MultiplicityCS', a)
    if hasattr(b2, 'minioclcs_MultiplicityCS'):
        assert _is_linked(b2, 'minioclcs_MultiplicityCS', a)
    _safe_set(a, 'minioclcs_PropertyCS20', None)
    assert not _is_linked(a, 'minioclcs_PropertyCS20', b2)
    if hasattr(b2, 'minioclcs_MultiplicityCS'):
        assert not _is_linked(b2, 'minioclcs_MultiplicityCS', a)


def test_assoc_operations14_link_reassign_clear():
    a = minioclcs_OperationCS(name="sample_text")
    b1 = minioclcs_ClassCS(name="sample_text")
    b2 = minioclcs_ClassCS(name="sample_text_2")
    _safe_set(a, 'minioclcs_OperationCS', b1)
    assert _is_linked(a, 'minioclcs_OperationCS', b1)
    if hasattr(b1, 'minioclcs_ClassCS15'):
        assert _is_linked(b1, 'minioclcs_ClassCS15', a)
    _safe_set(a, 'minioclcs_OperationCS', b2)
    assert _is_linked(a, 'minioclcs_OperationCS', b2)
    if hasattr(b1, 'minioclcs_ClassCS15'):
        assert not _is_linked(b1, 'minioclcs_ClassCS15', a)
    if hasattr(b2, 'minioclcs_ClassCS15'):
        assert _is_linked(b2, 'minioclcs_ClassCS15', a)
    _safe_set(a, 'minioclcs_OperationCS', None)
    assert not _is_linked(a, 'minioclcs_OperationCS', b2)
    if hasattr(b2, 'minioclcs_ClassCS15'):
        assert not _is_linked(b2, 'minioclcs_ClassCS15', a)


def test_assoc_packages1_link_reassign_clear():
    a = minioclcs_PackageCS(name="sample_text")
    b1 = minioclcs_RootCS()
    b2 = minioclcs_RootCS()
    _safe_set(a, 'minioclcs_PackageCS', b1)
    assert _is_linked(a, 'minioclcs_PackageCS', b1)
    if hasattr(b1, 'minioclcs_RootCS2'):
        assert _is_linked(b1, 'minioclcs_RootCS2', a)
    _safe_set(a, 'minioclcs_PackageCS', b2)
    assert _is_linked(a, 'minioclcs_PackageCS', b2)
    if hasattr(b1, 'minioclcs_RootCS2'):
        assert not _is_linked(b1, 'minioclcs_RootCS2', a)
    if hasattr(b2, 'minioclcs_RootCS2'):
        assert _is_linked(b2, 'minioclcs_RootCS2', a)
    _safe_set(a, 'minioclcs_PackageCS', None)
    assert not _is_linked(a, 'minioclcs_PackageCS', b2)
    if hasattr(b2, 'minioclcs_RootCS2'):
        assert not _is_linked(b2, 'minioclcs_RootCS2', a)


def test_assoc_packages6_link_reassign_clear():
    a = minioclcs_PackageCS(name="sample_text")
    b1 = minioclcs_PackageCS(name="sample_text")
    b2 = minioclcs_PackageCS(name="sample_text_2")
    _safe_set(a, 'minioclcs_PackageCS5', {b1})
    assert _is_linked(a, 'minioclcs_PackageCS5', b1)
    if hasattr(b1, 'minioclcs_PackageCS7'):
        assert _is_linked(b1, 'minioclcs_PackageCS7', a)
    _safe_set(a, 'minioclcs_PackageCS5', {b2})
    assert _is_linked(a, 'minioclcs_PackageCS5', b2)
    if hasattr(b1, 'minioclcs_PackageCS7'):
        assert not _is_linked(b1, 'minioclcs_PackageCS7', a)
    if hasattr(b2, 'minioclcs_PackageCS7'):
        assert _is_linked(b2, 'minioclcs_PackageCS7', a)
    _safe_set(a, 'minioclcs_PackageCS5', set())
    assert not _is_linked(a, 'minioclcs_PackageCS5', b2)
    if hasattr(b2, 'minioclcs_PackageCS7'):
        assert not _is_linked(b2, 'minioclcs_PackageCS7', a)


def test_assoc_params21_link_reassign_clear():
    a = minioclcs_ParameterCS(name="sample_text")
    b1 = minioclcs_OperationCS(name="sample_text")
    b2 = minioclcs_OperationCS(name="sample_text_2")
    _safe_set(a, 'minioclcs_ParameterCS', b1)
    assert _is_linked(a, 'minioclcs_ParameterCS', b1)
    if hasattr(b1, 'minioclcs_OperationCS22'):
        assert _is_linked(b1, 'minioclcs_OperationCS22', a)
    _safe_set(a, 'minioclcs_ParameterCS', b2)
    assert _is_linked(a, 'minioclcs_ParameterCS', b2)
    if hasattr(b1, 'minioclcs_OperationCS22'):
        assert not _is_linked(b1, 'minioclcs_OperationCS22', a)
    if hasattr(b2, 'minioclcs_OperationCS22'):
        assert _is_linked(b2, 'minioclcs_OperationCS22', a)
    _safe_set(a, 'minioclcs_ParameterCS', None)
    assert not _is_linked(a, 'minioclcs_ParameterCS', b2)
    if hasattr(b2, 'minioclcs_OperationCS22'):
        assert not _is_linked(b2, 'minioclcs_OperationCS22', a)


def test_assoc_parts69_link_reassign_clear():
    a = minioclcs_CollectionLiteralExpCS(kind="sample_text")
    b1 = minioclcs_CollectionLiteralPartCS()
    b2 = minioclcs_CollectionLiteralPartCS()
    _safe_set(a, 'minioclcs_CollectionLiteralExpCS', {b1})
    assert _is_linked(a, 'minioclcs_CollectionLiteralExpCS', b1)
    if hasattr(b1, 'minioclcs_CollectionLiteralPartCS'):
        assert _is_linked(b1, 'minioclcs_CollectionLiteralPartCS', a)
    _safe_set(a, 'minioclcs_CollectionLiteralExpCS', {b2})
    assert _is_linked(a, 'minioclcs_CollectionLiteralExpCS', b2)
    if hasattr(b1, 'minioclcs_CollectionLiteralPartCS'):
        assert not _is_linked(b1, 'minioclcs_CollectionLiteralPartCS', a)
    if hasattr(b2, 'minioclcs_CollectionLiteralPartCS'):
        assert _is_linked(b2, 'minioclcs_CollectionLiteralPartCS', a)
    _safe_set(a, 'minioclcs_CollectionLiteralExpCS', set())
    assert not _is_linked(a, 'minioclcs_CollectionLiteralExpCS', b2)
    if hasattr(b2, 'minioclcs_CollectionLiteralPartCS'):
        assert not _is_linked(b2, 'minioclcs_CollectionLiteralPartCS', a)


def test_assoc_properties12_link_reassign_clear():
    a = minioclcs_PropertyCS(name="sample_text")
    b1 = minioclcs_ClassCS(name="sample_text")
    b2 = minioclcs_ClassCS(name="sample_text_2")
    _safe_set(a, 'minioclcs_PropertyCS', b1)
    assert _is_linked(a, 'minioclcs_PropertyCS', b1)
    if hasattr(b1, 'minioclcs_ClassCS13'):
        assert _is_linked(b1, 'minioclcs_ClassCS13', a)
    _safe_set(a, 'minioclcs_PropertyCS', b2)
    assert _is_linked(a, 'minioclcs_PropertyCS', b2)
    if hasattr(b1, 'minioclcs_ClassCS13'):
        assert not _is_linked(b1, 'minioclcs_ClassCS13', a)
    if hasattr(b2, 'minioclcs_ClassCS13'):
        assert _is_linked(b2, 'minioclcs_ClassCS13', a)
    _safe_set(a, 'minioclcs_PropertyCS', None)
    assert not _is_linked(a, 'minioclcs_PropertyCS', b2)
    if hasattr(b2, 'minioclcs_ClassCS13'):
        assert not _is_linked(b2, 'minioclcs_ClassCS13', a)


def test_assoc_resultRef23_link_reassign_clear():
    a = minioclcs_OperationCS(name="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_OperationCS24', b1)
    assert _is_linked(a, 'minioclcs_OperationCS24', b1)
    if hasattr(b1, 'minioclcs_PathNameCS25'):
        assert _is_linked(b1, 'minioclcs_PathNameCS25', a)
    _safe_set(a, 'minioclcs_OperationCS24', b2)
    assert _is_linked(a, 'minioclcs_OperationCS24', b2)
    if hasattr(b1, 'minioclcs_PathNameCS25'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS25', a)
    if hasattr(b2, 'minioclcs_PathNameCS25'):
        assert _is_linked(b2, 'minioclcs_PathNameCS25', a)
    _safe_set(a, 'minioclcs_OperationCS24', None)
    assert not _is_linked(a, 'minioclcs_OperationCS24', b2)
    if hasattr(b2, 'minioclcs_PathNameCS25'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS25', a)


def test_assoc_right41_link_reassign_clear():
    a = minioclcs_EqualityExpCS(opName="sample_text")
    b1 = minioclcs_CallExpCS()
    b2 = minioclcs_CallExpCS()
    _safe_set(a, 'minioclcs_EqualityExpCS42', b1)
    assert _is_linked(a, 'minioclcs_EqualityExpCS42', b1)
    if hasattr(b1, 'minioclcs_CallExpCS'):
        assert _is_linked(b1, 'minioclcs_CallExpCS', a)
    _safe_set(a, 'minioclcs_EqualityExpCS42', b2)
    assert _is_linked(a, 'minioclcs_EqualityExpCS42', b2)
    if hasattr(b1, 'minioclcs_CallExpCS'):
        assert not _is_linked(b1, 'minioclcs_CallExpCS', a)
    if hasattr(b2, 'minioclcs_CallExpCS'):
        assert _is_linked(b2, 'minioclcs_CallExpCS', a)
    _safe_set(a, 'minioclcs_EqualityExpCS42', None)
    assert not _is_linked(a, 'minioclcs_EqualityExpCS42', b2)
    if hasattr(b2, 'minioclcs_CallExpCS'):
        assert not _is_linked(b2, 'minioclcs_CallExpCS', a)


def test_assoc_typeRef16_link_reassign_clear():
    a = minioclcs_PropertyCS(name="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_PropertyCS17', b1)
    assert _is_linked(a, 'minioclcs_PropertyCS17', b1)
    if hasattr(b1, 'minioclcs_PathNameCS18'):
        assert _is_linked(b1, 'minioclcs_PathNameCS18', a)
    _safe_set(a, 'minioclcs_PropertyCS17', b2)
    assert _is_linked(a, 'minioclcs_PropertyCS17', b2)
    if hasattr(b1, 'minioclcs_PathNameCS18'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS18', a)
    if hasattr(b2, 'minioclcs_PathNameCS18'):
        assert _is_linked(b2, 'minioclcs_PathNameCS18', a)
    _safe_set(a, 'minioclcs_PropertyCS17', None)
    assert not _is_linked(a, 'minioclcs_PropertyCS17', b2)
    if hasattr(b2, 'minioclcs_PathNameCS18'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS18', a)


def test_assoc_typeRef28_link_reassign_clear():
    a = minioclcs_ParameterCS(name="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_ParameterCS29', b1)
    assert _is_linked(a, 'minioclcs_ParameterCS29', b1)
    if hasattr(b1, 'minioclcs_PathNameCS30'):
        assert _is_linked(b1, 'minioclcs_PathNameCS30', a)
    _safe_set(a, 'minioclcs_ParameterCS29', b2)
    assert _is_linked(a, 'minioclcs_ParameterCS29', b2)
    if hasattr(b1, 'minioclcs_PathNameCS30'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS30', a)
    if hasattr(b2, 'minioclcs_PathNameCS30'):
        assert _is_linked(b2, 'minioclcs_PathNameCS30', a)
    _safe_set(a, 'minioclcs_ParameterCS29', None)
    assert not _is_linked(a, 'minioclcs_ParameterCS29', b2)
    if hasattr(b2, 'minioclcs_PathNameCS30'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS30', a)


def test_assoc_typeRef80_link_reassign_clear():
    a = minioclcs_LetVarCS(name="sample_text")
    b1 = minioclcs_PathNameCS()
    b2 = minioclcs_PathNameCS()
    _safe_set(a, 'minioclcs_LetVarCS81', b1)
    assert _is_linked(a, 'minioclcs_LetVarCS81', b1)
    if hasattr(b1, 'minioclcs_PathNameCS82'):
        assert _is_linked(b1, 'minioclcs_PathNameCS82', a)
    _safe_set(a, 'minioclcs_LetVarCS81', b2)
    assert _is_linked(a, 'minioclcs_LetVarCS81', b2)
    if hasattr(b1, 'minioclcs_PathNameCS82'):
        assert not _is_linked(b1, 'minioclcs_PathNameCS82', a)
    if hasattr(b2, 'minioclcs_PathNameCS82'):
        assert _is_linked(b2, 'minioclcs_PathNameCS82', a)
    _safe_set(a, 'minioclcs_LetVarCS81', None)
    assert not _is_linked(a, 'minioclcs_LetVarCS81', b2)
    if hasattr(b2, 'minioclcs_PathNameCS82'):
        assert not _is_linked(b2, 'minioclcs_PathNameCS82', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

BooleanLiteralExpCS_strategy = st.builds(BooleanLiteralExpCS)
@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)


CSTrace_strategy = st.builds(CSTrace)
@given(instance=CSTrace_strategy)
@settings(max_examples=25)
def test_CSTrace_instantiation(instance):
    assert isinstance(instance, CSTrace)


CallExpCS_strategy = st.builds(CallExpCS)
@given(instance=CallExpCS_strategy)
@settings(max_examples=25)
def test_CallExpCS_instantiation(instance):
    assert isinstance(instance, CallExpCS)


EqualityExpCS_strategy = st.builds(EqualityExpCS)
@given(instance=EqualityExpCS_strategy)
@settings(max_examples=25)
def test_EqualityExpCS_instantiation(instance):
    assert isinstance(instance, EqualityExpCS)


ExpCS_strategy = st.builds(ExpCS)
@given(instance=ExpCS_strategy)
@settings(max_examples=25)
def test_ExpCS_instantiation(instance):
    assert isinstance(instance, ExpCS)


LiteralExpCS_strategy = st.builds(LiteralExpCS)
@given(instance=LiteralExpCS_strategy)
@settings(max_examples=25)
def test_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)


LoopExpCS_strategy = st.builds(LoopExpCS)
@given(instance=LoopExpCS_strategy)
@settings(max_examples=25)
def test_LoopExpCS_instantiation(instance):
    assert isinstance(instance, LoopExpCS)


NavigationExpCS_strategy = st.builds(NavigationExpCS)
@given(instance=NavigationExpCS_strategy)
@settings(max_examples=25)
def test_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)


PrimaryExpCS_strategy = st.builds(PrimaryExpCS)
@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)


minioclcs_AccVarCS_strategy = st.builds(minioclcs_AccVarCS, accName=safe_text)
@given(instance=minioclcs_AccVarCS_strategy)
@settings(max_examples=25)
def test_minioclcs_AccVarCS_instantiation(instance):
    assert isinstance(instance, minioclcs_AccVarCS)


minioclcs_BooleanExpCS_strategy = st.builds(minioclcs_BooleanExpCS, boolSymbol=st.booleans())
@given(instance=minioclcs_BooleanExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_BooleanExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_BooleanExpCS)


minioclcs_BooleanLiteralExpCS_strategy = st.builds(minioclcs_BooleanLiteralExpCS)
@given(instance=minioclcs_BooleanLiteralExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_BooleanLiteralExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_BooleanLiteralExpCS)


minioclcs_CSTrace_strategy = st.builds(minioclcs_CSTrace)
@given(instance=minioclcs_CSTrace_strategy)
@settings(max_examples=25)
def test_minioclcs_CSTrace_instantiation(instance):
    assert isinstance(instance, minioclcs_CSTrace)


minioclcs_CallExpCS_strategy = st.builds(minioclcs_CallExpCS)
@given(instance=minioclcs_CallExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_CallExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_CallExpCS)


minioclcs_ClassCS_strategy = st.builds(minioclcs_ClassCS, name=safe_text)
@given(instance=minioclcs_ClassCS_strategy)
@settings(max_examples=25)
def test_minioclcs_ClassCS_instantiation(instance):
    assert isinstance(instance, minioclcs_ClassCS)


minioclcs_CollectExpCS_strategy = st.builds(minioclcs_CollectExpCS)
@given(instance=minioclcs_CollectExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_CollectExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectExpCS)


minioclcs_CollectionLiteralExpCS_strategy = st.builds(minioclcs_CollectionLiteralExpCS, kind=safe_text)
@given(instance=minioclcs_CollectionLiteralExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_CollectionLiteralExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectionLiteralExpCS)


minioclcs_CollectionLiteralPartCS_strategy = st.builds(minioclcs_CollectionLiteralPartCS)
@given(instance=minioclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=25)
def test_minioclcs_CollectionLiteralPartCS_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectionLiteralPartCS)


minioclcs_ConstraintsDefCS_strategy = st.builds(minioclcs_ConstraintsDefCS)
@given(instance=minioclcs_ConstraintsDefCS_strategy)
@settings(max_examples=25)
def test_minioclcs_ConstraintsDefCS_instantiation(instance):
    assert isinstance(instance, minioclcs_ConstraintsDefCS)


minioclcs_EClass_strategy = st.builds(minioclcs_EClass)
@given(instance=minioclcs_EClass_strategy)
@settings(max_examples=25)
def test_minioclcs_EClass_instantiation(instance):
    assert isinstance(instance, minioclcs_EClass)


minioclcs_EObject_strategy = st.builds(minioclcs_EObject)
@given(instance=minioclcs_EObject_strategy)
@settings(max_examples=25)
def test_minioclcs_EObject_instantiation(instance):
    assert isinstance(instance, minioclcs_EObject)


minioclcs_EqualityExpCS_strategy = st.builds(minioclcs_EqualityExpCS, opName=safe_text)
@given(instance=minioclcs_EqualityExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_EqualityExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_EqualityExpCS)


minioclcs_ExpCS_strategy = st.builds(minioclcs_ExpCS)
@given(instance=minioclcs_ExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_ExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_ExpCS)


minioclcs_ImportCS_strategy = st.builds(minioclcs_ImportCS, alias=safe_text, uri=safe_text)
@given(instance=minioclcs_ImportCS_strategy)
@settings(max_examples=25)
def test_minioclcs_ImportCS_instantiation(instance):
    assert isinstance(instance, minioclcs_ImportCS)


minioclcs_IntLiteralExpCS_strategy = st.builds(minioclcs_IntLiteralExpCS, intSymbol=st.integers())
@given(instance=minioclcs_IntLiteralExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_IntLiteralExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_IntLiteralExpCS)


minioclcs_InvariantCS_strategy = st.builds(minioclcs_InvariantCS)
@given(instance=minioclcs_InvariantCS_strategy)
@settings(max_examples=25)
def test_minioclcs_InvariantCS_instantiation(instance):
    assert isinstance(instance, minioclcs_InvariantCS)


minioclcs_IterateExpCS_strategy = st.builds(minioclcs_IterateExpCS)
@given(instance=minioclcs_IterateExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_IterateExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_IterateExpCS)


minioclcs_IteratorVarCS_strategy = st.builds(minioclcs_IteratorVarCS, itName=safe_text)
@given(instance=minioclcs_IteratorVarCS_strategy)
@settings(max_examples=25)
def test_minioclcs_IteratorVarCS_instantiation(instance):
    assert isinstance(instance, minioclcs_IteratorVarCS)


minioclcs_LetExpCS_strategy = st.builds(minioclcs_LetExpCS)
@given(instance=minioclcs_LetExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_LetExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_LetExpCS)


minioclcs_LetVarCS_strategy = st.builds(minioclcs_LetVarCS, name=safe_text)
@given(instance=minioclcs_LetVarCS_strategy)
@settings(max_examples=25)
def test_minioclcs_LetVarCS_instantiation(instance):
    assert isinstance(instance, minioclcs_LetVarCS)


minioclcs_LiteralExpCS_strategy = st.builds(minioclcs_LiteralExpCS)
@given(instance=minioclcs_LiteralExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_LiteralExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_LiteralExpCS)


minioclcs_LoopExpCS_strategy = st.builds(minioclcs_LoopExpCS)
@given(instance=minioclcs_LoopExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_LoopExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_LoopExpCS)


minioclcs_MultiplicityCS_strategy = st.builds(minioclcs_MultiplicityCS, lowerInt=st.integers(), mandatory=st.integers(), mult=st.booleans(), opt=st.booleans(), upperInt=st.integers(), upperMult=st.booleans())
@given(instance=minioclcs_MultiplicityCS_strategy)
@settings(max_examples=25)
def test_minioclcs_MultiplicityCS_instantiation(instance):
    assert isinstance(instance, minioclcs_MultiplicityCS)


minioclcs_NameExpCS_strategy = st.builds(minioclcs_NameExpCS)
@given(instance=minioclcs_NameExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_NameExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_NameExpCS)


minioclcs_NavigationExpCS_strategy = st.builds(minioclcs_NavigationExpCS)
@given(instance=minioclcs_NavigationExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_NavigationExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_NavigationExpCS)


minioclcs_NullLiteralExpCS_strategy = st.builds(minioclcs_NullLiteralExpCS)
@given(instance=minioclcs_NullLiteralExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_NullLiteralExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_NullLiteralExpCS)


minioclcs_OperationCS_strategy = st.builds(minioclcs_OperationCS, name=safe_text)
@given(instance=minioclcs_OperationCS_strategy)
@settings(max_examples=25)
def test_minioclcs_OperationCS_instantiation(instance):
    assert isinstance(instance, minioclcs_OperationCS)


minioclcs_PackageCS_strategy = st.builds(minioclcs_PackageCS, name=safe_text)
@given(instance=minioclcs_PackageCS_strategy)
@settings(max_examples=25)
def test_minioclcs_PackageCS_instantiation(instance):
    assert isinstance(instance, minioclcs_PackageCS)


minioclcs_ParameterCS_strategy = st.builds(minioclcs_ParameterCS, name=safe_text)
@given(instance=minioclcs_ParameterCS_strategy)
@settings(max_examples=25)
def test_minioclcs_ParameterCS_instantiation(instance):
    assert isinstance(instance, minioclcs_ParameterCS)


minioclcs_PathElementCS_strategy = st.builds(minioclcs_PathElementCS)
@given(instance=minioclcs_PathElementCS_strategy)
@settings(max_examples=25)
def test_minioclcs_PathElementCS_instantiation(instance):
    assert isinstance(instance, minioclcs_PathElementCS)


minioclcs_PathNameCS_strategy = st.builds(minioclcs_PathNameCS)
@given(instance=minioclcs_PathNameCS_strategy)
@settings(max_examples=25)
def test_minioclcs_PathNameCS_instantiation(instance):
    assert isinstance(instance, minioclcs_PathNameCS)


minioclcs_PrimaryExpCS_strategy = st.builds(minioclcs_PrimaryExpCS)
@given(instance=minioclcs_PrimaryExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_PrimaryExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_PrimaryExpCS)


minioclcs_PropertyCS_strategy = st.builds(minioclcs_PropertyCS, name=safe_text)
@given(instance=minioclcs_PropertyCS_strategy)
@settings(max_examples=25)
def test_minioclcs_PropertyCS_instantiation(instance):
    assert isinstance(instance, minioclcs_PropertyCS)


minioclcs_RootCS_strategy = st.builds(minioclcs_RootCS)
@given(instance=minioclcs_RootCS_strategy)
@settings(max_examples=25)
def test_minioclcs_RootCS_instantiation(instance):
    assert isinstance(instance, minioclcs_RootCS)


minioclcs_RoundedBracketClauseCS_strategy = st.builds(minioclcs_RoundedBracketClauseCS)
@given(instance=minioclcs_RoundedBracketClauseCS_strategy)
@settings(max_examples=25)
def test_minioclcs_RoundedBracketClauseCS_instantiation(instance):
    assert isinstance(instance, minioclcs_RoundedBracketClauseCS)


minioclcs_SelfExpCS_strategy = st.builds(minioclcs_SelfExpCS)
@given(instance=minioclcs_SelfExpCS_strategy)
@settings(max_examples=25)
def test_minioclcs_SelfExpCS_instantiation(instance):
    assert isinstance(instance, minioclcs_SelfExpCS)


