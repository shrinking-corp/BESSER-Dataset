from python_code import MavenProject_Build

def test_MavenProject_Build___init__():
    assert MavenProject_Build.__init__(MavenProject_Build('', '', '', MavenProject_Build=set(), MavenProject_Build9=set()), '', '', '', MavenProject_Build=set(), MavenProject_Build9=set()) == None


from python_code import Build
from python_code import MavenProject_Developer
from python_code import MavenProject_Project

def test_MavenProject_Developer___init__():
    assert MavenProject_Developer.__init__(MavenProject_Developer('', Person=MavenProject_Project('', '', '', '\x00', '', MavenProject_Project=set(), MavenProject_Project2=set(), MavenProject_Project4=Build(), MavenProject_Project6=set())), '', Person=MavenProject_Project('', '', '', '', '', MavenProject_Project=set(), MavenProject_Project2=set(), MavenProject_Project4=Build(), MavenProject_Project6=set())) == None


from python_code import MavenProject_MailingList

def test_MavenProject_MailingList___init__():
    assert MavenProject_MailingList.__init__(MavenProject_MailingList('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import MavenProject_Person

def test_MavenProject_Person___init__():
    assert MavenProject_Person.__init__(MavenProject_Person('', '', '', '', '', '', '\x00', ''), '', '', '', '', '', '', '', '') == None


from python_code import Build
from python_code import MavenProject_Project

def test_MavenProject_Project___init__():
    assert MavenProject_Project.__init__(MavenProject_Project('\x00', '', '', '', '', MavenProject_Project=set(), MavenProject_Project2=set(), MavenProject_Project4=Build(), MavenProject_Project6=set()), '', '', '', '', '', MavenProject_Project=set(), MavenProject_Project2=set(), MavenProject_Project4=Build(), MavenProject_Project6=set()) == None


from python_code import MavenProject_Resource

def test_MavenProject_Resource___init__():
    assert MavenProject_Resource.__init__(MavenProject_Resource('', '', '', '', ''), '', '', '', '', '') == None

