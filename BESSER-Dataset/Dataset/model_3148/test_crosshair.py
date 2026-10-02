from python_code import oclstdlibcs_LibIterationCS

def test_oclstdlibcs_LibIterationCS___init__():
    assert oclstdlibcs_LibIterationCS.__init__(oclstdlibcs_LibIterationCS('', '', oclstdlibcs_LibIterationCS=set(), oclstdlibcs_LibIterationCS4=set()), '', '', oclstdlibcs_LibIterationCS=set(), oclstdlibcs_LibIterationCS4=set()) == None

from python_code import oclstdlibcs_LibOperationCS
from python_code import oclstdlibcs_Precedence

def test_oclstdlibcs_LibOperationCS___init__():
    assert oclstdlibcs_LibOperationCS.__init__(oclstdlibcs_LibOperationCS('', '', '\x00\x00', oclstdlibcs_LibOperationCS=oclstdlibcs_Precedence()), '', '', '', oclstdlibcs_LibOperationCS=oclstdlibcs_Precedence()) == None

from python_code import oclstdlibcs_LibPropertyCS

def test_oclstdlibcs_LibPropertyCS___init__():
    assert oclstdlibcs_LibPropertyCS.__init__(oclstdlibcs_LibPropertyCS(''), '') == None

from python_code import oclstdlibcs_LibClassCS
from python_code import oclstdlibcs_MetaclassNameCS

def test_oclstdlibcs_MetaclassNameCS___init__():
    assert oclstdlibcs_MetaclassNameCS.__init__(oclstdlibcs_MetaclassNameCS('', oclstdlibcs_MetaclassNameCS=oclstdlibcs_LibClassCS()), '', oclstdlibcs_MetaclassNameCS=oclstdlibcs_LibClassCS()) == None

from python_code import oclstdlibcs_LibPackageCS
from python_code import oclstdlibcs_PrecedenceCS

def test_oclstdlibcs_PrecedenceCS___init__():
    assert oclstdlibcs_PrecedenceCS.__init__(oclstdlibcs_PrecedenceCS(True, oclstdlibcs_PrecedenceCS=oclstdlibcs_LibPackageCS()), False, oclstdlibcs_PrecedenceCS=oclstdlibcs_LibPackageCS()) == None
