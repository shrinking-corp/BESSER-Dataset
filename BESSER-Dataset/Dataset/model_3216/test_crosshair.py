from enum import Enum
from python_code import GlobalFunctionKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(GlobalFunctionKind.NORMAL, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(GlobalFunctionKind.NORMAL, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(GlobalFunctionKind.NORMAL, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(GlobalFunctionKind.NORMAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(GlobalFunctionKind.NORMAL, 'NORMAL') == GlobalFunctionKind.NORMAL

from enum import Enum
from python_code import JumpStatementKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(JumpStatementKind.JUMP, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(JumpStatementKind.JUMP, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(JumpStatementKind.JUMP, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(JumpStatementKind.JUMP, 0)

def test_Enum___new___2():
    assert Enum.__new__(JumpStatementKind.JUMP, 'JUMP') == JumpStatementKind.JUMP

from enum import Enum
from python_code import LoopStatementKind
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(LoopStatementKind.WHILE, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(LoopStatementKind.FOR, 0, '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(LoopStatementKind.FOR, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(LoopStatementKind.FOR, 0)

def test_Enum___new___2():
    assert Enum.__new__(LoopStatementKind.FOR, 'FOR') == LoopStatementKind.FOR

from enum import Enum
from python_code import Status
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Status.LIBRARY, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Status.NORMAL, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Status.LIBRARY, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Status.NORMAL, 0)

def test_Enum___new___2():
    assert Enum.__new__(Status.NORMAL, 'NORMAL') == Status.NORMAL

from enum import Enum
from python_code import Visibilities
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Visibilities.VISIBILITYPRIVAT, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Visibilities.VISIBILITYPUBLIC, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Visibilities.VISIBILITYPUBLIC, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Visibilities.VISIBILITYPRIVAT, 0)

def test_Enum___new___2():
    assert Enum.__new__(Visibilities.VISIBILITYPRIVAT, 'VISIBILITYPUBLIC') == Visibilities.VISIBILITYPUBLIC

from python_code import gast_accesses_InheritanceTypeAccess

def test_gast_accesses_InheritanceTypeAccess___init__():
    assert gast_accesses_InheritanceTypeAccess.__init__(gast_accesses_InheritanceTypeAccess(True), False) == None

from python_code import gast_accesses_SelfAccess

def test_gast_accesses_SelfAccess___init__():
    assert gast_accesses_SelfAccess.__init__(gast_accesses_SelfAccess(True), False) == None

from python_code import gast_accesses_ThrowTypeAccess

def test_gast_accesses_ThrowTypeAccess___init__():
    assert gast_accesses_ThrowTypeAccess.__init__(gast_accesses_ThrowTypeAccess(True), False) == None

from python_code import gast_annotations_Comment

def test_gast_annotations_Comment___init__():
    assert gast_annotations_Comment.__init__(gast_annotations_Comment(False, False, 0, ''), False, False, 0, '') == None

def test_gast_annotations_Comment_OCLtodo():
    assert gast_annotations_Comment.OCLtodo(gast_annotations_Comment(False, False, 0, ''), '', '') == None

from python_code import BasePath
from python_code import Directory
from python_code import gast_core_Directory

def test_gast_core_Directory___init__():
    assert gast_core_Directory.__init__(gast_core_Directory('', '', parentDirectory=set(), subDirectory=Directory(), directory=set(), directories=BasePath()), '', '', parentDirectory=set(), subDirectory=Directory(), directory=set(), directories=BasePath()) == None

from python_code import Directory
from python_code import Root
from python_code import gast_core_File

def test_gast_core_File___init__():
    assert gast_core_File.__init__(gast_core_File(False, True, 0, '', '', '', gast_core_File134=set(), gast_core_File137=set(), gast_core_File140=set(), gast_core_File143=set(), gast_core_File146=set(), gast_core_File149={<python_code.File object at 0x000001A808E0C450>}, files=Directory(), gast_core_File131=set(), gast_core_File=Root(), gast_core_File128=set()), False, True, 0, '\x00', '', '', gast_core_File134=set(), gast_core_File137=set(), gast_core_File140=set(), gast_core_File143=set(), gast_core_File146=set(), gast_core_File149=set(), files=Directory(), gast_core_File131=set(), gast_core_File=Root(), gast_core_File128=set()) == None

from python_code import gast_core_Identifier

def test_gast_core_Identifier___init__():
    assert gast_core_Identifier.__init__(gast_core_Identifier(''), '') == None

def test_gast_core_Identifier_idHasToBeUnique():
    assert gast_core_Identifier.idHasToBeUnique(gast_core_Identifier(''), 0, '\x00\x00') == None

from python_code import gast_core_ModelElement

def test_gast_core_ModelElement___init__():
    assert gast_core_ModelElement.__init__(gast_core_ModelElement('\x00\x00', 0, gast_core_ModelElement=set()), '', 0, gast_core_ModelElement=set()) == None

from python_code import Package
from python_code import Root
from python_code import gast_core_Package

def test_gast_core_Package___init__():
    assert gast_core_Package.__init__(gast_core_Package(0, 0, '', gast_core_Package=set(), gast_core_Package53=set(), gast_core_Package56=set(), gast_core_Package59=set(), gast_core_Package62=set(), surroundingPackage=set(), surroundingPackage65=set(), surroundingPackage67=set(), packages=Root(), surroundingPackage71=set(), subPackages=Package(), gast_core_Package78=set(), surroundingPackage81=set(), surroundingPackage74=set()), 0, 0, '', gast_core_Package=set(), gast_core_Package53=set(), gast_core_Package56=set(), gast_core_Package59={<python_code.gast_types_GASTUnion object at 0x0000017057726C10>}, gast_core_Package62=set(), surroundingPackage=set(), surroundingPackage65=set(), surroundingPackage67={<python_code.GlobalVariable object at 0x000001705686D490>}, packages=Root(), surroundingPackage71={<python_code.GASTClass object at 0x000001705686D0D0>}, subPackages=Package(), gast_core_Package78=set(), surroundingPackage81=set(), surroundingPackage74=set()) == None

from python_code import File
from python_code import SourceEntity
from python_code import gast_core_Position

def test_gast_core_Position_EitherAssemblyFileOrSourceFileSet():
    assert gast_core_Position.EitherAssemblyFileOrSourceFileSet(gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position156=File(), position=SourceEntity()), '', '') == None

from python_code import GASTClass
from python_code import gast_functions_Constructor

def test_gast_functions_Constructor___init__():
    assert gast_functions_Constructor.__init__(gast_functions_Constructor(False, constructors=GASTClass()), True, constructors=GASTClass()) == None

from python_code import BlockStatement
from python_code import DeclarationTypeAccess
from python_code import gast_functions_Function

def test_gast_functions_Function___init__():
    assert gast_functions_Function.__init__(gast_functions_Function(0, 0, 0, 0, 0, 0, False, function=DeclarationTypeAccess(), surroundingFunction296=set(), gast_functions_Function=set(), gast_functions_Function300=set(), gast_functions_Function302=set(), surroundingFunction305=BlockStatement(), surroundingFunction308=set(), surroundingFunction=set()), 0, 0, 0, 0, 0, 0, False, function=DeclarationTypeAccess(), surroundingFunction296=set(), gast_functions_Function=set(), gast_functions_Function300=set(), gast_functions_Function302=set(), surroundingFunction305=BlockStatement(), surroundingFunction308=set(), surroundingFunction={<python_code.FormalParameter object at 0x00000132C73BFD50>}) == None

from python_code import GASTClass
from python_code import Property
from python_code import gast_functions_Method

def test_gast_functions_Method___init__():
    assert gast_functions_Method.__init__(gast_functions_Method(False, gast_functions_Method=Property(), methods=GASTClass()), True, gast_functions_Method=Property(), methods=GASTClass()) == None

from python_code import gast_statements_Exit

def test_gast_statements_Exit___init__():
    assert gast_statements_Exit.__init__(gast_statements_Exit(''), '') == None

from python_code import BlockStatement
from python_code import Branch
from python_code import CloneInstance
from python_code import File
from python_code import LoopStatement
from python_code import SourceEntity
from python_code import Statement
from python_code import gast_core_Position
from python_code import gast_statements_ExceptionHandler
from python_code import gast_statements_Statement

def test_gast_statements_Statement___init__():
    assert gast_statements_Statement.__init__(gast_statements_Statement(0, 0, 0, 0, 0, 0, parentStatement=set(), statements=CloneInstance(), statements9=BlockStatement(), gast_statements_Statement=gast_statements_ExceptionHandler(), statement=Branch(), body=LoopStatement(), gast_statements_Statement15=set(), gast_statements_Statement18=set(), SourceEntity=gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position156=File(), position=SourceEntity())), 0, 0, 0, 0, 0, 0, parentStatement={<python_code.BaseAccess object at 0x000001D06B707A10>}, statements=CloneInstance(), statements9=BlockStatement(), gast_statements_Statement=Statement(), statement=Branch(), body=LoopStatement(), gast_statements_Statement15=set(), gast_statements_Statement18=set(), SourceEntity=gast_core_Position(0, 0, 0, 0, gast_core_Position=File(), gast_core_Position156=File(), position=SourceEntity())) == None

from python_code import GASTType
from python_code import gast_types_GASTArray

def test_gast_types_GASTArray___init__():
    assert gast_types_GASTArray.__init__(gast_types_GASTArray(0, gast_types_GASTArray=GASTType()), 0, gast_types_GASTArray=GASTType()) == None

from python_code import Field
from python_code import Function
from python_code import GASTClass
from python_code import Package
from python_code import gast_types_GASTClass

def test_gast_types_GASTClass___init__():
    assert gast_types_GASTClass.__init__(gast_types_GASTClass(0, False, True, False, True, False, surroundingClass=set(), surroundingClass194=set(), surroundingClass196=set(), surroundingClass198=set(), surroundingClass200=set(), localClasses=Function(), classes=Package(), gast_types_GASTClass=set(), surroundingClass208=set(), innerClasses=GASTClass(), surroundingClass191=set(), gast_types_GASTClass215=Field(), gastClass=set(), friendClasses=GASTClass(), gast_types_GASTClass213=set(), gast_types_GASTClass222=set(), gast_types_GASTClass225=set(), gast_types_GASTClass227=set(), gast_types_GASTClass230=set()), 0, False, True, False, False, False, surroundingClass=set(), surroundingClass194=set(), surroundingClass196={<python_code.Destructor object at 0x00000282A0E7FC10>}, surroundingClass198=set(), surroundingClass200={<python_code.Method object at 0x00000282A4B23290>}, localClasses=Function(), classes=Package(), gast_types_GASTClass=set(), surroundingClass208={<python_code.GASTClass object at 0x00000282A4B23990>}, innerClasses=GASTClass(), surroundingClass191={<python_code.Delegate object at 0x00000282A14FFA90>}, gast_types_GASTClass215=Field(), gastClass=set(), friendClasses=GASTClass(), gast_types_GASTClass213=set(), gast_types_GASTClass222=set(), gast_types_GASTClass225=set(), gast_types_GASTClass227=set(), gast_types_GASTClass230=set()) == None

from python_code import gast_types_GASTType

def test_gast_types_GASTType___init__():
    assert gast_types_GASTType.__init__(gast_types_GASTType('', False), '', False) == None
