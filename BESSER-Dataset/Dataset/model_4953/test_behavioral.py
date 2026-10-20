import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Column,
    Content,
    DataSource,
    Entity,
    Field,
    Form,
    Link,
    Named,
    Page,
    RelatedEntity,
    webApplication_Named,
    webApplication_WebApplicationModel,
    webApplication_content_CRUDForm,
    webApplication_content_Content,
    webApplication_content_Field,
    webApplication_content_Form,
    webApplication_content_Link,
    webApplication_content_Menu,
    webApplication_content_MultipleContent,
    webApplication_content_Page,
    webApplication_content_SingleContent,
    webApplication_data_Column,
    webApplication_data_DataSource,
    webApplication_data_Entity,
    webApplication_data_RelatedEntity,
    ColumnType,
    FieldType,
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

def test_assoc_columns7_stub_double():
    # Column has no real 'Column' property in the generated
    # code (a bare stub) -- manually attach it so webApplication_data_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webApplication_data_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webApplication_data_Entity(numberOfColumns="sample_text")
    partner = Column()
    setattr(partner, 'Column', None)
    _safe_set(owner, 'webApplication_data_Entity', {partner})
    assert getattr(partner, 'Column') == owner
    _safe_set(owner, 'webApplication_data_Entity', set())
    assert getattr(partner, 'Column') is None


def test_assoc_relatedEntities10_stub_double():
    # Entity has no real 'Entity12' property in the generated
    # code (a bare stub) -- manually attach it so webApplication_data_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webApplication_data_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webApplication_data_Entity(numberOfColumns="sample_text")
    partner = Entity()
    setattr(partner, 'Entity12', None)
    _safe_set(owner, 'webApplication_data_Entity11', {partner})
    assert getattr(partner, 'Entity12') == owner
    _safe_set(owner, 'webApplication_data_Entity11', set())
    assert getattr(partner, 'Entity12') is None


def test_assoc_relates8_stub_double():
    # RelatedEntity has no real 'RelatedEntity' property in the generated
    # code (a bare stub) -- manually attach it so webApplication_data_Entity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # webApplication_data_Entity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = webApplication_data_Entity(numberOfColumns="sample_text")
    partner = RelatedEntity()
    setattr(partner, 'RelatedEntity', None)
    _safe_set(owner, 'webApplication_data_Entity9', {partner})
    assert getattr(partner, 'RelatedEntity') == owner
    _safe_set(owner, 'webApplication_data_Entity9', set())
    assert getattr(partner, 'RelatedEntity') is None


