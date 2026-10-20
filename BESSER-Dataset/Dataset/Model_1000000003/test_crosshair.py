from python_code import AssessmentElement

def test_AssessmentElement___init__():
    assert AssessmentElement.__init__(AssessmentElement('', '\x00'), '\x00\x00', '') == None


from python_code import Configuration

def test_Configuration___init__():
    assert Configuration.__init__(Configuration('', '', params=set(), eval=set()), '', '', params=set(), eval=set()) == None


from python_code import Datashape

def test_Datashape___init__():
    assert Datashape.__init__(Datashape('', f_date=set(), f_features=set(), dataset_1=set()), '', f_date=set(), f_features=set(), dataset_1=set()) == None


from python_code import Derived

def test_Derived___init__():
    assert Derived.__init__(Derived('', '\x00', '', baseMetric=set(), measures=set(), category=set(), derivedBy=set()), '', '', '', baseMetric=set(), measures=set(), category=set(), derivedBy=set()) == None


from python_code import MetricCategory

def test_MetricCategory___init__():
    assert MetricCategory.__init__(MetricCategory('', '', metrics=set()), '', '', metrics=set()) == None


from python_code import Project
from python_code import ProjectStatus

def test_Project___init__():
    assert Project.__init__(Project('', ProjectStatus.Created, eval=set(), involves=set(), legal_requirements=set()), '', ProjectStatus.Closed, eval=set(), involves=set(), legal_requirements=set()) == None


from python_code import LicensingType
from python_code import TagsSector
from python_code import TagsTargetSystem
from python_code import TagsVerificationTarget
from python_code import Tool
from python_code import VerificationType

def test_Tool___init__():
    assert Tool.__init__(Tool('', '', LicensingType.Proprietary, VerificationType.Case_1, '\x00', '', '', '', '\x00', '', TagsVerificationTarget.Transparency, TagsSector.Investment, TagsTargetSystem.Computer_Vision, '', observation_1=set()), '', '', LicensingType.Proprietary, VerificationType.Case_2, '', '', '', '\x00', '', '', TagsVerificationTarget.Risk_management, TagsSector.Trade, TagsTargetSystem.Natural_Language_Processing, '', observation_1=set()) == None

