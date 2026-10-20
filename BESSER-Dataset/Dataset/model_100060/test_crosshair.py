from python_code import BugTracking
from python_code import SoftwareQualityControl_Bug

def test_SoftwareQualityControl_Bug___init__():
    assert SoftwareQualityControl_Bug.__init__(SoftwareQualityControl_Bug('', '', '', '', '\x00', '', '', '', '', bugs=BugTracking()), '', '', '', '', '', '\x00', '', '', '', bugs=BugTracking()) == None


from python_code import ControlType
from python_code import ControlsSequence
from python_code import DateType
from python_code import SoftwareQualityControl_Control

def test_SoftwareQualityControl_Control___init__():
    assert SoftwareQualityControl_Control.__init__(SoftwareQualityControl_Control('', '', '', '', '', '', '', '', ct_control=ControlType(), controls=ControlsSequence(), SoftwareQualityControl_Control=DateType()), '', '', '', '', '', '', '', '', ct_control=ControlType(), controls=ControlsSequence(), SoftwareQualityControl_Control=DateType()) == None


from python_code import SoftwareQualityControl_DateType

def test_SoftwareQualityControl_DateType___init__():
    assert SoftwareQualityControl_DateType.__init__(SoftwareQualityControl_DateType('', '', '\x00\x00'), '', '', '') == None

