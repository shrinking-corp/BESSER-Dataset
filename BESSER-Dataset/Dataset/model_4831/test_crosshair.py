from python_code import archimateC3_BusinessProcess

def test_archimateC3_BusinessProcess___init__():
    assert archimateC3_BusinessProcess.__init__(archimateC3_BusinessProcess('', '', '', 0, '', False), '', '', '', 0, '\x00', False) == None


from python_code import archimateC3_ArchimateModel
from python_code import archimateC3_Group

def test_archimateC3_Group___init__():
    assert archimateC3_Group.__init__(archimateC3_Group('', archimateC3_Group=archimateC3_ArchimateModel(), archimateC3_Group17=set()), '', archimateC3_Group=archimateC3_ArchimateModel(), archimateC3_Group17=set()) == None


from python_code import archimateC3_Location

def test_archimateC3_Location___init__():
    assert archimateC3_Location.__init__(archimateC3_Location(''), '') == None

