from python_code import SkillGraph_Graph
from python_code import SkillGraph_Parameter

def test_SkillGraph_Parameter___init__():
    assert SkillGraph_Parameter.__init__(SkillGraph_Parameter('', '', '', '', False, Parameter=SkillGraph_Graph(), parameterList=SkillGraph_Graph()), '', '', '', '', False, Parameter=SkillGraph_Graph(), parameterList=SkillGraph_Graph()) == None

