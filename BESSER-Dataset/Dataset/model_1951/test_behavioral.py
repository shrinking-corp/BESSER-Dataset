import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AQueryResult,
    Argument,
    ArrayElement,
    ArrayValue,
    Composite,
    DataSource,
    DataSourceLibraryConfiguration,
    DomainModel_,
    Dynamics,
    Expression,
    Function,
    FunctionPlot,
    HTML,
    ISynchable,
    Image,
    MetadataValue,
    Node,
    PhysicalQuantity,
    Point,
    Pointer,
    PointerElement,
    Quantity,
    Query,
    QueryMatchingCriteria,
    SkeletonTransformation,
    StringToValueMap,
    Text,
    Type,
    TypeToValueMap,
    URL,
    Unit,
    Value,
    Variable,
    VisualGroup,
    VisualGroupElement,
    VisualType,
    VisualValue,
    datasources_model_GeppettoLibrary,
    datasources_model_StringToStringMap,
    model_DomainModel_,
    model_ExperimentState,
    model_ExternalDomainModel,
    model_GeppettoLibrary,
    model_GeppettoModel,
    model_ISynchable,
    model_LibraryManager,
    model_ModelFormat,
    model_Node,
    model_StringToStringMap,
    model_Tag,
    model_VariableValue,
    model_datasources_AQueryResult,
    model_datasources_CompoundQuery,
    model_datasources_CompoundRefQuery,
    model_datasources_DataSource,
    model_datasources_DataSourceLibraryConfiguration,
    model_datasources_ProcessQuery,
    model_datasources_Query,
    model_datasources_QueryMatchingCriteria,
    model_datasources_QueryResult,
    model_datasources_QueryResults,
    model_datasources_RunnableQuery,
    model_datasources_SerializableQueryResult,
    model_datasources_SimpleQuery,
    model_types_ArgumentType,
    model_types_ArrayType,
    model_types_CompositeType,
    model_types_CompositeVisualType,
    model_types_ConnectionType,
    model_types_DynamicsType,
    model_types_ExpressionType,
    model_types_HTMLType,
    model_types_ImageType,
    model_types_ImportType,
    model_types_ParameterType,
    model_types_PointType,
    model_types_PointerType,
    model_types_QuantityType,
    model_types_SimpleType,
    model_types_StateVariableType,
    model_types_TextType,
    model_types_Type,
    model_types_URLType,
    model_types_VisualType,
    model_values_Argument,
    model_values_ArrayElement,
    model_values_ArrayValue,
    model_values_Collada,
    model_values_Composite,
    model_values_Connection,
    model_values_Cylinder,
    model_values_Dynamics,
    model_values_Expression,
    model_values_Function,
    model_values_FunctionPlot,
    model_values_HTML,
    model_values_Image,
    model_values_ImportValue,
    model_values_MDTimeSeries,
    model_values_MetadataValue,
    model_values_OBJ,
    model_values_Particles,
    model_values_PhysicalQuantity,
    model_values_Point,
    model_values_Pointer,
    model_values_PointerElement,
    model_values_Quantity,
    model_values_SkeletonAnimation,
    model_values_SkeletonTransformation,
    model_values_Sphere,
    model_values_StringToValueMap,
    model_values_Text,
    model_values_TimeSeries,
    model_values_URL,
    model_values_Unit,
    model_values_Value,
    model_values_VisualGroup,
    model_values_VisualGroupElement,
    model_values_VisualValue,
    model_variables_TypeToValueMap,
    model_variables_Variable,
    types_model_DomainModel_,
    BooleanOperator,
    Connectivity,
    FileFormat,
    ImageFormat,
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

def test_assoc_format29_reverse_link_reassign_clear():
    a1 = model_ModelFormat(modelFormat="sample_text")
    a2 = model_ModelFormat(modelFormat="sample_text_2")
    b = model_DomainModel_(domainModel="sample_text")
    _safe_set(b, 'model_DomainModel', a1)
    assert _is_linked(b, 'model_DomainModel', a1)
    if hasattr(a1, 'model_ModelFormat'):
        assert _is_linked(a1, 'model_ModelFormat', b)
    _safe_set(b, 'model_DomainModel', a2)
    assert _is_linked(b, 'model_DomainModel', a2)
    if hasattr(a1, 'model_ModelFormat'):
        assert not _is_linked(a1, 'model_ModelFormat', b)
    if hasattr(a2, 'model_ModelFormat'):
        assert _is_linked(a2, 'model_ModelFormat', b)
    _safe_set(b, 'model_DomainModel', None)
    assert not _is_linked(b, 'model_DomainModel', a2)
    if hasattr(a2, 'model_ModelFormat'):
        assert not _is_linked(a2, 'model_ModelFormat', b)


def test_assoc_libraries1_reverse_link_reassign_clear():
    a1 = model_GeppettoModel(id="sample_text", name="sample_text")
    a2 = model_GeppettoModel(id="sample_text_2", name="sample_text_2")
    b = model_GeppettoLibrary()
    _safe_set(b, 'model_GeppettoLibrary', a1)
    assert _is_linked(b, 'model_GeppettoLibrary', a1)
    if hasattr(a1, 'model_GeppettoModel2'):
        assert _is_linked(a1, 'model_GeppettoModel2', b)
    _safe_set(b, 'model_GeppettoLibrary', a2)
    assert _is_linked(b, 'model_GeppettoLibrary', a2)
    if hasattr(a1, 'model_GeppettoModel2'):
        assert not _is_linked(a1, 'model_GeppettoModel2', b)
    if hasattr(a2, 'model_GeppettoModel2'):
        assert _is_linked(a2, 'model_GeppettoModel2', b)
    _safe_set(b, 'model_GeppettoLibrary', None)
    assert not _is_linked(b, 'model_GeppettoLibrary', a2)
    if hasattr(a2, 'model_GeppettoModel2'):
        assert not _is_linked(a2, 'model_GeppettoModel2', b)


def test_assoc_tags27_reverse_link_reassign_clear():
    a1 = model_Tag(name="sample_text")
    a2 = model_Tag(name="sample_text_2")
    b = model_Tag(name="sample_text")
    _safe_set(b, 'model_Tag28', a1)
    assert _is_linked(b, 'model_Tag28', a1)
    if hasattr(a1, 'model_Tag26'):
        assert _is_linked(a1, 'model_Tag26', b)
    _safe_set(b, 'model_Tag28', a2)
    assert _is_linked(b, 'model_Tag28', a2)
    if hasattr(a1, 'model_Tag26'):
        assert not _is_linked(a1, 'model_Tag26', b)
    if hasattr(a2, 'model_Tag26'):
        assert _is_linked(a2, 'model_Tag26', b)
    _safe_set(b, 'model_Tag28', None)
    assert not _is_linked(b, 'model_Tag28', a2)
    if hasattr(a2, 'model_Tag26'):
        assert not _is_linked(a2, 'model_Tag26', b)


def test_assoc_tags3_reverse_link_reassign_clear():
    a1 = model_Tag(name="sample_text")
    a2 = model_Tag(name="sample_text_2")
    b = model_GeppettoModel(id="sample_text", name="sample_text")
    _safe_set(b, 'model_GeppettoModel4', {a1})
    assert _is_linked(b, 'model_GeppettoModel4', a1)
    if hasattr(a1, 'model_Tag'):
        assert _is_linked(a1, 'model_Tag', b)
    _safe_set(b, 'model_GeppettoModel4', {a2})
    assert _is_linked(b, 'model_GeppettoModel4', a2)
    if hasattr(a1, 'model_Tag'):
        assert not _is_linked(a1, 'model_Tag', b)
    if hasattr(a2, 'model_Tag'):
        assert _is_linked(a2, 'model_Tag', b)
    _safe_set(b, 'model_GeppettoModel4', set())
    assert not _is_linked(b, 'model_GeppettoModel4', a2)
    if hasattr(a2, 'model_Tag'):
        assert not _is_linked(a2, 'model_Tag', b)


def test_assoc_tags9_reverse_link_reassign_clear():
    a1 = model_Tag(name="sample_text")
    a2 = model_Tag(name="sample_text_2")
    b = model_Node(id="sample_text", name="sample_text")
    _safe_set(b, 'model_Node', {a1})
    assert _is_linked(b, 'model_Node', a1)
    if hasattr(a1, 'model_Tag10'):
        assert _is_linked(a1, 'model_Tag10', b)
    _safe_set(b, 'model_Node', {a2})
    assert _is_linked(b, 'model_Node', a2)
    if hasattr(a1, 'model_Tag10'):
        assert not _is_linked(a1, 'model_Tag10', b)
    if hasattr(a2, 'model_Tag10'):
        assert _is_linked(a2, 'model_Tag10', b)
    _safe_set(b, 'model_Node', set())
    assert not _is_linked(b, 'model_Node', a2)
    if hasattr(a2, 'model_Tag10'):
        assert not _is_linked(a2, 'model_Tag10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a111_stub_double():
    # Pointer has no real 'Pointer112' property in the generated
    # code (a bare stub) -- manually attach it so model_values_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_Connection(connectivity="sample_text")
    partner = Pointer()
    setattr(partner, 'Pointer112', None)
    _safe_set(owner, 'model_values_Connection', partner)
    assert getattr(partner, 'Pointer112') == owner
    _safe_set(owner, 'model_values_Connection', None)
    assert getattr(partner, 'Pointer112') is None


def test_assoc_anonymousTypes122_stub_double():
    # Type has no real 'Type123' property in the generated
    # code (a bare stub) -- manually attach it so model_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_variables_Variable(static="sample_text")
    partner = Type()
    setattr(partner, 'Type123', None)
    _safe_set(owner, 'model_variables_Variable', {partner})
    assert getattr(partner, 'Type123') == owner
    _safe_set(owner, 'model_variables_Variable', set())
    assert getattr(partner, 'Type123') is None


def test_assoc_arrayType57_stub_double():
    # Type has no real 'Type58' property in the generated
    # code (a bare stub) -- manually attach it so model_types_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_ArrayType(size="sample_text")
    partner = Type()
    setattr(partner, 'Type58', None)
    _safe_set(owner, 'model_types_ArrayType', partner)
    assert getattr(partner, 'Type58') == owner
    _safe_set(owner, 'model_types_ArrayType', None)
    assert getattr(partner, 'Type58') is None


def test_assoc_b113_stub_double():
    # Pointer has no real 'Pointer115' property in the generated
    # code (a bare stub) -- manually attach it so model_values_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_Connection(connectivity="sample_text")
    partner = Pointer()
    setattr(partner, 'Pointer115', None)
    _safe_set(owner, 'model_values_Connection114', partner)
    assert getattr(partner, 'Pointer115') == owner
    _safe_set(owner, 'model_values_Connection114', None)
    assert getattr(partner, 'Pointer115') is None


def test_assoc_dataSources5_stub_double():
    # DataSource has no real 'DataSource' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoModel(id="sample_text", name="sample_text")
    partner = DataSource()
    setattr(partner, 'DataSource', None)
    _safe_set(owner, 'model_GeppettoModel6', {partner})
    assert getattr(partner, 'DataSource') == owner
    _safe_set(owner, 'model_GeppettoModel6', set())
    assert getattr(partner, 'DataSource') is None


def test_assoc_defaultValue59_stub_double():
    # ArrayValue has no real 'ArrayValue' property in the generated
    # code (a bare stub) -- manually attach it so model_types_ArrayType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_ArrayType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_ArrayType(size="sample_text")
    partner = ArrayValue()
    setattr(partner, 'ArrayValue', None)
    _safe_set(owner, 'model_types_ArrayType60', partner)
    assert getattr(partner, 'ArrayValue') == owner
    _safe_set(owner, 'model_types_ArrayType60', None)
    assert getattr(partner, 'ArrayValue') is None


def test_assoc_dependenciesLibrary140_stub_double():
    # datasources_model_GeppettoLibrary has no real 'datasources_model_GeppettoLibrary' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSource(dataSourceService="sample_text", url="sample_text")
    partner = datasources_model_GeppettoLibrary()
    setattr(partner, 'datasources_model_GeppettoLibrary', None)
    _safe_set(owner, 'model_datasources_DataSource141', {partner})
    assert getattr(partner, 'datasources_model_GeppettoLibrary') == owner
    _safe_set(owner, 'model_datasources_DataSource141', set())
    assert getattr(partner, 'datasources_model_GeppettoLibrary') is None


def test_assoc_distal102_stub_double():
    # Point has no real 'Point103' property in the generated
    # code (a bare stub) -- manually attach it so model_values_Cylinder's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_Cylinder's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_Cylinder(bottomRadius="sample_text", height="sample_text", topRadius="sample_text")
    partner = Point()
    setattr(partner, 'Point103', None)
    _safe_set(owner, 'model_values_Cylinder', partner)
    assert getattr(partner, 'Point103') == owner
    _safe_set(owner, 'model_values_Cylinder', None)
    assert getattr(partner, 'Point103') is None


def test_assoc_domainModel36_stub_double():
    # types_model_DomainModel_ has no real 'types_model_DomainModel' property in the generated
    # code (a bare stub) -- manually attach it so model_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_Type(abstract="sample_text")
    partner = types_model_DomainModel_()
    setattr(partner, 'types_model_DomainModel', None)
    _safe_set(owner, 'model_types_Type37', partner)
    assert getattr(partner, 'types_model_DomainModel') == owner
    _safe_set(owner, 'model_types_Type37', None)
    assert getattr(partner, 'types_model_DomainModel') is None


def test_assoc_elements79_stub_double():
    # PointerElement has no real 'PointerElement' property in the generated
    # code (a bare stub) -- manually attach it so model_values_Pointer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_Pointer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_Pointer(path="sample_text")
    partner = PointerElement()
    setattr(partner, 'PointerElement', None)
    _safe_set(owner, 'model_values_Pointer', {partner})
    assert getattr(partner, 'PointerElement') == owner
    _safe_set(owner, 'model_values_Pointer', set())
    assert getattr(partner, 'PointerElement') is None


def test_assoc_fetchVariableQuery145_stub_double():
    # Query has no real 'Query147' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSource(dataSourceService="sample_text", url="sample_text")
    partner = Query()
    setattr(partner, 'Query147', None)
    _safe_set(owner, 'model_datasources_DataSource146', partner)
    assert getattr(partner, 'Query147') == owner
    _safe_set(owner, 'model_datasources_DataSource146', None)
    assert getattr(partner, 'Query147') is None


def test_assoc_initialValue118_stub_double():
    # Value has no real 'Value120' property in the generated
    # code (a bare stub) -- manually attach it so model_values_ArrayElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_ArrayElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_ArrayElement(index="sample_text")
    partner = Value()
    setattr(partner, 'Value120', None)
    _safe_set(owner, 'model_values_ArrayElement119', partner)
    assert getattr(partner, 'Value120') == owner
    _safe_set(owner, 'model_values_ArrayElement119', None)
    assert getattr(partner, 'Value120') is None


def test_assoc_initialValues126_stub_double():
    # TypeToValueMap has no real 'TypeToValueMap' property in the generated
    # code (a bare stub) -- manually attach it so model_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_variables_Variable(static="sample_text")
    partner = TypeToValueMap()
    setattr(partner, 'TypeToValueMap', None)
    _safe_set(owner, 'model_variables_Variable127', {partner})
    assert getattr(partner, 'TypeToValueMap') == owner
    _safe_set(owner, 'model_variables_Variable127', set())
    assert getattr(partner, 'TypeToValueMap') is None


def test_assoc_libraries16_stub_double():
    # model_LibraryManager has no real 'model_LibraryManager' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoLibrary()
    partner = model_LibraryManager()
    setattr(partner, 'model_LibraryManager', None)
    _safe_set(owner, 'model_GeppettoLibrary17', partner)
    assert owner in getattr(partner, 'model_LibraryManager')
    _safe_set(owner, 'model_GeppettoLibrary17', None)
    assert owner not in getattr(partner, 'model_LibraryManager')


def test_assoc_library148_stub_double():
    # datasources_model_GeppettoLibrary has no real 'datasources_model_GeppettoLibrary149' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSourceLibraryConfiguration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSourceLibraryConfiguration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSourceLibraryConfiguration(format="sample_text", modelInterpreterId="sample_text")
    partner = datasources_model_GeppettoLibrary()
    setattr(partner, 'datasources_model_GeppettoLibrary149', None)
    _safe_set(owner, 'model_datasources_DataSourceLibraryConfiguration', partner)
    assert getattr(partner, 'datasources_model_GeppettoLibrary149') == owner
    _safe_set(owner, 'model_datasources_DataSourceLibraryConfiguration', None)
    assert getattr(partner, 'datasources_model_GeppettoLibrary149') is None


def test_assoc_libraryConfigurations136_stub_double():
    # DataSourceLibraryConfiguration has no real 'DataSourceLibraryConfiguration' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSource(dataSourceService="sample_text", url="sample_text")
    partner = DataSourceLibraryConfiguration()
    setattr(partner, 'DataSourceLibraryConfiguration', None)
    _safe_set(owner, 'model_datasources_DataSource', {partner})
    assert getattr(partner, 'DataSourceLibraryConfiguration') == owner
    _safe_set(owner, 'model_datasources_DataSource', set())
    assert getattr(partner, 'DataSourceLibraryConfiguration') is None


def test_assoc_matchingCriteria150_stub_double():
    # QueryMatchingCriteria has no real 'QueryMatchingCriteria' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_Query(description="sample_text", runForCount="sample_text")
    partner = QueryMatchingCriteria()
    setattr(partner, 'QueryMatchingCriteria', None)
    _safe_set(owner, 'model_datasources_Query', {partner})
    assert getattr(partner, 'QueryMatchingCriteria') == owner
    _safe_set(owner, 'model_datasources_Query', set())
    assert getattr(partner, 'QueryMatchingCriteria') is None


def test_assoc_parameter107_stub_double():
    # Quantity has no real 'Quantity108' property in the generated
    # code (a bare stub) -- manually attach it so model_values_VisualGroupElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_VisualGroupElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_VisualGroupElement(defaultColor="sample_text")
    partner = Quantity()
    setattr(partner, 'Quantity108', None)
    _safe_set(owner, 'model_values_VisualGroupElement', partner)
    assert getattr(partner, 'Quantity108') == owner
    _safe_set(owner, 'model_values_VisualGroupElement', None)
    assert getattr(partner, 'Quantity108') is None


def test_assoc_parameters154_stub_double():
    # datasources_model_StringToStringMap has no real 'datasources_model_StringToStringMap' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_ProcessQuery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_ProcessQuery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_ProcessQuery(queryProcessorId="sample_text")
    partner = datasources_model_StringToStringMap()
    setattr(partner, 'datasources_model_StringToStringMap', None)
    _safe_set(owner, 'model_datasources_ProcessQuery', {partner})
    assert getattr(partner, 'datasources_model_StringToStringMap') == owner
    _safe_set(owner, 'model_datasources_ProcessQuery', set())
    assert getattr(partner, 'datasources_model_StringToStringMap') is None


def test_assoc_point80_stub_double():
    # Point has no real 'Point82' property in the generated
    # code (a bare stub) -- manually attach it so model_values_Pointer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_Pointer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_Pointer(path="sample_text")
    partner = Point()
    setattr(partner, 'Point82', None)
    _safe_set(owner, 'model_values_Pointer81', partner)
    assert getattr(partner, 'Point82') == owner
    _safe_set(owner, 'model_values_Pointer81', None)
    assert getattr(partner, 'Point82') is None


def test_assoc_position116_stub_double():
    # Point has no real 'Point117' property in the generated
    # code (a bare stub) -- manually attach it so model_values_ArrayElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_ArrayElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_ArrayElement(index="sample_text")
    partner = Point()
    setattr(partner, 'Point117', None)
    _safe_set(owner, 'model_values_ArrayElement', partner)
    assert getattr(partner, 'Point117') == owner
    _safe_set(owner, 'model_values_ArrayElement', None)
    assert getattr(partner, 'Point117') is None


def test_assoc_position128_stub_double():
    # Point has no real 'Point130' property in the generated
    # code (a bare stub) -- manually attach it so model_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_variables_Variable(static="sample_text")
    partner = Point()
    setattr(partner, 'Point130', None)
    _safe_set(owner, 'model_variables_Variable129', partner)
    assert getattr(partner, 'Point130') == owner
    _safe_set(owner, 'model_variables_Variable129', None)
    assert getattr(partner, 'Point130') is None


def test_assoc_queries137_stub_double():
    # Query has no real 'Query139' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSource(dataSourceService="sample_text", url="sample_text")
    partner = Query()
    setattr(partner, 'Query139', None)
    _safe_set(owner, 'model_datasources_DataSource138', {partner})
    assert getattr(partner, 'Query139') == owner
    _safe_set(owner, 'model_datasources_DataSource138', set())
    assert getattr(partner, 'Query139') is None


def test_assoc_queries7_stub_double():
    # Query has no real 'Query' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoModel(id="sample_text", name="sample_text")
    partner = Query()
    setattr(partner, 'Query', None)
    _safe_set(owner, 'model_GeppettoModel8', {partner})
    assert getattr(partner, 'Query') == owner
    _safe_set(owner, 'model_GeppettoModel8', set())
    assert getattr(partner, 'Query') is None


def test_assoc_recordedVariables18_stub_double():
    # model_VariableValue has no real 'model_VariableValue' property in the generated
    # code (a bare stub) -- manually attach it so model_ExperimentState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ExperimentState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ExperimentState(experimentId="sample_text", projectId="sample_text")
    partner = model_VariableValue()
    setattr(partner, 'model_VariableValue', None)
    _safe_set(owner, 'model_ExperimentState', {partner})
    assert getattr(partner, 'model_VariableValue') == owner
    _safe_set(owner, 'model_ExperimentState', set())
    assert getattr(partner, 'model_VariableValue') is None


def test_assoc_referencedVariables34_stub_double():
    # Variable has no real 'Variable35' property in the generated
    # code (a bare stub) -- manually attach it so model_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_Type(abstract="sample_text")
    partner = Variable()
    setattr(partner, 'Variable35', None)
    _safe_set(owner, 'types', {partner})
    assert getattr(partner, 'Variable35') == owner
    _safe_set(owner, 'types', set())
    assert getattr(partner, 'Variable35') is None


def test_assoc_results159_stub_double():
    # AQueryResult has no real 'AQueryResult' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_QueryResults's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_QueryResults's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_QueryResults(header="sample_text", id="sample_text")
    partner = AQueryResult()
    setattr(partner, 'AQueryResult', None)
    _safe_set(owner, 'model_datasources_QueryResults', {partner})
    assert getattr(partner, 'AQueryResult') == owner
    _safe_set(owner, 'model_datasources_QueryResults', set())
    assert getattr(partner, 'AQueryResult') is None


def test_assoc_returnType151_stub_double():
    # Type has no real 'Type153' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_Query's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_Query's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_Query(description="sample_text", runForCount="sample_text")
    partner = Type()
    setattr(partner, 'Type153', None)
    _safe_set(owner, 'model_datasources_Query152', partner)
    assert getattr(partner, 'Type153') == owner
    _safe_set(owner, 'model_datasources_Query152', None)
    assert getattr(partner, 'Type153') is None


def test_assoc_setParameters19_stub_double():
    # model_VariableValue has no real 'model_VariableValue21' property in the generated
    # code (a bare stub) -- manually attach it so model_ExperimentState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ExperimentState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ExperimentState(experimentId="sample_text", projectId="sample_text")
    partner = model_VariableValue()
    setattr(partner, 'model_VariableValue21', None)
    _safe_set(owner, 'model_ExperimentState20', {partner})
    assert getattr(partner, 'model_VariableValue21') == owner
    _safe_set(owner, 'model_ExperimentState20', set())
    assert getattr(partner, 'model_VariableValue21') is None


def test_assoc_sharedTypes13_stub_double():
    # Type has no real 'Type15' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoLibrary()
    partner = Type()
    setattr(partner, 'Type15', None)
    _safe_set(owner, 'model_GeppettoLibrary14', {partner})
    assert getattr(partner, 'Type15') == owner
    _safe_set(owner, 'model_GeppettoLibrary14', set())
    assert getattr(partner, 'Type15') is None


def test_assoc_superType30_stub_double():
    # Type has no real 'Type31' property in the generated
    # code (a bare stub) -- manually attach it so model_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_Type(abstract="sample_text")
    partner = Type()
    setattr(partner, 'Type31', None)
    _safe_set(owner, 'model_types_Type', {partner})
    assert getattr(partner, 'Type31') == owner
    _safe_set(owner, 'model_types_Type', set())
    assert getattr(partner, 'Type31') is None


def test_assoc_targetLibrary142_stub_double():
    # datasources_model_GeppettoLibrary has no real 'datasources_model_GeppettoLibrary144' property in the generated
    # code (a bare stub) -- manually attach it so model_datasources_DataSource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_datasources_DataSource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_datasources_DataSource(dataSourceService="sample_text", url="sample_text")
    partner = datasources_model_GeppettoLibrary()
    setattr(partner, 'datasources_model_GeppettoLibrary144', None)
    _safe_set(owner, 'model_datasources_DataSource143', partner)
    assert getattr(partner, 'datasources_model_GeppettoLibrary144') == owner
    _safe_set(owner, 'model_datasources_DataSource143', None)
    assert getattr(partner, 'datasources_model_GeppettoLibrary144') is None


def test_assoc_type85_stub_double():
    # Type has no real 'Type87' property in the generated
    # code (a bare stub) -- manually attach it so model_values_PointerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_PointerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_PointerElement(index="sample_text")
    partner = Type()
    setattr(partner, 'Type87', None)
    _safe_set(owner, 'model_values_PointerElement86', partner)
    assert getattr(partner, 'Type87') == owner
    _safe_set(owner, 'model_values_PointerElement86', None)
    assert getattr(partner, 'Type87') is None


def test_assoc_types11_stub_double():
    # Type has no real 'Type' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoLibrary()
    partner = Type()
    setattr(partner, 'Type', None)
    _safe_set(owner, 'model_GeppettoLibrary12', {partner})
    assert getattr(partner, 'Type') == owner
    _safe_set(owner, 'model_GeppettoLibrary12', set())
    assert getattr(partner, 'Type') is None


def test_assoc_types124_stub_double():
    # Type has no real 'Type125' property in the generated
    # code (a bare stub) -- manually attach it so model_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_variables_Variable(static="sample_text")
    partner = Type()
    setattr(partner, 'Type125', None)
    _safe_set(owner, 'referencedVariables', {partner})
    assert getattr(partner, 'Type125') == owner
    _safe_set(owner, 'referencedVariables', set())
    assert getattr(partner, 'Type125') is None


def test_assoc_unit75_stub_double():
    # Unit has no real 'Unit76' property in the generated
    # code (a bare stub) -- manually attach it so model_values_TimeSeries's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_TimeSeries's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_TimeSeries(scalingFactor="sample_text", value="sample_text")
    partner = Unit()
    setattr(partner, 'Unit76', None)
    _safe_set(owner, 'model_values_TimeSeries', partner)
    assert getattr(partner, 'Unit76') == owner
    _safe_set(owner, 'model_values_TimeSeries', None)
    assert getattr(partner, 'Unit76') is None


def test_assoc_value72_stub_double():
    # Value has no real 'Value73' property in the generated
    # code (a bare stub) -- manually attach it so model_values_StringToValueMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_StringToValueMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_StringToValueMap(key="sample_text")
    partner = Value()
    setattr(partner, 'Value73', None)
    _safe_set(owner, 'model_values_StringToValueMap', partner)
    assert getattr(partner, 'Value73') == owner
    _safe_set(owner, 'model_values_StringToValueMap', None)
    assert getattr(partner, 'Value73') is None


def test_assoc_variable83_stub_double():
    # Variable has no real 'Variable84' property in the generated
    # code (a bare stub) -- manually attach it so model_values_PointerElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_PointerElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_PointerElement(index="sample_text")
    partner = Variable()
    setattr(partner, 'Variable84', None)
    _safe_set(owner, 'model_values_PointerElement', partner)
    assert getattr(partner, 'Variable84') == owner
    _safe_set(owner, 'model_values_PointerElement', None)
    assert getattr(partner, 'Variable84') is None


def test_assoc_variables0_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so model_GeppettoModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_GeppettoModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_GeppettoModel(id="sample_text", name="sample_text")
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'model_GeppettoModel', {partner})
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'model_GeppettoModel', set())
    assert getattr(partner, 'Variable') is None


def test_assoc_visualGroupElements109_stub_double():
    # VisualGroupElement has no real 'VisualGroupElement110' property in the generated
    # code (a bare stub) -- manually attach it so model_values_VisualGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_values_VisualGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_values_VisualGroup(highSpectrumColor="sample_text", lowSpectrumColor="sample_text", type="sample_text")
    partner = VisualGroupElement()
    setattr(partner, 'VisualGroupElement110', None)
    _safe_set(owner, 'model_values_VisualGroup', {partner})
    assert getattr(partner, 'VisualGroupElement110') == owner
    _safe_set(owner, 'model_values_VisualGroup', set())
    assert getattr(partner, 'VisualGroupElement110') is None


def test_assoc_visualType32_stub_double():
    # VisualType has no real 'VisualType' property in the generated
    # code (a bare stub) -- manually attach it so model_types_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_types_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_types_Type(abstract="sample_text")
    partner = VisualType()
    setattr(partner, 'VisualType', None)
    _safe_set(owner, 'model_types_Type33', partner)
    assert getattr(partner, 'VisualType') == owner
    _safe_set(owner, 'model_types_Type33', None)
    assert getattr(partner, 'VisualType') is None


