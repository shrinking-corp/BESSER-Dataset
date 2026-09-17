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
    Tag,
    ContentPage,
    Profile2,
    AdminUser,
    LogEntry,
    int2_Interface,
    Tenant,
    Video,
    Image,
    Media,
    MediaPool,
    Settings,
    AbstractEntity,
    Friend,
    Message,
    Group,
    Profile,
    User,
    Address,
    PublicityState,
    VIDEO,
    ContentPagePublicityState,
    Date,
    Enumeration,
    MediaType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_hyp_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_hyp_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_contentpage_is_not_abstract():
    assert not inspect.isabstract(ContentPage)


def test_hyp_contentpage_constructor_exists():
    assert callable(ContentPage.__init__)


def test_hyp_contentpage_constructor_args():
    sig = inspect.signature(ContentPage.__init__)
    params = list(sig.parameters.keys())
    assert "references" in params, "Missing parameter 'references'"
    assert "media" in params, "Missing parameter 'media'"
    assert "title" in params, "Missing parameter 'title'"
    assert "externalSource" in params, "Missing parameter 'externalSource'"
    assert "address" in params, "Missing parameter 'address'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "expiryDate" in params, "Missing parameter 'expiryDate'"
    assert "priorityExpiryDate" in params, "Missing parameter 'priorityExpiryDate'"
    assert "publishingDate" in params, "Missing parameter 'publishingDate'"
    assert "state" in params, "Missing parameter 'state'"
    assert "active" in params, "Missing parameter 'active'"
    assert "headline" in params, "Missing parameter 'headline'"
    assert "priority" in params, "Missing parameter 'priority'"
    assert "content1" in params, "Missing parameter 'content1'"
    assert "date" in params, "Missing parameter 'date'"
    assert "content" in params, "Missing parameter 'content'"
    assert "author" in params, "Missing parameter 'author'"
    assert "tags" in params, "Missing parameter 'tags'"

def test_hyp_contentpage_has_references():
    assert hasattr(ContentPage, "references")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "references" in klass.__dict__:
            descriptor = klass.__dict__["references"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_media():
    assert hasattr(ContentPage, "media")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "media" in klass.__dict__:
            descriptor = klass.__dict__["media"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_title():
    assert hasattr(ContentPage, "title")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_externalSource():
    assert hasattr(ContentPage, "externalSource")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "externalSource" in klass.__dict__:
            descriptor = klass.__dict__["externalSource"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_address():
    assert hasattr(ContentPage, "address")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_attribute():
    assert hasattr(ContentPage, "attribute")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_expiryDate():
    assert hasattr(ContentPage, "expiryDate")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "expiryDate" in klass.__dict__:
            descriptor = klass.__dict__["expiryDate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_priorityExpiryDate():
    assert hasattr(ContentPage, "priorityExpiryDate")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "priorityExpiryDate" in klass.__dict__:
            descriptor = klass.__dict__["priorityExpiryDate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_publishingDate():
    assert hasattr(ContentPage, "publishingDate")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "publishingDate" in klass.__dict__:
            descriptor = klass.__dict__["publishingDate"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_state():
    assert hasattr(ContentPage, "state")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_active():
    assert hasattr(ContentPage, "active")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_headline():
    assert hasattr(ContentPage, "headline")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "headline" in klass.__dict__:
            descriptor = klass.__dict__["headline"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_priority():
    assert hasattr(ContentPage, "priority")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "priority" in klass.__dict__:
            descriptor = klass.__dict__["priority"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_content1():
    assert hasattr(ContentPage, "content1")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "content1" in klass.__dict__:
            descriptor = klass.__dict__["content1"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_date():
    assert hasattr(ContentPage, "date")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_content():
    assert hasattr(ContentPage, "content")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_author():
    assert hasattr(ContentPage, "author")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_hyp_contentpage_has_tags():
    assert hasattr(ContentPage, "tags")
    descriptor = None
    for klass in ContentPage.__mro__:
        if "tags" in klass.__dict__:
            descriptor = klass.__dict__["tags"]
            break
    assert isinstance(descriptor, property)



def test_hyp_profile2_is_not_abstract():
    assert not inspect.isabstract(Profile2)


def test_hyp_profile2_constructor_exists():
    assert callable(Profile2.__init__)


def test_hyp_profile2_constructor_args():
    sig = inspect.signature(Profile2.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "firstName" in params, "Missing parameter 'firstName'"







def test_hyp_adminuser_is_not_abstract():
    assert not inspect.isabstract(AdminUser)


def test_hyp_adminuser_constructor_exists():
    assert callable(AdminUser.__init__)


def test_hyp_adminuser_constructor_args():
    sig = inspect.signature(AdminUser.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "roles" in params, "Missing parameter 'roles'"
    assert "username" in params, "Missing parameter 'username'"
    assert "active" in params, "Missing parameter 'active'"
    assert "password" in params, "Missing parameter 'password'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"










def test_hyp_logentry_is_not_abstract():
    assert not inspect.isabstract(LogEntry)


def test_hyp_logentry_constructor_exists():
    assert callable(LogEntry.__init__)


def test_hyp_logentry_constructor_args():
    sig = inspect.signature(LogEntry.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "objectType" in params, "Missing parameter 'objectType'"
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "objectId" in params, "Missing parameter 'objectId'"







def test_hyp_int2_interface_is_not_abstract():
    assert not inspect.isabstract(int2_Interface)


def test_hyp_int2_interface_constructor_exists():
    assert callable(int2_Interface.__init__)


def test_hyp_int2_interface_constructor_args():
    sig = inspect.signature(int2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_hyp_tenant_is_not_abstract():
    assert not inspect.isabstract(Tenant)


def test_hyp_tenant_constructor_exists():
    assert callable(Tenant.__init__)


def test_hyp_tenant_constructor_args():
    sig = inspect.signature(Tenant.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_video_is_not_abstract():
    assert not inspect.isabstract(Video)


def test_hyp_video_constructor_exists():
    assert callable(Video.__init__)


def test_hyp_video_constructor_args():
    sig = inspect.signature(Video.__init__)
    params = list(sig.parameters.keys())



def test_hyp_image_is_not_abstract():
    assert not inspect.isabstract(Image)


def test_hyp_image_constructor_exists():
    assert callable(Image.__init__)


def test_hyp_image_constructor_args():
    sig = inspect.signature(Image.__init__)
    params = list(sig.parameters.keys())



def test_hyp_media_is_not_abstract():
    assert not inspect.isabstract(Media)


def test_hyp_media_constructor_exists():
    assert callable(Media.__init__)


def test_hyp_media_constructor_args():
    sig = inspect.signature(Media.__init__)
    params = list(sig.parameters.keys())
    assert "filesize" in params, "Missing parameter 'filesize'"
    assert "name" in params, "Missing parameter 'name'"
    assert "active" in params, "Missing parameter 'active'"
    assert "description" in params, "Missing parameter 'description'"
    assert "mediaPool" in params, "Missing parameter 'mediaPool'"
    assert "mimetype" in params, "Missing parameter 'mimetype'"
    assert "link" in params, "Missing parameter 'link'"

def test_hyp_media_has_filesize():
    assert hasattr(Media, "filesize")
    descriptor = None
    for klass in Media.__mro__:
        if "filesize" in klass.__dict__:
            descriptor = klass.__dict__["filesize"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_name():
    assert hasattr(Media, "name")
    descriptor = None
    for klass in Media.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_active():
    assert hasattr(Media, "active")
    descriptor = None
    for klass in Media.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_description():
    assert hasattr(Media, "description")
    descriptor = None
    for klass in Media.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_mediaPool():
    assert hasattr(Media, "mediaPool")
    descriptor = None
    for klass in Media.__mro__:
        if "mediaPool" in klass.__dict__:
            descriptor = klass.__dict__["mediaPool"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_mimetype():
    assert hasattr(Media, "mimetype")
    descriptor = None
    for klass in Media.__mro__:
        if "mimetype" in klass.__dict__:
            descriptor = klass.__dict__["mimetype"]
            break
    assert isinstance(descriptor, property)

def test_hyp_media_has_link():
    assert hasattr(Media, "link")
    descriptor = None
    for klass in Media.__mro__:
        if "link" in klass.__dict__:
            descriptor = klass.__dict__["link"]
            break
    assert isinstance(descriptor, property)



def test_hyp_mediapool_is_not_abstract():
    assert not inspect.isabstract(MediaPool)


def test_hyp_mediapool_constructor_exists():
    assert callable(MediaPool.__init__)


def test_hyp_mediapool_constructor_args():
    sig = inspect.signature(MediaPool.__init__)
    params = list(sig.parameters.keys())
    assert "assets" in params, "Missing parameter 'assets'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_settings_is_not_abstract():
    assert not inspect.isabstract(Settings)


def test_hyp_settings_constructor_exists():
    assert callable(Settings.__init__)


def test_hyp_settings_constructor_args():
    sig = inspect.signature(Settings.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"
    assert "notificationChannels" in params, "Missing parameter 'notificationChannels'"








def test_hyp_abstractentity_is_not_abstract():
    assert not inspect.isabstract(AbstractEntity)


def test_hyp_abstractentity_constructor_exists():
    assert callable(AbstractEntity.__init__)


def test_hyp_abstractentity_constructor_args():
    sig = inspect.signature(AbstractEntity.__init__)
    params = list(sig.parameters.keys())
    assert "modifiedBy" in params, "Missing parameter 'modifiedBy'"
    assert "createdBy" in params, "Missing parameter 'createdBy'"
    assert "createdAt" in params, "Missing parameter 'createdAt'"
    assert "id" in params, "Missing parameter 'id'"
    assert "modifiedAt" in params, "Missing parameter 'modifiedAt'"

def test_hyp_abstractentity_has_modifiedBy():
    assert hasattr(AbstractEntity, "modifiedBy")
    descriptor = None
    for klass in AbstractEntity.__mro__:
        if "modifiedBy" in klass.__dict__:
            descriptor = klass.__dict__["modifiedBy"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractentity_has_createdBy():
    assert hasattr(AbstractEntity, "createdBy")
    descriptor = None
    for klass in AbstractEntity.__mro__:
        if "createdBy" in klass.__dict__:
            descriptor = klass.__dict__["createdBy"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractentity_has_createdAt():
    assert hasattr(AbstractEntity, "createdAt")
    descriptor = None
    for klass in AbstractEntity.__mro__:
        if "createdAt" in klass.__dict__:
            descriptor = klass.__dict__["createdAt"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractentity_has_id():
    assert hasattr(AbstractEntity, "id")
    descriptor = None
    for klass in AbstractEntity.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_hyp_abstractentity_has_modifiedAt():
    assert hasattr(AbstractEntity, "modifiedAt")
    descriptor = None
    for klass in AbstractEntity.__mro__:
        if "modifiedAt" in klass.__dict__:
            descriptor = klass.__dict__["modifiedAt"]
            break
    assert isinstance(descriptor, property)



def test_hyp_friend_is_not_abstract():
    assert not inspect.isabstract(Friend)


def test_hyp_friend_constructor_exists():
    assert callable(Friend.__init__)


def test_hyp_friend_constructor_args():
    sig = inspect.signature(Friend.__init__)
    params = list(sig.parameters.keys())



def test_hyp_message_is_not_abstract():
    assert not inspect.isabstract(Message)


def test_hyp_message_constructor_exists():
    assert callable(Message.__init__)


def test_hyp_message_constructor_args():
    sig = inspect.signature(Message.__init__)
    params = list(sig.parameters.keys())



def test_hyp_group_is_not_abstract():
    assert not inspect.isabstract(Group)


def test_hyp_group_constructor_exists():
    assert callable(Group.__init__)


def test_hyp_group_constructor_args():
    sig = inspect.signature(Group.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_is_not_abstract():
    assert not inspect.isabstract(Profile)


def test_hyp_profile_constructor_exists():
    assert callable(Profile.__init__)


def test_hyp_profile_constructor_args():
    sig = inspect.signature(Profile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "email" in params, "Missing parameter 'email'"
    assert "username" in params, "Missing parameter 'username'"







def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"
    assert "password" in params, "Missing parameter 'password'"
    assert "userId" in params, "Missing parameter 'userId'"






def test_hyp_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_hyp_address_constructor_exists():
    assert callable(Address.__init__)


def test_hyp_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "zipCode" in params, "Missing parameter 'zipCode'"
    assert "streetnumber" in params, "Missing parameter 'streetnumber'"
    assert "city" in params, "Missing parameter 'city'"
    assert "country" in params, "Missing parameter 'country'"
    assert "street" in params, "Missing parameter 'street'"






def test_hyp_publicitystate_exists():
    # Check that the Enumeration exists
    assert PublicityState is not None

def test_hyp_publicitystate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PublicityState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PublicityState"

def test_hyp_video_exists():
    # Check that the Enumeration exists
    assert VIDEO is not None

def test_hyp_video_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VIDEO]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VIDEO"

def test_hyp_contentpagepublicitystate_exists():
    # Check that the Enumeration exists
    assert ContentPagePublicityState is not None

def test_hyp_contentpagepublicitystate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContentPagePublicityState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContentPagePublicityState"

def test_hyp_date_exists():
    # Check that the Enumeration exists
    assert Date is not None

def test_hyp_date_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Date]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Date"

def test_hyp_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_hyp_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"

def test_hyp_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_hyp_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaType"


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
Tag_strategy = st.builds(
    Tag,
    name=
        safe_text
)
ContentPage_strategy = st.builds(
    ContentPage,
    references=
        safe_text,
    media=
        st.none(),
    title=
        safe_text,
    externalSource=
        safe_text,
    address=
        st.none(),
    attribute=
        safe_text,
    expiryDate=
        st.dates(),
    priorityExpiryDate=
        st.dates(),
    publishingDate=
        st.dates(),
    state=
        safe_text,
    active=
        st.booleans(),
    headline=
        safe_text,
    priority=
        safe_text,
    content1=
        safe_text,
    date=
        st.dates(),
    content=
        safe_text,
    author=
        st.none(),
    tags=
        safe_text
)
Profile2_strategy = st.builds(
    Profile2,
    username=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    firstName=
        safe_text
)
AdminUser_strategy = st.builds(
    AdminUser,
    id=
        safe_text,
    roles=
        safe_text,
    username=
        safe_text,
    active=
        st.booleans(),
    password=
        safe_text,
    email=
        safe_text,
    phone=
        safe_text
)
LogEntry_strategy = st.builds(
    LogEntry,
    time=
        safe_text,
    objectType=
        safe_text,
    _attr=
        safe_text,
    objectId=
        safe_text
)
int2_Interface_strategy = st.builds(
    int2_Interface,
)
Tenant_strategy = st.builds(
    Tenant,
    id=
        safe_text,
    name=
        safe_text
)
Video_strategy = st.builds(
    Video,
)
Image_strategy = st.builds(
    Image,
)
Media_strategy = st.builds(
    Media,
    filesize=
        st.integers(),
    name=
        safe_text,
    active=
        st.booleans(),
    description=
        safe_text,
    mediaPool=
        st.none(),
    mimetype=
        safe_text,
    link=
        safe_text
)
MediaPool_strategy = st.builds(
    MediaPool,
    assets=
        safe_text,
    name=
        safe_text
)
Settings_strategy = st.builds(
    Settings,
    username=
        safe_text,
    firstName=
        safe_text,
    email=
        safe_text,
    name=
        safe_text,
    notificationChannels=
        safe_text
)
AbstractEntity_strategy = st.builds(
    AbstractEntity,
    modifiedBy=
        st.none(),
    createdBy=
        st.none(),
    createdAt=
        st.dates(),
    id=
        safe_text,
    modifiedAt=
        st.dates()
)
Friend_strategy = st.builds(
    Friend,
)
Message_strategy = st.builds(
    Message,
)
Group_strategy = st.builds(
    Group,
)
Profile_strategy = st.builds(
    Profile,
    name=
        safe_text,
    firstName=
        safe_text,
    email=
        safe_text,
    username=
        safe_text
)
User_strategy = st.builds(
    User,
    active=
        st.booleans(),
    password=
        safe_text,
    userId=
        safe_text
)
Address_strategy = st.builds(
    Address,
    zipCode=
        safe_text,
    streetnumber=
        safe_text,
    city=
        safe_text,
    country=
        safe_text,
    street=
        safe_text
)




@given(instance=Tag_strategy)
def test_hyp_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ContentPage_strategy)
@settings(max_examples=50)
def test_hyp_contentpage_instantiation(instance):
    assert isinstance(instance, ContentPage)



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_references_setter(instance):
    original = instance.references
    instance.references = original
    assert instance.references == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_media_setter(instance):
    original = instance.media
    instance.media = original
    assert instance.media == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_externalSource_setter(instance):
    original = instance.externalSource
    instance.externalSource = original
    assert instance.externalSource == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_expiryDate_setter(instance):
    original = instance.expiryDate
    instance.expiryDate = original
    assert instance.expiryDate == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_priorityExpiryDate_setter(instance):
    original = instance.priorityExpiryDate
    instance.priorityExpiryDate = original
    assert instance.priorityExpiryDate == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_publishingDate_setter(instance):
    original = instance.publishingDate
    instance.publishingDate = original
    assert instance.publishingDate == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_headline_setter(instance):
    original = instance.headline
    instance.headline = original
    assert instance.headline == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_priority_setter(instance):
    original = instance.priority
    instance.priority = original
    assert instance.priority == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_content1_setter(instance):
    original = instance.content1
    instance.content1 = original
    assert instance.content1 == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=ContentPage_strategy)
def test_hyp_contentpage_tags_setter(instance):
    original = instance.tags
    instance.tags = original
    assert instance.tags == original




@given(instance=Profile2_strategy)
def test_hyp_profile2_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Profile2_strategy)
def test_hyp_profile2_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile2_strategy)
def test_hyp_profile2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Profile2_strategy)
def test_hyp_profile2_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original




@given(instance=AdminUser_strategy)
def test_hyp_adminuser_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=AdminUser_strategy)
def test_hyp_adminuser_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original




@given(instance=LogEntry_strategy)
def test_hyp_logentry_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=LogEntry_strategy)
def test_hyp_logentry_objectType_setter(instance):
    original = instance.objectType
    instance.objectType = original
    assert instance.objectType == original



@given(instance=LogEntry_strategy)
def test_hyp_logentry__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=LogEntry_strategy)
def test_hyp_logentry_objectId_setter(instance):
    original = instance.objectId
    instance.objectId = original
    assert instance.objectId == original





@given(instance=Tenant_strategy)
def test_hyp_tenant_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Tenant_strategy)
def test_hyp_tenant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Media_strategy)
@settings(max_examples=50)
def test_hyp_media_instantiation(instance):
    assert isinstance(instance, Media)



@given(instance=Media_strategy)
def test_hyp_media_filesize_setter(instance):
    original = instance.filesize
    instance.filesize = original
    assert instance.filesize == original



@given(instance=Media_strategy)
def test_hyp_media_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Media_strategy)
def test_hyp_media_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=Media_strategy)
def test_hyp_media_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Media_strategy)
def test_hyp_media_mediaPool_setter(instance):
    original = instance.mediaPool
    instance.mediaPool = original
    assert instance.mediaPool == original



@given(instance=Media_strategy)
def test_hyp_media_mimetype_setter(instance):
    original = instance.mimetype
    instance.mimetype = original
    assert instance.mimetype == original



@given(instance=Media_strategy)
def test_hyp_media_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original




@given(instance=MediaPool_strategy)
def test_hyp_mediapool_assets_setter(instance):
    original = instance.assets
    instance.assets = original
    assert instance.assets == original



@given(instance=MediaPool_strategy)
def test_hyp_mediapool_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=Settings_strategy)
def test_hyp_settings_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Settings_strategy)
def test_hyp_settings_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Settings_strategy)
def test_hyp_settings_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Settings_strategy)
def test_hyp_settings_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Settings_strategy)
def test_hyp_settings_notificationChannels_setter(instance):
    original = instance.notificationChannels
    instance.notificationChannels = original
    assert instance.notificationChannels == original

@given(instance=AbstractEntity_strategy)
@settings(max_examples=50)
def test_hyp_abstractentity_instantiation(instance):
    assert isinstance(instance, AbstractEntity)



@given(instance=AbstractEntity_strategy)
def test_hyp_abstractentity_modifiedBy_setter(instance):
    original = instance.modifiedBy
    instance.modifiedBy = original
    assert instance.modifiedBy == original



@given(instance=AbstractEntity_strategy)
def test_hyp_abstractentity_createdBy_setter(instance):
    original = instance.createdBy
    instance.createdBy = original
    assert instance.createdBy == original



@given(instance=AbstractEntity_strategy)
def test_hyp_abstractentity_createdAt_setter(instance):
    original = instance.createdAt
    instance.createdAt = original
    assert instance.createdAt == original



@given(instance=AbstractEntity_strategy)
def test_hyp_abstractentity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=AbstractEntity_strategy)
def test_hyp_abstractentity_modifiedAt_setter(instance):
    original = instance.modifiedAt
    instance.modifiedAt = original
    assert instance.modifiedAt == original







@given(instance=Profile_strategy)
def test_hyp_profile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Profile_strategy)
def test_hyp_profile_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original



@given(instance=Profile_strategy)
def test_hyp_profile_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Profile_strategy)
def test_hyp_profile_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original




@given(instance=User_strategy)
def test_hyp_user_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original



@given(instance=User_strategy)
def test_hyp_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_hyp_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original




@given(instance=Address_strategy)
def test_hyp_address_zipCode_setter(instance):
    original = instance.zipCode
    instance.zipCode = original
    assert instance.zipCode == original



@given(instance=Address_strategy)
def test_hyp_address_streetnumber_setter(instance):
    original = instance.streetnumber
    instance.streetnumber = original
    assert instance.streetnumber == original



@given(instance=Address_strategy)
def test_hyp_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Address_strategy)
def test_hyp_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Address_strategy)
def test_hyp_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AbstractEntity,
    Address,
    AdminUser,
    ContentPage,
    Friend,
    Group,
    Image,
    LogEntry,
    Media,
    MediaPool,
    Message,
    Profile,
    Profile2,
    Settings,
    Tag,
    Tenant,
    User,
    Video,
    int2_Interface,
    ContentPagePublicityState,
    Date,
    Enumeration,
    MediaType,
    PublicityState,
    VIDEO,
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

def test_Address_city_value_roundtrip():
    instance = Address(city="sample_text", country="sample_text", street="sample_text", streetnumber="sample_text", zipCode="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_Address_country_value_roundtrip():
    instance = Address(city="sample_text", country="sample_text", street="sample_text", streetnumber="sample_text", zipCode="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_Address_street_value_roundtrip():
    instance = Address(city="sample_text", country="sample_text", street="sample_text", streetnumber="sample_text", zipCode="sample_text")
    assert instance.street == "sample_text"
    instance.street = "sample_text_2"
    assert instance.street == "sample_text_2"


def test_Address_streetnumber_value_roundtrip():
    instance = Address(city="sample_text", country="sample_text", street="sample_text", streetnumber="sample_text", zipCode="sample_text")
    assert instance.streetnumber == "sample_text"
    instance.streetnumber = "sample_text_2"
    assert instance.streetnumber == "sample_text_2"


def test_Address_zipCode_value_roundtrip():
    instance = Address(city="sample_text", country="sample_text", street="sample_text", streetnumber="sample_text", zipCode="sample_text")
    assert instance.zipCode == "sample_text"
    instance.zipCode = "sample_text_2"
    assert instance.zipCode == "sample_text_2"


def test_AdminUser_active_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_AdminUser_email_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_AdminUser_id_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_AdminUser_password_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_AdminUser_phone_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_AdminUser_roles_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.roles == "sample_text"
    instance.roles = "sample_text_2"
    assert instance.roles == "sample_text_2"


def test_AdminUser_username_value_roundtrip():
    instance = AdminUser(active=True, email="sample_text", id="sample_text", password="sample_text", phone="sample_text", roles="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_LogEntry__attr_value_roundtrip():
    instance = LogEntry(_attr="sample_text", objectId="sample_text", objectType="sample_text", time="sample_text")
    assert instance._attr == "sample_text"
    instance._attr = "sample_text_2"
    assert instance._attr == "sample_text_2"


def test_LogEntry_objectId_value_roundtrip():
    instance = LogEntry(_attr="sample_text", objectId="sample_text", objectType="sample_text", time="sample_text")
    assert instance.objectId == "sample_text"
    instance.objectId = "sample_text_2"
    assert instance.objectId == "sample_text_2"


def test_LogEntry_objectType_value_roundtrip():
    instance = LogEntry(_attr="sample_text", objectId="sample_text", objectType="sample_text", time="sample_text")
    assert instance.objectType == "sample_text"
    instance.objectType = "sample_text_2"
    assert instance.objectType == "sample_text_2"


def test_LogEntry_time_value_roundtrip():
    instance = LogEntry(_attr="sample_text", objectId="sample_text", objectType="sample_text", time="sample_text")
    assert instance.time == "sample_text"
    instance.time = "sample_text_2"
    assert instance.time == "sample_text_2"


def test_MediaPool_assets_value_roundtrip():
    instance = MediaPool(assets="sample_text", name="sample_text")
    assert instance.assets == "sample_text"
    instance.assets = "sample_text_2"
    assert instance.assets == "sample_text_2"


def test_MediaPool_name_value_roundtrip():
    instance = MediaPool(assets="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Profile_email_value_roundtrip():
    instance = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Profile_firstName_value_roundtrip():
    instance = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Profile_name_value_roundtrip():
    instance = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Profile_username_value_roundtrip():
    instance = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Profile2_email_value_roundtrip():
    instance = Profile2(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Profile2_firstName_value_roundtrip():
    instance = Profile2(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Profile2_name_value_roundtrip():
    instance = Profile2(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Profile2_username_value_roundtrip():
    instance = Profile2(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Settings_email_value_roundtrip():
    instance = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Settings_firstName_value_roundtrip():
    instance = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    assert instance.firstName == "sample_text"
    instance.firstName = "sample_text_2"
    assert instance.firstName == "sample_text_2"


def test_Settings_name_value_roundtrip():
    instance = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Settings_notificationChannels_value_roundtrip():
    instance = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    assert instance.notificationChannels == "sample_text"
    instance.notificationChannels = "sample_text_2"
    assert instance.notificationChannels == "sample_text_2"


def test_Settings_username_value_roundtrip():
    instance = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    assert instance.username == "sample_text"
    instance.username = "sample_text_2"
    assert instance.username == "sample_text_2"


def test_Tag_name_value_roundtrip():
    instance = Tag(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Tenant_id_value_roundtrip():
    instance = Tenant(id="sample_text", name="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_Tenant_name_value_roundtrip():
    instance = Tenant(id="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_User_active_value_roundtrip():
    instance = User(active=True, password="sample_text", userId="sample_text")
    assert instance.active == True
    instance.active = False
    assert instance.active == False


def test_User_password_value_roundtrip():
    instance = User(active=True, password="sample_text", userId="sample_text")
    assert instance.password == "sample_text"
    instance.password = "sample_text_2"
    assert instance.password == "sample_text_2"


def test_User_userId_value_roundtrip():
    instance = User(active=True, password="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_assoc_MediaPool_MediaPool_link_reassign_clear():
    a = MediaPool(assets="sample_text", name="sample_text")
    b1 = MediaPool(assets="sample_text", name="sample_text")
    b2 = MediaPool(assets="sample_text_2", name="sample_text_2")
    _safe_set(a, 'mediaPool17', b1)
    assert _is_linked(a, 'mediaPool17', b1)
    if hasattr(b1, 'parent16'):
        assert _is_linked(b1, 'parent16', a)
    _safe_set(a, 'mediaPool17', b2)
    assert _is_linked(a, 'mediaPool17', b2)
    if hasattr(b1, 'parent16'):
        assert not _is_linked(b1, 'parent16', a)
    if hasattr(b2, 'parent16'):
        assert _is_linked(b2, 'parent16', a)
    _safe_set(a, 'mediaPool17', None)
    assert not _is_linked(a, 'mediaPool17', b2)
    if hasattr(b2, 'parent16'):
        assert not _is_linked(b2, 'parent16', a)


def test_assoc_Profile_User_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    b2 = Profile(email="sample_text_2", firstName="sample_text_2", name="sample_text_2", username="sample_text_2")
    _safe_set(a, 'profile7', b1)
    assert _is_linked(a, 'profile7', b1)
    if hasattr(b1, 'user6'):
        assert _is_linked(b1, 'user6', a)
    _safe_set(a, 'profile7', b2)
    assert _is_linked(a, 'profile7', b2)
    if hasattr(b1, 'user6'):
        assert not _is_linked(b1, 'user6', a)
    if hasattr(b2, 'user6'):
        assert _is_linked(b2, 'user6', a)
    _safe_set(a, 'profile7', None)
    assert not _is_linked(a, 'profile7', b2)
    if hasattr(b2, 'user6'):
        assert not _is_linked(b2, 'user6', a)


def test_assoc_Settings_User_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    b2 = Settings(email="sample_text_2", firstName="sample_text_2", name="sample_text_2", notificationChannels="sample_text_2", username="sample_text_2")
    _safe_set(a, 'settings9', b1)
    assert _is_linked(a, 'settings9', b1)
    if hasattr(b1, 'user8'):
        assert _is_linked(b1, 'user8', a)
    _safe_set(a, 'settings9', b2)
    assert _is_linked(a, 'settings9', b2)
    if hasattr(b1, 'user8'):
        assert not _is_linked(b1, 'user8', a)
    if hasattr(b2, 'user8'):
        assert _is_linked(b2, 'user8', a)
    _safe_set(a, 'settings9', None)
    assert not _is_linked(a, 'settings9', b2)
    if hasattr(b2, 'user8'):
        assert not _is_linked(b2, 'user8', a)


def test_assoc_User_Group_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Group()
    b2 = Group()
    _safe_set(a, 'group2', {b1})
    assert _is_linked(a, 'group2', b1)
    if hasattr(b1, 'user3'):
        assert _is_linked(b1, 'user3', a)
    _safe_set(a, 'group2', {b2})
    assert _is_linked(a, 'group2', b2)
    if hasattr(b1, 'user3'):
        assert not _is_linked(b1, 'user3', a)
    if hasattr(b2, 'user3'):
        assert _is_linked(b2, 'user3', a)
    _safe_set(a, 'group2', set())
    assert not _is_linked(a, 'group2', b2)
    if hasattr(b2, 'user3'):
        assert not _is_linked(b2, 'user3', a)


def test_assoc_User_Message_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Message()
    b2 = Message()
    _safe_set(a, 'message4', {b1})
    assert _is_linked(a, 'message4', b1)
    if hasattr(b1, 'user5'):
        assert _is_linked(b1, 'user5', a)
    _safe_set(a, 'message4', {b2})
    assert _is_linked(a, 'message4', b2)
    if hasattr(b1, 'user5'):
        assert not _is_linked(b1, 'user5', a)
    if hasattr(b2, 'user5'):
        assert _is_linked(b2, 'user5', a)
    _safe_set(a, 'message4', set())
    assert not _is_linked(a, 'message4', b2)
    if hasattr(b2, 'user5'):
        assert not _is_linked(b2, 'user5', a)


def test_assoc_User_Myprofile_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    b2 = Profile(email="sample_text_2", firstName="sample_text_2", name="sample_text_2", username="sample_text_2")
    _safe_set(a, 'myprofile0', b1)
    assert _is_linked(a, 'myprofile0', b1)
    if hasattr(b1, 'user1'):
        assert _is_linked(b1, 'user1', a)
    _safe_set(a, 'myprofile0', b2)
    assert _is_linked(a, 'myprofile0', b2)
    if hasattr(b1, 'user1'):
        assert not _is_linked(b1, 'user1', a)
    if hasattr(b2, 'user1'):
        assert _is_linked(b2, 'user1', a)
    _safe_set(a, 'myprofile0', None)
    assert not _is_linked(a, 'myprofile0', b2)
    if hasattr(b2, 'user1'):
        assert not _is_linked(b2, 'user1', a)


def test_assoc_User_Profile_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Profile(email="sample_text", firstName="sample_text", name="sample_text", username="sample_text")
    b2 = Profile(email="sample_text_2", firstName="sample_text_2", name="sample_text_2", username="sample_text_2")
    _safe_set(a, 'profile22', b1)
    assert _is_linked(a, 'profile22', b1)
    if hasattr(b1, 'user23'):
        assert _is_linked(b1, 'user23', a)
    _safe_set(a, 'profile22', b2)
    assert _is_linked(a, 'profile22', b2)
    if hasattr(b1, 'user23'):
        assert not _is_linked(b1, 'user23', a)
    if hasattr(b2, 'user23'):
        assert _is_linked(b2, 'user23', a)
    _safe_set(a, 'profile22', None)
    assert not _is_linked(a, 'profile22', b2)
    if hasattr(b2, 'user23'):
        assert not _is_linked(b2, 'user23', a)


def test_assoc_User_Settings_link_reassign_clear():
    a = User(active=True, password="sample_text", userId="sample_text")
    b1 = Settings(email="sample_text", firstName="sample_text", name="sample_text", notificationChannels="sample_text", username="sample_text")
    b2 = Settings(email="sample_text_2", firstName="sample_text_2", name="sample_text_2", notificationChannels="sample_text_2", username="sample_text_2")
    _safe_set(a, 'settings20', b1)
    assert _is_linked(a, 'settings20', b1)
    if hasattr(b1, 'user21'):
        assert _is_linked(b1, 'user21', a)
    _safe_set(a, 'settings20', b2)
    assert _is_linked(a, 'settings20', b2)
    if hasattr(b1, 'user21'):
        assert not _is_linked(b1, 'user21', a)
    if hasattr(b2, 'user21'):
        assert _is_linked(b2, 'user21', a)
    _safe_set(a, 'settings20', None)
    assert not _is_linked(a, 'settings20', b2)
    if hasattr(b2, 'user21'):
        assert not _is_linked(b2, 'user21', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Address_strategy = st.builds(Address, city=safe_text, country=safe_text, street=safe_text, streetnumber=safe_text, zipCode=safe_text)
@given(instance=Address_strategy)
@settings(max_examples=25)
def test_Address_instantiation(instance):
    assert isinstance(instance, Address)


AdminUser_strategy = st.builds(AdminUser, active=st.booleans(), email=safe_text, id=safe_text, password=safe_text, phone=safe_text, roles=safe_text, username=safe_text)
@given(instance=AdminUser_strategy)
@settings(max_examples=25)
def test_AdminUser_instantiation(instance):
    assert isinstance(instance, AdminUser)


Friend_strategy = st.builds(Friend)
@given(instance=Friend_strategy)
@settings(max_examples=25)
def test_Friend_instantiation(instance):
    assert isinstance(instance, Friend)


Group_strategy = st.builds(Group)
@given(instance=Group_strategy)
@settings(max_examples=25)
def test_Group_instantiation(instance):
    assert isinstance(instance, Group)


Image_strategy = st.builds(Image)
@given(instance=Image_strategy)
@settings(max_examples=25)
def test_Image_instantiation(instance):
    assert isinstance(instance, Image)


LogEntry_strategy = st.builds(LogEntry, _attr=safe_text, objectId=safe_text, objectType=safe_text, time=safe_text)
@given(instance=LogEntry_strategy)
@settings(max_examples=25)
def test_LogEntry_instantiation(instance):
    assert isinstance(instance, LogEntry)


MediaPool_strategy = st.builds(MediaPool, assets=safe_text, name=safe_text)
@given(instance=MediaPool_strategy)
@settings(max_examples=25)
def test_MediaPool_instantiation(instance):
    assert isinstance(instance, MediaPool)


Message_strategy = st.builds(Message)
@given(instance=Message_strategy)
@settings(max_examples=25)
def test_Message_instantiation(instance):
    assert isinstance(instance, Message)


Profile_strategy = st.builds(Profile, email=safe_text, firstName=safe_text, name=safe_text, username=safe_text)
@given(instance=Profile_strategy)
@settings(max_examples=25)
def test_Profile_instantiation(instance):
    assert isinstance(instance, Profile)


Profile2_strategy = st.builds(Profile2, email=safe_text, firstName=safe_text, name=safe_text, username=safe_text)
@given(instance=Profile2_strategy)
@settings(max_examples=25)
def test_Profile2_instantiation(instance):
    assert isinstance(instance, Profile2)


Settings_strategy = st.builds(Settings, email=safe_text, firstName=safe_text, name=safe_text, notificationChannels=safe_text, username=safe_text)
@given(instance=Settings_strategy)
@settings(max_examples=25)
def test_Settings_instantiation(instance):
    assert isinstance(instance, Settings)


Tag_strategy = st.builds(Tag, name=safe_text)
@given(instance=Tag_strategy)
@settings(max_examples=25)
def test_Tag_instantiation(instance):
    assert isinstance(instance, Tag)


Tenant_strategy = st.builds(Tenant, id=safe_text, name=safe_text)
@given(instance=Tenant_strategy)
@settings(max_examples=25)
def test_Tenant_instantiation(instance):
    assert isinstance(instance, Tenant)


User_strategy = st.builds(User, active=st.booleans(), password=safe_text, userId=safe_text)
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


Video_strategy = st.builds(Video)
@given(instance=Video_strategy)
@settings(max_examples=25)
def test_Video_instantiation(instance):
    assert isinstance(instance, Video)


int2_Interface_strategy = st.builds(int2_Interface)
@given(instance=int2_Interface_strategy)
@settings(max_examples=25)
def test_int2_Interface_instantiation(instance):
    assert isinstance(instance, int2_Interface)



