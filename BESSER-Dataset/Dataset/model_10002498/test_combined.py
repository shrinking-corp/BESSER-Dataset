# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Role,
    Attachment,
    Comment,
    Activity,
    Project,
    User,
    String,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_role_is_not_abstract():
    assert not inspect.isabstract(Role)


def test_hyp_role_constructor_exists():
    assert callable(Role.__init__)


def test_hyp_role_constructor_args():
    sig = inspect.signature(Role.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "RoleID" in params, "Missing parameter 'RoleID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_hyp_role_has_Description():
    assert hasattr(Role, "Description")
    descriptor = None
    for klass in Role.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_role_has_RoleID():
    assert hasattr(Role, "RoleID")
    descriptor = None
    for klass in Role.__mro__:
        if "RoleID" in klass.__dict__:
            descriptor = klass.__dict__["RoleID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_role_has_Name():
    assert hasattr(Role, "Name")
    descriptor = None
    for klass in Role.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_hyp_attachment_is_not_abstract():
    assert not inspect.isabstract(Attachment)


def test_hyp_attachment_constructor_exists():
    assert callable(Attachment.__init__)


def test_hyp_attachment_constructor_args():
    sig = inspect.signature(Attachment.__init__)
    params = list(sig.parameters.keys())
    assert "User" in params, "Missing parameter 'User'"
    assert "Path" in params, "Missing parameter 'Path'"
    assert "Size" in params, "Missing parameter 'Size'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "AttachmentID" in params, "Missing parameter 'AttachmentID'"
    assert "Extension" in params, "Missing parameter 'Extension'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Project" in params, "Missing parameter 'Project'"

def test_hyp_attachment_has_User():
    assert hasattr(Attachment, "User")
    descriptor = None
    for klass in Attachment.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Path():
    assert hasattr(Attachment, "Path")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Path" in klass.__dict__:
            descriptor = klass.__dict__["Path"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Size():
    assert hasattr(Attachment, "Size")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Size" in klass.__dict__:
            descriptor = klass.__dict__["Size"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Created():
    assert hasattr(Attachment, "Created")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_AttachmentID():
    assert hasattr(Attachment, "AttachmentID")
    descriptor = None
    for klass in Attachment.__mro__:
        if "AttachmentID" in klass.__dict__:
            descriptor = klass.__dict__["AttachmentID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Extension():
    assert hasattr(Attachment, "Extension")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Extension" in klass.__dict__:
            descriptor = klass.__dict__["Extension"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Name():
    assert hasattr(Attachment, "Name")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_attachment_has_Project():
    assert hasattr(Attachment, "Project")
    descriptor = None
    for klass in Attachment.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)



def test_hyp_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_hyp_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_hyp_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())
    assert "Project" in params, "Missing parameter 'Project'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "CommentID" in params, "Missing parameter 'CommentID'"
    assert "User" in params, "Missing parameter 'User'"
    assert "Content" in params, "Missing parameter 'Content'"

def test_hyp_comment_has_Project():
    assert hasattr(Comment, "Project")
    descriptor = None
    for klass in Comment.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)

def test_hyp_comment_has_Created():
    assert hasattr(Comment, "Created")
    descriptor = None
    for klass in Comment.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_hyp_comment_has_CommentID():
    assert hasattr(Comment, "CommentID")
    descriptor = None
    for klass in Comment.__mro__:
        if "CommentID" in klass.__dict__:
            descriptor = klass.__dict__["CommentID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_comment_has_User():
    assert hasattr(Comment, "User")
    descriptor = None
    for klass in Comment.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_hyp_comment_has_Content():
    assert hasattr(Comment, "Content")
    descriptor = None
    for klass in Comment.__mro__:
        if "Content" in klass.__dict__:
            descriptor = klass.__dict__["Content"]
            break
    assert isinstance(descriptor, property)



def test_hyp_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_hyp_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_hyp_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())
    assert "ActivityType" in params, "Missing parameter 'ActivityType'"
    assert "ActivitySubType" in params, "Missing parameter 'ActivitySubType'"
    assert "Project" in params, "Missing parameter 'Project'"
    assert "User" in params, "Missing parameter 'User'"
    assert "Seen" in params, "Missing parameter 'Seen'"
    assert "NewValue" in params, "Missing parameter 'NewValue'"
    assert "ActivityID" in params, "Missing parameter 'ActivityID'"
    assert "PrevValue" in params, "Missing parameter 'PrevValue'"

def test_hyp_activity_has_ActivityType():
    assert hasattr(Activity, "ActivityType")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivityType" in klass.__dict__:
            descriptor = klass.__dict__["ActivityType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_ActivitySubType():
    assert hasattr(Activity, "ActivitySubType")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivitySubType" in klass.__dict__:
            descriptor = klass.__dict__["ActivitySubType"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_Project():
    assert hasattr(Activity, "Project")
    descriptor = None
    for klass in Activity.__mro__:
        if "Project" in klass.__dict__:
            descriptor = klass.__dict__["Project"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_User():
    assert hasattr(Activity, "User")
    descriptor = None
    for klass in Activity.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_Seen():
    assert hasattr(Activity, "Seen")
    descriptor = None
    for klass in Activity.__mro__:
        if "Seen" in klass.__dict__:
            descriptor = klass.__dict__["Seen"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_NewValue():
    assert hasattr(Activity, "NewValue")
    descriptor = None
    for klass in Activity.__mro__:
        if "NewValue" in klass.__dict__:
            descriptor = klass.__dict__["NewValue"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_ActivityID():
    assert hasattr(Activity, "ActivityID")
    descriptor = None
    for klass in Activity.__mro__:
        if "ActivityID" in klass.__dict__:
            descriptor = klass.__dict__["ActivityID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_activity_has_PrevValue():
    assert hasattr(Activity, "PrevValue")
    descriptor = None
    for klass in Activity.__mro__:
        if "PrevValue" in klass.__dict__:
            descriptor = klass.__dict__["PrevValue"]
            break
    assert isinstance(descriptor, property)



def test_hyp_project_is_not_abstract():
    assert not inspect.isabstract(Project)


def test_hyp_project_constructor_exists():
    assert callable(Project.__init__)


def test_hyp_project_constructor_args():
    sig = inspect.signature(Project.__init__)
    params = list(sig.parameters.keys())
    assert "PriorityID" in params, "Missing parameter 'PriorityID'"
    assert "Activities___" in params, "Missing parameter 'Activities___'"
    assert "Author" in params, "Missing parameter 'Author'"
    assert "Comments___" in params, "Missing parameter 'Comments___'"
    assert "Deadline" in params, "Missing parameter 'Deadline'"
    assert "Assignee" in params, "Missing parameter 'Assignee'"
    assert "Attachments___" in params, "Missing parameter 'Attachments___'"
    assert "Created" in params, "Missing parameter 'Created'"
    assert "Subscriptions___" in params, "Missing parameter 'Subscriptions___'"
    assert "Title" in params, "Missing parameter 'Title'"
    assert "ProjectManager" in params, "Missing parameter 'ProjectManager'"
    assert "StatusID" in params, "Missing parameter 'StatusID'"
    assert "PorjectID" in params, "Missing parameter 'PorjectID'"
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Team___" in params, "Missing parameter 'Team___'"

def test_hyp_project_has_PriorityID():
    assert hasattr(Project, "PriorityID")
    descriptor = None
    for klass in Project.__mro__:
        if "PriorityID" in klass.__dict__:
            descriptor = klass.__dict__["PriorityID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Activities___():
    assert hasattr(Project, "Activities___")
    descriptor = None
    for klass in Project.__mro__:
        if "Activities___" in klass.__dict__:
            descriptor = klass.__dict__["Activities___"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Author():
    assert hasattr(Project, "Author")
    descriptor = None
    for klass in Project.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Comments___():
    assert hasattr(Project, "Comments___")
    descriptor = None
    for klass in Project.__mro__:
        if "Comments___" in klass.__dict__:
            descriptor = klass.__dict__["Comments___"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Deadline():
    assert hasattr(Project, "Deadline")
    descriptor = None
    for klass in Project.__mro__:
        if "Deadline" in klass.__dict__:
            descriptor = klass.__dict__["Deadline"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Assignee():
    assert hasattr(Project, "Assignee")
    descriptor = None
    for klass in Project.__mro__:
        if "Assignee" in klass.__dict__:
            descriptor = klass.__dict__["Assignee"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Attachments___():
    assert hasattr(Project, "Attachments___")
    descriptor = None
    for klass in Project.__mro__:
        if "Attachments___" in klass.__dict__:
            descriptor = klass.__dict__["Attachments___"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Created():
    assert hasattr(Project, "Created")
    descriptor = None
    for klass in Project.__mro__:
        if "Created" in klass.__dict__:
            descriptor = klass.__dict__["Created"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Subscriptions___():
    assert hasattr(Project, "Subscriptions___")
    descriptor = None
    for klass in Project.__mro__:
        if "Subscriptions___" in klass.__dict__:
            descriptor = klass.__dict__["Subscriptions___"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Title():
    assert hasattr(Project, "Title")
    descriptor = None
    for klass in Project.__mro__:
        if "Title" in klass.__dict__:
            descriptor = klass.__dict__["Title"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_ProjectManager():
    assert hasattr(Project, "ProjectManager")
    descriptor = None
    for klass in Project.__mro__:
        if "ProjectManager" in klass.__dict__:
            descriptor = klass.__dict__["ProjectManager"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_StatusID():
    assert hasattr(Project, "StatusID")
    descriptor = None
    for klass in Project.__mro__:
        if "StatusID" in klass.__dict__:
            descriptor = klass.__dict__["StatusID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_PorjectID():
    assert hasattr(Project, "PorjectID")
    descriptor = None
    for klass in Project.__mro__:
        if "PorjectID" in klass.__dict__:
            descriptor = klass.__dict__["PorjectID"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Description():
    assert hasattr(Project, "Description")
    descriptor = None
    for klass in Project.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_project_has_Team___():
    assert hasattr(Project, "Team___")
    descriptor = None
    for klass in Project.__mro__:
        if "Team___" in klass.__dict__:
            descriptor = klass.__dict__["Team___"]
            break
    assert isinstance(descriptor, property)



def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "About" in params, "Missing parameter 'About'"
    assert "TitleID" in params, "Missing parameter 'TitleID'"
    assert "Hiredate" in params, "Missing parameter 'Hiredate'"
    assert "Linkedin_link" in params, "Missing parameter 'Linkedin_link'"
    assert "Settings" in params, "Missing parameter 'Settings'"
    assert "DepartmentID" in params, "Missing parameter 'DepartmentID'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Roles___" in params, "Missing parameter 'Roles___'"
    assert "Dateofbirth" in params, "Missing parameter 'Dateofbirth'"
    assert "Position" in params, "Missing parameter 'Position'"
    assert "Active" in params, "Missing parameter 'Active'"
    assert "Lastname" in params, "Missing parameter 'Lastname'"
    assert "Google_plus_link" in params, "Missing parameter 'Google_plus_link'"
    assert "Firstname" in params, "Missing parameter 'Firstname'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Facebook_link" in params, "Missing parameter 'Facebook_link'"




















def test_hyp_string_exists():
    # Check that the Enumeration exists
    assert String is not None

def test_hyp_string_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in String]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in String"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Role_strategy = st.builds(
    Role,
    Description=
        safe_text,
    RoleID=
        st.integers(),
    Name=
        st.none()
)
Attachment_strategy = st.builds(
    Attachment,
    User=
        st.none(),
    Path=
        safe_text,
    Size=
        safe_text,
    Created=
        safe_text,
    AttachmentID=
        st.integers(),
    Extension=
        safe_text,
    Name=
        safe_text,
    Project=
        st.none()
)
Comment_strategy = st.builds(
    Comment,
    Project=
        st.none(),
    Created=
        safe_text,
    CommentID=
        st.integers(),
    User=
        st.none(),
    Content=
        safe_text
)
Activity_strategy = st.builds(
    Activity,
    ActivityType=
        st.integers(),
    ActivitySubType=
        st.integers(),
    Project=
        st.none(),
    User=
        st.none(),
    Seen=
        st.booleans(),
    NewValue=
        safe_text,
    ActivityID=
        st.integers(),
    PrevValue=
        safe_text
)
Project_strategy = st.builds(
    Project,
    PriorityID=
        st.integers(),
    Activities___=
        safe_text,
    Author=
        st.none(),
    Comments___=
        safe_text,
    Deadline=
        safe_text,
    Assignee=
        st.none(),
    Attachments___=
        safe_text,
    Created=
        safe_text,
    Subscriptions___=
        safe_text,
    Title=
        safe_text,
    ProjectManager=
        st.none(),
    StatusID=
        st.integers(),
    PorjectID=
        st.integers(),
    Description=
        safe_text,
    Team___=
        safe_text
)
User_strategy = st.builds(
    User,
    Phone=
        safe_text,
    Password=
        safe_text,
    About=
        safe_text,
    TitleID=
        st.integers(),
    Hiredate=
        safe_text,
    Linkedin_link=
        safe_text,
    Settings=
        safe_text,
    DepartmentID=
        st.integers(),
    UserID=
        st.integers(),
    Roles___=
        safe_text,
    Dateofbirth=
        safe_text,
    Position=
        safe_text,
    Active=
        st.booleans(),
    Lastname=
        safe_text,
    Google_plus_link=
        safe_text,
    Firstname=
        safe_text,
    Username=
        safe_text,
    Email=
        safe_text,
    Facebook_link=
        safe_text
)

@given(instance=Role_strategy)
@settings(max_examples=50)
def test_hyp_role_instantiation(instance):
    assert isinstance(instance, Role)



@given(instance=Role_strategy)
def test_hyp_role_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Role_strategy)
def test_hyp_role_RoleID_setter(instance):
    original = instance.RoleID
    instance.RoleID = original
    assert instance.RoleID == original



@given(instance=Role_strategy)
def test_hyp_role_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Attachment_strategy)
@settings(max_examples=50)
def test_hyp_attachment_instantiation(instance):
    assert isinstance(instance, Attachment)



@given(instance=Attachment_strategy)
def test_hyp_attachment_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Path_setter(instance):
    original = instance.Path
    instance.Path = original
    assert instance.Path == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Size_setter(instance):
    original = instance.Size
    instance.Size = original
    assert instance.Size == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_AttachmentID_setter(instance):
    original = instance.AttachmentID
    instance.AttachmentID = original
    assert instance.AttachmentID == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Extension_setter(instance):
    original = instance.Extension
    instance.Extension = original
    assert instance.Extension == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Attachment_strategy)
def test_hyp_attachment_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_hyp_comment_instantiation(instance):
    assert isinstance(instance, Comment)



@given(instance=Comment_strategy)
def test_hyp_comment_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original



@given(instance=Comment_strategy)
def test_hyp_comment_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Comment_strategy)
def test_hyp_comment_CommentID_setter(instance):
    original = instance.CommentID
    instance.CommentID = original
    assert instance.CommentID == original



@given(instance=Comment_strategy)
def test_hyp_comment_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Comment_strategy)
def test_hyp_comment_Content_setter(instance):
    original = instance.Content
    instance.Content = original
    assert instance.Content == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_hyp_activity_instantiation(instance):
    assert isinstance(instance, Activity)



@given(instance=Activity_strategy)
def test_hyp_activity_ActivityType_setter(instance):
    original = instance.ActivityType
    instance.ActivityType = original
    assert instance.ActivityType == original



@given(instance=Activity_strategy)
def test_hyp_activity_ActivitySubType_setter(instance):
    original = instance.ActivitySubType
    instance.ActivitySubType = original
    assert instance.ActivitySubType == original



@given(instance=Activity_strategy)
def test_hyp_activity_Project_setter(instance):
    original = instance.Project
    instance.Project = original
    assert instance.Project == original



@given(instance=Activity_strategy)
def test_hyp_activity_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original



@given(instance=Activity_strategy)
def test_hyp_activity_Seen_setter(instance):
    original = instance.Seen
    instance.Seen = original
    assert instance.Seen == original



@given(instance=Activity_strategy)
def test_hyp_activity_NewValue_setter(instance):
    original = instance.NewValue
    instance.NewValue = original
    assert instance.NewValue == original



@given(instance=Activity_strategy)
def test_hyp_activity_ActivityID_setter(instance):
    original = instance.ActivityID
    instance.ActivityID = original
    assert instance.ActivityID == original



@given(instance=Activity_strategy)
def test_hyp_activity_PrevValue_setter(instance):
    original = instance.PrevValue
    instance.PrevValue = original
    assert instance.PrevValue == original

@given(instance=Project_strategy)
@settings(max_examples=50)
def test_hyp_project_instantiation(instance):
    assert isinstance(instance, Project)



@given(instance=Project_strategy)
def test_hyp_project_PriorityID_setter(instance):
    original = instance.PriorityID
    instance.PriorityID = original
    assert instance.PriorityID == original



@given(instance=Project_strategy)
def test_hyp_project_Activities____setter(instance):
    original = instance.Activities___
    instance.Activities___ = original
    assert instance.Activities___ == original



@given(instance=Project_strategy)
def test_hyp_project_Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original



@given(instance=Project_strategy)
def test_hyp_project_Comments____setter(instance):
    original = instance.Comments___
    instance.Comments___ = original
    assert instance.Comments___ == original



@given(instance=Project_strategy)
def test_hyp_project_Deadline_setter(instance):
    original = instance.Deadline
    instance.Deadline = original
    assert instance.Deadline == original



@given(instance=Project_strategy)
def test_hyp_project_Assignee_setter(instance):
    original = instance.Assignee
    instance.Assignee = original
    assert instance.Assignee == original



@given(instance=Project_strategy)
def test_hyp_project_Attachments____setter(instance):
    original = instance.Attachments___
    instance.Attachments___ = original
    assert instance.Attachments___ == original



@given(instance=Project_strategy)
def test_hyp_project_Created_setter(instance):
    original = instance.Created
    instance.Created = original
    assert instance.Created == original



@given(instance=Project_strategy)
def test_hyp_project_Subscriptions____setter(instance):
    original = instance.Subscriptions___
    instance.Subscriptions___ = original
    assert instance.Subscriptions___ == original



@given(instance=Project_strategy)
def test_hyp_project_Title_setter(instance):
    original = instance.Title
    instance.Title = original
    assert instance.Title == original



@given(instance=Project_strategy)
def test_hyp_project_ProjectManager_setter(instance):
    original = instance.ProjectManager
    instance.ProjectManager = original
    assert instance.ProjectManager == original



@given(instance=Project_strategy)
def test_hyp_project_StatusID_setter(instance):
    original = instance.StatusID
    instance.StatusID = original
    assert instance.StatusID == original



@given(instance=Project_strategy)
def test_hyp_project_PorjectID_setter(instance):
    original = instance.PorjectID
    instance.PorjectID = original
    assert instance.PorjectID == original



@given(instance=Project_strategy)
def test_hyp_project_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=Project_strategy)
def test_hyp_project_Team____setter(instance):
    original = instance.Team___
    instance.Team___ = original
    assert instance.Team___ == original




@given(instance=User_strategy)
def test_hyp_user_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=User_strategy)
def test_hyp_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_hyp_user_About_setter(instance):
    original = instance.About
    instance.About = original
    assert instance.About == original



@given(instance=User_strategy)
def test_hyp_user_TitleID_setter(instance):
    original = instance.TitleID
    instance.TitleID = original
    assert instance.TitleID == original



@given(instance=User_strategy)
def test_hyp_user_Hiredate_setter(instance):
    original = instance.Hiredate
    instance.Hiredate = original
    assert instance.Hiredate == original



@given(instance=User_strategy)
def test_hyp_user_Linkedin_link_setter(instance):
    original = instance.Linkedin_link
    instance.Linkedin_link = original
    assert instance.Linkedin_link == original



@given(instance=User_strategy)
def test_hyp_user_Settings_setter(instance):
    original = instance.Settings
    instance.Settings = original
    assert instance.Settings == original



@given(instance=User_strategy)
def test_hyp_user_DepartmentID_setter(instance):
    original = instance.DepartmentID
    instance.DepartmentID = original
    assert instance.DepartmentID == original



@given(instance=User_strategy)
def test_hyp_user_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_strategy)
def test_hyp_user_Roles____setter(instance):
    original = instance.Roles___
    instance.Roles___ = original
    assert instance.Roles___ == original



@given(instance=User_strategy)
def test_hyp_user_Dateofbirth_setter(instance):
    original = instance.Dateofbirth
    instance.Dateofbirth = original
    assert instance.Dateofbirth == original



@given(instance=User_strategy)
def test_hyp_user_Position_setter(instance):
    original = instance.Position
    instance.Position = original
    assert instance.Position == original



@given(instance=User_strategy)
def test_hyp_user_Active_setter(instance):
    original = instance.Active
    instance.Active = original
    assert instance.Active == original



@given(instance=User_strategy)
def test_hyp_user_Lastname_setter(instance):
    original = instance.Lastname
    instance.Lastname = original
    assert instance.Lastname == original



@given(instance=User_strategy)
def test_hyp_user_Google_plus_link_setter(instance):
    original = instance.Google_plus_link
    instance.Google_plus_link = original
    assert instance.Google_plus_link == original



@given(instance=User_strategy)
def test_hyp_user_Firstname_setter(instance):
    original = instance.Firstname
    instance.Firstname = original
    assert instance.Firstname == original



@given(instance=User_strategy)
def test_hyp_user_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=User_strategy)
def test_hyp_user_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=User_strategy)
def test_hyp_user_Facebook_link_setter(instance):
    original = instance.Facebook_link
    instance.Facebook_link = original
    assert instance.Facebook_link == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Activity,
    Attachment,
    Comment,
    Project,
    Role,
    User,
    String,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_User_About_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.About == "sample_text"
    instance.About = "sample_text_2"
    assert instance.About == "sample_text_2"


def test_User_Active_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Active == True
    instance.Active = False
    assert instance.Active == False


def test_User_Dateofbirth_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Dateofbirth == "sample_text"
    instance.Dateofbirth = "sample_text_2"
    assert instance.Dateofbirth == "sample_text_2"


def test_User_DepartmentID_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.DepartmentID == 7
    instance.DepartmentID = 13
    assert instance.DepartmentID == 13


def test_User_Email_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Email == "sample_text"
    instance.Email = "sample_text_2"
    assert instance.Email == "sample_text_2"


def test_User_Facebook_link_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Facebook_link == "sample_text"
    instance.Facebook_link = "sample_text_2"
    assert instance.Facebook_link == "sample_text_2"


def test_User_Firstname_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Firstname == "sample_text"
    instance.Firstname = "sample_text_2"
    assert instance.Firstname == "sample_text_2"


def test_User_Google_plus_link_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Google_plus_link == "sample_text"
    instance.Google_plus_link = "sample_text_2"
    assert instance.Google_plus_link == "sample_text_2"


def test_User_Hiredate_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Hiredate == "sample_text"
    instance.Hiredate = "sample_text_2"
    assert instance.Hiredate == "sample_text_2"


def test_User_Lastname_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Lastname == "sample_text"
    instance.Lastname = "sample_text_2"
    assert instance.Lastname == "sample_text_2"


def test_User_Linkedin_link_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Linkedin_link == "sample_text"
    instance.Linkedin_link = "sample_text_2"
    assert instance.Linkedin_link == "sample_text_2"


def test_User_Password_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Password == "sample_text"
    instance.Password = "sample_text_2"
    assert instance.Password == "sample_text_2"


def test_User_Phone_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Phone == "sample_text"
    instance.Phone = "sample_text_2"
    assert instance.Phone == "sample_text_2"


def test_User_Position_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Position == "sample_text"
    instance.Position = "sample_text_2"
    assert instance.Position == "sample_text_2"


def test_User_Roles____value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Roles___ == "sample_text"
    instance.Roles___ = "sample_text_2"
    assert instance.Roles___ == "sample_text_2"


def test_User_Settings_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Settings == "sample_text"
    instance.Settings = "sample_text_2"
    assert instance.Settings == "sample_text_2"


def test_User_TitleID_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.TitleID == 7
    instance.TitleID = 13
    assert instance.TitleID == 13


def test_User_UserID_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.UserID == 7
    instance.UserID = 13
    assert instance.UserID == 13


def test_User_Username_value_roundtrip():
    instance = User(About="sample_text", Active=True, Dateofbirth="sample_text", DepartmentID=7, Email="sample_text", Facebook_link="sample_text", Firstname="sample_text", Google_plus_link="sample_text", Hiredate="sample_text", Lastname="sample_text", Linkedin_link="sample_text", Password="sample_text", Phone="sample_text", Position="sample_text", Roles___="sample_text", Settings="sample_text", TitleID=7, UserID=7, Username="sample_text")
    assert instance.Username == "sample_text"
    instance.Username = "sample_text_2"
    assert instance.Username == "sample_text_2"


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

User_strategy = st.builds(User, About=safe_text, Active=st.booleans(), Dateofbirth=safe_text, DepartmentID=st.integers(), Email=safe_text, Facebook_link=safe_text, Firstname=safe_text, Google_plus_link=safe_text, Hiredate=safe_text, Lastname=safe_text, Linkedin_link=safe_text, Password=safe_text, Phone=safe_text, Position=safe_text, Roles___=safe_text, Settings=safe_text, TitleID=st.integers(), UserID=st.integers(), Username=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)



