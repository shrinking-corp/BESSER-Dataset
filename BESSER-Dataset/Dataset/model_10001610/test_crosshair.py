from python_code import account_UserAccountPasswordChange

def test_account_UserAccountPasswordChange___init__():
    assert account_UserAccountPasswordChange.__init__(account_UserAccountPasswordChange('', '', '\x00\x00'), '', '', '') == None


from python_code import game_Deck

def test_game_Deck___init__():
    assert game_Deck.__init__(game_Deck('', card1=set()), '', card1=set()) == None


from python_code import profile_UserProfile

def test_profile_UserProfile___init__():
    assert profile_UserProfile.__init__(profile_UserProfile('', '', '', '', ''), '', '', '', '', '') == None


from python_code import account_UserAccountRepository_Interface
from python_code import profile_UserProfileController
from python_code import profile_UserProfileRepository_Interface

def test_profile_UserProfileController___init__():
    assert profile_UserProfileController.__init__(profile_UserProfileController('', account_UserAccountRepository_Interface(), '\x00', profile_UserProfileRepository_Interface()), '\x00\x00', account_UserAccountRepository_Interface(), '', profile_UserProfileRepository_Interface()) == None

