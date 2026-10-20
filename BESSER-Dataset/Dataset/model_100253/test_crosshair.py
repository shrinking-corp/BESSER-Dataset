from python_code import table_DFeatureColumn

def test_table_DFeatureColumn___init__():
    assert table_DFeatureColumn.__init__(table_DFeatureColumn(''), '') == None


from python_code import table_DTableElementSynchronizer

def test_table_DTableElementSynchronizer___init__():
    assert table_DTableElementSynchronizer.__init__(table_DTableElementSynchronizer()) == None

def test_table_DTableElementSynchronizer_refresh():
    assert table_DTableElementSynchronizer.refresh(table_DTableElementSynchronizer(), '') == None


from python_code import BackgroundStyleDescription
from python_code import table_description_BackgroundConditionalStyle

def test_table_description_BackgroundConditionalStyle___init__():
    assert table_description_BackgroundConditionalStyle.__init__(table_description_BackgroundConditionalStyle('', table_description_BackgroundConditionalStyle=BackgroundStyleDescription()), '', table_description_BackgroundConditionalStyle=BackgroundStyleDescription()) == None


from python_code import LabelEditTool
from python_code import table_description_CellUpdater

def test_table_description_CellUpdater___init__():
    assert table_description_CellUpdater.__init__(table_description_CellUpdater('', table_description_CellUpdater=LabelEditTool()), '', table_description_CellUpdater=LabelEditTool()) == None

def test_table_description_CellUpdater_getLabelComputationExpression():
    assert table_description_CellUpdater.getLabelComputationExpression(table_description_CellUpdater('', table_description_CellUpdater=LabelEditTool())) == None

def test_table_description_CellUpdater_getCreateCell():
    assert table_description_CellUpdater.getCreateCell(table_description_CellUpdater('', table_description_CellUpdater=LabelEditTool())) == None


from python_code import table_DCellStyle
from python_code import table_DTableElement
from python_code import table_description_ColumnMapping

def test_table_description_ColumnMapping___init__():
    assert table_description_ColumnMapping.__init__(table_description_ColumnMapping('', 0, TableMapping=table_DTableElement(), TableMapping24=table_DCellStyle(), TableMapping27=table_DCellStyle()), '', 0, TableMapping=table_DTableElement(), TableMapping24=table_DCellStyle(), TableMapping27=table_DCellStyle()) == None


from python_code import DeleteColumnTool
from python_code import table_description_ElementColumnMapping

def test_table_description_ElementColumnMapping___init__():
    assert table_description_ElementColumnMapping.__init__(table_description_ElementColumnMapping('\x00\x00', '', mapping99=set(), mapping101=DeleteColumnTool()), '', '', mapping99=set(), mapping101=DeleteColumnTool()) == None


from python_code import table_description_FeatureColumnMapping

def test_table_description_FeatureColumnMapping___init__():
    assert table_description_FeatureColumnMapping.__init__(table_description_FeatureColumnMapping('', '', '\x00\x00'), '', '', '') == None


from python_code import ForegroundStyleDescription
from python_code import table_description_ForegroundConditionalStyle

def test_table_description_ForegroundConditionalStyle___init__():
    assert table_description_ForegroundConditionalStyle.__init__(table_description_ForegroundConditionalStyle('', table_description_ForegroundConditionalStyle=ForegroundStyleDescription()), '', table_description_ForegroundConditionalStyle=ForegroundStyleDescription()) == None


from python_code import ColorDescription
from python_code import table_description_ForegroundStyleDescription

def test_table_description_ForegroundStyleDescription___init__():
    assert table_description_ForegroundStyleDescription.__init__(table_description_ForegroundStyleDescription(0, '\x00', table_description_ForegroundStyleDescription=ColorDescription()), 0, '\x00', table_description_ForegroundStyleDescription=ColorDescription()) == None


from python_code import ColumnMapping
from python_code import CreateCellTool
from python_code import table_description_IntersectionMapping

def test_table_description_IntersectionMapping___init__():
    assert table_description_IntersectionMapping.__init__(table_description_IntersectionMapping(False, '', '', '', '\x00', '', '', table_description_IntersectionMapping=set(), table_description_IntersectionMapping113=ColumnMapping(), mapping116=CreateCellTool()), False, '', '', '', '', '', '', table_description_IntersectionMapping=set(), table_description_IntersectionMapping113=ColumnMapping(), mapping116=CreateCellTool()) == None


from python_code import DeleteLineTool
from python_code import table_description_LineMapping

def test_table_description_LineMapping___init__():
    assert table_description_LineMapping.__init__(table_description_LineMapping('', '', '', table_description_LineMapping=set(), reusedInMappings=set(), table_description_LineMapping90=set(), reusedSubLines=set(), table_description_LineMapping95=set(), mapping=DeleteLineTool()), '', '', '', table_description_LineMapping=set(), reusedInMappings=set(), table_description_LineMapping90=set(), reusedSubLines=set(), table_description_LineMapping95=set(), mapping=DeleteLineTool()) == None


from python_code import table_description_TableMapping

def test_table_description_TableMapping___init__():
    assert table_description_TableMapping.__init__(table_description_TableMapping(''), '') == None


from python_code import table_description_TableVariable

def test_table_description_TableVariable___init__():
    assert table_description_TableVariable.__init__(table_description_TableVariable(''), '') == None

