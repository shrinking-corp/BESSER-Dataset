import datetime as _ch_datetime
from python_code import db_DBResource

def test_db_DBResource___init__():
    assert db_DBResource.__init__(db_DBResource('', _ch_datetime.date(1, 1, 2), _ch_datetime.date(1, 1, 1), 0), '\x00', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0) == None


from python_code import db_Variable

def test_db_Variable___init__():
    assert db_Variable.__init__(db_Variable('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import config_SafletProject
from python_code import db_config_Prompt

def test_db_config_Prompt___init__():
    assert db_config_Prompt.__init__(db_config_Prompt(False, '\x00', prompts=config_SafletProject()), False, '\x00', prompts=config_SafletProject()) == None


from python_code import db_config_SFTPInfo

def test_db_config_SFTPInfo___init__():
    assert db_config_SFTPInfo.__init__(db_config_SFTPInfo('', '', 0), '\x00', '', 0) == None


from python_code import config_User
from python_code import db_config_SafiServer

def test_db_config_SafiServer___init__():
    assert db_config_SafiServer.__init__(db_config_SafiServer(False, True, 0, '', 0, db_config_SafiServer=config_User(), db_config_SafiServer22=set()), False, False, 0, '\x00', 0, db_config_SafiServer=config_User(), db_config_SafiServer22=set()) == None


from python_code import config_SafletProject
from python_code import db_config_Saflet

def test_db_config_Saflet___init__():
    assert db_config_Saflet.__init__(db_config_Saflet('', '\x00', saflets=config_SafletProject()), '\x00\x00', '', saflets=config_SafletProject()) == None


from python_code import db_config_SafletProject

def test_db_config_SafletProject___init__():
    assert db_config_SafletProject.__init__(db_config_SafletProject(False, project29=set(), project=set()), False, project29=set(), project=set()) == None


import datetime as _ch_datetime
from python_code import config_User
from python_code import db_config_ServerResource

def test_db_config_ServerResource___init__():
    assert db_config_ServerResource.__init__(db_config_ServerResource('', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 3), 0, '', db_config_ServerResource=config_User(), db_config_ServerResource17=config_User()), '', _ch_datetime.date(1, 1, 1), _ch_datetime.date(1, 1, 1), 0, '', db_config_ServerResource=config_User(), db_config_ServerResource17=config_User()) == None


from python_code import config_SafiServer
from python_code import db_config_TelephonySubsystem

def test_db_config_TelephonySubsystem___init__():
    assert db_config_TelephonySubsystem.__init__(db_config_TelephonySubsystem('\x00', False, False, '', False, '', '', 0, '', '', '\x00', db_config_TelephonySubsystem=config_SafiServer()), '', False, False, '', False, '', '', 0, '', '', '', db_config_TelephonySubsystem=config_SafiServer()) == None


from python_code import db_config_User

def test_db_config_User___init__():
    assert db_config_User.__init__(db_config_User('', '', '', db_config_User=set()), '', '', '', db_config_User=set()) == None

