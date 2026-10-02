from enum import Enum
from python_code import AccessType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AccessType.write, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AccessType.write, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AccessType.write, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AccessType.read, 0)

def test_Enum___new___2():
    assert Enum.__new__(AccessType.read, 'read') == AccessType.read

from enum import Enum
from python_code import AttrGetParams
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AttrGetParams.name, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AttrGetParams.type, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AttrGetParams.type, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AttrGetParams.name, 0)

def test_Enum___new___2():
    assert Enum.__new__(AttrGetParams.name, 'name') == AttrGetParams.name

from enum import Enum
from python_code import AttrSetParams
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(AttrSetParams.value, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(AttrSetParams.value, '', '', '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(AttrSetParams.value, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(AttrSetParams.value, 0)

def test_Enum___new___2():
    assert Enum.__new__(AttrSetParams.value, 'value') == AttrSetParams.value

from enum import Enum
from python_code import ButtonType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(ButtonType.ok, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(ButtonType.ok, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(ButtonType.ok, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(ButtonType.ok, 0)

def test_Enum___new___2():
    assert Enum.__new__(ButtonType.ok, 'ok') == ButtonType.ok

from enum import Enum
from python_code import Color
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Color.azure, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Color.aqua, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Color.aqua, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Color.beige, 0)

def test_Enum___new___2():
    assert Enum.__new__(Color.aqua, 'aqua') == Color.aqua

from enum import Enum
from python_code import EventName
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(EventName.createmodel, 0, '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(EventName.deletemodel, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(EventName.createmodel, '', '', 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(EventName.beforecreaterelationinstance, 0)

def test_Enum___new___2():
    assert Enum.__new__(EventName.deletemodel, 'deletemodel') == EventName.deletemodel

from enum import Enum
from python_code import Font
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Font.couriernew, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Font.arial, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Font.georgia, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Font.arial, 0)

def test_Enum___new___2():
    assert Enum.__new__(Font.arial, 'arial') == Font.arial

from enum import Enum
from python_code import SimpleType
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(SimpleType.Double, '', '', 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(SimpleType.String, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(SimpleType.String, 0, '', 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(SimpleType.Int, 0)

def test_Enum___new___2():
    assert Enum.__new__(SimpleType.Int, 'Int') == SimpleType.Int

from python_code import mMDSL_AttributeGet
from python_code import mMDSL_AttributeOperation

def test_mMDSL_AttributeGet___init__():
    assert mMDSL_AttributeGet.__init__(mMDSL_AttributeGet('', mMDSL_AttributeGet=mMDSL_AttributeOperation()), '', mMDSL_AttributeGet=mMDSL_AttributeOperation()) == None

from python_code import mMDSL_Circle
from python_code import mMDSL_SVGCommand

def test_mMDSL_Circle___init__():
    assert mMDSL_Circle.__init__(mMDSL_Circle('', '', '\x00\x00', mMDSL_Circle=mMDSL_SVGCommand()), '', '', '', mMDSL_Circle=mMDSL_SVGCommand()) == None

from python_code import mMDSL_DirCreate
from python_code import mMDSL_DirOperation

def test_mMDSL_DirCreate___init__():
    assert mMDSL_DirCreate.__init__(mMDSL_DirCreate('', mMDSL_DirCreate=mMDSL_DirOperation()), '', mMDSL_DirCreate=mMDSL_DirOperation()) == None

from python_code import mMDSL_DirDelete
from python_code import mMDSL_DirOperation

def test_mMDSL_DirDelete___init__():
    assert mMDSL_DirDelete.__init__(mMDSL_DirDelete('', mMDSL_DirDelete=mMDSL_DirOperation()), '', mMDSL_DirDelete=mMDSL_DirOperation()) == None

from python_code import mMDSL_DirList
from python_code import mMDSL_DirOperation

def test_mMDSL_DirList___init__():
    assert mMDSL_DirList.__init__(mMDSL_DirList('', mMDSL_DirList=mMDSL_DirOperation()), '', mMDSL_DirList=mMDSL_DirOperation()) == None

from python_code import mMDSL_DirOperation
from python_code import mMDSL_DirSetWorking

def test_mMDSL_DirSetWorking___init__():
    assert mMDSL_DirSetWorking.__init__(mMDSL_DirSetWorking('', mMDSL_DirSetWorking=mMDSL_DirOperation()), '', mMDSL_DirSetWorking=mMDSL_DirOperation()) == None

from python_code import mMDSL_EditBox
from python_code import mMDSL_SimpleUI

def test_mMDSL_EditBox___init__():
    assert mMDSL_EditBox.__init__(mMDSL_EditBox('', '', '\x00\x00', mMDSL_EditBox=mMDSL_SimpleUI()), '', '', '', mMDSL_EditBox=mMDSL_SimpleUI()) == None

from python_code import mMDSL_Ellipse
from python_code import mMDSL_SVGCommand

def test_mMDSL_Ellipse___init__():
    assert mMDSL_Ellipse.__init__(mMDSL_Ellipse('\x00\x00', '', '', '', mMDSL_Ellipse=mMDSL_SVGCommand()), '', '', '', '', mMDSL_Ellipse=mMDSL_SVGCommand()) == None

from python_code import mMDSL_EnumType
from python_code import mMDSL_Enumeration
from python_code import mMDSL_Method

def test_mMDSL_Enumeration___init__():
    assert mMDSL_Enumeration.__init__(mMDSL_Enumeration('', '\x00', mMDSL_Enumeration=mMDSL_Method(), mMDSL_Enumeration97=mMDSL_EnumType()), '\x00\x00', '', mMDSL_Enumeration=mMDSL_Method(), mMDSL_Enumeration97=mMDSL_EnumType()) == None

from python_code import mMDSL_ErrorBox
from python_code import mMDSL_SimpleUI

def test_mMDSL_ErrorBox___init__():
    assert mMDSL_ErrorBox.__init__(mMDSL_ErrorBox('', '', '\x00\x00', mMDSL_ErrorBox=mMDSL_SimpleUI()), '', '', '', mMDSL_ErrorBox=mMDSL_SimpleUI()) == None

from python_code import mMDSL_FileCopy
from python_code import mMDSL_FileOperation

def test_mMDSL_FileCopy___init__():
    assert mMDSL_FileCopy.__init__(mMDSL_FileCopy('', '\x00', mMDSL_FileCopy=mMDSL_FileOperation()), '\x00\x00', '', mMDSL_FileCopy=mMDSL_FileOperation()) == None

from python_code import mMDSL_FileCreate
from python_code import mMDSL_FileOperation

def test_mMDSL_FileCreate___init__():
    assert mMDSL_FileCreate.__init__(mMDSL_FileCreate('', mMDSL_FileCreate=mMDSL_FileOperation()), '', mMDSL_FileCreate=mMDSL_FileOperation()) == None

from python_code import mMDSL_FileDelete
from python_code import mMDSL_FileOperation

def test_mMDSL_FileDelete___init__():
    assert mMDSL_FileDelete.__init__(mMDSL_FileDelete('', mMDSL_FileDelete=mMDSL_FileOperation()), '', mMDSL_FileDelete=mMDSL_FileOperation()) == None

from python_code import mMDSL_FileOperation
from python_code import mMDSL_FileRead

def test_mMDSL_FileRead___init__():
    assert mMDSL_FileRead.__init__(mMDSL_FileRead('', mMDSL_FileRead=mMDSL_FileOperation()), '', mMDSL_FileRead=mMDSL_FileOperation()) == None

from python_code import mMDSL_FileOperation
from python_code import mMDSL_FileWrite

def test_mMDSL_FileWrite___init__():
    assert mMDSL_FileWrite.__init__(mMDSL_FileWrite('', '', '\x00\x00', mMDSL_FileWrite=mMDSL_FileOperation()), '', '', '', mMDSL_FileWrite=mMDSL_FileOperation()) == None

from python_code import mMDSL_ForLoop
from python_code import mMDSL_LoopStatement

def test_mMDSL_ForLoop___init__():
    assert mMDSL_ForLoop.__init__(mMDSL_ForLoop(0, 0, 0, mMDSL_ForLoop=mMDSL_LoopStatement(), mMDSL_ForLoop255=set(), mMDSL_ForLoop258=set()), 0, 0, 0, mMDSL_ForLoop=mMDSL_LoopStatement(), mMDSL_ForLoop255=set(), mMDSL_ForLoop258=set()) == None

from python_code import mMDSL_InfoBox
from python_code import mMDSL_SimpleUI

def test_mMDSL_InfoBox___init__():
    assert mMDSL_InfoBox.__init__(mMDSL_InfoBox('', '\x00', mMDSL_InfoBox=mMDSL_SimpleUI()), '\x00\x00', '', mMDSL_InfoBox=mMDSL_SimpleUI()) == None

from python_code import mMDSL_ContextItem
from python_code import mMDSL_InsertContextItem
from python_code import mMDSL_RemoveContextItem

def test_mMDSL_InsertContextItem___init__():
    assert mMDSL_InsertContextItem.__init__(mMDSL_InsertContextItem('', '\x00', mMDSL_InsertContextItem=mMDSL_ContextItem(), mMDSL_InsertContextItem382=mMDSL_RemoveContextItem()), '\x00\x00', '', mMDSL_InsertContextItem=mMDSL_ContextItem(), mMDSL_InsertContextItem382=mMDSL_RemoveContextItem()) == None

from python_code import mMDSL_InsertMenuItem
from python_code import mMDSL_MenuItem
from python_code import mMDSL_RemoveMenuItem

def test_mMDSL_InsertMenuItem___init__():
    assert mMDSL_InsertMenuItem.__init__(mMDSL_InsertMenuItem('', '\x00', mMDSL_InsertMenuItem=mMDSL_MenuItem(), mMDSL_InsertMenuItem375=mMDSL_RemoveMenuItem()), '\x00\x00', '', mMDSL_InsertMenuItem=mMDSL_MenuItem(), mMDSL_InsertMenuItem375=mMDSL_RemoveMenuItem()) == None

from python_code import mMDSL_Line
from python_code import mMDSL_SVGCommand

def test_mMDSL_Line___init__():
    assert mMDSL_Line.__init__(mMDSL_Line('\x00\x00', '', '', '', mMDSL_Line=mMDSL_SVGCommand()), '', '', '', '', mMDSL_Line=mMDSL_SVGCommand()) == None

from python_code import mMDSL_MethodName
from python_code import mMDSL_Root

def test_mMDSL_MethodName___init__():
    assert mMDSL_MethodName.__init__(mMDSL_MethodName('', mMDSL_MethodName=mMDSL_Root()), '', mMDSL_MethodName=mMDSL_Root()) == None

from python_code import mMDSL_OperatorAdd

def test_mMDSL_OperatorAdd___init__():
    assert mMDSL_OperatorAdd.__init__(mMDSL_OperatorAdd('', '\x00'), '\x00\x00', '') == None

from python_code import mMDSL_OperatorAnd

def test_mMDSL_OperatorAnd___init__():
    assert mMDSL_OperatorAnd.__init__(mMDSL_OperatorAnd(''), '') == None

from python_code import mMDSL_OperatorCompare

def test_mMDSL_OperatorCompare___init__():
    assert mMDSL_OperatorCompare.__init__(mMDSL_OperatorCompare('\x00\x00', '', '', ''), '', '', '', '') == None

from python_code import mMDSL_OperatorEqual

def test_mMDSL_OperatorEqual___init__():
    assert mMDSL_OperatorEqual.__init__(mMDSL_OperatorEqual('', '\x00'), '\x00\x00', '') == None

from python_code import mMDSL_OperatorMultiply

def test_mMDSL_OperatorMultiply___init__():
    assert mMDSL_OperatorMultiply.__init__(mMDSL_OperatorMultiply('', '', '\x00\x00'), '', '', '') == None

from python_code import mMDSL_OperatorOr

def test_mMDSL_OperatorOr___init__():
    assert mMDSL_OperatorOr.__init__(mMDSL_OperatorOr(''), '') == None

from python_code import mMDSL_OperatorUnary

def test_mMDSL_OperatorUnary___init__():
    assert mMDSL_OperatorUnary.__init__(mMDSL_OperatorUnary(''), '') == None

from python_code import mMDSL_CurveTo
from python_code import mMDSL_EllipticalArc
from python_code import mMDSL_HorizontalLineTo
from python_code import mMDSL_LineTo
from python_code import mMDSL_MoveTo
from python_code import mMDSL_Path
from python_code import mMDSL_PathData
from python_code import mMDSL_QuadraticBezierCurve
from python_code import mMDSL_SmoothCurveTo
from python_code import mMDSL_SmoothQuadraticBezierCurveTo
from python_code import mMDSL_VerticalLineTo

def test_mMDSL_PathData___init__():
    assert mMDSL_PathData.__init__(mMDSL_PathData('', mMDSL_PathData=mMDSL_Path(), mMDSL_PathData166=mMDSL_MoveTo(), mMDSL_PathData168=mMDSL_LineTo(), mMDSL_PathData170=mMDSL_HorizontalLineTo(), mMDSL_PathData172=mMDSL_VerticalLineTo(), mMDSL_PathData174=mMDSL_CurveTo(), mMDSL_PathData176=mMDSL_SmoothCurveTo(), mMDSL_PathData178=mMDSL_QuadraticBezierCurve(), mMDSL_PathData180=mMDSL_SmoothQuadraticBezierCurveTo(), mMDSL_PathData182=mMDSL_EllipticalArc()), '', mMDSL_PathData=mMDSL_Path(), mMDSL_PathData166=mMDSL_MoveTo(), mMDSL_PathData168=mMDSL_LineTo(), mMDSL_PathData170=mMDSL_HorizontalLineTo(), mMDSL_PathData172=mMDSL_VerticalLineTo(), mMDSL_PathData174=mMDSL_CurveTo(), mMDSL_PathData176=mMDSL_SmoothCurveTo(), mMDSL_PathData178=mMDSL_QuadraticBezierCurve(), mMDSL_PathData180=mMDSL_SmoothQuadraticBezierCurveTo(), mMDSL_PathData182=mMDSL_EllipticalArc()) == None

from python_code import mMDSL_EllipticalArc
from python_code import mMDSL_PathParametersA

def test_mMDSL_PathParametersA___init__():
    assert mMDSL_PathParametersA.__init__(mMDSL_PathParametersA('', '', '', '', '', '', '', mMDSL_PathParametersA=mMDSL_EllipticalArc()), '', '\x00', '', '', '', '', '', mMDSL_PathParametersA=mMDSL_EllipticalArc()) == None

from python_code import mMDSL_CurveTo
from python_code import mMDSL_PathParametersC

def test_mMDSL_PathParametersC___init__():
    assert mMDSL_PathParametersC.__init__(mMDSL_PathParametersC('', '', '', '', '', '', mMDSL_PathParametersC=mMDSL_CurveTo()), '', '', '', '', '\x00', '', mMDSL_PathParametersC=mMDSL_CurveTo()) == None

from python_code import mMDSL_HorizontalLineTo
from python_code import mMDSL_PathParametersHV
from python_code import mMDSL_VerticalLineTo

def test_mMDSL_PathParametersHV___init__():
    assert mMDSL_PathParametersHV.__init__(mMDSL_PathParametersHV('', mMDSL_PathParametersHV=mMDSL_HorizontalLineTo(), mMDSL_PathParametersHV192=mMDSL_VerticalLineTo()), '', mMDSL_PathParametersHV=mMDSL_HorizontalLineTo(), mMDSL_PathParametersHV192=mMDSL_VerticalLineTo()) == None

from python_code import mMDSL_LineTo
from python_code import mMDSL_MoveTo
from python_code import mMDSL_PathParametersMLT
from python_code import mMDSL_SmoothQuadraticBezierCurveTo

def test_mMDSL_PathParametersMLT___init__():
    assert mMDSL_PathParametersMLT.__init__(mMDSL_PathParametersMLT('', '\x00', mMDSL_PathParametersMLT=mMDSL_MoveTo(), mMDSL_PathParametersMLT187=mMDSL_LineTo(), mMDSL_PathParametersMLT201=mMDSL_SmoothQuadraticBezierCurveTo()), '\x00\x00', '', mMDSL_PathParametersMLT=mMDSL_MoveTo(), mMDSL_PathParametersMLT187=mMDSL_LineTo(), mMDSL_PathParametersMLT201=mMDSL_SmoothQuadraticBezierCurveTo()) == None

from python_code import mMDSL_PathParametersQ
from python_code import mMDSL_QuadraticBezierCurve

def test_mMDSL_PathParametersQ___init__():
    assert mMDSL_PathParametersQ.__init__(mMDSL_PathParametersQ('\x00\x00', '', '', '', mMDSL_PathParametersQ=mMDSL_QuadraticBezierCurve()), '', '', '', '', mMDSL_PathParametersQ=mMDSL_QuadraticBezierCurve()) == None

from python_code import mMDSL_PathParametersS
from python_code import mMDSL_SmoothCurveTo

def test_mMDSL_PathParametersS___init__():
    assert mMDSL_PathParametersS.__init__(mMDSL_PathParametersS('\x00\x00', '', '', '', mMDSL_PathParametersS=mMDSL_SmoothCurveTo()), '', '', '', '', mMDSL_PathParametersS=mMDSL_SmoothCurveTo()) == None

from python_code import mMDSL_Points
from python_code import mMDSL_Polygon
from python_code import mMDSL_Polyline

def test_mMDSL_Points___init__():
    assert mMDSL_Points.__init__(mMDSL_Points('', '\x00', mMDSL_Points=mMDSL_Polyline(), mMDSL_Points158=mMDSL_Polygon()), '\x00\x00', '', mMDSL_Points=mMDSL_Polyline(), mMDSL_Points158=mMDSL_Polygon()) == None

from python_code import mMDSL_Rectangle
from python_code import mMDSL_SVGCommand

def test_mMDSL_Rectangle___init__():
    assert mMDSL_Rectangle.__init__(mMDSL_Rectangle('\x00\x00', '', '', '', mMDSL_Rectangle=mMDSL_SVGCommand()), '', '', '', '', mMDSL_Rectangle=mMDSL_SVGCommand()) == None

from python_code import mMDSL_SimpleUI
from python_code import mMDSL_ViewBox

def test_mMDSL_ViewBox___init__():
    assert mMDSL_ViewBox.__init__(mMDSL_ViewBox('', '\x00', mMDSL_ViewBox=mMDSL_SimpleUI()), '\x00\x00', '', mMDSL_ViewBox=mMDSL_SimpleUI()) == None

from python_code import mMDSL_SimpleUI
from python_code import mMDSL_WarningBox

def test_mMDSL_WarningBox___init__():
    assert mMDSL_WarningBox.__init__(mMDSL_WarningBox('', '', '\x00\x00', mMDSL_WarningBox=mMDSL_SimpleUI()), '', '', '', mMDSL_WarningBox=mMDSL_SimpleUI()) == None
