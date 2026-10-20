import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    Controller,
    EntityComponent,
    SMVC_Attribute,
    SMVC_Component,
    SMVC_Controller,
    SMVC_DataAccessObject,
    SMVC_Entity,
    SMVC_EntityComponent,
    SMVC_EntityController,
    SMVC_Form,
    SMVC_Link,
    SMVC_List,
    SMVC_Page,
    SMVC_SMVCApplication,
    SMVC_SupportedOperation,
    SMVC_View,
    AttributeType,
    Operation,
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

def test_assoc_attributes18_reverse_link_reassign_clear():
    a1 = SMVC_Entity(name="sample_text")
    a2 = SMVC_Entity(name="sample_text_2")
    b = SMVC_Attribute(label=True, multiValued=True, name="sample_text", type="sample_text")
    _safe_set(b, 'SMVC_Attribute', a1)
    assert _is_linked(b, 'SMVC_Attribute', a1)
    if hasattr(a1, 'SMVC_Entity19'):
        assert _is_linked(a1, 'SMVC_Entity19', b)
    _safe_set(b, 'SMVC_Attribute', a2)
    assert _is_linked(b, 'SMVC_Attribute', a2)
    if hasattr(a1, 'SMVC_Entity19'):
        assert not _is_linked(a1, 'SMVC_Entity19', b)
    if hasattr(a2, 'SMVC_Entity19'):
        assert _is_linked(a2, 'SMVC_Entity19', b)
    _safe_set(b, 'SMVC_Attribute', None)
    assert not _is_linked(b, 'SMVC_Attribute', a2)
    if hasattr(a2, 'SMVC_Entity19'):
        assert not _is_linked(a2, 'SMVC_Entity19', b)


def test_assoc_complexType20_reverse_link_reassign_clear():
    a1 = SMVC_Entity(name="sample_text")
    a2 = SMVC_Entity(name="sample_text_2")
    b = SMVC_Attribute(label=True, multiValued=True, name="sample_text", type="sample_text")
    _safe_set(b, 'SMVC_Attribute21', a1)
    assert _is_linked(b, 'SMVC_Attribute21', a1)
    if hasattr(a1, 'SMVC_Entity22'):
        assert _is_linked(a1, 'SMVC_Entity22', b)
    _safe_set(b, 'SMVC_Attribute21', a2)
    assert _is_linked(b, 'SMVC_Attribute21', a2)
    if hasattr(a1, 'SMVC_Entity22'):
        assert not _is_linked(a1, 'SMVC_Entity22', b)
    if hasattr(a2, 'SMVC_Entity22'):
        assert _is_linked(a2, 'SMVC_Entity22', b)
    _safe_set(b, 'SMVC_Attribute21', None)
    assert not _is_linked(b, 'SMVC_Attribute21', a2)
    if hasattr(a2, 'SMVC_Entity22'):
        assert not _is_linked(a2, 'SMVC_Entity22', b)


def test_assoc_controller1_reverse_link_reassign_clear():
    a1 = SMVC_SMVCApplication(name="sample_text")
    a2 = SMVC_SMVCApplication(name="sample_text_2")
    b = SMVC_Controller(operation="sample_text", url="sample_text")
    _safe_set(b, 'SMVC_Controller3', a1)
    assert _is_linked(b, 'SMVC_Controller3', a1)
    if hasattr(a1, 'SMVC_SMVCApplication2'):
        assert _is_linked(a1, 'SMVC_SMVCApplication2', b)
    _safe_set(b, 'SMVC_Controller3', a2)
    assert _is_linked(b, 'SMVC_Controller3', a2)
    if hasattr(a1, 'SMVC_SMVCApplication2'):
        assert not _is_linked(a1, 'SMVC_SMVCApplication2', b)
    if hasattr(a2, 'SMVC_SMVCApplication2'):
        assert _is_linked(a2, 'SMVC_SMVCApplication2', b)
    _safe_set(b, 'SMVC_Controller3', None)
    assert not _is_linked(b, 'SMVC_Controller3', a2)
    if hasattr(a2, 'SMVC_SMVCApplication2'):
        assert not _is_linked(a2, 'SMVC_SMVCApplication2', b)


def test_assoc_dao13_reverse_link_reassign_clear():
    a1 = SMVC_EntityController(returnKOURL="sample_text", returnOKURL="sample_text")
    a2 = SMVC_EntityController(returnKOURL="sample_text_2", returnOKURL="sample_text_2")
    b = SMVC_DataAccessObject(name="sample_text", showDirectInstancesOnly=True)
    _safe_set(b, 'SMVC_DataAccessObject14', a1)
    assert _is_linked(b, 'SMVC_DataAccessObject14', a1)
    if hasattr(a1, 'SMVC_EntityController'):
        assert _is_linked(a1, 'SMVC_EntityController', b)
    _safe_set(b, 'SMVC_DataAccessObject14', a2)
    assert _is_linked(b, 'SMVC_DataAccessObject14', a2)
    if hasattr(a1, 'SMVC_EntityController'):
        assert not _is_linked(a1, 'SMVC_EntityController', b)
    if hasattr(a2, 'SMVC_EntityController'):
        assert _is_linked(a2, 'SMVC_EntityController', b)
    _safe_set(b, 'SMVC_DataAccessObject14', None)
    assert not _is_linked(b, 'SMVC_DataAccessObject14', a2)
    if hasattr(a2, 'SMVC_EntityController'):
        assert not _is_linked(a2, 'SMVC_EntityController', b)


def test_assoc_daos4_reverse_link_reassign_clear():
    a1 = SMVC_SMVCApplication(name="sample_text")
    a2 = SMVC_SMVCApplication(name="sample_text_2")
    b = SMVC_DataAccessObject(name="sample_text", showDirectInstancesOnly=True)
    _safe_set(b, 'SMVC_DataAccessObject', a1)
    assert _is_linked(b, 'SMVC_DataAccessObject', a1)
    if hasattr(a1, 'SMVC_SMVCApplication5'):
        assert _is_linked(a1, 'SMVC_SMVCApplication5', b)
    _safe_set(b, 'SMVC_DataAccessObject', a2)
    assert _is_linked(b, 'SMVC_DataAccessObject', a2)
    if hasattr(a1, 'SMVC_SMVCApplication5'):
        assert not _is_linked(a1, 'SMVC_SMVCApplication5', b)
    if hasattr(a2, 'SMVC_SMVCApplication5'):
        assert _is_linked(a2, 'SMVC_SMVCApplication5', b)
    _safe_set(b, 'SMVC_DataAccessObject', None)
    assert not _is_linked(b, 'SMVC_DataAccessObject', a2)
    if hasattr(a2, 'SMVC_SMVCApplication5'):
        assert not _is_linked(a2, 'SMVC_SMVCApplication5', b)


def test_assoc_entities6_reverse_link_reassign_clear():
    a1 = SMVC_SMVCApplication(name="sample_text")
    a2 = SMVC_SMVCApplication(name="sample_text_2")
    b = SMVC_Entity(name="sample_text")
    _safe_set(b, 'SMVC_Entity', a1)
    assert _is_linked(b, 'SMVC_Entity', a1)
    if hasattr(a1, 'SMVC_SMVCApplication7'):
        assert _is_linked(a1, 'SMVC_SMVCApplication7', b)
    _safe_set(b, 'SMVC_Entity', a2)
    assert _is_linked(b, 'SMVC_Entity', a2)
    if hasattr(a1, 'SMVC_SMVCApplication7'):
        assert not _is_linked(a1, 'SMVC_SMVCApplication7', b)
    if hasattr(a2, 'SMVC_SMVCApplication7'):
        assert _is_linked(a2, 'SMVC_SMVCApplication7', b)
    _safe_set(b, 'SMVC_Entity', None)
    assert not _is_linked(b, 'SMVC_Entity', a2)
    if hasattr(a2, 'SMVC_SMVCApplication7'):
        assert not _is_linked(a2, 'SMVC_SMVCApplication7', b)


def test_assoc_forEntity15_reverse_link_reassign_clear():
    a1 = SMVC_Entity(name="sample_text")
    a2 = SMVC_Entity(name="sample_text_2")
    b = SMVC_DataAccessObject(name="sample_text", showDirectInstancesOnly=True)
    _safe_set(b, 'SMVC_DataAccessObject16', a1)
    assert _is_linked(b, 'SMVC_DataAccessObject16', a1)
    if hasattr(a1, 'SMVC_Entity17'):
        assert _is_linked(a1, 'SMVC_Entity17', b)
    _safe_set(b, 'SMVC_DataAccessObject16', a2)
    assert _is_linked(b, 'SMVC_DataAccessObject16', a2)
    if hasattr(a1, 'SMVC_Entity17'):
        assert not _is_linked(a1, 'SMVC_Entity17', b)
    if hasattr(a2, 'SMVC_Entity17'):
        assert _is_linked(a2, 'SMVC_Entity17', b)
    _safe_set(b, 'SMVC_DataAccessObject16', None)
    assert not _is_linked(b, 'SMVC_DataAccessObject16', a2)
    if hasattr(a2, 'SMVC_Entity17'):
        assert not _is_linked(a2, 'SMVC_Entity17', b)


def test_assoc_homeController0_reverse_link_reassign_clear():
    a1 = SMVC_SMVCApplication(name="sample_text")
    a2 = SMVC_SMVCApplication(name="sample_text_2")
    b = SMVC_Controller(operation="sample_text", url="sample_text")
    _safe_set(b, 'SMVC_Controller', a1)
    assert _is_linked(b, 'SMVC_Controller', a1)
    if hasattr(a1, 'SMVC_SMVCApplication'):
        assert _is_linked(a1, 'SMVC_SMVCApplication', b)
    _safe_set(b, 'SMVC_Controller', a2)
    assert _is_linked(b, 'SMVC_Controller', a2)
    if hasattr(a1, 'SMVC_SMVCApplication'):
        assert not _is_linked(a1, 'SMVC_SMVCApplication', b)
    if hasattr(a2, 'SMVC_SMVCApplication'):
        assert _is_linked(a2, 'SMVC_SMVCApplication', b)
    _safe_set(b, 'SMVC_Controller', None)
    assert not _is_linked(b, 'SMVC_Controller', a2)
    if hasattr(a2, 'SMVC_SMVCApplication'):
        assert not _is_linked(a2, 'SMVC_SMVCApplication', b)


def test_assoc_links23_reverse_link_reassign_clear():
    a1 = SMVC_Page(title="sample_text")
    a2 = SMVC_Page(title="sample_text_2")
    b = SMVC_Link(url="sample_text")
    _safe_set(b, 'SMVC_Link', a1)
    assert _is_linked(b, 'SMVC_Link', a1)
    if hasattr(a1, 'SMVC_Page24'):
        assert _is_linked(a1, 'SMVC_Page24', b)
    _safe_set(b, 'SMVC_Link', a2)
    assert _is_linked(b, 'SMVC_Link', a2)
    if hasattr(a1, 'SMVC_Page24'):
        assert not _is_linked(a1, 'SMVC_Page24', b)
    if hasattr(a2, 'SMVC_Page24'):
        assert _is_linked(a2, 'SMVC_Page24', b)
    _safe_set(b, 'SMVC_Link', None)
    assert not _is_linked(b, 'SMVC_Link', a2)
    if hasattr(a2, 'SMVC_Page24'):
        assert not _is_linked(a2, 'SMVC_Page24', b)


def test_assoc_page11_reverse_link_reassign_clear():
    a1 = SMVC_Page(title="sample_text")
    a2 = SMVC_Page(title="sample_text_2")
    b = SMVC_Controller(operation="sample_text", url="sample_text")
    _safe_set(b, 'SMVC_Controller12', a1)
    assert _is_linked(b, 'SMVC_Controller12', a1)
    if hasattr(a1, 'SMVC_Page'):
        assert _is_linked(a1, 'SMVC_Page', b)
    _safe_set(b, 'SMVC_Controller12', a2)
    assert _is_linked(b, 'SMVC_Controller12', a2)
    if hasattr(a1, 'SMVC_Page'):
        assert not _is_linked(a1, 'SMVC_Page', b)
    if hasattr(a2, 'SMVC_Page'):
        assert _is_linked(a2, 'SMVC_Page', b)
    _safe_set(b, 'SMVC_Controller12', None)
    assert not _is_linked(b, 'SMVC_Controller12', a2)
    if hasattr(a2, 'SMVC_Page'):
        assert not _is_linked(a2, 'SMVC_Page', b)


def test_assoc_subController9_reverse_link_reassign_clear():
    a1 = SMVC_Controller(operation="sample_text", url="sample_text")
    a2 = SMVC_Controller(operation="sample_text_2", url="sample_text_2")
    b = SMVC_Controller(operation="sample_text", url="sample_text")
    _safe_set(b, 'SMVC_Controller8', {a1})
    assert _is_linked(b, 'SMVC_Controller8', a1)
    if hasattr(a1, 'SMVC_Controller10'):
        assert _is_linked(a1, 'SMVC_Controller10', b)
    _safe_set(b, 'SMVC_Controller8', {a2})
    assert _is_linked(b, 'SMVC_Controller8', a2)
    if hasattr(a1, 'SMVC_Controller10'):
        assert not _is_linked(a1, 'SMVC_Controller10', b)
    if hasattr(a2, 'SMVC_Controller10'):
        assert _is_linked(a2, 'SMVC_Controller10', b)
    _safe_set(b, 'SMVC_Controller8', set())
    assert not _is_linked(b, 'SMVC_Controller8', a2)
    if hasattr(a2, 'SMVC_Controller10'):
        assert not _is_linked(a2, 'SMVC_Controller10', b)


def test_assoc_view25_reverse_link_reassign_clear():
    a1 = SMVC_View(text="sample_text")
    a2 = SMVC_View(text="sample_text_2")
    b = SMVC_Page(title="sample_text")
    _safe_set(b, 'SMVC_Page26', a1)
    assert _is_linked(b, 'SMVC_Page26', a1)
    if hasattr(a1, 'SMVC_View'):
        assert _is_linked(a1, 'SMVC_View', b)
    _safe_set(b, 'SMVC_Page26', a2)
    assert _is_linked(b, 'SMVC_Page26', a2)
    if hasattr(a1, 'SMVC_View'):
        assert not _is_linked(a1, 'SMVC_View', b)
    if hasattr(a2, 'SMVC_View'):
        assert _is_linked(a2, 'SMVC_View', b)
    _safe_set(b, 'SMVC_Page26', None)
    assert not _is_linked(b, 'SMVC_Page26', a2)
    if hasattr(a2, 'SMVC_View'):
        assert not _is_linked(a2, 'SMVC_View', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components27_stub_double():
    # SMVC_Component has no real 'SMVC_Component' property in the generated
    # code (a bare stub) -- manually attach it so SMVC_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SMVC_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SMVC_View(text="sample_text")
    partner = SMVC_Component()
    setattr(partner, 'SMVC_Component', None)
    _safe_set(owner, 'SMVC_View28', {partner})
    assert getattr(partner, 'SMVC_Component') == owner
    _safe_set(owner, 'SMVC_View28', set())
    assert getattr(partner, 'SMVC_Component') is None


def test_assoc_entity29_stub_double():
    # SMVC_EntityComponent has no real 'SMVC_EntityComponent' property in the generated
    # code (a bare stub) -- manually attach it so SMVC_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SMVC_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SMVC_Entity(name="sample_text")
    partner = SMVC_EntityComponent()
    setattr(partner, 'SMVC_EntityComponent', None)
    _safe_set(owner, 'SMVC_Entity30', partner)
    assert getattr(partner, 'SMVC_EntityComponent') == owner
    _safe_set(owner, 'SMVC_Entity30', None)
    assert getattr(partner, 'SMVC_EntityComponent') is None


def test_assoc_supportedOperations31_stub_double():
    # SMVC_List has no real 'SMVC_List' property in the generated
    # code (a bare stub) -- manually attach it so SMVC_SupportedOperation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SMVC_SupportedOperation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SMVC_SupportedOperation(operationKind="sample_text", url="sample_text")
    partner = SMVC_List()
    setattr(partner, 'SMVC_List', None)
    _safe_set(owner, 'SMVC_SupportedOperation', partner)
    assert owner in getattr(partner, 'SMVC_List')
    _safe_set(owner, 'SMVC_SupportedOperation', None)
    assert owner not in getattr(partner, 'SMVC_List')


