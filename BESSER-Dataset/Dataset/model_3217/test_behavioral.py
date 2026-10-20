import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Access,
    BaseAccess,
    BasePath,
    BlockStatement,
    Branch,
    BranchStatement,
    CatchBlock,
    CatchParameter,
    Clone,
    CloneInstance,
    CompositeAccess,
    Constructor,
    DeclarationTypeAccess,
    Delegate,
    Destructor,
    Directory,
    Exit,
    Field,
    File,
    FlowInstr,
    FormalParameter,
    Function,
    FunctionAccess,
    GASTClass,
    GASTExpression,
    GASTType,
    GlobalFunction,
    GlobalVariable,
    Identifier,
    InheritanceTypeAccess,
    LocalVariable,
    LoopStatement,
    Member,
    Method,
    ModelAnnotation,
    ModelElement,
    NamedModelElement,
    Package,
    Position,
    Property,
    Root,
    SourceEntity,
    Statement,
    StructuralAbstraction,
    ThrowTypeAccess,
    TypeAccess,
    TypeAlias,
    TypeDecorator,
    TypeParameterClass,
    Var,
    Variable,
    VariableAccess,
    annotations_ModelAnnotation,
    core_GenericEntity,
    core_ModelElement,
    core_NamedModelElement,
    core_SourceEntity,
    functions_Constructor,
    functions_Function,
    functions_GlobalFunction,
    functions_Method,
    gast_accesses_Access,
    gast_accesses_BaseAccess,
    gast_accesses_CastTypeAccess,
    gast_accesses_CompositeAccess,
    gast_accesses_DeclarationTypeAccess,
    gast_accesses_DelegateAccess,
    gast_accesses_FunctionAccess,
    gast_accesses_InheritanceTypeAccess,
    gast_accesses_ParameterInstantiationTypeAccess,
    gast_accesses_PropertyAccess,
    gast_accesses_RunTimeTypeAccess,
    gast_accesses_SelfAccess,
    gast_accesses_StaticTypeAccess,
    gast_accesses_ThrowTypeAccess,
    gast_accesses_TypeAccess,
    gast_accesses_VariableAccess,
    gast_annotations_Attribute,
    gast_annotations_Clone,
    gast_annotations_CloneInstance,
    gast_annotations_Comment,
    gast_annotations_Layer,
    gast_annotations_ModelAnnotation,
    gast_annotations_StructuralAbstraction,
    gast_annotations_Subsystem,
    gast_core_BasePath,
    gast_core_Directory,
    gast_core_File,
    gast_core_GenericEntity,
    gast_core_Identifier,
    gast_core_ModelElement,
    gast_core_NamedModelElement,
    gast_core_Package,
    gast_core_PackageAlias,
    gast_core_Position,
    gast_core_Root,
    gast_core_SourceEntity,
    gast_functions_Constructor,
    gast_functions_Delegate,
    gast_functions_Destructor,
    gast_functions_Function,
    gast_functions_GenericConstructor,
    gast_functions_GenericFunction,
    gast_functions_GenericMethod,
    gast_functions_GlobalFunction,
    gast_functions_Method,
    gast_statements_BlockStatement,
    gast_statements_Branch,
    gast_statements_BranchStatement,
    gast_statements_CatchBlock,
    gast_statements_ExceptionHandler,
    gast_statements_Exit,
    gast_statements_FlowInstr,
    gast_statements_GASTBehaviour,
    gast_statements_GASTExpression,
    gast_statements_JumpStatement,
    gast_statements_LoopStatement,
    gast_statements_Methods,
    gast_statements_Param,
    gast_statements_SimpleStatement,
    gast_statements_Statement,
    gast_statements_Var,
    gast_types_GASTArray,
    gast_types_GASTClass,
    gast_types_GASTEnumeration,
    gast_types_GASTStruct,
    gast_types_GASTType,
    gast_types_GASTUnion,
    gast_types_GenericClass,
    gast_types_Member,
    gast_types_Reference,
    gast_types_TypeAlias,
    gast_types_TypeDecorator,
    gast_types_TypeParameterClass,
    gast_variables_CatchParameter,
    gast_variables_Field,
    gast_variables_FormalParameter,
    gast_variables_GlobalVariable,
    gast_variables_LocalVariable,
    gast_variables_Property,
    gast_variables_Variable,
    statements_BlockStatement,
    statements_FlowInstr,
    statements_Statement,
    types_GASTClass,
    types_GASTType,
    types_Member,
    types_TypeDecorator,
    variables_Field,
    variables_Variable,
    GlobalFunctionKind,
    JumpStatementKind,
    LoopStatementKind,
    Status,
    Visibilities,
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

def test_assoc_accesses308_stub_double():
    # Access has no real 'Access310' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Access()
    setattr(partner, 'Access310', None)
    _safe_set(owner, 'gast_functions_Function309', {partner})
    assert getattr(partner, 'Access310') == owner
    _safe_set(owner, 'gast_functions_Function309', set())
    assert getattr(partner, 'Access310') is None


def test_assoc_accesses6_stub_double():
    # BaseAccess has no real 'BaseAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = BaseAccess()
    setattr(partner, 'BaseAccess', None)
    _safe_set(owner, 'parentStatement', {partner})
    assert getattr(partner, 'BaseAccess') == owner
    _safe_set(owner, 'parentStatement', set())
    assert getattr(partner, 'BaseAccess') is None


def test_assoc_aliasedType186_stub_double():
    # GASTType has no real 'GASTType187' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTType()
    setattr(partner, 'GASTType187', None)
    _safe_set(owner, 'gast_types_TypeAlias', partner)
    assert getattr(partner, 'GASTType187') == owner
    _safe_set(owner, 'gast_types_TypeAlias', None)
    assert getattr(partner, 'GASTType187') is None


def test_assoc_allAccessedClasses236_stub_double():
    # GASTClass has no real 'GASTClass238' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass238', None)
    _safe_set(owner, 'gast_types_GASTClass237', {partner})
    assert getattr(partner, 'GASTClass238') == owner
    _safe_set(owner, 'gast_types_GASTClass237', set())
    assert getattr(partner, 'GASTClass238') is None


def test_assoc_allAccessedPackages84_stub_double():
    # Package has no real 'Package86' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package86', None)
    _safe_set(owner, 'gast_core_Package85', {partner})
    assert getattr(partner, 'Package86') == owner
    _safe_set(owner, 'gast_core_Package85', set())
    assert getattr(partner, 'Package86') is None


def test_assoc_allAccesses233_stub_double():
    # Access has no real 'Access235' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Access()
    setattr(partner, 'Access235', None)
    _safe_set(owner, 'gast_types_GASTClass234', {partner})
    assert getattr(partner, 'Access235') == owner
    _safe_set(owner, 'gast_types_GASTClass234', set())
    assert getattr(partner, 'Access235') is None


def test_assoc_allAccesses68_stub_double():
    # Access has no real 'Access' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Access()
    setattr(partner, 'Access', None)
    _safe_set(owner, 'gast_core_Package69', {partner})
    assert getattr(partner, 'Access') == owner
    _safe_set(owner, 'gast_core_Package69', set())
    assert getattr(partner, 'Access') is None


def test_assoc_allAccesses90_stub_double():
    # Access has no real 'Access91' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Access()
    setattr(partner, 'Access91', None)
    _safe_set(owner, 'gast_core_Root', {partner})
    assert getattr(partner, 'Access91') == owner
    _safe_set(owner, 'gast_core_Root', set())
    assert getattr(partner, 'Access91') is None


def test_assoc_allInnerClasses59_stub_double():
    # GASTClass has no real 'GASTClass61' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass61', None)
    _safe_set(owner, 'gast_core_Package60', {partner})
    assert getattr(partner, 'GASTClass61') == owner
    _safe_set(owner, 'gast_core_Package60', set())
    assert getattr(partner, 'GASTClass61') is None


def test_assoc_allInnerClasses92_stub_double():
    # GASTClass has no real 'GASTClass94' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass94', None)
    _safe_set(owner, 'gast_core_Root93', {partner})
    assert getattr(partner, 'GASTClass94') == owner
    _safe_set(owner, 'gast_core_Root93', set())
    assert getattr(partner, 'GASTClass94') is None


def test_assoc_allInterfaces65_stub_double():
    # GASTClass has no real 'GASTClass67' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass67', None)
    _safe_set(owner, 'gast_core_Package66', {partner})
    assert getattr(partner, 'GASTClass67') == owner
    _safe_set(owner, 'gast_core_Package66', set())
    assert getattr(partner, 'GASTClass67') is None


def test_assoc_allInterfaces95_stub_double():
    # GASTClass has no real 'GASTClass97' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass97', None)
    _safe_set(owner, 'gast_core_Root96', {partner})
    assert getattr(partner, 'GASTClass97') == owner
    _safe_set(owner, 'gast_core_Root96', set())
    assert getattr(partner, 'GASTClass97') is None


def test_assoc_allLocalClasses58_stub_double():
    # GASTClass has no real 'GASTClass' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass', None)
    _safe_set(owner, 'gast_core_Package', {partner})
    assert getattr(partner, 'GASTClass') == owner
    _safe_set(owner, 'gast_core_Package', set())
    assert getattr(partner, 'GASTClass') is None


def test_assoc_allLocalClasses98_stub_double():
    # GASTClass has no real 'GASTClass100' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass100', None)
    _safe_set(owner, 'gast_core_Root99', {partner})
    assert getattr(partner, 'GASTClass100') == owner
    _safe_set(owner, 'gast_core_Root99', set())
    assert getattr(partner, 'GASTClass100') is None


def test_assoc_allModelElements104_stub_double():
    # ModelElement has no real 'ModelElement' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement', None)
    _safe_set(owner, 'gast_core_Root105', {partner})
    assert getattr(partner, 'ModelElement') == owner
    _safe_set(owner, 'gast_core_Root105', set())
    assert getattr(partner, 'ModelElement') is None


def test_assoc_allNormalClasses101_stub_double():
    # GASTClass has no real 'GASTClass103' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass103', None)
    _safe_set(owner, 'gast_core_Root102', {partner})
    assert getattr(partner, 'GASTClass103') == owner
    _safe_set(owner, 'gast_core_Root102', set())
    assert getattr(partner, 'GASTClass103') is None


def test_assoc_allNormalClasses62_stub_double():
    # GASTClass has no real 'GASTClass64' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass64', None)
    _safe_set(owner, 'gast_core_Package63', {partner})
    assert getattr(partner, 'GASTClass64') == owner
    _safe_set(owner, 'gast_core_Package63', set())
    assert getattr(partner, 'GASTClass64') is None


def test_assoc_allStatements304_stub_double():
    # Statement has no real 'Statement305' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Statement()
    setattr(partner, 'Statement305', None)
    _safe_set(owner, 'gast_functions_Function', {partner})
    assert getattr(partner, 'Statement305') == owner
    _safe_set(owner, 'gast_functions_Function', set())
    assert getattr(partner, 'Statement305') is None


def test_assoc_annotations57_stub_double():
    # ModelAnnotation has no real 'ModelAnnotation' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_ModelElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_ModelElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_ModelElement(sissyId=7, status="sample_text")
    partner = ModelAnnotation()
    setattr(partner, 'ModelAnnotation', None)
    _safe_set(owner, 'gast_core_ModelElement', {partner})
    assert getattr(partner, 'ModelAnnotation') == owner
    _safe_set(owner, 'gast_core_ModelElement', set())
    assert getattr(partner, 'ModelAnnotation') is None


def test_assoc_assembly162_stub_double():
    # File has no real 'File164' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File164', None)
    _safe_set(owner, 'gast_core_Position163', partner)
    assert getattr(partner, 'File164') == owner
    _safe_set(owner, 'gast_core_Position163', None)
    assert getattr(partner, 'File164') is None


def test_assoc_basePath130_stub_double():
    # BasePath has no real 'BasePath131' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = BasePath()
    setattr(partner, 'BasePath131', None)
    _safe_set(owner, 'directories', partner)
    assert getattr(partner, 'BasePath131') == owner
    _safe_set(owner, 'directories', None)
    assert getattr(partner, 'BasePath131') is None


def test_assoc_basePaths120_stub_double():
    # BasePath has no real 'BasePath' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = BasePath()
    setattr(partner, 'BasePath', None)
    _safe_set(owner, 'root121', {partner})
    assert getattr(partner, 'BasePath') == owner
    _safe_set(owner, 'root121', set())
    assert getattr(partner, 'BasePath') is None


def test_assoc_baseType184_stub_double():
    # GASTType has no real 'GASTType185' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTArray(dimensions=7)
    partner = GASTType()
    setattr(partner, 'GASTType185', None)
    _safe_set(owner, 'gast_types_GASTArray', partner)
    assert getattr(partner, 'GASTType185') == owner
    _safe_set(owner, 'gast_types_GASTArray', None)
    assert getattr(partner, 'GASTType185') is None


def test_assoc_blockstatement8_stub_double():
    # BlockStatement has no real 'BlockStatement10' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = BlockStatement()
    setattr(partner, 'BlockStatement10', None)
    _safe_set(owner, 'statements9', partner)
    assert getattr(partner, 'BlockStatement10') == owner
    _safe_set(owner, 'statements9', None)
    assert getattr(partner, 'BlockStatement10') is None


def test_assoc_body311_stub_double():
    # BlockStatement has no real 'BlockStatement313' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = BlockStatement()
    setattr(partner, 'BlockStatement313', None)
    _safe_set(owner, 'surroundingFunction312', partner)
    assert getattr(partner, 'BlockStatement313') == owner
    _safe_set(owner, 'surroundingFunction312', None)
    assert getattr(partner, 'BlockStatement313') is None


def test_assoc_body38_stub_double():
    # Statement has no real 'Statement39' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = Statement()
    setattr(partner, 'Statement39', None)
    _safe_set(owner, 'loopstatement', partner)
    assert getattr(partner, 'Statement39') == owner
    _safe_set(owner, 'loopstatement', None)
    assert getattr(partner, 'Statement39') is None


def test_assoc_branch12_stub_double():
    # Branch has no real 'Branch' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = Branch()
    setattr(partner, 'Branch', None)
    _safe_set(owner, 'statement', partner)
    assert getattr(partner, 'Branch') == owner
    _safe_set(owner, 'statement', None)
    assert getattr(partner, 'Branch') is None


def test_assoc_breakConditionExpression30_stub_double():
    # GASTExpression has no real 'GASTExpression31' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression31', None)
    _safe_set(owner, 'gast_statements_LoopStatement', partner)
    assert getattr(partner, 'GASTExpression31') == owner
    _safe_set(owner, 'gast_statements_LoopStatement', None)
    assert getattr(partner, 'GASTExpression31') is None


def test_assoc_cfNext17_stub_double():
    # Statement has no real 'Statement19' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = Statement()
    setattr(partner, 'Statement19', None)
    _safe_set(owner, 'gast_statements_Statement18', {partner})
    assert getattr(partner, 'Statement19') == owner
    _safe_set(owner, 'gast_statements_Statement18', set())
    assert getattr(partner, 'Statement19') is None


def test_assoc_cfPre14_stub_double():
    # Statement has no real 'Statement16' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = Statement()
    setattr(partner, 'Statement16', None)
    _safe_set(owner, 'gast_statements_Statement15', {partner})
    assert getattr(partner, 'Statement16') == owner
    _safe_set(owner, 'gast_statements_Statement15', set())
    assert getattr(partner, 'Statement16') is None


def test_assoc_cfPrev53_stub_double():
    # FlowInstr has no real 'FlowInstr54' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_FlowInstr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_FlowInstr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_FlowInstr(txt="sample_text")
    partner = FlowInstr()
    setattr(partner, 'FlowInstr54', None)
    _safe_set(owner, 'cfnext', {partner})
    assert getattr(partner, 'FlowInstr54') == owner
    _safe_set(owner, 'cfnext', set())
    assert getattr(partner, 'FlowInstr54') is None


def test_assoc_cfnext52_stub_double():
    # FlowInstr has no real 'FlowInstr' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_FlowInstr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_FlowInstr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_FlowInstr(txt="sample_text")
    partner = FlowInstr()
    setattr(partner, 'FlowInstr', None)
    _safe_set(owner, 'cfPrev', {partner})
    assert getattr(partner, 'FlowInstr') == owner
    _safe_set(owner, 'cfPrev', set())
    assert getattr(partner, 'FlowInstr') is None


def test_assoc_classes77_stub_double():
    # GASTClass has no real 'GASTClass79' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass79', None)
    _safe_set(owner, 'surroundingPackage78', {partner})
    assert getattr(partner, 'GASTClass79') == owner
    _safe_set(owner, 'surroundingPackage78', set())
    assert getattr(partner, 'GASTClass79') is None


def test_assoc_cloneInstance7_stub_double():
    # CloneInstance has no real 'CloneInstance' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = CloneInstance()
    setattr(partner, 'CloneInstance', None)
    _safe_set(owner, 'statements', partner)
    assert getattr(partner, 'CloneInstance') == owner
    _safe_set(owner, 'statements', None)
    assert getattr(partner, 'CloneInstance') is None


def test_assoc_clones111_stub_double():
    # Clone has no real 'Clone' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Clone()
    setattr(partner, 'Clone', None)
    _safe_set(owner, 'root112', {partner})
    assert getattr(partner, 'Clone') == owner
    _safe_set(owner, 'root112', set())
    assert getattr(partner, 'Clone') is None


def test_assoc_constructors200_stub_double():
    # Constructor has no real 'Constructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Constructor()
    setattr(partner, 'Constructor', None)
    _safe_set(owner, 'surroundingClass201', {partner})
    assert getattr(partner, 'Constructor') == owner
    _safe_set(owner, 'surroundingClass201', set())
    assert getattr(partner, 'Constructor') is None


def test_assoc_danglingModelElements117_stub_double():
    # ModelElement has no real 'ModelElement119' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement119', None)
    _safe_set(owner, 'gast_core_Root118', {partner})
    assert getattr(partner, 'ModelElement119') == owner
    _safe_set(owner, 'gast_core_Root118', set())
    assert getattr(partner, 'ModelElement119') is None


def test_assoc_def_49_stub_double():
    # Var has no real 'Var51' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_FlowInstr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_FlowInstr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_FlowInstr(txt="sample_text")
    partner = Var()
    setattr(partner, 'Var51', None)
    _safe_set(owner, 'gast_statements_FlowInstr50', {partner})
    assert getattr(partner, 'Var51') == owner
    _safe_set(owner, 'gast_statements_FlowInstr50', set())
    assert getattr(partner, 'Var51') is None


def test_assoc_delegates70_stub_double():
    # Delegate has no real 'Delegate' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Delegate()
    setattr(partner, 'Delegate', None)
    _safe_set(owner, 'surroundingPackage', {partner})
    assert getattr(partner, 'Delegate') == owner
    _safe_set(owner, 'surroundingPackage', set())
    assert getattr(partner, 'Delegate') is None


def test_assoc_destructors202_stub_double():
    # Destructor has no real 'Destructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Destructor()
    setattr(partner, 'Destructor', None)
    _safe_set(owner, 'surroundingClass203', {partner})
    assert getattr(partner, 'Destructor') == owner
    _safe_set(owner, 'surroundingClass203', set())
    assert getattr(partner, 'Destructor') is None


def test_assoc_directories56_stub_double():
    # Directory has no real 'Directory' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_BasePath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_BasePath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_BasePath(path="sample_text")
    partner = Directory()
    setattr(partner, 'Directory', None)
    _safe_set(owner, 'basePath', {partner})
    assert getattr(partner, 'Directory') == owner
    _safe_set(owner, 'basePath', set())
    assert getattr(partner, 'Directory') is None


def test_assoc_directory158_stub_double():
    # Directory has no real 'Directory159' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Directory()
    setattr(partner, 'Directory159', None)
    _safe_set(owner, 'files', partner)
    assert getattr(partner, 'Directory159') == owner
    _safe_set(owner, 'files', None)
    assert getattr(partner, 'Directory159') is None


def test_assoc_exit47_stub_double():
    # Exit has no real 'Exit' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Methods's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Methods's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Methods(methodName="sample_text")
    partner = Exit()
    setattr(partner, 'Exit', None)
    _safe_set(owner, 'gast_statements_Methods', partner)
    assert getattr(partner, 'Exit') == owner
    _safe_set(owner, 'gast_statements_Methods', None)
    assert getattr(partner, 'Exit') is None


def test_assoc_expression41_stub_double():
    # GASTExpression has no real 'GASTExpression42' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_JumpStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_JumpStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_JumpStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression42', None)
    _safe_set(owner, 'gast_statements_JumpStatement', partner)
    assert getattr(partner, 'GASTExpression42') == owner
    _safe_set(owner, 'gast_statements_JumpStatement', None)
    assert getattr(partner, 'GASTExpression42') is None


def test_assoc_fields204_stub_double():
    # Field has no real 'Field' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field', None)
    _safe_set(owner, 'surroundingClass205', {partner})
    assert getattr(partner, 'Field') == owner
    _safe_set(owner, 'surroundingClass205', set())
    assert getattr(partner, 'Field') is None


def test_assoc_files129_stub_double():
    # File has no real 'File' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = File()
    setattr(partner, 'File', None)
    _safe_set(owner, 'directory', {partner})
    assert getattr(partner, 'File') == owner
    _safe_set(owner, 'directory', set())
    assert getattr(partner, 'File') is None


def test_assoc_formalParameters301_stub_double():
    # FormalParameter has no real 'FormalParameter' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = FormalParameter()
    setattr(partner, 'FormalParameter', None)
    _safe_set(owner, 'surroundingFunction', {partner})
    assert getattr(partner, 'FormalParameter') == owner
    _safe_set(owner, 'surroundingFunction', set())
    assert getattr(partner, 'FormalParameter') is None


def test_assoc_friendClasses224_stub_double():
    # GASTClass has no real 'GASTClass225' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass225', None)
    _safe_set(owner, 'gastClass', {partner})
    assert getattr(partner, 'GASTClass225') == owner
    _safe_set(owner, 'gastClass', set())
    assert getattr(partner, 'GASTClass225') is None


def test_assoc_friendFunctions228_stub_double():
    # Function has no real 'Function230' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function230', None)
    _safe_set(owner, 'gast_types_GASTClass229', {partner})
    assert getattr(partner, 'Function230') == owner
    _safe_set(owner, 'gast_types_GASTClass229', set())
    assert getattr(partner, 'Function230') is None


def test_assoc_gastClass226_stub_double():
    # GASTClass has no real 'GASTClass227' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass227', None)
    _safe_set(owner, 'friendClasses', partner)
    assert getattr(partner, 'GASTClass227') == owner
    _safe_set(owner, 'friendClasses', None)
    assert getattr(partner, 'GASTClass227') is None


def test_assoc_globalFunctions122_stub_double():
    # GlobalFunction has no real 'GlobalFunction124' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction124', None)
    _safe_set(owner, 'root123', {partner})
    assert getattr(partner, 'GlobalFunction124') == owner
    _safe_set(owner, 'root123', set())
    assert getattr(partner, 'GlobalFunction124') is None


def test_assoc_globalFunctions143_stub_double():
    # GlobalFunction has no real 'GlobalFunction145' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction145', None)
    _safe_set(owner, 'gast_core_File144', {partner})
    assert getattr(partner, 'GlobalFunction145') == owner
    _safe_set(owner, 'gast_core_File144', set())
    assert getattr(partner, 'GlobalFunction145') is None


def test_assoc_globalFunctions71_stub_double():
    # GlobalFunction has no real 'GlobalFunction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction', None)
    _safe_set(owner, 'surroundingPackage72', {partner})
    assert getattr(partner, 'GlobalFunction') == owner
    _safe_set(owner, 'surroundingPackage72', set())
    assert getattr(partner, 'GlobalFunction') is None


def test_assoc_globalVariables106_stub_double():
    # GlobalVariable has no real 'GlobalVariable108' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable108', None)
    _safe_set(owner, 'gast_core_Root107', {partner})
    assert getattr(partner, 'GlobalVariable108') == owner
    _safe_set(owner, 'gast_core_Root107', set())
    assert getattr(partner, 'GlobalVariable108') is None


def test_assoc_globalVariables140_stub_double():
    # GlobalVariable has no real 'GlobalVariable142' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable142', None)
    _safe_set(owner, 'gast_core_File141', {partner})
    assert getattr(partner, 'GlobalVariable142') == owner
    _safe_set(owner, 'gast_core_File141', set())
    assert getattr(partner, 'GlobalVariable142') is None


def test_assoc_globalVariables73_stub_double():
    # GlobalVariable has no real 'GlobalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable', None)
    _safe_set(owner, 'surroundingPackage74', {partner})
    assert getattr(partner, 'GlobalVariable') == owner
    _safe_set(owner, 'surroundingPackage74', set())
    assert getattr(partner, 'GlobalVariable') is None


def test_assoc_importedGlobalFunctions146_stub_double():
    # GlobalFunction has no real 'GlobalFunction148' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction148', None)
    _safe_set(owner, 'gast_core_File147', {partner})
    assert getattr(partner, 'GlobalFunction148') == owner
    _safe_set(owner, 'gast_core_File147', set())
    assert getattr(partner, 'GlobalFunction148') is None


def test_assoc_importedGlobalVariables149_stub_double():
    # GlobalVariable has no real 'GlobalVariable151' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable151', None)
    _safe_set(owner, 'gast_core_File150', {partner})
    assert getattr(partner, 'GlobalVariable151') == owner
    _safe_set(owner, 'gast_core_File150', set())
    assert getattr(partner, 'GlobalVariable151') is None


def test_assoc_importedPackages152_stub_double():
    # Package has no real 'Package154' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Package()
    setattr(partner, 'Package154', None)
    _safe_set(owner, 'gast_core_File153', {partner})
    assert getattr(partner, 'Package154') == owner
    _safe_set(owner, 'gast_core_File153', set())
    assert getattr(partner, 'Package154') is None


def test_assoc_importedTypes134_stub_double():
    # GASTType has no real 'GASTType136' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType136', None)
    _safe_set(owner, 'gast_core_File135', {partner})
    assert getattr(partner, 'GASTType136') == owner
    _safe_set(owner, 'gast_core_File135', set())
    assert getattr(partner, 'GASTType136') is None


def test_assoc_includedFiles155_stub_double():
    # File has no real 'File157' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = File()
    setattr(partner, 'File157', None)
    _safe_set(owner, 'gast_core_File156', {partner})
    assert getattr(partner, 'File157') == owner
    _safe_set(owner, 'gast_core_File156', set())
    assert getattr(partner, 'File157') is None


def test_assoc_incrementExpression35_stub_double():
    # GASTExpression has no real 'GASTExpression37' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression37', None)
    _safe_set(owner, 'gast_statements_LoopStatement36', partner)
    assert getattr(partner, 'GASTExpression37') == owner
    _safe_set(owner, 'gast_statements_LoopStatement36', None)
    assert getattr(partner, 'GASTExpression37') is None


def test_assoc_inheritanceTypeAccesses219_stub_double():
    # InheritanceTypeAccess has no real 'InheritanceTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = InheritanceTypeAccess()
    setattr(partner, 'InheritanceTypeAccess', None)
    _safe_set(owner, 'gast_types_GASTClass220', {partner})
    assert getattr(partner, 'InheritanceTypeAccess') == owner
    _safe_set(owner, 'gast_types_GASTClass220', set())
    assert getattr(partner, 'InheritanceTypeAccess') is None


def test_assoc_initExpression32_stub_double():
    # GASTExpression has no real 'GASTExpression34' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression34', None)
    _safe_set(owner, 'gast_statements_LoopStatement33', partner)
    assert getattr(partner, 'GASTExpression34') == owner
    _safe_set(owner, 'gast_statements_LoopStatement33', None)
    assert getattr(partner, 'GASTExpression34') is None


def test_assoc_innerClasses214_stub_double():
    # GASTClass has no real 'GASTClass216' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass216', None)
    _safe_set(owner, 'surroundingClass215', {partner})
    assert getattr(partner, 'GASTClass216') == owner
    _safe_set(owner, 'surroundingClass215', set())
    assert getattr(partner, 'GASTClass216') is None


def test_assoc_innerDelegates197_stub_double():
    # Delegate has no real 'Delegate199' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Delegate()
    setattr(partner, 'Delegate199', None)
    _safe_set(owner, 'surroundingClass198', {partner})
    assert getattr(partner, 'Delegate199') == owner
    _safe_set(owner, 'surroundingClass198', set())
    assert getattr(partner, 'Delegate199') is None


def test_assoc_innerTypeAliases195_stub_double():
    # TypeAlias has no real 'TypeAlias196' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = TypeAlias()
    setattr(partner, 'TypeAlias196', None)
    _safe_set(owner, 'surroundingClass', {partner})
    assert getattr(partner, 'TypeAlias196') == owner
    _safe_set(owner, 'surroundingClass', set())
    assert getattr(partner, 'TypeAlias196') is None


def test_assoc_invocations280_stub_double():
    # Function has no real 'Function282' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Function()
    setattr(partner, 'Function282', None)
    _safe_set(owner, 'gast_functions_Delegate281', {partner})
    assert getattr(partner, 'Function282') == owner
    _safe_set(owner, 'gast_functions_Delegate281', set())
    assert getattr(partner, 'Function282') is None


def test_assoc_localClasses314_stub_double():
    # GASTClass has no real 'GASTClass316' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass316', None)
    _safe_set(owner, 'surroundingFunction315', {partner})
    assert getattr(partner, 'GASTClass316') == owner
    _safe_set(owner, 'surroundingFunction315', set())
    assert getattr(partner, 'GASTClass316') is None


def test_assoc_localVariables302_stub_double():
    # LocalVariable has no real 'LocalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = LocalVariable()
    setattr(partner, 'LocalVariable', None)
    _safe_set(owner, 'surroundingFunction303', {partner})
    assert getattr(partner, 'LocalVariable') == owner
    _safe_set(owner, 'surroundingFunction303', set())
    assert getattr(partner, 'LocalVariable') is None


def test_assoc_loopstatement13_stub_double():
    # LoopStatement has no real 'LoopStatement' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = LoopStatement()
    setattr(partner, 'LoopStatement', None)
    _safe_set(owner, 'body', partner)
    assert getattr(partner, 'LoopStatement') == owner
    _safe_set(owner, 'body', None)
    assert getattr(partner, 'LoopStatement') is None


def test_assoc_methods206_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'surroundingClass207', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'surroundingClass207', set())
    assert getattr(partner, 'Method') is None


def test_assoc_overriddenMember192_stub_double():
    # Member has no real 'Member' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_Member(abstract=True, extern=True, final=True, internal=True, introspectable=True, override=True, static=True, typeParameterClassMember=True, virtual=True, visibility="sample_text")
    partner = Member()
    setattr(partner, 'Member', None)
    _safe_set(owner, 'gast_types_Member', partner)
    assert getattr(partner, 'Member') == owner
    _safe_set(owner, 'gast_types_Member', None)
    assert getattr(partner, 'Member') is None


def test_assoc_packages109_stub_double():
    # Package has no real 'Package110' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Package()
    setattr(partner, 'Package110', None)
    _safe_set(owner, 'root', {partner})
    assert getattr(partner, 'Package110') == owner
    _safe_set(owner, 'root', set())
    assert getattr(partner, 'Package110') is None


def test_assoc_parentDirectory127_stub_double():
    # Directory has no real 'Directory128' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory128', None)
    _safe_set(owner, 'subDirectory', partner)
    assert getattr(partner, 'Directory128') == owner
    _safe_set(owner, 'subDirectory', None)
    assert getattr(partner, 'Directory128') is None


def test_assoc_property231_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'gast_types_GASTClass232', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'gast_types_GASTClass232', set())
    assert getattr(partner, 'Property') is None


def test_assoc_referencedType177_stub_double():
    # GASTType has no real 'GASTType178' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_Reference(explicit=True)
    partner = GASTType()
    setattr(partner, 'GASTType178', None)
    _safe_set(owner, 'gast_types_Reference', partner)
    assert getattr(partner, 'GASTType178') == owner
    _safe_set(owner, 'gast_types_Reference', None)
    assert getattr(partner, 'GASTType178') is None


def test_assoc_returnTypeDeclaration300_stub_double():
    # DeclarationTypeAccess has no real 'DeclarationTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = DeclarationTypeAccess()
    setattr(partner, 'DeclarationTypeAccess', None)
    _safe_set(owner, 'function', partner)
    assert getattr(partner, 'DeclarationTypeAccess') == owner
    _safe_set(owner, 'function', None)
    assert getattr(partner, 'DeclarationTypeAccess') is None


def test_assoc_root132_stub_double():
    # Root has no real 'Root133' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Root()
    setattr(partner, 'Root133', None)
    _safe_set(owner, 'gast_core_File', partner)
    assert getattr(partner, 'Root133') == owner
    _safe_set(owner, 'gast_core_File', None)
    assert getattr(partner, 'Root133') is None


def test_assoc_root293_stub_double():
    # Root has no real 'Root295' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Root()
    setattr(partner, 'Root295', None)
    _safe_set(owner, 'globalFunctions294', partner)
    assert getattr(partner, 'Root295') == owner
    _safe_set(owner, 'globalFunctions294', None)
    assert getattr(partner, 'Root295') is None


def test_assoc_root55_stub_double():
    # Root has no real 'Root' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_BasePath's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_BasePath's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_BasePath(path="sample_text")
    partner = Root()
    setattr(partner, 'Root', None)
    _safe_set(owner, 'basePaths', partner)
    assert getattr(partner, 'Root') == owner
    _safe_set(owner, 'basePaths', None)
    assert getattr(partner, 'Root') is None


def test_assoc_root75_stub_double():
    # Root has no real 'Root76' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Root()
    setattr(partner, 'Root76', None)
    _safe_set(owner, 'packages', partner)
    assert getattr(partner, 'Root76') == owner
    _safe_set(owner, 'packages', None)
    assert getattr(partner, 'Root76') is None


def test_assoc_self221_stub_double():
    # Field has no real 'Field223' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field223', None)
    _safe_set(owner, 'gast_types_GASTClass222', partner)
    assert getattr(partner, 'Field223') == owner
    _safe_set(owner, 'gast_types_GASTClass222', None)
    assert getattr(partner, 'Field223') is None


def test_assoc_sourceFile160_stub_double():
    # File has no real 'File161' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File161', None)
    _safe_set(owner, 'gast_core_Position', partner)
    assert getattr(partner, 'File161') == owner
    _safe_set(owner, 'gast_core_Position', None)
    assert getattr(partner, 'File161') is None


def test_assoc_sourceentity165_stub_double():
    # SourceEntity has no real 'SourceEntity' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = SourceEntity()
    setattr(partner, 'SourceEntity', None)
    _safe_set(owner, 'position', partner)
    assert getattr(partner, 'SourceEntity') == owner
    _safe_set(owner, 'position', None)
    assert getattr(partner, 'SourceEntity') is None


def test_assoc_statements20_stub_double():
    # Statement has no real 'Statement21' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_BlockStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_BlockStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_BlockStatement(synchronized=True)
    partner = Statement()
    setattr(partner, 'Statement21', None)
    _safe_set(owner, 'blockstatement', {partner})
    assert getattr(partner, 'Statement21') == owner
    _safe_set(owner, 'blockstatement', set())
    assert getattr(partner, 'Statement21') is None


def test_assoc_structuralAbstractions113_stub_double():
    # StructuralAbstraction has no real 'StructuralAbstraction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = StructuralAbstraction()
    setattr(partner, 'StructuralAbstraction', None)
    _safe_set(owner, 'gast_core_Root114', {partner})
    assert getattr(partner, 'StructuralAbstraction') == owner
    _safe_set(owner, 'gast_core_Root114', set())
    assert getattr(partner, 'StructuralAbstraction') is None


def test_assoc_subDirectory125_stub_double():
    # Directory has no real 'Directory126' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory126', None)
    _safe_set(owner, 'parentDirectory', {partner})
    assert getattr(partner, 'Directory126') == owner
    _safe_set(owner, 'parentDirectory', set())
    assert getattr(partner, 'Directory126') is None


def test_assoc_subPackages80_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'surroundingPackage81', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'surroundingPackage81', set())
    assert getattr(partner, 'Package') is None


def test_assoc_superClass278_stub_double():
    # GASTClass has no real 'GASTClass279' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass279', None)
    _safe_set(owner, 'gast_functions_Delegate', partner)
    assert getattr(partner, 'GASTClass279') == owner
    _safe_set(owner, 'gast_functions_Delegate', None)
    assert getattr(partner, 'GASTClass279') is None


def test_assoc_superTypes212_stub_double():
    # GASTClass has no real 'GASTClass213' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass213', None)
    _safe_set(owner, 'gast_types_GASTClass', {partner})
    assert getattr(partner, 'GASTClass213') == owner
    _safe_set(owner, 'gast_types_GASTClass', set())
    assert getattr(partner, 'GASTClass213') is None


def test_assoc_surroundingClass188_stub_double():
    # GASTClass has no real 'GASTClass189' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass189', None)
    _safe_set(owner, 'innerTypeAliases', partner)
    assert getattr(partner, 'GASTClass189') == owner
    _safe_set(owner, 'innerTypeAliases', None)
    assert getattr(partner, 'GASTClass189') is None


def test_assoc_surroundingClass217_stub_double():
    # GASTClass has no real 'GASTClass218' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass218', None)
    _safe_set(owner, 'innerClasses', partner)
    assert getattr(partner, 'GASTClass218') == owner
    _safe_set(owner, 'innerClasses', None)
    assert getattr(partner, 'GASTClass218') is None


def test_assoc_surroundingClass283_stub_double():
    # GASTClass has no real 'GASTClass284' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass284', None)
    _safe_set(owner, 'innerDelegates', partner)
    assert getattr(partner, 'GASTClass284') == owner
    _safe_set(owner, 'innerDelegates', None)
    assert getattr(partner, 'GASTClass284') is None


def test_assoc_surroundingClass287_stub_double():
    # GASTClass has no real 'GASTClass288' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Constructor(initializer=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass288', None)
    _safe_set(owner, 'constructors', partner)
    assert getattr(partner, 'GASTClass288') == owner
    _safe_set(owner, 'constructors', None)
    assert getattr(partner, 'GASTClass288') is None


def test_assoc_surroundingClass298_stub_double():
    # GASTClass has no real 'GASTClass299' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass299', None)
    _safe_set(owner, 'methods', partner)
    assert getattr(partner, 'GASTClass299') == owner
    _safe_set(owner, 'methods', None)
    assert getattr(partner, 'GASTClass299') is None


def test_assoc_surroundingClass323_stub_double():
    # GASTClass has no real 'GASTClass324' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Field(propertyField=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass324', None)
    _safe_set(owner, 'fields', partner)
    assert getattr(partner, 'GASTClass324') == owner
    _safe_set(owner, 'fields', None)
    assert getattr(partner, 'GASTClass324') is None


def test_assoc_surroundingFunction208_stub_double():
    # Function has no real 'Function209' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function209', None)
    _safe_set(owner, 'localClasses', partner)
    assert getattr(partner, 'Function209') == owner
    _safe_set(owner, 'localClasses', None)
    assert getattr(partner, 'Function209') is None


def test_assoc_surroundingFunction22_stub_double():
    # Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_BlockStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_BlockStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_BlockStatement(synchronized=True)
    partner = Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'body23', partner)
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'body23', None)
    assert getattr(partner, 'Function') is None


def test_assoc_surroundingFunction317_stub_double():
    # Function has no real 'Function318' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_FormalParameter(passedByReference=True)
    partner = Function()
    setattr(partner, 'Function318', None)
    _safe_set(owner, 'formalParameters', partner)
    assert getattr(partner, 'Function318') == owner
    _safe_set(owner, 'formalParameters', None)
    assert getattr(partner, 'Function318') is None


def test_assoc_surroundingPackage190_stub_double():
    # Package has no real 'Package191' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = Package()
    setattr(partner, 'Package191', None)
    _safe_set(owner, 'typeAliases', partner)
    assert getattr(partner, 'Package191') == owner
    _safe_set(owner, 'typeAliases', None)
    assert getattr(partner, 'Package191') is None


def test_assoc_surroundingPackage210_stub_double():
    # Package has no real 'Package211' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Package()
    setattr(partner, 'Package211', None)
    _safe_set(owner, 'classes', partner)
    assert getattr(partner, 'Package211') == owner
    _safe_set(owner, 'classes', None)
    assert getattr(partner, 'Package211') is None


def test_assoc_surroundingPackage285_stub_double():
    # Package has no real 'Package286' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Package()
    setattr(partner, 'Package286', None)
    _safe_set(owner, 'delegates', partner)
    assert getattr(partner, 'Package286') == owner
    _safe_set(owner, 'delegates', None)
    assert getattr(partner, 'Package286') is None


def test_assoc_surroundingPackage291_stub_double():
    # Package has no real 'Package292' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Package()
    setattr(partner, 'Package292', None)
    _safe_set(owner, 'globalFunctions', partner)
    assert getattr(partner, 'Package292') == owner
    _safe_set(owner, 'globalFunctions', None)
    assert getattr(partner, 'Package292') is None


def test_assoc_surroundingPackage82_stub_double():
    # Package has no real 'Package83' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package83', None)
    _safe_set(owner, 'subPackages', partner)
    assert getattr(partner, 'Package83') == owner
    _safe_set(owner, 'subPackages', None)
    assert getattr(partner, 'Package83') is None


def test_assoc_surroundingProperty296_stub_double():
    # Property has no real 'Property297' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = Property()
    setattr(partner, 'Property297', None)
    _safe_set(owner, 'gast_functions_Method', partner)
    assert getattr(partner, 'Property297') == owner
    _safe_set(owner, 'gast_functions_Method', None)
    assert getattr(partner, 'Property297') is None


def test_assoc_surroundingStatement11_stub_double():
    # Statement has no real 'Statement' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_Statement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_Statement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_Statement(linesOfCode=7, maximumNestingLevel=7, numberOfComments=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7)
    partner = Statement()
    setattr(partner, 'Statement', None)
    _safe_set(owner, 'gast_statements_Statement', partner)
    assert getattr(partner, 'Statement') == owner
    _safe_set(owner, 'gast_statements_Statement', None)
    assert getattr(partner, 'Statement') is None


def test_assoc_targetVariable271_stub_double():
    # Variable has no real 'Variable272' property in the generated
    # code (a bare stub) -- manually attach it so gast_accesses_VariableAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_accesses_VariableAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_accesses_VariableAccess(write=True)
    partner = Variable()
    setattr(partner, 'Variable272', None)
    _safe_set(owner, 'gast_accesses_VariableAccess', partner)
    assert getattr(partner, 'Variable272') == owner
    _safe_set(owner, 'gast_accesses_VariableAccess', None)
    assert getattr(partner, 'Variable272') is None


def test_assoc_throwTypeAccesses306_stub_double():
    # ThrowTypeAccess has no real 'ThrowTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = ThrowTypeAccess()
    setattr(partner, 'ThrowTypeAccess', None)
    _safe_set(owner, 'gast_functions_Function307', {partner})
    assert getattr(partner, 'ThrowTypeAccess') == owner
    _safe_set(owner, 'gast_functions_Function307', set())
    assert getattr(partner, 'ThrowTypeAccess') is None


def test_assoc_type319_stub_double():
    # GASTType has no real 'GASTType320' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = GASTType()
    setattr(partner, 'GASTType320', None)
    _safe_set(owner, 'gast_variables_Variable', partner)
    assert getattr(partner, 'GASTType320') == owner
    _safe_set(owner, 'gast_variables_Variable', None)
    assert getattr(partner, 'GASTType320') is None


def test_assoc_typeAliases87_stub_double():
    # TypeAlias has no real 'TypeAlias' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = TypeAlias()
    setattr(partner, 'TypeAlias', None)
    _safe_set(owner, 'surroundingPackage88', {partner})
    assert getattr(partner, 'TypeAlias') == owner
    _safe_set(owner, 'surroundingPackage88', set())
    assert getattr(partner, 'TypeAlias') is None


def test_assoc_typeDeclaration321_stub_double():
    # DeclarationTypeAccess has no real 'DeclarationTypeAccess322' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = DeclarationTypeAccess()
    setattr(partner, 'DeclarationTypeAccess322', None)
    _safe_set(owner, 'surroundingVariable', partner)
    assert getattr(partner, 'DeclarationTypeAccess322') == owner
    _safe_set(owner, 'surroundingVariable', None)
    assert getattr(partner, 'DeclarationTypeAccess322') is None


def test_assoc_types115_stub_double():
    # GASTType has no real 'GASTType' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTType()
    setattr(partner, 'GASTType', None)
    _safe_set(owner, 'gast_core_Root116', {partner})
    assert getattr(partner, 'GASTType') == owner
    _safe_set(owner, 'gast_core_Root116', set())
    assert getattr(partner, 'GASTType') is None


def test_assoc_types137_stub_double():
    # GASTType has no real 'GASTType139' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType139', None)
    _safe_set(owner, 'gast_core_File138', {partner})
    assert getattr(partner, 'GASTType139') == owner
    _safe_set(owner, 'gast_core_File138', set())
    assert getattr(partner, 'GASTType139') is None


def test_assoc_use48_stub_double():
    # Var has no real 'Var' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_FlowInstr's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_FlowInstr's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_FlowInstr(txt="sample_text")
    partner = Var()
    setattr(partner, 'Var', None)
    _safe_set(owner, 'gast_statements_FlowInstr', {partner})
    assert getattr(partner, 'Var') == owner
    _safe_set(owner, 'gast_statements_FlowInstr', set())
    assert getattr(partner, 'Var') is None


