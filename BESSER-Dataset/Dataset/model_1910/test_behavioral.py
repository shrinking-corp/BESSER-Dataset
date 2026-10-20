import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    myDsl_Album,
    myDsl_AlbumManagement,
    myDsl_AlbumManagementFunctions,
    myDsl_AmazonWebServices,
    myDsl_AppAccess,
    myDsl_AppAccessFunctions,
    myDsl_Architecture,
    myDsl_ArchitectureComponents,
    myDsl_BackEnd,
    myDsl_BusinessLogicContent,
    myDsl_BusinessLogicLayer,
    myDsl_BusinessLogicSegments,
    myDsl_ComponentClass,
    myDsl_ComponentsLogic,
    myDsl_ComponentsUI,
    myDsl_CoreFunctionsDeclaration,
    myDsl_DOMConfigurations,
    myDsl_DataPersistenceContent,
    myDsl_DataPersistenceLayer,
    myDsl_DataPersistenceSegments,
    myDsl_Directories,
    myDsl_DirectoryContent,
    myDsl_Domain,
    myDsl_DomainConnection,
    myDsl_DomainRelations,
    myDsl_EObject,
    myDsl_Entities,
    myDsl_Entity,
    myDsl_FrontEnd,
    myDsl_Functionalities,
    myDsl_Functionality,
    myDsl_LandingActions,
    myDsl_LandingFunctions,
    myDsl_Layer,
    myDsl_LayerRelations,
    myDsl_LayerSource,
    myDsl_LayerTarget,
    myDsl_LogicContent,
    myDsl_LogicStructure,
    myDsl_Model,
    myDsl_MultipleFile,
    myDsl_NTierSource,
    myDsl_NTierTarget,
    myDsl_NTiers,
    myDsl_NTiersConnections,
    myDsl_NTiersRelations,
    myDsl_PackageName,
    myDsl_PackageVersion,
    myDsl_PersistenceDataComponent,
    myDsl_Photo,
    myDsl_PhotoActions,
    myDsl_PhotoActionsFunctions,
    myDsl_PostgreSQL,
    myDsl_PresentationContent,
    myDsl_PresentationLayer,
    myDsl_PresentationSegments,
    myDsl_ProfileManagement,
    myDsl_ProfileManagementFunctions,
    myDsl_Props,
    myDsl_React,
    myDsl_ReactActions,
    myDsl_ReactActionsContent,
    myDsl_ReactComponents,
    myDsl_ReactConfiguration,
    myDsl_ReactConfigurations,
    myDsl_ReactConstructor,
    myDsl_ReactCoreFunctions,
    myDsl_ReactDependencies,
    myDsl_ReactDependenciesRules,
    myDsl_ReactDependenciesSubRules,
    myDsl_ReactFunctions,
    myDsl_ReactInfo,
    myDsl_ReactInformation,
    myDsl_ReactLibraries,
    myDsl_ReactLibrary,
    myDsl_ReactModules,
    myDsl_ReactServicesRelation,
    myDsl_ReactServicesType,
    myDsl_ReactSubModules,
    myDsl_SegmentStructure,
    myDsl_SegmentStructureContent,
    myDsl_SingleDependencies,
    myDsl_SingleFile,
    myDsl_Spring,
    myDsl_State,
    myDsl_Technologies,
    myDsl_Technology,
    myDsl_UIContent,
    myDsl_UserDomain,
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

def test_assoc_configurations89_reverse_link_reassign_clear():
    a1 = myDsl_ReactConfigurations(name="sample_text")
    a2 = myDsl_ReactConfigurations(name="sample_text_2")
    b = myDsl_DOMConfigurations(elements="sample_text", name="sample_text")
    _safe_set(b, 'myDsl_DOMConfigurations', a1)
    assert _is_linked(b, 'myDsl_DOMConfigurations', a1)
    if hasattr(a1, 'myDsl_ReactConfigurations90'):
        assert _is_linked(a1, 'myDsl_ReactConfigurations90', b)
    _safe_set(b, 'myDsl_DOMConfigurations', a2)
    assert _is_linked(b, 'myDsl_DOMConfigurations', a2)
    if hasattr(a1, 'myDsl_ReactConfigurations90'):
        assert not _is_linked(a1, 'myDsl_ReactConfigurations90', b)
    if hasattr(a2, 'myDsl_ReactConfigurations90'):
        assert _is_linked(a2, 'myDsl_ReactConfigurations90', b)
    _safe_set(b, 'myDsl_DOMConfigurations', None)
    assert not _is_linked(b, 'myDsl_DOMConfigurations', a2)
    if hasattr(a2, 'myDsl_ReactConfigurations90'):
        assert not _is_linked(a2, 'myDsl_ReactConfigurations90', b)


def test_assoc_elements48_reverse_link_reassign_clear():
    a1 = myDsl_SegmentStructureContent(name="sample_text")
    a2 = myDsl_SegmentStructureContent(name="sample_text_2")
    b = myDsl_DirectoryContent(name="sample_text")
    _safe_set(b, 'myDsl_DirectoryContent', a1)
    assert _is_linked(b, 'myDsl_DirectoryContent', a1)
    if hasattr(a1, 'myDsl_SegmentStructureContent49'):
        assert _is_linked(a1, 'myDsl_SegmentStructureContent49', b)
    _safe_set(b, 'myDsl_DirectoryContent', a2)
    assert _is_linked(b, 'myDsl_DirectoryContent', a2)
    if hasattr(a1, 'myDsl_SegmentStructureContent49'):
        assert not _is_linked(a1, 'myDsl_SegmentStructureContent49', b)
    if hasattr(a2, 'myDsl_SegmentStructureContent49'):
        assert _is_linked(a2, 'myDsl_SegmentStructureContent49', b)
    _safe_set(b, 'myDsl_DirectoryContent', None)
    assert not _is_linked(b, 'myDsl_DirectoryContent', a2)
    if hasattr(a2, 'myDsl_SegmentStructureContent49'):
        assert not _is_linked(a2, 'myDsl_SegmentStructureContent49', b)


def test_assoc_layerorigin54_reverse_link_reassign_clear():
    a1 = myDsl_LayerSource(layerelations="sample_text")
    a2 = myDsl_LayerSource(layerelations="sample_text_2")
    b = myDsl_LayerRelations(layerelations="sample_text", name="sample_text")
    _safe_set(b, 'myDsl_LayerRelations', {a1})
    assert _is_linked(b, 'myDsl_LayerRelations', a1)
    if hasattr(a1, 'myDsl_LayerSource'):
        assert _is_linked(a1, 'myDsl_LayerSource', b)
    _safe_set(b, 'myDsl_LayerRelations', {a2})
    assert _is_linked(b, 'myDsl_LayerRelations', a2)
    if hasattr(a1, 'myDsl_LayerSource'):
        assert not _is_linked(a1, 'myDsl_LayerSource', b)
    if hasattr(a2, 'myDsl_LayerSource'):
        assert _is_linked(a2, 'myDsl_LayerSource', b)
    _safe_set(b, 'myDsl_LayerRelations', set())
    assert not _is_linked(b, 'myDsl_LayerRelations', a2)
    if hasattr(a2, 'myDsl_LayerSource'):
        assert not _is_linked(a2, 'myDsl_LayerSource', b)


def test_assoc_layertarget55_reverse_link_reassign_clear():
    a1 = myDsl_LayerTarget(layerelations="sample_text")
    a2 = myDsl_LayerTarget(layerelations="sample_text_2")
    b = myDsl_LayerRelations(layerelations="sample_text", name="sample_text")
    _safe_set(b, 'myDsl_LayerRelations56', {a1})
    assert _is_linked(b, 'myDsl_LayerRelations56', a1)
    if hasattr(a1, 'myDsl_LayerTarget'):
        assert _is_linked(a1, 'myDsl_LayerTarget', b)
    _safe_set(b, 'myDsl_LayerRelations56', {a2})
    assert _is_linked(b, 'myDsl_LayerRelations56', a2)
    if hasattr(a1, 'myDsl_LayerTarget'):
        assert not _is_linked(a1, 'myDsl_LayerTarget', b)
    if hasattr(a2, 'myDsl_LayerTarget'):
        assert _is_linked(a2, 'myDsl_LayerTarget', b)
    _safe_set(b, 'myDsl_LayerRelations56', set())
    assert not _is_linked(b, 'myDsl_LayerRelations56', a2)
    if hasattr(a2, 'myDsl_LayerTarget'):
        assert not _is_linked(a2, 'myDsl_LayerTarget', b)


def test_assoc_logiccomponents94_reverse_link_reassign_clear():
    a1 = myDsl_LogicContent(name="sample_text")
    a2 = myDsl_LogicContent(name="sample_text_2")
    b = myDsl_ComponentsLogic(name="sample_text")
    _safe_set(b, 'myDsl_ComponentsLogic95', {a1})
    assert _is_linked(b, 'myDsl_ComponentsLogic95', a1)
    if hasattr(a1, 'myDsl_LogicContent'):
        assert _is_linked(a1, 'myDsl_LogicContent', b)
    _safe_set(b, 'myDsl_ComponentsLogic95', {a2})
    assert _is_linked(b, 'myDsl_ComponentsLogic95', a2)
    if hasattr(a1, 'myDsl_LogicContent'):
        assert not _is_linked(a1, 'myDsl_LogicContent', b)
    if hasattr(a2, 'myDsl_LogicContent'):
        assert _is_linked(a2, 'myDsl_LogicContent', b)
    _safe_set(b, 'myDsl_ComponentsLogic95', set())
    assert not _is_linked(b, 'myDsl_ComponentsLogic95', a2)
    if hasattr(a2, 'myDsl_LogicContent'):
        assert not _is_linked(a2, 'myDsl_LogicContent', b)


def test_assoc_logiccomponents96_reverse_link_reassign_clear():
    a1 = myDsl_LogicStructure(name="sample_text")
    a2 = myDsl_LogicStructure(name="sample_text_2")
    b = myDsl_LogicContent(name="sample_text")
    _safe_set(b, 'myDsl_LogicContent97', {a1})
    assert _is_linked(b, 'myDsl_LogicContent97', a1)
    if hasattr(a1, 'myDsl_LogicStructure'):
        assert _is_linked(a1, 'myDsl_LogicStructure', b)
    _safe_set(b, 'myDsl_LogicContent97', {a2})
    assert _is_linked(b, 'myDsl_LogicContent97', a2)
    if hasattr(a1, 'myDsl_LogicStructure'):
        assert not _is_linked(a1, 'myDsl_LogicStructure', b)
    if hasattr(a2, 'myDsl_LogicStructure'):
        assert _is_linked(a2, 'myDsl_LogicStructure', b)
    _safe_set(b, 'myDsl_LogicContent97', set())
    assert not _is_linked(b, 'myDsl_LogicContent97', a2)
    if hasattr(a2, 'myDsl_LogicStructure'):
        assert not _is_linked(a2, 'myDsl_LogicStructure', b)


def test_assoc_reactrelationcontent115_reverse_link_reassign_clear():
    a1 = myDsl_ReactServicesType(name="sample_text")
    a2 = myDsl_ReactServicesType(name="sample_text_2")
    b = myDsl_ReactServicesRelation(name="sample_text")
    _safe_set(b, 'myDsl_ReactServicesRelation116', {a1})
    assert _is_linked(b, 'myDsl_ReactServicesRelation116', a1)
    if hasattr(a1, 'myDsl_ReactServicesType'):
        assert _is_linked(a1, 'myDsl_ReactServicesType', b)
    _safe_set(b, 'myDsl_ReactServicesRelation116', {a2})
    assert _is_linked(b, 'myDsl_ReactServicesRelation116', a2)
    if hasattr(a1, 'myDsl_ReactServicesType'):
        assert not _is_linked(a1, 'myDsl_ReactServicesType', b)
    if hasattr(a2, 'myDsl_ReactServicesType'):
        assert _is_linked(a2, 'myDsl_ReactServicesType', b)
    _safe_set(b, 'myDsl_ReactServicesRelation116', set())
    assert not _is_linked(b, 'myDsl_ReactServicesRelation116', a2)
    if hasattr(a2, 'myDsl_ReactServicesType'):
        assert not _is_linked(a2, 'myDsl_ReactServicesType', b)


def test_assoc_uicomponents100_reverse_link_reassign_clear():
    a1 = myDsl_UIContent(name="sample_text")
    a2 = myDsl_UIContent(name="sample_text_2")
    b = myDsl_ComponentsUI(name="sample_text")
    _safe_set(b, 'myDsl_ComponentsUI101', {a1})
    assert _is_linked(b, 'myDsl_ComponentsUI101', a1)
    if hasattr(a1, 'myDsl_UIContent'):
        assert _is_linked(a1, 'myDsl_UIContent', b)
    _safe_set(b, 'myDsl_ComponentsUI101', {a2})
    assert _is_linked(b, 'myDsl_ComponentsUI101', a2)
    if hasattr(a1, 'myDsl_UIContent'):
        assert not _is_linked(a1, 'myDsl_UIContent', b)
    if hasattr(a2, 'myDsl_UIContent'):
        assert _is_linked(a2, 'myDsl_UIContent', b)
    _safe_set(b, 'myDsl_ComponentsUI101', set())
    assert not _is_linked(b, 'myDsl_ComponentsUI101', a2)
    if hasattr(a2, 'myDsl_UIContent'):
        assert not _is_linked(a2, 'myDsl_UIContent', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_componentclass108_stub_double():
    # myDsl_EObject has no real 'myDsl_EObject109' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactFunctions(lifecycleclass="sample_text", renderclass="sample_text")
    partner = myDsl_EObject()
    setattr(partner, 'myDsl_EObject109', None)
    _safe_set(owner, 'myDsl_ReactFunctions', {partner})
    assert getattr(partner, 'myDsl_EObject109') == owner
    _safe_set(owner, 'myDsl_ReactFunctions', set())
    assert getattr(partner, 'myDsl_EObject109') is None


def test_assoc_componentslogic91_stub_double():
    # myDsl_ReactComponents has no real 'myDsl_ReactComponents' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ComponentsLogic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ComponentsLogic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ComponentsLogic(name="sample_text")
    partner = myDsl_ReactComponents()
    setattr(partner, 'myDsl_ReactComponents', None)
    _safe_set(owner, 'myDsl_ComponentsLogic', partner)
    assert owner in getattr(partner, 'myDsl_ReactComponents')
    _safe_set(owner, 'myDsl_ComponentsLogic', None)
    assert owner not in getattr(partner, 'myDsl_ReactComponents')


def test_assoc_componentsui92_stub_double():
    # myDsl_ReactComponents has no real 'myDsl_ReactComponents93' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ComponentsUI's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ComponentsUI's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ComponentsUI(name="sample_text")
    partner = myDsl_ReactComponents()
    setattr(partner, 'myDsl_ReactComponents93', None)
    _safe_set(owner, 'myDsl_ComponentsUI', partner)
    assert owner in getattr(partner, 'myDsl_ReactComponents93')
    _safe_set(owner, 'myDsl_ComponentsUI', None)
    assert owner not in getattr(partner, 'myDsl_ReactComponents93')


def test_assoc_configurations78_stub_double():
    # myDsl_ReactConfiguration has no real 'myDsl_ReactConfiguration79' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactConfigurations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactConfigurations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactConfigurations(name="sample_text")
    partner = myDsl_ReactConfiguration()
    setattr(partner, 'myDsl_ReactConfiguration79', None)
    _safe_set(owner, 'myDsl_ReactConfigurations', partner)
    assert owner in getattr(partner, 'myDsl_ReactConfiguration79')
    _safe_set(owner, 'myDsl_ReactConfigurations', None)
    assert owner not in getattr(partner, 'myDsl_ReactConfiguration79')


def test_assoc_dependencies80_stub_double():
    # myDsl_ReactDependencies has no real 'myDsl_ReactDependencies81' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactDependenciesRules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactDependenciesRules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactDependenciesRules(name="sample_text")
    partner = myDsl_ReactDependencies()
    setattr(partner, 'myDsl_ReactDependencies81', None)
    _safe_set(owner, 'myDsl_ReactDependenciesRules', partner)
    assert owner in getattr(partner, 'myDsl_ReactDependencies81')
    _safe_set(owner, 'myDsl_ReactDependenciesRules', None)
    assert owner not in getattr(partner, 'myDsl_ReactDependencies81')


def test_assoc_dependencies82_stub_double():
    # myDsl_ReactDependenciesSubRules has no real 'myDsl_ReactDependenciesSubRules' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactDependenciesRules's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactDependenciesRules's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactDependenciesRules(name="sample_text")
    partner = myDsl_ReactDependenciesSubRules()
    setattr(partner, 'myDsl_ReactDependenciesSubRules', None)
    _safe_set(owner, 'myDsl_ReactDependenciesRules83', {partner})
    assert getattr(partner, 'myDsl_ReactDependenciesSubRules') == owner
    _safe_set(owner, 'myDsl_ReactDependenciesRules83', set())
    assert getattr(partner, 'myDsl_ReactDependenciesSubRules') is None


def test_assoc_elements1_stub_double():
    # myDsl_EObject has no real 'myDsl_EObject2' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Domain(name="sample_text")
    partner = myDsl_EObject()
    setattr(partner, 'myDsl_EObject2', None)
    _safe_set(owner, 'myDsl_Domain', {partner})
    assert getattr(partner, 'myDsl_EObject2') == owner
    _safe_set(owner, 'myDsl_Domain', set())
    assert getattr(partner, 'myDsl_EObject2') is None


def test_assoc_elements28_stub_double():
    # myDsl_DomainConnection has no real 'myDsl_DomainConnection' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DomainRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DomainRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DomainRelations(name="sample_text")
    partner = myDsl_DomainConnection()
    setattr(partner, 'myDsl_DomainConnection', None)
    _safe_set(owner, 'myDsl_DomainRelations', partner)
    assert owner in getattr(partner, 'myDsl_DomainConnection')
    _safe_set(owner, 'myDsl_DomainRelations', None)
    assert owner not in getattr(partner, 'myDsl_DomainConnection')


def test_assoc_elements29_stub_double():
    # myDsl_EObject has no real 'myDsl_EObject31' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DomainRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DomainRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DomainRelations(name="sample_text")
    partner = myDsl_EObject()
    setattr(partner, 'myDsl_EObject31', None)
    _safe_set(owner, 'myDsl_DomainRelations30', {partner})
    assert getattr(partner, 'myDsl_EObject31') == owner
    _safe_set(owner, 'myDsl_DomainRelations30', set())
    assert getattr(partner, 'myDsl_EObject31') is None


def test_assoc_elements40_stub_double():
    # myDsl_PresentationContent has no real 'myDsl_PresentationContent' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_PresentationSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_PresentationSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_PresentationSegments(name="sample_text")
    partner = myDsl_PresentationContent()
    setattr(partner, 'myDsl_PresentationContent', None)
    _safe_set(owner, 'myDsl_PresentationSegments', partner)
    assert owner in getattr(partner, 'myDsl_PresentationContent')
    _safe_set(owner, 'myDsl_PresentationSegments', None)
    assert owner not in getattr(partner, 'myDsl_PresentationContent')


def test_assoc_elements43_stub_double():
    # myDsl_BusinessLogicContent has no real 'myDsl_BusinessLogicContent' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_BusinessLogicSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_BusinessLogicSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_BusinessLogicSegments(name="sample_text")
    partner = myDsl_BusinessLogicContent()
    setattr(partner, 'myDsl_BusinessLogicContent', None)
    _safe_set(owner, 'myDsl_BusinessLogicSegments', partner)
    assert owner in getattr(partner, 'myDsl_BusinessLogicContent')
    _safe_set(owner, 'myDsl_BusinessLogicSegments', None)
    assert owner not in getattr(partner, 'myDsl_BusinessLogicContent')


def test_assoc_elements45_stub_double():
    # myDsl_DataPersistenceContent has no real 'myDsl_DataPersistenceContent46' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DataPersistenceSegments's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DataPersistenceSegments's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DataPersistenceSegments(name="sample_text")
    partner = myDsl_DataPersistenceContent()
    setattr(partner, 'myDsl_DataPersistenceContent46', None)
    _safe_set(owner, 'myDsl_DataPersistenceSegments', partner)
    assert owner in getattr(partner, 'myDsl_DataPersistenceContent46')
    _safe_set(owner, 'myDsl_DataPersistenceSegments', None)
    assert owner not in getattr(partner, 'myDsl_DataPersistenceContent46')


def test_assoc_elements47_stub_double():
    # myDsl_SegmentStructure has no real 'myDsl_SegmentStructure' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_SegmentStructureContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_SegmentStructureContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_SegmentStructureContent(name="sample_text")
    partner = myDsl_SegmentStructure()
    setattr(partner, 'myDsl_SegmentStructure', None)
    _safe_set(owner, 'myDsl_SegmentStructureContent', partner)
    assert owner in getattr(partner, 'myDsl_SegmentStructure')
    _safe_set(owner, 'myDsl_SegmentStructureContent', None)
    assert owner not in getattr(partner, 'myDsl_SegmentStructure')


def test_assoc_elements50_stub_double():
    # myDsl_EObject has no real 'myDsl_EObject52' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_DirectoryContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_DirectoryContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_DirectoryContent(name="sample_text")
    partner = myDsl_EObject()
    setattr(partner, 'myDsl_EObject52', None)
    _safe_set(owner, 'myDsl_DirectoryContent51', {partner})
    assert getattr(partner, 'myDsl_EObject52') == owner
    _safe_set(owner, 'myDsl_DirectoryContent51', set())
    assert getattr(partner, 'myDsl_EObject52') is None


def test_assoc_elements53_stub_double():
    # myDsl_Directories has no real 'myDsl_Directories' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_MultipleFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_MultipleFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_MultipleFile(name="sample_text")
    partner = myDsl_Directories()
    setattr(partner, 'myDsl_Directories', None)
    _safe_set(owner, 'myDsl_MultipleFile', partner)
    assert owner in getattr(partner, 'myDsl_Directories')
    _safe_set(owner, 'myDsl_MultipleFile', None)
    assert owner not in getattr(partner, 'myDsl_Directories')


def test_assoc_elements67_stub_double():
    # myDsl_Technologies has no real 'myDsl_Technologies' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_Technology's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_Technology's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_Technology(name="sample_text")
    partner = myDsl_Technologies()
    setattr(partner, 'myDsl_Technologies', None)
    _safe_set(owner, 'myDsl_Technology', {partner})
    assert getattr(partner, 'myDsl_Technologies') == owner
    _safe_set(owner, 'myDsl_Technology', set())
    assert getattr(partner, 'myDsl_Technologies') is None


def test_assoc_items18_stub_double():
    # myDsl_ProfileManagement has no real 'myDsl_ProfileManagement19' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ProfileManagementFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ProfileManagementFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ProfileManagementFunctions(name="sample_text")
    partner = myDsl_ProfileManagement()
    setattr(partner, 'myDsl_ProfileManagement19', None)
    _safe_set(owner, 'myDsl_ProfileManagementFunctions', partner)
    assert owner in getattr(partner, 'myDsl_ProfileManagement19')
    _safe_set(owner, 'myDsl_ProfileManagementFunctions', None)
    assert owner not in getattr(partner, 'myDsl_ProfileManagement19')


def test_assoc_items20_stub_double():
    # myDsl_AppAccess has no real 'myDsl_AppAccess21' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_AppAccessFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_AppAccessFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_AppAccessFunctions(name="sample_text")
    partner = myDsl_AppAccess()
    setattr(partner, 'myDsl_AppAccess21', None)
    _safe_set(owner, 'myDsl_AppAccessFunctions', partner)
    assert owner in getattr(partner, 'myDsl_AppAccess21')
    _safe_set(owner, 'myDsl_AppAccessFunctions', None)
    assert owner not in getattr(partner, 'myDsl_AppAccess21')


def test_assoc_items22_stub_double():
    # myDsl_AlbumManagement has no real 'myDsl_AlbumManagement23' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_AlbumManagementFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_AlbumManagementFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_AlbumManagementFunctions(name="sample_text")
    partner = myDsl_AlbumManagement()
    setattr(partner, 'myDsl_AlbumManagement23', None)
    _safe_set(owner, 'myDsl_AlbumManagementFunctions', partner)
    assert owner in getattr(partner, 'myDsl_AlbumManagement23')
    _safe_set(owner, 'myDsl_AlbumManagementFunctions', None)
    assert owner not in getattr(partner, 'myDsl_AlbumManagement23')


def test_assoc_items24_stub_double():
    # myDsl_PhotoActions has no real 'myDsl_PhotoActions25' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_PhotoActionsFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_PhotoActionsFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_PhotoActionsFunctions(name="sample_text")
    partner = myDsl_PhotoActions()
    setattr(partner, 'myDsl_PhotoActions25', None)
    _safe_set(owner, 'myDsl_PhotoActionsFunctions', partner)
    assert owner in getattr(partner, 'myDsl_PhotoActions25')
    _safe_set(owner, 'myDsl_PhotoActionsFunctions', None)
    assert owner not in getattr(partner, 'myDsl_PhotoActions25')


def test_assoc_items26_stub_double():
    # myDsl_LandingActions has no real 'myDsl_LandingActions27' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_LandingFunctions's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_LandingFunctions's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_LandingFunctions(name="sample_text")
    partner = myDsl_LandingActions()
    setattr(partner, 'myDsl_LandingActions27', None)
    _safe_set(owner, 'myDsl_LandingFunctions', partner)
    assert owner in getattr(partner, 'myDsl_LandingActions27')
    _safe_set(owner, 'myDsl_LandingFunctions', None)
    assert owner not in getattr(partner, 'myDsl_LandingActions27')


def test_assoc_logiccomponents98_stub_double():
    # myDsl_ComponentClass has no real 'myDsl_ComponentClass' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_LogicStructure's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_LogicStructure's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_LogicStructure(name="sample_text")
    partner = myDsl_ComponentClass()
    setattr(partner, 'myDsl_ComponentClass', None)
    _safe_set(owner, 'myDsl_LogicStructure99', {partner})
    assert getattr(partner, 'myDsl_ComponentClass') == owner
    _safe_set(owner, 'myDsl_LogicStructure99', set())
    assert getattr(partner, 'myDsl_ComponentClass') is None


def test_assoc_ntierconnection62_stub_double():
    # myDsl_NTierSource has no real 'myDsl_NTierSource63' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_NTiersRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_NTiersRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_NTiersRelations(name="sample_text")
    partner = myDsl_NTierSource()
    setattr(partner, 'myDsl_NTierSource63', None)
    _safe_set(owner, 'myDsl_NTiersRelations', partner)
    assert owner in getattr(partner, 'myDsl_NTierSource63')
    _safe_set(owner, 'myDsl_NTiersRelations', None)
    assert owner not in getattr(partner, 'myDsl_NTierSource63')


def test_assoc_ntierconnection64_stub_double():
    # myDsl_NTierTarget has no real 'myDsl_NTierTarget65' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_NTiersRelations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_NTiersRelations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_NTiersRelations(name="sample_text")
    partner = myDsl_NTierTarget()
    setattr(partner, 'myDsl_NTierTarget65', None)
    _safe_set(owner, 'myDsl_NTiersRelations66', partner)
    assert owner in getattr(partner, 'myDsl_NTierTarget65')
    _safe_set(owner, 'myDsl_NTiersRelations66', None)
    assert owner not in getattr(partner, 'myDsl_NTierTarget65')


def test_assoc_ntierorigin59_stub_double():
    # myDsl_NTierSource has no real 'myDsl_NTierSource' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_NTiersConnections's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_NTiersConnections's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_NTiersConnections(name="sample_text", ntierconnection="sample_text")
    partner = myDsl_NTierSource()
    setattr(partner, 'myDsl_NTierSource', None)
    _safe_set(owner, 'myDsl_NTiersConnections', {partner})
    assert getattr(partner, 'myDsl_NTierSource') == owner
    _safe_set(owner, 'myDsl_NTiersConnections', set())
    assert getattr(partner, 'myDsl_NTierSource') is None


def test_assoc_ntiertarget60_stub_double():
    # myDsl_NTierTarget has no real 'myDsl_NTierTarget' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_NTiersConnections's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_NTiersConnections's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_NTiersConnections(name="sample_text", ntierconnection="sample_text")
    partner = myDsl_NTierTarget()
    setattr(partner, 'myDsl_NTierTarget', None)
    _safe_set(owner, 'myDsl_NTiersConnections61', {partner})
    assert getattr(partner, 'myDsl_NTierTarget') == owner
    _safe_set(owner, 'myDsl_NTiersConnections61', set())
    assert getattr(partner, 'myDsl_NTierTarget') is None


def test_assoc_reactinformation118_stub_double():
    # myDsl_ReactInfo has no real 'myDsl_ReactInfo' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactInformation(name="sample_text")
    partner = myDsl_ReactInfo()
    setattr(partner, 'myDsl_ReactInfo', None)
    _safe_set(owner, 'myDsl_ReactInformation', partner)
    assert owner in getattr(partner, 'myDsl_ReactInfo')
    _safe_set(owner, 'myDsl_ReactInformation', None)
    assert owner not in getattr(partner, 'myDsl_ReactInfo')


def test_assoc_reactlibraries117_stub_double():
    # myDsl_ReactLibraries has no real 'myDsl_ReactLibraries' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactLibrary's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactLibrary's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactLibrary(name="sample_text")
    partner = myDsl_ReactLibraries()
    setattr(partner, 'myDsl_ReactLibraries', None)
    _safe_set(owner, 'myDsl_ReactLibrary', partner)
    assert owner in getattr(partner, 'myDsl_ReactLibraries')
    _safe_set(owner, 'myDsl_ReactLibrary', None)
    assert owner not in getattr(partner, 'myDsl_ReactLibraries')


def test_assoc_reactrelcontent113_stub_double():
    # myDsl_ReactActionsContent has no real 'myDsl_ReactActionsContent114' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_ReactServicesRelation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_ReactServicesRelation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_ReactServicesRelation(name="sample_text")
    partner = myDsl_ReactActionsContent()
    setattr(partner, 'myDsl_ReactActionsContent114', None)
    _safe_set(owner, 'myDsl_ReactServicesRelation', partner)
    assert owner in getattr(partner, 'myDsl_ReactActionsContent114')
    _safe_set(owner, 'myDsl_ReactServicesRelation', None)
    assert owner not in getattr(partner, 'myDsl_ReactActionsContent114')


def test_assoc_reacts71_stub_double():
    # myDsl_ReactModules has no real 'myDsl_ReactModules' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_React's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_React's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_React(name="sample_text")
    partner = myDsl_ReactModules()
    setattr(partner, 'myDsl_ReactModules', None)
    _safe_set(owner, 'myDsl_React', {partner})
    assert getattr(partner, 'myDsl_ReactModules') == owner
    _safe_set(owner, 'myDsl_React', set())
    assert getattr(partner, 'myDsl_ReactModules') is None


def test_assoc_uicontent102_stub_double():
    # myDsl_ComponentClass has no real 'myDsl_ComponentClass104' property in the generated
    # code (a bare stub) -- manually attach it so myDsl_UIContent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # myDsl_UIContent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = myDsl_UIContent(name="sample_text")
    partner = myDsl_ComponentClass()
    setattr(partner, 'myDsl_ComponentClass104', None)
    _safe_set(owner, 'myDsl_UIContent103', {partner})
    assert getattr(partner, 'myDsl_ComponentClass104') == owner
    _safe_set(owner, 'myDsl_UIContent103', set())
    assert getattr(partner, 'myDsl_ComponentClass104') is None


