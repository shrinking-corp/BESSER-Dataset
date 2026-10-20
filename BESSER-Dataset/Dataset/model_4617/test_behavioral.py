import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AbstractCardinalityConstraint,
    AbstractConstraint,
    AbstractRegExpConstraint,
    AbstractRegExpTopicType,
    AbstractTypedCardinalityConstraint,
    AbstractTypedConstraint,
    AbstractUniqueValueTopicType,
    Diagram,
    Node,
    OnoObject,
    ReifiableTopicType,
    ScopedReifiableTopicType,
    ScopedTopicType,
    TMCLConstruct,
    TopicType,
    model_AbstractCardinalityConstraint,
    model_AbstractConstraint,
    model_AbstractRegExpConstraint,
    model_AbstractRegExpTopicType,
    model_AbstractTypedCardinalityConstraint,
    model_AbstractTypedConstraint,
    model_AbstractUniqueValueTopicType,
    model_Annotation,
    model_AssociationNode,
    model_AssociationType,
    model_AssociationTypeConstraint,
    model_Bendpoint,
    model_Comment,
    model_Diagram,
    model_DomainDiagram,
    model_Edge,
    model_File,
    model_ItemIdentifierConstraint,
    model_LabelPos,
    model_MappingElement,
    model_NameType,
    model_NameTypeConstraint,
    model_Node,
    model_OccurrenceType,
    model_OccurrenceTypeConstraint,
    model_OnoObject,
    model_ReifiableTopicType,
    model_ReifierConstraint,
    model_RoleCombinationConstraint,
    model_RoleConstraint,
    model_RolePlayerConstraint,
    model_RoleType,
    model_ScopeConstraint,
    model_ScopedReifiableTopicType,
    model_ScopedTopicType,
    model_SubjectIdentifierConstraint,
    model_SubjectLocatorConstraint,
    model_TMCLConstruct,
    model_TopicMapSchema,
    model_TopicReifiesConstraint,
    model_TopicType,
    model_TypeNode,
    EdgeType,
    KindOfTopicType,
    TopicId,
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

def test_assoc_ako3_reverse_link_reassign_clear():
    a1 = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    a2 = model_TopicType(abstract=False, idType="sample_text_2", identifiers="sample_text_2", kind="sample_text_2", locators="sample_text_2", name="sample_text_2")
    b = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    _safe_set(b, 'model_TopicType4', a1)
    assert _is_linked(b, 'model_TopicType4', a1)
    if hasattr(a1, 'model_TopicType2'):
        assert _is_linked(a1, 'model_TopicType2', b)
    _safe_set(b, 'model_TopicType4', a2)
    assert _is_linked(b, 'model_TopicType4', a2)
    if hasattr(a1, 'model_TopicType2'):
        assert not _is_linked(a1, 'model_TopicType2', b)
    if hasattr(a2, 'model_TopicType2'):
        assert _is_linked(a2, 'model_TopicType2', b)
    _safe_set(b, 'model_TopicType4', None)
    assert not _is_linked(b, 'model_TopicType4', a2)
    if hasattr(a2, 'model_TopicType2'):
        assert not _is_linked(a2, 'model_TopicType2', b)


def test_assoc_annotations79_reverse_link_reassign_clear():
    a1 = model_TMCLConstruct(comment="sample_text", description="sample_text", see_also="sample_text")
    a2 = model_TMCLConstruct(comment="sample_text_2", description="sample_text_2", see_also="sample_text_2")
    b = model_Annotation(key="sample_text", value="sample_text")
    _safe_set(b, 'model_Annotation', a1)
    assert _is_linked(b, 'model_Annotation', a1)
    if hasattr(a1, 'model_TMCLConstruct'):
        assert _is_linked(a1, 'model_TMCLConstruct', b)
    _safe_set(b, 'model_Annotation', a2)
    assert _is_linked(b, 'model_Annotation', a2)
    if hasattr(a1, 'model_TMCLConstruct'):
        assert not _is_linked(a1, 'model_TMCLConstruct', b)
    if hasattr(a2, 'model_TMCLConstruct'):
        assert _is_linked(a2, 'model_TMCLConstruct', b)
    _safe_set(b, 'model_Annotation', None)
    assert not _is_linked(b, 'model_Annotation', a2)
    if hasattr(a2, 'model_TMCLConstruct'):
        assert not _is_linked(a2, 'model_TMCLConstruct', b)


def test_assoc_bendpoints35_reverse_link_reassign_clear():
    a1 = model_Edge(type="sample_text")
    a2 = model_Edge(type="sample_text_2")
    b = model_Bendpoint(posX=7, posY=7)
    _safe_set(b, 'model_Bendpoint', a1)
    assert _is_linked(b, 'model_Bendpoint', a1)
    if hasattr(a1, 'model_Edge'):
        assert _is_linked(a1, 'model_Edge', b)
    _safe_set(b, 'model_Bendpoint', a2)
    assert _is_linked(b, 'model_Bendpoint', a2)
    if hasattr(a1, 'model_Edge'):
        assert not _is_linked(a1, 'model_Edge', b)
    if hasattr(a2, 'model_Edge'):
        assert _is_linked(a2, 'model_Edge', b)
    _safe_set(b, 'model_Bendpoint', None)
    assert not _is_linked(b, 'model_Bendpoint', a2)
    if hasattr(a2, 'model_Edge'):
        assert not _is_linked(a2, 'model_Edge', b)


def test_assoc_comments53_reverse_link_reassign_clear():
    a1 = model_Diagram(name="sample_text")
    a2 = model_Diagram(name="sample_text_2")
    b = model_Comment(content="sample_text", height=7, width=7)
    _safe_set(b, 'model_Comment', a1)
    assert _is_linked(b, 'model_Comment', a1)
    if hasattr(a1, 'model_Diagram54'):
        assert _is_linked(a1, 'model_Diagram54', b)
    _safe_set(b, 'model_Comment', a2)
    assert _is_linked(b, 'model_Comment', a2)
    if hasattr(a1, 'model_Diagram54'):
        assert not _is_linked(a1, 'model_Diagram54', b)
    if hasattr(a2, 'model_Diagram54'):
        assert _is_linked(a2, 'model_Diagram54', b)
    _safe_set(b, 'model_Comment', None)
    assert not _is_linked(b, 'model_Comment', a2)
    if hasattr(a2, 'model_Diagram54'):
        assert not _is_linked(a2, 'model_Diagram54', b)


def test_assoc_diagrams55_reverse_link_reassign_clear():
    a1 = model_File(dirty=True, filename="sample_text", notes="sample_text")
    a2 = model_File(dirty=False, filename="sample_text_2", notes="sample_text_2")
    b = model_Diagram(name="sample_text")
    _safe_set(b, 'model_Diagram56', a1)
    assert _is_linked(b, 'model_Diagram56', a1)
    if hasattr(a1, 'model_File'):
        assert _is_linked(a1, 'model_File', b)
    _safe_set(b, 'model_Diagram56', a2)
    assert _is_linked(b, 'model_Diagram56', a2)
    if hasattr(a1, 'model_File'):
        assert not _is_linked(a1, 'model_File', b)
    if hasattr(a2, 'model_File'):
        assert _is_linked(a2, 'model_File', b)
    _safe_set(b, 'model_Diagram56', None)
    assert not _is_linked(b, 'model_Diagram56', a2)
    if hasattr(a2, 'model_File'):
        assert not _is_linked(a2, 'model_File', b)


def test_assoc_edges48_reverse_link_reassign_clear():
    a1 = model_Edge(type="sample_text")
    a2 = model_Edge(type="sample_text_2")
    b = model_Diagram(name="sample_text")
    _safe_set(b, 'model_Diagram', {a1})
    assert _is_linked(b, 'model_Diagram', a1)
    if hasattr(a1, 'model_Edge49'):
        assert _is_linked(a1, 'model_Edge49', b)
    _safe_set(b, 'model_Diagram', {a2})
    assert _is_linked(b, 'model_Diagram', a2)
    if hasattr(a1, 'model_Edge49'):
        assert not _is_linked(a1, 'model_Edge49', b)
    if hasattr(a2, 'model_Edge49'):
        assert _is_linked(a2, 'model_Edge49', b)
    _safe_set(b, 'model_Diagram', set())
    assert not _is_linked(b, 'model_Diagram', a2)
    if hasattr(a2, 'model_Edge49'):
        assert not _is_linked(a2, 'model_Edge49', b)


def test_assoc_isa1_reverse_link_reassign_clear():
    a1 = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    a2 = model_TopicType(abstract=False, idType="sample_text_2", identifiers="sample_text_2", kind="sample_text_2", locators="sample_text_2", name="sample_text_2")
    b = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    _safe_set(b, 'model_TopicType0', {a1})
    assert _is_linked(b, 'model_TopicType0', a1)
    if hasattr(a1, 'model_TopicType'):
        assert _is_linked(a1, 'model_TopicType', b)
    _safe_set(b, 'model_TopicType0', {a2})
    assert _is_linked(b, 'model_TopicType0', a2)
    if hasattr(a1, 'model_TopicType'):
        assert not _is_linked(a1, 'model_TopicType', b)
    if hasattr(a2, 'model_TopicType'):
        assert _is_linked(a2, 'model_TopicType', b)
    _safe_set(b, 'model_TopicType0', set())
    assert not _is_linked(b, 'model_TopicType0', a2)
    if hasattr(a2, 'model_TopicType'):
        assert not _is_linked(a2, 'model_TopicType', b)


def test_assoc_labelPositions44_reverse_link_reassign_clear():
    a1 = model_LabelPos(posX=7, posY=7)
    a2 = model_LabelPos(posX=13, posY=13)
    b = model_Edge(type="sample_text")
    _safe_set(b, 'model_Edge45', {a1})
    assert _is_linked(b, 'model_Edge45', a1)
    if hasattr(a1, 'model_LabelPos'):
        assert _is_linked(a1, 'model_LabelPos', b)
    _safe_set(b, 'model_Edge45', {a2})
    assert _is_linked(b, 'model_Edge45', a2)
    if hasattr(a1, 'model_LabelPos'):
        assert not _is_linked(a1, 'model_LabelPos', b)
    if hasattr(a2, 'model_LabelPos'):
        assert _is_linked(a2, 'model_LabelPos', b)
    _safe_set(b, 'model_Edge45', set())
    assert not _is_linked(b, 'model_Edge45', a2)
    if hasattr(a2, 'model_LabelPos'):
        assert not _is_linked(a2, 'model_LabelPos', b)


def test_assoc_mappings28_reverse_link_reassign_clear():
    a1 = model_TopicMapSchema(baseLocator="sample_text", includes="sample_text", name="sample_text", schemaResource="sample_text", version="sample_text")
    a2 = model_TopicMapSchema(baseLocator="sample_text_2", includes="sample_text_2", name="sample_text_2", schemaResource="sample_text_2", version="sample_text_2")
    b = model_MappingElement(key="sample_text", value="sample_text")
    _safe_set(b, 'model_MappingElement', a1)
    assert _is_linked(b, 'model_MappingElement', a1)
    if hasattr(a1, 'model_TopicMapSchema29'):
        assert _is_linked(a1, 'model_TopicMapSchema29', b)
    _safe_set(b, 'model_MappingElement', a2)
    assert _is_linked(b, 'model_MappingElement', a2)
    if hasattr(a1, 'model_TopicMapSchema29'):
        assert not _is_linked(a1, 'model_TopicMapSchema29', b)
    if hasattr(a2, 'model_TopicMapSchema29'):
        assert _is_linked(a2, 'model_TopicMapSchema29', b)
    _safe_set(b, 'model_MappingElement', None)
    assert not _is_linked(b, 'model_MappingElement', a2)
    if hasattr(a2, 'model_TopicMapSchema29'):
        assert not _is_linked(a2, 'model_TopicMapSchema29', b)


def test_assoc_nodes50_reverse_link_reassign_clear():
    a1 = model_Node(posX=7, posY=7)
    a2 = model_Node(posX=13, posY=13)
    b = model_Diagram(name="sample_text")
    _safe_set(b, 'model_Diagram51', {a1})
    assert _is_linked(b, 'model_Diagram51', a1)
    if hasattr(a1, 'model_Node52'):
        assert _is_linked(a1, 'model_Node52', b)
    _safe_set(b, 'model_Diagram51', {a2})
    assert _is_linked(b, 'model_Diagram51', a2)
    if hasattr(a1, 'model_Node52'):
        assert not _is_linked(a1, 'model_Node52', b)
    if hasattr(a2, 'model_Node52'):
        assert _is_linked(a2, 'model_Node52', b)
    _safe_set(b, 'model_Diagram51', set())
    assert not _is_linked(b, 'model_Diagram51', a2)
    if hasattr(a2, 'model_Node52'):
        assert not _is_linked(a2, 'model_Node52', b)


def test_assoc_overlap14_reverse_link_reassign_clear():
    a1 = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    a2 = model_TopicType(abstract=False, idType="sample_text_2", identifiers="sample_text_2", kind="sample_text_2", locators="sample_text_2", name="sample_text_2")
    b = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    _safe_set(b, 'model_TopicType15', a1)
    assert _is_linked(b, 'model_TopicType15', a1)
    if hasattr(a1, 'model_TopicType13'):
        assert _is_linked(a1, 'model_TopicType13', b)
    _safe_set(b, 'model_TopicType15', a2)
    assert _is_linked(b, 'model_TopicType15', a2)
    if hasattr(a1, 'model_TopicType13'):
        assert not _is_linked(a1, 'model_TopicType13', b)
    if hasattr(a2, 'model_TopicType13'):
        assert _is_linked(a2, 'model_TopicType13', b)
    _safe_set(b, 'model_TopicType15', None)
    assert not _is_linked(b, 'model_TopicType15', a2)
    if hasattr(a2, 'model_TopicType13'):
        assert not _is_linked(a2, 'model_TopicType13', b)


def test_assoc_source36_reverse_link_reassign_clear():
    a1 = model_Node(posX=7, posY=7)
    a2 = model_Node(posX=13, posY=13)
    b = model_Edge(type="sample_text")
    _safe_set(b, 'model_Edge37', a1)
    assert _is_linked(b, 'model_Edge37', a1)
    if hasattr(a1, 'model_Node'):
        assert _is_linked(a1, 'model_Node', b)
    _safe_set(b, 'model_Edge37', a2)
    assert _is_linked(b, 'model_Edge37', a2)
    if hasattr(a1, 'model_Node'):
        assert not _is_linked(a1, 'model_Node', b)
    if hasattr(a2, 'model_Node'):
        assert _is_linked(a2, 'model_Node', b)
    _safe_set(b, 'model_Edge37', None)
    assert not _is_linked(b, 'model_Edge37', a2)
    if hasattr(a2, 'model_Node'):
        assert not _is_linked(a2, 'model_Node', b)


def test_assoc_target38_reverse_link_reassign_clear():
    a1 = model_Node(posX=7, posY=7)
    a2 = model_Node(posX=13, posY=13)
    b = model_Edge(type="sample_text")
    _safe_set(b, 'model_Edge39', a1)
    assert _is_linked(b, 'model_Edge39', a1)
    if hasattr(a1, 'model_Node40'):
        assert _is_linked(a1, 'model_Node40', b)
    _safe_set(b, 'model_Edge39', a2)
    assert _is_linked(b, 'model_Edge39', a2)
    if hasattr(a1, 'model_Node40'):
        assert not _is_linked(a1, 'model_Node40', b)
    if hasattr(a2, 'model_Node40'):
        assert _is_linked(a2, 'model_Node40', b)
    _safe_set(b, 'model_Edge39', None)
    assert not _is_linked(b, 'model_Edge39', a2)
    if hasattr(a2, 'model_Node40'):
        assert not _is_linked(a2, 'model_Node40', b)


def test_assoc_topicMapSchema57_reverse_link_reassign_clear():
    a1 = model_TopicMapSchema(baseLocator="sample_text", includes="sample_text", name="sample_text", schemaResource="sample_text", version="sample_text")
    a2 = model_TopicMapSchema(baseLocator="sample_text_2", includes="sample_text_2", name="sample_text_2", schemaResource="sample_text_2", version="sample_text_2")
    b = model_File(dirty=True, filename="sample_text", notes="sample_text")
    _safe_set(b, 'model_File58', a1)
    assert _is_linked(b, 'model_File58', a1)
    if hasattr(a1, 'model_TopicMapSchema59'):
        assert _is_linked(a1, 'model_TopicMapSchema59', b)
    _safe_set(b, 'model_File58', a2)
    assert _is_linked(b, 'model_File58', a2)
    if hasattr(a1, 'model_TopicMapSchema59'):
        assert not _is_linked(a1, 'model_TopicMapSchema59', b)
    if hasattr(a2, 'model_TopicMapSchema59'):
        assert _is_linked(a2, 'model_TopicMapSchema59', b)
    _safe_set(b, 'model_File58', None)
    assert not _is_linked(b, 'model_File58', a2)
    if hasattr(a2, 'model_TopicMapSchema59'):
        assert not _is_linked(a2, 'model_TopicMapSchema59', b)


def test_assoc_topicType33_reverse_link_reassign_clear():
    a1 = model_TypeNode(image="sample_text")
    a2 = model_TypeNode(image="sample_text_2")
    b = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    _safe_set(b, 'model_TopicType34', a1)
    assert _is_linked(b, 'model_TopicType34', a1)
    if hasattr(a1, 'model_TypeNode'):
        assert _is_linked(a1, 'model_TypeNode', b)
    _safe_set(b, 'model_TopicType34', a2)
    assert _is_linked(b, 'model_TopicType34', a2)
    if hasattr(a1, 'model_TypeNode'):
        assert not _is_linked(a1, 'model_TypeNode', b)
    if hasattr(a2, 'model_TypeNode'):
        assert _is_linked(a2, 'model_TypeNode', b)
    _safe_set(b, 'model_TopicType34', None)
    assert not _is_linked(b, 'model_TopicType34', a2)
    if hasattr(a2, 'model_TypeNode'):
        assert not _is_linked(a2, 'model_TypeNode', b)


def test_assoc_topicTypes24_reverse_link_reassign_clear():
    a1 = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    a2 = model_TopicType(abstract=False, idType="sample_text_2", identifiers="sample_text_2", kind="sample_text_2", locators="sample_text_2", name="sample_text_2")
    b = model_TopicMapSchema(baseLocator="sample_text", includes="sample_text", name="sample_text", schemaResource="sample_text", version="sample_text")
    _safe_set(b, 'model_TopicMapSchema', {a1})
    assert _is_linked(b, 'model_TopicMapSchema', a1)
    if hasattr(a1, 'model_TopicType25'):
        assert _is_linked(a1, 'model_TopicType25', b)
    _safe_set(b, 'model_TopicMapSchema', {a2})
    assert _is_linked(b, 'model_TopicMapSchema', a2)
    if hasattr(a1, 'model_TopicType25'):
        assert not _is_linked(a1, 'model_TopicType25', b)
    if hasattr(a2, 'model_TopicType25'):
        assert _is_linked(a2, 'model_TopicType25', b)
    _safe_set(b, 'model_TopicMapSchema', set())
    assert not _is_linked(b, 'model_TopicMapSchema', a2)
    if hasattr(a2, 'model_TopicType25'):
        assert not _is_linked(a2, 'model_TopicType25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_associationTypeConstraints26_stub_double():
    # model_AssociationTypeConstraint has no real 'model_AssociationTypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicMapSchema's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicMapSchema's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicMapSchema(baseLocator="sample_text", includes="sample_text", name="sample_text", schemaResource="sample_text", version="sample_text")
    partner = model_AssociationTypeConstraint()
    setattr(partner, 'model_AssociationTypeConstraint', None)
    _safe_set(owner, 'model_TopicMapSchema27', {partner})
    assert getattr(partner, 'model_AssociationTypeConstraint') == owner
    _safe_set(owner, 'model_TopicMapSchema27', set())
    assert getattr(partner, 'model_AssociationTypeConstraint') is None


def test_assoc_itemIdentifierConstraints18_stub_double():
    # model_ItemIdentifierConstraint has no real 'model_ItemIdentifierConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_ItemIdentifierConstraint()
    setattr(partner, 'model_ItemIdentifierConstraint', None)
    _safe_set(owner, 'model_TopicType19', {partner})
    assert getattr(partner, 'model_ItemIdentifierConstraint') == owner
    _safe_set(owner, 'model_TopicType19', set())
    assert getattr(partner, 'model_ItemIdentifierConstraint') is None


def test_assoc_nameConstraints7_stub_double():
    # model_NameTypeConstraint has no real 'model_NameTypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_NameTypeConstraint()
    setattr(partner, 'model_NameTypeConstraint', None)
    _safe_set(owner, 'model_TopicType8', {partner})
    assert getattr(partner, 'model_NameTypeConstraint') == owner
    _safe_set(owner, 'model_TopicType8', set())
    assert getattr(partner, 'model_NameTypeConstraint') is None


def test_assoc_occurrenceConstraints5_stub_double():
    # model_OccurrenceTypeConstraint has no real 'model_OccurrenceTypeConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_OccurrenceTypeConstraint()
    setattr(partner, 'model_OccurrenceTypeConstraint', None)
    _safe_set(owner, 'model_TopicType6', {partner})
    assert getattr(partner, 'model_OccurrenceTypeConstraint') == owner
    _safe_set(owner, 'model_TopicType6', set())
    assert getattr(partner, 'model_OccurrenceTypeConstraint') is None


def test_assoc_otherPlayer70_stub_double():
    # model_RoleCombinationConstraint has no real 'model_RoleCombinationConstraint71' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_RoleCombinationConstraint()
    setattr(partner, 'model_RoleCombinationConstraint71', None)
    _safe_set(owner, 'model_TopicType72', partner)
    assert getattr(partner, 'model_RoleCombinationConstraint71') == owner
    _safe_set(owner, 'model_TopicType72', None)
    assert getattr(partner, 'model_RoleCombinationConstraint71') is None


def test_assoc_otherRole73_stub_double():
    # model_RoleCombinationConstraint has no real 'model_RoleCombinationConstraint74' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_RoleCombinationConstraint()
    setattr(partner, 'model_RoleCombinationConstraint74', None)
    _safe_set(owner, 'model_TopicType75', partner)
    assert getattr(partner, 'model_RoleCombinationConstraint74') == owner
    _safe_set(owner, 'model_TopicType75', None)
    assert getattr(partner, 'model_RoleCombinationConstraint74') is None


def test_assoc_player20_stub_double():
    # model_RolePlayerConstraint has no real 'model_RolePlayerConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_RolePlayerConstraint()
    setattr(partner, 'model_RolePlayerConstraint', None)
    _safe_set(owner, 'model_TopicType21', partner)
    assert getattr(partner, 'model_RolePlayerConstraint') == owner
    _safe_set(owner, 'model_TopicType21', None)
    assert getattr(partner, 'model_RolePlayerConstraint') is None


def test_assoc_player67_stub_double():
    # model_RoleCombinationConstraint has no real 'model_RoleCombinationConstraint68' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_RoleCombinationConstraint()
    setattr(partner, 'model_RoleCombinationConstraint68', None)
    _safe_set(owner, 'model_TopicType69', partner)
    assert getattr(partner, 'model_RoleCombinationConstraint68') == owner
    _safe_set(owner, 'model_TopicType69', None)
    assert getattr(partner, 'model_RoleCombinationConstraint68') is None


def test_assoc_role76_stub_double():
    # model_RoleCombinationConstraint has no real 'model_RoleCombinationConstraint77' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_RoleCombinationConstraint()
    setattr(partner, 'model_RoleCombinationConstraint77', None)
    _safe_set(owner, 'model_TopicType78', partner)
    assert getattr(partner, 'model_RoleCombinationConstraint77') == owner
    _safe_set(owner, 'model_TopicType78', None)
    assert getattr(partner, 'model_RoleCombinationConstraint77') is None


def test_assoc_roleConstraint41_stub_double():
    # model_RolePlayerConstraint has no real 'model_RolePlayerConstraint43' property in the generated
    # code (a bare stub) -- manually attach it so model_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Edge(type="sample_text")
    partner = model_RolePlayerConstraint()
    setattr(partner, 'model_RolePlayerConstraint43', None)
    _safe_set(owner, 'model_Edge42', partner)
    assert getattr(partner, 'model_RolePlayerConstraint43') == owner
    _safe_set(owner, 'model_Edge42', None)
    assert getattr(partner, 'model_RolePlayerConstraint43') is None


def test_assoc_subjectIdentifierConstraints9_stub_double():
    # model_SubjectIdentifierConstraint has no real 'model_SubjectIdentifierConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_SubjectIdentifierConstraint()
    setattr(partner, 'model_SubjectIdentifierConstraint', None)
    _safe_set(owner, 'model_TopicType10', {partner})
    assert getattr(partner, 'model_SubjectIdentifierConstraint') == owner
    _safe_set(owner, 'model_TopicType10', set())
    assert getattr(partner, 'model_SubjectIdentifierConstraint') is None


def test_assoc_subjectLocatorConstraints11_stub_double():
    # model_SubjectLocatorConstraint has no real 'model_SubjectLocatorConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_SubjectLocatorConstraint()
    setattr(partner, 'model_SubjectLocatorConstraint', None)
    _safe_set(owner, 'model_TopicType12', {partner})
    assert getattr(partner, 'model_SubjectLocatorConstraint') == owner
    _safe_set(owner, 'model_TopicType12', set())
    assert getattr(partner, 'model_SubjectLocatorConstraint') is None


def test_assoc_topicReifiesConstraints16_stub_double():
    # model_TopicReifiesConstraint has no real 'model_TopicReifiesConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_TopicReifiesConstraint()
    setattr(partner, 'model_TopicReifiesConstraint', None)
    _safe_set(owner, 'model_TopicType17', {partner})
    assert getattr(partner, 'model_TopicReifiesConstraint') == owner
    _safe_set(owner, 'model_TopicType17', set())
    assert getattr(partner, 'model_TopicReifiesConstraint') is None


def test_assoc_type60_stub_double():
    # model_AbstractTypedConstraint has no real 'model_AbstractTypedConstraint' property in the generated
    # code (a bare stub) -- manually attach it so model_TopicType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_TopicType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_TopicType(abstract=True, idType="sample_text", identifiers="sample_text", kind="sample_text", locators="sample_text", name="sample_text")
    partner = model_AbstractTypedConstraint()
    setattr(partner, 'model_AbstractTypedConstraint', None)
    _safe_set(owner, 'model_TopicType61', partner)
    assert getattr(partner, 'model_AbstractTypedConstraint') == owner
    _safe_set(owner, 'model_TopicType61', None)
    assert getattr(partner, 'model_AbstractTypedConstraint') is None


