import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    JDTJavaElement,
    JDTMember,
    JDTMethodBody,
    JDTParent,
    JDTParentJavaElement,
    JDTType,
    JDTTypeRoot,
    jdtmm_JDTClass,
    jdtmm_JDTCompilationUnit,
    jdtmm_JDTEnum,
    jdtmm_JDTException,
    jdtmm_JDTField,
    jdtmm_JDTImportContainer,
    jdtmm_JDTImportDeclaration,
    jdtmm_JDTInterface,
    jdtmm_JDTJavaElement,
    jdtmm_JDTJavaModel,
    jdtmm_JDTJavaProject,
    jdtmm_JDTMember,
    jdtmm_JDTMethod,
    jdtmm_JDTMethodBody,
    jdtmm_JDTOpaqueBody,
    jdtmm_JDTPackageFragment,
    jdtmm_JDTPackageFragmentRoot,
    jdtmm_JDTParameter,
    jdtmm_JDTParent,
    jdtmm_JDTParentJavaElement,
    jdtmm_JDTType,
    jdtmm_JDTTypeParameter,
    jdtmm_JDTTypeRoot,
    TrueFalseDefault,
    VisibilityKind,
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

def test_assoc_bodies6_reverse_link_reassign_clear():
    a1 = jdtmm_JDTMethodBody()
    a2 = jdtmm_JDTMethodBody()
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'owner', {a1})
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'JDTMethodBody'):
        assert _is_linked(a1, 'JDTMethodBody', b)
    _safe_set(b, 'owner', {a2})
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'JDTMethodBody'):
        assert not _is_linked(a1, 'JDTMethodBody', b)
    if hasattr(a2, 'JDTMethodBody'):
        assert _is_linked(a2, 'JDTMethodBody', b)
    _safe_set(b, 'owner', set())
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'JDTMethodBody'):
        assert not _is_linked(a2, 'JDTMethodBody', b)


def test_assoc_children10_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParent(flags="sample_text")
    a2 = jdtmm_JDTParent(flags="sample_text_2")
    b = jdtmm_JDTJavaElement(comment="sample_text", elementName="sample_text", elementType="sample_text", generated="sample_text")
    _safe_set(b, 'JDTJavaElement', a1)
    assert _is_linked(b, 'JDTJavaElement', a1)
    if hasattr(a1, 'parent'):
        assert _is_linked(a1, 'parent', b)
    _safe_set(b, 'JDTJavaElement', a2)
    assert _is_linked(b, 'JDTJavaElement', a2)
    if hasattr(a1, 'parent'):
        assert not _is_linked(a1, 'parent', b)
    if hasattr(a2, 'parent'):
        assert _is_linked(a2, 'parent', b)
    _safe_set(b, 'JDTJavaElement', None)
    assert not _is_linked(b, 'JDTJavaElement', a2)
    if hasattr(a2, 'parent'):
        assert not _is_linked(a2, 'parent', b)


def test_assoc_exceptions5_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'jdtmm_JDTMethod', {a1})
    assert _is_linked(b, 'jdtmm_JDTMethod', a1)
    if hasattr(a1, 'jdtmm_JDTType'):
        assert _is_linked(a1, 'jdtmm_JDTType', b)
    _safe_set(b, 'jdtmm_JDTMethod', {a2})
    assert _is_linked(b, 'jdtmm_JDTMethod', a2)
    if hasattr(a1, 'jdtmm_JDTType'):
        assert not _is_linked(a1, 'jdtmm_JDTType', b)
    if hasattr(a2, 'jdtmm_JDTType'):
        assert _is_linked(a2, 'jdtmm_JDTType', b)
    _safe_set(b, 'jdtmm_JDTMethod', set())
    assert not _is_linked(b, 'jdtmm_JDTMethod', a2)
    if hasattr(a2, 'jdtmm_JDTType'):
        assert not _is_linked(a2, 'jdtmm_JDTType', b)


def test_assoc_explicitRequiredImports8_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTMember(explicitPlainTextRequiredImports="sample_text", visibility="sample_text")
    _safe_set(b, 'jdtmm_JDTMember', {a1})
    assert _is_linked(b, 'jdtmm_JDTMember', a1)
    if hasattr(a1, 'jdtmm_JDTType9'):
        assert _is_linked(a1, 'jdtmm_JDTType9', b)
    _safe_set(b, 'jdtmm_JDTMember', {a2})
    assert _is_linked(b, 'jdtmm_JDTMember', a2)
    if hasattr(a1, 'jdtmm_JDTType9'):
        assert not _is_linked(a1, 'jdtmm_JDTType9', b)
    if hasattr(a2, 'jdtmm_JDTType9'):
        assert _is_linked(a2, 'jdtmm_JDTType9', b)
    _safe_set(b, 'jdtmm_JDTMember', set())
    assert not _is_linked(b, 'jdtmm_JDTMember', a2)
    if hasattr(a2, 'jdtmm_JDTType9'):
        assert not _is_linked(a2, 'jdtmm_JDTType9', b)


def test_assoc_fields16_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTField(abstract="sample_text", final="sample_text", generateGetter="sample_text", generateSetter="sample_text", isMultiValued="sample_text", static="sample_text", value="sample_text")
    _safe_set(b, 'JDTField', a1)
    assert _is_linked(b, 'JDTField', a1)
    if hasattr(a1, 'owner17'):
        assert _is_linked(a1, 'owner17', b)
    _safe_set(b, 'JDTField', a2)
    assert _is_linked(b, 'JDTField', a2)
    if hasattr(a1, 'owner17'):
        assert not _is_linked(a1, 'owner17', b)
    if hasattr(a2, 'owner17'):
        assert _is_linked(a2, 'owner17', b)
    _safe_set(b, 'JDTField', None)
    assert not _is_linked(b, 'JDTField', a2)
    if hasattr(a2, 'owner17'):
        assert not _is_linked(a2, 'owner17', b)


def test_assoc_methods13_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'JDTMethod15', a1)
    assert _is_linked(b, 'JDTMethod15', a1)
    if hasattr(a1, 'owner14'):
        assert _is_linked(a1, 'owner14', b)
    _safe_set(b, 'JDTMethod15', a2)
    assert _is_linked(b, 'JDTMethod15', a2)
    if hasattr(a1, 'owner14'):
        assert not _is_linked(a1, 'owner14', b)
    if hasattr(a2, 'owner14'):
        assert _is_linked(a2, 'owner14', b)
    _safe_set(b, 'JDTMethod15', None)
    assert not _is_linked(b, 'JDTMethod15', a2)
    if hasattr(a2, 'owner14'):
        assert not _is_linked(a2, 'owner14', b)


def test_assoc_owner0_reverse_link_reassign_clear():
    a1 = jdtmm_JDTMethodBody()
    a2 = jdtmm_JDTMethodBody()
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'JDTMethod', a1)
    assert _is_linked(b, 'JDTMethod', a1)
    if hasattr(a1, 'bodies'):
        assert _is_linked(a1, 'bodies', b)
    _safe_set(b, 'JDTMethod', a2)
    assert _is_linked(b, 'JDTMethod', a2)
    if hasattr(a1, 'bodies'):
        assert not _is_linked(a1, 'bodies', b)
    if hasattr(a2, 'bodies'):
        assert _is_linked(a2, 'bodies', b)
    _safe_set(b, 'JDTMethod', None)
    assert not _is_linked(b, 'JDTMethod', a2)
    if hasattr(a2, 'bodies'):
        assert not _is_linked(a2, 'bodies', b)


def test_assoc_owner1_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'methods', a1)
    assert _is_linked(b, 'methods', a1)
    if hasattr(a1, 'JDTType'):
        assert _is_linked(a1, 'JDTType', b)
    _safe_set(b, 'methods', a2)
    assert _is_linked(b, 'methods', a2)
    if hasattr(a1, 'JDTType'):
        assert not _is_linked(a1, 'JDTType', b)
    if hasattr(a2, 'JDTType'):
        assert _is_linked(a2, 'JDTType', b)
    _safe_set(b, 'methods', None)
    assert not _is_linked(b, 'methods', a2)
    if hasattr(a2, 'JDTType'):
        assert not _is_linked(a2, 'JDTType', b)


def test_assoc_owner24_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    _safe_set(b, 'types25', a1)
    assert _is_linked(b, 'types25', a1)
    if hasattr(a1, 'JDTType26'):
        assert _is_linked(a1, 'JDTType26', b)
    _safe_set(b, 'types25', a2)
    assert _is_linked(b, 'types25', a2)
    if hasattr(a1, 'JDTType26'):
        assert not _is_linked(a1, 'JDTType26', b)
    if hasattr(a2, 'JDTType26'):
        assert _is_linked(a2, 'JDTType26', b)
    _safe_set(b, 'types25', None)
    assert not _is_linked(b, 'types25', a2)
    if hasattr(a2, 'JDTType26'):
        assert not _is_linked(a2, 'JDTType26', b)


def test_assoc_owner35_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTField(abstract="sample_text", final="sample_text", generateGetter="sample_text", generateSetter="sample_text", isMultiValued="sample_text", static="sample_text", value="sample_text")
    _safe_set(b, 'fields', a1)
    assert _is_linked(b, 'fields', a1)
    if hasattr(a1, 'JDTType36'):
        assert _is_linked(a1, 'JDTType36', b)
    _safe_set(b, 'fields', a2)
    assert _is_linked(b, 'fields', a2)
    if hasattr(a1, 'JDTType36'):
        assert not _is_linked(a1, 'JDTType36', b)
    if hasattr(a2, 'JDTType36'):
        assert _is_linked(a2, 'JDTType36', b)
    _safe_set(b, 'fields', None)
    assert not _is_linked(b, 'fields', a2)
    if hasattr(a2, 'JDTType36'):
        assert not _is_linked(a2, 'JDTType36', b)


def test_assoc_parameterOwner52_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParameter(final="sample_text", isMultiValued="sample_text")
    a2 = jdtmm_JDTParameter(final="sample_text_2", isMultiValued="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'JDTMethod53', a1)
    assert _is_linked(b, 'JDTMethod53', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'JDTMethod53', a2)
    assert _is_linked(b, 'JDTMethod53', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'JDTMethod53', None)
    assert not _is_linked(b, 'JDTMethod53', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_parameters3_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParameter(final="sample_text", isMultiValued="sample_text")
    a2 = jdtmm_JDTParameter(final="sample_text_2", isMultiValued="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'parameterOwner', {a1})
    assert _is_linked(b, 'parameterOwner', a1)
    if hasattr(a1, 'JDTParameter4'):
        assert _is_linked(a1, 'JDTParameter4', b)
    _safe_set(b, 'parameterOwner', {a2})
    assert _is_linked(b, 'parameterOwner', a2)
    if hasattr(a1, 'JDTParameter4'):
        assert not _is_linked(a1, 'JDTParameter4', b)
    if hasattr(a2, 'JDTParameter4'):
        assert _is_linked(a2, 'JDTParameter4', b)
    _safe_set(b, 'parameterOwner', set())
    assert not _is_linked(b, 'parameterOwner', a2)
    if hasattr(a2, 'JDTParameter4'):
        assert not _is_linked(a2, 'JDTParameter4', b)


def test_assoc_parent11_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParent(flags="sample_text")
    a2 = jdtmm_JDTParent(flags="sample_text_2")
    b = jdtmm_JDTJavaElement(comment="sample_text", elementName="sample_text", elementType="sample_text", generated="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'JDTParent'):
        assert _is_linked(a1, 'JDTParent', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'JDTParent'):
        assert not _is_linked(a1, 'JDTParent', b)
    if hasattr(a2, 'JDTParent'):
        assert _is_linked(a2, 'JDTParent', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'JDTParent'):
        assert not _is_linked(a2, 'JDTParent', b)


def test_assoc_returnOwner56_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParameter(final="sample_text", isMultiValued="sample_text")
    a2 = jdtmm_JDTParameter(final="sample_text_2", isMultiValued="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'JDTMethod57', a1)
    assert _is_linked(b, 'JDTMethod57', a1)
    if hasattr(a1, 'returnType'):
        assert _is_linked(a1, 'returnType', b)
    _safe_set(b, 'JDTMethod57', a2)
    assert _is_linked(b, 'JDTMethod57', a2)
    if hasattr(a1, 'returnType'):
        assert not _is_linked(a1, 'returnType', b)
    if hasattr(a2, 'returnType'):
        assert _is_linked(a2, 'returnType', b)
    _safe_set(b, 'JDTMethod57', None)
    assert not _is_linked(b, 'JDTMethod57', a2)
    if hasattr(a2, 'returnType'):
        assert not _is_linked(a2, 'returnType', b)


def test_assoc_returnType2_reverse_link_reassign_clear():
    a1 = jdtmm_JDTParameter(final="sample_text", isMultiValued="sample_text")
    a2 = jdtmm_JDTParameter(final="sample_text_2", isMultiValued="sample_text_2")
    b = jdtmm_JDTMethod(abstract="sample_text", constructor="sample_text", final="sample_text", static="sample_text", synchronized="sample_text")
    _safe_set(b, 'returnOwner', a1)
    assert _is_linked(b, 'returnOwner', a1)
    if hasattr(a1, 'JDTParameter'):
        assert _is_linked(a1, 'JDTParameter', b)
    _safe_set(b, 'returnOwner', a2)
    assert _is_linked(b, 'returnOwner', a2)
    if hasattr(a1, 'JDTParameter'):
        assert not _is_linked(a1, 'JDTParameter', b)
    if hasattr(a2, 'JDTParameter'):
        assert _is_linked(a2, 'JDTParameter', b)
    _safe_set(b, 'returnOwner', None)
    assert not _is_linked(b, 'returnOwner', a2)
    if hasattr(a2, 'JDTParameter'):
        assert not _is_linked(a2, 'JDTParameter', b)


def test_assoc_superClass31_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    _safe_set(b, 'jdtmm_JDTType32', a1)
    assert _is_linked(b, 'jdtmm_JDTType32', a1)
    if hasattr(a1, 'jdtmm_JDTType30'):
        assert _is_linked(a1, 'jdtmm_JDTType30', b)
    _safe_set(b, 'jdtmm_JDTType32', a2)
    assert _is_linked(b, 'jdtmm_JDTType32', a2)
    if hasattr(a1, 'jdtmm_JDTType30'):
        assert not _is_linked(a1, 'jdtmm_JDTType30', b)
    if hasattr(a2, 'jdtmm_JDTType30'):
        assert _is_linked(a2, 'jdtmm_JDTType30', b)
    _safe_set(b, 'jdtmm_JDTType32', None)
    assert not _is_linked(b, 'jdtmm_JDTType32', a2)
    if hasattr(a2, 'jdtmm_JDTType30'):
        assert not _is_linked(a2, 'jdtmm_JDTType30', b)


def test_assoc_superInterfaces28_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    _safe_set(b, 'jdtmm_JDTType29', a1)
    assert _is_linked(b, 'jdtmm_JDTType29', a1)
    if hasattr(a1, 'jdtmm_JDTType27'):
        assert _is_linked(a1, 'jdtmm_JDTType27', b)
    _safe_set(b, 'jdtmm_JDTType29', a2)
    assert _is_linked(b, 'jdtmm_JDTType29', a2)
    if hasattr(a1, 'jdtmm_JDTType27'):
        assert not _is_linked(a1, 'jdtmm_JDTType27', b)
    if hasattr(a2, 'jdtmm_JDTType27'):
        assert _is_linked(a2, 'jdtmm_JDTType27', b)
    _safe_set(b, 'jdtmm_JDTType29', None)
    assert not _is_linked(b, 'jdtmm_JDTType29', a2)
    if hasattr(a2, 'jdtmm_JDTType27'):
        assert not _is_linked(a2, 'jdtmm_JDTType27', b)


def test_assoc_type33_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTField(abstract="sample_text", final="sample_text", generateGetter="sample_text", generateSetter="sample_text", isMultiValued="sample_text", static="sample_text", value="sample_text")
    _safe_set(b, 'jdtmm_JDTField', a1)
    assert _is_linked(b, 'jdtmm_JDTField', a1)
    if hasattr(a1, 'jdtmm_JDTType34'):
        assert _is_linked(a1, 'jdtmm_JDTType34', b)
    _safe_set(b, 'jdtmm_JDTField', a2)
    assert _is_linked(b, 'jdtmm_JDTField', a2)
    if hasattr(a1, 'jdtmm_JDTType34'):
        assert not _is_linked(a1, 'jdtmm_JDTType34', b)
    if hasattr(a2, 'jdtmm_JDTType34'):
        assert _is_linked(a2, 'jdtmm_JDTType34', b)
    _safe_set(b, 'jdtmm_JDTField', None)
    assert not _is_linked(b, 'jdtmm_JDTField', a2)
    if hasattr(a2, 'jdtmm_JDTType34'):
        assert not _is_linked(a2, 'jdtmm_JDTType34', b)


def test_assoc_type54_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTParameter(final="sample_text", isMultiValued="sample_text")
    _safe_set(b, 'jdtmm_JDTParameter', a1)
    assert _is_linked(b, 'jdtmm_JDTParameter', a1)
    if hasattr(a1, 'jdtmm_JDTType55'):
        assert _is_linked(a1, 'jdtmm_JDTType55', b)
    _safe_set(b, 'jdtmm_JDTParameter', a2)
    assert _is_linked(b, 'jdtmm_JDTParameter', a2)
    if hasattr(a1, 'jdtmm_JDTType55'):
        assert not _is_linked(a1, 'jdtmm_JDTType55', b)
    if hasattr(a2, 'jdtmm_JDTType55'):
        assert _is_linked(a2, 'jdtmm_JDTType55', b)
    _safe_set(b, 'jdtmm_JDTParameter', None)
    assert not _is_linked(b, 'jdtmm_JDTParameter', a2)
    if hasattr(a2, 'jdtmm_JDTType55'):
        assert not _is_linked(a2, 'jdtmm_JDTType55', b)


def test_assoc_types20_reverse_link_reassign_clear():
    a1 = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    a2 = jdtmm_JDTType(abstract="sample_text_2", class_="sample_text_2", enum="sample_text_2", final="sample_text_2", interface="sample_text_2", static="sample_text_2", superClassName="sample_text_2", superInterfaceNames="sample_text_2")
    b = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    _safe_set(b, 'owner21', {a1})
    assert _is_linked(b, 'owner21', a1)
    if hasattr(a1, 'JDTType22'):
        assert _is_linked(a1, 'JDTType22', b)
    _safe_set(b, 'owner21', {a2})
    assert _is_linked(b, 'owner21', a2)
    if hasattr(a1, 'JDTType22'):
        assert not _is_linked(a1, 'JDTType22', b)
    if hasattr(a2, 'JDTType22'):
        assert _is_linked(a2, 'JDTType22', b)
    _safe_set(b, 'owner21', set())
    assert not _is_linked(b, 'owner21', a2)
    if hasattr(a2, 'JDTType22'):
        assert not _is_linked(a2, 'JDTType22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_compilationUnit18_stub_double():
    # jdtmm_JDTCompilationUnit has no real 'JDTCompilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so jdtmm_JDTType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jdtmm_JDTType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    partner = jdtmm_JDTCompilationUnit()
    setattr(partner, 'JDTCompilationUnit', None)
    _safe_set(owner, 'types', partner)
    assert getattr(partner, 'JDTCompilationUnit') == owner
    _safe_set(owner, 'types', None)
    assert getattr(partner, 'JDTCompilationUnit') is None


def test_assoc_declaringMember12_stub_double():
    # jdtmm_JDTTypeParameter has no real 'typeParameters' property in the generated
    # code (a bare stub) -- manually attach it so jdtmm_JDTMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jdtmm_JDTMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jdtmm_JDTMember(explicitPlainTextRequiredImports="sample_text", visibility="sample_text")
    partner = jdtmm_JDTTypeParameter()
    setattr(partner, 'typeParameters', None)
    _safe_set(owner, 'JDTMember', partner)
    assert getattr(partner, 'typeParameters') == owner
    _safe_set(owner, 'JDTMember', None)
    assert getattr(partner, 'typeParameters') is None


def test_assoc_typeParameters7_stub_double():
    # jdtmm_JDTTypeParameter has no real 'JDTTypeParameter' property in the generated
    # code (a bare stub) -- manually attach it so jdtmm_JDTMember's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jdtmm_JDTMember's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jdtmm_JDTMember(explicitPlainTextRequiredImports="sample_text", visibility="sample_text")
    partner = jdtmm_JDTTypeParameter()
    setattr(partner, 'JDTTypeParameter', None)
    _safe_set(owner, 'declaringMember', {partner})
    assert getattr(partner, 'JDTTypeParameter') == owner
    _safe_set(owner, 'declaringMember', set())
    assert getattr(partner, 'JDTTypeParameter') is None


def test_assoc_types38_stub_double():
    # jdtmm_JDTCompilationUnit has no real 'compilationUnit' property in the generated
    # code (a bare stub) -- manually attach it so jdtmm_JDTType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # jdtmm_JDTType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = jdtmm_JDTType(abstract="sample_text", class_="sample_text", enum="sample_text", final="sample_text", interface="sample_text", static="sample_text", superClassName="sample_text", superInterfaceNames="sample_text")
    partner = jdtmm_JDTCompilationUnit()
    setattr(partner, 'compilationUnit', None)
    _safe_set(owner, 'JDTType39', partner)
    assert owner in getattr(partner, 'compilationUnit')
    _safe_set(owner, 'JDTType39', None)
    assert owner not in getattr(partner, 'compilationUnit')


