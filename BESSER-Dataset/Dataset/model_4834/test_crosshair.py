from python_code import archimateC2_BusinessProcess

def test_archimateC2_BusinessProcess___init__():
    assert archimateC2_BusinessProcess.__init__(archimateC2_BusinessProcess('', '', '', 0, '', False), '', '', '', 0, '\x00', False) == None


from python_code import archimateC2_ApplicationService
from python_code import archimateC2_BusinessService
from python_code import archimateC2_Contract
from python_code import archimateC2_InfrastructureService
from python_code import archimateC2_Product
from python_code import archimateC2_Value

def test_archimateC2_Product___init__():
    assert archimateC2_Product.__init__(archimateC2_Product('\x00', aggregatedByProductContract=set(), aggregatedByProductBusinessService=set(), Product=archimateC2_Value(), associatedWithProductValue=set(), aggregatesProductApplicationService=set(), aggregatesProductInfrastructureService=set(), Product19=archimateC2_Contract(), Product34=archimateC2_BusinessService(), Product152=archimateC2_ApplicationService(), Product228=archimateC2_InfrastructureService()), '', aggregatedByProductContract=set(), aggregatedByProductBusinessService=set(), Product=archimateC2_Value(), associatedWithProductValue=set(), aggregatesProductApplicationService=set(), aggregatesProductInfrastructureService=set(), Product19=archimateC2_Contract(), Product34=archimateC2_BusinessService(), Product152=archimateC2_ApplicationService(), Product228=archimateC2_InfrastructureService()) == None

