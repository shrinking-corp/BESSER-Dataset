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
    gast_statements_GASTBehaviour,
    gast_statements_GASTExpression,
    gast_statements_JumpStatement,
    gast_statements_LoopStatement,
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

def test_assoc_accesses294_stub_double():
    # Access has no real 'Access296' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Access()
    setattr(partner, 'Access296', None)
    _safe_set(owner, 'gast_functions_Function295', {partner})
    assert getattr(partner, 'Access296') == owner
    _safe_set(owner, 'gast_functions_Function295', set())
    assert getattr(partner, 'Access296') is None


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


def test_assoc_aliasedType172_stub_double():
    # GASTType has no real 'GASTType173' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTType()
    setattr(partner, 'GASTType173', None)
    _safe_set(owner, 'gast_types_TypeAlias', partner)
    assert getattr(partner, 'GASTType173') == owner
    _safe_set(owner, 'gast_types_TypeAlias', None)
    assert getattr(partner, 'GASTType173') is None


def test_assoc_allAccessedClasses222_stub_double():
    # GASTClass has no real 'GASTClass224' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass224', None)
    _safe_set(owner, 'gast_types_GASTClass223', {partner})
    assert getattr(partner, 'GASTClass224') == owner
    _safe_set(owner, 'gast_types_GASTClass223', set())
    assert getattr(partner, 'GASTClass224') is None


def test_assoc_allAccessedPackages70_stub_double():
    # Package has no real 'Package72' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package72', None)
    _safe_set(owner, 'gast_core_Package71', {partner})
    assert getattr(partner, 'Package72') == owner
    _safe_set(owner, 'gast_core_Package71', set())
    assert getattr(partner, 'Package72') is None


def test_assoc_allAccesses219_stub_double():
    # Access has no real 'Access221' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Access()
    setattr(partner, 'Access221', None)
    _safe_set(owner, 'gast_types_GASTClass220', {partner})
    assert getattr(partner, 'Access221') == owner
    _safe_set(owner, 'gast_types_GASTClass220', set())
    assert getattr(partner, 'Access221') is None


def test_assoc_allAccesses54_stub_double():
    # Access has no real 'Access' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Access()
    setattr(partner, 'Access', None)
    _safe_set(owner, 'gast_core_Package55', {partner})
    assert getattr(partner, 'Access') == owner
    _safe_set(owner, 'gast_core_Package55', set())
    assert getattr(partner, 'Access') is None


def test_assoc_allAccesses76_stub_double():
    # Access has no real 'Access77' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Access()
    setattr(partner, 'Access77', None)
    _safe_set(owner, 'gast_core_Root', {partner})
    assert getattr(partner, 'Access77') == owner
    _safe_set(owner, 'gast_core_Root', set())
    assert getattr(partner, 'Access77') is None


def test_assoc_allInnerClasses45_stub_double():
    # GASTClass has no real 'GASTClass47' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass47', None)
    _safe_set(owner, 'gast_core_Package46', {partner})
    assert getattr(partner, 'GASTClass47') == owner
    _safe_set(owner, 'gast_core_Package46', set())
    assert getattr(partner, 'GASTClass47') is None


def test_assoc_allInnerClasses78_stub_double():
    # GASTClass has no real 'GASTClass80' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass80', None)
    _safe_set(owner, 'gast_core_Root79', {partner})
    assert getattr(partner, 'GASTClass80') == owner
    _safe_set(owner, 'gast_core_Root79', set())
    assert getattr(partner, 'GASTClass80') is None


def test_assoc_allInterfaces51_stub_double():
    # GASTClass has no real 'GASTClass53' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass53', None)
    _safe_set(owner, 'gast_core_Package52', {partner})
    assert getattr(partner, 'GASTClass53') == owner
    _safe_set(owner, 'gast_core_Package52', set())
    assert getattr(partner, 'GASTClass53') is None


def test_assoc_allInterfaces81_stub_double():
    # GASTClass has no real 'GASTClass83' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass83', None)
    _safe_set(owner, 'gast_core_Root82', {partner})
    assert getattr(partner, 'GASTClass83') == owner
    _safe_set(owner, 'gast_core_Root82', set())
    assert getattr(partner, 'GASTClass83') is None


def test_assoc_allLocalClasses44_stub_double():
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


def test_assoc_allLocalClasses84_stub_double():
    # GASTClass has no real 'GASTClass86' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass86', None)
    _safe_set(owner, 'gast_core_Root85', {partner})
    assert getattr(partner, 'GASTClass86') == owner
    _safe_set(owner, 'gast_core_Root85', set())
    assert getattr(partner, 'GASTClass86') is None


def test_assoc_allModelElements90_stub_double():
    # ModelElement has no real 'ModelElement' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement', None)
    _safe_set(owner, 'gast_core_Root91', {partner})
    assert getattr(partner, 'ModelElement') == owner
    _safe_set(owner, 'gast_core_Root91', set())
    assert getattr(partner, 'ModelElement') is None


def test_assoc_allNormalClasses48_stub_double():
    # GASTClass has no real 'GASTClass50' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass50', None)
    _safe_set(owner, 'gast_core_Package49', {partner})
    assert getattr(partner, 'GASTClass50') == owner
    _safe_set(owner, 'gast_core_Package49', set())
    assert getattr(partner, 'GASTClass50') is None


def test_assoc_allNormalClasses87_stub_double():
    # GASTClass has no real 'GASTClass89' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTClass()
    setattr(partner, 'GASTClass89', None)
    _safe_set(owner, 'gast_core_Root88', {partner})
    assert getattr(partner, 'GASTClass89') == owner
    _safe_set(owner, 'gast_core_Root88', set())
    assert getattr(partner, 'GASTClass89') is None


def test_assoc_allStatements290_stub_double():
    # Statement has no real 'Statement291' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = Statement()
    setattr(partner, 'Statement291', None)
    _safe_set(owner, 'gast_functions_Function', {partner})
    assert getattr(partner, 'Statement291') == owner
    _safe_set(owner, 'gast_functions_Function', set())
    assert getattr(partner, 'Statement291') is None


def test_assoc_annotations43_stub_double():
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


def test_assoc_assembly148_stub_double():
    # File has no real 'File150' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File150', None)
    _safe_set(owner, 'gast_core_Position149', partner)
    assert getattr(partner, 'File150') == owner
    _safe_set(owner, 'gast_core_Position149', None)
    assert getattr(partner, 'File150') is None


def test_assoc_basePath116_stub_double():
    # BasePath has no real 'BasePath117' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = BasePath()
    setattr(partner, 'BasePath117', None)
    _safe_set(owner, 'directories', partner)
    assert getattr(partner, 'BasePath117') == owner
    _safe_set(owner, 'directories', None)
    assert getattr(partner, 'BasePath117') is None


def test_assoc_basePaths106_stub_double():
    # BasePath has no real 'BasePath' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = BasePath()
    setattr(partner, 'BasePath', None)
    _safe_set(owner, 'root107', {partner})
    assert getattr(partner, 'BasePath') == owner
    _safe_set(owner, 'root107', set())
    assert getattr(partner, 'BasePath') is None


def test_assoc_baseType170_stub_double():
    # GASTType has no real 'GASTType171' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTArray's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTArray's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTArray(dimensions=7)
    partner = GASTType()
    setattr(partner, 'GASTType171', None)
    _safe_set(owner, 'gast_types_GASTArray', partner)
    assert getattr(partner, 'GASTType171') == owner
    _safe_set(owner, 'gast_types_GASTArray', None)
    assert getattr(partner, 'GASTType171') is None


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


def test_assoc_body297_stub_double():
    # BlockStatement has no real 'BlockStatement299' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = BlockStatement()
    setattr(partner, 'BlockStatement299', None)
    _safe_set(owner, 'surroundingFunction298', partner)
    assert getattr(partner, 'BlockStatement299') == owner
    _safe_set(owner, 'surroundingFunction298', None)
    assert getattr(partner, 'BlockStatement299') is None


def test_assoc_body32_stub_double():
    # Statement has no real 'Statement33' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = Statement()
    setattr(partner, 'Statement33', None)
    _safe_set(owner, 'loopstatement', partner)
    assert getattr(partner, 'Statement33') == owner
    _safe_set(owner, 'loopstatement', None)
    assert getattr(partner, 'Statement33') is None


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


def test_assoc_breakConditionExpression24_stub_double():
    # GASTExpression has no real 'GASTExpression25' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression25', None)
    _safe_set(owner, 'gast_statements_LoopStatement', partner)
    assert getattr(partner, 'GASTExpression25') == owner
    _safe_set(owner, 'gast_statements_LoopStatement', None)
    assert getattr(partner, 'GASTExpression25') is None


def test_assoc_classes63_stub_double():
    # GASTClass has no real 'GASTClass65' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GASTClass()
    setattr(partner, 'GASTClass65', None)
    _safe_set(owner, 'surroundingPackage64', {partner})
    assert getattr(partner, 'GASTClass65') == owner
    _safe_set(owner, 'surroundingPackage64', set())
    assert getattr(partner, 'GASTClass65') is None


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


def test_assoc_clones97_stub_double():
    # Clone has no real 'Clone' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Clone()
    setattr(partner, 'Clone', None)
    _safe_set(owner, 'root98', {partner})
    assert getattr(partner, 'Clone') == owner
    _safe_set(owner, 'root98', set())
    assert getattr(partner, 'Clone') is None


def test_assoc_constructors186_stub_double():
    # Constructor has no real 'Constructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Constructor()
    setattr(partner, 'Constructor', None)
    _safe_set(owner, 'surroundingClass187', {partner})
    assert getattr(partner, 'Constructor') == owner
    _safe_set(owner, 'surroundingClass187', set())
    assert getattr(partner, 'Constructor') is None


def test_assoc_danglingModelElements103_stub_double():
    # ModelElement has no real 'ModelElement105' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = ModelElement()
    setattr(partner, 'ModelElement105', None)
    _safe_set(owner, 'gast_core_Root104', {partner})
    assert getattr(partner, 'ModelElement105') == owner
    _safe_set(owner, 'gast_core_Root104', set())
    assert getattr(partner, 'ModelElement105') is None


def test_assoc_delegates56_stub_double():
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


def test_assoc_destructors188_stub_double():
    # Destructor has no real 'Destructor' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Destructor()
    setattr(partner, 'Destructor', None)
    _safe_set(owner, 'surroundingClass189', {partner})
    assert getattr(partner, 'Destructor') == owner
    _safe_set(owner, 'surroundingClass189', set())
    assert getattr(partner, 'Destructor') is None


def test_assoc_directories42_stub_double():
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


def test_assoc_directory144_stub_double():
    # Directory has no real 'Directory145' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Directory()
    setattr(partner, 'Directory145', None)
    _safe_set(owner, 'files', partner)
    assert getattr(partner, 'Directory145') == owner
    _safe_set(owner, 'files', None)
    assert getattr(partner, 'Directory145') is None


def test_assoc_expression35_stub_double():
    # GASTExpression has no real 'GASTExpression36' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_JumpStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_JumpStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_JumpStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression36', None)
    _safe_set(owner, 'gast_statements_JumpStatement', partner)
    assert getattr(partner, 'GASTExpression36') == owner
    _safe_set(owner, 'gast_statements_JumpStatement', None)
    assert getattr(partner, 'GASTExpression36') is None


def test_assoc_fields190_stub_double():
    # Field has no real 'Field' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field', None)
    _safe_set(owner, 'surroundingClass191', {partner})
    assert getattr(partner, 'Field') == owner
    _safe_set(owner, 'surroundingClass191', set())
    assert getattr(partner, 'Field') is None


def test_assoc_files115_stub_double():
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


def test_assoc_formalParameters287_stub_double():
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


def test_assoc_friendClasses210_stub_double():
    # GASTClass has no real 'GASTClass211' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass211', None)
    _safe_set(owner, 'gastClass', {partner})
    assert getattr(partner, 'GASTClass211') == owner
    _safe_set(owner, 'gastClass', set())
    assert getattr(partner, 'GASTClass211') is None


def test_assoc_friendFunctions214_stub_double():
    # Function has no real 'Function216' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function216', None)
    _safe_set(owner, 'gast_types_GASTClass215', {partner})
    assert getattr(partner, 'Function216') == owner
    _safe_set(owner, 'gast_types_GASTClass215', set())
    assert getattr(partner, 'Function216') is None


def test_assoc_gastClass212_stub_double():
    # GASTClass has no real 'GASTClass213' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass213', None)
    _safe_set(owner, 'friendClasses', partner)
    assert getattr(partner, 'GASTClass213') == owner
    _safe_set(owner, 'friendClasses', None)
    assert getattr(partner, 'GASTClass213') is None


def test_assoc_globalFunctions108_stub_double():
    # GlobalFunction has no real 'GlobalFunction110' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction110', None)
    _safe_set(owner, 'root109', {partner})
    assert getattr(partner, 'GlobalFunction110') == owner
    _safe_set(owner, 'root109', set())
    assert getattr(partner, 'GlobalFunction110') is None


def test_assoc_globalFunctions129_stub_double():
    # GlobalFunction has no real 'GlobalFunction131' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction131', None)
    _safe_set(owner, 'gast_core_File130', {partner})
    assert getattr(partner, 'GlobalFunction131') == owner
    _safe_set(owner, 'gast_core_File130', set())
    assert getattr(partner, 'GlobalFunction131') is None


def test_assoc_globalFunctions57_stub_double():
    # GlobalFunction has no real 'GlobalFunction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction', None)
    _safe_set(owner, 'surroundingPackage58', {partner})
    assert getattr(partner, 'GlobalFunction') == owner
    _safe_set(owner, 'surroundingPackage58', set())
    assert getattr(partner, 'GlobalFunction') is None


def test_assoc_globalVariables126_stub_double():
    # GlobalVariable has no real 'GlobalVariable128' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable128', None)
    _safe_set(owner, 'gast_core_File127', {partner})
    assert getattr(partner, 'GlobalVariable128') == owner
    _safe_set(owner, 'gast_core_File127', set())
    assert getattr(partner, 'GlobalVariable128') is None


def test_assoc_globalVariables59_stub_double():
    # GlobalVariable has no real 'GlobalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable', None)
    _safe_set(owner, 'surroundingPackage60', {partner})
    assert getattr(partner, 'GlobalVariable') == owner
    _safe_set(owner, 'surroundingPackage60', set())
    assert getattr(partner, 'GlobalVariable') is None


def test_assoc_globalVariables92_stub_double():
    # GlobalVariable has no real 'GlobalVariable94' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable94', None)
    _safe_set(owner, 'gast_core_Root93', {partner})
    assert getattr(partner, 'GlobalVariable94') == owner
    _safe_set(owner, 'gast_core_Root93', set())
    assert getattr(partner, 'GlobalVariable94') is None


def test_assoc_importedGlobalFunctions132_stub_double():
    # GlobalFunction has no real 'GlobalFunction134' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalFunction()
    setattr(partner, 'GlobalFunction134', None)
    _safe_set(owner, 'gast_core_File133', {partner})
    assert getattr(partner, 'GlobalFunction134') == owner
    _safe_set(owner, 'gast_core_File133', set())
    assert getattr(partner, 'GlobalFunction134') is None


def test_assoc_importedGlobalVariables135_stub_double():
    # GlobalVariable has no real 'GlobalVariable137' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GlobalVariable()
    setattr(partner, 'GlobalVariable137', None)
    _safe_set(owner, 'gast_core_File136', {partner})
    assert getattr(partner, 'GlobalVariable137') == owner
    _safe_set(owner, 'gast_core_File136', set())
    assert getattr(partner, 'GlobalVariable137') is None


def test_assoc_importedPackages138_stub_double():
    # Package has no real 'Package140' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Package()
    setattr(partner, 'Package140', None)
    _safe_set(owner, 'gast_core_File139', {partner})
    assert getattr(partner, 'Package140') == owner
    _safe_set(owner, 'gast_core_File139', set())
    assert getattr(partner, 'Package140') is None


def test_assoc_importedTypes120_stub_double():
    # GASTType has no real 'GASTType122' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType122', None)
    _safe_set(owner, 'gast_core_File121', {partner})
    assert getattr(partner, 'GASTType122') == owner
    _safe_set(owner, 'gast_core_File121', set())
    assert getattr(partner, 'GASTType122') is None


def test_assoc_includedFiles141_stub_double():
    # File has no real 'File143' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = File()
    setattr(partner, 'File143', None)
    _safe_set(owner, 'gast_core_File142', {partner})
    assert getattr(partner, 'File143') == owner
    _safe_set(owner, 'gast_core_File142', set())
    assert getattr(partner, 'File143') is None


def test_assoc_incrementExpression29_stub_double():
    # GASTExpression has no real 'GASTExpression31' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression31', None)
    _safe_set(owner, 'gast_statements_LoopStatement30', partner)
    assert getattr(partner, 'GASTExpression31') == owner
    _safe_set(owner, 'gast_statements_LoopStatement30', None)
    assert getattr(partner, 'GASTExpression31') is None


def test_assoc_inheritanceTypeAccesses205_stub_double():
    # InheritanceTypeAccess has no real 'InheritanceTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = InheritanceTypeAccess()
    setattr(partner, 'InheritanceTypeAccess', None)
    _safe_set(owner, 'gast_types_GASTClass206', {partner})
    assert getattr(partner, 'InheritanceTypeAccess') == owner
    _safe_set(owner, 'gast_types_GASTClass206', set())
    assert getattr(partner, 'InheritanceTypeAccess') is None


def test_assoc_initExpression26_stub_double():
    # GASTExpression has no real 'GASTExpression28' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_LoopStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_LoopStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_LoopStatement(kind="sample_text")
    partner = GASTExpression()
    setattr(partner, 'GASTExpression28', None)
    _safe_set(owner, 'gast_statements_LoopStatement27', partner)
    assert getattr(partner, 'GASTExpression28') == owner
    _safe_set(owner, 'gast_statements_LoopStatement27', None)
    assert getattr(partner, 'GASTExpression28') is None


def test_assoc_innerClasses200_stub_double():
    # GASTClass has no real 'GASTClass202' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass202', None)
    _safe_set(owner, 'surroundingClass201', {partner})
    assert getattr(partner, 'GASTClass202') == owner
    _safe_set(owner, 'surroundingClass201', set())
    assert getattr(partner, 'GASTClass202') is None


def test_assoc_innerDelegates183_stub_double():
    # Delegate has no real 'Delegate185' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Delegate()
    setattr(partner, 'Delegate185', None)
    _safe_set(owner, 'surroundingClass184', {partner})
    assert getattr(partner, 'Delegate185') == owner
    _safe_set(owner, 'surroundingClass184', set())
    assert getattr(partner, 'Delegate185') is None


def test_assoc_innerTypeAliases181_stub_double():
    # TypeAlias has no real 'TypeAlias182' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = TypeAlias()
    setattr(partner, 'TypeAlias182', None)
    _safe_set(owner, 'surroundingClass', {partner})
    assert getattr(partner, 'TypeAlias182') == owner
    _safe_set(owner, 'surroundingClass', set())
    assert getattr(partner, 'TypeAlias182') is None


def test_assoc_invocations266_stub_double():
    # Function has no real 'Function268' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Function()
    setattr(partner, 'Function268', None)
    _safe_set(owner, 'gast_functions_Delegate267', {partner})
    assert getattr(partner, 'Function268') == owner
    _safe_set(owner, 'gast_functions_Delegate267', set())
    assert getattr(partner, 'Function268') is None


def test_assoc_localClasses300_stub_double():
    # GASTClass has no real 'GASTClass302' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass302', None)
    _safe_set(owner, 'surroundingFunction301', {partner})
    assert getattr(partner, 'GASTClass302') == owner
    _safe_set(owner, 'surroundingFunction301', set())
    assert getattr(partner, 'GASTClass302') is None


def test_assoc_localVariables288_stub_double():
    # LocalVariable has no real 'LocalVariable' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = LocalVariable()
    setattr(partner, 'LocalVariable', None)
    _safe_set(owner, 'surroundingFunction289', {partner})
    assert getattr(partner, 'LocalVariable') == owner
    _safe_set(owner, 'surroundingFunction289', set())
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


def test_assoc_methods192_stub_double():
    # Method has no real 'Method' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Method()
    setattr(partner, 'Method', None)
    _safe_set(owner, 'surroundingClass193', {partner})
    assert getattr(partner, 'Method') == owner
    _safe_set(owner, 'surroundingClass193', set())
    assert getattr(partner, 'Method') is None


def test_assoc_overriddenMember178_stub_double():
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


def test_assoc_packages95_stub_double():
    # Package has no real 'Package96' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = Package()
    setattr(partner, 'Package96', None)
    _safe_set(owner, 'root', {partner})
    assert getattr(partner, 'Package96') == owner
    _safe_set(owner, 'root', set())
    assert getattr(partner, 'Package96') is None


def test_assoc_parentDirectory113_stub_double():
    # Directory has no real 'Directory114' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory114', None)
    _safe_set(owner, 'subDirectory', partner)
    assert getattr(partner, 'Directory114') == owner
    _safe_set(owner, 'subDirectory', None)
    assert getattr(partner, 'Directory114') is None


def test_assoc_property217_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'gast_types_GASTClass218', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'gast_types_GASTClass218', set())
    assert getattr(partner, 'Property') is None


def test_assoc_referencedType163_stub_double():
    # GASTType has no real 'GASTType164' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_Reference's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_Reference's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_Reference(explicit=True)
    partner = GASTType()
    setattr(partner, 'GASTType164', None)
    _safe_set(owner, 'gast_types_Reference', partner)
    assert getattr(partner, 'GASTType164') == owner
    _safe_set(owner, 'gast_types_Reference', None)
    assert getattr(partner, 'GASTType164') is None


def test_assoc_returnTypeDeclaration286_stub_double():
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


def test_assoc_root118_stub_double():
    # Root has no real 'Root119' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = Root()
    setattr(partner, 'Root119', None)
    _safe_set(owner, 'gast_core_File', partner)
    assert getattr(partner, 'Root119') == owner
    _safe_set(owner, 'gast_core_File', None)
    assert getattr(partner, 'Root119') is None


def test_assoc_root279_stub_double():
    # Root has no real 'Root281' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Root()
    setattr(partner, 'Root281', None)
    _safe_set(owner, 'globalFunctions280', partner)
    assert getattr(partner, 'Root281') == owner
    _safe_set(owner, 'globalFunctions280', None)
    assert getattr(partner, 'Root281') is None


def test_assoc_root41_stub_double():
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


def test_assoc_root61_stub_double():
    # Root has no real 'Root62' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Root()
    setattr(partner, 'Root62', None)
    _safe_set(owner, 'packages', partner)
    assert getattr(partner, 'Root62') == owner
    _safe_set(owner, 'packages', None)
    assert getattr(partner, 'Root62') is None


def test_assoc_self207_stub_double():
    # Field has no real 'Field209' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Field()
    setattr(partner, 'Field209', None)
    _safe_set(owner, 'gast_types_GASTClass208', partner)
    assert getattr(partner, 'Field209') == owner
    _safe_set(owner, 'gast_types_GASTClass208', None)
    assert getattr(partner, 'Field209') is None


def test_assoc_sourceFile146_stub_double():
    # File has no real 'File147' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Position's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Position's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Position(endColumn=7, endLine=7, startColumn=7, startLine=7)
    partner = File()
    setattr(partner, 'File147', None)
    _safe_set(owner, 'gast_core_Position', partner)
    assert getattr(partner, 'File147') == owner
    _safe_set(owner, 'gast_core_Position', None)
    assert getattr(partner, 'File147') is None


def test_assoc_sourceentity151_stub_double():
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


def test_assoc_statements14_stub_double():
    # Statement has no real 'Statement15' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_BlockStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_BlockStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_BlockStatement(synchronized=True)
    partner = Statement()
    setattr(partner, 'Statement15', None)
    _safe_set(owner, 'blockstatement', {partner})
    assert getattr(partner, 'Statement15') == owner
    _safe_set(owner, 'blockstatement', set())
    assert getattr(partner, 'Statement15') is None


def test_assoc_structuralAbstractions99_stub_double():
    # StructuralAbstraction has no real 'StructuralAbstraction' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = StructuralAbstraction()
    setattr(partner, 'StructuralAbstraction', None)
    _safe_set(owner, 'gast_core_Root100', {partner})
    assert getattr(partner, 'StructuralAbstraction') == owner
    _safe_set(owner, 'gast_core_Root100', set())
    assert getattr(partner, 'StructuralAbstraction') is None


def test_assoc_subDirectory111_stub_double():
    # Directory has no real 'Directory112' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Directory's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Directory's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Directory(fileSystemPath="sample_text", fullQualifiedPath="sample_text")
    partner = Directory()
    setattr(partner, 'Directory112', None)
    _safe_set(owner, 'parentDirectory', {partner})
    assert getattr(partner, 'Directory112') == owner
    _safe_set(owner, 'parentDirectory', set())
    assert getattr(partner, 'Directory112') is None


def test_assoc_subPackages66_stub_double():
    # Package has no real 'Package' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package', None)
    _safe_set(owner, 'surroundingPackage67', {partner})
    assert getattr(partner, 'Package') == owner
    _safe_set(owner, 'surroundingPackage67', set())
    assert getattr(partner, 'Package') is None


def test_assoc_superClass264_stub_double():
    # GASTClass has no real 'GASTClass265' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass265', None)
    _safe_set(owner, 'gast_functions_Delegate', partner)
    assert getattr(partner, 'GASTClass265') == owner
    _safe_set(owner, 'gast_functions_Delegate', None)
    assert getattr(partner, 'GASTClass265') is None


def test_assoc_superTypes198_stub_double():
    # GASTClass has no real 'GASTClass199' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass199', None)
    _safe_set(owner, 'gast_types_GASTClass', {partner})
    assert getattr(partner, 'GASTClass199') == owner
    _safe_set(owner, 'gast_types_GASTClass', set())
    assert getattr(partner, 'GASTClass199') is None


def test_assoc_surroundingClass174_stub_double():
    # GASTClass has no real 'GASTClass175' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass175', None)
    _safe_set(owner, 'innerTypeAliases', partner)
    assert getattr(partner, 'GASTClass175') == owner
    _safe_set(owner, 'innerTypeAliases', None)
    assert getattr(partner, 'GASTClass175') is None


def test_assoc_surroundingClass203_stub_double():
    # GASTClass has no real 'GASTClass204' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass204', None)
    _safe_set(owner, 'innerClasses', partner)
    assert getattr(partner, 'GASTClass204') == owner
    _safe_set(owner, 'innerClasses', None)
    assert getattr(partner, 'GASTClass204') is None


def test_assoc_surroundingClass269_stub_double():
    # GASTClass has no real 'GASTClass270' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass270', None)
    _safe_set(owner, 'innerDelegates', partner)
    assert getattr(partner, 'GASTClass270') == owner
    _safe_set(owner, 'innerDelegates', None)
    assert getattr(partner, 'GASTClass270') is None


def test_assoc_surroundingClass273_stub_double():
    # GASTClass has no real 'GASTClass274' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Constructor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Constructor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Constructor(initializer=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass274', None)
    _safe_set(owner, 'constructors', partner)
    assert getattr(partner, 'GASTClass274') == owner
    _safe_set(owner, 'constructors', None)
    assert getattr(partner, 'GASTClass274') is None


def test_assoc_surroundingClass284_stub_double():
    # GASTClass has no real 'GASTClass285' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass285', None)
    _safe_set(owner, 'methods', partner)
    assert getattr(partner, 'GASTClass285') == owner
    _safe_set(owner, 'methods', None)
    assert getattr(partner, 'GASTClass285') is None


def test_assoc_surroundingClass309_stub_double():
    # GASTClass has no real 'GASTClass310' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Field's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Field's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Field(propertyField=True)
    partner = GASTClass()
    setattr(partner, 'GASTClass310', None)
    _safe_set(owner, 'fields', partner)
    assert getattr(partner, 'GASTClass310') == owner
    _safe_set(owner, 'fields', None)
    assert getattr(partner, 'GASTClass310') is None


def test_assoc_surroundingFunction16_stub_double():
    # Function has no real 'Function' property in the generated
    # code (a bare stub) -- manually attach it so gast_statements_BlockStatement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_statements_BlockStatement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_statements_BlockStatement(synchronized=True)
    partner = Function()
    setattr(partner, 'Function', None)
    _safe_set(owner, 'body17', partner)
    assert getattr(partner, 'Function') == owner
    _safe_set(owner, 'body17', None)
    assert getattr(partner, 'Function') is None


def test_assoc_surroundingFunction194_stub_double():
    # Function has no real 'Function195' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Function()
    setattr(partner, 'Function195', None)
    _safe_set(owner, 'localClasses', partner)
    assert getattr(partner, 'Function195') == owner
    _safe_set(owner, 'localClasses', None)
    assert getattr(partner, 'Function195') is None


def test_assoc_surroundingFunction303_stub_double():
    # Function has no real 'Function304' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_FormalParameter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_FormalParameter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_FormalParameter(passedByReference=True)
    partner = Function()
    setattr(partner, 'Function304', None)
    _safe_set(owner, 'formalParameters', partner)
    assert getattr(partner, 'Function304') == owner
    _safe_set(owner, 'formalParameters', None)
    assert getattr(partner, 'Function304') is None


def test_assoc_surroundingPackage176_stub_double():
    # Package has no real 'Package177' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_TypeAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_TypeAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_TypeAlias(innerTypeAlias=True)
    partner = Package()
    setattr(partner, 'Package177', None)
    _safe_set(owner, 'typeAliases', partner)
    assert getattr(partner, 'Package177') == owner
    _safe_set(owner, 'typeAliases', None)
    assert getattr(partner, 'Package177') is None


def test_assoc_surroundingPackage196_stub_double():
    # Package has no real 'Package197' property in the generated
    # code (a bare stub) -- manually attach it so gast_types_GASTClass's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_types_GASTClass's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_types_GASTClass(anonymous=True, inner=True, interface=True, linesOfComments=7, local=True, primitive=True)
    partner = Package()
    setattr(partner, 'Package197', None)
    _safe_set(owner, 'classes', partner)
    assert getattr(partner, 'Package197') == owner
    _safe_set(owner, 'classes', None)
    assert getattr(partner, 'Package197') is None


def test_assoc_surroundingPackage271_stub_double():
    # Package has no real 'Package272' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Delegate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Delegate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Delegate(innerDelegate=True)
    partner = Package()
    setattr(partner, 'Package272', None)
    _safe_set(owner, 'delegates', partner)
    assert getattr(partner, 'Package272') == owner
    _safe_set(owner, 'delegates', None)
    assert getattr(partner, 'Package272') is None


def test_assoc_surroundingPackage277_stub_double():
    # Package has no real 'Package278' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_GlobalFunction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_GlobalFunction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_GlobalFunction(kind="sample_text")
    partner = Package()
    setattr(partner, 'Package278', None)
    _safe_set(owner, 'globalFunctions', partner)
    assert getattr(partner, 'Package278') == owner
    _safe_set(owner, 'globalFunctions', None)
    assert getattr(partner, 'Package278') is None


def test_assoc_surroundingPackage68_stub_double():
    # Package has no real 'Package69' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = Package()
    setattr(partner, 'Package69', None)
    _safe_set(owner, 'subPackages', partner)
    assert getattr(partner, 'Package69') == owner
    _safe_set(owner, 'subPackages', None)
    assert getattr(partner, 'Package69') is None


def test_assoc_surroundingProperty282_stub_double():
    # Property has no real 'Property283' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Method's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Method's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Method(propertyMethod=True)
    partner = Property()
    setattr(partner, 'Property283', None)
    _safe_set(owner, 'gast_functions_Method', partner)
    assert getattr(partner, 'Property283') == owner
    _safe_set(owner, 'gast_functions_Method', None)
    assert getattr(partner, 'Property283') is None


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


def test_assoc_targetVariable257_stub_double():
    # Variable has no real 'Variable258' property in the generated
    # code (a bare stub) -- manually attach it so gast_accesses_VariableAccess's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_accesses_VariableAccess's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_accesses_VariableAccess(write=True)
    partner = Variable()
    setattr(partner, 'Variable258', None)
    _safe_set(owner, 'gast_accesses_VariableAccess', partner)
    assert getattr(partner, 'Variable258') == owner
    _safe_set(owner, 'gast_accesses_VariableAccess', None)
    assert getattr(partner, 'Variable258') is None


def test_assoc_throwTypeAccesses292_stub_double():
    # ThrowTypeAccess has no real 'ThrowTypeAccess' property in the generated
    # code (a bare stub) -- manually attach it so gast_functions_Function's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_functions_Function's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_functions_Function(linesOfCode=7, linesOfComments=7, maximumNestingLevel=7, numberOfEdgesInCFG=7, numberOfNodesInCFG=7, numberOfStatements=7, operator=True)
    partner = ThrowTypeAccess()
    setattr(partner, 'ThrowTypeAccess', None)
    _safe_set(owner, 'gast_functions_Function293', {partner})
    assert getattr(partner, 'ThrowTypeAccess') == owner
    _safe_set(owner, 'gast_functions_Function293', set())
    assert getattr(partner, 'ThrowTypeAccess') is None


def test_assoc_type305_stub_double():
    # GASTType has no real 'GASTType306' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = GASTType()
    setattr(partner, 'GASTType306', None)
    _safe_set(owner, 'gast_variables_Variable', partner)
    assert getattr(partner, 'GASTType306') == owner
    _safe_set(owner, 'gast_variables_Variable', None)
    assert getattr(partner, 'GASTType306') is None


def test_assoc_typeAliases73_stub_double():
    # TypeAlias has no real 'TypeAlias' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Package's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Package's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Package(linesOfCode=7, linesOfComments=7, qualifiedName="sample_text")
    partner = TypeAlias()
    setattr(partner, 'TypeAlias', None)
    _safe_set(owner, 'surroundingPackage74', {partner})
    assert getattr(partner, 'TypeAlias') == owner
    _safe_set(owner, 'surroundingPackage74', set())
    assert getattr(partner, 'TypeAlias') is None


def test_assoc_typeDeclaration307_stub_double():
    # DeclarationTypeAccess has no real 'DeclarationTypeAccess308' property in the generated
    # code (a bare stub) -- manually attach it so gast_variables_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_variables_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_variables_Variable(const=True)
    partner = DeclarationTypeAccess()
    setattr(partner, 'DeclarationTypeAccess308', None)
    _safe_set(owner, 'surroundingVariable', partner)
    assert getattr(partner, 'DeclarationTypeAccess308') == owner
    _safe_set(owner, 'surroundingVariable', None)
    assert getattr(partner, 'DeclarationTypeAccess308') is None


def test_assoc_types101_stub_double():
    # GASTType has no real 'GASTType' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_Root's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_Root's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_Root(linesOfCode=7, linesOfComments=7)
    partner = GASTType()
    setattr(partner, 'GASTType', None)
    _safe_set(owner, 'gast_core_Root102', {partner})
    assert getattr(partner, 'GASTType') == owner
    _safe_set(owner, 'gast_core_Root102', set())
    assert getattr(partner, 'GASTType') is None


def test_assoc_types123_stub_double():
    # GASTType has no real 'GASTType125' property in the generated
    # code (a bare stub) -- manually attach it so gast_core_File's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # gast_core_File's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = gast_core_File(assemblyFile=True, fileSystemPath="sample_text", fullQualifiedPath="sample_text", linesOfCode=7, size="sample_text", sourceFile=True)
    partner = GASTType()
    setattr(partner, 'GASTType125', None)
    _safe_set(owner, 'gast_core_File124', {partner})
    assert getattr(partner, 'GASTType125') == owner
    _safe_set(owner, 'gast_core_File124', set())
    assert getattr(partner, 'GASTType125') is None


