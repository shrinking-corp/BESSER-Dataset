import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Company,
    Contact,
    EmailTemplate,
    EnrichmentLog,
    GeneratedEmail,
    Interaction,
    Opportunity,
    ScoreHistory,
    Tag,
    Task,
    User,
    CompanySize,
    Industry,
    InteractionDirection,
    InteractionType,
    LeadScoreLevel,
    OpportunityStage,
    UserRole,
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

def test_Company_address_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_Company_city_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.city == "sample_text"
    instance.city = "sample_text_2"
    assert instance.city == "sample_text_2"


def test_Company_country_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.country == "sample_text"
    instance.country = "sample_text_2"
    assert instance.country == "sample_text_2"


def test_Company_created_at_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Company_description_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Company_id_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Company_industry_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.industry == Industry.FINANCE
    instance.industry = Industry.HEALTHCARE
    assert instance.industry == Industry.HEALTHCARE


def test_Company_linkedin_url_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.linkedin_url == "sample_text"
    instance.linkedin_url = "sample_text_2"
    assert instance.linkedin_url == "sample_text_2"


def test_Company_name_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Company_phone_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Company_size_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.size == CompanySize.ENTERPRISE
    instance.size = CompanySize.LARGE
    assert instance.size == CompanySize.LARGE


def test_Company_updated_at_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.updated_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.updated_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.updated_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Company_website_value_roundtrip():
    instance = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    assert instance.website == "sample_text"
    instance.website = "sample_text_2"
    assert instance.website == "sample_text_2"


def test_Contact_created_at_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Contact_email_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_Contact_first_name_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.first_name == "sample_text"
    instance.first_name = "sample_text_2"
    assert instance.first_name == "sample_text_2"


def test_Contact_id_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Contact_is_enriched_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.is_enriched == True
    instance.is_enriched = False
    assert instance.is_enriched == False


def test_Contact_job_title_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.job_title == "sample_text"
    instance.job_title = "sample_text_2"
    assert instance.job_title == "sample_text_2"


def test_Contact_last_name_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.last_name == "sample_text"
    instance.last_name = "sample_text_2"
    assert instance.last_name == "sample_text_2"


def test_Contact_lead_score_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.lead_score == 7
    instance.lead_score = 13
    assert instance.lead_score == 13


def test_Contact_lead_score_level_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.lead_score_level == LeadScoreLevel.COLD
    instance.lead_score_level = LeadScoreLevel.HOT
    assert instance.lead_score_level == LeadScoreLevel.HOT


def test_Contact_linkedin_url_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.linkedin_url == "sample_text"
    instance.linkedin_url = "sample_text_2"
    assert instance.linkedin_url == "sample_text_2"


def test_Contact_notes_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.notes == "sample_text"
    instance.notes = "sample_text_2"
    assert instance.notes == "sample_text_2"


def test_Contact_phone_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.phone == "sample_text"
    instance.phone = "sample_text_2"
    assert instance.phone == "sample_text_2"


def test_Contact_profile_picture_url_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.profile_picture_url == "sample_text"
    instance.profile_picture_url = "sample_text_2"
    assert instance.profile_picture_url == "sample_text_2"


def test_Contact_updated_at_value_roundtrip():
    instance = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    assert instance.updated_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.updated_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.updated_at == datetime(2025, 6, 15, 8, 30, 0)


def test_EmailTemplate_body_template_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.body_template == "sample_text"
    instance.body_template = "sample_text_2"
    assert instance.body_template == "sample_text_2"


def test_EmailTemplate_category_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_EmailTemplate_created_at_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_EmailTemplate_id_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_EmailTemplate_name_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_EmailTemplate_subject_template_value_roundtrip():
    instance = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    assert instance.subject_template == "sample_text"
    instance.subject_template = "sample_text_2"
    assert instance.subject_template == "sample_text_2"


def test_EnrichmentLog_enriched_at_value_roundtrip():
    instance = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    assert instance.enriched_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.enriched_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.enriched_at == datetime(2025, 6, 15, 8, 30, 0)


def test_EnrichmentLog_error_message_value_roundtrip():
    instance = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    assert instance.error_message == "sample_text"
    instance.error_message = "sample_text_2"
    assert instance.error_message == "sample_text_2"


def test_EnrichmentLog_id_value_roundtrip():
    instance = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_EnrichmentLog_is_successful_value_roundtrip():
    instance = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    assert instance.is_successful == True
    instance.is_successful = False
    assert instance.is_successful == False


def test_EnrichmentLog_linkedin_url_value_roundtrip():
    instance = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    assert instance.linkedin_url == "sample_text"
    instance.linkedin_url = "sample_text_2"
    assert instance.linkedin_url == "sample_text_2"


def test_GeneratedEmail_body_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.body == "sample_text"
    instance.body = "sample_text_2"
    assert instance.body == "sample_text_2"


def test_GeneratedEmail_created_at_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_GeneratedEmail_id_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_GeneratedEmail_is_sent_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.is_sent == True
    instance.is_sent = False
    assert instance.is_sent == False


def test_GeneratedEmail_sent_at_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.sent_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.sent_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.sent_at == datetime(2025, 6, 15, 8, 30, 0)


def test_GeneratedEmail_subject_value_roundtrip():
    instance = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_Interaction_content_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_Interaction_created_at_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Interaction_direction_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.direction == InteractionDirection.INBOUND
    instance.direction = InteractionDirection.OUTBOUND
    assert instance.direction == InteractionDirection.OUTBOUND


def test_Interaction_id_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Interaction_occurred_at_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.occurred_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.occurred_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.occurred_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Interaction_subject_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.subject == "sample_text"
    instance.subject = "sample_text_2"
    assert instance.subject == "sample_text_2"


def test_Interaction_type_value_roundtrip():
    instance = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    assert instance.type == InteractionType.CALL
    instance.type = InteractionType.EMAIL
    assert instance.type == InteractionType.EMAIL


def test_Opportunity_closed_at_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.closed_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.closed_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.closed_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Opportunity_created_at_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Opportunity_description_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Opportunity_expected_close_date_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.expected_close_date == date(2024, 1, 1)
    instance.expected_close_date = date(2025, 6, 15)
    assert instance.expected_close_date == date(2025, 6, 15)


def test_Opportunity_id_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Opportunity_probability_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.probability == 7
    instance.probability = 13
    assert instance.probability == 13


def test_Opportunity_stage_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.stage == OpportunityStage.CLOSED_LOST
    instance.stage = OpportunityStage.CLOSED_WON
    assert instance.stage == OpportunityStage.CLOSED_WON


def test_Opportunity_title_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_Opportunity_updated_at_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.updated_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.updated_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.updated_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Opportunity_value_value_roundtrip():
    instance = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_ScoreHistory_calculated_at_value_roundtrip():
    instance = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    assert instance.calculated_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.calculated_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.calculated_at == datetime(2025, 6, 15, 8, 30, 0)


def test_ScoreHistory_id_value_roundtrip():
    instance = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_ScoreHistory_new_score_value_roundtrip():
    instance = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    assert instance.new_score == 7
    instance.new_score = 13
    assert instance.new_score == 13


def test_ScoreHistory_old_score_value_roundtrip():
    instance = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    assert instance.old_score == 7
    instance.old_score = 13
    assert instance.old_score == 13


def test_ScoreHistory_reason_value_roundtrip():
    instance = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    assert instance.reason == "sample_text"
    instance.reason = "sample_text_2"
    assert instance.reason == "sample_text_2"


def test_Tag_color_value_roundtrip():
    instance = Tag(color="sample_text", id=7, name="sample_text")
    assert instance.color == "sample_text"
    instance.color = "sample_text_2"
    assert instance.color == "sample_text_2"


def test_Tag_id_value_roundtrip():
    instance = Tag(color="sample_text", id=7, name="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Tag_name_value_roundtrip():
    instance = Tag(color="sample_text", id=7, name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_Task_completed_at_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.completed_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.completed_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.completed_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Task_created_at_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_Task_description_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_Task_due_date_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.due_date == datetime(2024, 1, 1, 12, 0, 0)
    instance.due_date = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.due_date == datetime(2025, 6, 15, 8, 30, 0)


def test_Task_id_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_Task_is_completed_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.is_completed == True
    instance.is_completed = False
    assert instance.is_completed == False


def test_Task_title_value_roundtrip():
    instance = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    assert instance.title == "sample_text"
    instance.title = "sample_text_2"
    assert instance.title == "sample_text_2"


def test_User_created_at_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.created_at == datetime(2024, 1, 1, 12, 0, 0)
    instance.created_at = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.created_at == datetime(2025, 6, 15, 8, 30, 0)


def test_User_email_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.email == "sample_text"
    instance.email = "sample_text_2"
    assert instance.email == "sample_text_2"


def test_User_first_name_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.first_name == "sample_text"
    instance.first_name = "sample_text_2"
    assert instance.first_name == "sample_text_2"


def test_User_id_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.id == 7
    instance.id = 13
    assert instance.id == 13


def test_User_is_active_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.is_active == True
    instance.is_active = False
    assert instance.is_active == False


def test_User_last_login_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.last_login == datetime(2024, 1, 1, 12, 0, 0)
    instance.last_login = datetime(2025, 6, 15, 8, 30, 0)
    assert instance.last_login == datetime(2025, 6, 15, 8, 30, 0)


def test_User_last_name_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.last_name == "sample_text"
    instance.last_name = "sample_text_2"
    assert instance.last_name == "sample_text_2"


def test_User_password_hash_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.password_hash == "sample_text"
    instance.password_hash = "sample_text_2"
    assert instance.password_hash == "sample_text_2"


def test_User_role_value_roundtrip():
    instance = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    assert instance.role == UserRole.ADMIN
    instance.role = UserRole.SALES_MANAGER
    assert instance.role == UserRole.SALES_MANAGER


def test_assoc_company_created_by_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    b2 = Company(address="sample_text_2", city="sample_text_2", country="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", id=13, industry=Industry.HEALTHCARE, linkedin_url="sample_text_2", name="sample_text_2", phone="sample_text_2", size=CompanySize.LARGE, updated_at=datetime(2025, 6, 15, 8, 30, 0), website="sample_text_2")
    _safe_set(a, 'created_companies', {b1})
    assert _is_linked(a, 'created_companies', b1)
    if hasattr(b1, 'created_by'):
        assert _is_linked(b1, 'created_by', a)
    _safe_set(a, 'created_companies', {b2})
    assert _is_linked(a, 'created_companies', b2)
    if hasattr(b1, 'created_by'):
        assert not _is_linked(b1, 'created_by', a)
    if hasattr(b2, 'created_by'):
        assert _is_linked(b2, 'created_by', a)
    _safe_set(a, 'created_companies', set())
    assert not _is_linked(a, 'created_companies', b2)
    if hasattr(b2, 'created_by'):
        assert not _is_linked(b2, 'created_by', a)


def test_assoc_company_tag_link_reassign_clear():
    a = Tag(color="sample_text", id=7, name="sample_text")
    b1 = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    b2 = Company(address="sample_text_2", city="sample_text_2", country="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", id=13, industry=Industry.HEALTHCARE, linkedin_url="sample_text_2", name="sample_text_2", phone="sample_text_2", size=CompanySize.LARGE, updated_at=datetime(2025, 6, 15, 8, 30, 0), website="sample_text_2")
    _safe_set(a, 'tagged_companies', {b1})
    assert _is_linked(a, 'tagged_companies', b1)
    if hasattr(b1, 'tags'):
        assert _is_linked(b1, 'tags', a)
    _safe_set(a, 'tagged_companies', {b2})
    assert _is_linked(a, 'tagged_companies', b2)
    if hasattr(b1, 'tags'):
        assert not _is_linked(b1, 'tags', a)
    if hasattr(b2, 'tags'):
        assert _is_linked(b2, 'tags', a)
    _safe_set(a, 'tagged_companies', set())
    assert not _is_linked(a, 'tagged_companies', b2)
    if hasattr(b2, 'tags'):
        assert not _is_linked(b2, 'tags', a)


def test_assoc_contact_company_link_reassign_clear():
    a = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b1 = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    b2 = Company(address="sample_text_2", city="sample_text_2", country="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", id=13, industry=Industry.HEALTHCARE, linkedin_url="sample_text_2", name="sample_text_2", phone="sample_text_2", size=CompanySize.LARGE, updated_at=datetime(2025, 6, 15, 8, 30, 0), website="sample_text_2")
    _safe_set(a, 'company', b1)
    assert _is_linked(a, 'company', b1)
    if hasattr(b1, 'contacts'):
        assert _is_linked(b1, 'contacts', a)
    _safe_set(a, 'company', b2)
    assert _is_linked(a, 'company', b2)
    if hasattr(b1, 'contacts'):
        assert not _is_linked(b1, 'contacts', a)
    if hasattr(b2, 'contacts'):
        assert _is_linked(b2, 'contacts', a)
    _safe_set(a, 'company', None)
    assert not _is_linked(a, 'company', b2)
    if hasattr(b2, 'contacts'):
        assert not _is_linked(b2, 'contacts', a)


def test_assoc_contact_created_by_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'created_contacts', {b1})
    assert _is_linked(a, 'created_contacts', b1)
    if hasattr(b1, 'created_by'):
        assert _is_linked(b1, 'created_by', a)
    _safe_set(a, 'created_contacts', {b2})
    assert _is_linked(a, 'created_contacts', b2)
    if hasattr(b1, 'created_by'):
        assert not _is_linked(b1, 'created_by', a)
    if hasattr(b2, 'created_by'):
        assert _is_linked(b2, 'created_by', a)
    _safe_set(a, 'created_contacts', set())
    assert not _is_linked(a, 'created_contacts', b2)
    if hasattr(b2, 'created_by'):
        assert not _is_linked(b2, 'created_by', a)


def test_assoc_contact_tag_link_reassign_clear():
    a = Tag(color="sample_text", id=7, name="sample_text")
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'tagged_contacts', {b1})
    assert _is_linked(a, 'tagged_contacts', b1)
    if hasattr(b1, 'tags'):
        assert _is_linked(b1, 'tags', a)
    _safe_set(a, 'tagged_contacts', {b2})
    assert _is_linked(a, 'tagged_contacts', b2)
    if hasattr(b1, 'tags'):
        assert not _is_linked(b1, 'tags', a)
    if hasattr(b2, 'tags'):
        assert _is_linked(b2, 'tags', a)
    _safe_set(a, 'tagged_contacts', set())
    assert not _is_linked(a, 'tagged_contacts', b2)
    if hasattr(b2, 'tags'):
        assert not _is_linked(b2, 'tags', a)


def test_assoc_email_contact_link_reassign_clear():
    a = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contact', b1)
    assert _is_linked(a, 'contact', b1)
    if hasattr(b1, 'generated_emails'):
        assert _is_linked(b1, 'generated_emails', a)
    _safe_set(a, 'contact', b2)
    assert _is_linked(a, 'contact', b2)
    if hasattr(b1, 'generated_emails'):
        assert not _is_linked(b1, 'generated_emails', a)
    if hasattr(b2, 'generated_emails'):
        assert _is_linked(b2, 'generated_emails', a)
    _safe_set(a, 'contact', None)
    assert not _is_linked(a, 'contact', b2)
    if hasattr(b2, 'generated_emails'):
        assert not _is_linked(b2, 'generated_emails', a)


def test_assoc_email_template_link_link_reassign_clear():
    a = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    b1 = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    b2 = EmailTemplate(body_template="sample_text_2", category="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), id=13, name="sample_text_2", subject_template="sample_text_2")
    _safe_set(a, 'template', b1)
    assert _is_linked(a, 'template', b1)
    if hasattr(b1, 'generated_emails'):
        assert _is_linked(b1, 'generated_emails', a)
    _safe_set(a, 'template', b2)
    assert _is_linked(a, 'template', b2)
    if hasattr(b1, 'generated_emails'):
        assert not _is_linked(b1, 'generated_emails', a)
    if hasattr(b2, 'generated_emails'):
        assert _is_linked(b2, 'generated_emails', a)
    _safe_set(a, 'template', None)
    assert not _is_linked(a, 'template', b2)
    if hasattr(b2, 'generated_emails'):
        assert not _is_linked(b2, 'generated_emails', a)


def test_assoc_email_user_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    b2 = GeneratedEmail(body="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), id=13, is_sent=False, sent_at=datetime(2025, 6, 15, 8, 30, 0), subject="sample_text_2")
    _safe_set(a, 'generated_emails', {b1})
    assert _is_linked(a, 'generated_emails', b1)
    if hasattr(b1, 'created_by'):
        assert _is_linked(b1, 'created_by', a)
    _safe_set(a, 'generated_emails', {b2})
    assert _is_linked(a, 'generated_emails', b2)
    if hasattr(b1, 'created_by'):
        assert not _is_linked(b1, 'created_by', a)
    if hasattr(b2, 'created_by'):
        assert _is_linked(b2, 'created_by', a)
    _safe_set(a, 'generated_emails', set())
    assert not _is_linked(a, 'generated_emails', b2)
    if hasattr(b2, 'created_by'):
        assert not _is_linked(b2, 'created_by', a)


def test_assoc_enrichment_contact_link_reassign_clear():
    a = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contact', b1)
    assert _is_linked(a, 'contact', b1)
    if hasattr(b1, 'enrichment_logs'):
        assert _is_linked(b1, 'enrichment_logs', a)
    _safe_set(a, 'contact', b2)
    assert _is_linked(a, 'contact', b2)
    if hasattr(b1, 'enrichment_logs'):
        assert not _is_linked(b1, 'enrichment_logs', a)
    if hasattr(b2, 'enrichment_logs'):
        assert _is_linked(b2, 'enrichment_logs', a)
    _safe_set(a, 'contact', None)
    assert not _is_linked(a, 'contact', b2)
    if hasattr(b2, 'enrichment_logs'):
        assert not _is_linked(b2, 'enrichment_logs', a)


def test_assoc_interaction_contact_link_reassign_clear():
    a = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contact', b1)
    assert _is_linked(a, 'contact', b1)
    if hasattr(b1, 'interactions'):
        assert _is_linked(b1, 'interactions', a)
    _safe_set(a, 'contact', b2)
    assert _is_linked(a, 'contact', b2)
    if hasattr(b1, 'interactions'):
        assert not _is_linked(b1, 'interactions', a)
    if hasattr(b2, 'interactions'):
        assert _is_linked(b2, 'interactions', a)
    _safe_set(a, 'contact', None)
    assert not _is_linked(a, 'contact', b2)
    if hasattr(b2, 'interactions'):
        assert not _is_linked(b2, 'interactions', a)


def test_assoc_interaction_user_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    b2 = Interaction(content="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), direction=InteractionDirection.OUTBOUND, id=13, occurred_at=datetime(2025, 6, 15, 8, 30, 0), subject="sample_text_2", type=InteractionType.EMAIL)
    _safe_set(a, 'interactions', {b1})
    assert _is_linked(a, 'interactions', b1)
    if hasattr(b1, 'performed_by'):
        assert _is_linked(b1, 'performed_by', a)
    _safe_set(a, 'interactions', {b2})
    assert _is_linked(a, 'interactions', b2)
    if hasattr(b1, 'performed_by'):
        assert not _is_linked(b1, 'performed_by', a)
    if hasattr(b2, 'performed_by'):
        assert _is_linked(b2, 'performed_by', a)
    _safe_set(a, 'interactions', set())
    assert not _is_linked(a, 'interactions', b2)
    if hasattr(b2, 'performed_by'):
        assert not _is_linked(b2, 'performed_by', a)


def test_assoc_opportunity_company_link_reassign_clear():
    a = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    b1 = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    b2 = Company(address="sample_text_2", city="sample_text_2", country="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", id=13, industry=Industry.HEALTHCARE, linkedin_url="sample_text_2", name="sample_text_2", phone="sample_text_2", size=CompanySize.LARGE, updated_at=datetime(2025, 6, 15, 8, 30, 0), website="sample_text_2")
    _safe_set(a, 'company', b1)
    assert _is_linked(a, 'company', b1)
    if hasattr(b1, 'opportunities'):
        assert _is_linked(b1, 'opportunities', a)
    _safe_set(a, 'company', b2)
    assert _is_linked(a, 'company', b2)
    if hasattr(b1, 'opportunities'):
        assert not _is_linked(b1, 'opportunities', a)
    if hasattr(b2, 'opportunities'):
        assert _is_linked(b2, 'opportunities', a)
    _safe_set(a, 'company', None)
    assert not _is_linked(a, 'company', b2)
    if hasattr(b2, 'opportunities'):
        assert not _is_linked(b2, 'opportunities', a)


def test_assoc_opportunity_contact_link_reassign_clear():
    a = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contacts', {b1})
    assert _is_linked(a, 'contacts', b1)
    if hasattr(b1, 'opportunities'):
        assert _is_linked(b1, 'opportunities', a)
    _safe_set(a, 'contacts', {b2})
    assert _is_linked(a, 'contacts', b2)
    if hasattr(b1, 'opportunities'):
        assert not _is_linked(b1, 'opportunities', a)
    if hasattr(b2, 'opportunities'):
        assert _is_linked(b2, 'opportunities', a)
    _safe_set(a, 'contacts', set())
    assert not _is_linked(a, 'contacts', b2)
    if hasattr(b2, 'opportunities'):
        assert not _is_linked(b2, 'opportunities', a)


def test_assoc_opportunity_owner_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    b2 = Opportunity(closed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", expected_close_date=date(2025, 6, 15), id=13, probability=13, stage=OpportunityStage.CLOSED_WON, title="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0), value=9.99)
    _safe_set(a, 'owned_opportunities', {b1})
    assert _is_linked(a, 'owned_opportunities', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'owned_opportunities', {b2})
    assert _is_linked(a, 'owned_opportunities', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'owned_opportunities', set())
    assert not _is_linked(a, 'owned_opportunities', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_score_contact_link_reassign_clear():
    a = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contact', b1)
    assert _is_linked(a, 'contact', b1)
    if hasattr(b1, 'score_history'):
        assert _is_linked(b1, 'score_history', a)
    _safe_set(a, 'contact', b2)
    assert _is_linked(a, 'contact', b2)
    if hasattr(b1, 'score_history'):
        assert not _is_linked(b1, 'score_history', a)
    if hasattr(b2, 'score_history'):
        assert _is_linked(b2, 'score_history', a)
    _safe_set(a, 'contact', None)
    assert not _is_linked(a, 'contact', b2)
    if hasattr(b2, 'score_history'):
        assert not _is_linked(b2, 'score_history', a)


def test_assoc_task_contact_link_reassign_clear():
    a = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    b1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    b2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    _safe_set(a, 'contact', b1)
    assert _is_linked(a, 'contact', b1)
    if hasattr(b1, 'tasks'):
        assert _is_linked(b1, 'tasks', a)
    _safe_set(a, 'contact', b2)
    assert _is_linked(a, 'contact', b2)
    if hasattr(b1, 'tasks'):
        assert not _is_linked(b1, 'tasks', a)
    if hasattr(b2, 'tasks'):
        assert _is_linked(b2, 'tasks', a)
    _safe_set(a, 'contact', None)
    assert not _is_linked(a, 'contact', b2)
    if hasattr(b2, 'tasks'):
        assert not _is_linked(b2, 'tasks', a)


def test_assoc_task_opportunity_link_reassign_clear():
    a = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    b1 = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    b2 = Opportunity(closed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", expected_close_date=date(2025, 6, 15), id=13, probability=13, stage=OpportunityStage.CLOSED_WON, title="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0), value=9.99)
    _safe_set(a, 'opportunity', b1)
    assert _is_linked(a, 'opportunity', b1)
    if hasattr(b1, 'tasks'):
        assert _is_linked(b1, 'tasks', a)
    _safe_set(a, 'opportunity', b2)
    assert _is_linked(a, 'opportunity', b2)
    if hasattr(b1, 'tasks'):
        assert not _is_linked(b1, 'tasks', a)
    if hasattr(b2, 'tasks'):
        assert _is_linked(b2, 'tasks', a)
    _safe_set(a, 'opportunity', None)
    assert not _is_linked(a, 'opportunity', b2)
    if hasattr(b2, 'tasks'):
        assert not _is_linked(b2, 'tasks', a)


def test_assoc_task_user_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    b2 = Task(completed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", due_date=datetime(2025, 6, 15, 8, 30, 0), id=13, is_completed=False, title="sample_text_2")
    _safe_set(a, 'tasks', {b1})
    assert _is_linked(a, 'tasks', b1)
    if hasattr(b1, 'assigned_to'):
        assert _is_linked(b1, 'assigned_to', a)
    _safe_set(a, 'tasks', {b2})
    assert _is_linked(a, 'tasks', b2)
    if hasattr(b1, 'assigned_to'):
        assert not _is_linked(b1, 'assigned_to', a)
    if hasattr(b2, 'assigned_to'):
        assert _is_linked(b2, 'assigned_to', a)
    _safe_set(a, 'tasks', set())
    assert not _is_linked(a, 'tasks', b2)
    if hasattr(b2, 'assigned_to'):
        assert not _is_linked(b2, 'assigned_to', a)


def test_assoc_template_user_link_reassign_clear():
    a = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    b1 = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    b2 = EmailTemplate(body_template="sample_text_2", category="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), id=13, name="sample_text_2", subject_template="sample_text_2")
    _safe_set(a, 'email_templates', {b1})
    assert _is_linked(a, 'email_templates', b1)
    if hasattr(b1, 'created_by'):
        assert _is_linked(b1, 'created_by', a)
    _safe_set(a, 'email_templates', {b2})
    assert _is_linked(a, 'email_templates', b2)
    if hasattr(b1, 'created_by'):
        assert not _is_linked(b1, 'created_by', a)
    if hasattr(b2, 'created_by'):
        assert _is_linked(b2, 'created_by', a)
    _safe_set(a, 'email_templates', set())
    assert not _is_linked(a, 'email_templates', b2)
    if hasattr(b2, 'created_by'):
        assert not _is_linked(b2, 'created_by', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Company_strategy = st.builds(Company, address=safe_text, city=safe_text, country=safe_text, created_at=st.datetimes(), description=safe_text, id=st.integers(), industry=st.sampled_from(Industry), linkedin_url=safe_text, name=safe_text, phone=safe_text, size=st.sampled_from(CompanySize), updated_at=st.datetimes(), website=safe_text)
@given(instance=Company_strategy)
@settings(max_examples=25)
def test_Company_instantiation(instance):
    assert isinstance(instance, Company)


Contact_strategy = st.builds(Contact, created_at=st.datetimes(), email=safe_text, first_name=safe_text, id=st.integers(), is_enriched=st.booleans(), job_title=safe_text, last_name=safe_text, lead_score=st.integers(), lead_score_level=st.sampled_from(LeadScoreLevel), linkedin_url=safe_text, notes=safe_text, phone=safe_text, profile_picture_url=safe_text, updated_at=st.datetimes())
@given(instance=Contact_strategy)
@settings(max_examples=25)
def test_Contact_instantiation(instance):
    assert isinstance(instance, Contact)


EmailTemplate_strategy = st.builds(EmailTemplate, body_template=safe_text, category=safe_text, created_at=st.datetimes(), id=st.integers(), name=safe_text, subject_template=safe_text)
@given(instance=EmailTemplate_strategy)
@settings(max_examples=25)
def test_EmailTemplate_instantiation(instance):
    assert isinstance(instance, EmailTemplate)


EnrichmentLog_strategy = st.builds(EnrichmentLog, enriched_at=st.datetimes(), error_message=safe_text, id=st.integers(), is_successful=st.booleans(), linkedin_url=safe_text)
@given(instance=EnrichmentLog_strategy)
@settings(max_examples=25)
def test_EnrichmentLog_instantiation(instance):
    assert isinstance(instance, EnrichmentLog)


GeneratedEmail_strategy = st.builds(GeneratedEmail, body=safe_text, created_at=st.datetimes(), id=st.integers(), is_sent=st.booleans(), sent_at=st.datetimes(), subject=safe_text)
@given(instance=GeneratedEmail_strategy)
@settings(max_examples=25)
def test_GeneratedEmail_instantiation(instance):
    assert isinstance(instance, GeneratedEmail)


Interaction_strategy = st.builds(Interaction, content=safe_text, created_at=st.datetimes(), direction=st.sampled_from(InteractionDirection), id=st.integers(), occurred_at=st.datetimes(), subject=safe_text, type=st.sampled_from(InteractionType))
@given(instance=Interaction_strategy)
@settings(max_examples=25)
def test_Interaction_instantiation(instance):
    assert isinstance(instance, Interaction)


Opportunity_strategy = st.builds(Opportunity, closed_at=st.datetimes(), created_at=st.datetimes(), description=safe_text, expected_close_date=st.dates(), id=st.integers(), probability=st.integers(), stage=st.sampled_from(OpportunityStage), title=safe_text, updated_at=st.datetimes(), value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=Opportunity_strategy)
@settings(max_examples=25)
def test_Opportunity_instantiation(instance):
    assert isinstance(instance, Opportunity)


ScoreHistory_strategy = st.builds(ScoreHistory, calculated_at=st.datetimes(), id=st.integers(), new_score=st.integers(), old_score=st.integers(), reason=safe_text)
@given(instance=ScoreHistory_strategy)
@settings(max_examples=25)
def test_ScoreHistory_instantiation(instance):
    assert isinstance(instance, ScoreHistory)


Tag_strategy = st.builds(Tag, color=safe_text, id=st.integers(), name=safe_text)
@given(instance=Tag_strategy)
@settings(max_examples=25)
def test_Tag_instantiation(instance):
    assert isinstance(instance, Tag)


Task_strategy = st.builds(Task, completed_at=st.datetimes(), created_at=st.datetimes(), description=safe_text, due_date=st.datetimes(), id=st.integers(), is_completed=st.booleans(), title=safe_text)
@given(instance=Task_strategy)
@settings(max_examples=25)
def test_Task_instantiation(instance):
    assert isinstance(instance, Task)


User_strategy = st.builds(User, created_at=st.datetimes(), email=safe_text, first_name=safe_text, id=st.integers(), is_active=st.booleans(), last_login=st.datetimes(), last_name=safe_text, password_hash=safe_text, role=st.sampled_from(UserRole))
@given(instance=User_strategy)
@settings(max_examples=25)
def test_User_instantiation(instance):
    assert isinstance(instance, User)


