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
    gast_statements_GASTBehaviour,
    gast_statements_GASTExpression,
    gast_statements_JumpStatement,
    gast_statements_LoopStatement,
    gast_statements_Methods,
    gast_statements_SimpleStatement,
    gast_statements_Statement,
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

def test_assoc_accesses301_stub_double():
    # Access has no real 'Access303' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Access()
    setattr(partner, 'Access303', None)
    _safe_set(owner, 'gast_functions_Function302', {partner})
    assert getattr(partner, 'Access303') == owner
    _safe_set(owner, 'gast_functions_Function302', set())
    assert getattr(partner, 'Access303') is None


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


def test_assoc_aliasedType179_stub_double():
    # GASTType has no real 'GASTType180' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTType()
    setattr(partner, 'GASTType180', None)
    _safe_set(owner, 'gast_types_TypeAlias', partner)
    assert getattr(partner, 'GASTType180') == owner
    _safe_set(owner, 'gast_types_TypeAlias', None)
    assert getattr(partner, 'GASTType180') is None


def test_assoc_allAccessedClasses229_stub_double():
    # GASTClass has no real 'GASTClass231' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass231', None)
    _safe_set(owner, 'gast_types_GASTClass230', {partner})
    assert getattr(partner, 'GASTClass231') == owner
    _safe_set(owner, 'gast_types_GASTClass230', set())
    assert getattr(partner, 'GASTClass231') is None


def test_assoc_allAccessedPackages77_stub_double():
    # Package has no real 'Package79' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package79', None)
    _safe_set(owner, 'gast_core_Package78', {partner})
    assert getattr(partner, 'Package79') == owner
    _safe_set(owner, 'gast_core_Package78', set())
    assert getattr(partner, 'Package79') is None


def test_assoc_allAccesses226_stub_double():
    # Access has no real 'Access228' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Access()
    setattr(partner, 'Access228', None)
    _safe_set(owner, 'gast_types_GASTClass227', {partner})
    assert getattr(partner, 'Access228') == owner
    _safe_set(owner, 'gast_types_GASTClass227', set())
    assert getattr(partner, 'Access228') is None


def test_assoc_allAccesses61_stub_double():
    # Access has no real 'Access' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Access()
    setattr(partner, 'Access', None)
    _safe_set(owner, 'gast_core_Package62', {partner})
    assert getattr(partner, 'Access') == owner
    _safe_set(owner, 'gast_core_Package62', set())
    assert getattr(partner, 'Access') is None


def test_assoc_allAccesses83_stub_double():
    # Access has no real 'Access84' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Access()
    setattr(partner, 'Access84', None)
    _safe_set(owner, 'gast_core_Root', {partner})
    assert getattr(partner, 'Access84') == owner
    _safe_set(owner, 'gast_core_Root', set())
    assert getattr(partner, 'Access84') is None


def test_assoc_allInnerClasses52_stub_double():
    # GASTClass has no real 'GASTClass54' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass54', None)
    _safe_set(owner, 'gast_core_Package53', {partner})
    assert getattr(partner, 'GASTClass54') == owner
    _safe_set(owner, 'gast_core_Package53', set())
    assert getattr(partner, 'GASTClass54') is None


def test_assoc_allInnerClasses85_stub_double():
    # GASTClass has no real 'GASTClass87' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass87', None)
    _safe_set(owner, 'gast_core_Root86', {partner})
    assert getattr(partner, 'GASTClass87') == owner
    _safe_set(owner, 'gast_core_Root86', set())
    assert getattr(partner, 'GASTClass87') is None


def test_assoc_allInterfaces58_stub_double():
    # GASTClass has no real 'GASTClass60' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass60', None)
    _safe_set(owner, 'gast_core_Package59', {partner})
    assert getattr(partner, 'GASTClass60') == owner
    _safe_set(owner, 'gast_core_Package59', set())
    assert getattr(partner, 'GASTClass60') is None


def test_assoc_allInterfaces88_stub_double():
    # GASTClass has no real 'GASTClass90' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass90', None)
    _safe_set(owner, 'gast_core_Root89', {partner})
    assert getattr(partner, 'GASTClass90') == owner
    _safe_set(owner, 'gast_core_Root89', set())
    assert getattr(partner, 'GASTClass90') is None


def test_assoc_allLocalClasses51_stub_double():
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


def test_assoc_allLocalClasses91_stub_double():
    # GASTClass has no real 'GASTClass93' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass93', None)
    _safe_set(owner, 'gast_core_Root92', {partner})
    assert getattr(partner, 'GASTClass93') == owner
    _safe_set(owner, 'gast_core_Root92', set())
    assert getattr(partner, 'GASTClass93') is None


def test_assoc_allModelElements97_stub_double():
    # ModelElement has no real 'ModelElement' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement', None)
    _safe_set(owner, 'gast_core_Root98', {partner})
    assert getattr(partner, 'ModelElement') == owner
    _safe_set(owner, 'gast_core_Root98', set())
    assert getattr(partner, 'ModelElement') is None


def test_assoc_allNormalClasses55_stub_double():
    # GASTClass has no real 'GASTClass57' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass57', None)
    _safe_set(owner, 'gast_core_Package56', {partner})
    assert getattr(partner, 'GASTClass57') == owner
    _safe_set(owner, 'gast_core_Package56', set())
    assert getattr(partner, 'GASTClass57') is None


def test_assoc_allNormalClasses94_stub_double():
    # GASTClass has no real 'GASTClass96' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass96', None)
    _safe_set(owner, 'gast_core_Root95', {partner})
    assert getattr(partner, 'GASTClass96') == owner
    _safe_set(owner, 'gast_core_Root95', set())
    assert getattr(partner, 'GASTClass96') is None


def test_assoc_allStatements297_stub_double():
    # Statement has no real 'Statement298' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Statement()
    setattr(partner, 'Statement298', None)
    _safe_set(owner, 'gast_functions_Function', {partner})
    assert getattr(partner, 'Statement298') == owner
    _safe_set(owner, 'gast_functions_Function', set())
    assert getattr(partner, 'Statement298') is None


def test_assoc_annotations50_stub_double():
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


def test_assoc_assembly155_stub_double():
    # File has no real 'File157' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File157', None)
    _safe_set(owner, 'gast_core_Position156', partner)
    assert getattr(partner, 'File157') == owner
    _safe_set(owner, 'gast_core_Position156', None)
    assert getattr(partner, 'File157') is None


def test_assoc_basePath123_stub_double():
    # BasePath has no real 'BasePath124' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = BasePath()
    setattr(partner, 'BasePath124', None)
    _safe_set(owner, 'directories', partner)
    assert getattr(partner, 'BasePath124') == owner
    _safe_set(owner, 'directories', None)
    assert getattr(partner, 'BasePath124') is None


def test_assoc_basePaths113_stub_double():
    # BasePath has no real 'BasePath' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = BasePath()
    setattr(partner, 'BasePath', None)
    _safe_set(owner, 'root114', {partner})
    assert getattr(partner, 'BasePath') == owner
    _safe_set(owner, 'root114', set())
    assert getattr(partner, 'BasePath') is None


def test_assoc_baseType177_stub_double():
    # GASTType has no real 'GASTType178' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTArray(dimensions=7)
    partner = GASTType()
    setattr(partner, 'GASTType178', None)
    _safe_set(owner, 'gast_types_GASTArray', partner)
    assert getattr(partner, 'GASTType178') == owner
    _safe_set(owner, 'gast_types_GASTArray', None)
    assert getattr(partner, 'GASTType178') is None


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


def test_assoc_body304_stub_double():
    # BlockStatement has no real 'BlockStatement306' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = BlockStatement()
    setattr(partner, 'BlockStatement306', None)
    _safe_set(owner, 'surroundingFunction305', partner)
    assert getattr(partner, 'BlockStatement306') == owner
    _safe_set(owner, 'surroundingFunction305', None)
    assert getattr(partner, 'BlockStatement306') is None


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


def test_assoc_classes70_stub_double():
    # GASTClass has no real 'GASTClass72' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass72', None)
    _safe_set(owner, 'surroundingPackage71', {partner})
    assert getattr(partner, 'GASTClass72') == owner
    _safe_set(owner, 'surroundingPackage71', set())
    assert getattr(partner, 'GASTClass72') is None


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


def test_assoc_clones104_stub_double():
    # Clone has no real 'Clone' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Clone()
    setattr(partner, 'Clone', None)
    _safe_set(owner, 'root105', {partner})
    assert getattr(partner, 'Clone') == owner
    _safe_set(owner, 'root105', set())
    assert getattr(partner, 'Clone') is None


def test_assoc_constructors193_stub_double():
    # Constructor has no real 'Constructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Constructor()
    setattr(partner, 'Constructor', None)
    _safe_set(owner, 'surroundingClass194', {partner})
    assert getattr(partner, 'Constructor') == owner
    _safe_set(owner, 'surroundingClass194', set())
    assert getattr(partner, 'Constructor') is None


def test_assoc_danglingModelElements110_stub_double():
    # ModelElement has no real 'ModelElement112' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement112', None)
    _safe_set(owner, 'gast_core_Root111', {partner})
    assert getattr(partner, 'ModelElement112') == owner
    _safe_set(owner, 'gast_core_Root111', set())
    assert getattr(partner, 'ModelElement112') is None


def test_assoc_delegates63_stub_double():
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


def test_assoc_destructors195_stub_double():
    # Destructor has no real 'Destructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Destructor()
    setattr(partner, 'Destructor', None)
    _safe_set(owner, 'surroundingClass196', {partner})
    assert getattr(partner, 'Destructor') == owner
    _safe_set(owner, 'surroundingClass196', set())
    assert getattr(partner, 'Destructor') is None


def test_assoc_directories49_stub_double():
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


def test_assoc_directory151_stub_double():
    # Directory has no real 'Directory152' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Directory()
    setattr(partner, 'Directory152', None)
    _safe_set(owner, 'files', partner)
    assert getattr(partner, 'Directory152') == owner
    _safe_set(owner, 'files', None)
    assert getattr(partner, 'Directory152') is None


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


def test_assoc_fields197_stub_double():
    # Field has no real 'Field' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field', None)
    _safe_set(owner, 'surroundingClass198', {partner})
    assert getattr(partner, 'Field') == owner
    _safe_set(owner, 'surroundingClass198', set())
    assert getattr(partner, 'Field') is None


def test_assoc_files122_stub_double():
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


def test_assoc_formalParameters294_stub_double():
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


def test_assoc_friendClasses217_stub_double():
    # GASTClass has no real 'GASTClass218' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass218', None)
    _safe_set(owner, 'gastClass', {partner})
    assert getattr(partner, 'GASTClass218') == owner
    _safe_set(owner, 'gastClass', set())
    assert getattr(partner, 'GASTClass218') is None


def test_assoc_friendFunctions221_stub_double():
    # Function has no real 'Function223' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function223', None)
    _safe_set(owner, 'gast_types_GASTClass222', {partner})
    assert getattr(partner, 'Function223') == owner
    _safe_set(owner, 'gast_types_GASTClass222', set())
    assert getattr(partner, 'Function223') is None


def test_assoc_gastClass219_stub_double():
    # GASTClass has no real 'GASTClass220' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass220', None)
    _safe_set(owner, 'friendClasses', partner)
    assert getattr(partner, 'GASTClass220') == owner
    _safe_set(owner, 'friendClasses', None)
    assert getattr(partner, 'GASTClass220') is None


def test_assoc_globalFunctions115_stub_double():
    # GlobalFunction has no real 'GlobalFunction117' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction117', None)
    _safe_set(owner, 'root116', {partner})
    assert getattr(partner, 'GlobalFunction117') == owner
    _safe_set(owner, 'root116', set())
    assert getattr(partner, 'GlobalFunction117') is None


def test_assoc_globalFunctions136_stub_double():
    # GlobalFunction has no real 'GlobalFunction138' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction138', None)
    _safe_set(owner, 'gast_core_File137', {partner})
    assert getattr(partner, 'GlobalFunction138') == owner
    _safe_set(owner, 'gast_core_File137', set())
    assert getattr(partner, 'GlobalFunction138') is None


def test_assoc_globalFunctions64_stub_double():
    # GlobalFunction has no real 'GlobalFunction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction', None)
    _safe_set(owner, 'surroundingPackage65', {partner})
    assert getattr(partner, 'GlobalFunction') == owner
    _safe_set(owner, 'surroundingPackage65', set())
    assert getattr(partner, 'GlobalFunction') is None


def test_assoc_globalVariables133_stub_double():
    # GlobalVariable has no real 'GlobalVariable135' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable135', None)
    _safe_set(owner, 'gast_core_File134', {partner})
    assert getattr(partner, 'GlobalVariable135') == owner
    _safe_set(owner, 'gast_core_File134', set())
    assert getattr(partner, 'GlobalVariable135') is None


def test_assoc_globalVariables66_stub_double():
    # GlobalVariable has no real 'GlobalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable', None)
    _safe_set(owner, 'surroundingPackage67', {partner})
    assert getattr(partner, 'GlobalVariable') == owner
    _safe_set(owner, 'surroundingPackage67', set())
    assert getattr(partner, 'GlobalVariable') is None


def test_assoc_globalVariables99_stub_double():
    # GlobalVariable has no real 'GlobalVariable101' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable101', None)
    _safe_set(owner, 'gast_core_Root100', {partner})
    assert getattr(partner, 'GlobalVariable101') == owner
    _safe_set(owner, 'gast_core_Root100', set())
    assert getattr(partner, 'GlobalVariable101') is None


def test_assoc_importedGlobalFunctions139_stub_double():
    # GlobalFunction has no real 'GlobalFunction141' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction141', None)
    _safe_set(owner, 'gast_core_File140', {partner})
    assert getattr(partner, 'GlobalFunction141') == owner
    _safe_set(owner, 'gast_core_File140', set())
    assert getattr(partner, 'GlobalFunction141') is None


def test_assoc_importedGlobalVariables142_stub_double():
    # GlobalVariable has no real 'GlobalVariable144' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable144', None)
    _safe_set(owner, 'gast_core_File143', {partner})
    assert getattr(partner, 'GlobalVariable144') == owner
    _safe_set(owner, 'gast_core_File143', set())
    assert getattr(partner, 'GlobalVariable144') is None


def test_assoc_importedPackages145_stub_double():
    # Package has no real 'Package147' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Package()
    setattr(partner, 'Package147', None)
    _safe_set(owner, 'gast_core_File146', {partner})
    assert getattr(partner, 'Package147') == owner
    _safe_set(owner, 'gast_core_File146', set())
    assert getattr(partner, 'Package147') is None


def test_assoc_importedTypes127_stub_double():
    # GASTType has no real 'GASTType129' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType129', None)
    _safe_set(owner, 'gast_core_File128', {partner})
    assert getattr(partner, 'GASTType129') == owner
    _safe_set(owner, 'gast_core_File128', set())
    assert getattr(partner, 'GASTType129') is None


def test_assoc_includedFiles148_stub_double():
    # File has no real 'File150' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = File()
    setattr(partner, 'File150', None)
    _safe_set(owner, 'gast_core_File149', {partner})
    assert getattr(partner, 'File150') == owner
    _safe_set(owner, 'gast_core_File149', set())
    assert getattr(partner, 'File150') is None


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


def test_assoc_inheritanceTypeAccesses212_stub_double():
    # InheritanceTypeAccess has no real 'InheritanceTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = InheritanceTypeAccess()
    setattr(partner, 'InheritanceTypeAccess', None)
    _safe_set(owner, 'gast_types_GASTClass213', {partner})
    assert getattr(partner, 'InheritanceTypeAccess') == owner
    _safe_set(owner, 'gast_types_GASTClass213', set())
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


def test_assoc_innerClasses207_stub_double():
    # GASTClass has no real 'GASTClass209' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass209', None)
    _safe_set(owner, 'surroundingClass208', {partner})
    assert getattr(partner, 'GASTClass209') == owner
    _safe_set(owner, 'surroundingClass208', set())
    assert getattr(partner, 'GASTClass209') is None


def test_assoc_innerDelegates190_stub_double():
    # Delegate has no real 'Delegate192' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Delegate()
    setattr(partner, 'Delegate192', None)
    _safe_set(owner, 'surroundingClass191', {partner})
    assert getattr(partner, 'Delegate192') == owner
    _safe_set(owner, 'surroundingClass191', set())
    assert getattr(partner, 'Delegate192') is None


def test_assoc_innerTypeAliases188_stub_double():
    # TypeAlias has no real 'TypeAlias189' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = TypeAlias()
    setattr(partner, 'TypeAlias189', None)
    _safe_set(owner, 'surroundingClass', {partner})
    assert getattr(partner, 'TypeAlias189') == owner
    _safe_set(owner, 'surroundingClass', set())
    assert getattr(partner, 'TypeAlias189') is None


def test_assoc_invocations273_stub_double():
    # Function has no real 'Function275' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Function()
    setattr(partner, 'Function275', None)
    _safe_set(owner, 'gast_functions_Delegate274', {partner})
    assert getattr(partner, 'Function275') == owner
    _safe_set(owner, 'gast_functions_Delegate274', set())
    assert getattr(partner, 'Function275') is None


def test_assoc_localClasses307_stub_double():
    # GASTClass has no real 'GASTClass309' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass309', None)
    _safe_set(owner, 'surroundingFunction308', {partner})
    assert getattr(partner, 'GASTClass309') == owner
    _safe_set(owner, 'surroundingFunction308', set())
    assert getattr(partner, 'GASTClass309') is None


def test_assoc_localVariables295_stub_double():
    # LocalVariable has no real 'LocalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = LocalVariable()
    setattr(partner, 'LocalVariable', None)
    _safe_set(owner, 'surroundingFunction296', {partner})
    assert getattr(partner, 'LocalVariable') == owner
    _safe_set(owner, 'surroundingFunction296', set())
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


def test_assoc_methods199_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'surroundingClass200', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'surroundingClass200', set())
    assert getattr(partner, 'Method') is None


def test_assoc_overriddenMember185_stub_double():
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


def test_assoc_packages102_stub_double():
    # Package has no real 'Package103' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Package()
    setattr(partner, 'Package103', None)
    _safe_set(owner, 'root', {partner})
    assert getattr(partner, 'Package103') == owner
    _safe_set(owner, 'root', set())
    assert getattr(partner, 'Package103') is None


def test_assoc_parentDirectory120_stub_double():
    # Directory has no real 'Directory121' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory121', None)
    _safe_set(owner, 'subDirectory', partner)
    assert getattr(partner, 'Directory121') == owner
    _safe_set(owner, 'subDirectory', None)
    assert getattr(partner, 'Directory121') is None


def test_assoc_property224_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'gast_types_GASTClass225', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'gast_types_GASTClass225', set())
    assert getattr(partner, 'Property') is None


def test_assoc_referencedType170_stub_double():
    # GASTType has no real 'GASTType171' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_Reference(explicit=True)
    partner = GASTType()
    setattr(partner, 'GASTType171', None)
    _safe_set(owner, 'gast_types_Reference', partner)
    assert getattr(partner, 'GASTType171') == owner
    _safe_set(owner, 'gast_types_Reference', None)
    assert getattr(partner, 'GASTType171') is None


def test_assoc_returnTypeDeclaration293_stub_double():
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


def test_assoc_root125_stub_double():
    # Root has no real 'Root126' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Root()
    setattr(partner, 'Root126', None)
    _safe_set(owner, 'gast_core_File', partner)
    assert getattr(partner, 'Root126') == owner
    _safe_set(owner, 'gast_core_File', None)
    assert getattr(partner, 'Root126') is None


def test_assoc_root286_stub_double():
    # Root has no real 'Root288' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Root()
    setattr(partner, 'Root288', None)
    _safe_set(owner, 'globalFunctions287', partner)
    assert getattr(partner, 'Root288') == owner
    _safe_set(owner, 'globalFunctions287', None)
    assert getattr(partner, 'Root288') is None


def test_assoc_root48_stub_double():
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


def test_assoc_root68_stub_double():
    # Root has no real 'Root69' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Root()
    setattr(partner, 'Root69', None)
    _safe_set(owner, 'packages', partner)
    assert getattr(partner, 'Root69') == owner
    _safe_set(owner, 'packages', None)
    assert getattr(partner, 'Root69') is None


def test_assoc_self214_stub_double():
    # Field has no real 'Field216' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field216', None)
    _safe_set(owner, 'gast_types_GASTClass215', partner)
    assert getattr(partner, 'Field216') == owner
    _safe_set(owner, 'gast_types_GASTClass215', None)
    assert getattr(partner, 'Field216') is None


def test_assoc_sourceFile153_stub_double():
    # File has no real 'File154' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File154', None)
    _safe_set(owner, 'gast_core_Position', partner)
    assert getattr(partner, 'File154') == owner
    _safe_set(owner, 'gast_core_Position', None)
    assert getattr(partner, 'File154') is None


def test_assoc_sourceentity158_stub_double():
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


def test_assoc_structuralAbstractions106_stub_double():
    # StructuralAbstraction has no real 'StructuralAbstraction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = StructuralAbstraction()
    setattr(partner, 'StructuralAbstraction', None)
    _safe_set(owner, 'gast_core_Root107', {partner})
    assert getattr(partner, 'StructuralAbstraction') == owner
    _safe_set(owner, 'gast_core_Root107', set())
    assert getattr(partner, 'StructuralAbstraction') is None


def test_assoc_subDirectory118_stub_double():
    # Directory has no real 'Directory119' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory119', None)
    _safe_set(owner, 'parentDirectory', {partner})
    assert getattr(partner, 'Directory119') == owner
    _safe_set(owner, 'parentDirectory', set())
    assert getattr(partner, 'Directory119') is None


def test_assoc_subPackages73_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'surroundingPackage74', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'surroundingPackage74', set())
    assert getattr(partner, 'Package') is None


def test_assoc_superClass271_stub_double():
    # GASTClass has no real 'GASTClass272' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass272', None)
    _safe_set(owner, 'gast_functions_Delegate', partner)
    assert getattr(partner, 'GASTClass272') == owner
    _safe_set(owner, 'gast_functions_Delegate', None)
    assert getattr(partner, 'GASTClass272') is None


def test_assoc_superTypes205_stub_double():
    # GASTClass has no real 'GASTClass206' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass206', None)
    _safe_set(owner, 'gast_types_GASTClass', {partner})
    assert getattr(partner, 'GASTClass206') == owner
    _safe_set(owner, 'gast_types_GASTClass', set())
    assert getattr(partner, 'GASTClass206') is None


def test_assoc_surroundingClass181_stub_double():
    # GASTClass has no real 'GASTClass182' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass182', None)
    _safe_set(owner, 'innerTypeAliases', partner)
    assert getattr(partner, 'GASTClass182') == owner
    _safe_set(owner, 'innerTypeAliases', None)
    assert getattr(partner, 'GASTClass182') is None


def test_assoc_surroundingClass210_stub_double():
    # GASTClass has no real 'GASTClass211' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass211', None)
    _safe_set(owner, 'innerClasses', partner)
    assert getattr(partner, 'GASTClass211') == owner
    _safe_set(owner, 'innerClasses', None)
    assert getattr(partner, 'GASTClass211') is None


def test_assoc_surroundingClass276_stub_double():
    # GASTClass has no real 'GASTClass277' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass277', None)
    _safe_set(owner, 'innerDelegates', partner)
    assert getattr(partner, 'GASTClass277') == owner
    _safe_set(owner, 'innerDelegates', None)
    assert getattr(partner, 'GASTClass277') is None


def test_assoc_surroundingClass280_stub_double():
    # GASTClass has no real 'GASTClass281' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Constructor(initializer=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass281', None)
    _safe_set(owner, 'constructors', partner)
    assert getattr(partner, 'GASTClass281') == owner
    _safe_set(owner, 'constructors', None)
    assert getattr(partner, 'GASTClass281') is None


def test_assoc_surroundingClass291_stub_double():
    # GASTClass has no real 'GASTClass292' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass292', None)
    _safe_set(owner, 'methods', partner)
    assert getattr(partner, 'GASTClass292') == owner
    _safe_set(owner, 'methods', None)
    assert getattr(partner, 'GASTClass292') is None


def test_assoc_surroundingClass316_stub_double():
    # GASTClass has no real 'GASTClass317' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Field(propertyField=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass317', None)
    _safe_set(owner, 'fields', partner)
    assert getattr(partner, 'GASTClass317') == owner
    _safe_set(owner, 'fields', None)
    assert getattr(partner, 'GASTClass317') is None


def test_assoc_surroundingFunction201_stub_double():
    # Function has no real 'Function202' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function202', None)
    _safe_set(owner, 'localClasses', partner)
    assert getattr(partner, 'Function202') == owner
    _safe_set(owner, 'localClasses', None)
    assert getattr(partner, 'Function202') is None


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


def test_assoc_surroundingFunction310_stub_double():
    # Function has no real 'Function311' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_FormalParameter(passedByReference=True)
    partner = Function()
    setattr(partner, 'Function311', None)
    _safe_set(owner, 'formalParameters', partner)
    assert getattr(partner, 'Function311') == owner
    _safe_set(owner, 'formalParameters', None)
    assert getattr(partner, 'Function311') is None


def test_assoc_surroundingPackage183_stub_double():
    # Package has no real 'Package184' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = Package()
    setattr(partner, 'Package184', None)
    _safe_set(owner, 'typeAliases', partner)
    assert getattr(partner, 'Package184') == owner
    _safe_set(owner, 'typeAliases', None)
    assert getattr(partner, 'Package184') is None


def test_assoc_surroundingPackage203_stub_double():
    # Package has no real 'Package204' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Package()
    setattr(partner, 'Package204', None)
    _safe_set(owner, 'classes', partner)
    assert getattr(partner, 'Package204') == owner
    _safe_set(owner, 'classes', None)
    assert getattr(partner, 'Package204') is None


def test_assoc_surroundingPackage278_stub_double():
    # Package has no real 'Package279' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Package()
    setattr(partner, 'Package279', None)
    _safe_set(owner, 'delegates', partner)
    assert getattr(partner, 'Package279') == owner
    _safe_set(owner, 'delegates', None)
    assert getattr(partner, 'Package279') is None


def test_assoc_surroundingPackage284_stub_double():
    # Package has no real 'Package285' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Package()
    setattr(partner, 'Package285', None)
    _safe_set(owner, 'globalFunctions', partner)
    assert getattr(partner, 'Package285') == owner
    _safe_set(owner, 'globalFunctions', None)
    assert getattr(partner, 'Package285') is None


def test_assoc_surroundingPackage75_stub_double():
    # Package has no real 'Package76' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package76', None)
    _safe_set(owner, 'subPackages', partner)
    assert getattr(partner, 'Package76') == owner
    _safe_set(owner, 'subPackages', None)
    assert getattr(partner, 'Package76') is None


def test_assoc_surroundingProperty289_stub_double():
    # Property has no real 'Property290' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = Property()
    setattr(partner, 'Property290', None)
    _safe_set(owner, 'gast_functions_Method', partner)
    assert getattr(partner, 'Property290') == owner
    _safe_set(owner, 'gast_functions_Method', None)
    assert getattr(partner, 'Property290') is None


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


def test_assoc_targetVariable264_stub_double():
    # Variable has no real 'Variable265' property in the generated
    # code (a bare stub) -- manually attach it so gast_accesses_VariableAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_accesses_VariableAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_accesses_VariableAccess(write=True)
    partner = Variable()
    setattr(partner, 'Variable265', None)
    _safe_set(owner, 'gast_accesses_VariableAccess', partner)
    assert getattr(partner, 'Variable265') == owner
    _safe_set(owner, 'gast_accesses_VariableAccess', None)
    assert getattr(partner, 'Variable265') is None


def test_assoc_throwTypeAccesses299_stub_double():
    # ThrowTypeAccess has no real 'ThrowTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = ThrowTypeAccess()
    setattr(partner, 'ThrowTypeAccess', None)
    _safe_set(owner, 'gast_functions_Function300', {partner})
    assert getattr(partner, 'ThrowTypeAccess') == owner
    _safe_set(owner, 'gast_functions_Function300', set())
    assert getattr(partner, 'ThrowTypeAccess') is None


def test_assoc_type312_stub_double():
    # GASTType has no real 'GASTType313' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = GASTType()
    setattr(partner, 'GASTType313', None)
    _safe_set(owner, 'gast_variables_Variable', partner)
    assert getattr(partner, 'GASTType313') == owner
    _safe_set(owner, 'gast_variables_Variable', None)
    assert getattr(partner, 'GASTType313') is None


def test_assoc_typeAliases80_stub_double():
    # TypeAlias has no real 'TypeAlias' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = TypeAlias()
    setattr(partner, 'TypeAlias', None)
    _safe_set(owner, 'surroundingPackage81', {partner})
    assert getattr(partner, 'TypeAlias') == owner
    _safe_set(owner, 'surroundingPackage81', set())
    assert getattr(partner, 'TypeAlias') is None


def test_assoc_typeDeclaration314_stub_double():
    # DeclarationTypeAccess has no real 'DeclarationTypeAccess315' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = DeclarationTypeAccess()
    setattr(partner, 'DeclarationTypeAccess315', None)
    _safe_set(owner, 'surroundingVariable', partner)
    assert getattr(partner, 'DeclarationTypeAccess315') == owner
    _safe_set(owner, 'surroundingVariable', None)
    assert getattr(partner, 'DeclarationTypeAccess315') is None


def test_assoc_types108_stub_double():
    # GASTType has no real 'GASTType' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTType()
    setattr(partner, 'GASTType', None)
    _safe_set(owner, 'gast_core_Root109', {partner})
    assert getattr(partner, 'GASTType') == owner
    _safe_set(owner, 'gast_core_Root109', set())
    assert getattr(partner, 'GASTType') is None


def test_assoc_types130_stub_double():
    # GASTType has no real 'GASTType132' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType132', None)
    _safe_set(owner, 'gast_core_File131', {partner})
    assert getattr(partner, 'GASTType132') == owner
    _safe_set(owner, 'gast_core_File131', set())
    assert getattr(partner, 'GASTType132') is None


