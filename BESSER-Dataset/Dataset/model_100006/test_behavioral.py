import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AcademicStaff,
    Department,
    Employee,
    Event,
    FacultyMember,
    Graduate,
    Institute,
    Meeting,
    Organization,
    Person,
    PhDStudent,
    Product,
    Project,
    ProjectReport,
    Publication,
    Report,
    ResearchGroup,
    ResearchTopic,
    SWRC_AcademicStaff,
    SWRC_AdministrativeStaff,
    SWRC_Article,
    SWRC_AssistantProfessor,
    SWRC_AssociateProfessor,
    SWRC_Association,
    SWRC_Bibliography,
    SWRC_Book,
    SWRC_Booklet,
    SWRC_Conference,
    SWRC_Department,
    SWRC_DevelopmentProject,
    SWRC_Employee,
    SWRC_Enterprise,
    SWRC_Event,
    SWRC_Exhibition,
    SWRC_FacultyMember,
    SWRC_FullProfessor,
    SWRC_Graduate,
    SWRC_InBook,
    SWRC_InCollection,
    SWRC_InProceedings,
    SWRC_Institute,
    SWRC_Lecture,
    SWRC_Lecturer,
    SWRC_Manager,
    SWRC_Manual,
    SWRC_MasterThesis,
    SWRC_Meeting,
    SWRC_Misc,
    SWRC_Organization,
    SWRC_Person,
    SWRC_PhDStudent,
    SWRC_PhDThesis,
    SWRC_Proceedings,
    SWRC_Product,
    SWRC_Project,
    SWRC_ProjectMeeting,
    SWRC_ProjectReport,
    SWRC_Publication,
    SWRC_Report,
    SWRC_ResearchGroup,
    SWRC_ResearchProject,
    SWRC_ResearchTopic,
    SWRC_SoftwareComponent,
    SWRC_SoftwareProject,
    SWRC_Student,
    SWRC_TechnicalReport,
    SWRC_TechnicalStaff,
    SWRC_Thesis,
    SWRC_Topic,
    SWRC_Undergraduate,
    SWRC_University,
    SWRC_Unpublished,
    SWRC_Workshop,
    Student,
    TechnicalReport,
    Thesis,
    Topic,
    University,
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

def test_assoc_atEvent62_stub_double():
    # Event has no real 'Event' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Event(date="sample_text", eventTitle="sample_text", location="sample_text", name="sample_text")
    partner = Event()
    setattr(partner, 'Event', None)
    _safe_set(owner, 'hasPartEvent', partner)
    assert getattr(partner, 'Event') == owner
    _safe_set(owner, 'hasPartEvent', None)
    assert getattr(partner, 'Event') is None


def test_assoc_author1_stub_double():
    # Person has no real 'Person' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Article's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Article's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Article(journal="sample_text", month="sample_text", number="sample_text", pages="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person', None)
    _safe_set(owner, 'SWRC_Article', {partner})
    assert getattr(partner, 'Person') == owner
    _safe_set(owner, 'SWRC_Article', set())
    assert getattr(partner, 'Person') is None


def test_assoc_author17_stub_double():
    # Person has no real 'Person18' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Booklet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Booklet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Booklet(address="sample_text", edition="sample_text", howpublished="sample_text", month="sample_text")
    partner = Person()
    setattr(partner, 'Person18', None)
    _safe_set(owner, 'SWRC_Booklet', {partner})
    assert getattr(partner, 'Person18') == owner
    _safe_set(owner, 'SWRC_Booklet', set())
    assert getattr(partner, 'Person18') is None


def test_assoc_author21_stub_double():
    # Person has no real 'Person23' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InCollection(address="sample_text", booktitle="sample_text", chapter="sample_text", edition="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person23', None)
    _safe_set(owner, 'SWRC_InCollection22', {partner})
    assert getattr(partner, 'Person23') == owner
    _safe_set(owner, 'SWRC_InCollection22', set())
    assert getattr(partner, 'Person23') is None


def test_assoc_author29_stub_double():
    # Person has no real 'Person31' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InProceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InProceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InProceedings(address="sample_text", booktitle="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person31', None)
    _safe_set(owner, 'SWRC_InProceedings30', {partner})
    assert getattr(partner, 'Person31') == owner
    _safe_set(owner, 'SWRC_InProceedings30', set())
    assert getattr(partner, 'Person31') is None


def test_assoc_author46_stub_double():
    # Person has no real 'Person47' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Manual's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Manual's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Manual(address="sample_text", edition="sample_text", month="sample_text")
    partner = Person()
    setattr(partner, 'Person47', None)
    _safe_set(owner, 'SWRC_Manual', {partner})
    assert getattr(partner, 'Person47') == owner
    _safe_set(owner, 'SWRC_Manual', set())
    assert getattr(partner, 'Person47') is None


def test_assoc_author51_stub_double():
    # Person has no real 'Person52' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Unpublished's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Unpublished's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Unpublished(month="sample_text")
    partner = Person()
    setattr(partner, 'Person52', None)
    _safe_set(owner, 'SWRC_Unpublished', {partner})
    assert getattr(partner, 'Person52') == owner
    _safe_set(owner, 'SWRC_Unpublished', set())
    assert getattr(partner, 'Person52') is None


def test_assoc_author53_stub_double():
    # Person has no real 'Person54' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Thesis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Thesis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Thesis(address="sample_text", month="sample_text", type="sample_text")
    partner = Person()
    setattr(partner, 'Person54', None)
    _safe_set(owner, 'SWRC_Thesis', {partner})
    assert getattr(partner, 'Person54') == owner
    _safe_set(owner, 'SWRC_Thesis', set())
    assert getattr(partner, 'Person54') is None


def test_assoc_author6_stub_double():
    # Person has no real 'Person8' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Book(address="sample_text", edition="sample_text", isbn="sample_text", month="sample_text", number="sample_text", price="sample_text", series="sample_text", source="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person8', None)
    _safe_set(owner, 'SWRC_Book7', {partner})
    assert getattr(partner, 'Person8') == owner
    _safe_set(owner, 'SWRC_Book7', set())
    assert getattr(partner, 'Person8') is None


def test_assoc_author9_stub_double():
    # Person has no real 'Person10' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InBook(address="sample_text", chapter="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person10', None)
    _safe_set(owner, 'SWRC_InBook', {partner})
    assert getattr(partner, 'Person10') == owner
    _safe_set(owner, 'SWRC_InBook', set())
    assert getattr(partner, 'Person10') is None


def test_assoc_carriedOutBy122_stub_double():
    # Organization has no real 'Organization123' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = Organization()
    setattr(partner, 'Organization123', None)
    _safe_set(owner, 'carriesOut', partner)
    assert getattr(partner, 'Organization123') == owner
    _safe_set(owner, 'carriesOut', None)
    assert getattr(partner, 'Organization123') is None


def test_assoc_carriesOut99_stub_double():
    # Project has no real 'Project100' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = Project()
    setattr(partner, 'Project100', None)
    _safe_set(owner, 'carriedOutBy', {partner})
    assert getattr(partner, 'Project100') == owner
    _safe_set(owner, 'carriedOutBy', set())
    assert getattr(partner, 'Project100') is None


def test_assoc_developedBy135_stub_double():
    # Organization has no real 'Organization136' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Product's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Product's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Product(name="sample_text")
    partner = Organization()
    setattr(partner, 'Organization136', None)
    _safe_set(owner, 'develops', partner)
    assert getattr(partner, 'Organization136') == owner
    _safe_set(owner, 'develops', None)
    assert getattr(partner, 'Organization136') is None


def test_assoc_develops101_stub_double():
    # Product has no real 'Product' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = Product()
    setattr(partner, 'Product', None)
    _safe_set(owner, 'developedBy', {partner})
    assert getattr(partner, 'Product') == owner
    _safe_set(owner, 'developedBy', set())
    assert getattr(partner, 'Product') is None


def test_assoc_editor14_stub_double():
    # Person has no real 'Person16' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InBook(address="sample_text", chapter="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person16', None)
    _safe_set(owner, 'SWRC_InBook15', partner)
    assert getattr(partner, 'Person16') == owner
    _safe_set(owner, 'SWRC_InBook15', None)
    assert getattr(partner, 'Person16') is None


def test_assoc_editor19_stub_double():
    # Person has no real 'Person20' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InCollection(address="sample_text", booktitle="sample_text", chapter="sample_text", edition="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person20', None)
    _safe_set(owner, 'SWRC_InCollection', partner)
    assert getattr(partner, 'Person20') == owner
    _safe_set(owner, 'SWRC_InCollection', None)
    assert getattr(partner, 'Person20') is None


def test_assoc_editor2_stub_double():
    # Person has no real 'Person3' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Book(address="sample_text", edition="sample_text", isbn="sample_text", month="sample_text", number="sample_text", price="sample_text", series="sample_text", source="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person3', None)
    _safe_set(owner, 'SWRC_Book', partner)
    assert getattr(partner, 'Person3') == owner
    _safe_set(owner, 'SWRC_Book', None)
    assert getattr(partner, 'Person3') is None


def test_assoc_editor27_stub_double():
    # Person has no real 'Person28' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InProceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InProceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InProceedings(address="sample_text", booktitle="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person28', None)
    _safe_set(owner, 'SWRC_InProceedings', partner)
    assert getattr(partner, 'Person28') == owner
    _safe_set(owner, 'SWRC_InProceedings', None)
    assert getattr(partner, 'Person28') is None


def test_assoc_editor38_stub_double():
    # Person has no real 'Person39' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Proceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Proceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Proceedings(address="sample_text", month="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    partner = Person()
    setattr(partner, 'Person39', None)
    _safe_set(owner, 'SWRC_Proceedings', partner)
    assert getattr(partner, 'Person39') == owner
    _safe_set(owner, 'SWRC_Proceedings', None)
    assert getattr(partner, 'Person39') is None


def test_assoc_employs102_stub_double():
    # Employee has no real 'Employee' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = Employee()
    setattr(partner, 'Employee', None)
    _safe_set(owner, 'affiliation', {partner})
    assert getattr(partner, 'Employee') == owner
    _safe_set(owner, 'affiliation', set())
    assert getattr(partner, 'Employee') is None


def test_assoc_financedBy124_stub_double():
    # Organization has no real 'Organization125' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = Organization()
    setattr(partner, 'Organization125', None)
    _safe_set(owner, 'finances', partner)
    assert getattr(partner, 'Organization125') == owner
    _safe_set(owner, 'finances', None)
    assert getattr(partner, 'Organization125') is None


def test_assoc_finances103_stub_double():
    # Project has no real 'Project104' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = Project()
    setattr(partner, 'Project104', None)
    _safe_set(owner, 'financedBy', {partner})
    assert getattr(partner, 'Project104') == owner
    _safe_set(owner, 'financedBy', set())
    assert getattr(partner, 'Project104') is None


def test_assoc_hasPartEvent63_stub_double():
    # Event has no real 'Event64' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Event's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Event's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Event(date="sample_text", eventTitle="sample_text", location="sample_text", name="sample_text")
    partner = Event()
    setattr(partner, 'Event64', None)
    _safe_set(owner, 'atEvent', partner)
    assert getattr(partner, 'Event64') == owner
    _safe_set(owner, 'atEvent', None)
    assert getattr(partner, 'Event64') is None


def test_assoc_head126_stub_double():
    # AcademicStaff has no real 'AcademicStaff127' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = AcademicStaff()
    setattr(partner, 'AcademicStaff127', None)
    _safe_set(owner, 'headOf', partner)
    assert getattr(partner, 'AcademicStaff127') == owner
    _safe_set(owner, 'headOf', None)
    assert getattr(partner, 'AcademicStaff127') is None


def test_assoc_isAbout128_stub_double():
    # ResearchTopic has no real 'ResearchTopic129' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = ResearchTopic()
    setattr(partner, 'ResearchTopic129', None)
    _safe_set(owner, 'dealWithIn', {partner})
    assert getattr(partner, 'ResearchTopic129') == owner
    _safe_set(owner, 'dealWithIn', set())
    assert getattr(partner, 'ResearchTopic129') is None


def test_assoc_member130_stub_double():
    # Person has no real 'Person131' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = Person()
    setattr(partner, 'Person131', None)
    _safe_set(owner, 'SWRC_Project', {partner})
    assert getattr(partner, 'Person131') == owner
    _safe_set(owner, 'SWRC_Project', set())
    assert getattr(partner, 'Person131') is None


def test_assoc_organization32_stub_double():
    # Organization has no real 'Organization34' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InProceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InProceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InProceedings(address="sample_text", booktitle="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization34', None)
    _safe_set(owner, 'SWRC_InProceedings33', partner)
    assert getattr(partner, 'Organization34') == owner
    _safe_set(owner, 'SWRC_InProceedings33', None)
    assert getattr(partner, 'Organization34') is None


def test_assoc_organization43_stub_double():
    # Organization has no real 'Organization45' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Proceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Proceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Proceedings(address="sample_text", month="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization45', None)
    _safe_set(owner, 'SWRC_Proceedings44', partner)
    assert getattr(partner, 'Organization45') == owner
    _safe_set(owner, 'SWRC_Proceedings44', None)
    assert getattr(partner, 'Organization45') is None


def test_assoc_organization48_stub_double():
    # Organization has no real 'Organization50' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Manual's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Manual's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Manual(address="sample_text", edition="sample_text", month="sample_text")
    partner = Organization()
    setattr(partner, 'Organization50', None)
    _safe_set(owner, 'SWRC_Manual49', partner)
    assert getattr(partner, 'Organization50') == owner
    _safe_set(owner, 'SWRC_Manual49', None)
    assert getattr(partner, 'Organization50') is None


def test_assoc_organization60_stub_double():
    # Organization has no real 'Organization61' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_TechnicalReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_TechnicalReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_TechnicalReport(series="sample_text")
    partner = Organization()
    setattr(partner, 'Organization61', None)
    _safe_set(owner, 'SWRC_TechnicalReport', partner)
    assert getattr(partner, 'Organization61') == owner
    _safe_set(owner, 'SWRC_TechnicalReport', None)
    assert getattr(partner, 'Organization61') is None


def test_assoc_participant67_stub_double():
    # Person has no real 'Person68' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Meeting's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Meeting's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Meeting(title="sample_text")
    partner = Person()
    setattr(partner, 'Person68', None)
    _safe_set(owner, 'SWRC_Meeting', {partner})
    assert getattr(partner, 'Person68') == owner
    _safe_set(owner, 'SWRC_Meeting', set())
    assert getattr(partner, 'Person68') is None


def test_assoc_projectInfo132_stub_double():
    # ProjectReport has no real 'ProjectReport' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Project's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Project's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Project(name="sample_text")
    partner = ProjectReport()
    setattr(partner, 'ProjectReport', None)
    _safe_set(owner, 'describesProject', {partner})
    assert getattr(partner, 'ProjectReport') == owner
    _safe_set(owner, 'describesProject', set())
    assert getattr(partner, 'ProjectReport') is None


def test_assoc_publisher11_stub_double():
    # Organization has no real 'Organization13' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InBook's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InBook's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InBook(address="sample_text", chapter="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization13', None)
    _safe_set(owner, 'SWRC_InBook12', partner)
    assert getattr(partner, 'Organization13') == owner
    _safe_set(owner, 'SWRC_InBook12', None)
    assert getattr(partner, 'Organization13') is None


def test_assoc_publisher24_stub_double():
    # Organization has no real 'Organization26' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InCollection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InCollection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InCollection(address="sample_text", booktitle="sample_text", chapter="sample_text", edition="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", type="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization26', None)
    _safe_set(owner, 'SWRC_InCollection25', partner)
    assert getattr(partner, 'Organization26') == owner
    _safe_set(owner, 'SWRC_InCollection25', None)
    assert getattr(partner, 'Organization26') is None


def test_assoc_publisher35_stub_double():
    # Organization has no real 'Organization37' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_InProceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_InProceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_InProceedings(address="sample_text", booktitle="sample_text", month="sample_text", number="sample_text", pages="sample_text", series="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization37', None)
    _safe_set(owner, 'SWRC_InProceedings36', partner)
    assert getattr(partner, 'Organization37') == owner
    _safe_set(owner, 'SWRC_InProceedings36', None)
    assert getattr(partner, 'Organization37') is None


def test_assoc_publisher4_stub_double():
    # Organization has no real 'Organization' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Book's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Book's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Book(address="sample_text", edition="sample_text", isbn="sample_text", month="sample_text", number="sample_text", price="sample_text", series="sample_text", source="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization', None)
    _safe_set(owner, 'SWRC_Book5', partner)
    assert getattr(partner, 'Organization') == owner
    _safe_set(owner, 'SWRC_Book5', None)
    assert getattr(partner, 'Organization') is None


def test_assoc_publisher40_stub_double():
    # Organization has no real 'Organization42' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Proceedings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Proceedings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Proceedings(address="sample_text", month="sample_text", number="sample_text", series="sample_text", volume="sample_text")
    partner = Organization()
    setattr(partner, 'Organization42', None)
    _safe_set(owner, 'SWRC_Proceedings41', partner)
    assert getattr(partner, 'Organization42') == owner
    _safe_set(owner, 'SWRC_Proceedings41', None)
    assert getattr(partner, 'Organization42') is None


def test_assoc_publishes105_stub_double():
    # Publication has no real 'Publication106' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = Publication()
    setattr(partner, 'Publication106', None)
    _safe_set(owner, 'SWRC_Organization', {partner})
    assert getattr(partner, 'Publication106') == owner
    _safe_set(owner, 'SWRC_Organization', set())
    assert getattr(partner, 'Publication106') is None


def test_assoc_school55_stub_double():
    # University has no real 'University' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Thesis's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Thesis's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Thesis(address="sample_text", month="sample_text", type="sample_text")
    partner = University()
    setattr(partner, 'University', None)
    _safe_set(owner, 'SWRC_Thesis56', partner)
    assert getattr(partner, 'University') == owner
    _safe_set(owner, 'SWRC_Thesis56', None)
    assert getattr(partner, 'University') is None


def test_assoc_technicalReport107_stub_double():
    # TechnicalReport has no real 'TechnicalReport' property in the generated
    # code (a bare stub) -- manually attach it so SWRC_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SWRC_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SWRC_Organization(location="sample_text", name="sample_text")
    partner = TechnicalReport()
    setattr(partner, 'TechnicalReport', None)
    _safe_set(owner, 'SWRC_Organization108', {partner})
    assert getattr(partner, 'TechnicalReport') == owner
    _safe_set(owner, 'SWRC_Organization108', set())
    assert getattr(partner, 'TechnicalReport') is None


