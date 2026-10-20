from python_code import WebApp_GroupOfQuestions

def test_WebApp_GroupOfQuestions___init__():
    assert WebApp_GroupOfQuestions.__init__(WebApp_GroupOfQuestions('', WebApp_GroupOfQuestions=set()), '', WebApp_GroupOfQuestions=set()) == None


from python_code import WebApp_Multiple
from python_code import WebApp_MultipleForQuestionnary
from python_code import WebApp_Option

def test_WebApp_Option___init__():
    assert WebApp_Option.__init__(WebApp_Option('', 0, WebApp_Option=WebApp_Multiple(), WebApp_Option29=WebApp_MultipleForQuestionnary()), '', 0, WebApp_Option=WebApp_Multiple(), WebApp_Option29=WebApp_MultipleForQuestionnary()) == None


from python_code import WebApp_Questionnary

def test_WebApp_Questionnary___init__():
    assert WebApp_Questionnary.__init__(WebApp_Questionnary(True), False) == None


from python_code import WebApp_RSSFeed

def test_WebApp_RSSFeed___init__():
    assert WebApp_RSSFeed.__init__(WebApp_RSSFeed('\x00\x00', 0, '', ''), '', 0, '', '') == None


from python_code import WebApp_SimpleQuestion

def test_WebApp_SimpleQuestion___init__():
    assert WebApp_SimpleQuestion.__init__(WebApp_SimpleQuestion('', '\x00'), '\x00\x00', '') == None


from python_code import WebApp_TrueFalseForQuestionnary

def test_WebApp_TrueFalseForQuestionnary___init__():
    assert WebApp_TrueFalseForQuestionnary.__init__(WebApp_TrueFalseForQuestionnary(''), '') == None


from python_code import WebApp_Twitter

def test_WebApp_Twitter___init__():
    assert WebApp_Twitter.__init__(WebApp_Twitter(''), '') == None


from python_code import WebApp_DataBase
from python_code import WebApp_QuestionBank
from python_code import WebApp_WebApp

def test_WebApp_WebApp___init__():
    assert WebApp_WebApp.__init__(WebApp_WebApp('', '', '', WebApp_WebApp=set(), WebApp_WebApp2=WebApp_DataBase(), WebApp_WebApp4=WebApp_QuestionBank()), '', '', '', WebApp_WebApp=set(), WebApp_WebApp2=WebApp_DataBase(), WebApp_WebApp4=WebApp_QuestionBank()) == None

