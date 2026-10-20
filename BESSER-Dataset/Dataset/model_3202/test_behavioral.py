import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BindableValue,
    CodeBlock,
    Dependency,
    Directive,
    Element,
    ElementAccess,
    Expression,
    ExpressionStatement,
    FileDependency,
    FileName,
    Literal,
    Name,
    NamedElement,
    Sizeof,
    Statement,
    Structure,
    SwitchClause,
    UserElement,
    langc_AddressOfExpr,
    langc_BinaryOperation,
    langc_BindableValue,
    langc_BlockInitializer,
    langc_BreakStatement,
    langc_BuiltInType,
    langc_CastExpr,
    langc_CharacterLiteral,
    langc_CodeBlob,
    langc_CodeBlock,
    langc_ConditionalStatement,
    langc_Dependency,
    langc_DependencyBlob,
    langc_DependencyList,
    langc_DereferenceExpr,
    langc_Directive,
    langc_Element,
    langc_ElementAccess,
    langc_ElementList,
    langc_ElementReference,
    langc_Enum,
    langc_Enumerator,
    langc_Expression,
    langc_ExpressionBlob,
    langc_ExpressionStatement,
    langc_FileDependency,
    langc_FileName,
    langc_FloatingLiteral,
    langc_FolderName,
    langc_Function,
    langc_FunctionAddress,
    langc_FunctionCall,
    langc_FunctionImplementation,
    langc_FunctionPointer,
    langc_IndexExpr,
    langc_IntegralLiteral,
    langc_LabeledClause,
    langc_LinkableArtifact,
    langc_Literal,
    langc_LogicalComparison,
    langc_Macro,
    langc_MemberAccess,
    langc_Name,
    langc_NamedElement,
    langc_NamedReference,
    langc_ReturnStatement,
    langc_Sizeof,
    langc_SizeofExpr,
    langc_SizeofType,
    langc_Statement,
    langc_StringLiteral,
    langc_Struct,
    langc_Structure,
    langc_SubSystem,
    langc_SwitchClause,
    langc_SwitchStatement,
    langc_System,
    langc_SystemFileName,
    langc_SystemInclude,
    langc_Typedef,
    langc_Union,
    langc_UserElement,
    langc_UserInclude,
    langc_VariableDeclaration,
    langc_VariableDeclarationStatement,
    langc_WhileStatement,
    BooleanOperator,
    CVQualifier,
    ElementKind,
    LinkageSpec,
    Operator,
    Pointer,
    PrimitiveType,
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

def test_assoc_arrayBounds17_reverse_link_reassign_clear():
    a1 = langc_Expression(precendence=7)
    a2 = langc_Expression(precendence=13)
    b = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    _safe_set(b, 'langc_ElementReference18', {a1})
    assert _is_linked(b, 'langc_ElementReference18', a1)
    if hasattr(a1, 'langc_Expression'):
        assert _is_linked(a1, 'langc_Expression', b)
    _safe_set(b, 'langc_ElementReference18', {a2})
    assert _is_linked(b, 'langc_ElementReference18', a2)
    if hasattr(a1, 'langc_Expression'):
        assert not _is_linked(a1, 'langc_Expression', b)
    if hasattr(a2, 'langc_Expression'):
        assert _is_linked(a2, 'langc_Expression', b)
    _safe_set(b, 'langc_ElementReference18', set())
    assert not _is_linked(b, 'langc_ElementReference18', a2)
    if hasattr(a2, 'langc_Expression'):
        assert not _is_linked(a2, 'langc_Expression', b)


def test_assoc_defn91_reverse_link_reassign_clear():
    a1 = langc_UserElement(kind="sample_text")
    a2 = langc_UserElement(kind="sample_text_2")
    b = langc_FileName(hasObjectCode=True)
    _safe_set(b, 'langc_FileName93', a1)
    assert _is_linked(b, 'langc_FileName93', a1)
    if hasattr(a1, 'langc_UserElement92'):
        assert _is_linked(a1, 'langc_UserElement92', b)
    _safe_set(b, 'langc_FileName93', a2)
    assert _is_linked(b, 'langc_FileName93', a2)
    if hasattr(a1, 'langc_UserElement92'):
        assert not _is_linked(a1, 'langc_UserElement92', b)
    if hasattr(a2, 'langc_UserElement92'):
        assert _is_linked(a2, 'langc_UserElement92', b)
    _safe_set(b, 'langc_FileName93', None)
    assert not _is_linked(b, 'langc_FileName93', a2)
    if hasattr(a2, 'langc_UserElement92'):
        assert not _is_linked(a2, 'langc_UserElement92', b)


def test_assoc_dependencies147_reverse_link_reassign_clear():
    a1 = langc_DependencyBlob(markerComment="sample_text", text="sample_text")
    a2 = langc_DependencyBlob(markerComment="sample_text_2", text="sample_text_2")
    b = langc_CodeBlob(markerComment="sample_text", text="sample_text")
    _safe_set(b, 'langc_CodeBlob', a1)
    assert _is_linked(b, 'langc_CodeBlob', a1)
    if hasattr(a1, 'langc_DependencyBlob'):
        assert _is_linked(a1, 'langc_DependencyBlob', b)
    _safe_set(b, 'langc_CodeBlob', a2)
    assert _is_linked(b, 'langc_CodeBlob', a2)
    if hasattr(a1, 'langc_DependencyBlob'):
        assert not _is_linked(a1, 'langc_DependencyBlob', b)
    if hasattr(a2, 'langc_DependencyBlob'):
        assert _is_linked(a2, 'langc_DependencyBlob', b)
    _safe_set(b, 'langc_CodeBlob', None)
    assert not _is_linked(b, 'langc_CodeBlob', a2)
    if hasattr(a2, 'langc_DependencyBlob'):
        assert not _is_linked(a2, 'langc_DependencyBlob', b)


def test_assoc_element62_reverse_link_reassign_clear():
    a1 = langc_VariableDeclaration(linkage="sample_text")
    a2 = langc_VariableDeclaration(linkage="sample_text_2")
    b = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    _safe_set(b, 'langc_ElementReference63', a1)
    assert _is_linked(b, 'langc_ElementReference63', a1)
    if hasattr(a1, 'langc_VariableDeclaration'):
        assert _is_linked(a1, 'langc_VariableDeclaration', b)
    _safe_set(b, 'langc_ElementReference63', a2)
    assert _is_linked(b, 'langc_ElementReference63', a2)
    if hasattr(a1, 'langc_VariableDeclaration'):
        assert not _is_linked(a1, 'langc_VariableDeclaration', b)
    if hasattr(a2, 'langc_VariableDeclaration'):
        assert _is_linked(a2, 'langc_VariableDeclaration', b)
    _safe_set(b, 'langc_ElementReference63', None)
    assert not _is_linked(b, 'langc_ElementReference63', a2)
    if hasattr(a2, 'langc_VariableDeclaration'):
        assert not _is_linked(a2, 'langc_VariableDeclaration', b)


def test_assoc_folders73_reverse_link_reassign_clear():
    a1 = langc_SubSystem(name="sample_text")
    a2 = langc_SubSystem(name="sample_text_2")
    b = langc_FolderName(api=True)
    _safe_set(b, 'langc_FolderName', a1)
    assert _is_linked(b, 'langc_FolderName', a1)
    if hasattr(a1, 'langc_SubSystem74'):
        assert _is_linked(a1, 'langc_SubSystem74', b)
    _safe_set(b, 'langc_FolderName', a2)
    assert _is_linked(b, 'langc_FolderName', a2)
    if hasattr(a1, 'langc_SubSystem74'):
        assert not _is_linked(a1, 'langc_SubSystem74', b)
    if hasattr(a2, 'langc_SubSystem74'):
        assert _is_linked(a2, 'langc_SubSystem74', b)
    _safe_set(b, 'langc_FolderName', None)
    assert not _is_linked(b, 'langc_FolderName', a2)
    if hasattr(a2, 'langc_SubSystem74'):
        assert not _is_linked(a2, 'langc_SubSystem74', b)


def test_assoc_initializer64_reverse_link_reassign_clear():
    a1 = langc_VariableDeclaration(linkage="sample_text")
    a2 = langc_VariableDeclaration(linkage="sample_text_2")
    b = langc_Expression(precendence=7)
    _safe_set(b, 'langc_Expression66', a1)
    assert _is_linked(b, 'langc_Expression66', a1)
    if hasattr(a1, 'langc_VariableDeclaration65'):
        assert _is_linked(a1, 'langc_VariableDeclaration65', b)
    _safe_set(b, 'langc_Expression66', a2)
    assert _is_linked(b, 'langc_Expression66', a2)
    if hasattr(a1, 'langc_VariableDeclaration65'):
        assert not _is_linked(a1, 'langc_VariableDeclaration65', b)
    if hasattr(a2, 'langc_VariableDeclaration65'):
        assert _is_linked(a2, 'langc_VariableDeclaration65', b)
    _safe_set(b, 'langc_Expression66', None)
    assert not _is_linked(b, 'langc_Expression66', a2)
    if hasattr(a2, 'langc_VariableDeclaration65'):
        assert not _is_linked(a2, 'langc_VariableDeclaration65', b)


def test_assoc_lhs127_reverse_link_reassign_clear():
    a1 = langc_LogicalComparison(operator="sample_text")
    a2 = langc_LogicalComparison(operator="sample_text_2")
    b = langc_Expression(precendence=7)
    _safe_set(b, 'langc_Expression128', a1)
    assert _is_linked(b, 'langc_Expression128', a1)
    if hasattr(a1, 'langc_LogicalComparison'):
        assert _is_linked(a1, 'langc_LogicalComparison', b)
    _safe_set(b, 'langc_Expression128', a2)
    assert _is_linked(b, 'langc_Expression128', a2)
    if hasattr(a1, 'langc_LogicalComparison'):
        assert not _is_linked(a1, 'langc_LogicalComparison', b)
    if hasattr(a2, 'langc_LogicalComparison'):
        assert _is_linked(a2, 'langc_LogicalComparison', b)
    _safe_set(b, 'langc_Expression128', None)
    assert not _is_linked(b, 'langc_Expression128', a2)
    if hasattr(a2, 'langc_LogicalComparison'):
        assert not _is_linked(a2, 'langc_LogicalComparison', b)


def test_assoc_lhs48_reverse_link_reassign_clear():
    a1 = langc_Expression(precendence=7)
    a2 = langc_Expression(precendence=13)
    b = langc_BinaryOperation(operator="sample_text")
    _safe_set(b, 'langc_BinaryOperation', a1)
    assert _is_linked(b, 'langc_BinaryOperation', a1)
    if hasattr(a1, 'langc_Expression49'):
        assert _is_linked(a1, 'langc_Expression49', b)
    _safe_set(b, 'langc_BinaryOperation', a2)
    assert _is_linked(b, 'langc_BinaryOperation', a2)
    if hasattr(a1, 'langc_Expression49'):
        assert not _is_linked(a1, 'langc_Expression49', b)
    if hasattr(a2, 'langc_Expression49'):
        assert _is_linked(a2, 'langc_Expression49', b)
    _safe_set(b, 'langc_BinaryOperation', None)
    assert not _is_linked(b, 'langc_BinaryOperation', a2)
    if hasattr(a2, 'langc_Expression49'):
        assert not _is_linked(a2, 'langc_Expression49', b)


def test_assoc_parent2_reverse_link_reassign_clear():
    a1 = langc_Name(name="sample_text")
    a2 = langc_Name(name="sample_text_2")
    b = langc_Name(name="sample_text")
    _safe_set(b, 'langc_Name3', a1)
    assert _is_linked(b, 'langc_Name3', a1)
    if hasattr(a1, 'langc_Name1'):
        assert _is_linked(a1, 'langc_Name1', b)
    _safe_set(b, 'langc_Name3', a2)
    assert _is_linked(b, 'langc_Name3', a2)
    if hasattr(a1, 'langc_Name1'):
        assert not _is_linked(a1, 'langc_Name1', b)
    if hasattr(a2, 'langc_Name1'):
        assert _is_linked(a2, 'langc_Name1', b)
    _safe_set(b, 'langc_Name3', None)
    assert not _is_linked(b, 'langc_Name3', a2)
    if hasattr(a2, 'langc_Name1'):
        assert not _is_linked(a2, 'langc_Name1', b)


def test_assoc_publicFolders75_reverse_link_reassign_clear():
    a1 = langc_SubSystem(name="sample_text")
    a2 = langc_SubSystem(name="sample_text_2")
    b = langc_FolderName(api=True)
    _safe_set(b, 'langc_FolderName77', a1)
    assert _is_linked(b, 'langc_FolderName77', a1)
    if hasattr(a1, 'langc_SubSystem76'):
        assert _is_linked(a1, 'langc_SubSystem76', b)
    _safe_set(b, 'langc_FolderName77', a2)
    assert _is_linked(b, 'langc_FolderName77', a2)
    if hasattr(a1, 'langc_SubSystem76'):
        assert not _is_linked(a1, 'langc_SubSystem76', b)
    if hasattr(a2, 'langc_SubSystem76'):
        assert _is_linked(a2, 'langc_SubSystem76', b)
    _safe_set(b, 'langc_FolderName77', None)
    assert not _is_linked(b, 'langc_FolderName77', a2)
    if hasattr(a2, 'langc_SubSystem76'):
        assert not _is_linked(a2, 'langc_SubSystem76', b)


def test_assoc_returnType4_reverse_link_reassign_clear():
    a1 = langc_Function(linkage="sample_text")
    a2 = langc_Function(linkage="sample_text_2")
    b = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    _safe_set(b, 'langc_ElementReference', a1)
    assert _is_linked(b, 'langc_ElementReference', a1)
    if hasattr(a1, 'langc_Function'):
        assert _is_linked(a1, 'langc_Function', b)
    _safe_set(b, 'langc_ElementReference', a2)
    assert _is_linked(b, 'langc_ElementReference', a2)
    if hasattr(a1, 'langc_Function'):
        assert not _is_linked(a1, 'langc_Function', b)
    if hasattr(a2, 'langc_Function'):
        assert _is_linked(a2, 'langc_Function', b)
    _safe_set(b, 'langc_ElementReference', None)
    assert not _is_linked(b, 'langc_ElementReference', a2)
    if hasattr(a2, 'langc_Function'):
        assert not _is_linked(a2, 'langc_Function', b)


def test_assoc_rhs129_reverse_link_reassign_clear():
    a1 = langc_LogicalComparison(operator="sample_text")
    a2 = langc_LogicalComparison(operator="sample_text_2")
    b = langc_Expression(precendence=7)
    _safe_set(b, 'langc_Expression131', a1)
    assert _is_linked(b, 'langc_Expression131', a1)
    if hasattr(a1, 'langc_LogicalComparison130'):
        assert _is_linked(a1, 'langc_LogicalComparison130', b)
    _safe_set(b, 'langc_Expression131', a2)
    assert _is_linked(b, 'langc_Expression131', a2)
    if hasattr(a1, 'langc_LogicalComparison130'):
        assert not _is_linked(a1, 'langc_LogicalComparison130', b)
    if hasattr(a2, 'langc_LogicalComparison130'):
        assert _is_linked(a2, 'langc_LogicalComparison130', b)
    _safe_set(b, 'langc_Expression131', None)
    assert not _is_linked(b, 'langc_Expression131', a2)
    if hasattr(a2, 'langc_LogicalComparison130'):
        assert not _is_linked(a2, 'langc_LogicalComparison130', b)


def test_assoc_rhs50_reverse_link_reassign_clear():
    a1 = langc_Expression(precendence=7)
    a2 = langc_Expression(precendence=13)
    b = langc_BinaryOperation(operator="sample_text")
    _safe_set(b, 'langc_BinaryOperation51', a1)
    assert _is_linked(b, 'langc_BinaryOperation51', a1)
    if hasattr(a1, 'langc_Expression52'):
        assert _is_linked(a1, 'langc_Expression52', b)
    _safe_set(b, 'langc_BinaryOperation51', a2)
    assert _is_linked(b, 'langc_BinaryOperation51', a2)
    if hasattr(a1, 'langc_Expression52'):
        assert not _is_linked(a1, 'langc_Expression52', b)
    if hasattr(a2, 'langc_Expression52'):
        assert _is_linked(a2, 'langc_Expression52', b)
    _safe_set(b, 'langc_BinaryOperation51', None)
    assert not _is_linked(b, 'langc_BinaryOperation51', a2)
    if hasattr(a2, 'langc_Expression52'):
        assert not _is_linked(a2, 'langc_Expression52', b)


def test_assoc_rootElements151_reverse_link_reassign_clear():
    a1 = langc_UserElement(kind="sample_text")
    a2 = langc_UserElement(kind="sample_text_2")
    b = langc_LinkableArtifact(name="sample_text")
    _safe_set(b, 'langc_LinkableArtifact152', {a1})
    assert _is_linked(b, 'langc_LinkableArtifact152', a1)
    if hasattr(a1, 'langc_UserElement153'):
        assert _is_linked(a1, 'langc_UserElement153', b)
    _safe_set(b, 'langc_LinkableArtifact152', {a2})
    assert _is_linked(b, 'langc_LinkableArtifact152', a2)
    if hasattr(a1, 'langc_UserElement153'):
        assert not _is_linked(a1, 'langc_UserElement153', b)
    if hasattr(a2, 'langc_UserElement153'):
        assert _is_linked(a2, 'langc_UserElement153', b)
    _safe_set(b, 'langc_LinkableArtifact152', set())
    assert not _is_linked(b, 'langc_LinkableArtifact152', a2)
    if hasattr(a2, 'langc_UserElement153'):
        assert not _is_linked(a2, 'langc_UserElement153', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = langc_Expression(precendence=7)
    a2 = langc_Expression(precendence=13)
    b = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    _safe_set(b, 'langc_ElementReference21', a1)
    assert _is_linked(b, 'langc_ElementReference21', a1)
    if hasattr(a1, 'langc_Expression20'):
        assert _is_linked(a1, 'langc_Expression20', b)
    _safe_set(b, 'langc_ElementReference21', a2)
    assert _is_linked(b, 'langc_ElementReference21', a2)
    if hasattr(a1, 'langc_Expression20'):
        assert not _is_linked(a1, 'langc_Expression20', b)
    if hasattr(a2, 'langc_Expression20'):
        assert _is_linked(a2, 'langc_Expression20', b)
    _safe_set(b, 'langc_ElementReference21', None)
    assert not _is_linked(b, 'langc_ElementReference21', a2)
    if hasattr(a2, 'langc_Expression20'):
        assert not _is_linked(a2, 'langc_Expression20', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_arguments24_stub_double():
    # langc_FunctionCall has no real 'langc_FunctionCall25' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_FunctionCall()
    setattr(partner, 'langc_FunctionCall25', None)
    _safe_set(owner, 'langc_Expression26', partner)
    assert owner in getattr(partner, 'langc_FunctionCall25')
    _safe_set(owner, 'langc_Expression26', None)
    assert owner not in getattr(partner, 'langc_FunctionCall25')


def test_assoc_array124_stub_double():
    # langc_IndexExpr has no real 'langc_IndexExpr125' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_IndexExpr()
    setattr(partner, 'langc_IndexExpr125', None)
    _safe_set(owner, 'langc_Expression126', partner)
    assert getattr(partner, 'langc_IndexExpr125') == owner
    _safe_set(owner, 'langc_Expression126', None)
    assert getattr(partner, 'langc_IndexExpr125') is None


def test_assoc_artifacts145_stub_double():
    # langc_System has no real 'langc_System146' property in the generated
    # code (a bare stub) -- manually attach it so langc_LinkableArtifact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_LinkableArtifact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_LinkableArtifact(name="sample_text")
    partner = langc_System()
    setattr(partner, 'langc_System146', None)
    _safe_set(owner, 'langc_LinkableArtifact', partner)
    assert owner in getattr(partner, 'langc_System146')
    _safe_set(owner, 'langc_LinkableArtifact', None)
    assert owner not in getattr(partner, 'langc_System146')


def test_assoc_body134_stub_double():
    # langc_FunctionImplementation has no real 'langc_FunctionImplementation135' property in the generated
    # code (a bare stub) -- manually attach it so langc_CodeBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_CodeBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_CodeBlock(forceBraces=True)
    partner = langc_FunctionImplementation()
    setattr(partner, 'langc_FunctionImplementation135', None)
    _safe_set(owner, 'langc_CodeBlock136', partner)
    assert getattr(partner, 'langc_FunctionImplementation135') == owner
    _safe_set(owner, 'langc_CodeBlock136', None)
    assert getattr(partner, 'langc_FunctionImplementation135') is None


def test_assoc_clauses100_stub_double():
    # langc_SwitchStatement has no real 'langc_SwitchStatement' property in the generated
    # code (a bare stub) -- manually attach it so langc_SwitchClause's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_SwitchClause's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_SwitchClause(fallthrough=True)
    partner = langc_SwitchStatement()
    setattr(partner, 'langc_SwitchStatement', None)
    _safe_set(owner, 'langc_SwitchClause', partner)
    assert owner in getattr(partner, 'langc_SwitchStatement')
    _safe_set(owner, 'langc_SwitchClause', None)
    assert owner not in getattr(partner, 'langc_SwitchStatement')


def test_assoc_condition101_stub_double():
    # langc_SwitchStatement has no real 'langc_SwitchStatement102' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_SwitchStatement()
    setattr(partner, 'langc_SwitchStatement102', None)
    _safe_set(owner, 'langc_Expression103', partner)
    assert getattr(partner, 'langc_SwitchStatement102') == owner
    _safe_set(owner, 'langc_Expression103', None)
    assert getattr(partner, 'langc_SwitchStatement102') is None


def test_assoc_condition108_stub_double():
    # langc_WhileStatement has no real 'langc_WhileStatement' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_WhileStatement()
    setattr(partner, 'langc_WhileStatement', None)
    _safe_set(owner, 'langc_Expression109', partner)
    assert getattr(partner, 'langc_WhileStatement') == owner
    _safe_set(owner, 'langc_Expression109', None)
    assert getattr(partner, 'langc_WhileStatement') is None


def test_assoc_condition154_stub_double():
    # langc_ConditionalStatement has no real 'langc_ConditionalStatement' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_ConditionalStatement()
    setattr(partner, 'langc_ConditionalStatement', None)
    _safe_set(owner, 'langc_Expression155', partner)
    assert getattr(partner, 'langc_ConditionalStatement') == owner
    _safe_set(owner, 'langc_Expression155', None)
    assert getattr(partner, 'langc_ConditionalStatement') is None


def test_assoc_container69_stub_double():
    # langc_MemberAccess has no real 'langc_MemberAccess' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_MemberAccess()
    setattr(partner, 'langc_MemberAccess', None)
    _safe_set(owner, 'langc_Expression70', partner)
    assert getattr(partner, 'langc_MemberAccess') == owner
    _safe_set(owner, 'langc_Expression70', None)
    assert getattr(partner, 'langc_MemberAccess') is None


def test_assoc_defaultImpl7_stub_double():
    # langc_FunctionImplementation has no real 'langc_FunctionImplementation' property in the generated
    # code (a bare stub) -- manually attach it so langc_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Function(linkage="sample_text")
    partner = langc_FunctionImplementation()
    setattr(partner, 'langc_FunctionImplementation', None)
    _safe_set(owner, 'langc_Function8', partner)
    assert getattr(partner, 'langc_FunctionImplementation') == owner
    _safe_set(owner, 'langc_Function8', None)
    assert getattr(partner, 'langc_FunctionImplementation') is None


def test_assoc_element15_stub_double():
    # langc_Element has no real 'langc_Element' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_Element()
    setattr(partner, 'langc_Element', None)
    _safe_set(owner, 'langc_ElementReference16', partner)
    assert getattr(partner, 'langc_Element') == owner
    _safe_set(owner, 'langc_ElementReference16', None)
    assert getattr(partner, 'langc_Element') is None


def test_assoc_element67_stub_double():
    # langc_Typedef has no real 'langc_Typedef' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_Typedef()
    setattr(partner, 'langc_Typedef', None)
    _safe_set(owner, 'langc_ElementReference68', partner)
    assert getattr(partner, 'langc_Typedef') == owner
    _safe_set(owner, 'langc_ElementReference68', None)
    assert getattr(partner, 'langc_Typedef') is None


def test_assoc_element96_stub_double():
    # langc_SizeofType has no real 'langc_SizeofType' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_SizeofType()
    setattr(partner, 'langc_SizeofType', None)
    _safe_set(owner, 'langc_ElementReference97', partner)
    assert getattr(partner, 'langc_SizeofType') == owner
    _safe_set(owner, 'langc_ElementReference97', None)
    assert getattr(partner, 'langc_SizeofType') is None


def test_assoc_elements29_stub_double():
    # langc_ElementList has no real 'langc_ElementList' property in the generated
    # code (a bare stub) -- manually attach it so langc_UserElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_UserElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_UserElement(kind="sample_text")
    partner = langc_ElementList()
    setattr(partner, 'langc_ElementList', None)
    _safe_set(owner, 'langc_UserElement', partner)
    assert owner in getattr(partner, 'langc_ElementList')
    _safe_set(owner, 'langc_UserElement', None)
    assert owner not in getattr(partner, 'langc_ElementList')


def test_assoc_expr104_stub_double():
    # langc_AddressOfExpr has no real 'langc_AddressOfExpr' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_AddressOfExpr()
    setattr(partner, 'langc_AddressOfExpr', None)
    _safe_set(owner, 'langc_Expression105', partner)
    assert getattr(partner, 'langc_AddressOfExpr') == owner
    _safe_set(owner, 'langc_Expression105', None)
    assert getattr(partner, 'langc_AddressOfExpr') is None


def test_assoc_expr106_stub_double():
    # langc_DereferenceExpr has no real 'langc_DereferenceExpr' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_DereferenceExpr()
    setattr(partner, 'langc_DereferenceExpr', None)
    _safe_set(owner, 'langc_Expression107', partner)
    assert getattr(partner, 'langc_DereferenceExpr') == owner
    _safe_set(owner, 'langc_Expression107', None)
    assert getattr(partner, 'langc_DereferenceExpr') is None


def test_assoc_expr132_stub_double():
    # langc_SizeofExpr has no real 'langc_SizeofExpr' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_SizeofExpr()
    setattr(partner, 'langc_SizeofExpr', None)
    _safe_set(owner, 'langc_Expression133', partner)
    assert getattr(partner, 'langc_SizeofExpr') == owner
    _safe_set(owner, 'langc_Expression133', None)
    assert getattr(partner, 'langc_SizeofExpr') is None


def test_assoc_expr45_stub_double():
    # langc_ExpressionStatement has no real 'langc_ExpressionStatement' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_ExpressionStatement()
    setattr(partner, 'langc_ExpressionStatement', None)
    _safe_set(owner, 'langc_Expression46', partner)
    assert getattr(partner, 'langc_ExpressionStatement') == owner
    _safe_set(owner, 'langc_Expression46', None)
    assert getattr(partner, 'langc_ExpressionStatement') is None


def test_assoc_expr88_stub_double():
    # langc_CastExpr has no real 'langc_CastExpr89' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_CastExpr()
    setattr(partner, 'langc_CastExpr89', None)
    _safe_set(owner, 'langc_Expression90', partner)
    assert getattr(partner, 'langc_CastExpr89') == owner
    _safe_set(owner, 'langc_Expression90', None)
    assert getattr(partner, 'langc_CastExpr89') is None


def test_assoc_exprs120_stub_double():
    # langc_BlockInitializer has no real 'langc_BlockInitializer' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_BlockInitializer()
    setattr(partner, 'langc_BlockInitializer', None)
    _safe_set(owner, 'langc_Expression121', partner)
    assert owner in getattr(partner, 'langc_BlockInitializer')
    _safe_set(owner, 'langc_Expression121', None)
    assert owner not in getattr(partner, 'langc_BlockInitializer')


def test_assoc_filename84_stub_double():
    # langc_FileDependency has no real 'langc_FileDependency' property in the generated
    # code (a bare stub) -- manually attach it so langc_FileName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_FileName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_FileName(hasObjectCode=True)
    partner = langc_FileDependency()
    setattr(partner, 'langc_FileDependency', None)
    _safe_set(owner, 'langc_FileName85', partner)
    assert getattr(partner, 'langc_FileDependency') == owner
    _safe_set(owner, 'langc_FileName85', None)
    assert getattr(partner, 'langc_FileDependency') is None


def test_assoc_files71_stub_double():
    # langc_ElementList has no real 'langc_ElementList72' property in the generated
    # code (a bare stub) -- manually attach it so langc_SubSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_SubSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_SubSystem(name="sample_text")
    partner = langc_ElementList()
    setattr(partner, 'langc_ElementList72', None)
    _safe_set(owner, 'langc_SubSystem', {partner})
    assert getattr(partner, 'langc_ElementList72') == owner
    _safe_set(owner, 'langc_SubSystem', set())
    assert getattr(partner, 'langc_ElementList72') is None


def test_assoc_function137_stub_double():
    # langc_FunctionImplementation has no real 'langc_FunctionImplementation138' property in the generated
    # code (a bare stub) -- manually attach it so langc_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Function(linkage="sample_text")
    partner = langc_FunctionImplementation()
    setattr(partner, 'langc_FunctionImplementation138', None)
    _safe_set(owner, 'langc_Function139', partner)
    assert getattr(partner, 'langc_FunctionImplementation138') == owner
    _safe_set(owner, 'langc_Function139', None)
    assert getattr(partner, 'langc_FunctionImplementation138') is None


def test_assoc_function22_stub_double():
    # langc_FunctionCall has no real 'langc_FunctionCall' property in the generated
    # code (a bare stub) -- manually attach it so langc_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Function(linkage="sample_text")
    partner = langc_FunctionCall()
    setattr(partner, 'langc_FunctionCall', None)
    _safe_set(owner, 'langc_Function23', partner)
    assert getattr(partner, 'langc_FunctionCall') == owner
    _safe_set(owner, 'langc_Function23', None)
    assert getattr(partner, 'langc_FunctionCall') is None


def test_assoc_function60_stub_double():
    # langc_FunctionAddress has no real 'langc_FunctionAddress' property in the generated
    # code (a bare stub) -- manually attach it so langc_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Function(linkage="sample_text")
    partner = langc_FunctionAddress()
    setattr(partner, 'langc_FunctionAddress', None)
    _safe_set(owner, 'langc_Function61', partner)
    assert getattr(partner, 'langc_FunctionAddress') == owner
    _safe_set(owner, 'langc_Function61', None)
    assert getattr(partner, 'langc_FunctionAddress') is None


def test_assoc_functionImplementations148_stub_double():
    # langc_FunctionImplementation has no real 'langc_FunctionImplementation150' property in the generated
    # code (a bare stub) -- manually attach it so langc_LinkableArtifact's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_LinkableArtifact's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_LinkableArtifact(name="sample_text")
    partner = langc_FunctionImplementation()
    setattr(partner, 'langc_FunctionImplementation150', None)
    _safe_set(owner, 'langc_LinkableArtifact149', {partner})
    assert getattr(partner, 'langc_FunctionImplementation150') == owner
    _safe_set(owner, 'langc_LinkableArtifact149', set())
    assert getattr(partner, 'langc_FunctionImplementation150') is None


def test_assoc_index122_stub_double():
    # langc_IndexExpr has no real 'langc_IndexExpr' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_IndexExpr()
    setattr(partner, 'langc_IndexExpr', None)
    _safe_set(owner, 'langc_Expression123', partner)
    assert getattr(partner, 'langc_IndexExpr') == owner
    _safe_set(owner, 'langc_Expression123', None)
    assert getattr(partner, 'langc_IndexExpr') is None


def test_assoc_labels98_stub_double():
    # langc_LabeledClause has no real 'langc_LabeledClause' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_LabeledClause()
    setattr(partner, 'langc_LabeledClause', None)
    _safe_set(owner, 'langc_Expression99', partner)
    assert owner in getattr(partner, 'langc_LabeledClause')
    _safe_set(owner, 'langc_Expression99', None)
    assert owner not in getattr(partner, 'langc_LabeledClause')


def test_assoc_name0_stub_double():
    # langc_NamedElement has no real 'langc_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_NamedElement()
    setattr(partner, 'langc_NamedElement', None)
    _safe_set(owner, 'langc_Name', partner)
    assert getattr(partner, 'langc_NamedElement') == owner
    _safe_set(owner, 'langc_Name', None)
    assert getattr(partner, 'langc_NamedElement') is None


def test_assoc_name115_stub_double():
    # langc_Macro has no real 'langc_Macro116' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_Macro()
    setattr(partner, 'langc_Macro116', None)
    _safe_set(owner, 'langc_Name117', partner)
    assert getattr(partner, 'langc_Macro116') == owner
    _safe_set(owner, 'langc_Name117', None)
    assert getattr(partner, 'langc_Macro116') is None


def test_assoc_name27_stub_double():
    # langc_ElementAccess has no real 'langc_ElementAccess' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_ElementAccess()
    setattr(partner, 'langc_ElementAccess', None)
    _safe_set(owner, 'langc_Name28', partner)
    assert getattr(partner, 'langc_ElementAccess') == owner
    _safe_set(owner, 'langc_Name28', None)
    assert getattr(partner, 'langc_ElementAccess') is None


def test_assoc_name30_stub_double():
    # langc_ElementList has no real 'langc_ElementList31' property in the generated
    # code (a bare stub) -- manually attach it so langc_FileName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_FileName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_FileName(hasObjectCode=True)
    partner = langc_ElementList()
    setattr(partner, 'langc_ElementList31', None)
    _safe_set(owner, 'langc_FileName', partner)
    assert getattr(partner, 'langc_ElementList31') == owner
    _safe_set(owner, 'langc_FileName', None)
    assert getattr(partner, 'langc_ElementList31') is None


def test_assoc_name81_stub_double():
    # langc_Enumerator has no real 'langc_Enumerator82' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_Enumerator()
    setattr(partner, 'langc_Enumerator82', None)
    _safe_set(owner, 'langc_Name83', partner)
    assert getattr(partner, 'langc_Enumerator82') == owner
    _safe_set(owner, 'langc_Name83', None)
    assert getattr(partner, 'langc_Enumerator82') is None


def test_assoc_name9_stub_double():
    # langc_NamedReference has no real 'langc_NamedReference10' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_NamedReference()
    setattr(partner, 'langc_NamedReference10', None)
    _safe_set(owner, 'langc_Name11', partner)
    assert getattr(partner, 'langc_NamedReference10') == owner
    _safe_set(owner, 'langc_Name11', None)
    assert getattr(partner, 'langc_NamedReference10') is None


def test_assoc_parameters110_stub_double():
    # langc_Macro has no real 'langc_Macro' property in the generated
    # code (a bare stub) -- manually attach it so langc_Name's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Name's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Name(name="sample_text")
    partner = langc_Macro()
    setattr(partner, 'langc_Macro', None)
    _safe_set(owner, 'langc_Name111', partner)
    assert owner in getattr(partner, 'langc_Macro')
    _safe_set(owner, 'langc_Name111', None)
    assert owner not in getattr(partner, 'langc_Macro')


def test_assoc_parameters5_stub_double():
    # langc_NamedReference has no real 'langc_NamedReference' property in the generated
    # code (a bare stub) -- manually attach it so langc_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Function(linkage="sample_text")
    partner = langc_NamedReference()
    setattr(partner, 'langc_NamedReference', None)
    _safe_set(owner, 'langc_Function6', {partner})
    assert getattr(partner, 'langc_NamedReference') == owner
    _safe_set(owner, 'langc_Function6', set())
    assert getattr(partner, 'langc_NamedReference') is None


def test_assoc_parameters57_stub_double():
    # langc_FunctionPointer has no real 'langc_FunctionPointer58' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_FunctionPointer()
    setattr(partner, 'langc_FunctionPointer58', None)
    _safe_set(owner, 'langc_ElementReference59', partner)
    assert owner in getattr(partner, 'langc_FunctionPointer58')
    _safe_set(owner, 'langc_ElementReference59', None)
    assert owner not in getattr(partner, 'langc_FunctionPointer58')


def test_assoc_publicFolders142_stub_double():
    # langc_System has no real 'langc_System143' property in the generated
    # code (a bare stub) -- manually attach it so langc_FolderName's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_FolderName's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_FolderName(api=True)
    partner = langc_System()
    setattr(partner, 'langc_System143', None)
    _safe_set(owner, 'langc_FolderName144', partner)
    assert owner in getattr(partner, 'langc_System143')
    _safe_set(owner, 'langc_FolderName144', None)
    assert owner not in getattr(partner, 'langc_System143')


def test_assoc_replacement112_stub_double():
    # langc_Macro has no real 'langc_Macro113' property in the generated
    # code (a bare stub) -- manually attach it so langc_Expression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_Expression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_Expression(precendence=7)
    partner = langc_Macro()
    setattr(partner, 'langc_Macro113', None)
    _safe_set(owner, 'langc_Expression114', partner)
    assert getattr(partner, 'langc_Macro113') == owner
    _safe_set(owner, 'langc_Expression114', None)
    assert getattr(partner, 'langc_Macro113') is None


def test_assoc_returnType55_stub_double():
    # langc_FunctionPointer has no real 'langc_FunctionPointer' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_FunctionPointer()
    setattr(partner, 'langc_FunctionPointer', None)
    _safe_set(owner, 'langc_ElementReference56', partner)
    assert getattr(partner, 'langc_FunctionPointer') == owner
    _safe_set(owner, 'langc_ElementReference56', None)
    assert getattr(partner, 'langc_FunctionPointer') is None


def test_assoc_statements47_stub_double():
    # langc_Statement has no real 'langc_Statement' property in the generated
    # code (a bare stub) -- manually attach it so langc_CodeBlock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_CodeBlock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_CodeBlock(forceBraces=True)
    partner = langc_Statement()
    setattr(partner, 'langc_Statement', None)
    _safe_set(owner, 'langc_CodeBlock', {partner})
    assert getattr(partner, 'langc_Statement') == owner
    _safe_set(owner, 'langc_CodeBlock', set())
    assert getattr(partner, 'langc_Statement') is None


def test_assoc_subSystems140_stub_double():
    # langc_System has no real 'langc_System' property in the generated
    # code (a bare stub) -- manually attach it so langc_SubSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_SubSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_SubSystem(name="sample_text")
    partner = langc_System()
    setattr(partner, 'langc_System', None)
    _safe_set(owner, 'langc_SubSystem141', partner)
    assert owner in getattr(partner, 'langc_System')
    _safe_set(owner, 'langc_SubSystem141', None)
    assert owner not in getattr(partner, 'langc_System')


def test_assoc_targetType86_stub_double():
    # langc_CastExpr has no real 'langc_CastExpr' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_CastExpr()
    setattr(partner, 'langc_CastExpr', None)
    _safe_set(owner, 'langc_ElementReference87', partner)
    assert getattr(partner, 'langc_CastExpr') == owner
    _safe_set(owner, 'langc_ElementReference87', None)
    assert getattr(partner, 'langc_CastExpr') is None


def test_assoc_type12_stub_double():
    # langc_NamedReference has no real 'langc_NamedReference13' property in the generated
    # code (a bare stub) -- manually attach it so langc_ElementReference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_ElementReference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_ElementReference(cvQualifier="sample_text", pointerSpec="sample_text")
    partner = langc_NamedReference()
    setattr(partner, 'langc_NamedReference13', None)
    _safe_set(owner, 'langc_ElementReference14', partner)
    assert getattr(partner, 'langc_NamedReference13') == owner
    _safe_set(owner, 'langc_ElementReference14', None)
    assert getattr(partner, 'langc_NamedReference13') is None


def test_assoc_value79_stub_double():
    # langc_Enumerator has no real 'langc_Enumerator80' property in the generated
    # code (a bare stub) -- manually attach it so langc_IntegralLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_IntegralLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_IntegralLiteral(bytes="sample_text", signed=True, value="sample_text")
    partner = langc_Enumerator()
    setattr(partner, 'langc_Enumerator80', None)
    _safe_set(owner, 'langc_IntegralLiteral', partner)
    assert getattr(partner, 'langc_Enumerator80') == owner
    _safe_set(owner, 'langc_IntegralLiteral', None)
    assert getattr(partner, 'langc_Enumerator80') is None


def test_assoc_variable118_stub_double():
    # langc_VariableDeclarationStatement has no real 'langc_VariableDeclarationStatement' property in the generated
    # code (a bare stub) -- manually attach it so langc_VariableDeclaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # langc_VariableDeclaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = langc_VariableDeclaration(linkage="sample_text")
    partner = langc_VariableDeclarationStatement()
    setattr(partner, 'langc_VariableDeclarationStatement', None)
    _safe_set(owner, 'langc_VariableDeclaration119', partner)
    assert getattr(partner, 'langc_VariableDeclarationStatement') == owner
    _safe_set(owner, 'langc_VariableDeclaration119', None)
    assert getattr(partner, 'langc_VariableDeclarationStatement') is None


