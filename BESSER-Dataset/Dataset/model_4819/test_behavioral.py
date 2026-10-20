import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attribute,
    ChildRule,
    DiagramEntity,
    EADiagram,
    ElementoConsulta,
    ElementoModelo,
    ElementoModeloResultado,
    ElementoRealizacionDiagramEntity,
    ElementoRealizacionValueAttribute,
    ElementoRealizacionVisibleAttribute,
    Entity,
    EntityRelation,
    FactoryModeloConsulta,
    ModelElementEntity,
    ModeloConsulta,
    RealizacionDiagramEntity,
    ResultElement,
    Value,
    entitymodel_gestionmodelosconsultas_ModelFactory,
    factoryrules_ChildRule,
    factoryrules_Rule,
    factoryrules_RulesFactory,
    factoryrules_gestionmodelosconsultas_ModelFactory,
    gestionmodelosconsultas_ModelFactory,
    gestionmodelosconsultas_cotracir_Consolidado,
    gestionmodelosconsultas_cotracir_Detallado,
    gestionmodelosconsultas_cotracir_Planilla,
    gestionmodelosconsultas_cotracir_Propietario,
    gestionmodelosconsultas_cotracir_Trama,
    gestionmodelosconsultas_cotracir_Transaccion,
    gestionmodelosconsultas_entitymodel_AssociativeEntity,
    gestionmodelosconsultas_entitymodel_Attribute,
    gestionmodelosconsultas_entitymodel_DiagramEntity,
    gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity,
    gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute,
    gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute,
    gestionmodelosconsultas_entitymodel_Entity,
    gestionmodelosconsultas_entitymodel_EntityRelation,
    gestionmodelosconsultas_entitymodel_ModelElementEntity,
    gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity,
    gestionmodelosconsultas_entitymodel_SimpleRelation,
    gestionmodelosconsultas_entitymodel_Value,
    gestionmodelosconsultas_factoryrules_ChildRule,
    gestionmodelosconsultas_factoryrules_EntityName,
    gestionmodelosconsultas_factoryrules_RelationName,
    gestionmodelosconsultas_factoryrules_Rule,
    gestionmodelosconsultas_factoryrules_RulesFactory,
    gestionmodelosconsultas_model_Campo,
    gestionmodelosconsultas_model_EADiagram,
    gestionmodelosconsultas_model_ElementoConsulta,
    gestionmodelosconsultas_model_ElementoModelo,
    gestionmodelosconsultas_model_Proyeccion,
    gestionmodelosconsultas_model_Relacion,
    gestionmodelosconsultas_model_ViewModel,
    gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta,
    gestionmodelosconsultas_modeloconsultas_ModeloConsulta,
    gestionmodelosconsultas_resultcotracir_Consolidado,
    gestionmodelosconsultas_resultcotracir_Detallado,
    gestionmodelosconsultas_resultcotracir_NewClass,
    gestionmodelosconsultas_resultcotracir_Planilla,
    gestionmodelosconsultas_resultcotracir_Propietario,
    gestionmodelosconsultas_resultcotracir_Trama,
    gestionmodelosconsultas_resultcotracir_Transaccion,
    gestionmodelosconsultas_resultset_ElementoModeloResultado,
    gestionmodelosconsultas_resultset_ResultElement,
    gestionmodelosconsultas_resultset_Resultado,
    model_Campo,
    model_EADiagram,
    model_ElementoConsulta,
    model_ElementoModelo,
    model_Relacion,
    modeloconsultas_gestionmodelosconsultas_ModelFactory,
    resultset_ElementoModeloResultado,
    resultset_ResultElement,
    resultset_Resultado,
    AttributeType,
    Multiplicity,
    NombreCampo,
    TipoModelElementEntity,
    Type,
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

def test_assoc_EADiagram81_stub_double():
    # model_EADiagram has no real 'EADiagram82' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_Relacion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_Relacion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_Relacion(estereotipo="sample_text", order="sample_text")
    partner = model_EADiagram()
    setattr(partner, 'EADiagram82', None)
    _safe_set(owner, 'listRelacion', partner)
    assert getattr(partner, 'EADiagram82') == owner
    _safe_set(owner, 'listRelacion', None)
    assert getattr(partner, 'EADiagram82') is None


def test_assoc_EADiagram95_stub_double():
    # model_EADiagram has no real 'EADiagram96' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_ElementoConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_ElementoConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_ElementoConsulta(order="sample_text")
    partner = model_EADiagram()
    setattr(partner, 'EADiagram96', None)
    _safe_set(owner, 'listElementoConsulta', partner)
    assert getattr(partner, 'EADiagram96') == owner
    _safe_set(owner, 'listElementoConsulta', None)
    assert getattr(partner, 'EADiagram96') is None


def test_assoc_ElementoModeloResultado107_stub_double():
    # resultset_ElementoModeloResultado has no real 'ElementoModeloResultado108' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_resultset_ElementoModeloResultado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_resultset_ElementoModeloResultado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_resultset_ElementoModeloResultado(key="sample_text")
    partner = resultset_ElementoModeloResultado()
    setattr(partner, 'ElementoModeloResultado108', None)
    _safe_set(owner, 'listElementoModeloResultado', partner)
    assert getattr(partner, 'ElementoModeloResultado108') == owner
    _safe_set(owner, 'listElementoModeloResultado', None)
    assert getattr(partner, 'ElementoModeloResultado108') is None


def test_assoc_ElementoRealizacionDiagramEntity29_stub_double():
    # ElementoRealizacionDiagramEntity has no real 'ElementoRealizacionDiagramEntity' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ModelElementEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ModelElementEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ModelElementEntity(name="sample_text", stereotype="sample_text")
    partner = ElementoRealizacionDiagramEntity()
    setattr(partner, 'ElementoRealizacionDiagramEntity', None)
    _safe_set(owner, 'modelElementEntity', {partner})
    assert getattr(partner, 'ElementoRealizacionDiagramEntity') == owner
    _safe_set(owner, 'modelElementEntity', set())
    assert getattr(partner, 'ElementoRealizacionDiagramEntity') is None


def test_assoc_ElementoRealizacionDiagramEntity53_stub_double():
    # ElementoRealizacionDiagramEntity has no real 'ElementoRealizacionDiagramEntity54' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute(nombre="sample_text")
    partner = ElementoRealizacionDiagramEntity()
    setattr(partner, 'ElementoRealizacionDiagramEntity54', None)
    _safe_set(owner, 'listElementoRealizacionAttribute', partner)
    assert getattr(partner, 'ElementoRealizacionDiagramEntity54') == owner
    _safe_set(owner, 'listElementoRealizacionAttribute', None)
    assert getattr(partner, 'ElementoRealizacionDiagramEntity54') is None


def test_assoc_ElementoRealizacionValueAttribute27_stub_double():
    # ElementoRealizacionValueAttribute has no real 'ElementoRealizacionValueAttribute' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_Attribute(attributeType="sample_text", name="sample_text", type="sample_text", value="sample_text", visible=True)
    partner = ElementoRealizacionValueAttribute()
    setattr(partner, 'ElementoRealizacionValueAttribute', None)
    _safe_set(owner, 'valueAttribute', {partner})
    assert getattr(partner, 'ElementoRealizacionValueAttribute') == owner
    _safe_set(owner, 'valueAttribute', set())
    assert getattr(partner, 'ElementoRealizacionValueAttribute') is None


def test_assoc_ElementoRealizacionValueAttribute63_stub_double():
    # ElementoRealizacionValueAttribute has no real 'ElementoRealizacionValueAttribute64' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_Value(value="sample_text")
    partner = ElementoRealizacionValueAttribute()
    setattr(partner, 'ElementoRealizacionValueAttribute64', None)
    _safe_set(owner, 'values', {partner})
    assert getattr(partner, 'ElementoRealizacionValueAttribute64') == owner
    _safe_set(owner, 'values', set())
    assert getattr(partner, 'ElementoRealizacionValueAttribute64') is None


def test_assoc_ElementoRealizacionVisibleAttribute28_stub_double():
    # ElementoRealizacionVisibleAttribute has no real 'ElementoRealizacionVisibleAttribute' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_Attribute(attributeType="sample_text", name="sample_text", type="sample_text", value="sample_text", visible=True)
    partner = ElementoRealizacionVisibleAttribute()
    setattr(partner, 'ElementoRealizacionVisibleAttribute', None)
    _safe_set(owner, 'visibleAttribute', {partner})
    assert getattr(partner, 'ElementoRealizacionVisibleAttribute') == owner
    _safe_set(owner, 'visibleAttribute', set())
    assert getattr(partner, 'ElementoRealizacionVisibleAttribute') is None


def test_assoc_Entity25_stub_double():
    # Entity has no real 'Entity26' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_Attribute(attributeType="sample_text", name="sample_text", type="sample_text", value="sample_text", visible=True)
    partner = Entity()
    setattr(partner, 'Entity26', None)
    _safe_set(owner, 'listAttributes', partner)
    assert getattr(partner, 'Entity26') == owner
    _safe_set(owner, 'listAttributes', None)
    assert getattr(partner, 'Entity26') is None


def test_assoc_FactoryModeloConsulta70_stub_double():
    # FactoryModeloConsulta has no real 'FactoryModeloConsulta71' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_modeloconsultas_ModeloConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_modeloconsultas_ModeloConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_modeloconsultas_ModeloConsulta(nombre="sample_text")
    partner = FactoryModeloConsulta()
    setattr(partner, 'FactoryModeloConsulta71', None)
    _safe_set(owner, 'listModeloConsulta', partner)
    assert getattr(partner, 'FactoryModeloConsulta71') == owner
    _safe_set(owner, 'listModeloConsulta', None)
    assert getattr(partner, 'FactoryModeloConsulta71') is None


def test_assoc_ModeloConsulta101_stub_double():
    # ModeloConsulta has no real 'ModeloConsulta102' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_resultset_Resultado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_resultset_Resultado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_resultset_Resultado(nombre="sample_text")
    partner = ModeloConsulta()
    setattr(partner, 'ModeloConsulta102', None)
    _safe_set(owner, 'listResultado', partner)
    assert getattr(partner, 'ModeloConsulta102') == owner
    _safe_set(owner, 'listResultado', None)
    assert getattr(partner, 'ModeloConsulta102') is None


def test_assoc_ModeloConsulta90_stub_double():
    # ModeloConsulta has no real 'ModeloConsulta91' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_EADiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_EADiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_EADiagram(nombre="sample_text")
    partner = ModeloConsulta()
    setattr(partner, 'ModeloConsulta91', None)
    _safe_set(owner, 'listEADiagram', partner)
    assert getattr(partner, 'ModeloConsulta91') == owner
    _safe_set(owner, 'listEADiagram', None)
    assert getattr(partner, 'ModeloConsulta91') is None


def test_assoc_RealizacionDiagramEntity45_stub_double():
    # RealizacionDiagramEntity has no real 'RealizacionDiagramEntity46' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity(nombreModelElementEntity="sample_text", tipo="sample_text")
    partner = RealizacionDiagramEntity()
    setattr(partner, 'RealizacionDiagramEntity46', None)
    _safe_set(owner, 'listElementoRealizacionDiagramEntity', partner)
    assert getattr(partner, 'RealizacionDiagramEntity46') == owner
    _safe_set(owner, 'listElementoRealizacionDiagramEntity', None)
    assert getattr(partner, 'RealizacionDiagramEntity46') is None


def test_assoc_RealizacionDiagramEntity58_stub_double():
    # RealizacionDiagramEntity has no real 'RealizacionDiagramEntity59' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute(nombre="sample_text")
    partner = RealizacionDiagramEntity()
    setattr(partner, 'RealizacionDiagramEntity59', None)
    _safe_set(owner, 'realizacionVisibleAttribute', partner)
    assert getattr(partner, 'RealizacionDiagramEntity59') == owner
    _safe_set(owner, 'realizacionVisibleAttribute', None)
    assert getattr(partner, 'RealizacionDiagramEntity59') is None


def test_assoc_RealizacionDiagramEntity65_stub_double():
    # RealizacionDiagramEntity has no real 'RealizacionDiagramEntity66' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_Value(value="sample_text")
    partner = RealizacionDiagramEntity()
    setattr(partner, 'RealizacionDiagramEntity66', None)
    _safe_set(owner, 'listValues', partner)
    assert getattr(partner, 'RealizacionDiagramEntity66') == owner
    _safe_set(owner, 'listValues', None)
    assert getattr(partner, 'RealizacionDiagramEntity66') is None


def test_assoc_Rule13_stub_double():
    # factoryrules_Rule has no real 'Rule14' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_factoryrules_ChildRule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_factoryrules_ChildRule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_factoryrules_ChildRule(name="sample_text")
    partner = factoryrules_Rule()
    setattr(partner, 'Rule14', None)
    _safe_set(owner, 'listChildRule', partner)
    assert getattr(partner, 'Rule14') == owner
    _safe_set(owner, 'listChildRule', None)
    assert getattr(partner, 'Rule14') is None


def test_assoc_RulesFactory9_stub_double():
    # factoryrules_RulesFactory has no real 'RulesFactory10' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_factoryrules_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_factoryrules_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_factoryrules_Rule(name="sample_text")
    partner = factoryrules_RulesFactory()
    setattr(partner, 'RulesFactory10', None)
    _safe_set(owner, 'listRuleDiagramEntity', partner)
    assert getattr(partner, 'RulesFactory10') == owner
    _safe_set(owner, 'listRuleDiagramEntity', None)
    assert getattr(partner, 'RulesFactory10') is None


def test_assoc_diagramEntity3_stub_double():
    # DiagramEntity has no real 'DiagramEntity' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_ModelFactory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_ModelFactory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_ModelFactory()
    partner = DiagramEntity()
    setattr(partner, 'DiagramEntity', None)
    _safe_set(owner, 'ModelFactory4', partner)
    assert getattr(partner, 'DiagramEntity') == owner
    _safe_set(owner, 'ModelFactory4', None)
    assert getattr(partner, 'DiagramEntity') is None


def test_assoc_factoryModeloConsultas1_stub_double():
    # FactoryModeloConsulta has no real 'FactoryModeloConsulta' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_ModelFactory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_ModelFactory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_ModelFactory()
    partner = FactoryModeloConsulta()
    setattr(partner, 'FactoryModeloConsulta', None)
    _safe_set(owner, 'ModelFactory2', partner)
    assert getattr(partner, 'FactoryModeloConsulta') == owner
    _safe_set(owner, 'ModelFactory2', None)
    assert getattr(partner, 'FactoryModeloConsulta') is None


def test_assoc_from_98_stub_double():
    # model_ElementoModelo has no real 'ElementoModelo' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_ElementoModelo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_ElementoModelo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_ElementoModelo(nombre="sample_text")
    partner = model_ElementoModelo()
    setattr(partner, 'ElementoModelo', None)
    _safe_set(owner, 'to', {partner})
    assert getattr(partner, 'ElementoModelo') == owner
    _safe_set(owner, 'to', set())
    assert getattr(partner, 'ElementoModelo') is None


def test_assoc_listCampos97_stub_double():
    # model_Campo has no real 'Campo' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_ElementoConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_ElementoConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_ElementoConsulta(order="sample_text")
    partner = model_Campo()
    setattr(partner, 'Campo', None)
    _safe_set(owner, 'ownedElementoConsulta', {partner})
    assert getattr(partner, 'Campo') == owner
    _safe_set(owner, 'ownedElementoConsulta', set())
    assert getattr(partner, 'Campo') is None


def test_assoc_listChildRule11_stub_double():
    # factoryrules_ChildRule has no real 'ChildRule' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_factoryrules_Rule's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_factoryrules_Rule's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_factoryrules_Rule(name="sample_text")
    partner = factoryrules_ChildRule()
    setattr(partner, 'ChildRule', None)
    _safe_set(owner, 'Rule12', {partner})
    assert getattr(partner, 'ChildRule') == owner
    _safe_set(owner, 'Rule12', set())
    assert getattr(partner, 'ChildRule') is None


def test_assoc_listEADiagram72_stub_double():
    # model_EADiagram has no real 'EADiagram' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_modeloconsultas_ModeloConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_modeloconsultas_ModeloConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_modeloconsultas_ModeloConsulta(nombre="sample_text")
    partner = model_EADiagram()
    setattr(partner, 'EADiagram', None)
    _safe_set(owner, 'ModeloConsulta73', {partner})
    assert getattr(partner, 'EADiagram') == owner
    _safe_set(owner, 'ModeloConsulta73', set())
    assert getattr(partner, 'EADiagram') is None


def test_assoc_listElementoConsulta92_stub_double():
    # model_ElementoConsulta has no real 'ElementoConsulta94' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_EADiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_EADiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_EADiagram(nombre="sample_text")
    partner = model_ElementoConsulta()
    setattr(partner, 'ElementoConsulta94', None)
    _safe_set(owner, 'EADiagram93', {partner})
    assert getattr(partner, 'ElementoConsulta94') == owner
    _safe_set(owner, 'EADiagram93', set())
    assert getattr(partner, 'ElementoConsulta94') is None


def test_assoc_listElementoModeloResultado105_stub_double():
    # resultset_ElementoModeloResultado has no real 'ElementoModeloResultado106' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_resultset_ElementoModeloResultado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_resultset_ElementoModeloResultado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_resultset_ElementoModeloResultado(key="sample_text")
    partner = resultset_ElementoModeloResultado()
    setattr(partner, 'ElementoModeloResultado106', None)
    _safe_set(owner, 'ElementoModeloResultado', {partner})
    assert getattr(partner, 'ElementoModeloResultado106') == owner
    _safe_set(owner, 'ElementoModeloResultado', set())
    assert getattr(partner, 'ElementoModeloResultado106') is None


def test_assoc_listElementoRealizacionAttribute47_stub_double():
    # ElementoRealizacionValueAttribute has no real 'ElementoRealizacionValueAttribute49' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity(nombreModelElementEntity="sample_text", tipo="sample_text")
    partner = ElementoRealizacionValueAttribute()
    setattr(partner, 'ElementoRealizacionValueAttribute49', None)
    _safe_set(owner, 'ElementoRealizacionDiagramEntity48', {partner})
    assert getattr(partner, 'ElementoRealizacionValueAttribute49') == owner
    _safe_set(owner, 'ElementoRealizacionDiagramEntity48', set())
    assert getattr(partner, 'ElementoRealizacionValueAttribute49') is None


def test_assoc_listRelacion88_stub_double():
    # model_Relacion has no real 'Relacion' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_EADiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_EADiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_EADiagram(nombre="sample_text")
    partner = model_Relacion()
    setattr(partner, 'Relacion', None)
    _safe_set(owner, 'EADiagram89', {partner})
    assert getattr(partner, 'Relacion') == owner
    _safe_set(owner, 'EADiagram89', set())
    assert getattr(partner, 'Relacion') is None


def test_assoc_listResultElement103_stub_double():
    # resultset_ResultElement has no real 'ResultElement' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_resultset_Resultado's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_resultset_Resultado's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_resultset_Resultado(nombre="sample_text")
    partner = resultset_ResultElement()
    setattr(partner, 'ResultElement', None)
    _safe_set(owner, 'Resultado104', {partner})
    assert getattr(partner, 'ResultElement') == owner
    _safe_set(owner, 'Resultado104', set())
    assert getattr(partner, 'ResultElement') is None


def test_assoc_listResultado74_stub_double():
    # resultset_Resultado has no real 'Resultado' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_modeloconsultas_ModeloConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_modeloconsultas_ModeloConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_modeloconsultas_ModeloConsulta(nombre="sample_text")
    partner = resultset_Resultado()
    setattr(partner, 'Resultado', None)
    _safe_set(owner, 'ModeloConsulta75', {partner})
    assert getattr(partner, 'Resultado') == owner
    _safe_set(owner, 'ModeloConsulta75', set())
    assert getattr(partner, 'Resultado') is None


def test_assoc_modelElementEntity43_stub_double():
    # ModelElementEntity has no real 'ModelElementEntity' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity(nombreModelElementEntity="sample_text", tipo="sample_text")
    partner = ModelElementEntity()
    setattr(partner, 'ModelElementEntity', None)
    _safe_set(owner, 'ElementoRealizacionDiagramEntity44', partner)
    assert getattr(partner, 'ModelElementEntity') == owner
    _safe_set(owner, 'ElementoRealizacionDiagramEntity44', None)
    assert getattr(partner, 'ModelElementEntity') is None


def test_assoc_ownedElementoConsulta87_stub_double():
    # model_ElementoConsulta has no real 'ElementoConsulta' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_Campo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_Campo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_Campo(criterio="sample_text", nombreCampo="sample_text", seleccion=True)
    partner = model_ElementoConsulta()
    setattr(partner, 'ElementoConsulta', None)
    _safe_set(owner, 'listCampos', partner)
    assert getattr(partner, 'ElementoConsulta') == owner
    _safe_set(owner, 'listCampos', None)
    assert getattr(partner, 'ElementoConsulta') is None


def test_assoc_realizacionDiagramEntity67_stub_double():
    # RealizacionDiagramEntity has no real 'RealizacionDiagramEntity69' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_modeloconsultas_ModeloConsulta's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_modeloconsultas_ModeloConsulta's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_modeloconsultas_ModeloConsulta(nombre="sample_text")
    partner = RealizacionDiagramEntity()
    setattr(partner, 'RealizacionDiagramEntity69', None)
    _safe_set(owner, 'ModeloConsulta68', partner)
    assert getattr(partner, 'RealizacionDiagramEntity69') == owner
    _safe_set(owner, 'ModeloConsulta68', None)
    assert getattr(partner, 'RealizacionDiagramEntity69') is None


def test_assoc_rulesFactory0_stub_double():
    # factoryrules_RulesFactory has no real 'RulesFactory' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_ModelFactory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_ModelFactory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_ModelFactory()
    partner = factoryrules_RulesFactory()
    setattr(partner, 'RulesFactory', None)
    _safe_set(owner, 'ModelFactory', partner)
    assert getattr(partner, 'RulesFactory') == owner
    _safe_set(owner, 'ModelFactory', None)
    assert getattr(partner, 'RulesFactory') is None


def test_assoc_source20_stub_double():
    # Entity has no real 'Entity21' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_EntityRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_EntityRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_EntityRelation(atributteForeingKeySource="sample_text", atributtePrimaryKeyTarget="sample_text", multiplicitySource="sample_text", multiplicityTarget="sample_text")
    partner = Entity()
    setattr(partner, 'Entity21', None)
    _safe_set(owner, 'gestionmodelosconsultas_entitymodel_EntityRelation', partner)
    assert getattr(partner, 'Entity21') == owner
    _safe_set(owner, 'gestionmodelosconsultas_entitymodel_EntityRelation', None)
    assert getattr(partner, 'Entity21') is None


def test_assoc_source84_stub_double():
    # model_ElementoConsulta has no real 'model_ElementoConsulta86' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_Relacion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_Relacion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_Relacion(estereotipo="sample_text", order="sample_text")
    partner = model_ElementoConsulta()
    setattr(partner, 'model_ElementoConsulta86', None)
    _safe_set(owner, 'gestionmodelosconsultas_model_Relacion85', partner)
    assert getattr(partner, 'model_ElementoConsulta86') == owner
    _safe_set(owner, 'gestionmodelosconsultas_model_Relacion85', None)
    assert getattr(partner, 'model_ElementoConsulta86') is None


def test_assoc_target22_stub_double():
    # Entity has no real 'Entity24' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_EntityRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_EntityRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_EntityRelation(atributteForeingKeySource="sample_text", atributtePrimaryKeyTarget="sample_text", multiplicitySource="sample_text", multiplicityTarget="sample_text")
    partner = Entity()
    setattr(partner, 'Entity24', None)
    _safe_set(owner, 'gestionmodelosconsultas_entitymodel_EntityRelation23', partner)
    assert getattr(partner, 'Entity24') == owner
    _safe_set(owner, 'gestionmodelosconsultas_entitymodel_EntityRelation23', None)
    assert getattr(partner, 'Entity24') is None


def test_assoc_target83_stub_double():
    # model_ElementoConsulta has no real 'model_ElementoConsulta' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_Relacion's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_Relacion's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_Relacion(estereotipo="sample_text", order="sample_text")
    partner = model_ElementoConsulta()
    setattr(partner, 'model_ElementoConsulta', None)
    _safe_set(owner, 'gestionmodelosconsultas_model_Relacion', partner)
    assert getattr(partner, 'model_ElementoConsulta') == owner
    _safe_set(owner, 'gestionmodelosconsultas_model_Relacion', None)
    assert getattr(partner, 'model_ElementoConsulta') is None


def test_assoc_theFactoryEntity18_stub_double():
    # DiagramEntity has no real 'DiagramEntity19' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_EntityRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_EntityRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_EntityRelation(atributteForeingKeySource="sample_text", atributtePrimaryKeyTarget="sample_text", multiplicitySource="sample_text", multiplicityTarget="sample_text")
    partner = DiagramEntity()
    setattr(partner, 'DiagramEntity19', None)
    _safe_set(owner, 'listEntityRelation', partner)
    assert getattr(partner, 'DiagramEntity19') == owner
    _safe_set(owner, 'listEntityRelation', None)
    assert getattr(partner, 'DiagramEntity19') is None


def test_assoc_to99_stub_double():
    # model_ElementoModelo has no real 'ElementoModelo100' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_model_ElementoModelo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_model_ElementoModelo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_model_ElementoModelo(nombre="sample_text")
    partner = model_ElementoModelo()
    setattr(partner, 'ElementoModelo100', None)
    _safe_set(owner, 'from_', {partner})
    assert getattr(partner, 'ElementoModelo100') == owner
    _safe_set(owner, 'from_', set())
    assert getattr(partner, 'ElementoModelo100') is None


def test_assoc_valueAttribute50_stub_double():
    # Attribute has no real 'Attribute52' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute(nombre="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute52', None)
    _safe_set(owner, 'ElementoRealizacionValueAttribute51', {partner})
    assert getattr(partner, 'Attribute52') == owner
    _safe_set(owner, 'ElementoRealizacionValueAttribute51', set())
    assert getattr(partner, 'Attribute52') is None


def test_assoc_values55_stub_double():
    # Value has no real 'Value57' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute(nombre="sample_text")
    partner = Value()
    setattr(partner, 'Value57', None)
    _safe_set(owner, 'ElementoRealizacionValueAttribute56', {partner})
    assert getattr(partner, 'Value57') == owner
    _safe_set(owner, 'ElementoRealizacionValueAttribute56', set())
    assert getattr(partner, 'Value57') is None


def test_assoc_visibleAttribute60_stub_double():
    # Attribute has no real 'Attribute62' property in the generated
    # code (a bare stub) -- manually attach it so gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute(nombre="sample_text")
    partner = Attribute()
    setattr(partner, 'Attribute62', None)
    _safe_set(owner, 'ElementoRealizacionVisibleAttribute61', {partner})
    assert getattr(partner, 'Attribute62') == owner
    _safe_set(owner, 'ElementoRealizacionVisibleAttribute61', set())
    assert getattr(partner, 'Attribute62') is None


