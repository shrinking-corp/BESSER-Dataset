from python_code import bean_CategoryCounts

def test_bean_CategoryCounts___init__():
    assert bean_CategoryCounts.__init__(bean_CategoryCounts(0, 0, 0, 0, 0), 0, 0, 0, 0, 0) == None


from python_code import bean_CommentBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_CommentBean___init__():
    assert bean_CommentBean.__init__(bean_CommentBean(0, 0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), ''), 0, 0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), '') == None


from python_code import bean_FriendRequest
from python_code import genmymodelreverse_java_sql_Timestamp

def test_bean_FriendRequest___init__():
    assert bean_FriendRequest.__init__(bean_FriendRequest(0, '', '\x00\x00', genmymodelreverse_java_sql_Timestamp()), 0, '', '', genmymodelreverse_java_sql_Timestamp()) == None


from python_code import bean_Friends

def test_bean_Friends___init__():
    assert bean_Friends.__init__(bean_Friends('', '\x00'), '\x00\x00', '') == None


from python_code import bean_ImageBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_ImageBean___init__():
    assert bean_ImageBean.__init__(bean_ImageBean(0, '\x00', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), 0), 0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), 0) == None


from python_code import bean_LikeBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_LikeBean___init__():
    assert bean_LikeBean.__init__(bean_LikeBean(0, '', 0, genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()), 0, '', 0, genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()) == None


from python_code import bean_MessageBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_MessageBean___init__():
    assert bean_MessageBean.__init__(bean_MessageBean(0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), '', '', 0, ''), 0, '\x00', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date(), '', '', 0, '') == None


from python_code import bean_MessageCommentBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_MessageCommentBean___init__():
    assert bean_MessageCommentBean.__init__(bean_MessageCommentBean('', 0, 0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()), '', 0, 0, '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()) == None


from python_code import bean_MessageLikeBean
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_MessageLikeBean___init__():
    assert bean_MessageLikeBean.__init__(bean_MessageLikeBean(0, '', 0, genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()), 0, '', 0, genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()) == None


from python_code import bean_ProfessionBean

def test_bean_ProfessionBean___init__():
    assert bean_ProfessionBean.__init__(bean_ProfessionBean('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import bean_ProfileInfo

def test_bean_ProfileInfo___init__():
    assert bean_ProfileInfo.__init__(bean_ProfileInfo('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import bean_TableBean

def test_bean_TableBean___init__():
    assert bean_TableBean.__init__(bean_TableBean(0, '', '\x00\x00'), 0, '', '') == None


from python_code import bean_UserInfo

def test_bean_UserInfo___init__():
    assert bean_UserInfo.__init__(bean_UserInfo('', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '\x00', '', '', '') == None


from python_code import bean_Warning
from python_code import genmymodelreverse_java_sql_Date
from python_code import genmymodelreverse_java_sql_Time

def test_bean_Warning___init__():
    assert bean_Warning.__init__(bean_Warning(0, '\x00', '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()), 0, '', '', '', genmymodelreverse_java_sql_Time(), genmymodelreverse_java_sql_Date()) == None


from python_code import file_FileUploadHandler

def test_file_FileUploadHandler___init__():
    assert file_FileUploadHandler.__init__(file_FileUploadHandler('', '\x00'), '\x00\x00', '') == None


from python_code import network_AcceptRequest

def test_network_AcceptRequest___init__():
    assert network_AcceptRequest.__init__(network_AcceptRequest(0), 0) == None


from python_code import network_Delete

def test_network_Delete___init__():
    assert network_Delete.__init__(network_Delete(0), 0) == None


from python_code import network_DeleteMessComment

def test_network_DeleteMessComment___init__():
    assert network_DeleteMessComment.__init__(network_DeleteMessComment(0), 0) == None


from python_code import network_Like

def test_network_Like___init__():
    assert network_Like.__init__(network_Like(0), 0) == None


from python_code import network_MessageLike

def test_network_MessageLike___init__():
    assert network_MessageLike.__init__(network_MessageLike(0), 0) == None


from python_code import network_MessageUnlike

def test_network_MessageUnlike___init__():
    assert network_MessageUnlike.__init__(network_MessageUnlike(0), 0) == None


from python_code import network_RejectRequest

def test_network_RejectRequest___init__():
    assert network_RejectRequest.__init__(network_RejectRequest(0), 0) == None


from python_code import network_RemoveMessage

def test_network_RemoveMessage___init__():
    assert network_RemoveMessage.__init__(network_RemoveMessage(0), 0) == None


from python_code import network_RemovePost

def test_network_RemovePost___init__():
    assert network_RemovePost.__init__(network_RemovePost(0), 0) == None


from python_code import network_SendRequest

def test_network_SendRequest___init__():
    assert network_SendRequest.__init__(network_SendRequest(0), 0) == None


from python_code import network_Unfriend

def test_network_Unfriend___init__():
    assert network_Unfriend.__init__(network_Unfriend(0), 0) == None


from python_code import network_Unlike

def test_network_Unlike___init__():
    assert network_Unlike.__init__(network_Unlike(0), 0) == None


from python_code import network_UpdateProfession

def test_network_UpdateProfession___init__():
    assert network_UpdateProfession.__init__(network_UpdateProfession(0), 0) == None


from python_code import network_UserRegistration

def test_network_UserRegistration___init__():
    assert network_UserRegistration.__init__(network_UserRegistration(0, '\x00'), 0, '\x00') == None

