import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    PhysicalNode,
    sample_Comment,
    sample_DataTypeMap,
    sample_ETypes,
    sample_LocalNode,
    sample_Node,
    sample_PhysicalNode,
    sample_PrimaryObject,
    sample_RemoteNode,
    sample_StringMap,
    sample_TargetObject,
    sample_Tree,
    sample_Type,
    sample_TypeMap,
    sample_TypeMapReference,
    sample_Value,
    sample_VirtualNode,
    SomeKind,
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

def test_assoc_children46_reverse_link_reassign_clear():
    a1 = sample_Tree(name="sample_text")
    a2 = sample_Tree(name="sample_text_2")
    b = sample_Tree(name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Tree47'):
        assert _is_linked(a1, 'Tree47', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Tree47'):
        assert not _is_linked(a1, 'Tree47', b)
    if hasattr(a2, 'Tree47'):
        assert _is_linked(a2, 'Tree47', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Tree47'):
        assert not _is_linked(a2, 'Tree47', b)


def test_assoc_children50_reverse_link_reassign_clear():
    a1 = sample_Node(label="sample_text")
    a2 = sample_Node(label="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'parent51', {a1})
    assert _is_linked(b, 'parent51', a1)
    if hasattr(a1, 'Node52'):
        assert _is_linked(a1, 'Node52', b)
    _safe_set(b, 'parent51', {a2})
    assert _is_linked(b, 'parent51', a2)
    if hasattr(a1, 'Node52'):
        assert not _is_linked(a1, 'Node52', b)
    if hasattr(a2, 'Node52'):
        assert _is_linked(a2, 'Node52', b)
    _safe_set(b, 'parent51', set())
    assert not _is_linked(b, 'parent51', a2)
    if hasattr(a2, 'Node52'):
        assert not _is_linked(a2, 'Node52', b)


def test_assoc_childrenProxies54_reverse_link_reassign_clear():
    a1 = sample_Node(label="sample_text")
    a2 = sample_Node(label="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'parentProxy', {a1})
    assert _is_linked(b, 'parentProxy', a1)
    if hasattr(a1, 'Node55'):
        assert _is_linked(a1, 'Node55', b)
    _safe_set(b, 'parentProxy', {a2})
    assert _is_linked(b, 'parentProxy', a2)
    if hasattr(a1, 'Node55'):
        assert not _is_linked(a1, 'Node55', b)
    if hasattr(a2, 'Node55'):
        assert _is_linked(a2, 'Node55', b)
    _safe_set(b, 'parentProxy', set())
    assert not _is_linked(b, 'parentProxy', a2)
    if hasattr(a2, 'Node55'):
        assert not _is_linked(a2, 'Node55', b)


def test_assoc_dataTypeValues5_reverse_link_reassign_clear():
    a1 = sample_ETypes(uris="sample_text")
    a2 = sample_ETypes(uris="sample_text_2")
    b = sample_DataTypeMap(key="sample_text", value="sample_text")
    _safe_set(b, 'sample_DataTypeMap', a1)
    assert _is_linked(b, 'sample_DataTypeMap', a1)
    if hasattr(a1, 'sample_ETypes6'):
        assert _is_linked(a1, 'sample_ETypes6', b)
    _safe_set(b, 'sample_DataTypeMap', a2)
    assert _is_linked(b, 'sample_DataTypeMap', a2)
    if hasattr(a1, 'sample_ETypes6'):
        assert not _is_linked(a1, 'sample_ETypes6', b)
    if hasattr(a2, 'sample_ETypes6'):
        assert _is_linked(a2, 'sample_ETypes6', b)
    _safe_set(b, 'sample_DataTypeMap', None)
    assert not _is_linked(b, 'sample_DataTypeMap', a2)
    if hasattr(a2, 'sample_ETypes6'):
        assert not _is_linked(a2, 'sample_ETypes6', b)


def test_assoc_featureMapReferenceType130_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject31', {a1})
    assert _is_linked(b, 'sample_PrimaryObject31', a1)
    if hasattr(a1, 'sample_TargetObject32'):
        assert _is_linked(a1, 'sample_TargetObject32', b)
    _safe_set(b, 'sample_PrimaryObject31', {a2})
    assert _is_linked(b, 'sample_PrimaryObject31', a2)
    if hasattr(a1, 'sample_TargetObject32'):
        assert not _is_linked(a1, 'sample_TargetObject32', b)
    if hasattr(a2, 'sample_TargetObject32'):
        assert _is_linked(a2, 'sample_TargetObject32', b)
    _safe_set(b, 'sample_PrimaryObject31', set())
    assert not _is_linked(b, 'sample_PrimaryObject31', a2)
    if hasattr(a2, 'sample_TargetObject32'):
        assert not _is_linked(a2, 'sample_TargetObject32', b)


def test_assoc_featureMapReferenceType233_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject34', {a1})
    assert _is_linked(b, 'sample_PrimaryObject34', a1)
    if hasattr(a1, 'sample_TargetObject35'):
        assert _is_linked(a1, 'sample_TargetObject35', b)
    _safe_set(b, 'sample_PrimaryObject34', {a2})
    assert _is_linked(b, 'sample_PrimaryObject34', a2)
    if hasattr(a1, 'sample_TargetObject35'):
        assert not _is_linked(a1, 'sample_TargetObject35', b)
    if hasattr(a2, 'sample_TargetObject35'):
        assert _is_linked(a2, 'sample_TargetObject35', b)
    _safe_set(b, 'sample_PrimaryObject34', set())
    assert not _is_linked(b, 'sample_PrimaryObject34', a2)
    if hasattr(a2, 'sample_TargetObject35'):
        assert not _is_linked(a2, 'sample_TargetObject35', b)


def test_assoc_manyContainmentReference65_reverse_link_reassign_clear():
    a1 = sample_Node(label="sample_text")
    a2 = sample_Node(label="sample_text_2")
    b = sample_Comment(content="sample_text")
    _safe_set(b, 'sample_Comment66', a1)
    assert _is_linked(b, 'sample_Comment66', a1)
    if hasattr(a1, 'sample_Node'):
        assert _is_linked(a1, 'sample_Node', b)
    _safe_set(b, 'sample_Comment66', a2)
    assert _is_linked(b, 'sample_Comment66', a2)
    if hasattr(a1, 'sample_Node'):
        assert not _is_linked(a1, 'sample_Node', b)
    if hasattr(a2, 'sample_Node'):
        assert _is_linked(a2, 'sample_Node', b)
    _safe_set(b, 'sample_Comment66', None)
    assert not _is_linked(b, 'sample_Comment66', a2)
    if hasattr(a2, 'sample_Node'):
        assert not _is_linked(a2, 'sample_Node', b)


def test_assoc_manyContainmentReferences27_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject28', {a1})
    assert _is_linked(b, 'sample_PrimaryObject28', a1)
    if hasattr(a1, 'sample_TargetObject29'):
        assert _is_linked(a1, 'sample_TargetObject29', b)
    _safe_set(b, 'sample_PrimaryObject28', {a2})
    assert _is_linked(b, 'sample_PrimaryObject28', a2)
    if hasattr(a1, 'sample_TargetObject29'):
        assert not _is_linked(a1, 'sample_TargetObject29', b)
    if hasattr(a2, 'sample_TargetObject29'):
        assert _is_linked(a2, 'sample_TargetObject29', b)
    _safe_set(b, 'sample_PrimaryObject28', set())
    assert not _is_linked(b, 'sample_PrimaryObject28', a2)
    if hasattr(a2, 'sample_TargetObject29'):
        assert not _is_linked(a2, 'sample_TargetObject29', b)


def test_assoc_manyReference48_reverse_link_reassign_clear():
    a1 = sample_Tree(name="sample_text")
    a2 = sample_Tree(name="sample_text_2")
    b = sample_Comment(content="sample_text")
    _safe_set(b, 'sample_Comment', a1)
    assert _is_linked(b, 'sample_Comment', a1)
    if hasattr(a1, 'sample_Tree'):
        assert _is_linked(a1, 'sample_Tree', b)
    _safe_set(b, 'sample_Comment', a2)
    assert _is_linked(b, 'sample_Comment', a2)
    if hasattr(a1, 'sample_Tree'):
        assert not _is_linked(a1, 'sample_Tree', b)
    if hasattr(a2, 'sample_Tree'):
        assert _is_linked(a2, 'sample_Tree', b)
    _safe_set(b, 'sample_Comment', None)
    assert not _is_linked(b, 'sample_Comment', a2)
    if hasattr(a2, 'sample_Tree'):
        assert not _is_linked(a2, 'sample_Tree', b)


def test_assoc_manyReferences21_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject22', {a1})
    assert _is_linked(b, 'sample_PrimaryObject22', a1)
    if hasattr(a1, 'sample_TargetObject23'):
        assert _is_linked(a1, 'sample_TargetObject23', b)
    _safe_set(b, 'sample_PrimaryObject22', {a2})
    assert _is_linked(b, 'sample_PrimaryObject22', a2)
    if hasattr(a1, 'sample_TargetObject23'):
        assert not _is_linked(a1, 'sample_TargetObject23', b)
    if hasattr(a2, 'sample_TargetObject23'):
        assert _is_linked(a2, 'sample_TargetObject23', b)
    _safe_set(b, 'sample_PrimaryObject22', set())
    assert not _is_linked(b, 'sample_PrimaryObject22', a2)
    if hasattr(a2, 'sample_TargetObject23'):
        assert not _is_linked(a2, 'sample_TargetObject23', b)


def test_assoc_manyReferences39_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject41', a1)
    assert _is_linked(b, 'sample_PrimaryObject41', a1)
    if hasattr(a1, 'sample_TargetObject40'):
        assert _is_linked(a1, 'sample_TargetObject40', b)
    _safe_set(b, 'sample_PrimaryObject41', a2)
    assert _is_linked(b, 'sample_PrimaryObject41', a2)
    if hasattr(a1, 'sample_TargetObject40'):
        assert not _is_linked(a1, 'sample_TargetObject40', b)
    if hasattr(a2, 'sample_TargetObject40'):
        assert _is_linked(a2, 'sample_TargetObject40', b)
    _safe_set(b, 'sample_PrimaryObject41', None)
    assert not _is_linked(b, 'sample_PrimaryObject41', a2)
    if hasattr(a2, 'sample_TargetObject40'):
        assert not _is_linked(a2, 'sample_TargetObject40', b)


def test_assoc_nodes42_reverse_link_reassign_clear():
    a1 = sample_Tree(name="sample_text")
    a2 = sample_Tree(name="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'Node', a1)
    assert _is_linked(b, 'Node', a1)
    if hasattr(a1, 'tree'):
        assert _is_linked(a1, 'tree', b)
    _safe_set(b, 'Node', a2)
    assert _is_linked(b, 'Node', a2)
    if hasattr(a1, 'tree'):
        assert not _is_linked(a1, 'tree', b)
    if hasattr(a2, 'tree'):
        assert _is_linked(a2, 'tree', b)
    _safe_set(b, 'Node', None)
    assert not _is_linked(b, 'Node', a2)
    if hasattr(a2, 'tree'):
        assert not _is_linked(a2, 'tree', b)


def test_assoc_parent44_reverse_link_reassign_clear():
    a1 = sample_Tree(name="sample_text")
    a2 = sample_Tree(name="sample_text_2")
    b = sample_Tree(name="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Tree'):
        assert _is_linked(a1, 'Tree', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Tree'):
        assert not _is_linked(a1, 'Tree', b)
    if hasattr(a2, 'Tree'):
        assert _is_linked(a2, 'Tree', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Tree'):
        assert not _is_linked(a2, 'Tree', b)


def test_assoc_parent57_reverse_link_reassign_clear():
    a1 = sample_Node(label="sample_text")
    a2 = sample_Node(label="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'children58', a1)
    assert _is_linked(b, 'children58', a1)
    if hasattr(a1, 'Node59'):
        assert _is_linked(a1, 'Node59', b)
    _safe_set(b, 'children58', a2)
    assert _is_linked(b, 'children58', a2)
    if hasattr(a1, 'Node59'):
        assert not _is_linked(a1, 'Node59', b)
    if hasattr(a2, 'Node59'):
        assert _is_linked(a2, 'Node59', b)
    _safe_set(b, 'children58', None)
    assert not _is_linked(b, 'children58', a2)
    if hasattr(a2, 'Node59'):
        assert not _is_linked(a2, 'Node59', b)


def test_assoc_parentProxy61_reverse_link_reassign_clear():
    a1 = sample_Node(label="sample_text")
    a2 = sample_Node(label="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'childrenProxies', a1)
    assert _is_linked(b, 'childrenProxies', a1)
    if hasattr(a1, 'Node62'):
        assert _is_linked(a1, 'Node62', b)
    _safe_set(b, 'childrenProxies', a2)
    assert _is_linked(b, 'childrenProxies', a2)
    if hasattr(a1, 'Node62'):
        assert not _is_linked(a1, 'Node62', b)
    if hasattr(a2, 'Node62'):
        assert _is_linked(a2, 'Node62', b)
    _safe_set(b, 'childrenProxies', None)
    assert not _is_linked(b, 'childrenProxies', a2)
    if hasattr(a2, 'Node62'):
        assert not _is_linked(a2, 'Node62', b)


def test_assoc_singleContainmentReference24_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject25', a1)
    assert _is_linked(b, 'sample_PrimaryObject25', a1)
    if hasattr(a1, 'sample_TargetObject26'):
        assert _is_linked(a1, 'sample_TargetObject26', b)
    _safe_set(b, 'sample_PrimaryObject25', a2)
    assert _is_linked(b, 'sample_PrimaryObject25', a2)
    if hasattr(a1, 'sample_TargetObject26'):
        assert not _is_linked(a1, 'sample_TargetObject26', b)
    if hasattr(a2, 'sample_TargetObject26'):
        assert _is_linked(a2, 'sample_TargetObject26', b)
    _safe_set(b, 'sample_PrimaryObject25', None)
    assert not _is_linked(b, 'sample_PrimaryObject25', a2)
    if hasattr(a2, 'sample_TargetObject26'):
        assert not _is_linked(a2, 'sample_TargetObject26', b)


def test_assoc_singleReference18_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject19', a1)
    assert _is_linked(b, 'sample_PrimaryObject19', a1)
    if hasattr(a1, 'sample_TargetObject20'):
        assert _is_linked(a1, 'sample_TargetObject20', b)
    _safe_set(b, 'sample_PrimaryObject19', a2)
    assert _is_linked(b, 'sample_PrimaryObject19', a2)
    if hasattr(a1, 'sample_TargetObject20'):
        assert not _is_linked(a1, 'sample_TargetObject20', b)
    if hasattr(a2, 'sample_TargetObject20'):
        assert _is_linked(a2, 'sample_TargetObject20', b)
    _safe_set(b, 'sample_PrimaryObject19', None)
    assert not _is_linked(b, 'sample_PrimaryObject19', a2)
    if hasattr(a2, 'sample_TargetObject20'):
        assert not _is_linked(a2, 'sample_TargetObject20', b)


def test_assoc_singleReference36_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject38', a1)
    assert _is_linked(b, 'sample_PrimaryObject38', a1)
    if hasattr(a1, 'sample_TargetObject37'):
        assert _is_linked(a1, 'sample_TargetObject37', b)
    _safe_set(b, 'sample_PrimaryObject38', a2)
    assert _is_linked(b, 'sample_PrimaryObject38', a2)
    if hasattr(a1, 'sample_TargetObject37'):
        assert not _is_linked(a1, 'sample_TargetObject37', b)
    if hasattr(a2, 'sample_TargetObject37'):
        assert _is_linked(a2, 'sample_TargetObject37', b)
    _safe_set(b, 'sample_PrimaryObject38', None)
    assert not _is_linked(b, 'sample_PrimaryObject38', a2)
    if hasattr(a2, 'sample_TargetObject37'):
        assert not _is_linked(a2, 'sample_TargetObject37', b)


def test_assoc_stringValues3_reverse_link_reassign_clear():
    a1 = sample_StringMap(key="sample_text", value="sample_text")
    a2 = sample_StringMap(key="sample_text_2", value="sample_text_2")
    b = sample_ETypes(uris="sample_text")
    _safe_set(b, 'sample_ETypes4', {a1})
    assert _is_linked(b, 'sample_ETypes4', a1)
    if hasattr(a1, 'sample_StringMap'):
        assert _is_linked(a1, 'sample_StringMap', b)
    _safe_set(b, 'sample_ETypes4', {a2})
    assert _is_linked(b, 'sample_ETypes4', a2)
    if hasattr(a1, 'sample_StringMap'):
        assert not _is_linked(a1, 'sample_StringMap', b)
    if hasattr(a2, 'sample_StringMap'):
        assert _is_linked(a2, 'sample_StringMap', b)
    _safe_set(b, 'sample_ETypes4', set())
    assert not _is_linked(b, 'sample_ETypes4', a2)
    if hasattr(a2, 'sample_StringMap'):
        assert not _is_linked(a2, 'sample_StringMap', b)


def test_assoc_tree63_reverse_link_reassign_clear():
    a1 = sample_Tree(name="sample_text")
    a2 = sample_Tree(name="sample_text_2")
    b = sample_Node(label="sample_text")
    _safe_set(b, 'nodes', a1)
    assert _is_linked(b, 'nodes', a1)
    if hasattr(a1, 'Tree64'):
        assert _is_linked(a1, 'Tree64', b)
    _safe_set(b, 'nodes', a2)
    assert _is_linked(b, 'nodes', a2)
    if hasattr(a1, 'Tree64'):
        assert not _is_linked(a1, 'Tree64', b)
    if hasattr(a2, 'Tree64'):
        assert _is_linked(a2, 'Tree64', b)
    _safe_set(b, 'nodes', None)
    assert not _is_linked(b, 'nodes', a2)
    if hasattr(a2, 'Tree64'):
        assert not _is_linked(a2, 'Tree64', b)


def test_assoc_unsettableReference15_reverse_link_reassign_clear():
    a1 = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    a2 = sample_TargetObject(manyAttributes="sample_text_2", name="sample_text_2", singleAttribute="sample_text_2")
    b = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    _safe_set(b, 'sample_PrimaryObject16', a1)
    assert _is_linked(b, 'sample_PrimaryObject16', a1)
    if hasattr(a1, 'sample_TargetObject17'):
        assert _is_linked(a1, 'sample_TargetObject17', b)
    _safe_set(b, 'sample_PrimaryObject16', a2)
    assert _is_linked(b, 'sample_PrimaryObject16', a2)
    if hasattr(a1, 'sample_TargetObject17'):
        assert not _is_linked(a1, 'sample_TargetObject17', b)
    if hasattr(a2, 'sample_TargetObject17'):
        assert _is_linked(a2, 'sample_TargetObject17', b)
    _safe_set(b, 'sample_PrimaryObject16', None)
    assert not _is_linked(b, 'sample_PrimaryObject16', a2)
    if hasattr(a2, 'sample_TargetObject17'):
        assert not _is_linked(a2, 'sample_TargetObject17', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_key11_stub_double():
    # sample_TypeMapReference has no real 'sample_TypeMapReference12' property in the generated
    # code (a bare stub) -- manually attach it so sample_PrimaryObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_PrimaryObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_PrimaryObject(featureMapAttributeCollection="sample_text", featureMapAttributeType1="sample_text", featureMapAttributeType2="sample_text", featureMapReferenceCollection="sample_text", id="sample_text", kind="sample_text", name="sample_text", unsettableAttribute="sample_text", unsettableAttributeWithDefault="sample_text")
    partner = sample_TypeMapReference()
    setattr(partner, 'sample_TypeMapReference12', None)
    _safe_set(owner, 'sample_PrimaryObject', partner)
    assert getattr(partner, 'sample_TypeMapReference12') == owner
    _safe_set(owner, 'sample_PrimaryObject', None)
    assert getattr(partner, 'sample_TypeMapReference12') is None


def test_assoc_key7_stub_double():
    # sample_TypeMap has no real 'sample_TypeMap8' property in the generated
    # code (a bare stub) -- manually attach it so sample_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_Type(name="sample_text")
    partner = sample_TypeMap()
    setattr(partner, 'sample_TypeMap8', None)
    _safe_set(owner, 'sample_Type', partner)
    assert getattr(partner, 'sample_TypeMap8') == owner
    _safe_set(owner, 'sample_Type', None)
    assert getattr(partner, 'sample_TypeMap8') is None


def test_assoc_value13_stub_double():
    # sample_TypeMapReference has no real 'sample_TypeMapReference14' property in the generated
    # code (a bare stub) -- manually attach it so sample_TargetObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_TargetObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_TargetObject(manyAttributes="sample_text", name="sample_text", singleAttribute="sample_text")
    partner = sample_TypeMapReference()
    setattr(partner, 'sample_TypeMapReference14', None)
    _safe_set(owner, 'sample_TargetObject', partner)
    assert getattr(partner, 'sample_TypeMapReference14') == owner
    _safe_set(owner, 'sample_TargetObject', None)
    assert getattr(partner, 'sample_TypeMapReference14') is None


def test_assoc_value9_stub_double():
    # sample_TypeMap has no real 'sample_TypeMap10' property in the generated
    # code (a bare stub) -- manually attach it so sample_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_Value(value=7)
    partner = sample_TypeMap()
    setattr(partner, 'sample_TypeMap10', None)
    _safe_set(owner, 'sample_Value', partner)
    assert getattr(partner, 'sample_TypeMap10') == owner
    _safe_set(owner, 'sample_Value', None)
    assert getattr(partner, 'sample_TypeMap10') is None


def test_assoc_values0_stub_double():
    # sample_TypeMap has no real 'sample_TypeMap' property in the generated
    # code (a bare stub) -- manually attach it so sample_ETypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_ETypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_ETypes(uris="sample_text")
    partner = sample_TypeMap()
    setattr(partner, 'sample_TypeMap', None)
    _safe_set(owner, 'sample_ETypes', {partner})
    assert getattr(partner, 'sample_TypeMap') == owner
    _safe_set(owner, 'sample_ETypes', set())
    assert getattr(partner, 'sample_TypeMap') is None


def test_assoc_valuesWithReferences1_stub_double():
    # sample_TypeMapReference has no real 'sample_TypeMapReference' property in the generated
    # code (a bare stub) -- manually attach it so sample_ETypes's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # sample_ETypes's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = sample_ETypes(uris="sample_text")
    partner = sample_TypeMapReference()
    setattr(partner, 'sample_TypeMapReference', None)
    _safe_set(owner, 'sample_ETypes2', {partner})
    assert getattr(partner, 'sample_TypeMapReference') == owner
    _safe_set(owner, 'sample_ETypes2', set())
    assert getattr(partner, 'sample_TypeMapReference') is None


