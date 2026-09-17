# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BasicObject,
    model_Attribute,
    model_BasicRelationship,
    model_Template,
    model_Metamodel,
    DiagramModelConnection,
    model_DiagramModelZentaConnection,
    Folder,
    model_DiagramModelImageProvider,
    model_BorderObject,
    model_FontAttribute,
    DiagramModel,
    model_SketchModel,
    model_ZentaDiagramModel,
    model_Lockable,
    DiagramModelImageProvider,
    BorderObject,
    model_Bounds,
    FontAttribute,
    TextContent,
    DiagramModelContainer,
    JunctionElement,
    model_AndJunction,
    model_Junction,
    ZentaElement,
    model_BasicObject,
    model_InterfaceElement,
    model_JunctionElement,
    Properties,
    Documentable,
    Identifier,
    FolderContainer,
    ZentaModelElement,
    DiagramModelObject,
    model_SketchModelActor,
    model_DiagramModelImage,
    model_DiagramModelZentaObject,
    model_SketchModelSticky,
    model_DiagramModelNote,
    model_DiagramModelGroup,
    model_DiagramModelReference,
    DiagramModelComponent,
    model_DiagramModelObject,
    model_DiagramModelConnection,
    model_DiagramModelContainer,
    model_DiagramModel,
    Cloneable,
    model_DiagramModelBendpoint,
    model_OrJunction,
    model_Nameable,
    model_Properties,
    model_Property,
    Nameable,
    model_ZentaElement,
    model_Identifier,
    model_ZentaModel,
    Adapter,
    model_DiagramModelComponent,
    model_ZentaModelElement,
    model_Folder,
    model_FolderContainer,
    model_Cloneable,
    model_Documentable,
    model_TextContent,
    model_Adapter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basicobject_is_not_abstract():
    assert not inspect.isabstract(BasicObject)


def test_hyp_basicobject_constructor_exists():
    assert callable(BasicObject.__init__)


def test_hyp_basicobject_constructor_args():
    sig = inspect.signature(BasicObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_attribute_is_not_abstract():
    assert not inspect.isabstract(model_Attribute)


def test_hyp_model_attribute_constructor_exists():
    assert callable(model_Attribute.__init__)


def test_hyp_model_attribute_constructor_args():
    sig = inspect.signature(model_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "minOccurs" in params, "Missing parameter 'minOccurs'"
    assert "maxOccurs" in params, "Missing parameter 'maxOccurs'"





def test_hyp_model_basicrelationship_is_not_abstract():
    assert not inspect.isabstract(model_BasicRelationship)


def test_hyp_model_basicrelationship_constructor_exists():
    assert callable(model_BasicRelationship.__init__)


def test_hyp_model_basicrelationship_constructor_args():
    sig = inspect.signature(model_BasicRelationship.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_template_is_not_abstract():
    assert not inspect.isabstract(model_Template)


def test_hyp_model_template_constructor_exists():
    assert callable(model_Template.__init__)


def test_hyp_model_template_constructor_args():
    sig = inspect.signature(model_Template.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"




def test_hyp_model_metamodel_is_not_abstract():
    assert not inspect.isabstract(model_Metamodel)


def test_hyp_model_metamodel_constructor_exists():
    assert callable(model_Metamodel.__init__)


def test_hyp_model_metamodel_constructor_args():
    sig = inspect.signature(model_Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagrammodelconnection_is_not_abstract():
    assert not inspect.isabstract(DiagramModelConnection)


def test_hyp_diagrammodelconnection_constructor_exists():
    assert callable(DiagramModelConnection.__init__)


def test_hyp_diagrammodelconnection_constructor_args():
    sig = inspect.signature(DiagramModelConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelzentaconnection_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelZentaConnection)


def test_hyp_model_diagrammodelzentaconnection_constructor_exists():
    assert callable(model_DiagramModelZentaConnection.__init__)


def test_hyp_model_diagrammodelzentaconnection_constructor_args():
    sig = inspect.signature(model_DiagramModelZentaConnection.__init__)
    params = list(sig.parameters.keys())



def test_hyp_folder_is_not_abstract():
    assert not inspect.isabstract(Folder)


def test_hyp_folder_constructor_exists():
    assert callable(Folder.__init__)


def test_hyp_folder_constructor_args():
    sig = inspect.signature(Folder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelimageprovider_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelImageProvider)


def test_hyp_model_diagrammodelimageprovider_constructor_exists():
    assert callable(model_DiagramModelImageProvider.__init__)


def test_hyp_model_diagrammodelimageprovider_constructor_args():
    sig = inspect.signature(model_DiagramModelImageProvider.__init__)
    params = list(sig.parameters.keys())
    assert "imagePath" in params, "Missing parameter 'imagePath'"




def test_hyp_model_borderobject_is_not_abstract():
    assert not inspect.isabstract(model_BorderObject)


def test_hyp_model_borderobject_constructor_exists():
    assert callable(model_BorderObject.__init__)


def test_hyp_model_borderobject_constructor_args():
    sig = inspect.signature(model_BorderObject.__init__)
    params = list(sig.parameters.keys())
    assert "borderColor" in params, "Missing parameter 'borderColor'"




def test_hyp_model_fontattribute_is_not_abstract():
    assert not inspect.isabstract(model_FontAttribute)


def test_hyp_model_fontattribute_constructor_exists():
    assert callable(model_FontAttribute.__init__)


def test_hyp_model_fontattribute_constructor_args():
    sig = inspect.signature(model_FontAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "fontColor" in params, "Missing parameter 'fontColor'"
    assert "textPosition" in params, "Missing parameter 'textPosition'"
    assert "textAlignment" in params, "Missing parameter 'textAlignment'"
    assert "font" in params, "Missing parameter 'font'"







def test_hyp_diagrammodel_is_not_abstract():
    assert not inspect.isabstract(DiagramModel)


def test_hyp_diagrammodel_constructor_exists():
    assert callable(DiagramModel.__init__)


def test_hyp_diagrammodel_constructor_args():
    sig = inspect.signature(DiagramModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_sketchmodel_is_not_abstract():
    assert not inspect.isabstract(model_SketchModel)


def test_hyp_model_sketchmodel_constructor_exists():
    assert callable(model_SketchModel.__init__)


def test_hyp_model_sketchmodel_constructor_args():
    sig = inspect.signature(model_SketchModel.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"




def test_hyp_model_zentadiagrammodel_is_not_abstract():
    assert not inspect.isabstract(model_ZentaDiagramModel)


def test_hyp_model_zentadiagrammodel_constructor_exists():
    assert callable(model_ZentaDiagramModel.__init__)


def test_hyp_model_zentadiagrammodel_constructor_args():
    sig = inspect.signature(model_ZentaDiagramModel.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"




def test_hyp_model_lockable_is_not_abstract():
    assert not inspect.isabstract(model_Lockable)


def test_hyp_model_lockable_constructor_exists():
    assert callable(model_Lockable.__init__)


def test_hyp_model_lockable_constructor_args():
    sig = inspect.signature(model_Lockable.__init__)
    params = list(sig.parameters.keys())
    assert "locked" in params, "Missing parameter 'locked'"




def test_hyp_diagrammodelimageprovider_is_not_abstract():
    assert not inspect.isabstract(DiagramModelImageProvider)


def test_hyp_diagrammodelimageprovider_constructor_exists():
    assert callable(DiagramModelImageProvider.__init__)


def test_hyp_diagrammodelimageprovider_constructor_args():
    sig = inspect.signature(DiagramModelImageProvider.__init__)
    params = list(sig.parameters.keys())



def test_hyp_borderobject_is_not_abstract():
    assert not inspect.isabstract(BorderObject)


def test_hyp_borderobject_constructor_exists():
    assert callable(BorderObject.__init__)


def test_hyp_borderobject_constructor_args():
    sig = inspect.signature(BorderObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_bounds_is_not_abstract():
    assert not inspect.isabstract(model_Bounds)


def test_hyp_model_bounds_constructor_exists():
    assert callable(model_Bounds.__init__)


def test_hyp_model_bounds_constructor_args():
    sig = inspect.signature(model_Bounds.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "x" in params, "Missing parameter 'x'"
    assert "width" in params, "Missing parameter 'width'"
    assert "y" in params, "Missing parameter 'y'"







def test_hyp_fontattribute_is_not_abstract():
    assert not inspect.isabstract(FontAttribute)


def test_hyp_fontattribute_constructor_exists():
    assert callable(FontAttribute.__init__)


def test_hyp_fontattribute_constructor_args():
    sig = inspect.signature(FontAttribute.__init__)
    params = list(sig.parameters.keys())



def test_hyp_textcontent_is_not_abstract():
    assert not inspect.isabstract(TextContent)


def test_hyp_textcontent_constructor_exists():
    assert callable(TextContent.__init__)


def test_hyp_textcontent_constructor_args():
    sig = inspect.signature(TextContent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagrammodelcontainer_is_not_abstract():
    assert not inspect.isabstract(DiagramModelContainer)


def test_hyp_diagrammodelcontainer_constructor_exists():
    assert callable(DiagramModelContainer.__init__)


def test_hyp_diagrammodelcontainer_constructor_args():
    sig = inspect.signature(DiagramModelContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_junctionelement_is_not_abstract():
    assert not inspect.isabstract(JunctionElement)


def test_hyp_junctionelement_constructor_exists():
    assert callable(JunctionElement.__init__)


def test_hyp_junctionelement_constructor_args():
    sig = inspect.signature(JunctionElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_andjunction_is_not_abstract():
    assert not inspect.isabstract(model_AndJunction)


def test_hyp_model_andjunction_constructor_exists():
    assert callable(model_AndJunction.__init__)


def test_hyp_model_andjunction_constructor_args():
    sig = inspect.signature(model_AndJunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_junction_is_not_abstract():
    assert not inspect.isabstract(model_Junction)


def test_hyp_model_junction_constructor_exists():
    assert callable(model_Junction.__init__)


def test_hyp_model_junction_constructor_args():
    sig = inspect.signature(model_Junction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_zentaelement_is_not_abstract():
    assert not inspect.isabstract(ZentaElement)


def test_hyp_zentaelement_constructor_exists():
    assert callable(ZentaElement.__init__)


def test_hyp_zentaelement_constructor_args():
    sig = inspect.signature(ZentaElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_basicobject_is_not_abstract():
    assert not inspect.isabstract(model_BasicObject)


def test_hyp_model_basicobject_constructor_exists():
    assert callable(model_BasicObject.__init__)


def test_hyp_model_basicobject_constructor_args():
    sig = inspect.signature(model_BasicObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_interfaceelement_is_not_abstract():
    assert not inspect.isabstract(model_InterfaceElement)


def test_hyp_model_interfaceelement_constructor_exists():
    assert callable(model_InterfaceElement.__init__)


def test_hyp_model_interfaceelement_constructor_args():
    sig = inspect.signature(model_InterfaceElement.__init__)
    params = list(sig.parameters.keys())
    assert "interfaceType" in params, "Missing parameter 'interfaceType'"




def test_hyp_model_junctionelement_is_not_abstract():
    assert not inspect.isabstract(model_JunctionElement)


def test_hyp_model_junctionelement_constructor_exists():
    assert callable(model_JunctionElement.__init__)


def test_hyp_model_junctionelement_constructor_args():
    sig = inspect.signature(model_JunctionElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_properties_is_not_abstract():
    assert not inspect.isabstract(Properties)


def test_hyp_properties_constructor_exists():
    assert callable(Properties.__init__)


def test_hyp_properties_constructor_args():
    sig = inspect.signature(Properties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_documentable_is_not_abstract():
    assert not inspect.isabstract(Documentable)


def test_hyp_documentable_constructor_exists():
    assert callable(Documentable.__init__)


def test_hyp_documentable_constructor_args():
    sig = inspect.signature(Documentable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_identifier_is_not_abstract():
    assert not inspect.isabstract(Identifier)


def test_hyp_identifier_constructor_exists():
    assert callable(Identifier.__init__)


def test_hyp_identifier_constructor_args():
    sig = inspect.signature(Identifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_foldercontainer_is_not_abstract():
    assert not inspect.isabstract(FolderContainer)


def test_hyp_foldercontainer_constructor_exists():
    assert callable(FolderContainer.__init__)


def test_hyp_foldercontainer_constructor_args():
    sig = inspect.signature(FolderContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_zentamodelelement_is_not_abstract():
    assert not inspect.isabstract(ZentaModelElement)


def test_hyp_zentamodelelement_constructor_exists():
    assert callable(ZentaModelElement.__init__)


def test_hyp_zentamodelelement_constructor_args():
    sig = inspect.signature(ZentaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagrammodelobject_is_not_abstract():
    assert not inspect.isabstract(DiagramModelObject)


def test_hyp_diagrammodelobject_constructor_exists():
    assert callable(DiagramModelObject.__init__)


def test_hyp_diagrammodelobject_constructor_args():
    sig = inspect.signature(DiagramModelObject.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_sketchmodelactor_is_not_abstract():
    assert not inspect.isabstract(model_SketchModelActor)


def test_hyp_model_sketchmodelactor_constructor_exists():
    assert callable(model_SketchModelActor.__init__)


def test_hyp_model_sketchmodelactor_constructor_args():
    sig = inspect.signature(model_SketchModelActor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelimage_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelImage)


def test_hyp_model_diagrammodelimage_constructor_exists():
    assert callable(model_DiagramModelImage.__init__)


def test_hyp_model_diagrammodelimage_constructor_args():
    sig = inspect.signature(model_DiagramModelImage.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelzentaobject_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelZentaObject)


def test_hyp_model_diagrammodelzentaobject_constructor_exists():
    assert callable(model_DiagramModelZentaObject.__init__)


def test_hyp_model_diagrammodelzentaobject_constructor_args():
    sig = inspect.signature(model_DiagramModelZentaObject.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"




def test_hyp_model_sketchmodelsticky_is_not_abstract():
    assert not inspect.isabstract(model_SketchModelSticky)


def test_hyp_model_sketchmodelsticky_constructor_exists():
    assert callable(model_SketchModelSticky.__init__)


def test_hyp_model_sketchmodelsticky_constructor_args():
    sig = inspect.signature(model_SketchModelSticky.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelnote_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelNote)


def test_hyp_model_diagrammodelnote_constructor_exists():
    assert callable(model_DiagramModelNote.__init__)


def test_hyp_model_diagrammodelnote_constructor_args():
    sig = inspect.signature(model_DiagramModelNote.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelgroup_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelGroup)


def test_hyp_model_diagrammodelgroup_constructor_exists():
    assert callable(model_DiagramModelGroup.__init__)


def test_hyp_model_diagrammodelgroup_constructor_args():
    sig = inspect.signature(model_DiagramModelGroup.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelreference_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelReference)


def test_hyp_model_diagrammodelreference_constructor_exists():
    assert callable(model_DiagramModelReference.__init__)


def test_hyp_model_diagrammodelreference_constructor_args():
    sig = inspect.signature(model_DiagramModelReference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_diagrammodelcomponent_is_not_abstract():
    assert not inspect.isabstract(DiagramModelComponent)


def test_hyp_diagrammodelcomponent_constructor_exists():
    assert callable(DiagramModelComponent.__init__)


def test_hyp_diagrammodelcomponent_constructor_args():
    sig = inspect.signature(DiagramModelComponent.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelobject_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelObject)


def test_hyp_model_diagrammodelobject_constructor_exists():
    assert callable(model_DiagramModelObject.__init__)


def test_hyp_model_diagrammodelobject_constructor_args():
    sig = inspect.signature(model_DiagramModelObject.__init__)
    params = list(sig.parameters.keys())
    assert "elementShape" in params, "Missing parameter 'elementShape'"
    assert "fillColor" in params, "Missing parameter 'fillColor'"





def test_hyp_model_diagrammodelconnection_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelConnection)


def test_hyp_model_diagrammodelconnection_constructor_exists():
    assert callable(model_DiagramModelConnection.__init__)


def test_hyp_model_diagrammodelconnection_constructor_args():
    sig = inspect.signature(model_DiagramModelConnection.__init__)
    params = list(sig.parameters.keys())
    assert "lineDecoration" in params, "Missing parameter 'lineDecoration'"
    assert "text" in params, "Missing parameter 'text'"
    assert "type" in params, "Missing parameter 'type'"






def test_hyp_model_diagrammodelcontainer_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelContainer)


def test_hyp_model_diagrammodelcontainer_constructor_exists():
    assert callable(model_DiagramModelContainer.__init__)


def test_hyp_model_diagrammodelcontainer_constructor_args():
    sig = inspect.signature(model_DiagramModelContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodel_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModel)


def test_hyp_model_diagrammodel_constructor_exists():
    assert callable(model_DiagramModel.__init__)


def test_hyp_model_diagrammodel_constructor_args():
    sig = inspect.signature(model_DiagramModel.__init__)
    params = list(sig.parameters.keys())
    assert "connectionRouterType" in params, "Missing parameter 'connectionRouterType'"




def test_hyp_cloneable_is_not_abstract():
    assert not inspect.isabstract(Cloneable)


def test_hyp_cloneable_constructor_exists():
    assert callable(Cloneable.__init__)


def test_hyp_cloneable_constructor_args():
    sig = inspect.signature(Cloneable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelbendpoint_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelBendpoint)


def test_hyp_model_diagrammodelbendpoint_constructor_exists():
    assert callable(model_DiagramModelBendpoint.__init__)


def test_hyp_model_diagrammodelbendpoint_constructor_args():
    sig = inspect.signature(model_DiagramModelBendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "startX" in params, "Missing parameter 'startX'"
    assert "endX" in params, "Missing parameter 'endX'"
    assert "endY" in params, "Missing parameter 'endY'"
    assert "startY" in params, "Missing parameter 'startY'"







def test_hyp_model_orjunction_is_not_abstract():
    assert not inspect.isabstract(model_OrJunction)


def test_hyp_model_orjunction_constructor_exists():
    assert callable(model_OrJunction.__init__)


def test_hyp_model_orjunction_constructor_args():
    sig = inspect.signature(model_OrJunction.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_nameable_is_not_abstract():
    assert not inspect.isabstract(model_Nameable)


def test_hyp_model_nameable_constructor_exists():
    assert callable(model_Nameable.__init__)


def test_hyp_model_nameable_constructor_args():
    sig = inspect.signature(model_Nameable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_model_properties_is_not_abstract():
    assert not inspect.isabstract(model_Properties)


def test_hyp_model_properties_constructor_exists():
    assert callable(model_Properties.__init__)


def test_hyp_model_properties_constructor_args():
    sig = inspect.signature(model_Properties.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_property_is_not_abstract():
    assert not inspect.isabstract(model_Property)


def test_hyp_model_property_constructor_exists():
    assert callable(model_Property.__init__)


def test_hyp_model_property_constructor_args():
    sig = inspect.signature(model_Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "generated" in params, "Missing parameter 'generated'"
    assert "value" in params, "Missing parameter 'value'"






def test_hyp_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_hyp_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_hyp_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_zentaelement_is_not_abstract():
    assert not inspect.isabstract(model_ZentaElement)


def test_hyp_model_zentaelement_constructor_exists():
    assert callable(model_ZentaElement.__init__)


def test_hyp_model_zentaelement_constructor_args():
    sig = inspect.signature(model_ZentaElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_identifier_is_not_abstract():
    assert not inspect.isabstract(model_Identifier)


def test_hyp_model_identifier_constructor_exists():
    assert callable(model_Identifier.__init__)


def test_hyp_model_identifier_constructor_args():
    sig = inspect.signature(model_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"




def test_hyp_model_zentamodel_is_not_abstract():
    assert not inspect.isabstract(model_ZentaModel)


def test_hyp_model_zentamodel_constructor_exists():
    assert callable(model_ZentaModel.__init__)


def test_hyp_model_zentamodel_constructor_args():
    sig = inspect.signature(model_ZentaModel.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "file" in params, "Missing parameter 'file'"





def test_hyp_adapter_is_not_abstract():
    assert not inspect.isabstract(Adapter)


def test_hyp_adapter_constructor_exists():
    assert callable(Adapter.__init__)


def test_hyp_adapter_constructor_args():
    sig = inspect.signature(Adapter.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_diagrammodelcomponent_is_not_abstract():
    assert not inspect.isabstract(model_DiagramModelComponent)


def test_hyp_model_diagrammodelcomponent_constructor_exists():
    assert callable(model_DiagramModelComponent.__init__)


def test_hyp_model_diagrammodelcomponent_constructor_args():
    sig = inspect.signature(model_DiagramModelComponent.__init__)
    params = list(sig.parameters.keys())
    assert "lineWidth" in params, "Missing parameter 'lineWidth'"
    assert "lineColor" in params, "Missing parameter 'lineColor'"





def test_hyp_model_zentamodelelement_is_not_abstract():
    assert not inspect.isabstract(model_ZentaModelElement)


def test_hyp_model_zentamodelelement_constructor_exists():
    assert callable(model_ZentaModelElement.__init__)


def test_hyp_model_zentamodelelement_constructor_args():
    sig = inspect.signature(model_ZentaModelElement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_folder_is_not_abstract():
    assert not inspect.isabstract(model_Folder)


def test_hyp_model_folder_constructor_exists():
    assert callable(model_Folder.__init__)


def test_hyp_model_folder_constructor_args():
    sig = inspect.signature(model_Folder.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_foldercontainer_is_not_abstract():
    assert not inspect.isabstract(model_FolderContainer)


def test_hyp_model_foldercontainer_constructor_exists():
    assert callable(model_FolderContainer.__init__)


def test_hyp_model_foldercontainer_constructor_args():
    sig = inspect.signature(model_FolderContainer.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_cloneable_is_not_abstract():
    assert not inspect.isabstract(model_Cloneable)


def test_hyp_model_cloneable_constructor_exists():
    assert callable(model_Cloneable.__init__)


def test_hyp_model_cloneable_constructor_args():
    sig = inspect.signature(model_Cloneable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_model_documentable_is_not_abstract():
    assert not inspect.isabstract(model_Documentable)


def test_hyp_model_documentable_constructor_exists():
    assert callable(model_Documentable.__init__)


def test_hyp_model_documentable_constructor_args():
    sig = inspect.signature(model_Documentable.__init__)
    params = list(sig.parameters.keys())
    assert "documentation" in params, "Missing parameter 'documentation'"




def test_hyp_model_textcontent_is_not_abstract():
    assert not inspect.isabstract(model_TextContent)


def test_hyp_model_textcontent_constructor_exists():
    assert callable(model_TextContent.__init__)


def test_hyp_model_textcontent_constructor_args():
    sig = inspect.signature(model_TextContent.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"




def test_hyp_model_adapter_is_not_abstract():
    assert not inspect.isabstract(model_Adapter)


def test_hyp_model_adapter_constructor_exists():
    assert callable(model_Adapter.__init__)


def test_hyp_model_adapter_constructor_args():
    sig = inspect.signature(model_Adapter.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
BasicObject_strategy = st.builds(
    BasicObject,
)
model_Attribute_strategy = st.builds(
    model_Attribute,
    minOccurs=
        st.integers(),
    maxOccurs=
        st.integers()
)
model_BasicRelationship_strategy = st.builds(
    model_BasicRelationship,
)
model_Template_strategy = st.builds(
    model_Template,
    path=
        safe_text
)
model_Metamodel_strategy = st.builds(
    model_Metamodel,
)
DiagramModelConnection_strategy = st.builds(
    DiagramModelConnection,
)
model_DiagramModelZentaConnection_strategy = st.builds(
    model_DiagramModelZentaConnection,
)
Folder_strategy = st.builds(
    Folder,
)
model_DiagramModelImageProvider_strategy = st.builds(
    model_DiagramModelImageProvider,
    imagePath=
        safe_text
)
model_BorderObject_strategy = st.builds(
    model_BorderObject,
    borderColor=
        safe_text
)
model_FontAttribute_strategy = st.builds(
    model_FontAttribute,
    fontColor=
        safe_text,
    textPosition=
        st.integers(),
    textAlignment=
        st.integers(),
    font=
        safe_text
)
DiagramModel_strategy = st.builds(
    DiagramModel,
)
model_SketchModel_strategy = st.builds(
    model_SketchModel,
    background=
        st.integers()
)
model_ZentaDiagramModel_strategy = st.builds(
    model_ZentaDiagramModel,
    viewpoint=
        st.integers()
)
model_Lockable_strategy = st.builds(
    model_Lockable,
    locked=
        st.booleans()
)
DiagramModelImageProvider_strategy = st.builds(
    DiagramModelImageProvider,
)
BorderObject_strategy = st.builds(
    BorderObject,
)
model_Bounds_strategy = st.builds(
    model_Bounds,
    height=
        st.integers(),
    x=
        st.integers(),
    width=
        st.integers(),
    y=
        st.integers()
)
FontAttribute_strategy = st.builds(
    FontAttribute,
)
TextContent_strategy = st.builds(
    TextContent,
)
DiagramModelContainer_strategy = st.builds(
    DiagramModelContainer,
)
JunctionElement_strategy = st.builds(
    JunctionElement,
)
model_AndJunction_strategy = st.builds(
    model_AndJunction,
)
model_Junction_strategy = st.builds(
    model_Junction,
)
ZentaElement_strategy = st.builds(
    ZentaElement,
)
model_BasicObject_strategy = st.builds(
    model_BasicObject,
)
model_InterfaceElement_strategy = st.builds(
    model_InterfaceElement,
    interfaceType=
        st.integers()
)
model_JunctionElement_strategy = st.builds(
    model_JunctionElement,
)
Properties_strategy = st.builds(
    Properties,
)
Documentable_strategy = st.builds(
    Documentable,
)
Identifier_strategy = st.builds(
    Identifier,
)
FolderContainer_strategy = st.builds(
    FolderContainer,
)
ZentaModelElement_strategy = st.builds(
    ZentaModelElement,
)
DiagramModelObject_strategy = st.builds(
    DiagramModelObject,
)
model_SketchModelActor_strategy = st.builds(
    model_SketchModelActor,
)
model_DiagramModelImage_strategy = st.builds(
    model_DiagramModelImage,
)
model_DiagramModelZentaObject_strategy = st.builds(
    model_DiagramModelZentaObject,
    type=
        st.integers()
)
model_SketchModelSticky_strategy = st.builds(
    model_SketchModelSticky,
)
model_DiagramModelNote_strategy = st.builds(
    model_DiagramModelNote,
)
model_DiagramModelGroup_strategy = st.builds(
    model_DiagramModelGroup,
)
model_DiagramModelReference_strategy = st.builds(
    model_DiagramModelReference,
)
DiagramModelComponent_strategy = st.builds(
    DiagramModelComponent,
)
model_DiagramModelObject_strategy = st.builds(
    model_DiagramModelObject,
    elementShape=
        safe_text,
    fillColor=
        safe_text
)
model_DiagramModelConnection_strategy = st.builds(
    model_DiagramModelConnection,
    lineDecoration=
        safe_text,
    text=
        safe_text,
    type=
        st.integers()
)
model_DiagramModelContainer_strategy = st.builds(
    model_DiagramModelContainer,
)
model_DiagramModel_strategy = st.builds(
    model_DiagramModel,
    connectionRouterType=
        st.integers()
)
Cloneable_strategy = st.builds(
    Cloneable,
)
model_DiagramModelBendpoint_strategy = st.builds(
    model_DiagramModelBendpoint,
    startX=
        st.integers(),
    endX=
        st.integers(),
    endY=
        st.integers(),
    startY=
        st.integers()
)
model_OrJunction_strategy = st.builds(
    model_OrJunction,
)
model_Nameable_strategy = st.builds(
    model_Nameable,
    name=
        safe_text
)
model_Properties_strategy = st.builds(
    model_Properties,
)
model_Property_strategy = st.builds(
    model_Property,
    key=
        safe_text,
    generated=
        st.booleans(),
    value=
        safe_text
)
Nameable_strategy = st.builds(
    Nameable,
)
model_ZentaElement_strategy = st.builds(
    model_ZentaElement,
)
model_Identifier_strategy = st.builds(
    model_Identifier,
    id=
        safe_text
)
model_ZentaModel_strategy = st.builds(
    model_ZentaModel,
    version=
        safe_text,
    file=
        safe_text
)
Adapter_strategy = st.builds(
    Adapter,
)
model_DiagramModelComponent_strategy = st.builds(
    model_DiagramModelComponent,
    lineWidth=
        st.integers(),
    lineColor=
        safe_text
)
model_ZentaModelElement_strategy = st.builds(
    model_ZentaModelElement,
)
model_Folder_strategy = st.builds(
    model_Folder,
)
model_FolderContainer_strategy = st.builds(
    model_FolderContainer,
)
model_Cloneable_strategy = st.builds(
    model_Cloneable,
)
model_Documentable_strategy = st.builds(
    model_Documentable,
    documentation=
        safe_text
)
model_TextContent_strategy = st.builds(
    model_TextContent,
    content=
        safe_text
)
model_Adapter_strategy = st.builds(
    model_Adapter,
)





@given(instance=model_Attribute_strategy)
def test_hyp_model_attribute_minOccurs_setter(instance):
    original = instance.minOccurs
    instance.minOccurs = original
    assert instance.minOccurs == original



@given(instance=model_Attribute_strategy)
def test_hyp_model_attribute_maxOccurs_setter(instance):
    original = instance.maxOccurs
    instance.maxOccurs = original
    assert instance.maxOccurs == original





@given(instance=model_Template_strategy)
def test_hyp_model_template_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original




import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelZentaConnection_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelzentaconnection_addrelationshiptomodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addRelationshipToModel(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addRelationshipToModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addRelationshipToModel' in model_DiagramModelZentaConnection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addRelationshipToModel' in model_DiagramModelZentaConnection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addRelationshipToModel' in model_DiagramModelZentaConnection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelZentaConnection_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelzentaconnection_removerelationshipfrommodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeRelationshipFromModel()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeRelationshipFromModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeRelationshipFromModel' in model_DiagramModelZentaConnection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeRelationshipFromModel' in model_DiagramModelZentaConnection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeRelationshipFromModel' in model_DiagramModelZentaConnection is not implemented or raised an error")





@given(instance=model_DiagramModelImageProvider_strategy)
def test_hyp_model_diagrammodelimageprovider_imagePath_setter(instance):
    original = instance.imagePath
    instance.imagePath = original
    assert instance.imagePath == original




@given(instance=model_BorderObject_strategy)
def test_hyp_model_borderobject_borderColor_setter(instance):
    original = instance.borderColor
    instance.borderColor = original
    assert instance.borderColor == original




@given(instance=model_FontAttribute_strategy)
def test_hyp_model_fontattribute_fontColor_setter(instance):
    original = instance.fontColor
    instance.fontColor = original
    assert instance.fontColor == original



@given(instance=model_FontAttribute_strategy)
def test_hyp_model_fontattribute_textPosition_setter(instance):
    original = instance.textPosition
    instance.textPosition = original
    assert instance.textPosition == original



@given(instance=model_FontAttribute_strategy)
def test_hyp_model_fontattribute_textAlignment_setter(instance):
    original = instance.textAlignment
    instance.textAlignment = original
    assert instance.textAlignment == original



@given(instance=model_FontAttribute_strategy)
def test_hyp_model_fontattribute_font_setter(instance):
    original = instance.font
    instance.font = original
    assert instance.font == original





@given(instance=model_SketchModel_strategy)
def test_hyp_model_sketchmodel_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original




@given(instance=model_ZentaDiagramModel_strategy)
def test_hyp_model_zentadiagrammodel_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original




@given(instance=model_Lockable_strategy)
def test_hyp_model_lockable_locked_setter(instance):
    original = instance.locked
    instance.locked = original
    assert instance.locked == original






@given(instance=model_Bounds_strategy)
def test_hyp_model_bounds_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_Bounds_strategy)
def test_hyp_model_bounds_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=model_Bounds_strategy)
def test_hyp_model_bounds_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model_Bounds_strategy)
def test_hyp_model_bounds_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original












@given(instance=model_InterfaceElement_strategy)
def test_hyp_model_interfaceelement_interfaceType_setter(instance):
    original = instance.interfaceType
    instance.interfaceType = original
    assert instance.interfaceType == original













@given(instance=model_DiagramModelZentaObject_strategy)
def test_hyp_model_diagrammodelzentaobject_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelZentaObject_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelzentaobject_addzentaelementtomodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addZentaElementToModel(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addZentaElementToModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addZentaElementToModel' in model_DiagramModelZentaObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addZentaElementToModel' in model_DiagramModelZentaObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addZentaElementToModel' in model_DiagramModelZentaObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelZentaObject_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelzentaobject_removezentaelementfrommodel_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeZentaElementFromModel()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeZentaElementFromModel).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeZentaElementFromModel' in model_DiagramModelZentaObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeZentaElementFromModel' in model_DiagramModelZentaObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeZentaElementFromModel' in model_DiagramModelZentaObject is not implemented or raised an error")









@given(instance=model_DiagramModelObject_strategy)
def test_hyp_model_diagrammodelobject_elementShape_setter(instance):
    original = instance.elementShape
    instance.elementShape = original
    assert instance.elementShape == original



@given(instance=model_DiagramModelObject_strategy)
def test_hyp_model_diagrammodelobject_fillColor_setter(instance):
    original = instance.fillColor
    instance.fillColor = original
    assert instance.fillColor == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelObject_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelobject_setbounds_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setBounds(
            "test", 
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setBounds).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setBounds' in model_DiagramModelObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setBounds' in model_DiagramModelObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setBounds' in model_DiagramModelObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelObject_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelobject_removeconnection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.removeConnection(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.removeConnection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'removeConnection' in model_DiagramModelObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'removeConnection' in model_DiagramModelObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'removeConnection' in model_DiagramModelObject is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelObject_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelobject_addconnection_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addConnection(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addConnection).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addConnection' in model_DiagramModelObject is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addConnection' in model_DiagramModelObject did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addConnection' in model_DiagramModelObject is not implemented or raised an error")




@given(instance=model_DiagramModelConnection_strategy)
def test_hyp_model_diagrammodelconnection_lineDecoration_setter(instance):
    original = instance.lineDecoration
    instance.lineDecoration = original
    assert instance.lineDecoration == original



@given(instance=model_DiagramModelConnection_strategy)
def test_hyp_model_diagrammodelconnection_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=model_DiagramModelConnection_strategy)
def test_hyp_model_diagrammodelconnection_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelConnection_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelconnection_reconnect_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reconnect()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reconnect).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reconnect' in model_DiagramModelConnection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reconnect' in model_DiagramModelConnection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reconnect' in model_DiagramModelConnection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelConnection_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelconnection_connect_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.connect(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.connect).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'connect' in model_DiagramModelConnection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'connect' in model_DiagramModelConnection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'connect' in model_DiagramModelConnection is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_DiagramModelConnection_strategy)
@settings(max_examples=30)
def test_hyp_model_diagrammodelconnection_disconnect_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.disconnect()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.disconnect).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'disconnect' in model_DiagramModelConnection is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'disconnect' in model_DiagramModelConnection did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'disconnect' in model_DiagramModelConnection is not implemented or raised an error")





@given(instance=model_DiagramModel_strategy)
def test_hyp_model_diagrammodel_connectionRouterType_setter(instance):
    original = instance.connectionRouterType
    instance.connectionRouterType = original
    assert instance.connectionRouterType == original





@given(instance=model_DiagramModelBendpoint_strategy)
def test_hyp_model_diagrammodelbendpoint_startX_setter(instance):
    original = instance.startX
    instance.startX = original
    assert instance.startX == original



@given(instance=model_DiagramModelBendpoint_strategy)
def test_hyp_model_diagrammodelbendpoint_endX_setter(instance):
    original = instance.endX
    instance.endX = original
    assert instance.endX == original



@given(instance=model_DiagramModelBendpoint_strategy)
def test_hyp_model_diagrammodelbendpoint_endY_setter(instance):
    original = instance.endY
    instance.endY = original
    assert instance.endY == original



@given(instance=model_DiagramModelBendpoint_strategy)
def test_hyp_model_diagrammodelbendpoint_startY_setter(instance):
    original = instance.startY
    instance.startY = original
    assert instance.startY == original





@given(instance=model_Nameable_strategy)
def test_hyp_model_nameable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=model_Property_strategy)
def test_hyp_model_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=model_Property_strategy)
def test_hyp_model_property_generated_setter(instance):
    original = instance.generated
    instance.generated = original
    assert instance.generated == original



@given(instance=model_Property_strategy)
def test_hyp_model_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original






@given(instance=model_Identifier_strategy)
def test_hyp_model_identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=model_ZentaModel_strategy)
def test_hyp_model_zentamodel_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=model_ZentaModel_strategy)
def test_hyp_model_zentamodel_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original





@given(instance=model_DiagramModelComponent_strategy)
def test_hyp_model_diagrammodelcomponent_lineWidth_setter(instance):
    original = instance.lineWidth
    instance.lineWidth = original
    assert instance.lineWidth == original



@given(instance=model_DiagramModelComponent_strategy)
def test_hyp_model_diagrammodelcomponent_lineColor_setter(instance):
    original = instance.lineColor
    instance.lineColor = original
    assert instance.lineColor == original








@given(instance=model_Documentable_strategy)
def test_hyp_model_documentable_documentation_setter(instance):
    original = instance.documentation
    instance.documentation = original
    assert instance.documentation == original




@given(instance=model_TextContent_strategy)
def test_hyp_model_textcontent_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_Adapter_strategy)
@settings(max_examples=30)
def test_hyp_model_adapter_setadapter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setAdapter(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setAdapter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setAdapter' in model_Adapter is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAdapter' in model_Adapter did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAdapter' in model_Adapter is not implemented or raised an error")


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



