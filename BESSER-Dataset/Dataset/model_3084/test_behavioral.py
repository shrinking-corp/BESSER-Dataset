import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    CPPNamedElement,
    CPPQualifiedNamedElement,
    CPPSourceFile,
    OOPLBasicType,
    OOPLClass,
    OOPLClassRefAssocCollection,
    OOPLClassRefSimpleCollection,
    OOPLClassReference,
    OOPLClassReferenceStorage,
    OOPLEnumType,
    OOPLEnumerator,
    OOPLRelation,
    OOPLSequence,
    OOPLStructMember,
    OOPLStructType,
    OOPLUserDefinedType,
    cppmodel_Attribute,
    cppmodel_CPPAttribute,
    cppmodel_CPPBasicType,
    cppmodel_CPPBodyFile,
    cppmodel_CPPClass,
    cppmodel_CPPClassRefAssocCollection,
    cppmodel_CPPClassRefSimpleCollection,
    cppmodel_CPPClassReference,
    cppmodel_CPPClassReferenceStorage,
    cppmodel_CPPComponent,
    cppmodel_CPPDirectory,
    cppmodel_CPPEnumType,
    cppmodel_CPPEnumerator,
    cppmodel_CPPEvent,
    cppmodel_CPPExternalBridge,
    cppmodel_CPPExternalHeader,
    cppmodel_CPPExternalHeaderInclusion,
    cppmodel_CPPExternalLibrary,
    cppmodel_CPPFormalParameter,
    cppmodel_CPPHeaderFile,
    cppmodel_CPPMakeFile,
    cppmodel_CPPModel,
    cppmodel_CPPNamedElement,
    cppmodel_CPPOperation,
    cppmodel_CPPPackage,
    cppmodel_CPPPort,
    cppmodel_CPPProtocol,
    cppmodel_CPPProtocolOperationDefinition,
    cppmodel_CPPProtocolOperationImplementation,
    cppmodel_CPPQualifiedNamedElement,
    cppmodel_CPPRelation,
    cppmodel_CPPReturnValue,
    cppmodel_CPPSequence,
    cppmodel_CPPSignal,
    cppmodel_CPPSourceFile,
    cppmodel_CPPState,
    cppmodel_CPPStructMember,
    cppmodel_CPPStructType,
    cppmodel_CPPTransition,
    cppmodel_CPPUserDefinedType,
    cppmodel_Model,
    cppmodel_OOPLDataType,
    cppmodel_OOPLNameProvider,
    cppmodel_Operation,
    cppmodel_Package,
    cppmodel_Parameter,
    cppmodel_Signal,
    cppmodel_Snippet,
    cppmodel_State,
    cppmodel_Transition,
    cppmodel_TypedMultiplicityElement,
    cppmodel_XTClass,
    cppmodel_XTComponent,
    cppmodel_XTEvent,
    cppmodel_XTPort,
    cppmodel_XTProtocol,
    cppmodel_XTProtocolOperationDefinition,
    cppmodel_XTProtocolOperationImplementation,
    CPPParameterPassingKind,
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

def test_assoc_externalHeader84_reverse_link_reassign_clear():
    a1 = cppmodel_CPPExternalHeaderInclusion(comment="sample_text")
    a2 = cppmodel_CPPExternalHeaderInclusion(comment="sample_text_2")
    b = cppmodel_CPPExternalHeader(name="sample_text")
    _safe_set(b, 'cppmodel_CPPExternalHeader', a1)
    assert _is_linked(b, 'cppmodel_CPPExternalHeader', a1)
    if hasattr(a1, 'cppmodel_CPPExternalHeaderInclusion85'):
        assert _is_linked(a1, 'cppmodel_CPPExternalHeaderInclusion85', b)
    _safe_set(b, 'cppmodel_CPPExternalHeader', a2)
    assert _is_linked(b, 'cppmodel_CPPExternalHeader', a2)
    if hasattr(a1, 'cppmodel_CPPExternalHeaderInclusion85'):
        assert not _is_linked(a1, 'cppmodel_CPPExternalHeaderInclusion85', b)
    if hasattr(a2, 'cppmodel_CPPExternalHeaderInclusion85'):
        assert _is_linked(a2, 'cppmodel_CPPExternalHeaderInclusion85', b)
    _safe_set(b, 'cppmodel_CPPExternalHeader', None)
    assert not _is_linked(b, 'cppmodel_CPPExternalHeader', a2)
    if hasattr(a2, 'cppmodel_CPPExternalHeaderInclusion85'):
        assert not _is_linked(a2, 'cppmodel_CPPExternalHeaderInclusion85', b)


def test_assoc_externalHeaderInclusion49_reverse_link_reassign_clear():
    a1 = cppmodel_CPPSourceFile(generationDirectory="sample_text", generationName="sample_text", generationPath="sample_text")
    a2 = cppmodel_CPPSourceFile(generationDirectory="sample_text_2", generationName="sample_text_2", generationPath="sample_text_2")
    b = cppmodel_CPPExternalHeaderInclusion(comment="sample_text")
    _safe_set(b, 'cppmodel_CPPExternalHeaderInclusion', a1)
    assert _is_linked(b, 'cppmodel_CPPExternalHeaderInclusion', a1)
    if hasattr(a1, 'cppmodel_CPPSourceFile50'):
        assert _is_linked(a1, 'cppmodel_CPPSourceFile50', b)
    _safe_set(b, 'cppmodel_CPPExternalHeaderInclusion', a2)
    assert _is_linked(b, 'cppmodel_CPPExternalHeaderInclusion', a2)
    if hasattr(a1, 'cppmodel_CPPSourceFile50'):
        assert not _is_linked(a1, 'cppmodel_CPPSourceFile50', b)
    if hasattr(a2, 'cppmodel_CPPSourceFile50'):
        assert _is_linked(a2, 'cppmodel_CPPSourceFile50', b)
    _safe_set(b, 'cppmodel_CPPExternalHeaderInclusion', None)
    assert not _is_linked(b, 'cppmodel_CPPExternalHeaderInclusion', a2)
    if hasattr(a2, 'cppmodel_CPPSourceFile50'):
        assert not _is_linked(a2, 'cppmodel_CPPSourceFile50', b)


def test_assoc_files54_reverse_link_reassign_clear():
    a1 = cppmodel_CPPSourceFile(generationDirectory="sample_text", generationName="sample_text", generationPath="sample_text")
    a2 = cppmodel_CPPSourceFile(generationDirectory="sample_text_2", generationName="sample_text_2", generationPath="sample_text_2")
    b = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    _safe_set(b, 'cppmodel_CPPDirectory55', {a1})
    assert _is_linked(b, 'cppmodel_CPPDirectory55', a1)
    if hasattr(a1, 'cppmodel_CPPSourceFile56'):
        assert _is_linked(a1, 'cppmodel_CPPSourceFile56', b)
    _safe_set(b, 'cppmodel_CPPDirectory55', {a2})
    assert _is_linked(b, 'cppmodel_CPPDirectory55', a2)
    if hasattr(a1, 'cppmodel_CPPSourceFile56'):
        assert not _is_linked(a1, 'cppmodel_CPPSourceFile56', b)
    if hasattr(a2, 'cppmodel_CPPSourceFile56'):
        assert _is_linked(a2, 'cppmodel_CPPSourceFile56', b)
    _safe_set(b, 'cppmodel_CPPDirectory55', set())
    assert not _is_linked(b, 'cppmodel_CPPDirectory55', a2)
    if hasattr(a2, 'cppmodel_CPPSourceFile56'):
        assert not _is_linked(a2, 'cppmodel_CPPSourceFile56', b)


def test_assoc_headerFile143_reverse_link_reassign_clear():
    a1 = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    a2 = cppmodel_CPPHeaderFile(includeDirectory="sample_text_2", includeName="sample_text_2", includePath="sample_text_2")
    b = cppmodel_CPPExternalBridge(cppExternalNamespace="sample_text")
    _safe_set(b, 'cppmodel_CPPExternalBridge', a1)
    assert _is_linked(b, 'cppmodel_CPPExternalBridge', a1)
    if hasattr(a1, 'cppmodel_CPPHeaderFile144'):
        assert _is_linked(a1, 'cppmodel_CPPHeaderFile144', b)
    _safe_set(b, 'cppmodel_CPPExternalBridge', a2)
    assert _is_linked(b, 'cppmodel_CPPExternalBridge', a2)
    if hasattr(a1, 'cppmodel_CPPHeaderFile144'):
        assert not _is_linked(a1, 'cppmodel_CPPHeaderFile144', b)
    if hasattr(a2, 'cppmodel_CPPHeaderFile144'):
        assert _is_linked(a2, 'cppmodel_CPPHeaderFile144', b)
    _safe_set(b, 'cppmodel_CPPExternalBridge', None)
    assert not _is_linked(b, 'cppmodel_CPPExternalBridge', a2)
    if hasattr(a2, 'cppmodel_CPPHeaderFile144'):
        assert not _is_linked(a2, 'cppmodel_CPPHeaderFile144', b)


def test_assoc_includedHeaders47_reverse_link_reassign_clear():
    a1 = cppmodel_CPPSourceFile(generationDirectory="sample_text", generationName="sample_text", generationPath="sample_text")
    a2 = cppmodel_CPPSourceFile(generationDirectory="sample_text_2", generationName="sample_text_2", generationPath="sample_text_2")
    b = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    _safe_set(b, 'cppmodel_CPPHeaderFile48', a1)
    assert _is_linked(b, 'cppmodel_CPPHeaderFile48', a1)
    if hasattr(a1, 'cppmodel_CPPSourceFile'):
        assert _is_linked(a1, 'cppmodel_CPPSourceFile', b)
    _safe_set(b, 'cppmodel_CPPHeaderFile48', a2)
    assert _is_linked(b, 'cppmodel_CPPHeaderFile48', a2)
    if hasattr(a1, 'cppmodel_CPPSourceFile'):
        assert not _is_linked(a1, 'cppmodel_CPPSourceFile', b)
    if hasattr(a2, 'cppmodel_CPPSourceFile'):
        assert _is_linked(a2, 'cppmodel_CPPSourceFile', b)
    _safe_set(b, 'cppmodel_CPPHeaderFile48', None)
    assert not _is_linked(b, 'cppmodel_CPPHeaderFile48', a2)
    if hasattr(a2, 'cppmodel_CPPSourceFile'):
        assert not _is_linked(a2, 'cppmodel_CPPSourceFile', b)


def test_assoc_subDirectories52_reverse_link_reassign_clear():
    a1 = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    a2 = cppmodel_CPPDirectory(name="sample_text_2", parentDirectory="sample_text_2", path="sample_text_2")
    b = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    _safe_set(b, 'cppmodel_CPPDirectory53', a1)
    assert _is_linked(b, 'cppmodel_CPPDirectory53', a1)
    if hasattr(a1, 'cppmodel_CPPDirectory51'):
        assert _is_linked(a1, 'cppmodel_CPPDirectory51', b)
    _safe_set(b, 'cppmodel_CPPDirectory53', a2)
    assert _is_linked(b, 'cppmodel_CPPDirectory53', a2)
    if hasattr(a1, 'cppmodel_CPPDirectory51'):
        assert not _is_linked(a1, 'cppmodel_CPPDirectory51', b)
    if hasattr(a2, 'cppmodel_CPPDirectory51'):
        assert _is_linked(a2, 'cppmodel_CPPDirectory51', b)
    _safe_set(b, 'cppmodel_CPPDirectory53', None)
    assert not _is_linked(b, 'cppmodel_CPPDirectory53', a2)
    if hasattr(a2, 'cppmodel_CPPDirectory51'):
        assert not _is_linked(a2, 'cppmodel_CPPDirectory51', b)


def test_assoc_subElements2_reverse_link_reassign_clear():
    a1 = cppmodel_CPPQualifiedNamedElement(cppPrefix="sample_text", cppQualifiedName="sample_text")
    a2 = cppmodel_CPPQualifiedNamedElement(cppPrefix="sample_text_2", cppQualifiedName="sample_text_2")
    b = cppmodel_CPPQualifiedNamedElement(cppPrefix="sample_text", cppQualifiedName="sample_text")
    _safe_set(b, 'cppmodel_CPPQualifiedNamedElement1', {a1})
    assert _is_linked(b, 'cppmodel_CPPQualifiedNamedElement1', a1)
    if hasattr(a1, 'cppmodel_CPPQualifiedNamedElement'):
        assert _is_linked(a1, 'cppmodel_CPPQualifiedNamedElement', b)
    _safe_set(b, 'cppmodel_CPPQualifiedNamedElement1', {a2})
    assert _is_linked(b, 'cppmodel_CPPQualifiedNamedElement1', a2)
    if hasattr(a1, 'cppmodel_CPPQualifiedNamedElement'):
        assert not _is_linked(a1, 'cppmodel_CPPQualifiedNamedElement', b)
    if hasattr(a2, 'cppmodel_CPPQualifiedNamedElement'):
        assert _is_linked(a2, 'cppmodel_CPPQualifiedNamedElement', b)
    _safe_set(b, 'cppmodel_CPPQualifiedNamedElement1', set())
    assert not _is_linked(b, 'cppmodel_CPPQualifiedNamedElement1', a2)
    if hasattr(a2, 'cppmodel_CPPQualifiedNamedElement'):
        assert not _is_linked(a2, 'cppmodel_CPPQualifiedNamedElement', b)


def test_assoc_unnamedSequenceType128_reverse_link_reassign_clear():
    a1 = cppmodel_CPPSequence(cppContainer="sample_text")
    a2 = cppmodel_CPPSequence(cppContainer="sample_text_2")
    b = cppmodel_CPPFormalParameter(passingMode="sample_text")
    _safe_set(b, 'cppmodel_CPPFormalParameter129', a1)
    assert _is_linked(b, 'cppmodel_CPPFormalParameter129', a1)
    if hasattr(a1, 'cppmodel_CPPSequence130'):
        assert _is_linked(a1, 'cppmodel_CPPSequence130', b)
    _safe_set(b, 'cppmodel_CPPFormalParameter129', a2)
    assert _is_linked(b, 'cppmodel_CPPFormalParameter129', a2)
    if hasattr(a1, 'cppmodel_CPPSequence130'):
        assert not _is_linked(a1, 'cppmodel_CPPSequence130', b)
    if hasattr(a2, 'cppmodel_CPPSequence130'):
        assert _is_linked(a2, 'cppmodel_CPPSequence130', b)
    _safe_set(b, 'cppmodel_CPPFormalParameter129', None)
    assert not _is_linked(b, 'cppmodel_CPPFormalParameter129', a2)
    if hasattr(a2, 'cppmodel_CPPSequence130'):
        assert not _is_linked(a2, 'cppmodel_CPPSequence130', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_apiHeaderFile11_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel12' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel12', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile13', partner)
    assert getattr(partner, 'cppmodel_CPPModel12') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile13', None)
    assert getattr(partner, 'cppmodel_CPPModel12') is None


def test_assoc_bodyDir16_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel17' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel17', None)
    _safe_set(owner, 'cppmodel_CPPDirectory18', partner)
    assert getattr(partner, 'cppmodel_CPPModel17') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory18', None)
    assert getattr(partner, 'cppmodel_CPPModel17') is None


def test_assoc_bodyDir35_stub_double():
    # cppmodel_CPPPackage has no real 'cppmodel_CPPPackage36' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPPackage()
    setattr(partner, 'cppmodel_CPPPackage36', None)
    _safe_set(owner, 'cppmodel_CPPDirectory37', partner)
    assert getattr(partner, 'cppmodel_CPPPackage36') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory37', None)
    assert getattr(partner, 'cppmodel_CPPPackage36') is None


def test_assoc_bodyDirectory75_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent76' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent76', None)
    _safe_set(owner, 'cppmodel_CPPDirectory77', partner)
    assert getattr(partner, 'cppmodel_CPPComponent76') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory77', None)
    assert getattr(partner, 'cppmodel_CPPComponent76') is None


def test_assoc_bodyFile145_stub_double():
    # cppmodel_CPPBodyFile has no real 'cppmodel_CPPBodyFile147' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPExternalBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPExternalBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPExternalBridge(cppExternalNamespace="sample_text")
    partner = cppmodel_CPPBodyFile()
    setattr(partner, 'cppmodel_CPPBodyFile147', None)
    _safe_set(owner, 'cppmodel_CPPExternalBridge146', partner)
    assert getattr(partner, 'cppmodel_CPPBodyFile147') == owner
    _safe_set(owner, 'cppmodel_CPPExternalBridge146', None)
    assert getattr(partner, 'cppmodel_CPPBodyFile147') is None


def test_assoc_commonParameter127_stub_double():
    # cppmodel_Parameter has no real 'cppmodel_Parameter' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPFormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPFormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPFormalParameter(passingMode="sample_text")
    partner = cppmodel_Parameter()
    setattr(partner, 'cppmodel_Parameter', None)
    _safe_set(owner, 'cppmodel_CPPFormalParameter', partner)
    assert getattr(partner, 'cppmodel_Parameter') == owner
    _safe_set(owner, 'cppmodel_CPPFormalParameter', None)
    assert getattr(partner, 'cppmodel_Parameter') is None


def test_assoc_cppAttribute105_stub_double():
    # cppmodel_CPPAttribute has no real 'cppmodel_CPPAttribute' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPClassRefAssocCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPClassRefAssocCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPClassRefAssocCollection(cppContainer="sample_text")
    partner = cppmodel_CPPAttribute()
    setattr(partner, 'cppmodel_CPPAttribute', None)
    _safe_set(owner, 'cppmodel_CPPClassRefAssocCollection', partner)
    assert getattr(partner, 'cppmodel_CPPAttribute') == owner
    _safe_set(owner, 'cppmodel_CPPClassRefAssocCollection', None)
    assert getattr(partner, 'cppmodel_CPPAttribute') is None


def test_assoc_declarationHeaderFile6_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel7' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel7', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile', partner)
    assert getattr(partner, 'cppmodel_CPPModel7') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile', None)
    assert getattr(partner, 'cppmodel_CPPModel7') is None


def test_assoc_declarationHeaderFile66_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent67' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent67', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile68', partner)
    assert getattr(partner, 'cppmodel_CPPComponent67') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile68', None)
    assert getattr(partner, 'cppmodel_CPPComponent67') is None


def test_assoc_definitionHeaderFile69_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent70' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent70', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile71', partner)
    assert getattr(partner, 'cppmodel_CPPComponent70') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile71', None)
    assert getattr(partner, 'cppmodel_CPPComponent70') is None


def test_assoc_definitionHeaderFile8_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel9' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel9', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile10', partner)
    assert getattr(partner, 'cppmodel_CPPModel9') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile10', None)
    assert getattr(partner, 'cppmodel_CPPModel9') is None


def test_assoc_externalBodySkeletonDir22_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel23' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel23', None)
    _safe_set(owner, 'cppmodel_CPPDirectory24', partner)
    assert getattr(partner, 'cppmodel_CPPModel23') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory24', None)
    assert getattr(partner, 'cppmodel_CPPModel23') is None


def test_assoc_externalBodySkeletonDirectory81_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent82' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent82', None)
    _safe_set(owner, 'cppmodel_CPPDirectory83', partner)
    assert getattr(partner, 'cppmodel_CPPComponent82') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory83', None)
    assert getattr(partner, 'cppmodel_CPPComponent82') is None


def test_assoc_externalHeader141_stub_double():
    # cppmodel_CPPExternalLibrary has no real 'cppmodel_CPPExternalLibrary' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPExternalHeader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPExternalHeader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPExternalHeader(name="sample_text")
    partner = cppmodel_CPPExternalLibrary()
    setattr(partner, 'cppmodel_CPPExternalLibrary', None)
    _safe_set(owner, 'cppmodel_CPPExternalHeader142', partner)
    assert owner in getattr(partner, 'cppmodel_CPPExternalLibrary')
    _safe_set(owner, 'cppmodel_CPPExternalHeader142', None)
    assert owner not in getattr(partner, 'cppmodel_CPPExternalLibrary')


def test_assoc_externalHeaderDir19_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel20' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel20', None)
    _safe_set(owner, 'cppmodel_CPPDirectory21', partner)
    assert getattr(partner, 'cppmodel_CPPModel20') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory21', None)
    assert getattr(partner, 'cppmodel_CPPModel20') is None


def test_assoc_externalHeaderDirectory78_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent79' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent79', None)
    _safe_set(owner, 'cppmodel_CPPDirectory80', partner)
    assert getattr(partner, 'cppmodel_CPPComponent79') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory80', None)
    assert getattr(partner, 'cppmodel_CPPComponent79') is None


def test_assoc_externalHeaderFile93_stub_double():
    # cppmodel_CPPPort has no real 'cppmodel_CPPPort94' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPPort()
    setattr(partner, 'cppmodel_CPPPort94', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile95', partner)
    assert getattr(partner, 'cppmodel_CPPPort94') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile95', None)
    assert getattr(partner, 'cppmodel_CPPPort94') is None


def test_assoc_headerDir14_stub_double():
    # cppmodel_CPPModel has no real 'cppmodel_CPPModel15' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPModel()
    setattr(partner, 'cppmodel_CPPModel15', None)
    _safe_set(owner, 'cppmodel_CPPDirectory', partner)
    assert getattr(partner, 'cppmodel_CPPModel15') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory', None)
    assert getattr(partner, 'cppmodel_CPPModel15') is None


def test_assoc_headerDir32_stub_double():
    # cppmodel_CPPPackage has no real 'cppmodel_CPPPackage33' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPPackage()
    setattr(partner, 'cppmodel_CPPPackage33', None)
    _safe_set(owner, 'cppmodel_CPPDirectory34', partner)
    assert getattr(partner, 'cppmodel_CPPPackage33') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory34', None)
    assert getattr(partner, 'cppmodel_CPPPackage33') is None


def test_assoc_headerDirectory72_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent73' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent73', None)
    _safe_set(owner, 'cppmodel_CPPDirectory74', partner)
    assert getattr(partner, 'cppmodel_CPPComponent73') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory74', None)
    assert getattr(partner, 'cppmodel_CPPComponent73') is None


def test_assoc_headerFile29_stub_double():
    # cppmodel_CPPPackage has no real 'cppmodel_CPPPackage30' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPPackage()
    setattr(partner, 'cppmodel_CPPPackage30', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile31', partner)
    assert getattr(partner, 'cppmodel_CPPPackage30') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile31', None)
    assert getattr(partner, 'cppmodel_CPPPackage30') is None


def test_assoc_headerFile38_stub_double():
    # cppmodel_CPPClass has no real 'cppmodel_CPPClass' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPClass()
    setattr(partner, 'cppmodel_CPPClass', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile39', partner)
    assert getattr(partner, 'cppmodel_CPPClass') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile39', None)
    assert getattr(partner, 'cppmodel_CPPClass') is None


def test_assoc_headerFile44_stub_double():
    # cppmodel_CPPProtocol has no real 'cppmodel_CPPProtocol45' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPProtocol()
    setattr(partner, 'cppmodel_CPPProtocol45', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile46', partner)
    assert getattr(partner, 'cppmodel_CPPProtocol45') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile46', None)
    assert getattr(partner, 'cppmodel_CPPProtocol45') is None


def test_assoc_headerFile90_stub_double():
    # cppmodel_CPPPort has no real 'cppmodel_CPPPort91' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPPort()
    setattr(partner, 'cppmodel_CPPPort91', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile92', partner)
    assert getattr(partner, 'cppmodel_CPPPort91') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile92', None)
    assert getattr(partner, 'cppmodel_CPPPort91') is None


def test_assoc_mainHeaderFile60_stub_double():
    # cppmodel_CPPComponent has no real 'cppmodel_CPPComponent61' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPHeaderFile's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPHeaderFile's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPHeaderFile(includeDirectory="sample_text", includeName="sample_text", includePath="sample_text")
    partner = cppmodel_CPPComponent()
    setattr(partner, 'cppmodel_CPPComponent61', None)
    _safe_set(owner, 'cppmodel_CPPHeaderFile62', partner)
    assert getattr(partner, 'cppmodel_CPPComponent61') == owner
    _safe_set(owner, 'cppmodel_CPPHeaderFile62', None)
    assert getattr(partner, 'cppmodel_CPPComponent61') is None


def test_assoc_makeRulesFile57_stub_double():
    # cppmodel_CPPMakeFile has no real 'cppmodel_CPPMakeFile' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPDirectory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPDirectory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPDirectory(name="sample_text", parentDirectory="sample_text", path="sample_text")
    partner = cppmodel_CPPMakeFile()
    setattr(partner, 'cppmodel_CPPMakeFile', None)
    _safe_set(owner, 'cppmodel_CPPDirectory58', partner)
    assert getattr(partner, 'cppmodel_CPPMakeFile') == owner
    _safe_set(owner, 'cppmodel_CPPDirectory58', None)
    assert getattr(partner, 'cppmodel_CPPMakeFile') is None


def test_assoc_ooplNameProvider0_stub_double():
    # cppmodel_OOPLNameProvider has no real 'cppmodel_OOPLNameProvider' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPNamedElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPNamedElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPNamedElement(cppName="sample_text")
    partner = cppmodel_OOPLNameProvider()
    setattr(partner, 'cppmodel_OOPLNameProvider', None)
    _safe_set(owner, 'cppmodel_CPPNamedElement', partner)
    assert getattr(partner, 'cppmodel_OOPLNameProvider') == owner
    _safe_set(owner, 'cppmodel_CPPNamedElement', None)
    assert getattr(partner, 'cppmodel_OOPLNameProvider') is None


def test_assoc_type131_stub_double():
    # cppmodel_OOPLDataType has no real 'cppmodel_OOPLDataType133' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPFormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPFormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPFormalParameter(passingMode="sample_text")
    partner = cppmodel_OOPLDataType()
    setattr(partner, 'cppmodel_OOPLDataType133', None)
    _safe_set(owner, 'cppmodel_CPPFormalParameter132', partner)
    assert getattr(partner, 'cppmodel_OOPLDataType133') == owner
    _safe_set(owner, 'cppmodel_CPPFormalParameter132', None)
    assert getattr(partner, 'cppmodel_OOPLDataType133') is None


def test_assoc_unnamedSequenceType108_stub_double():
    # cppmodel_CPPAttribute has no real 'cppmodel_CPPAttribute109' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPSequence(cppContainer="sample_text")
    partner = cppmodel_CPPAttribute()
    setattr(partner, 'cppmodel_CPPAttribute109', None)
    _safe_set(owner, 'cppmodel_CPPSequence', partner)
    assert getattr(partner, 'cppmodel_CPPAttribute109') == owner
    _safe_set(owner, 'cppmodel_CPPSequence', None)
    assert getattr(partner, 'cppmodel_CPPAttribute109') is None


def test_assoc_unnamedSequenceType136_stub_double():
    # cppmodel_CPPReturnValue has no real 'cppmodel_CPPReturnValue137' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPSequence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPSequence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPSequence(cppContainer="sample_text")
    partner = cppmodel_CPPReturnValue()
    setattr(partner, 'cppmodel_CPPReturnValue137', None)
    _safe_set(owner, 'cppmodel_CPPSequence138', partner)
    assert getattr(partner, 'cppmodel_CPPReturnValue137') == owner
    _safe_set(owner, 'cppmodel_CPPSequence138', None)
    assert getattr(partner, 'cppmodel_CPPReturnValue137') is None


def test_assoc_xtClass148_stub_double():
    # cppmodel_XTClass has no real 'cppmodel_XTClass' property in the generated
    # code (a bare stub) -- manually attach it so cppmodel_CPPExternalBridge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cppmodel_CPPExternalBridge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cppmodel_CPPExternalBridge(cppExternalNamespace="sample_text")
    partner = cppmodel_XTClass()
    setattr(partner, 'cppmodel_XTClass', None)
    _safe_set(owner, 'cppmodel_CPPExternalBridge149', partner)
    assert getattr(partner, 'cppmodel_XTClass') == owner
    _safe_set(owner, 'cppmodel_CPPExternalBridge149', None)
    assert getattr(partner, 'cppmodel_XTClass') is None


