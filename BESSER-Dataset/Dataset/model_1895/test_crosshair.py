from python_code import PSM_ArtifactElement

def test_PSM_ArtifactElement___init__():
    assert PSM_ArtifactElement.__init__(PSM_ArtifactElement('', '', '\x00\x00'), '', '', '') == None


from python_code import PSM_ConfigurationProperty
from python_code import PSM_JavaSpringWebApplicationProject

def test_PSM_ConfigurationProperty___init__():
    assert PSM_ConfigurationProperty.__init__(PSM_ConfigurationProperty('', '', '\x00\x00', PSM_ConfigurationProperty=PSM_JavaSpringWebApplicationProject()), '', '', '', PSM_ConfigurationProperty=PSM_JavaSpringWebApplicationProject()) == None


from python_code import PSM_JavaElement

def test_PSM_JavaElement___init__():
    assert PSM_JavaElement.__init__(PSM_JavaElement('\x00\x00', '', PSM_JavaElement=set()), '', '', PSM_JavaElement=set()) == None


from python_code import PSM_JavaSpringWebApplicationProject
from python_code import PSM_SpringWebApplicationLayer

def test_PSM_SpringWebApplicationLayer___init__():
    assert PSM_SpringWebApplicationLayer.__init__(PSM_SpringWebApplicationLayer('', PSM_SpringWebApplicationLayer=PSM_JavaSpringWebApplicationProject(), PSM_SpringWebApplicationLayer17=set()), '', PSM_SpringWebApplicationLayer=PSM_JavaSpringWebApplicationProject(), PSM_SpringWebApplicationLayer17=set()) == None

