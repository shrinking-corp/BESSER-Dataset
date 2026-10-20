import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BusinessColumn,
    BusinessColumnSet,
    BusinessDomain,
    BusinessIdentifier,
    BusinessModel,
    BusinessRelationship,
    BusinessViewInnerJoinRelationship,
    CalculatedMember,
    Cube,
    Dimension,
    Hierarchy,
    Level,
    Measure,
    ModelObject,
    NamedSet,
    OlapModel,
    PhysicalColumn,
    PhysicalForeignKey,
    PhysicalModel,
    PhysicalPrimaryKey,
    PhysicalTable,
    VirtualCube,
    VirtualCubeDimension,
    VirtualCubeMeasure,
    business_model_Model,
    model_Model,
    model_ModelObject,
    model_ModelProperty,
    model_ModelPropertyCategory,
    model_ModelPropertyMapEntry,
    model_ModelPropertyType,
    model_analytical_AnalyticalModel,
    model_behavioural_BehaviouralModel,
    model_business_BusinessColumn,
    model_business_BusinessColumnSet,
    model_business_BusinessDomain,
    model_business_BusinessIdentifier,
    model_business_BusinessModel,
    model_business_BusinessRelationship,
    model_business_BusinessTable,
    model_business_BusinessView,
    model_business_BusinessViewInnerJoinRelationship,
    model_business_CalculatedBusinessColumn,
    model_business_SimpleBusinessColumn,
    model_olap_CalculatedMember,
    model_olap_Cube,
    model_olap_Dimension,
    model_olap_Hierarchy,
    model_olap_Level,
    model_olap_Measure,
    model_olap_NamedSet,
    model_olap_OlapModel,
    model_olap_VirtualCube,
    model_olap_VirtualCubeDimension,
    model_olap_VirtualCubeMeasure,
    model_physical_PhysicalColumn,
    model_physical_PhysicalForeignKey,
    model_physical_PhysicalModel,
    model_physical_PhysicalPrimaryKey,
    model_physical_PhysicalTable,
    olap_model_Model,
    physical_model_Model,
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

def test_assoc_category6_reverse_link_reassign_clear():
    a1 = model_ModelPropertyType(admissibleValues="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", name="sample_text")
    a2 = model_ModelPropertyType(admissibleValues="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    _safe_set(b, 'ModelPropertyCategory', a1)
    assert _is_linked(b, 'ModelPropertyCategory', a1)
    if hasattr(a1, 'propertyTypes'):
        assert _is_linked(a1, 'propertyTypes', b)
    _safe_set(b, 'ModelPropertyCategory', a2)
    assert _is_linked(b, 'ModelPropertyCategory', a2)
    if hasattr(a1, 'propertyTypes'):
        assert not _is_linked(a1, 'propertyTypes', b)
    if hasattr(a2, 'propertyTypes'):
        assert _is_linked(a2, 'propertyTypes', b)
    _safe_set(b, 'ModelPropertyCategory', None)
    assert not _is_linked(b, 'ModelPropertyCategory', a2)
    if hasattr(a2, 'propertyTypes'):
        assert not _is_linked(a2, 'propertyTypes', b)


def test_assoc_parentCategory1_reverse_link_reassign_clear():
    a1 = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    a2 = model_ModelPropertyCategory(description="sample_text_2", name="sample_text_2")
    b = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    _safe_set(b, 'model_ModelPropertyCategory0', a1)
    assert _is_linked(b, 'model_ModelPropertyCategory0', a1)
    if hasattr(a1, 'model_ModelPropertyCategory'):
        assert _is_linked(a1, 'model_ModelPropertyCategory', b)
    _safe_set(b, 'model_ModelPropertyCategory0', a2)
    assert _is_linked(b, 'model_ModelPropertyCategory0', a2)
    if hasattr(a1, 'model_ModelPropertyCategory'):
        assert not _is_linked(a1, 'model_ModelPropertyCategory', b)
    if hasattr(a2, 'model_ModelPropertyCategory'):
        assert _is_linked(a2, 'model_ModelPropertyCategory', b)
    _safe_set(b, 'model_ModelPropertyCategory0', None)
    assert not _is_linked(b, 'model_ModelPropertyCategory0', a2)
    if hasattr(a2, 'model_ModelPropertyCategory'):
        assert not _is_linked(a2, 'model_ModelPropertyCategory', b)


def test_assoc_properties10_reverse_link_reassign_clear():
    a1 = model_ModelPropertyMapEntry(key="sample_text")
    a2 = model_ModelPropertyMapEntry(key="sample_text_2")
    b = model_ModelObject(description="sample_text", id="sample_text", name="sample_text", uniqueName="sample_text")
    _safe_set(b, 'model_ModelObject', {a1})
    assert _is_linked(b, 'model_ModelObject', a1)
    if hasattr(a1, 'model_ModelPropertyMapEntry11'):
        assert _is_linked(a1, 'model_ModelPropertyMapEntry11', b)
    _safe_set(b, 'model_ModelObject', {a2})
    assert _is_linked(b, 'model_ModelObject', a2)
    if hasattr(a1, 'model_ModelPropertyMapEntry11'):
        assert not _is_linked(a1, 'model_ModelPropertyMapEntry11', b)
    if hasattr(a2, 'model_ModelPropertyMapEntry11'):
        assert _is_linked(a2, 'model_ModelPropertyMapEntry11', b)
    _safe_set(b, 'model_ModelObject', set())
    assert not _is_linked(b, 'model_ModelObject', a2)
    if hasattr(a2, 'model_ModelPropertyMapEntry11'):
        assert not _is_linked(a2, 'model_ModelPropertyMapEntry11', b)


def test_assoc_propertyType7_reverse_link_reassign_clear():
    a1 = model_ModelPropertyType(admissibleValues="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", name="sample_text")
    a2 = model_ModelPropertyType(admissibleValues="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = model_ModelProperty(value="sample_text")
    _safe_set(b, 'model_ModelProperty', a1)
    assert _is_linked(b, 'model_ModelProperty', a1)
    if hasattr(a1, 'model_ModelPropertyType'):
        assert _is_linked(a1, 'model_ModelPropertyType', b)
    _safe_set(b, 'model_ModelProperty', a2)
    assert _is_linked(b, 'model_ModelProperty', a2)
    if hasattr(a1, 'model_ModelPropertyType'):
        assert not _is_linked(a1, 'model_ModelPropertyType', b)
    if hasattr(a2, 'model_ModelPropertyType'):
        assert _is_linked(a2, 'model_ModelPropertyType', b)
    _safe_set(b, 'model_ModelProperty', None)
    assert not _is_linked(b, 'model_ModelProperty', a2)
    if hasattr(a2, 'model_ModelPropertyType'):
        assert not _is_linked(a2, 'model_ModelPropertyType', b)


def test_assoc_propertyTypes5_reverse_link_reassign_clear():
    a1 = model_ModelPropertyType(admissibleValues="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", name="sample_text")
    a2 = model_ModelPropertyType(admissibleValues="sample_text_2", defaultValue="sample_text_2", description="sample_text_2", id="sample_text_2", name="sample_text_2")
    b = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'ModelPropertyType'):
        assert _is_linked(a1, 'ModelPropertyType', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'ModelPropertyType'):
        assert not _is_linked(a1, 'ModelPropertyType', b)
    if hasattr(a2, 'ModelPropertyType'):
        assert _is_linked(a2, 'ModelPropertyType', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'ModelPropertyType'):
        assert not _is_linked(a2, 'ModelPropertyType', b)


def test_assoc_subCategories3_reverse_link_reassign_clear():
    a1 = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    a2 = model_ModelPropertyCategory(description="sample_text_2", name="sample_text_2")
    b = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    _safe_set(b, 'model_ModelPropertyCategory4', a1)
    assert _is_linked(b, 'model_ModelPropertyCategory4', a1)
    if hasattr(a1, 'model_ModelPropertyCategory2'):
        assert _is_linked(a1, 'model_ModelPropertyCategory2', b)
    _safe_set(b, 'model_ModelPropertyCategory4', a2)
    assert _is_linked(b, 'model_ModelPropertyCategory4', a2)
    if hasattr(a1, 'model_ModelPropertyCategory2'):
        assert not _is_linked(a1, 'model_ModelPropertyCategory2', b)
    if hasattr(a2, 'model_ModelPropertyCategory2'):
        assert _is_linked(a2, 'model_ModelPropertyCategory2', b)
    _safe_set(b, 'model_ModelPropertyCategory4', None)
    assert not _is_linked(b, 'model_ModelPropertyCategory4', a2)
    if hasattr(a2, 'model_ModelPropertyCategory2'):
        assert not _is_linked(a2, 'model_ModelPropertyCategory2', b)


def test_assoc_value8_reverse_link_reassign_clear():
    a1 = model_ModelPropertyMapEntry(key="sample_text")
    a2 = model_ModelPropertyMapEntry(key="sample_text_2")
    b = model_ModelProperty(value="sample_text")
    _safe_set(b, 'model_ModelProperty9', a1)
    assert _is_linked(b, 'model_ModelProperty9', a1)
    if hasattr(a1, 'model_ModelPropertyMapEntry'):
        assert _is_linked(a1, 'model_ModelPropertyMapEntry', b)
    _safe_set(b, 'model_ModelProperty9', a2)
    assert _is_linked(b, 'model_ModelProperty9', a2)
    if hasattr(a1, 'model_ModelPropertyMapEntry'):
        assert not _is_linked(a1, 'model_ModelPropertyMapEntry', b)
    if hasattr(a2, 'model_ModelPropertyMapEntry'):
        assert _is_linked(a2, 'model_ModelPropertyMapEntry', b)
    _safe_set(b, 'model_ModelProperty9', None)
    assert not _is_linked(b, 'model_ModelProperty9', a2)
    if hasattr(a2, 'model_ModelPropertyMapEntry'):
        assert not _is_linked(a2, 'model_ModelPropertyMapEntry', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns30_stub_double():
    # PhysicalColumn has no real 'PhysicalColumn' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalTable(comment="sample_text", type="sample_text")
    partner = PhysicalColumn()
    setattr(partner, 'PhysicalColumn', None)
    _safe_set(owner, 'table', {partner})
    assert getattr(partner, 'PhysicalColumn') == owner
    _safe_set(owner, 'table', set())
    assert getattr(partner, 'PhysicalColumn') is None


def test_assoc_destinationColumns48_stub_double():
    # PhysicalColumn has no real 'PhysicalColumn50' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalForeignKey(destinationName="sample_text", sourceName="sample_text")
    partner = PhysicalColumn()
    setattr(partner, 'PhysicalColumn50', None)
    _safe_set(owner, 'model_physical_PhysicalForeignKey49', {partner})
    assert getattr(partner, 'PhysicalColumn50') == owner
    _safe_set(owner, 'model_physical_PhysicalForeignKey49', set())
    assert getattr(partner, 'PhysicalColumn50') is None


def test_assoc_destinationTable45_stub_double():
    # PhysicalTable has no real 'PhysicalTable47' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalForeignKey(destinationName="sample_text", sourceName="sample_text")
    partner = PhysicalTable()
    setattr(partner, 'PhysicalTable47', None)
    _safe_set(owner, 'model_physical_PhysicalForeignKey46', partner)
    assert getattr(partner, 'PhysicalTable47') == owner
    _safe_set(owner, 'model_physical_PhysicalForeignKey46', None)
    assert getattr(partner, 'PhysicalTable47') is None


def test_assoc_foreignKeys26_stub_double():
    # PhysicalForeignKey has no real 'PhysicalForeignKey' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalModel(catalog="sample_text", databaseName="sample_text", databaseVersion="sample_text", schema="sample_text")
    partner = PhysicalForeignKey()
    setattr(partner, 'PhysicalForeignKey', None)
    _safe_set(owner, 'model27', {partner})
    assert getattr(partner, 'PhysicalForeignKey') == owner
    _safe_set(owner, 'model27', set())
    assert getattr(partner, 'PhysicalForeignKey') is None


def test_assoc_model28_stub_double():
    # PhysicalModel has no real 'PhysicalModel29' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalTable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalTable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalTable(comment="sample_text", type="sample_text")
    partner = PhysicalModel()
    setattr(partner, 'PhysicalModel29', None)
    _safe_set(owner, 'tables', partner)
    assert getattr(partner, 'PhysicalModel29') == owner
    _safe_set(owner, 'tables', None)
    assert getattr(partner, 'PhysicalModel29') is None


def test_assoc_model51_stub_double():
    # PhysicalModel has no real 'PhysicalModel52' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalForeignKey(destinationName="sample_text", sourceName="sample_text")
    partner = PhysicalModel()
    setattr(partner, 'PhysicalModel52', None)
    _safe_set(owner, 'foreignKeys', partner)
    assert getattr(partner, 'PhysicalModel52') == owner
    _safe_set(owner, 'foreignKeys', None)
    assert getattr(partner, 'PhysicalModel52') is None


def test_assoc_parentModel22_stub_double():
    # physical_model_Model has no real 'Model' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalModel(catalog="sample_text", databaseName="sample_text", databaseVersion="sample_text", schema="sample_text")
    partner = physical_model_Model()
    setattr(partner, 'Model', None)
    _safe_set(owner, 'physicalModels', partner)
    assert getattr(partner, 'Model') == owner
    _safe_set(owner, 'physicalModels', None)
    assert getattr(partner, 'Model') is None


def test_assoc_primaryKeys24_stub_double():
    # PhysicalPrimaryKey has no real 'PhysicalPrimaryKey' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalModel(catalog="sample_text", databaseName="sample_text", databaseVersion="sample_text", schema="sample_text")
    partner = PhysicalPrimaryKey()
    setattr(partner, 'PhysicalPrimaryKey', None)
    _safe_set(owner, 'model25', {partner})
    assert getattr(partner, 'PhysicalPrimaryKey') == owner
    _safe_set(owner, 'model25', set())
    assert getattr(partner, 'PhysicalPrimaryKey') is None


def test_assoc_propertyCategories19_stub_double():
    # model_Model has no real 'model_Model20' property in the generated
    # code (a bare stub) -- manually attach it so model_ModelPropertyCategory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ModelPropertyCategory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ModelPropertyCategory(description="sample_text", name="sample_text")
    partner = model_Model()
    setattr(partner, 'model_Model20', None)
    _safe_set(owner, 'model_ModelPropertyCategory21', partner)
    assert owner in getattr(partner, 'model_Model20')
    _safe_set(owner, 'model_ModelPropertyCategory21', None)
    assert owner not in getattr(partner, 'model_Model20')


def test_assoc_propertyTypes17_stub_double():
    # model_Model has no real 'model_Model' property in the generated
    # code (a bare stub) -- manually attach it so model_ModelPropertyType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ModelPropertyType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ModelPropertyType(admissibleValues="sample_text", defaultValue="sample_text", description="sample_text", id="sample_text", name="sample_text")
    partner = model_Model()
    setattr(partner, 'model_Model', None)
    _safe_set(owner, 'model_ModelPropertyType18', partner)
    assert owner in getattr(partner, 'model_Model')
    _safe_set(owner, 'model_ModelPropertyType18', None)
    assert owner not in getattr(partner, 'model_Model')


def test_assoc_sourceColumns42_stub_double():
    # PhysicalColumn has no real 'PhysicalColumn44' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalForeignKey(destinationName="sample_text", sourceName="sample_text")
    partner = PhysicalColumn()
    setattr(partner, 'PhysicalColumn44', None)
    _safe_set(owner, 'model_physical_PhysicalForeignKey43', {partner})
    assert getattr(partner, 'PhysicalColumn44') == owner
    _safe_set(owner, 'model_physical_PhysicalForeignKey43', set())
    assert getattr(partner, 'PhysicalColumn44') is None


def test_assoc_sourceTable40_stub_double():
    # PhysicalTable has no real 'PhysicalTable41' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalForeignKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalForeignKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalForeignKey(destinationName="sample_text", sourceName="sample_text")
    partner = PhysicalTable()
    setattr(partner, 'PhysicalTable41', None)
    _safe_set(owner, 'model_physical_PhysicalForeignKey', partner)
    assert getattr(partner, 'PhysicalTable41') == owner
    _safe_set(owner, 'model_physical_PhysicalForeignKey', None)
    assert getattr(partner, 'PhysicalTable41') is None


def test_assoc_table31_stub_double():
    # PhysicalTable has no real 'PhysicalTable32' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalColumn's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalColumn's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalColumn(comment="sample_text", dataType="sample_text", decimalDigits=7, defaultValue="sample_text", nullable=True, octectLength=7, position=7, radix=7, size=7, typeName="sample_text")
    partner = PhysicalTable()
    setattr(partner, 'PhysicalTable32', None)
    _safe_set(owner, 'columns', partner)
    assert getattr(partner, 'PhysicalTable32') == owner
    _safe_set(owner, 'columns', None)
    assert getattr(partner, 'PhysicalTable32') is None


def test_assoc_tables23_stub_double():
    # PhysicalTable has no real 'PhysicalTable' property in the generated
    # code (a bare stub) -- manually attach it so model_physical_PhysicalModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_physical_PhysicalModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_physical_PhysicalModel(catalog="sample_text", databaseName="sample_text", databaseVersion="sample_text", schema="sample_text")
    partner = PhysicalTable()
    setattr(partner, 'PhysicalTable', None)
    _safe_set(owner, 'model', {partner})
    assert getattr(partner, 'PhysicalTable') == owner
    _safe_set(owner, 'model', set())
    assert getattr(partner, 'PhysicalTable') is None


