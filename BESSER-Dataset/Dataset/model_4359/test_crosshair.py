from python_code import jointPackage_CPL2SPL_SrcAddressSwitch

def test_jointPackage_CPL2SPL_SrcAddressSwitch___init__():
    assert jointPackage_CPL2SPL_SrcAddressSwitch.__init__(jointPackage_CPL2SPL_SrcAddressSwitch('\x00\x00', '', jointPackage_CPL2SPL_SrcAddressSwitch=set()), '', '', jointPackage_CPL2SPL_SrcAddressSwitch=set()) == None


from python_code import jointPackage_CPL2SPL_SrcLocation
from python_code import jointPackage_CPL2SPL_SrcNodeContainer

def test_jointPackage_CPL2SPL_SrcLocation___init__():
    assert jointPackage_CPL2SPL_SrcLocation.__init__(jointPackage_CPL2SPL_SrcLocation('', '', '\x00\x00', SrcNode=jointPackage_CPL2SPL_SrcNodeContainer()), '', '', '', SrcNode=jointPackage_CPL2SPL_SrcNodeContainer()) == None


from python_code import SrcBusy
from python_code import SrcDefault
from python_code import SrcFailure
from python_code import SrcNoAnswer
from python_code import SrcRedirection
from python_code import jointPackage_CPL2SPL_SrcProxy

def test_jointPackage_CPL2SPL_SrcProxy___init__():
    assert jointPackage_CPL2SPL_SrcProxy.__init__(jointPackage_CPL2SPL_SrcProxy('', '', '\x00\x00', jointPackage_CPL2SPL_SrcProxy=SrcBusy(), jointPackage_CPL2SPL_SrcProxy16=SrcNoAnswer(), jointPackage_CPL2SPL_SrcProxy18=SrcRedirection(), jointPackage_CPL2SPL_SrcProxy20=SrcFailure(), jointPackage_CPL2SPL_SrcProxy22=SrcDefault()), '', '', '', jointPackage_CPL2SPL_SrcProxy=SrcBusy(), jointPackage_CPL2SPL_SrcProxy16=SrcNoAnswer(), jointPackage_CPL2SPL_SrcProxy18=SrcRedirection(), jointPackage_CPL2SPL_SrcProxy20=SrcFailure(), jointPackage_CPL2SPL_SrcProxy22=SrcDefault()) == None


from python_code import jointPackage_CPL2SPL_SrcRedirect

def test_jointPackage_CPL2SPL_SrcRedirect___init__():
    assert jointPackage_CPL2SPL_SrcRedirect.__init__(jointPackage_CPL2SPL_SrcRedirect(''), '') == None


from python_code import jointPackage_CPL2SPL_SrcReject

def test_jointPackage_CPL2SPL_SrcReject___init__():
    assert jointPackage_CPL2SPL_SrcReject.__init__(jointPackage_CPL2SPL_SrcReject('', '\x00'), '\x00\x00', '') == None


from python_code import jointPackage_CPL2SPL_SrcStringSwitch

def test_jointPackage_CPL2SPL_SrcStringSwitch___init__():
    assert jointPackage_CPL2SPL_SrcStringSwitch.__init__(jointPackage_CPL2SPL_SrcStringSwitch('', jointPackage_CPL2SPL_SrcStringSwitch=set()), '', jointPackage_CPL2SPL_SrcStringSwitch=set()) == None


from python_code import jointPackage_CPL2SPL_SrcSubAction

def test_jointPackage_CPL2SPL_SrcSubAction___init__():
    assert jointPackage_CPL2SPL_SrcSubAction.__init__(jointPackage_CPL2SPL_SrcSubAction(''), '') == None


from python_code import jointPackage_CPL2SPL_SrcNodeContainer
from python_code import jointPackage_CPL2SPL_SrcSubCall

def test_jointPackage_CPL2SPL_SrcSubCall___init__():
    assert jointPackage_CPL2SPL_SrcSubCall.__init__(jointPackage_CPL2SPL_SrcSubCall('', SrcNode=jointPackage_CPL2SPL_SrcNodeContainer()), '', SrcNode=jointPackage_CPL2SPL_SrcNodeContainer()) == None


from python_code import jointPackage_CPL2SPL_SrcSwitchedAddress

def test_jointPackage_CPL2SPL_SrcSwitchedAddress___init__():
    assert jointPackage_CPL2SPL_SrcSwitchedAddress.__init__(jointPackage_CPL2SPL_SrcSwitchedAddress('', '', '\x00\x00'), '', '', '') == None


from python_code import jointPackage_CPL2SPL_SrcSwitchedLanguage

def test_jointPackage_CPL2SPL_SrcSwitchedLanguage___init__():
    assert jointPackage_CPL2SPL_SrcSwitchedLanguage.__init__(jointPackage_CPL2SPL_SrcSwitchedLanguage(''), '') == None


from python_code import jointPackage_CPL2SPL_SrcSwitchedPriority

def test_jointPackage_CPL2SPL_SrcSwitchedPriority___init__():
    assert jointPackage_CPL2SPL_SrcSwitchedPriority.__init__(jointPackage_CPL2SPL_SrcSwitchedPriority('', '', '\x00\x00'), '', '', '') == None


from python_code import jointPackage_CPL2SPL_SrcSwitchedString

def test_jointPackage_CPL2SPL_SrcSwitchedString___init__():
    assert jointPackage_CPL2SPL_SrcSwitchedString.__init__(jointPackage_CPL2SPL_SrcSwitchedString('', '\x00'), '\x00\x00', '') == None


from python_code import jointPackage_CPL2SPL_SrcSwitchedTime

def test_jointPackage_CPL2SPL_SrcSwitchedTime___init__():
    assert jointPackage_CPL2SPL_SrcSwitchedTime.__init__(jointPackage_CPL2SPL_SrcSwitchedTime('\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00'), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '') == None


from python_code import jointPackage_CPL2SPL_SrcTimeSwitch

def test_jointPackage_CPL2SPL_SrcTimeSwitch___init__():
    assert jointPackage_CPL2SPL_SrcTimeSwitch.__init__(jointPackage_CPL2SPL_SrcTimeSwitch('\x00\x00', '', jointPackage_CPL2SPL_SrcTimeSwitch=set()), '', '', jointPackage_CPL2SPL_SrcTimeSwitch=set()) == None


from python_code import TrgConstant
from python_code import jointPackage_CPL2SPL_TrgBooleanConstant
from python_code import jointPackage_CPL2SPL_TrgConstantExp
from python_code import jointPackage_CPL2SPL_TrgSelectCase
from python_code import jointPackage_CPL2SPL_TrgSequenceConstant
from python_code import jointPackage_CPL2SPL_TrgWhenHeader

def test_jointPackage_CPL2SPL_TrgBooleanConstant___init__():
    assert jointPackage_CPL2SPL_TrgBooleanConstant.__init__(jointPackage_CPL2SPL_TrgBooleanConstant(False, TrgConstant=jointPackage_CPL2SPL_TrgWhenHeader('', jointPackage_CPL2SPL_TrgWhenHeader=TrgConstant()), TrgConstant127=jointPackage_CPL2SPL_TrgConstantExp(), TrgConstant151=jointPackage_CPL2SPL_TrgSequenceConstant(), TrgConstant125=jointPackage_CPL2SPL_TrgSelectCase()), False, TrgConstant=jointPackage_CPL2SPL_TrgWhenHeader('', jointPackage_CPL2SPL_TrgWhenHeader=TrgConstant()), TrgConstant127=jointPackage_CPL2SPL_TrgConstantExp(), TrgConstant151=jointPackage_CPL2SPL_TrgSequenceConstant(), TrgConstant125=jointPackage_CPL2SPL_TrgSelectCase()) == None


from python_code import jointPackage_CPL2SPL_TrgClientErrorResponse

def test_jointPackage_CPL2SPL_TrgClientErrorResponse___init__():
    assert jointPackage_CPL2SPL_TrgClientErrorResponse.__init__(jointPackage_CPL2SPL_TrgClientErrorResponse(''), '') == None


from python_code import jointPackage_CPL2SPL_TrgDeclaration

def test_jointPackage_CPL2SPL_TrgDeclaration___init__():
    assert jointPackage_CPL2SPL_TrgDeclaration.__init__(jointPackage_CPL2SPL_TrgDeclaration(''), '') == None


from python_code import jointPackage_CPL2SPL_TrgEvent
from python_code import jointPackage_CPL2SPL_TrgRegistration
from python_code import jointPackage_CPL2SPL_TrgService

def test_jointPackage_CPL2SPL_TrgEvent___init__():
    assert jointPackage_CPL2SPL_TrgEvent.__init__(jointPackage_CPL2SPL_TrgEvent('', jointPackage_CPL2SPL_TrgEvent=set(), jointPackage_CPL2SPL_TrgEvent44=set(), TrgSession=jointPackage_CPL2SPL_TrgService('', jointPackage_CPL2SPL_TrgService=set(), jointPackage_CPL2SPL_TrgService31=set()), TrgSession36=jointPackage_CPL2SPL_TrgRegistration()), '', jointPackage_CPL2SPL_TrgEvent=set(), jointPackage_CPL2SPL_TrgEvent44=set(), TrgSession=jointPackage_CPL2SPL_TrgService('\x00', jointPackage_CPL2SPL_TrgService=set(), jointPackage_CPL2SPL_TrgService31=set()), TrgSession36=jointPackage_CPL2SPL_TrgRegistration()) == None


from python_code import jointPackage_CPL2SPL_TrgGlobalErrorResponse

def test_jointPackage_CPL2SPL_TrgGlobalErrorResponse___init__():
    assert jointPackage_CPL2SPL_TrgGlobalErrorResponse.__init__(jointPackage_CPL2SPL_TrgGlobalErrorResponse(''), '') == None


from python_code import jointPackage_CPL2SPL_TrgHeadedMessageField
from python_code import jointPackage_CPL2SPL_TrgWithExp

def test_jointPackage_CPL2SPL_TrgHeadedMessageField___init__():
    assert jointPackage_CPL2SPL_TrgHeadedMessageField.__init__(jointPackage_CPL2SPL_TrgHeadedMessageField('', TrgMessageField=jointPackage_CPL2SPL_TrgWithExp()), '', TrgMessageField=jointPackage_CPL2SPL_TrgWithExp()) == None


from python_code import TrgConstant
from python_code import jointPackage_CPL2SPL_TrgConstantExp
from python_code import jointPackage_CPL2SPL_TrgIntegerConstant
from python_code import jointPackage_CPL2SPL_TrgSelectCase
from python_code import jointPackage_CPL2SPL_TrgSequenceConstant
from python_code import jointPackage_CPL2SPL_TrgWhenHeader

def test_jointPackage_CPL2SPL_TrgIntegerConstant___init__():
    assert jointPackage_CPL2SPL_TrgIntegerConstant.__init__(jointPackage_CPL2SPL_TrgIntegerConstant(0, TrgConstant=jointPackage_CPL2SPL_TrgWhenHeader('\x00', jointPackage_CPL2SPL_TrgWhenHeader=TrgConstant()), TrgConstant127=jointPackage_CPL2SPL_TrgConstantExp(), TrgConstant151=jointPackage_CPL2SPL_TrgSequenceConstant(), TrgConstant125=jointPackage_CPL2SPL_TrgSelectCase()), 0, TrgConstant=jointPackage_CPL2SPL_TrgWhenHeader('', jointPackage_CPL2SPL_TrgWhenHeader=TrgConstant()), TrgConstant127=jointPackage_CPL2SPL_TrgConstantExp(), TrgConstant151=jointPackage_CPL2SPL_TrgSequenceConstant(), TrgConstant125=jointPackage_CPL2SPL_TrgSelectCase()) == None


from python_code import jointPackage_CPL2SPL_TrgLocatedElement

def test_jointPackage_CPL2SPL_TrgLocatedElement___init__():
    assert jointPackage_CPL2SPL_TrgLocatedElement.__init__(jointPackage_CPL2SPL_TrgLocatedElement('', '', '\x00\x00'), '', '', '') == None


from python_code import jointPackage_CPL2SPL_TrgRedirectionErrorResponse

def test_jointPackage_CPL2SPL_TrgRedirectionErrorResponse___init__():
    assert jointPackage_CPL2SPL_TrgRedirectionErrorResponse.__init__(jointPackage_CPL2SPL_TrgRedirectionErrorResponse(''), '') == None


from python_code import jointPackage_CPL2SPL_TrgFunctionCall
from python_code import jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration

def test_jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration___init__():
    assert jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration.__init__(jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration('', TrgFunctionDeclaration=jointPackage_CPL2SPL_TrgFunctionCall()), '', TrgFunctionDeclaration=jointPackage_CPL2SPL_TrgFunctionCall()) == None


from python_code import jointPackage_CPL2SPL_TrgPopExp
from python_code import jointPackage_CPL2SPL_TrgPushStat
from python_code import jointPackage_CPL2SPL_TrgSIPHeaderPlace
from python_code import jointPackage_CPL2SPL_TrgSetStat

def test_jointPackage_CPL2SPL_TrgSIPHeaderPlace___init__():
    assert jointPackage_CPL2SPL_TrgSIPHeaderPlace.__init__(jointPackage_CPL2SPL_TrgSIPHeaderPlace('', TrgPlace117=jointPackage_CPL2SPL_TrgPushStat(), TrgPlace=jointPackage_CPL2SPL_TrgSetStat(), TrgPlace142=jointPackage_CPL2SPL_TrgPopExp()), '', TrgPlace117=jointPackage_CPL2SPL_TrgPushStat(), TrgPlace=jointPackage_CPL2SPL_TrgSetStat(), TrgPlace142=jointPackage_CPL2SPL_TrgPopExp()) == None

