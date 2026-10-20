from python_code import vml_Category
from python_code import vml_StackBarChart
from python_code import vml_StackBars

def test_vml_Category___init__():
    assert vml_Category.__init__(vml_Category('', vml_Category=vml_StackBarChart(), vml_Category65=vml_StackBars()), '', vml_Category=vml_StackBarChart(), vml_Category65=vml_StackBars()) == None


from python_code import vml_Chart
from python_code import vml_ChartWithAxisStyle

def test_vml_Chart___init__():
    assert vml_Chart.__init__(vml_Chart('\x00\x00', '', '', '', vml_Chart=vml_ChartWithAxisStyle()), '', '', '', '', vml_Chart=vml_ChartWithAxisStyle()) == None


from python_code import vml_ChartElement

def test_vml_ChartElement___init__():
    assert vml_ChartElement.__init__(vml_ChartElement('', '', '\x00\x00'), '', '', '') == None


from python_code import vml_Graph
from python_code import vml_GraphStyle

def test_vml_Graph___init__():
    assert vml_Graph.__init__(vml_Graph('', '', vml_Graph=set(), vml_Graph49=set(), vml_Graph51=vml_GraphStyle()), '', '', vml_Graph=set(), vml_Graph49=set(), vml_Graph51=vml_GraphStyle()) == None


from python_code import vml_ChartWithoutAxisStyle
from python_code import vml_Pie

def test_vml_Pie___init__():
    assert vml_Pie.__init__(vml_Pie('\x00\x00', '', vml_Pie=set(), vml_Pie45=vml_ChartWithoutAxisStyle()), '', '', vml_Pie=set(), vml_Pie45=vml_ChartWithoutAxisStyle()) == None


from python_code import vml_DiagramElement
from python_code import vml_Model
from python_code import vml_Table

def test_vml_Table___init__():
    assert vml_Table.__init__(vml_Table('', vml_Table=vml_Model(), vml_Table42=vml_DiagramElement(), vml_Table4=set(), vml_Table6=set()), '', vml_Table=vml_Model(), vml_Table42=vml_DiagramElement(), vml_Table4=set(), vml_Table6=set()) == None

