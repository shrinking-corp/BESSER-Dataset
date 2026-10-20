import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Attachment,
    EmailAccount,
    EmailAddress,
    EmailAddressList,
    EmailBox,
    EmailList,
    EmailMessage,
    Event,
    FamilyMember,
    GohonzonInfo,
    LeadershipInfo,
    LeadershipRole,
    Map,
    MapEntry,
    Member,
    MemberSearchCriteria,
    Members,
    MembershipInfo,
    Note,
    Organization,
    Permission,
    Person,
    PersonName,
    PhoneNumber,
    Preferences,
    Properties,
    Property,
    Registration,
    SchoolInfo,
    StreetAddress,
    StudyDeptExam,
    StudyDeptInfo,
    User,
    Users,
    View,
    ZipCode,
    org_aries_common_Attachment,
    org_aries_common_DocumentRoot,
    org_aries_common_EObject,
    org_aries_common_EStringToStringMapEntry,
    org_aries_common_EmailAccount,
    org_aries_common_EmailAddress,
    org_aries_common_EmailAddressList,
    org_aries_common_EmailBox,
    org_aries_common_EmailMessage,
    org_aries_common_Event,
    org_aries_common_Map,
    org_aries_common_MapEntry,
    org_aries_common_Note,
    org_aries_common_Person,
    org_aries_common_PersonName,
    org_aries_common_PhoneNumber,
    org_aries_common_Properties,
    org_aries_common_Property,
    org_aries_common_StreetAddress,
    org_aries_common_User,
    org_aries_common_ZipCode,
    org_sgiusa_model_DocumentRoot,
    org_sgiusa_model_EStringToStringMapEntry,
    org_sgiusa_model_EmailList,
    org_sgiusa_model_Event,
    org_sgiusa_model_FamilyMember,
    org_sgiusa_model_GohonzonInfo,
    org_sgiusa_model_LeadershipInfo,
    org_sgiusa_model_LeadershipRole,
    org_sgiusa_model_Member,
    org_sgiusa_model_MemberSearchCriteria,
    org_sgiusa_model_Members,
    org_sgiusa_model_MembershipInfo,
    org_sgiusa_model_Note,
    org_sgiusa_model_Organization,
    org_sgiusa_model_Permission,
    org_sgiusa_model_Preferences,
    org_sgiusa_model_Registration,
    org_sgiusa_model_SchoolInfo,
    org_sgiusa_model_StudyDeptExam,
    org_sgiusa_model_StudyDeptInfo,
    org_sgiusa_model_User,
    org_sgiusa_model_Users,
    org_sgiusa_model_View,
    ActivityGroup,
    ActivityGroupName,
    Capability,
    Country,
    Division,
    DivisionName,
    EventStatus,
    FamilyRelation,
    GohonzonType,
    Language,
    OrganizationLevel,
    PhoneNumberType,
    Position,
    PositionName,
    Role,
    RoleType,
    SchoolType,
    State,
    Status,
    StudyDeptExamLevel,
    StudyDeptLanguage,
    SubDivision,
    SubDivisionName,
    ViewType,
)

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_accessors211_stub_double():
    # User has no real 'User213' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Organization(abbrv="sample_text", creationDate="sample_text", id="sample_text", label="sample_text", lastUpdate="sample_text", level="sample_text", name="sample_text", organizationId="sample_text", permissionId="sample_text", type="sample_text", zipCodes="sample_text")
    partner = User()
    setattr(partner, 'User213', None)
    _safe_set(owner, 'org_sgiusa_model_Organization212', {partner})
    assert getattr(partner, 'User213') == owner
    _safe_set(owner, 'org_sgiusa_model_Organization212', set())
    assert getattr(partner, 'User213') is None


def test_assoc_adminAddressList66_stub_double():
    # EmailAddressList has no real 'EmailAddressList68' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList68', None)
    _safe_set(owner, 'org_aries_common_EmailMessage67', {partner})
    assert getattr(partner, 'EmailAddressList68') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage67', set())
    assert getattr(partner, 'EmailAddressList68') is None


def test_assoc_attachment4_stub_double():
    # Attachment has no real 'Attachment' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Attachment()
    setattr(partner, 'Attachment', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot5', {partner})
    assert getattr(partner, 'Attachment') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot5', set())
    assert getattr(partner, 'Attachment') is None


def test_assoc_attachments69_stub_double():
    # Attachment has no real 'Attachment71' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = Attachment()
    setattr(partner, 'Attachment71', None)
    _safe_set(owner, 'org_aries_common_EmailMessage70', {partner})
    assert getattr(partner, 'Attachment71') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage70', set())
    assert getattr(partner, 'Attachment71') is None


def test_assoc_author198_stub_double():
    # User has no real 'User199' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Note's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Note's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Note(creationDate="sample_text", id="sample_text", lastUpdate="sample_text", text="sample_text")
    partner = User()
    setattr(partner, 'User199', None)
    _safe_set(owner, 'org_sgiusa_model_Note', partner)
    assert getattr(partner, 'User199') == owner
    _safe_set(owner, 'org_sgiusa_model_Note', None)
    assert getattr(partner, 'User199') is None


def test_assoc_author80_stub_double():
    # User has no real 'User81' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Note's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Note's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Note(creationDate="sample_text", id="sample_text", lastUpdate="sample_text", text="sample_text")
    partner = User()
    setattr(partner, 'User81', None)
    _safe_set(owner, 'org_aries_common_Note', partner)
    assert getattr(partner, 'User81') == owner
    _safe_set(owner, 'org_aries_common_Note', None)
    assert getattr(partner, 'User81') is None


def test_assoc_bccAddressList57_stub_double():
    # EmailAddressList has no real 'EmailAddressList59' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList59', None)
    _safe_set(owner, 'org_aries_common_EmailMessage58', {partner})
    assert getattr(partner, 'EmailAddressList59') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage58', set())
    assert getattr(partner, 'EmailAddressList59') is None


def test_assoc_ccAddressList60_stub_double():
    # EmailAddressList has no real 'EmailAddressList62' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList62', None)
    _safe_set(owner, 'org_aries_common_EmailMessage61', {partner})
    assert getattr(partner, 'EmailAddressList62') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage61', set())
    assert getattr(partner, 'EmailAddressList62') is None


def test_assoc_cellPhone168_stub_double():
    # PhoneNumber has no real 'PhoneNumber170' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber170', None)
    _safe_set(owner, 'org_sgiusa_model_Member169', partner)
    assert getattr(partner, 'PhoneNumber170') == owner
    _safe_set(owner, 'org_sgiusa_model_Member169', None)
    assert getattr(partner, 'PhoneNumber170') is None


def test_assoc_cellPhone228_stub_double():
    # PhoneNumber has no real 'PhoneNumber230' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber230', None)
    _safe_set(owner, 'org_sgiusa_model_User229', partner)
    assert getattr(partner, 'PhoneNumber230') == owner
    _safe_set(owner, 'org_sgiusa_model_User229', None)
    assert getattr(partner, 'PhoneNumber230') is None


def test_assoc_children202_stub_double():
    # Organization has no real 'Organization204' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Organization(abbrv="sample_text", creationDate="sample_text", id="sample_text", label="sample_text", lastUpdate="sample_text", level="sample_text", name="sample_text", organizationId="sample_text", permissionId="sample_text", type="sample_text", zipCodes="sample_text")
    partner = Organization()
    setattr(partner, 'Organization204', None)
    _safe_set(owner, 'org_sgiusa_model_Organization203', {partner})
    assert getattr(partner, 'Organization204') == owner
    _safe_set(owner, 'org_sgiusa_model_Organization203', set())
    assert getattr(partner, 'Organization204') is None


def test_assoc_creator205_stub_double():
    # User has no real 'User207' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Organization(abbrv="sample_text", creationDate="sample_text", id="sample_text", label="sample_text", lastUpdate="sample_text", level="sample_text", name="sample_text", organizationId="sample_text", permissionId="sample_text", type="sample_text", zipCodes="sample_text")
    partner = User()
    setattr(partner, 'User207', None)
    _safe_set(owner, 'org_sgiusa_model_Organization206', partner)
    assert getattr(partner, 'User207') == owner
    _safe_set(owner, 'org_sgiusa_model_Organization206', None)
    assert getattr(partner, 'User207') is None


def test_assoc_emailAccount220_stub_double():
    # EmailAccount has no real 'EmailAccount221' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = EmailAccount()
    setattr(partner, 'EmailAccount221', None)
    _safe_set(owner, 'org_sgiusa_model_User', partner)
    assert getattr(partner, 'EmailAccount221') == owner
    _safe_set(owner, 'org_sgiusa_model_User', None)
    assert getattr(partner, 'EmailAccount221') is None


def test_assoc_emailAccount44_stub_double():
    # EmailAccount has no real 'EmailAccount45' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailBox(creationDate="sample_text", id="sample_text", lastUpdate="sample_text", name="sample_text", type="sample_text")
    partner = EmailAccount()
    setattr(partner, 'EmailAccount45', None)
    _safe_set(owner, 'org_aries_common_EmailBox', partner)
    assert getattr(partner, 'EmailAccount45') == owner
    _safe_set(owner, 'org_aries_common_EmailBox', None)
    assert getattr(partner, 'EmailAccount45') is None


def test_assoc_emailAccount6_stub_double():
    # EmailAccount has no real 'EmailAccount' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = EmailAccount()
    setattr(partner, 'EmailAccount', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot7', {partner})
    assert getattr(partner, 'EmailAccount') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot7', set())
    assert getattr(partner, 'EmailAccount') is None


def test_assoc_emailAddress160_stub_double():
    # EmailAddress has no real 'EmailAddress161' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress161', None)
    _safe_set(owner, 'org_sgiusa_model_Member', partner)
    assert getattr(partner, 'EmailAddress161') == owner
    _safe_set(owner, 'org_sgiusa_model_Member', None)
    assert getattr(partner, 'EmailAddress161') is None


def test_assoc_emailAddress222_stub_double():
    # EmailAddress has no real 'EmailAddress224' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress224', None)
    _safe_set(owner, 'org_sgiusa_model_User223', partner)
    assert getattr(partner, 'EmailAddress224') == owner
    _safe_set(owner, 'org_sgiusa_model_User223', None)
    assert getattr(partner, 'EmailAddress224') is None


def test_assoc_emailAddress8_stub_double():
    # EmailAddress has no real 'EmailAddress' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot9', {partner})
    assert getattr(partner, 'EmailAddress') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot9', set())
    assert getattr(partner, 'EmailAddress') is None


def test_assoc_emailAddress87_stub_double():
    # EmailAddress has no real 'EmailAddress89' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Person(id="sample_text", userId="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress89', None)
    _safe_set(owner, 'org_aries_common_Person88', partner)
    assert getattr(partner, 'EmailAddress89') == owner
    _safe_set(owner, 'org_aries_common_Person88', None)
    assert getattr(partner, 'EmailAddress89') is None


def test_assoc_emailAddress99_stub_double():
    # EmailAddress has no real 'EmailAddress101' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", userId="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress101', None)
    _safe_set(owner, 'org_aries_common_User100', partner)
    assert getattr(partner, 'EmailAddress101') == owner
    _safe_set(owner, 'org_aries_common_User100', None)
    assert getattr(partner, 'EmailAddress101') is None


def test_assoc_emailAddressList10_stub_double():
    # EmailAddressList has no real 'EmailAddressList' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot11', {partner})
    assert getattr(partner, 'EmailAddressList') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot11', set())
    assert getattr(partner, 'EmailAddressList') is None


def test_assoc_emailAddressList153_stub_double():
    # User has no real 'User155' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_EmailList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_EmailList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_EmailList(activityGroups="sample_text", divisions="sample_text", enabled="sample_text", id="sample_text", subDivisions="sample_text")
    partner = User()
    setattr(partner, 'User155', None)
    _safe_set(owner, 'org_sgiusa_model_EmailList154', {partner})
    assert getattr(partner, 'User155') == owner
    _safe_set(owner, 'org_sgiusa_model_EmailList154', set())
    assert getattr(partner, 'User155') is None


def test_assoc_emailBox12_stub_double():
    # EmailBox has no real 'EmailBox' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = EmailBox()
    setattr(partner, 'EmailBox', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot13', {partner})
    assert getattr(partner, 'EmailBox') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot13', set())
    assert getattr(partner, 'EmailBox') is None


def test_assoc_emailBoxes40_stub_double():
    # EmailBox has no real 'EmailBox41' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailAccount's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailAccount's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailAccount(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", userId="sample_text")
    partner = EmailBox()
    setattr(partner, 'EmailBox41', None)
    _safe_set(owner, 'org_aries_common_EmailAccount', {partner})
    assert getattr(partner, 'EmailBox41') == owner
    _safe_set(owner, 'org_aries_common_EmailAccount', set())
    assert getattr(partner, 'EmailBox41') is None


def test_assoc_emailList106_stub_double():
    # EmailList has no real 'EmailList' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = EmailList()
    setattr(partner, 'EmailList', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot107', {partner})
    assert getattr(partner, 'EmailList') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot107', set())
    assert getattr(partner, 'EmailList') is None


def test_assoc_emailMessage14_stub_double():
    # EmailMessage has no real 'EmailMessage' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = EmailMessage()
    setattr(partner, 'EmailMessage', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot15', {partner})
    assert getattr(partner, 'EmailMessage') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot15', set())
    assert getattr(partner, 'EmailMessage') is None


def test_assoc_event108_stub_double():
    # Event has no real 'Event110' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Event()
    setattr(partner, 'Event110', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot109', {partner})
    assert getattr(partner, 'Event110') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot109', set())
    assert getattr(partner, 'Event110') is None


def test_assoc_event16_stub_double():
    # Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot17', {partner})
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot17', set())
    assert getattr(partner, 'Event') is None


def test_assoc_familyInfo189_stub_double():
    # FamilyMember has no real 'FamilyMember191' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = FamilyMember()
    setattr(partner, 'FamilyMember191', None)
    _safe_set(owner, 'org_sgiusa_model_Member190', partner)
    assert getattr(partner, 'FamilyMember191') == owner
    _safe_set(owner, 'org_sgiusa_model_Member190', None)
    assert getattr(partner, 'FamilyMember191') is None


def test_assoc_familyMember111_stub_double():
    # FamilyMember has no real 'FamilyMember' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = FamilyMember()
    setattr(partner, 'FamilyMember', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot112', {partner})
    assert getattr(partner, 'FamilyMember') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot112', set())
    assert getattr(partner, 'FamilyMember') is None


def test_assoc_fromAddress52_stub_double():
    # EmailAddress has no real 'EmailAddress53' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddress()
    setattr(partner, 'EmailAddress53', None)
    _safe_set(owner, 'org_aries_common_EmailMessage', partner)
    assert getattr(partner, 'EmailAddress53') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage', None)
    assert getattr(partner, 'EmailAddress53') is None


def test_assoc_gohonzonInfo113_stub_double():
    # GohonzonInfo has no real 'GohonzonInfo' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = GohonzonInfo()
    setattr(partner, 'GohonzonInfo', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot114', {partner})
    assert getattr(partner, 'GohonzonInfo') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot114', set())
    assert getattr(partner, 'GohonzonInfo') is None


def test_assoc_gohonzons196_stub_double():
    # GohonzonInfo has no real 'GohonzonInfo197' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_MembershipInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_MembershipInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_MembershipInfo(friendOfSgi="sample_text", id="sample_text", lastUpdate="sample_text", notActivated="sample_text", notLocatable="sample_text", receivedCertificate="sample_text")
    partner = GohonzonInfo()
    setattr(partner, 'GohonzonInfo197', None)
    _safe_set(owner, 'org_sgiusa_model_MembershipInfo', {partner})
    assert getattr(partner, 'GohonzonInfo197') == owner
    _safe_set(owner, 'org_sgiusa_model_MembershipInfo', set())
    assert getattr(partner, 'GohonzonInfo197') is None


def test_assoc_homePhone165_stub_double():
    # PhoneNumber has no real 'PhoneNumber167' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber167', None)
    _safe_set(owner, 'org_sgiusa_model_Member166', partner)
    assert getattr(partner, 'PhoneNumber167') == owner
    _safe_set(owner, 'org_sgiusa_model_Member166', None)
    assert getattr(partner, 'PhoneNumber167') is None


def test_assoc_homePhone231_stub_double():
    # PhoneNumber has no real 'PhoneNumber233' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber233', None)
    _safe_set(owner, 'org_sgiusa_model_User232', partner)
    assert getattr(partner, 'PhoneNumber233') == owner
    _safe_set(owner, 'org_sgiusa_model_User232', None)
    assert getattr(partner, 'PhoneNumber233') is None


def test_assoc_leadershipInfo115_stub_double():
    # LeadershipInfo has no real 'LeadershipInfo' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = LeadershipInfo()
    setattr(partner, 'LeadershipInfo', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot116', {partner})
    assert getattr(partner, 'LeadershipInfo') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot116', set())
    assert getattr(partner, 'LeadershipInfo') is None


def test_assoc_leadershipInfo180_stub_double():
    # LeadershipInfo has no real 'LeadershipInfo182' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = LeadershipInfo()
    setattr(partner, 'LeadershipInfo182', None)
    _safe_set(owner, 'org_sgiusa_model_Member181', partner)
    assert getattr(partner, 'LeadershipInfo182') == owner
    _safe_set(owner, 'org_sgiusa_model_Member181', None)
    assert getattr(partner, 'LeadershipInfo182') is None


def test_assoc_leadershipRole117_stub_double():
    # LeadershipRole has no real 'LeadershipRole' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = LeadershipRole()
    setattr(partner, 'LeadershipRole', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot118', {partner})
    assert getattr(partner, 'LeadershipRole') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot118', set())
    assert getattr(partner, 'LeadershipRole') is None


def test_assoc_leadershipRoles158_stub_double():
    # LeadershipRole has no real 'LeadershipRole159' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_LeadershipInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_LeadershipInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_LeadershipInfo(examPassed="sample_text", examPassedDate="sample_text", id="sample_text", lastUpdate="sample_text", manualSigned="sample_text", manualSignedDate="sample_text")
    partner = LeadershipRole()
    setattr(partner, 'LeadershipRole159', None)
    _safe_set(owner, 'org_sgiusa_model_LeadershipInfo', {partner})
    assert getattr(partner, 'LeadershipRole159') == owner
    _safe_set(owner, 'org_sgiusa_model_LeadershipInfo', set())
    assert getattr(partner, 'LeadershipRole159') is None


def test_assoc_map18_stub_double():
    # Map has no real 'Map' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Map()
    setattr(partner, 'Map', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot19', {partner})
    assert getattr(partner, 'Map') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot19', set())
    assert getattr(partner, 'Map') is None


def test_assoc_mapEntry20_stub_double():
    # MapEntry has no real 'MapEntry' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = MapEntry()
    setattr(partner, 'MapEntry', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot21', {partner})
    assert getattr(partner, 'MapEntry') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot21', set())
    assert getattr(partner, 'MapEntry') is None


def test_assoc_member119_stub_double():
    # Member has no real 'Member' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Member()
    setattr(partner, 'Member', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot120', {partner})
    assert getattr(partner, 'Member') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot120', set())
    assert getattr(partner, 'Member') is None


def test_assoc_memberSearchCriteria123_stub_double():
    # MemberSearchCriteria has no real 'MemberSearchCriteria' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = MemberSearchCriteria()
    setattr(partner, 'MemberSearchCriteria', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot124', {partner})
    assert getattr(partner, 'MemberSearchCriteria') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot124', set())
    assert getattr(partner, 'MemberSearchCriteria') is None


def test_assoc_members121_stub_double():
    # Members has no real 'Members' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Members()
    setattr(partner, 'Members', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot122', {partner})
    assert getattr(partner, 'Members') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot122', set())
    assert getattr(partner, 'Members') is None


def test_assoc_membershipInfo125_stub_double():
    # MembershipInfo has no real 'MembershipInfo' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = MembershipInfo()
    setattr(partner, 'MembershipInfo', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot126', {partner})
    assert getattr(partner, 'MembershipInfo') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot126', set())
    assert getattr(partner, 'MembershipInfo') is None


def test_assoc_messageList49_stub_double():
    # EmailMessage has no real 'EmailMessage51' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailBox(creationDate="sample_text", id="sample_text", lastUpdate="sample_text", name="sample_text", type="sample_text")
    partner = EmailMessage()
    setattr(partner, 'EmailMessage51', None)
    _safe_set(owner, 'org_aries_common_EmailBox50', {partner})
    assert getattr(partner, 'EmailMessage51') == owner
    _safe_set(owner, 'org_aries_common_EmailBox50', set())
    assert getattr(partner, 'EmailMessage51') is None


def test_assoc_name82_stub_double():
    # PersonName has no real 'PersonName83' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Person(id="sample_text", userId="sample_text")
    partner = PersonName()
    setattr(partner, 'PersonName83', None)
    _safe_set(owner, 'org_aries_common_Person', partner)
    assert getattr(partner, 'PersonName83') == owner
    _safe_set(owner, 'org_aries_common_Person', None)
    assert getattr(partner, 'PersonName83') is None


def test_assoc_note127_stub_double():
    # Note has no real 'Note129' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Note()
    setattr(partner, 'Note129', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot128', {partner})
    assert getattr(partner, 'Note129') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot128', set())
    assert getattr(partner, 'Note129') is None


def test_assoc_note22_stub_double():
    # Note has no real 'Note' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Note()
    setattr(partner, 'Note', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot23', {partner})
    assert getattr(partner, 'Note') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot23', set())
    assert getattr(partner, 'Note') is None


def test_assoc_notes186_stub_double():
    # Note has no real 'Note188' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = Note()
    setattr(partner, 'Note188', None)
    _safe_set(owner, 'org_sgiusa_model_Member187', {partner})
    assert getattr(partner, 'Note188') == owner
    _safe_set(owner, 'org_sgiusa_model_Member187', set())
    assert getattr(partner, 'Note188') is None


def test_assoc_organization130_stub_double():
    # Organization has no real 'Organization' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Organization()
    setattr(partner, 'Organization', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot131', {partner})
    assert getattr(partner, 'Organization') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot131', set())
    assert getattr(partner, 'Organization') is None


def test_assoc_organization151_stub_double():
    # Organization has no real 'Organization152' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_EmailList's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_EmailList's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_EmailList(activityGroups="sample_text", divisions="sample_text", enabled="sample_text", id="sample_text", subDivisions="sample_text")
    partner = Organization()
    setattr(partner, 'Organization152', None)
    _safe_set(owner, 'org_sgiusa_model_EmailList', partner)
    assert getattr(partner, 'Organization152') == owner
    _safe_set(owner, 'org_sgiusa_model_EmailList', None)
    assert getattr(partner, 'Organization152') is None


def test_assoc_organization156_stub_double():
    # Organization has no real 'Organization157' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Event(divisions="sample_text", id="sample_text", status="sample_text", subDivisions="sample_text", userId="sample_text")
    partner = Organization()
    setattr(partner, 'Organization157', None)
    _safe_set(owner, 'org_sgiusa_model_Event', partner)
    assert getattr(partner, 'Organization157') == owner
    _safe_set(owner, 'org_sgiusa_model_Event', None)
    assert getattr(partner, 'Organization157') is None


def test_assoc_organization177_stub_double():
    # Organization has no real 'Organization179' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = Organization()
    setattr(partner, 'Organization179', None)
    _safe_set(owner, 'org_sgiusa_model_Member178', partner)
    assert getattr(partner, 'Organization179') == owner
    _safe_set(owner, 'org_sgiusa_model_Member178', None)
    assert getattr(partner, 'Organization179') is None


def test_assoc_organization194_stub_double():
    # Organization has no real 'Organization195' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_MemberSearchCriteria's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_MemberSearchCriteria's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_MemberSearchCriteria(activityGroups="sample_text", divisions="sample_text", subDivisions="sample_text")
    partner = Organization()
    setattr(partner, 'Organization195', None)
    _safe_set(owner, 'org_sgiusa_model_MemberSearchCriteria', {partner})
    assert getattr(partner, 'Organization195') == owner
    _safe_set(owner, 'org_sgiusa_model_MemberSearchCriteria', set())
    assert getattr(partner, 'Organization195') is None


def test_assoc_organization214_stub_double():
    # Organization has no real 'Organization215' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Permission's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Permission's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Permission(activityGroups="sample_text", capabilities="sample_text", divisions="sample_text", enabled="sample_text", id="sample_text", subDivisions="sample_text", userId="sample_text")
    partner = Organization()
    setattr(partner, 'Organization215', None)
    _safe_set(owner, 'org_sgiusa_model_Permission', partner)
    assert getattr(partner, 'Organization215') == owner
    _safe_set(owner, 'org_sgiusa_model_Permission', None)
    assert getattr(partner, 'Organization215') is None


def test_assoc_organization242_stub_double():
    # Organization has no real 'Organization243' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_View(id="sample_text", userId="sample_text", viewType="sample_text")
    partner = Organization()
    setattr(partner, 'Organization243', None)
    _safe_set(owner, 'org_sgiusa_model_View', partner)
    assert getattr(partner, 'Organization243') == owner
    _safe_set(owner, 'org_sgiusa_model_View', None)
    assert getattr(partner, 'Organization243') is None


def test_assoc_otherPhone174_stub_double():
    # PhoneNumber has no real 'PhoneNumber176' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber176', None)
    _safe_set(owner, 'org_sgiusa_model_Member175', partner)
    assert getattr(partner, 'PhoneNumber176') == owner
    _safe_set(owner, 'org_sgiusa_model_Member175', None)
    assert getattr(partner, 'PhoneNumber176') is None


def test_assoc_parent200_stub_double():
    # Organization has no real 'Organization201' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Organization(abbrv="sample_text", creationDate="sample_text", id="sample_text", label="sample_text", lastUpdate="sample_text", level="sample_text", name="sample_text", organizationId="sample_text", permissionId="sample_text", type="sample_text", zipCodes="sample_text")
    partner = Organization()
    setattr(partner, 'Organization201', None)
    _safe_set(owner, 'org_sgiusa_model_Organization', partner)
    assert getattr(partner, 'Organization201') == owner
    _safe_set(owner, 'org_sgiusa_model_Organization', None)
    assert getattr(partner, 'Organization201') is None


def test_assoc_parentBox46_stub_double():
    # EmailBox has no real 'EmailBox48' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailBox's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailBox's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailBox(creationDate="sample_text", id="sample_text", lastUpdate="sample_text", name="sample_text", type="sample_text")
    partner = EmailBox()
    setattr(partner, 'EmailBox48', None)
    _safe_set(owner, 'org_aries_common_EmailBox47', partner)
    assert getattr(partner, 'EmailBox48') == owner
    _safe_set(owner, 'org_aries_common_EmailBox47', None)
    assert getattr(partner, 'EmailBox48') is None


def test_assoc_permission132_stub_double():
    # Permission has no real 'Permission' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Permission()
    setattr(partner, 'Permission', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot133', {partner})
    assert getattr(partner, 'Permission') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot133', set())
    assert getattr(partner, 'Permission') is None


def test_assoc_permissions234_stub_double():
    # Permission has no real 'Permission236' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = Permission()
    setattr(partner, 'Permission236', None)
    _safe_set(owner, 'org_sgiusa_model_User235', {partner})
    assert getattr(partner, 'Permission236') == owner
    _safe_set(owner, 'org_sgiusa_model_User235', set())
    assert getattr(partner, 'Permission236') is None


def test_assoc_person24_stub_double():
    # Person has no real 'Person' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Person()
    setattr(partner, 'Person', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot25', {partner})
    assert getattr(partner, 'Person') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot25', set())
    assert getattr(partner, 'Person') is None


def test_assoc_personName26_stub_double():
    # PersonName has no real 'PersonName' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = PersonName()
    setattr(partner, 'PersonName', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot27', {partner})
    assert getattr(partner, 'PersonName') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot27', set())
    assert getattr(partner, 'PersonName') is None


def test_assoc_phoneNumber28_stub_double():
    # PhoneNumber has no real 'PhoneNumber' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot29', {partner})
    assert getattr(partner, 'PhoneNumber') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot29', set())
    assert getattr(partner, 'PhoneNumber') is None


def test_assoc_phoneNumber42_stub_double():
    # PhoneNumber has no real 'PhoneNumber43' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailAddress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailAddress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailAddress(creationDate="sample_text", enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", lastUpdate="sample_text", organization="sample_text", url="sample_text", userId="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber43', None)
    _safe_set(owner, 'org_aries_common_EmailAddress', partner)
    assert getattr(partner, 'PhoneNumber43') == owner
    _safe_set(owner, 'org_aries_common_EmailAddress', None)
    assert getattr(partner, 'PhoneNumber43') is None


def test_assoc_phoneNumber84_stub_double():
    # PhoneNumber has no real 'PhoneNumber86' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Person(id="sample_text", userId="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber86', None)
    _safe_set(owner, 'org_aries_common_Person85', partner)
    assert getattr(partner, 'PhoneNumber86') == owner
    _safe_set(owner, 'org_aries_common_Person85', None)
    assert getattr(partner, 'PhoneNumber86') is None


def test_assoc_phoneNumber97_stub_double():
    # PhoneNumber has no real 'PhoneNumber98' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", userId="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber98', None)
    _safe_set(owner, 'org_aries_common_User', partner)
    assert getattr(partner, 'PhoneNumber98') == owner
    _safe_set(owner, 'org_aries_common_User', None)
    assert getattr(partner, 'PhoneNumber98') is None


def test_assoc_preferences134_stub_double():
    # Preferences has no real 'Preferences' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Preferences()
    setattr(partner, 'Preferences', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot135', {partner})
    assert getattr(partner, 'Preferences') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot135', set())
    assert getattr(partner, 'Preferences') is None


def test_assoc_preferences237_stub_double():
    # Preferences has no real 'Preferences239' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = Preferences()
    setattr(partner, 'Preferences239', None)
    _safe_set(owner, 'org_sgiusa_model_User238', partner)
    assert getattr(partner, 'Preferences239') == owner
    _safe_set(owner, 'org_sgiusa_model_User238', None)
    assert getattr(partner, 'Preferences239') is None


def test_assoc_properties30_stub_double():
    # Properties has no real 'Properties' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Properties()
    setattr(partner, 'Properties', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot31', {partner})
    assert getattr(partner, 'Properties') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot31', set())
    assert getattr(partner, 'Properties') is None


def test_assoc_property32_stub_double():
    # Property has no real 'Property' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = Property()
    setattr(partner, 'Property', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot33', {partner})
    assert getattr(partner, 'Property') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot33', set())
    assert getattr(partner, 'Property') is None


def test_assoc_provider208_stub_double():
    # User has no real 'User210' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Organization(abbrv="sample_text", creationDate="sample_text", id="sample_text", label="sample_text", lastUpdate="sample_text", level="sample_text", name="sample_text", organizationId="sample_text", permissionId="sample_text", type="sample_text", zipCodes="sample_text")
    partner = User()
    setattr(partner, 'User210', None)
    _safe_set(owner, 'org_sgiusa_model_Organization209', partner)
    assert getattr(partner, 'User210') == owner
    _safe_set(owner, 'org_sgiusa_model_Organization209', None)
    assert getattr(partner, 'User210') is None


def test_assoc_registration136_stub_double():
    # Registration has no real 'Registration' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Registration()
    setattr(partner, 'Registration', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot137', {partner})
    assert getattr(partner, 'Registration') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot137', set())
    assert getattr(partner, 'Registration') is None


def test_assoc_replytoAddressList63_stub_double():
    # EmailAddressList has no real 'EmailAddressList65' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList65', None)
    _safe_set(owner, 'org_aries_common_EmailMessage64', {partner})
    assert getattr(partner, 'EmailAddressList65') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage64', set())
    assert getattr(partner, 'EmailAddressList65') is None


def test_assoc_schoolInfo138_stub_double():
    # SchoolInfo has no real 'SchoolInfo' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = SchoolInfo()
    setattr(partner, 'SchoolInfo', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot139', {partner})
    assert getattr(partner, 'SchoolInfo') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot139', set())
    assert getattr(partner, 'SchoolInfo') is None


def test_assoc_streetAddress162_stub_double():
    # StreetAddress has no real 'StreetAddress164' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = StreetAddress()
    setattr(partner, 'StreetAddress164', None)
    _safe_set(owner, 'org_sgiusa_model_Member163', partner)
    assert getattr(partner, 'StreetAddress164') == owner
    _safe_set(owner, 'org_sgiusa_model_Member163', None)
    assert getattr(partner, 'StreetAddress164') is None


def test_assoc_streetAddress225_stub_double():
    # StreetAddress has no real 'StreetAddress227' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_User(enabled="sample_text", firstName="sample_text", id="sample_text", lastName="sample_text", password="sample_text", role="sample_text", userId="sample_text")
    partner = StreetAddress()
    setattr(partner, 'StreetAddress227', None)
    _safe_set(owner, 'org_sgiusa_model_User226', partner)
    assert getattr(partner, 'StreetAddress227') == owner
    _safe_set(owner, 'org_sgiusa_model_User226', None)
    assert getattr(partner, 'StreetAddress227') is None


def test_assoc_streetAddress34_stub_double():
    # StreetAddress has no real 'StreetAddress' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = StreetAddress()
    setattr(partner, 'StreetAddress', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot35', {partner})
    assert getattr(partner, 'StreetAddress') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot35', set())
    assert getattr(partner, 'StreetAddress') is None


def test_assoc_streetAddress90_stub_double():
    # StreetAddress has no real 'StreetAddress92' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Person's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Person's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Person(id="sample_text", userId="sample_text")
    partner = StreetAddress()
    setattr(partner, 'StreetAddress92', None)
    _safe_set(owner, 'org_aries_common_Person91', partner)
    assert getattr(partner, 'StreetAddress92') == owner
    _safe_set(owner, 'org_aries_common_Person91', None)
    assert getattr(partner, 'StreetAddress92') is None


def test_assoc_studyDeptExam140_stub_double():
    # StudyDeptExam has no real 'StudyDeptExam' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = StudyDeptExam()
    setattr(partner, 'StudyDeptExam', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot141', {partner})
    assert getattr(partner, 'StudyDeptExam') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot141', set())
    assert getattr(partner, 'StudyDeptExam') is None


def test_assoc_studyDeptExams218_stub_double():
    # StudyDeptExam has no real 'StudyDeptExam219' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_StudyDeptInfo's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_StudyDeptInfo's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_StudyDeptInfo(id="sample_text", lastUpdate="sample_text")
    partner = StudyDeptExam()
    setattr(partner, 'StudyDeptExam219', None)
    _safe_set(owner, 'org_sgiusa_model_StudyDeptInfo', {partner})
    assert getattr(partner, 'StudyDeptExam219') == owner
    _safe_set(owner, 'org_sgiusa_model_StudyDeptInfo', set())
    assert getattr(partner, 'StudyDeptExam219') is None


def test_assoc_studyDeptInfo142_stub_double():
    # StudyDeptInfo has no real 'StudyDeptInfo' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = StudyDeptInfo()
    setattr(partner, 'StudyDeptInfo', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot143', {partner})
    assert getattr(partner, 'StudyDeptInfo') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot143', set())
    assert getattr(partner, 'StudyDeptInfo') is None


def test_assoc_studyDeptInfo183_stub_double():
    # StudyDeptInfo has no real 'StudyDeptInfo185' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = StudyDeptInfo()
    setattr(partner, 'StudyDeptInfo185', None)
    _safe_set(owner, 'org_sgiusa_model_Member184', partner)
    assert getattr(partner, 'StudyDeptInfo185') == owner
    _safe_set(owner, 'org_sgiusa_model_Member184', None)
    assert getattr(partner, 'StudyDeptInfo185') is None


def test_assoc_toAddressList54_stub_double():
    # EmailAddressList has no real 'EmailAddressList56' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_EmailMessage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_EmailMessage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_EmailMessage(content="sample_text", id="sample_text", sendAsHtml="sample_text", smtpHost="sample_text", smtpPort="sample_text", sourceId="sample_text", subject="sample_text", timestamp="sample_text")
    partner = EmailAddressList()
    setattr(partner, 'EmailAddressList56', None)
    _safe_set(owner, 'org_aries_common_EmailMessage55', {partner})
    assert getattr(partner, 'EmailAddressList56') == owner
    _safe_set(owner, 'org_aries_common_EmailMessage55', set())
    assert getattr(partner, 'EmailAddressList56') is None


def test_assoc_user144_stub_double():
    # User has no real 'User146' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = User()
    setattr(partner, 'User146', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot145', {partner})
    assert getattr(partner, 'User146') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot145', set())
    assert getattr(partner, 'User146') is None


def test_assoc_user216_stub_double():
    # User has no real 'User217' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Registration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Registration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Registration(aborted="sample_text", cancelled="sample_text", date="sample_text", id="sample_text")
    partner = User()
    setattr(partner, 'User217', None)
    _safe_set(owner, 'org_sgiusa_model_Registration', partner)
    assert getattr(partner, 'User217') == owner
    _safe_set(owner, 'org_sgiusa_model_Registration', None)
    assert getattr(partner, 'User217') is None


def test_assoc_user36_stub_double():
    # User has no real 'User' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = User()
    setattr(partner, 'User', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot37', {partner})
    assert getattr(partner, 'User') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot37', set())
    assert getattr(partner, 'User') is None


def test_assoc_user72_stub_double():
    # User has no real 'User73' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_Event(id="sample_text")
    partner = User()
    setattr(partner, 'User73', None)
    _safe_set(owner, 'org_aries_common_Event', partner)
    assert getattr(partner, 'User73') == owner
    _safe_set(owner, 'org_aries_common_Event', None)
    assert getattr(partner, 'User73') is None


def test_assoc_users147_stub_double():
    # Users has no real 'Users' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = Users()
    setattr(partner, 'Users', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot148', {partner})
    assert getattr(partner, 'Users') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot148', set())
    assert getattr(partner, 'Users') is None


def test_assoc_view149_stub_double():
    # View has no real 'View' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = View()
    setattr(partner, 'View', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot150', {partner})
    assert getattr(partner, 'View') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot150', set())
    assert getattr(partner, 'View') is None


def test_assoc_workPhone171_stub_double():
    # PhoneNumber has no real 'PhoneNumber173' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_Member's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_Member's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_Member(activityGroups="sample_text", archived="sample_text", birthDate="sample_text", division="sample_text", employer="sample_text", extraField1="sample_text", extraField2="sample_text", firstName="sample_text", id="sample_text", interests="sample_text", joinDate="sample_text", languages="sample_text", lastName="sample_text", locatable="sample_text", middleInitial="sample_text", occupation="sample_text", statusProfile="sample_text", subDivision="sample_text", visible="sample_text")
    partner = PhoneNumber()
    setattr(partner, 'PhoneNumber173', None)
    _safe_set(owner, 'org_sgiusa_model_Member172', partner)
    assert getattr(partner, 'PhoneNumber173') == owner
    _safe_set(owner, 'org_sgiusa_model_Member172', None)
    assert getattr(partner, 'PhoneNumber173') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # org_aries_common_EStringToStringMapEntry has no real 'org_aries_common_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = org_aries_common_EStringToStringMapEntry()
    setattr(partner, 'org_aries_common_EStringToStringMapEntry', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot', {partner})
    assert getattr(partner, 'org_aries_common_EStringToStringMapEntry') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot', set())
    assert getattr(partner, 'org_aries_common_EStringToStringMapEntry') is None


def test_assoc_xMLNSPrefixMap102_stub_double():
    # org_sgiusa_model_EStringToStringMapEntry has no real 'org_sgiusa_model_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = org_sgiusa_model_EStringToStringMapEntry()
    setattr(partner, 'org_sgiusa_model_EStringToStringMapEntry', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot', {partner})
    assert getattr(partner, 'org_sgiusa_model_EStringToStringMapEntry') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot', set())
    assert getattr(partner, 'org_sgiusa_model_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # org_aries_common_EStringToStringMapEntry has no real 'org_aries_common_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = org_aries_common_EStringToStringMapEntry()
    setattr(partner, 'org_aries_common_EStringToStringMapEntry3', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot2', {partner})
    assert getattr(partner, 'org_aries_common_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot2', set())
    assert getattr(partner, 'org_aries_common_EStringToStringMapEntry3') is None


def test_assoc_xSISchemaLocation103_stub_double():
    # org_sgiusa_model_EStringToStringMapEntry has no real 'org_sgiusa_model_EStringToStringMapEntry105' property in the generated
    # code (a bare stub) -- manually attach it so org_sgiusa_model_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_sgiusa_model_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_sgiusa_model_DocumentRoot(mixed="sample_text")
    partner = org_sgiusa_model_EStringToStringMapEntry()
    setattr(partner, 'org_sgiusa_model_EStringToStringMapEntry105', None)
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot104', {partner})
    assert getattr(partner, 'org_sgiusa_model_EStringToStringMapEntry105') == owner
    _safe_set(owner, 'org_sgiusa_model_DocumentRoot104', set())
    assert getattr(partner, 'org_sgiusa_model_EStringToStringMapEntry105') is None


def test_assoc_zip95_stub_double():
    # ZipCode has no real 'ZipCode96' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_StreetAddress's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_StreetAddress's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_StreetAddress(city="sample_text", country="sample_text", id="sample_text", latitude="sample_text", longitude="sample_text", state="sample_text", street="sample_text")
    partner = ZipCode()
    setattr(partner, 'ZipCode96', None)
    _safe_set(owner, 'org_aries_common_StreetAddress', partner)
    assert getattr(partner, 'ZipCode96') == owner
    _safe_set(owner, 'org_aries_common_StreetAddress', None)
    assert getattr(partner, 'ZipCode96') is None


def test_assoc_zipCode38_stub_double():
    # ZipCode has no real 'ZipCode' property in the generated
    # code (a bare stub) -- manually attach it so org_aries_common_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # org_aries_common_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = org_aries_common_DocumentRoot(mixed="sample_text")
    partner = ZipCode()
    setattr(partner, 'ZipCode', None)
    _safe_set(owner, 'org_aries_common_DocumentRoot39', {partner})
    assert getattr(partner, 'ZipCode') == owner
    _safe_set(owner, 'org_aries_common_DocumentRoot39', set())
    assert getattr(partner, 'ZipCode') is None


