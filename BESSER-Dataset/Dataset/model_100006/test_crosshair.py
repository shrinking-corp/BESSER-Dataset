from python_code import Event
from python_code import SWRC_AcademicStaff
from python_code import SWRC_Conference
from python_code import SWRC_Event

def test_SWRC_Conference___init__():
    assert SWRC_Conference.__init__(SWRC_Conference('', Event=SWRC_Event('', '\x00\x00', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()), '\x00', Event=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()) == None


from python_code import Event
from python_code import SWRC_Event

def test_SWRC_Event___init__():
    assert SWRC_Event.__init__(SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), '', '', '\x00', '', hasPartEvent=Event(), atEvent=Event()) == None


from python_code import Event
from python_code import SWRC_AcademicStaff
from python_code import SWRC_Event
from python_code import SWRC_Meeting

def test_SWRC_Meeting___init__():
    assert SWRC_Meeting.__init__(SWRC_Meeting('', SWRC_Meeting=set(), Event=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '\x00', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()), '', SWRC_Meeting=set(), Event=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()) == None


from python_code import SWRC_AcademicStaff
from python_code import SWRC_Bibliography
from python_code import SWRC_Misc
from python_code import SWRC_Organization
from python_code import SWRC_PhDStudent

def test_SWRC_Misc___init__():
    assert SWRC_Misc.__init__(SWRC_Misc('', '', Publication93=SWRC_PhDStudent(), Publication87=SWRC_AcademicStaff(), Publication74=SWRC_AcademicStaff(), Publication106=SWRC_Organization('', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()), Publication=SWRC_Bibliography()), '', '', Publication93=SWRC_PhDStudent(), Publication87=SWRC_AcademicStaff(), Publication74=SWRC_AcademicStaff(), Publication106=SWRC_Organization('', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()), Publication=SWRC_Bibliography()) == None


from python_code import SWRC_Organization

def test_SWRC_Organization___init__():
    assert SWRC_Organization.__init__(SWRC_Organization('', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()), '', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()) == None


from python_code import SWRC_Person

def test_SWRC_Person___init__():
    assert SWRC_Person.__init__(SWRC_Person('', '', '', '', '', '', ''), '', '\x00', '', '', '', '', '') == None


from python_code import Organization
from python_code import SWRC_Product

def test_SWRC_Product___init__():
    assert SWRC_Product.__init__(SWRC_Product('', develops=Organization()), '', develops=Organization()) == None


from python_code import AcademicStaff
from python_code import Organization
from python_code import SWRC_Project

def test_SWRC_Project___init__():
    assert SWRC_Project.__init__(SWRC_Project('', carriesOut=Organization(), finances=Organization(), dealWithIn=set(), SWRC_Project=set(), describesProject=set(), headOf=AcademicStaff()), '', carriesOut=Organization(), finances=Organization(), dealWithIn=set(), SWRC_Project=set(), describesProject=set(), headOf=AcademicStaff()) == None


from python_code import SWRC_Publication

def test_SWRC_Publication___init__():
    assert SWRC_Publication.__init__(SWRC_Publication('', '', '', '', ''), '', '', '', '', '') == None


from python_code import SWRC_Organization
from python_code import SWRC_SoftwareComponent
from python_code import SWRC_SoftwareProject

def test_SWRC_SoftwareComponent___init__():
    assert SWRC_SoftwareComponent.__init__(SWRC_SoftwareComponent('', Product=SWRC_Organization('\x00', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()), Product134=SWRC_SoftwareProject()), '', Product=SWRC_Organization('', '', financedBy=set(), SWRC_Organization=set(), SWRC_Organization108=set(), carriedOutBy=set(), developedBy=set(), affiliation=set()), Product134=SWRC_SoftwareProject()) == None


from python_code import Organization
from python_code import SWRC_TechnicalReport

def test_SWRC_TechnicalReport___init__():
    assert SWRC_TechnicalReport.__init__(SWRC_TechnicalReport('', SWRC_TechnicalReport=Organization()), '', SWRC_TechnicalReport=Organization()) == None


from python_code import SWRC_Topic

def test_SWRC_Topic___init__():
    assert SWRC_Topic.__init__(SWRC_Topic(''), '') == None


from python_code import Event
from python_code import SWRC_AcademicStaff
from python_code import SWRC_Event
from python_code import SWRC_Workshop

def test_SWRC_Workshop___init__():
    assert SWRC_Workshop.__init__(SWRC_Workshop('', Event=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()), '', Event=SWRC_Event('\x00\x00\x00', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event64=SWRC_Event('', '', '', '', hasPartEvent=Event(), atEvent=Event()), Event84=SWRC_AcademicStaff(), Event81=SWRC_AcademicStaff()) == None

