from python_code import conf101_NamedElement

def test_conf101_NamedElement___init__():
    assert conf101_NamedElement.__init__(conf101_NamedElement(''), '') == None


from python_code import conf101_Conference
from python_code import conf101_Contribution
from python_code import conf101_Location
from python_code import conf101_ProgramComitee
from python_code import conf101_Session
from python_code import conf101_SteeringComitee

def test_conf101_Session___init__():
    assert conf101_Session.__init__(conf101_Session('', conf101_Session=conf101_Location(), conf101_Session9=conf101_ProgramComitee(), conf101_Session11=conf101_SteeringComitee(), conf101_Session13=conf101_Contribution(), conf101_Session19=conf101_Conference()), '', conf101_Session=conf101_Location(), conf101_Session9=conf101_ProgramComitee(), conf101_Session11=conf101_SteeringComitee(), conf101_Session13=conf101_Contribution(), conf101_Session19=conf101_Conference()) == None

