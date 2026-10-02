from python_code import soaml_Class
from python_code import soaml_DataType
from python_code import soaml_MessageType
from python_code import soaml_Signal

def test_soaml_MessageType___init__():
    assert soaml_MessageType.__init__(soaml_MessageType('', soaml_MessageType=soaml_Class(), soaml_MessageType34=soaml_DataType(), soaml_MessageType36=soaml_Signal()), '', soaml_MessageType=soaml_Class(), soaml_MessageType34=soaml_DataType(), soaml_MessageType36=soaml_Signal()) == None

from python_code import soaml_Comment
from python_code import soaml_Milestone
from python_code import soaml_Signal

def test_soaml_Milestone___init__():
    assert soaml_Milestone.__init__(soaml_Milestone('', soaml_Milestone=set(), soaml_Milestone39=soaml_Signal(), soaml_Milestone42=soaml_Comment()), '', soaml_Milestone=set(), soaml_Milestone39=soaml_Signal(), soaml_Milestone42=soaml_Comment()) == None
