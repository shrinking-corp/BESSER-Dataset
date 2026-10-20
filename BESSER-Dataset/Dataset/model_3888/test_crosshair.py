from python_code import gaml_Access
from python_code import gaml_ExpressionList

def test_gaml_Access___init__():
    assert gaml_Access.__init__(gaml_Access('', gaml_Access=gaml_ExpressionList()), '', gaml_Access=gaml_ExpressionList()) == None


from python_code import gaml_GamlDefinition

def test_gaml_GamlDefinition___init__():
    assert gaml_GamlDefinition.__init__(gaml_GamlDefinition(''), '') == None


from python_code import gaml_Block
from python_code import gaml_ExperimentFileStructure
from python_code import gaml_HeadlessExperiment

def test_gaml_HeadlessExperiment___init__():
    assert gaml_HeadlessExperiment.__init__(gaml_HeadlessExperiment('', '', '', '', gaml_HeadlessExperiment=gaml_ExperimentFileStructure(), gaml_HeadlessExperiment15=set(), gaml_HeadlessExperiment17=gaml_Block()), '', '', '', '', gaml_HeadlessExperiment=gaml_ExperimentFileStructure(), gaml_HeadlessExperiment15=set(), gaml_HeadlessExperiment17=gaml_Block()) == None


from python_code import gaml_Import
from python_code import gaml_Model

def test_gaml_Import___init__():
    assert gaml_Import.__init__(gaml_Import('', gaml_Import=gaml_Model()), '', gaml_Import=gaml_Model()) == None


from python_code import gaml_Parameter

def test_gaml_Parameter___init__():
    assert gaml_Parameter.__init__(gaml_Parameter(''), '') == None


from python_code import gaml_Model
from python_code import gaml_Pragma

def test_gaml_Pragma___init__():
    assert gaml_Pragma.__init__(gaml_Pragma('', gaml_Pragma=gaml_Model()), '', gaml_Pragma=gaml_Model()) == None


from python_code import gaml_S_Display

def test_gaml_S_Display___init__():
    assert gaml_S_Display.__init__(gaml_S_Display(''), '') == None

