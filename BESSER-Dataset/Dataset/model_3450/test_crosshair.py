from python_code import org_aries_common_Attachment

def test_org_aries_common_Attachment___init__():
    assert org_aries_common_Attachment.__init__(org_aries_common_Attachment('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import org_aries_common_EmailAccount

def test_org_aries_common_EmailAccount___init__():
    assert org_aries_common_EmailAccount.__init__(org_aries_common_EmailAccount('', '', '\x00', '', '', '', org_aries_common_EmailAccount=set()), '', '', '', '', '', '', org_aries_common_EmailAccount=set()) == None


from python_code import PhoneNumber
from python_code import org_aries_common_EmailAddress

def test_org_aries_common_EmailAddress___init__():
    assert org_aries_common_EmailAddress.__init__(org_aries_common_EmailAddress('', '', '', '', '\x00', '', '', '', '', org_aries_common_EmailAddress=PhoneNumber()), '', '', '', '', '', '\x00', '', '', '', org_aries_common_EmailAddress=PhoneNumber()) == None


from python_code import org_aries_common_EmailAddressList

def test_org_aries_common_EmailAddressList___init__():
    assert org_aries_common_EmailAddressList.__init__(org_aries_common_EmailAddressList('', '\x00'), '\x00\x00', '') == None


from python_code import EmailAccount
from python_code import EmailBox
from python_code import org_aries_common_EmailBox

def test_org_aries_common_EmailBox___init__():
    assert org_aries_common_EmailBox.__init__(org_aries_common_EmailBox('', '', '', '', '', org_aries_common_EmailBox47=EmailBox(), org_aries_common_EmailBox50=set(), org_aries_common_EmailBox=EmailAccount()), '', '', '', '\x00', '', org_aries_common_EmailBox47=EmailBox(), org_aries_common_EmailBox50=set(), org_aries_common_EmailBox=EmailAccount()) == None

