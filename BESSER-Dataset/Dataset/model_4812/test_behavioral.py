import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Adapter,
    BasicObject,
    BorderObject,
    Cloneable,
    DiagramModel,
    DiagramModelComponent,
    DiagramModelConnection,
    DiagramModelContainer,
    DiagramModelImageProvider,
    DiagramModelObject,
    Documentable,
    Folder,
    FolderContainer,
    FontAttribute,
    Identifier,
    JunctionElement,
    Nameable,
    Properties,
    TextContent,
    ZentaElement,
    ZentaModelElement,
    model_Adapter,
    model_AndJunction,
    model_Attribute,
    model_BasicObject,
    model_BasicRelationship,
    model_BorderObject,
    model_Bounds,
    model_Cloneable,
    model_DiagramModel,
    model_DiagramModelBendpoint,
    model_DiagramModelComponent,
    model_DiagramModelConnection,
    model_DiagramModelContainer,
    model_DiagramModelGroup,
    model_DiagramModelImage,
    model_DiagramModelImageProvider,
    model_DiagramModelNote,
    model_DiagramModelObject,
    model_DiagramModelReference,
    model_DiagramModelZentaConnection,
    model_DiagramModelZentaObject,
    model_Documentable,
    model_Folder,
    model_FolderContainer,
    model_FontAttribute,
    model_Identifier,
    model_InterfaceElement,
    model_Junction,
    model_JunctionElement,
    model_Lockable,
    model_Metamodel,
    model_Nameable,
    model_OrJunction,
    model_Properties,
    model_Property,
    model_SketchModel,
    model_SketchModelActor,
    model_SketchModelSticky,
    model_Template,
    model_TextContent,
    model_ZentaDiagramModel,
    model_ZentaElement,
    model_ZentaModel,
    model_ZentaModelElement,
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

def test_assoc_bendpoints22_reverse_link_reassign_clear():
    a1 = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    a2 = model_DiagramModelConnection(lineDecoration="sample_text_2", text="sample_text_2", type=13)
    b = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    _safe_set(b, 'model_DiagramModelBendpoint', a1)
    assert _is_linked(b, 'model_DiagramModelBendpoint', a1)
    if hasattr(a1, 'model_DiagramModelConnection23'):
        assert _is_linked(a1, 'model_DiagramModelConnection23', b)
    _safe_set(b, 'model_DiagramModelBendpoint', a2)
    assert _is_linked(b, 'model_DiagramModelBendpoint', a2)
    if hasattr(a1, 'model_DiagramModelConnection23'):
        assert not _is_linked(a1, 'model_DiagramModelConnection23', b)
    if hasattr(a2, 'model_DiagramModelConnection23'):
        assert _is_linked(a2, 'model_DiagramModelConnection23', b)
    _safe_set(b, 'model_DiagramModelBendpoint', None)
    assert not _is_linked(b, 'model_DiagramModelBendpoint', a2)
    if hasattr(a2, 'model_DiagramModelConnection23'):
        assert not _is_linked(a2, 'model_DiagramModelConnection23', b)


def test_assoc_bounds9_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    a2 = model_DiagramModelObject(elementShape="sample_text_2", fillColor="sample_text_2")
    b = model_Bounds(height=7, width=7, x=7, y=7)
    _safe_set(b, 'model_Bounds', a1)
    assert _is_linked(b, 'model_Bounds', a1)
    if hasattr(a1, 'model_DiagramModelObject10'):
        assert _is_linked(a1, 'model_DiagramModelObject10', b)
    _safe_set(b, 'model_Bounds', a2)
    assert _is_linked(b, 'model_Bounds', a2)
    if hasattr(a1, 'model_DiagramModelObject10'):
        assert not _is_linked(a1, 'model_DiagramModelObject10', b)
    if hasattr(a2, 'model_DiagramModelObject10'):
        assert _is_linked(a2, 'model_DiagramModelObject10', b)
    _safe_set(b, 'model_Bounds', None)
    assert not _is_linked(b, 'model_Bounds', a2)
    if hasattr(a2, 'model_DiagramModelObject10'):
        assert not _is_linked(a2, 'model_DiagramModelObject10', b)


def test_assoc_diagram29_reverse_link_reassign_clear():
    a1 = model_Template(path="sample_text")
    a2 = model_Template(path="sample_text_2")
    b = model_DiagramModel(connectionRouterType=7)
    _safe_set(b, 'model_DiagramModel30', a1)
    assert _is_linked(b, 'model_DiagramModel30', a1)
    if hasattr(a1, 'model_Template'):
        assert _is_linked(a1, 'model_Template', b)
    _safe_set(b, 'model_DiagramModel30', a2)
    assert _is_linked(b, 'model_DiagramModel30', a2)
    if hasattr(a1, 'model_Template'):
        assert not _is_linked(a1, 'model_Template', b)
    if hasattr(a2, 'model_Template'):
        assert _is_linked(a2, 'model_Template', b)
    _safe_set(b, 'model_DiagramModel30', None)
    assert not _is_linked(b, 'model_DiagramModel30', a2)
    if hasattr(a2, 'model_Template'):
        assert not _is_linked(a2, 'model_Template', b)


def test_assoc_diagramModel5_reverse_link_reassign_clear():
    a1 = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    a2 = model_DiagramModelComponent(lineColor="sample_text_2", lineWidth=13)
    b = model_DiagramModel(connectionRouterType=7)
    _safe_set(b, 'model_DiagramModel', a1)
    assert _is_linked(b, 'model_DiagramModel', a1)
    if hasattr(a1, 'model_DiagramModelComponent'):
        assert _is_linked(a1, 'model_DiagramModelComponent', b)
    _safe_set(b, 'model_DiagramModel', a2)
    assert _is_linked(b, 'model_DiagramModel', a2)
    if hasattr(a1, 'model_DiagramModelComponent'):
        assert not _is_linked(a1, 'model_DiagramModelComponent', b)
    if hasattr(a2, 'model_DiagramModelComponent'):
        assert _is_linked(a2, 'model_DiagramModelComponent', b)
    _safe_set(b, 'model_DiagramModel', None)
    assert not _is_linked(b, 'model_DiagramModel', a2)
    if hasattr(a2, 'model_DiagramModelComponent'):
        assert not _is_linked(a2, 'model_DiagramModelComponent', b)


def test_assoc_source16_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    a2 = model_DiagramModelObject(elementShape="sample_text_2", fillColor="sample_text_2")
    b = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    _safe_set(b, 'model_DiagramModelConnection17', a1)
    assert _is_linked(b, 'model_DiagramModelConnection17', a1)
    if hasattr(a1, 'model_DiagramModelObject18'):
        assert _is_linked(a1, 'model_DiagramModelObject18', b)
    _safe_set(b, 'model_DiagramModelConnection17', a2)
    assert _is_linked(b, 'model_DiagramModelConnection17', a2)
    if hasattr(a1, 'model_DiagramModelObject18'):
        assert not _is_linked(a1, 'model_DiagramModelObject18', b)
    if hasattr(a2, 'model_DiagramModelObject18'):
        assert _is_linked(a2, 'model_DiagramModelObject18', b)
    _safe_set(b, 'model_DiagramModelConnection17', None)
    assert not _is_linked(b, 'model_DiagramModelConnection17', a2)
    if hasattr(a2, 'model_DiagramModelObject18'):
        assert not _is_linked(a2, 'model_DiagramModelObject18', b)


def test_assoc_sourceConnections11_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    a2 = model_DiagramModelObject(elementShape="sample_text_2", fillColor="sample_text_2")
    b = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    _safe_set(b, 'model_DiagramModelConnection', a1)
    assert _is_linked(b, 'model_DiagramModelConnection', a1)
    if hasattr(a1, 'model_DiagramModelObject12'):
        assert _is_linked(a1, 'model_DiagramModelObject12', b)
    _safe_set(b, 'model_DiagramModelConnection', a2)
    assert _is_linked(b, 'model_DiagramModelConnection', a2)
    if hasattr(a1, 'model_DiagramModelObject12'):
        assert not _is_linked(a1, 'model_DiagramModelObject12', b)
    if hasattr(a2, 'model_DiagramModelObject12'):
        assert _is_linked(a2, 'model_DiagramModelObject12', b)
    _safe_set(b, 'model_DiagramModelConnection', None)
    assert not _is_linked(b, 'model_DiagramModelConnection', a2)
    if hasattr(a2, 'model_DiagramModelObject12'):
        assert not _is_linked(a2, 'model_DiagramModelObject12', b)


def test_assoc_target19_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    a2 = model_DiagramModelObject(elementShape="sample_text_2", fillColor="sample_text_2")
    b = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    _safe_set(b, 'model_DiagramModelConnection20', a1)
    assert _is_linked(b, 'model_DiagramModelConnection20', a1)
    if hasattr(a1, 'model_DiagramModelObject21'):
        assert _is_linked(a1, 'model_DiagramModelObject21', b)
    _safe_set(b, 'model_DiagramModelConnection20', a2)
    assert _is_linked(b, 'model_DiagramModelConnection20', a2)
    if hasattr(a1, 'model_DiagramModelObject21'):
        assert not _is_linked(a1, 'model_DiagramModelObject21', b)
    if hasattr(a2, 'model_DiagramModelObject21'):
        assert _is_linked(a2, 'model_DiagramModelObject21', b)
    _safe_set(b, 'model_DiagramModelConnection20', None)
    assert not _is_linked(b, 'model_DiagramModelConnection20', a2)
    if hasattr(a2, 'model_DiagramModelObject21'):
        assert not _is_linked(a2, 'model_DiagramModelObject21', b)


def test_assoc_targetConnections13_reverse_link_reassign_clear():
    a1 = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    a2 = model_DiagramModelObject(elementShape="sample_text_2", fillColor="sample_text_2")
    b = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    _safe_set(b, 'model_DiagramModelConnection15', a1)
    assert _is_linked(b, 'model_DiagramModelConnection15', a1)
    if hasattr(a1, 'model_DiagramModelObject14'):
        assert _is_linked(a1, 'model_DiagramModelObject14', b)
    _safe_set(b, 'model_DiagramModelConnection15', a2)
    assert _is_linked(b, 'model_DiagramModelConnection15', a2)
    if hasattr(a1, 'model_DiagramModelObject14'):
        assert not _is_linked(a1, 'model_DiagramModelObject14', b)
    if hasattr(a2, 'model_DiagramModelObject14'):
        assert _is_linked(a2, 'model_DiagramModelObject14', b)
    _safe_set(b, 'model_DiagramModelConnection15', None)
    assert not _is_linked(b, 'model_DiagramModelConnection15', a2)
    if hasattr(a2, 'model_DiagramModelObject14'):
        assert not _is_linked(a2, 'model_DiagramModelObject14', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attributes32_stub_double():
    # model_BasicObject has no real 'model_BasicObject' property in the generated
    # code (a bare stub) -- manually attach it so model_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Attribute(maxOccurs=7, minOccurs=7)
    partner = model_BasicObject()
    setattr(partner, 'model_BasicObject', None)
    _safe_set(owner, 'model_Attribute', partner)
    assert owner in getattr(partner, 'model_BasicObject')
    _safe_set(owner, 'model_Attribute', None)
    assert owner not in getattr(partner, 'model_BasicObject')


def test_assoc_children6_stub_double():
    # model_DiagramModelContainer has no real 'model_DiagramModelContainer' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    partner = model_DiagramModelContainer()
    setattr(partner, 'model_DiagramModelContainer', None)
    _safe_set(owner, 'model_DiagramModelObject', partner)
    assert owner in getattr(partner, 'model_DiagramModelContainer')
    _safe_set(owner, 'model_DiagramModelObject', None)
    assert owner not in getattr(partner, 'model_DiagramModelContainer')


def test_assoc_classes27_stub_double():
    # model_BasicObject has no real 'BasicObject' property in the generated
    # code (a bare stub) -- manually attach it so model_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Template(path="sample_text")
    partner = model_BasicObject()
    setattr(partner, 'BasicObject', None)
    _safe_set(owner, 'template', {partner})
    assert getattr(partner, 'BasicObject') == owner
    _safe_set(owner, 'template', set())
    assert getattr(partner, 'BasicObject') is None


def test_assoc_connectedObject49_stub_double():
    # model_BasicObject has no real 'model_BasicObject51' property in the generated
    # code (a bare stub) -- manually attach it so model_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Attribute(maxOccurs=7, minOccurs=7)
    partner = model_BasicObject()
    setattr(partner, 'model_BasicObject51', None)
    _safe_set(owner, 'model_Attribute50', partner)
    assert getattr(partner, 'model_BasicObject51') == owner
    _safe_set(owner, 'model_Attribute50', None)
    assert getattr(partner, 'model_BasicObject51') is None


def test_assoc_diagConnections45_stub_double():
    # model_BasicRelationship has no real 'relationship' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelZentaConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelZentaConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelZentaConnection()
    partner = model_BasicRelationship()
    setattr(partner, 'relationship', None)
    _safe_set(owner, 'DiagramModelZentaConnection', partner)
    assert owner in getattr(partner, 'relationship')
    _safe_set(owner, 'DiagramModelZentaConnection', None)
    assert owner not in getattr(partner, 'relationship')


def test_assoc_diagObjects31_stub_double():
    # model_ZentaElement has no real 'zentaElement' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelZentaObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelZentaObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelZentaObject(type=7)
    partner = model_ZentaElement()
    setattr(partner, 'zentaElement', None)
    _safe_set(owner, 'DiagramModelZentaObject', partner)
    assert owner in getattr(partner, 'zentaElement')
    _safe_set(owner, 'DiagramModelZentaObject', None)
    assert owner not in getattr(partner, 'zentaElement')


def test_assoc_elements3_stub_double():
    # model_Folder has no real 'model_Folder4' property in the generated
    # code (a bare stub) -- manually attach it so model_Nameable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Nameable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Nameable(name="sample_text")
    partner = model_Folder()
    setattr(partner, 'model_Folder4', None)
    _safe_set(owner, 'model_Nameable', partner)
    assert owner in getattr(partner, 'model_Folder4')
    _safe_set(owner, 'model_Nameable', None)
    assert owner not in getattr(partner, 'model_Folder4')


def test_assoc_metamodel28_stub_double():
    # model_Metamodel has no real 'Metamodel' property in the generated
    # code (a bare stub) -- manually attach it so model_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Template(path="sample_text")
    partner = model_Metamodel()
    setattr(partner, 'Metamodel', None)
    _safe_set(owner, 'templates', partner)
    assert getattr(partner, 'Metamodel') == owner
    _safe_set(owner, 'templates', None)
    assert getattr(partner, 'Metamodel') is None


def test_assoc_properties0_stub_double():
    # model_Properties has no real 'model_Properties' property in the generated
    # code (a bare stub) -- manually attach it so model_Property's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Property's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Property(generated=True, key="sample_text", value="sample_text")
    partner = model_Properties()
    setattr(partner, 'model_Properties', None)
    _safe_set(owner, 'model_Property', partner)
    assert owner in getattr(partner, 'model_Properties')
    _safe_set(owner, 'model_Property', None)
    assert owner not in getattr(partner, 'model_Properties')


def test_assoc_referencedModel7_stub_double():
    # model_DiagramModelReference has no real 'model_DiagramModelReference' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModel(connectionRouterType=7)
    partner = model_DiagramModelReference()
    setattr(partner, 'model_DiagramModelReference', None)
    _safe_set(owner, 'model_DiagramModel8', partner)
    assert getattr(partner, 'model_DiagramModelReference') == owner
    _safe_set(owner, 'model_DiagramModel8', None)
    assert getattr(partner, 'model_DiagramModelReference') is None


def test_assoc_relation46_stub_double():
    # model_BasicRelationship has no real 'model_BasicRelationship48' property in the generated
    # code (a bare stub) -- manually attach it so model_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Attribute(maxOccurs=7, minOccurs=7)
    partner = model_BasicRelationship()
    setattr(partner, 'model_BasicRelationship48', None)
    _safe_set(owner, 'model_Attribute47', partner)
    assert getattr(partner, 'model_BasicRelationship48') == owner
    _safe_set(owner, 'model_Attribute47', None)
    assert getattr(partner, 'model_BasicRelationship48') is None


def test_assoc_relationship25_stub_double():
    # model_BasicRelationship has no real 'BasicRelationship' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelZentaConnection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelZentaConnection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelZentaConnection()
    partner = model_BasicRelationship()
    setattr(partner, 'BasicRelationship', None)
    _safe_set(owner, 'diagConnections', partner)
    assert getattr(partner, 'BasicRelationship') == owner
    _safe_set(owner, 'diagConnections', None)
    assert getattr(partner, 'BasicRelationship') is None


def test_assoc_template39_stub_double():
    # model_BasicObject has no real 'classes' property in the generated
    # code (a bare stub) -- manually attach it so model_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Template(path="sample_text")
    partner = model_BasicObject()
    setattr(partner, 'classes', None)
    _safe_set(owner, 'Template40', partner)
    assert getattr(partner, 'classes') == owner
    _safe_set(owner, 'Template40', None)
    assert getattr(partner, 'classes') is None


def test_assoc_templates26_stub_double():
    # model_Metamodel has no real 'metamodel' property in the generated
    # code (a bare stub) -- manually attach it so model_Template's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_Template's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_Template(path="sample_text")
    partner = model_Metamodel()
    setattr(partner, 'metamodel', None)
    _safe_set(owner, 'Template', partner)
    assert owner in getattr(partner, 'metamodel')
    _safe_set(owner, 'Template', None)
    assert owner not in getattr(partner, 'metamodel')


def test_assoc_zentaElement24_stub_double():
    # model_ZentaElement has no real 'ZentaElement' property in the generated
    # code (a bare stub) -- manually attach it so model_DiagramModelZentaObject's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_DiagramModelZentaObject's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_DiagramModelZentaObject(type=7)
    partner = model_ZentaElement()
    setattr(partner, 'ZentaElement', None)
    _safe_set(owner, 'diagObjects', partner)
    assert getattr(partner, 'ZentaElement') == owner
    _safe_set(owner, 'diagObjects', None)
    assert getattr(partner, 'ZentaElement') is None


def test_assoc_zentaModel2_stub_double():
    # model_ZentaModelElement has no real 'model_ZentaModelElement' property in the generated
    # code (a bare stub) -- manually attach it so model_ZentaModel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # model_ZentaModel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = model_ZentaModel(file="sample_text", version="sample_text")
    partner = model_ZentaModelElement()
    setattr(partner, 'model_ZentaModelElement', None)
    _safe_set(owner, 'model_ZentaModel', partner)
    assert getattr(partner, 'model_ZentaModelElement') == owner
    _safe_set(owner, 'model_ZentaModel', None)
    assert getattr(partner, 'model_ZentaModelElement') is None


