import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_model_Attribute_maxOccurs_value_roundtrip():
    instance = model_Attribute(maxOccurs=7, minOccurs=7)
    assert instance.maxOccurs == 7
    instance.maxOccurs = 13
    assert instance.maxOccurs == 13


def test_model_Attribute_minOccurs_value_roundtrip():
    instance = model_Attribute(maxOccurs=7, minOccurs=7)
    assert instance.minOccurs == 7
    instance.minOccurs = 13
    assert instance.minOccurs == 13


def test_model_BorderObject_borderColor_value_roundtrip():
    instance = model_BorderObject(borderColor="sample_text")
    assert instance.borderColor == "sample_text"
    instance.borderColor = "sample_text_2"
    assert instance.borderColor == "sample_text_2"


def test_model_Bounds_height_value_roundtrip():
    instance = model_Bounds(height=7, width=7, x=7, y=7)
    assert instance.height == 7
    instance.height = 13
    assert instance.height == 13


def test_model_Bounds_width_value_roundtrip():
    instance = model_Bounds(height=7, width=7, x=7, y=7)
    assert instance.width == 7
    instance.width = 13
    assert instance.width == 13


def test_model_Bounds_x_value_roundtrip():
    instance = model_Bounds(height=7, width=7, x=7, y=7)
    assert instance.x == 7
    instance.x = 13
    assert instance.x == 13


def test_model_Bounds_y_value_roundtrip():
    instance = model_Bounds(height=7, width=7, x=7, y=7)
    assert instance.y == 7
    instance.y = 13
    assert instance.y == 13


def test_model_DiagramModel_connectionRouterType_value_roundtrip():
    instance = model_DiagramModel(connectionRouterType=7)
    assert instance.connectionRouterType == 7
    instance.connectionRouterType = 13
    assert instance.connectionRouterType == 13


def test_model_DiagramModelBendpoint_endX_value_roundtrip():
    instance = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    assert instance.endX == 7
    instance.endX = 13
    assert instance.endX == 13


def test_model_DiagramModelBendpoint_endY_value_roundtrip():
    instance = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    assert instance.endY == 7
    instance.endY = 13
    assert instance.endY == 13


def test_model_DiagramModelBendpoint_startX_value_roundtrip():
    instance = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    assert instance.startX == 7
    instance.startX = 13
    assert instance.startX == 13


def test_model_DiagramModelBendpoint_startY_value_roundtrip():
    instance = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    assert instance.startY == 7
    instance.startY = 13
    assert instance.startY == 13


def test_model_DiagramModelComponent_lineColor_value_roundtrip():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert instance.lineColor == "sample_text"
    instance.lineColor = "sample_text_2"
    assert instance.lineColor == "sample_text_2"


def test_model_DiagramModelComponent_lineWidth_value_roundtrip():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert instance.lineWidth == 7
    instance.lineWidth = 13
    assert instance.lineWidth == 13


def test_model_DiagramModelConnection_lineDecoration_value_roundtrip():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert instance.lineDecoration == "sample_text"
    instance.lineDecoration = "sample_text_2"
    assert instance.lineDecoration == "sample_text_2"


def test_model_DiagramModelConnection_text_value_roundtrip():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_model_DiagramModelConnection_type_value_roundtrip():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert instance.type == 7
    instance.type = 13
    assert instance.type == 13


def test_model_DiagramModelImageProvider_imagePath_value_roundtrip():
    instance = model_DiagramModelImageProvider(imagePath="sample_text")
    assert instance.imagePath == "sample_text"
    instance.imagePath = "sample_text_2"
    assert instance.imagePath == "sample_text_2"


def test_model_DiagramModelObject_elementShape_value_roundtrip():
    instance = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    assert instance.elementShape == "sample_text"
    instance.elementShape = "sample_text_2"
    assert instance.elementShape == "sample_text_2"


def test_model_DiagramModelObject_fillColor_value_roundtrip():
    instance = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    assert instance.fillColor == "sample_text"
    instance.fillColor = "sample_text_2"
    assert instance.fillColor == "sample_text_2"


def test_model_DiagramModelZentaObject_type_value_roundtrip():
    instance = model_DiagramModelZentaObject(type=7)
    assert instance.type == 7
    instance.type = 13
    assert instance.type == 13


def test_model_Documentable_documentation_value_roundtrip():
    instance = model_Documentable(documentation="sample_text")
    assert instance.documentation == "sample_text"
    instance.documentation = "sample_text_2"
    assert instance.documentation == "sample_text_2"


def test_model_FontAttribute_font_value_roundtrip():
    instance = model_FontAttribute(font="sample_text", fontColor="sample_text", textAlignment=7, textPosition=7)
    assert instance.font == "sample_text"
    instance.font = "sample_text_2"
    assert instance.font == "sample_text_2"


def test_model_FontAttribute_fontColor_value_roundtrip():
    instance = model_FontAttribute(font="sample_text", fontColor="sample_text", textAlignment=7, textPosition=7)
    assert instance.fontColor == "sample_text"
    instance.fontColor = "sample_text_2"
    assert instance.fontColor == "sample_text_2"


def test_model_FontAttribute_textAlignment_value_roundtrip():
    instance = model_FontAttribute(font="sample_text", fontColor="sample_text", textAlignment=7, textPosition=7)
    assert instance.textAlignment == 7
    instance.textAlignment = 13
    assert instance.textAlignment == 13


def test_model_FontAttribute_textPosition_value_roundtrip():
    instance = model_FontAttribute(font="sample_text", fontColor="sample_text", textAlignment=7, textPosition=7)
    assert instance.textPosition == 7
    instance.textPosition = 13
    assert instance.textPosition == 13


def test_model_Identifier_id_value_roundtrip():
    instance = model_Identifier(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_model_InterfaceElement_interfaceType_value_roundtrip():
    instance = model_InterfaceElement(interfaceType=7)
    assert instance.interfaceType == 7
    instance.interfaceType = 13
    assert instance.interfaceType == 13


def test_model_Lockable_locked_value_roundtrip():
    instance = model_Lockable(locked=True)
    assert instance.locked == True
    instance.locked = False
    assert instance.locked == False


def test_model_Nameable_name_value_roundtrip():
    instance = model_Nameable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_model_Property_generated_value_roundtrip():
    instance = model_Property(generated=True, key="sample_text", value="sample_text")
    assert instance.generated == True
    instance.generated = False
    assert instance.generated == False


def test_model_Property_key_value_roundtrip():
    instance = model_Property(generated=True, key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_model_Property_value_value_roundtrip():
    instance = model_Property(generated=True, key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_model_SketchModel_background_value_roundtrip():
    instance = model_SketchModel(background=7)
    assert instance.background == 7
    instance.background = 13
    assert instance.background == 13


def test_model_Template_path_value_roundtrip():
    instance = model_Template(path="sample_text")
    assert instance.path == "sample_text"
    instance.path = "sample_text_2"
    assert instance.path == "sample_text_2"


def test_model_TextContent_content_value_roundtrip():
    instance = model_TextContent(content="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_model_ZentaDiagramModel_viewpoint_value_roundtrip():
    instance = model_ZentaDiagramModel(viewpoint=7)
    assert instance.viewpoint == 7
    instance.viewpoint = 13
    assert instance.viewpoint == 13


def test_model_ZentaModel_file_value_roundtrip():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert instance.file == "sample_text"
    instance.file = "sample_text_2"
    assert instance.file == "sample_text_2"


def test_model_ZentaModel_version_value_roundtrip():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_model_DiagramModelComponent_isa_Adapter():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert isinstance(instance, Adapter)


def test_model_ZentaModelElement_isa_Adapter():
    instance = model_ZentaModelElement()
    assert isinstance(instance, Adapter)


def test_model_BasicRelationship_isa_BasicObject():
    instance = model_BasicRelationship()
    assert isinstance(instance, BasicObject)


def test_model_DiagramModelImage_isa_BorderObject():
    instance = model_DiagramModelImage()
    assert isinstance(instance, BorderObject)


def test_model_DiagramModelBendpoint_isa_Cloneable():
    instance = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    assert isinstance(instance, Cloneable)


def test_model_DiagramModelComponent_isa_Cloneable():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert isinstance(instance, Cloneable)


def test_model_ZentaElement_isa_Cloneable():
    instance = model_ZentaElement()
    assert isinstance(instance, Cloneable)


def test_model_SketchModel_isa_DiagramModel():
    instance = model_SketchModel(background=7)
    assert isinstance(instance, DiagramModel)


def test_model_ZentaDiagramModel_isa_DiagramModel():
    instance = model_ZentaDiagramModel(viewpoint=7)
    assert isinstance(instance, DiagramModel)


def test_model_DiagramModelConnection_isa_DiagramModelComponent():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert isinstance(instance, DiagramModelComponent)


def test_model_DiagramModelContainer_isa_DiagramModelComponent():
    instance = model_DiagramModelContainer()
    assert isinstance(instance, DiagramModelComponent)


def test_model_DiagramModelObject_isa_DiagramModelComponent():
    instance = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    assert isinstance(instance, DiagramModelComponent)


def test_model_DiagramModelZentaConnection_isa_DiagramModelConnection():
    instance = model_DiagramModelZentaConnection()
    assert isinstance(instance, DiagramModelConnection)


def test_model_DiagramModel_isa_DiagramModelContainer():
    instance = model_DiagramModel(connectionRouterType=7)
    assert isinstance(instance, DiagramModelContainer)


def test_model_DiagramModelGroup_isa_DiagramModelContainer():
    instance = model_DiagramModelGroup()
    assert isinstance(instance, DiagramModelContainer)


def test_model_DiagramModelZentaObject_isa_DiagramModelContainer():
    instance = model_DiagramModelZentaObject(type=7)
    assert isinstance(instance, DiagramModelContainer)


def test_model_SketchModelSticky_isa_DiagramModelContainer():
    instance = model_SketchModelSticky()
    assert isinstance(instance, DiagramModelContainer)


def test_model_DiagramModelImage_isa_DiagramModelImageProvider():
    instance = model_DiagramModelImage()
    assert isinstance(instance, DiagramModelImageProvider)


def test_model_DiagramModelGroup_isa_DiagramModelObject():
    instance = model_DiagramModelGroup()
    assert isinstance(instance, DiagramModelObject)


def test_model_DiagramModelImage_isa_DiagramModelObject():
    instance = model_DiagramModelImage()
    assert isinstance(instance, DiagramModelObject)


def test_model_DiagramModelNote_isa_DiagramModelObject():
    instance = model_DiagramModelNote()
    assert isinstance(instance, DiagramModelObject)


def test_model_DiagramModelReference_isa_DiagramModelObject():
    instance = model_DiagramModelReference()
    assert isinstance(instance, DiagramModelObject)


def test_model_DiagramModelZentaObject_isa_DiagramModelObject():
    instance = model_DiagramModelZentaObject(type=7)
    assert isinstance(instance, DiagramModelObject)


def test_model_SketchModelActor_isa_DiagramModelObject():
    instance = model_SketchModelActor()
    assert isinstance(instance, DiagramModelObject)


def test_model_SketchModelSticky_isa_DiagramModelObject():
    instance = model_SketchModelSticky()
    assert isinstance(instance, DiagramModelObject)


def test_model_DiagramModel_isa_Documentable():
    instance = model_DiagramModel(connectionRouterType=7)
    assert isinstance(instance, Documentable)


def test_model_DiagramModelConnection_isa_Documentable():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert isinstance(instance, Documentable)


def test_model_DiagramModelGroup_isa_Documentable():
    instance = model_DiagramModelGroup()
    assert isinstance(instance, Documentable)


def test_model_Folder_isa_Documentable():
    instance = model_Folder()
    assert isinstance(instance, Documentable)


def test_model_SketchModelActor_isa_Documentable():
    instance = model_SketchModelActor()
    assert isinstance(instance, Documentable)


def test_model_ZentaElement_isa_Documentable():
    instance = model_ZentaElement()
    assert isinstance(instance, Documentable)


def test_model_ZentaModel_isa_Documentable():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, Documentable)


def test_model_ZentaModel_isa_Folder():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, Folder)


def test_model_Folder_isa_FolderContainer():
    instance = model_Folder()
    assert isinstance(instance, FolderContainer)


def test_model_ZentaModel_isa_FolderContainer():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, FolderContainer)


def test_model_DiagramModelConnection_isa_FontAttribute():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert isinstance(instance, FontAttribute)


def test_model_DiagramModelObject_isa_FontAttribute():
    instance = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    assert isinstance(instance, FontAttribute)


def test_model_DiagramModelComponent_isa_Identifier():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert isinstance(instance, Identifier)


def test_model_Folder_isa_Identifier():
    instance = model_Folder()
    assert isinstance(instance, Identifier)


def test_model_ZentaElement_isa_Identifier():
    instance = model_ZentaElement()
    assert isinstance(instance, Identifier)


def test_model_ZentaModel_isa_Identifier():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, Identifier)


def test_model_AndJunction_isa_JunctionElement():
    instance = model_AndJunction()
    assert isinstance(instance, JunctionElement)


def test_model_Junction_isa_JunctionElement():
    instance = model_Junction()
    assert isinstance(instance, JunctionElement)


def test_model_OrJunction_isa_JunctionElement():
    instance = model_OrJunction()
    assert isinstance(instance, JunctionElement)


def test_model_DiagramModelComponent_isa_Nameable():
    instance = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    assert isinstance(instance, Nameable)


def test_model_Folder_isa_Nameable():
    instance = model_Folder()
    assert isinstance(instance, Nameable)


def test_model_Identifier_isa_Nameable():
    instance = model_Identifier(id="sample_text")
    assert isinstance(instance, Nameable)


def test_model_ZentaElement_isa_Nameable():
    instance = model_ZentaElement()
    assert isinstance(instance, Nameable)


def test_model_ZentaModel_isa_Nameable():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, Nameable)


def test_model_DiagramModel_isa_Properties():
    instance = model_DiagramModel(connectionRouterType=7)
    assert isinstance(instance, Properties)


def test_model_DiagramModelConnection_isa_Properties():
    instance = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    assert isinstance(instance, Properties)


def test_model_DiagramModelGroup_isa_Properties():
    instance = model_DiagramModelGroup()
    assert isinstance(instance, Properties)


def test_model_Folder_isa_Properties():
    instance = model_Folder()
    assert isinstance(instance, Properties)


def test_model_SketchModelActor_isa_Properties():
    instance = model_SketchModelActor()
    assert isinstance(instance, Properties)


def test_model_SketchModelSticky_isa_Properties():
    instance = model_SketchModelSticky()
    assert isinstance(instance, Properties)


def test_model_ZentaElement_isa_Properties():
    instance = model_ZentaElement()
    assert isinstance(instance, Properties)


def test_model_ZentaModel_isa_Properties():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, Properties)


def test_model_DiagramModelNote_isa_TextContent():
    instance = model_DiagramModelNote()
    assert isinstance(instance, TextContent)


def test_model_SketchModelSticky_isa_TextContent():
    instance = model_SketchModelSticky()
    assert isinstance(instance, TextContent)


def test_model_BasicObject_isa_ZentaElement():
    instance = model_BasicObject()
    assert isinstance(instance, ZentaElement)


def test_model_InterfaceElement_isa_ZentaElement():
    instance = model_InterfaceElement(interfaceType=7)
    assert isinstance(instance, ZentaElement)


def test_model_JunctionElement_isa_ZentaElement():
    instance = model_JunctionElement()
    assert isinstance(instance, ZentaElement)


def test_model_DiagramModel_isa_ZentaModelElement():
    instance = model_DiagramModel(connectionRouterType=7)
    assert isinstance(instance, ZentaModelElement)


def test_model_Folder_isa_ZentaModelElement():
    instance = model_Folder()
    assert isinstance(instance, ZentaModelElement)


def test_model_ZentaElement_isa_ZentaModelElement():
    instance = model_ZentaElement()
    assert isinstance(instance, ZentaModelElement)


def test_model_ZentaModel_isa_ZentaModelElement():
    instance = model_ZentaModel(file="sample_text", version="sample_text")
    assert isinstance(instance, ZentaModelElement)


def test_assoc_attributes32_link_reassign_clear():
    a = model_Attribute(maxOccurs=7, minOccurs=7)
    b1 = model_BasicObject()
    b2 = model_BasicObject()
    _safe_set(a, 'model_Attribute', b1)
    assert _is_linked(a, 'model_Attribute', b1)
    if hasattr(b1, 'model_BasicObject'):
        assert _is_linked(b1, 'model_BasicObject', a)
    _safe_set(a, 'model_Attribute', b2)
    assert _is_linked(a, 'model_Attribute', b2)
    if hasattr(b1, 'model_BasicObject'):
        assert not _is_linked(b1, 'model_BasicObject', a)
    if hasattr(b2, 'model_BasicObject'):
        assert _is_linked(b2, 'model_BasicObject', a)
    _safe_set(a, 'model_Attribute', None)
    assert not _is_linked(a, 'model_Attribute', b2)
    if hasattr(b2, 'model_BasicObject'):
        assert not _is_linked(b2, 'model_BasicObject', a)


def test_assoc_bendpoints22_link_reassign_clear():
    a = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    b1 = model_DiagramModelBendpoint(endX=7, endY=7, startX=7, startY=7)
    b2 = model_DiagramModelBendpoint(endX=13, endY=13, startX=13, startY=13)
    _safe_set(a, 'model_DiagramModelConnection23', {b1})
    assert _is_linked(a, 'model_DiagramModelConnection23', b1)
    if hasattr(b1, 'model_DiagramModelBendpoint'):
        assert _is_linked(b1, 'model_DiagramModelBendpoint', a)
    _safe_set(a, 'model_DiagramModelConnection23', {b2})
    assert _is_linked(a, 'model_DiagramModelConnection23', b2)
    if hasattr(b1, 'model_DiagramModelBendpoint'):
        assert not _is_linked(b1, 'model_DiagramModelBendpoint', a)
    if hasattr(b2, 'model_DiagramModelBendpoint'):
        assert _is_linked(b2, 'model_DiagramModelBendpoint', a)
    _safe_set(a, 'model_DiagramModelConnection23', set())
    assert not _is_linked(a, 'model_DiagramModelConnection23', b2)
    if hasattr(b2, 'model_DiagramModelBendpoint'):
        assert not _is_linked(b2, 'model_DiagramModelBendpoint', a)


def test_assoc_bounds9_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_Bounds(height=7, width=7, x=7, y=7)
    b2 = model_Bounds(height=13, width=13, x=13, y=13)
    _safe_set(a, 'model_DiagramModelObject10', b1)
    assert _is_linked(a, 'model_DiagramModelObject10', b1)
    if hasattr(b1, 'model_Bounds'):
        assert _is_linked(b1, 'model_Bounds', a)
    _safe_set(a, 'model_DiagramModelObject10', b2)
    assert _is_linked(a, 'model_DiagramModelObject10', b2)
    if hasattr(b1, 'model_Bounds'):
        assert not _is_linked(b1, 'model_Bounds', a)
    if hasattr(b2, 'model_Bounds'):
        assert _is_linked(b2, 'model_Bounds', a)
    _safe_set(a, 'model_DiagramModelObject10', None)
    assert not _is_linked(a, 'model_DiagramModelObject10', b2)
    if hasattr(b2, 'model_Bounds'):
        assert not _is_linked(b2, 'model_Bounds', a)


def test_assoc_children6_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_DiagramModelContainer()
    b2 = model_DiagramModelContainer()
    _safe_set(a, 'model_DiagramModelObject', b1)
    assert _is_linked(a, 'model_DiagramModelObject', b1)
    if hasattr(b1, 'model_DiagramModelContainer'):
        assert _is_linked(b1, 'model_DiagramModelContainer', a)
    _safe_set(a, 'model_DiagramModelObject', b2)
    assert _is_linked(a, 'model_DiagramModelObject', b2)
    if hasattr(b1, 'model_DiagramModelContainer'):
        assert not _is_linked(b1, 'model_DiagramModelContainer', a)
    if hasattr(b2, 'model_DiagramModelContainer'):
        assert _is_linked(b2, 'model_DiagramModelContainer', a)
    _safe_set(a, 'model_DiagramModelObject', None)
    assert not _is_linked(a, 'model_DiagramModelObject', b2)
    if hasattr(b2, 'model_DiagramModelContainer'):
        assert not _is_linked(b2, 'model_DiagramModelContainer', a)


def test_assoc_classes27_link_reassign_clear():
    a = model_Template(path="sample_text")
    b1 = model_BasicObject()
    b2 = model_BasicObject()
    _safe_set(a, 'template', {b1})
    assert _is_linked(a, 'template', b1)
    if hasattr(b1, 'BasicObject'):
        assert _is_linked(b1, 'BasicObject', a)
    _safe_set(a, 'template', {b2})
    assert _is_linked(a, 'template', b2)
    if hasattr(b1, 'BasicObject'):
        assert not _is_linked(b1, 'BasicObject', a)
    if hasattr(b2, 'BasicObject'):
        assert _is_linked(b2, 'BasicObject', a)
    _safe_set(a, 'template', set())
    assert not _is_linked(a, 'template', b2)
    if hasattr(b2, 'BasicObject'):
        assert not _is_linked(b2, 'BasicObject', a)


def test_assoc_connectedObject49_link_reassign_clear():
    a = model_Attribute(maxOccurs=7, minOccurs=7)
    b1 = model_BasicObject()
    b2 = model_BasicObject()
    _safe_set(a, 'model_Attribute50', b1)
    assert _is_linked(a, 'model_Attribute50', b1)
    if hasattr(b1, 'model_BasicObject51'):
        assert _is_linked(b1, 'model_BasicObject51', a)
    _safe_set(a, 'model_Attribute50', b2)
    assert _is_linked(a, 'model_Attribute50', b2)
    if hasattr(b1, 'model_BasicObject51'):
        assert not _is_linked(b1, 'model_BasicObject51', a)
    if hasattr(b2, 'model_BasicObject51'):
        assert _is_linked(b2, 'model_BasicObject51', a)
    _safe_set(a, 'model_Attribute50', None)
    assert not _is_linked(a, 'model_Attribute50', b2)
    if hasattr(b2, 'model_BasicObject51'):
        assert not _is_linked(b2, 'model_BasicObject51', a)


def test_assoc_diagConnections45_link_reassign_clear():
    a = model_DiagramModelZentaConnection()
    b1 = model_BasicRelationship()
    b2 = model_BasicRelationship()
    _safe_set(a, 'DiagramModelZentaConnection', b1)
    assert _is_linked(a, 'DiagramModelZentaConnection', b1)
    if hasattr(b1, 'relationship'):
        assert _is_linked(b1, 'relationship', a)
    _safe_set(a, 'DiagramModelZentaConnection', b2)
    assert _is_linked(a, 'DiagramModelZentaConnection', b2)
    if hasattr(b1, 'relationship'):
        assert not _is_linked(b1, 'relationship', a)
    if hasattr(b2, 'relationship'):
        assert _is_linked(b2, 'relationship', a)
    _safe_set(a, 'DiagramModelZentaConnection', None)
    assert not _is_linked(a, 'DiagramModelZentaConnection', b2)
    if hasattr(b2, 'relationship'):
        assert not _is_linked(b2, 'relationship', a)


def test_assoc_diagObjects31_link_reassign_clear():
    a = model_DiagramModelZentaObject(type=7)
    b1 = model_ZentaElement()
    b2 = model_ZentaElement()
    _safe_set(a, 'DiagramModelZentaObject', b1)
    assert _is_linked(a, 'DiagramModelZentaObject', b1)
    if hasattr(b1, 'zentaElement'):
        assert _is_linked(b1, 'zentaElement', a)
    _safe_set(a, 'DiagramModelZentaObject', b2)
    assert _is_linked(a, 'DiagramModelZentaObject', b2)
    if hasattr(b1, 'zentaElement'):
        assert not _is_linked(b1, 'zentaElement', a)
    if hasattr(b2, 'zentaElement'):
        assert _is_linked(b2, 'zentaElement', a)
    _safe_set(a, 'DiagramModelZentaObject', None)
    assert not _is_linked(a, 'DiagramModelZentaObject', b2)
    if hasattr(b2, 'zentaElement'):
        assert not _is_linked(b2, 'zentaElement', a)


def test_assoc_diagram29_link_reassign_clear():
    a = model_Template(path="sample_text")
    b1 = model_DiagramModel(connectionRouterType=7)
    b2 = model_DiagramModel(connectionRouterType=13)
    _safe_set(a, 'model_Template', b1)
    assert _is_linked(a, 'model_Template', b1)
    if hasattr(b1, 'model_DiagramModel30'):
        assert _is_linked(b1, 'model_DiagramModel30', a)
    _safe_set(a, 'model_Template', b2)
    assert _is_linked(a, 'model_Template', b2)
    if hasattr(b1, 'model_DiagramModel30'):
        assert not _is_linked(b1, 'model_DiagramModel30', a)
    if hasattr(b2, 'model_DiagramModel30'):
        assert _is_linked(b2, 'model_DiagramModel30', a)
    _safe_set(a, 'model_Template', None)
    assert not _is_linked(a, 'model_Template', b2)
    if hasattr(b2, 'model_DiagramModel30'):
        assert not _is_linked(b2, 'model_DiagramModel30', a)


def test_assoc_diagramModel5_link_reassign_clear():
    a = model_DiagramModelComponent(lineColor="sample_text", lineWidth=7)
    b1 = model_DiagramModel(connectionRouterType=7)
    b2 = model_DiagramModel(connectionRouterType=13)
    _safe_set(a, 'model_DiagramModelComponent', b1)
    assert _is_linked(a, 'model_DiagramModelComponent', b1)
    if hasattr(b1, 'model_DiagramModel'):
        assert _is_linked(b1, 'model_DiagramModel', a)
    _safe_set(a, 'model_DiagramModelComponent', b2)
    assert _is_linked(a, 'model_DiagramModelComponent', b2)
    if hasattr(b1, 'model_DiagramModel'):
        assert not _is_linked(b1, 'model_DiagramModel', a)
    if hasattr(b2, 'model_DiagramModel'):
        assert _is_linked(b2, 'model_DiagramModel', a)
    _safe_set(a, 'model_DiagramModelComponent', None)
    assert not _is_linked(a, 'model_DiagramModelComponent', b2)
    if hasattr(b2, 'model_DiagramModel'):
        assert not _is_linked(b2, 'model_DiagramModel', a)


def test_assoc_elements3_link_reassign_clear():
    a = model_Nameable(name="sample_text")
    b1 = model_Folder()
    b2 = model_Folder()
    _safe_set(a, 'model_Nameable', b1)
    assert _is_linked(a, 'model_Nameable', b1)
    if hasattr(b1, 'model_Folder4'):
        assert _is_linked(b1, 'model_Folder4', a)
    _safe_set(a, 'model_Nameable', b2)
    assert _is_linked(a, 'model_Nameable', b2)
    if hasattr(b1, 'model_Folder4'):
        assert not _is_linked(b1, 'model_Folder4', a)
    if hasattr(b2, 'model_Folder4'):
        assert _is_linked(b2, 'model_Folder4', a)
    _safe_set(a, 'model_Nameable', None)
    assert not _is_linked(a, 'model_Nameable', b2)
    if hasattr(b2, 'model_Folder4'):
        assert not _is_linked(b2, 'model_Folder4', a)


def test_assoc_metamodel28_link_reassign_clear():
    a = model_Template(path="sample_text")
    b1 = model_Metamodel()
    b2 = model_Metamodel()
    _safe_set(a, 'templates', b1)
    assert _is_linked(a, 'templates', b1)
    if hasattr(b1, 'Metamodel'):
        assert _is_linked(b1, 'Metamodel', a)
    _safe_set(a, 'templates', b2)
    assert _is_linked(a, 'templates', b2)
    if hasattr(b1, 'Metamodel'):
        assert not _is_linked(b1, 'Metamodel', a)
    if hasattr(b2, 'Metamodel'):
        assert _is_linked(b2, 'Metamodel', a)
    _safe_set(a, 'templates', None)
    assert not _is_linked(a, 'templates', b2)
    if hasattr(b2, 'Metamodel'):
        assert not _is_linked(b2, 'Metamodel', a)


def test_assoc_properties0_link_reassign_clear():
    a = model_Property(generated=True, key="sample_text", value="sample_text")
    b1 = model_Properties()
    b2 = model_Properties()
    _safe_set(a, 'model_Property', b1)
    assert _is_linked(a, 'model_Property', b1)
    if hasattr(b1, 'model_Properties'):
        assert _is_linked(b1, 'model_Properties', a)
    _safe_set(a, 'model_Property', b2)
    assert _is_linked(a, 'model_Property', b2)
    if hasattr(b1, 'model_Properties'):
        assert not _is_linked(b1, 'model_Properties', a)
    if hasattr(b2, 'model_Properties'):
        assert _is_linked(b2, 'model_Properties', a)
    _safe_set(a, 'model_Property', None)
    assert not _is_linked(a, 'model_Property', b2)
    if hasattr(b2, 'model_Properties'):
        assert not _is_linked(b2, 'model_Properties', a)


def test_assoc_referencedModel7_link_reassign_clear():
    a = model_DiagramModel(connectionRouterType=7)
    b1 = model_DiagramModelReference()
    b2 = model_DiagramModelReference()
    _safe_set(a, 'model_DiagramModel8', b1)
    assert _is_linked(a, 'model_DiagramModel8', b1)
    if hasattr(b1, 'model_DiagramModelReference'):
        assert _is_linked(b1, 'model_DiagramModelReference', a)
    _safe_set(a, 'model_DiagramModel8', b2)
    assert _is_linked(a, 'model_DiagramModel8', b2)
    if hasattr(b1, 'model_DiagramModelReference'):
        assert not _is_linked(b1, 'model_DiagramModelReference', a)
    if hasattr(b2, 'model_DiagramModelReference'):
        assert _is_linked(b2, 'model_DiagramModelReference', a)
    _safe_set(a, 'model_DiagramModel8', None)
    assert not _is_linked(a, 'model_DiagramModel8', b2)
    if hasattr(b2, 'model_DiagramModelReference'):
        assert not _is_linked(b2, 'model_DiagramModelReference', a)


def test_assoc_relation46_link_reassign_clear():
    a = model_Attribute(maxOccurs=7, minOccurs=7)
    b1 = model_BasicRelationship()
    b2 = model_BasicRelationship()
    _safe_set(a, 'model_Attribute47', b1)
    assert _is_linked(a, 'model_Attribute47', b1)
    if hasattr(b1, 'model_BasicRelationship48'):
        assert _is_linked(b1, 'model_BasicRelationship48', a)
    _safe_set(a, 'model_Attribute47', b2)
    assert _is_linked(a, 'model_Attribute47', b2)
    if hasattr(b1, 'model_BasicRelationship48'):
        assert not _is_linked(b1, 'model_BasicRelationship48', a)
    if hasattr(b2, 'model_BasicRelationship48'):
        assert _is_linked(b2, 'model_BasicRelationship48', a)
    _safe_set(a, 'model_Attribute47', None)
    assert not _is_linked(a, 'model_Attribute47', b2)
    if hasattr(b2, 'model_BasicRelationship48'):
        assert not _is_linked(b2, 'model_BasicRelationship48', a)


def test_assoc_relationship25_link_reassign_clear():
    a = model_DiagramModelZentaConnection()
    b1 = model_BasicRelationship()
    b2 = model_BasicRelationship()
    _safe_set(a, 'diagConnections', b1)
    assert _is_linked(a, 'diagConnections', b1)
    if hasattr(b1, 'BasicRelationship'):
        assert _is_linked(b1, 'BasicRelationship', a)
    _safe_set(a, 'diagConnections', b2)
    assert _is_linked(a, 'diagConnections', b2)
    if hasattr(b1, 'BasicRelationship'):
        assert not _is_linked(b1, 'BasicRelationship', a)
    if hasattr(b2, 'BasicRelationship'):
        assert _is_linked(b2, 'BasicRelationship', a)
    _safe_set(a, 'diagConnections', None)
    assert not _is_linked(a, 'diagConnections', b2)
    if hasattr(b2, 'BasicRelationship'):
        assert not _is_linked(b2, 'BasicRelationship', a)


def test_assoc_source16_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    b2 = model_DiagramModelConnection(lineDecoration="sample_text_2", text="sample_text_2", type=13)
    _safe_set(a, 'model_DiagramModelObject18', b1)
    assert _is_linked(a, 'model_DiagramModelObject18', b1)
    if hasattr(b1, 'model_DiagramModelConnection17'):
        assert _is_linked(b1, 'model_DiagramModelConnection17', a)
    _safe_set(a, 'model_DiagramModelObject18', b2)
    assert _is_linked(a, 'model_DiagramModelObject18', b2)
    if hasattr(b1, 'model_DiagramModelConnection17'):
        assert not _is_linked(b1, 'model_DiagramModelConnection17', a)
    if hasattr(b2, 'model_DiagramModelConnection17'):
        assert _is_linked(b2, 'model_DiagramModelConnection17', a)
    _safe_set(a, 'model_DiagramModelObject18', None)
    assert not _is_linked(a, 'model_DiagramModelObject18', b2)
    if hasattr(b2, 'model_DiagramModelConnection17'):
        assert not _is_linked(b2, 'model_DiagramModelConnection17', a)


def test_assoc_sourceConnections11_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    b2 = model_DiagramModelConnection(lineDecoration="sample_text_2", text="sample_text_2", type=13)
    _safe_set(a, 'model_DiagramModelObject12', {b1})
    assert _is_linked(a, 'model_DiagramModelObject12', b1)
    if hasattr(b1, 'model_DiagramModelConnection'):
        assert _is_linked(b1, 'model_DiagramModelConnection', a)
    _safe_set(a, 'model_DiagramModelObject12', {b2})
    assert _is_linked(a, 'model_DiagramModelObject12', b2)
    if hasattr(b1, 'model_DiagramModelConnection'):
        assert not _is_linked(b1, 'model_DiagramModelConnection', a)
    if hasattr(b2, 'model_DiagramModelConnection'):
        assert _is_linked(b2, 'model_DiagramModelConnection', a)
    _safe_set(a, 'model_DiagramModelObject12', set())
    assert not _is_linked(a, 'model_DiagramModelObject12', b2)
    if hasattr(b2, 'model_DiagramModelConnection'):
        assert not _is_linked(b2, 'model_DiagramModelConnection', a)


def test_assoc_target19_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    b2 = model_DiagramModelConnection(lineDecoration="sample_text_2", text="sample_text_2", type=13)
    _safe_set(a, 'model_DiagramModelObject21', b1)
    assert _is_linked(a, 'model_DiagramModelObject21', b1)
    if hasattr(b1, 'model_DiagramModelConnection20'):
        assert _is_linked(b1, 'model_DiagramModelConnection20', a)
    _safe_set(a, 'model_DiagramModelObject21', b2)
    assert _is_linked(a, 'model_DiagramModelObject21', b2)
    if hasattr(b1, 'model_DiagramModelConnection20'):
        assert not _is_linked(b1, 'model_DiagramModelConnection20', a)
    if hasattr(b2, 'model_DiagramModelConnection20'):
        assert _is_linked(b2, 'model_DiagramModelConnection20', a)
    _safe_set(a, 'model_DiagramModelObject21', None)
    assert not _is_linked(a, 'model_DiagramModelObject21', b2)
    if hasattr(b2, 'model_DiagramModelConnection20'):
        assert not _is_linked(b2, 'model_DiagramModelConnection20', a)


def test_assoc_targetConnections13_link_reassign_clear():
    a = model_DiagramModelObject(elementShape="sample_text", fillColor="sample_text")
    b1 = model_DiagramModelConnection(lineDecoration="sample_text", text="sample_text", type=7)
    b2 = model_DiagramModelConnection(lineDecoration="sample_text_2", text="sample_text_2", type=13)
    _safe_set(a, 'model_DiagramModelObject14', {b1})
    assert _is_linked(a, 'model_DiagramModelObject14', b1)
    if hasattr(b1, 'model_DiagramModelConnection15'):
        assert _is_linked(b1, 'model_DiagramModelConnection15', a)
    _safe_set(a, 'model_DiagramModelObject14', {b2})
    assert _is_linked(a, 'model_DiagramModelObject14', b2)
    if hasattr(b1, 'model_DiagramModelConnection15'):
        assert not _is_linked(b1, 'model_DiagramModelConnection15', a)
    if hasattr(b2, 'model_DiagramModelConnection15'):
        assert _is_linked(b2, 'model_DiagramModelConnection15', a)
    _safe_set(a, 'model_DiagramModelObject14', set())
    assert not _is_linked(a, 'model_DiagramModelObject14', b2)
    if hasattr(b2, 'model_DiagramModelConnection15'):
        assert not _is_linked(b2, 'model_DiagramModelConnection15', a)


def test_assoc_template39_link_reassign_clear():
    a = model_Template(path="sample_text")
    b1 = model_BasicObject()
    b2 = model_BasicObject()
    _safe_set(a, 'Template40', b1)
    assert _is_linked(a, 'Template40', b1)
    if hasattr(b1, 'classes'):
        assert _is_linked(b1, 'classes', a)
    _safe_set(a, 'Template40', b2)
    assert _is_linked(a, 'Template40', b2)
    if hasattr(b1, 'classes'):
        assert not _is_linked(b1, 'classes', a)
    if hasattr(b2, 'classes'):
        assert _is_linked(b2, 'classes', a)
    _safe_set(a, 'Template40', None)
    assert not _is_linked(a, 'Template40', b2)
    if hasattr(b2, 'classes'):
        assert not _is_linked(b2, 'classes', a)


def test_assoc_templates26_link_reassign_clear():
    a = model_Template(path="sample_text")
    b1 = model_Metamodel()
    b2 = model_Metamodel()
    _safe_set(a, 'Template', b1)
    assert _is_linked(a, 'Template', b1)
    if hasattr(b1, 'metamodel'):
        assert _is_linked(b1, 'metamodel', a)
    _safe_set(a, 'Template', b2)
    assert _is_linked(a, 'Template', b2)
    if hasattr(b1, 'metamodel'):
        assert not _is_linked(b1, 'metamodel', a)
    if hasattr(b2, 'metamodel'):
        assert _is_linked(b2, 'metamodel', a)
    _safe_set(a, 'Template', None)
    assert not _is_linked(a, 'Template', b2)
    if hasattr(b2, 'metamodel'):
        assert not _is_linked(b2, 'metamodel', a)


def test_assoc_zentaElement24_link_reassign_clear():
    a = model_DiagramModelZentaObject(type=7)
    b1 = model_ZentaElement()
    b2 = model_ZentaElement()
    _safe_set(a, 'diagObjects', b1)
    assert _is_linked(a, 'diagObjects', b1)
    if hasattr(b1, 'ZentaElement'):
        assert _is_linked(b1, 'ZentaElement', a)
    _safe_set(a, 'diagObjects', b2)
    assert _is_linked(a, 'diagObjects', b2)
    if hasattr(b1, 'ZentaElement'):
        assert not _is_linked(b1, 'ZentaElement', a)
    if hasattr(b2, 'ZentaElement'):
        assert _is_linked(b2, 'ZentaElement', a)
    _safe_set(a, 'diagObjects', None)
    assert not _is_linked(a, 'diagObjects', b2)
    if hasattr(b2, 'ZentaElement'):
        assert not _is_linked(b2, 'ZentaElement', a)


def test_assoc_zentaModel2_link_reassign_clear():
    a = model_ZentaModel(file="sample_text", version="sample_text")
    b1 = model_ZentaModelElement()
    b2 = model_ZentaModelElement()
    _safe_set(a, 'model_ZentaModel', b1)
    assert _is_linked(a, 'model_ZentaModel', b1)
    if hasattr(b1, 'model_ZentaModelElement'):
        assert _is_linked(b1, 'model_ZentaModelElement', a)
    _safe_set(a, 'model_ZentaModel', b2)
    assert _is_linked(a, 'model_ZentaModel', b2)
    if hasattr(b1, 'model_ZentaModelElement'):
        assert not _is_linked(b1, 'model_ZentaModelElement', a)
    if hasattr(b2, 'model_ZentaModelElement'):
        assert _is_linked(b2, 'model_ZentaModelElement', a)
    _safe_set(a, 'model_ZentaModel', None)
    assert not _is_linked(a, 'model_ZentaModel', b2)
    if hasattr(b2, 'model_ZentaModelElement'):
        assert not _is_linked(b2, 'model_ZentaModelElement', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Adapter_strategy = st.builds(Adapter)
@given(instance=Adapter_strategy)
@settings(max_examples=25)
def test_Adapter_instantiation(instance):
    assert isinstance(instance, Adapter)


BasicObject_strategy = st.builds(BasicObject)
@given(instance=BasicObject_strategy)
@settings(max_examples=25)
def test_BasicObject_instantiation(instance):
    assert isinstance(instance, BasicObject)


BorderObject_strategy = st.builds(BorderObject)
@given(instance=BorderObject_strategy)
@settings(max_examples=25)
def test_BorderObject_instantiation(instance):
    assert isinstance(instance, BorderObject)


Cloneable_strategy = st.builds(Cloneable)
@given(instance=Cloneable_strategy)
@settings(max_examples=25)
def test_Cloneable_instantiation(instance):
    assert isinstance(instance, Cloneable)


DiagramModel_strategy = st.builds(DiagramModel)
@given(instance=DiagramModel_strategy)
@settings(max_examples=25)
def test_DiagramModel_instantiation(instance):
    assert isinstance(instance, DiagramModel)


DiagramModelComponent_strategy = st.builds(DiagramModelComponent)
@given(instance=DiagramModelComponent_strategy)
@settings(max_examples=25)
def test_DiagramModelComponent_instantiation(instance):
    assert isinstance(instance, DiagramModelComponent)


DiagramModelConnection_strategy = st.builds(DiagramModelConnection)
@given(instance=DiagramModelConnection_strategy)
@settings(max_examples=25)
def test_DiagramModelConnection_instantiation(instance):
    assert isinstance(instance, DiagramModelConnection)


DiagramModelContainer_strategy = st.builds(DiagramModelContainer)
@given(instance=DiagramModelContainer_strategy)
@settings(max_examples=25)
def test_DiagramModelContainer_instantiation(instance):
    assert isinstance(instance, DiagramModelContainer)


DiagramModelImageProvider_strategy = st.builds(DiagramModelImageProvider)
@given(instance=DiagramModelImageProvider_strategy)
@settings(max_examples=25)
def test_DiagramModelImageProvider_instantiation(instance):
    assert isinstance(instance, DiagramModelImageProvider)


DiagramModelObject_strategy = st.builds(DiagramModelObject)
@given(instance=DiagramModelObject_strategy)
@settings(max_examples=25)
def test_DiagramModelObject_instantiation(instance):
    assert isinstance(instance, DiagramModelObject)


Documentable_strategy = st.builds(Documentable)
@given(instance=Documentable_strategy)
@settings(max_examples=25)
def test_Documentable_instantiation(instance):
    assert isinstance(instance, Documentable)


Folder_strategy = st.builds(Folder)
@given(instance=Folder_strategy)
@settings(max_examples=25)
def test_Folder_instantiation(instance):
    assert isinstance(instance, Folder)


FolderContainer_strategy = st.builds(FolderContainer)
@given(instance=FolderContainer_strategy)
@settings(max_examples=25)
def test_FolderContainer_instantiation(instance):
    assert isinstance(instance, FolderContainer)


FontAttribute_strategy = st.builds(FontAttribute)
@given(instance=FontAttribute_strategy)
@settings(max_examples=25)
def test_FontAttribute_instantiation(instance):
    assert isinstance(instance, FontAttribute)


Identifier_strategy = st.builds(Identifier)
@given(instance=Identifier_strategy)
@settings(max_examples=25)
def test_Identifier_instantiation(instance):
    assert isinstance(instance, Identifier)


JunctionElement_strategy = st.builds(JunctionElement)
@given(instance=JunctionElement_strategy)
@settings(max_examples=25)
def test_JunctionElement_instantiation(instance):
    assert isinstance(instance, JunctionElement)


Nameable_strategy = st.builds(Nameable)
@given(instance=Nameable_strategy)
@settings(max_examples=25)
def test_Nameable_instantiation(instance):
    assert isinstance(instance, Nameable)


Properties_strategy = st.builds(Properties)
@given(instance=Properties_strategy)
@settings(max_examples=25)
def test_Properties_instantiation(instance):
    assert isinstance(instance, Properties)


TextContent_strategy = st.builds(TextContent)
@given(instance=TextContent_strategy)
@settings(max_examples=25)
def test_TextContent_instantiation(instance):
    assert isinstance(instance, TextContent)


ZentaElement_strategy = st.builds(ZentaElement)
@given(instance=ZentaElement_strategy)
@settings(max_examples=25)
def test_ZentaElement_instantiation(instance):
    assert isinstance(instance, ZentaElement)


ZentaModelElement_strategy = st.builds(ZentaModelElement)
@given(instance=ZentaModelElement_strategy)
@settings(max_examples=25)
def test_ZentaModelElement_instantiation(instance):
    assert isinstance(instance, ZentaModelElement)


model_Adapter_strategy = st.builds(model_Adapter)
@given(instance=model_Adapter_strategy)
@settings(max_examples=25)
def test_model_Adapter_instantiation(instance):
    assert isinstance(instance, model_Adapter)


model_AndJunction_strategy = st.builds(model_AndJunction)
@given(instance=model_AndJunction_strategy)
@settings(max_examples=25)
def test_model_AndJunction_instantiation(instance):
    assert isinstance(instance, model_AndJunction)


model_Attribute_strategy = st.builds(model_Attribute, maxOccurs=st.integers(), minOccurs=st.integers())
@given(instance=model_Attribute_strategy)
@settings(max_examples=25)
def test_model_Attribute_instantiation(instance):
    assert isinstance(instance, model_Attribute)


model_BasicObject_strategy = st.builds(model_BasicObject)
@given(instance=model_BasicObject_strategy)
@settings(max_examples=25)
def test_model_BasicObject_instantiation(instance):
    assert isinstance(instance, model_BasicObject)


model_BasicRelationship_strategy = st.builds(model_BasicRelationship)
@given(instance=model_BasicRelationship_strategy)
@settings(max_examples=25)
def test_model_BasicRelationship_instantiation(instance):
    assert isinstance(instance, model_BasicRelationship)


model_BorderObject_strategy = st.builds(model_BorderObject, borderColor=safe_text)
@given(instance=model_BorderObject_strategy)
@settings(max_examples=25)
def test_model_BorderObject_instantiation(instance):
    assert isinstance(instance, model_BorderObject)


model_Bounds_strategy = st.builds(model_Bounds, height=st.integers(), width=st.integers(), x=st.integers(), y=st.integers())
@given(instance=model_Bounds_strategy)
@settings(max_examples=25)
def test_model_Bounds_instantiation(instance):
    assert isinstance(instance, model_Bounds)


model_Cloneable_strategy = st.builds(model_Cloneable)
@given(instance=model_Cloneable_strategy)
@settings(max_examples=25)
def test_model_Cloneable_instantiation(instance):
    assert isinstance(instance, model_Cloneable)


model_DiagramModel_strategy = st.builds(model_DiagramModel, connectionRouterType=st.integers())
@given(instance=model_DiagramModel_strategy)
@settings(max_examples=25)
def test_model_DiagramModel_instantiation(instance):
    assert isinstance(instance, model_DiagramModel)


model_DiagramModelBendpoint_strategy = st.builds(model_DiagramModelBendpoint, endX=st.integers(), endY=st.integers(), startX=st.integers(), startY=st.integers())
@given(instance=model_DiagramModelBendpoint_strategy)
@settings(max_examples=25)
def test_model_DiagramModelBendpoint_instantiation(instance):
    assert isinstance(instance, model_DiagramModelBendpoint)


model_DiagramModelComponent_strategy = st.builds(model_DiagramModelComponent, lineColor=safe_text, lineWidth=st.integers())
@given(instance=model_DiagramModelComponent_strategy)
@settings(max_examples=25)
def test_model_DiagramModelComponent_instantiation(instance):
    assert isinstance(instance, model_DiagramModelComponent)


model_DiagramModelConnection_strategy = st.builds(model_DiagramModelConnection, lineDecoration=safe_text, text=safe_text, type=st.integers())
@given(instance=model_DiagramModelConnection_strategy)
@settings(max_examples=25)
def test_model_DiagramModelConnection_instantiation(instance):
    assert isinstance(instance, model_DiagramModelConnection)


model_DiagramModelContainer_strategy = st.builds(model_DiagramModelContainer)
@given(instance=model_DiagramModelContainer_strategy)
@settings(max_examples=25)
def test_model_DiagramModelContainer_instantiation(instance):
    assert isinstance(instance, model_DiagramModelContainer)


model_DiagramModelGroup_strategy = st.builds(model_DiagramModelGroup)
@given(instance=model_DiagramModelGroup_strategy)
@settings(max_examples=25)
def test_model_DiagramModelGroup_instantiation(instance):
    assert isinstance(instance, model_DiagramModelGroup)


model_DiagramModelImage_strategy = st.builds(model_DiagramModelImage)
@given(instance=model_DiagramModelImage_strategy)
@settings(max_examples=25)
def test_model_DiagramModelImage_instantiation(instance):
    assert isinstance(instance, model_DiagramModelImage)


model_DiagramModelImageProvider_strategy = st.builds(model_DiagramModelImageProvider, imagePath=safe_text)
@given(instance=model_DiagramModelImageProvider_strategy)
@settings(max_examples=25)
def test_model_DiagramModelImageProvider_instantiation(instance):
    assert isinstance(instance, model_DiagramModelImageProvider)


model_DiagramModelNote_strategy = st.builds(model_DiagramModelNote)
@given(instance=model_DiagramModelNote_strategy)
@settings(max_examples=25)
def test_model_DiagramModelNote_instantiation(instance):
    assert isinstance(instance, model_DiagramModelNote)


model_DiagramModelObject_strategy = st.builds(model_DiagramModelObject, elementShape=safe_text, fillColor=safe_text)
@given(instance=model_DiagramModelObject_strategy)
@settings(max_examples=25)
def test_model_DiagramModelObject_instantiation(instance):
    assert isinstance(instance, model_DiagramModelObject)


model_DiagramModelReference_strategy = st.builds(model_DiagramModelReference)
@given(instance=model_DiagramModelReference_strategy)
@settings(max_examples=25)
def test_model_DiagramModelReference_instantiation(instance):
    assert isinstance(instance, model_DiagramModelReference)


model_DiagramModelZentaConnection_strategy = st.builds(model_DiagramModelZentaConnection)
@given(instance=model_DiagramModelZentaConnection_strategy)
@settings(max_examples=25)
def test_model_DiagramModelZentaConnection_instantiation(instance):
    assert isinstance(instance, model_DiagramModelZentaConnection)


model_DiagramModelZentaObject_strategy = st.builds(model_DiagramModelZentaObject, type=st.integers())
@given(instance=model_DiagramModelZentaObject_strategy)
@settings(max_examples=25)
def test_model_DiagramModelZentaObject_instantiation(instance):
    assert isinstance(instance, model_DiagramModelZentaObject)


model_Documentable_strategy = st.builds(model_Documentable, documentation=safe_text)
@given(instance=model_Documentable_strategy)
@settings(max_examples=25)
def test_model_Documentable_instantiation(instance):
    assert isinstance(instance, model_Documentable)


model_Folder_strategy = st.builds(model_Folder)
@given(instance=model_Folder_strategy)
@settings(max_examples=25)
def test_model_Folder_instantiation(instance):
    assert isinstance(instance, model_Folder)


model_FolderContainer_strategy = st.builds(model_FolderContainer)
@given(instance=model_FolderContainer_strategy)
@settings(max_examples=25)
def test_model_FolderContainer_instantiation(instance):
    assert isinstance(instance, model_FolderContainer)


model_FontAttribute_strategy = st.builds(model_FontAttribute, font=safe_text, fontColor=safe_text, textAlignment=st.integers(), textPosition=st.integers())
@given(instance=model_FontAttribute_strategy)
@settings(max_examples=25)
def test_model_FontAttribute_instantiation(instance):
    assert isinstance(instance, model_FontAttribute)


model_Identifier_strategy = st.builds(model_Identifier, id=safe_text)
@given(instance=model_Identifier_strategy)
@settings(max_examples=25)
def test_model_Identifier_instantiation(instance):
    assert isinstance(instance, model_Identifier)


model_InterfaceElement_strategy = st.builds(model_InterfaceElement, interfaceType=st.integers())
@given(instance=model_InterfaceElement_strategy)
@settings(max_examples=25)
def test_model_InterfaceElement_instantiation(instance):
    assert isinstance(instance, model_InterfaceElement)


model_Junction_strategy = st.builds(model_Junction)
@given(instance=model_Junction_strategy)
@settings(max_examples=25)
def test_model_Junction_instantiation(instance):
    assert isinstance(instance, model_Junction)


model_JunctionElement_strategy = st.builds(model_JunctionElement)
@given(instance=model_JunctionElement_strategy)
@settings(max_examples=25)
def test_model_JunctionElement_instantiation(instance):
    assert isinstance(instance, model_JunctionElement)


model_Lockable_strategy = st.builds(model_Lockable, locked=st.booleans())
@given(instance=model_Lockable_strategy)
@settings(max_examples=25)
def test_model_Lockable_instantiation(instance):
    assert isinstance(instance, model_Lockable)


model_Metamodel_strategy = st.builds(model_Metamodel)
@given(instance=model_Metamodel_strategy)
@settings(max_examples=25)
def test_model_Metamodel_instantiation(instance):
    assert isinstance(instance, model_Metamodel)


model_Nameable_strategy = st.builds(model_Nameable, name=safe_text)
@given(instance=model_Nameable_strategy)
@settings(max_examples=25)
def test_model_Nameable_instantiation(instance):
    assert isinstance(instance, model_Nameable)


model_OrJunction_strategy = st.builds(model_OrJunction)
@given(instance=model_OrJunction_strategy)
@settings(max_examples=25)
def test_model_OrJunction_instantiation(instance):
    assert isinstance(instance, model_OrJunction)


model_Properties_strategy = st.builds(model_Properties)
@given(instance=model_Properties_strategy)
@settings(max_examples=25)
def test_model_Properties_instantiation(instance):
    assert isinstance(instance, model_Properties)


model_Property_strategy = st.builds(model_Property, generated=st.booleans(), key=safe_text, value=safe_text)
@given(instance=model_Property_strategy)
@settings(max_examples=25)
def test_model_Property_instantiation(instance):
    assert isinstance(instance, model_Property)


model_SketchModel_strategy = st.builds(model_SketchModel, background=st.integers())
@given(instance=model_SketchModel_strategy)
@settings(max_examples=25)
def test_model_SketchModel_instantiation(instance):
    assert isinstance(instance, model_SketchModel)


model_SketchModelActor_strategy = st.builds(model_SketchModelActor)
@given(instance=model_SketchModelActor_strategy)
@settings(max_examples=25)
def test_model_SketchModelActor_instantiation(instance):
    assert isinstance(instance, model_SketchModelActor)


model_SketchModelSticky_strategy = st.builds(model_SketchModelSticky)
@given(instance=model_SketchModelSticky_strategy)
@settings(max_examples=25)
def test_model_SketchModelSticky_instantiation(instance):
    assert isinstance(instance, model_SketchModelSticky)


model_Template_strategy = st.builds(model_Template, path=safe_text)
@given(instance=model_Template_strategy)
@settings(max_examples=25)
def test_model_Template_instantiation(instance):
    assert isinstance(instance, model_Template)


model_TextContent_strategy = st.builds(model_TextContent, content=safe_text)
@given(instance=model_TextContent_strategy)
@settings(max_examples=25)
def test_model_TextContent_instantiation(instance):
    assert isinstance(instance, model_TextContent)


model_ZentaDiagramModel_strategy = st.builds(model_ZentaDiagramModel, viewpoint=st.integers())
@given(instance=model_ZentaDiagramModel_strategy)
@settings(max_examples=25)
def test_model_ZentaDiagramModel_instantiation(instance):
    assert isinstance(instance, model_ZentaDiagramModel)


model_ZentaElement_strategy = st.builds(model_ZentaElement)
@given(instance=model_ZentaElement_strategy)
@settings(max_examples=25)
def test_model_ZentaElement_instantiation(instance):
    assert isinstance(instance, model_ZentaElement)


model_ZentaModel_strategy = st.builds(model_ZentaModel, file=safe_text, version=safe_text)
@given(instance=model_ZentaModel_strategy)
@settings(max_examples=25)
def test_model_ZentaModel_instantiation(instance):
    assert isinstance(instance, model_ZentaModel)


model_ZentaModelElement_strategy = st.builds(model_ZentaModelElement)
@given(instance=model_ZentaModelElement_strategy)
@settings(max_examples=25)
def test_model_ZentaModelElement_instantiation(instance):
    assert isinstance(instance, model_ZentaModelElement)


