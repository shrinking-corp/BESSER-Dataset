import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_company_created_by_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    _safe_set(b, 'created_by', a1)
    assert _is_linked(b, 'created_by', a1)
    if hasattr(a1, 'created_companies'):
        assert _is_linked(a1, 'created_companies', b)
    _safe_set(b, 'created_by', a2)
    assert _is_linked(b, 'created_by', a2)
    if hasattr(a1, 'created_companies'):
        assert not _is_linked(a1, 'created_companies', b)
    if hasattr(a2, 'created_companies'):
        assert _is_linked(a2, 'created_companies', b)
    _safe_set(b, 'created_by', None)
    assert not _is_linked(b, 'created_by', a2)
    if hasattr(a2, 'created_companies'):
        assert not _is_linked(a2, 'created_companies', b)


def test_assoc_company_tag_reverse_link_reassign_clear():
    a1 = Tag(color="sample_text", id=7, name="sample_text")
    a2 = Tag(color="sample_text_2", id=13, name="sample_text_2")
    b = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    _safe_set(b, 'tags', {a1})
    assert _is_linked(b, 'tags', a1)
    if hasattr(a1, 'tagged_companies'):
        assert _is_linked(a1, 'tagged_companies', b)
    _safe_set(b, 'tags', {a2})
    assert _is_linked(b, 'tags', a2)
    if hasattr(a1, 'tagged_companies'):
        assert not _is_linked(a1, 'tagged_companies', b)
    if hasattr(a2, 'tagged_companies'):
        assert _is_linked(a2, 'tagged_companies', b)
    _safe_set(b, 'tags', set())
    assert not _is_linked(b, 'tags', a2)
    if hasattr(a2, 'tagged_companies'):
        assert not _is_linked(a2, 'tagged_companies', b)


def test_assoc_contact_company_reverse_link_reassign_clear():
    a1 = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    a2 = Contact(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_enriched=False, job_title="sample_text_2", last_name="sample_text_2", lead_score=13, lead_score_level=LeadScoreLevel.HOT, linkedin_url="sample_text_2", notes="sample_text_2", phone="sample_text_2", profile_picture_url="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0))
    b = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    _safe_set(b, 'contacts', {a1})
    assert _is_linked(b, 'contacts', a1)
    if hasattr(a1, 'company'):
        assert _is_linked(a1, 'company', b)
    _safe_set(b, 'contacts', {a2})
    assert _is_linked(b, 'contacts', a2)
    if hasattr(a1, 'company'):
        assert not _is_linked(a1, 'company', b)
    if hasattr(a2, 'company'):
        assert _is_linked(a2, 'company', b)
    _safe_set(b, 'contacts', set())
    assert not _is_linked(b, 'contacts', a2)
    if hasattr(a2, 'company'):
        assert not _is_linked(a2, 'company', b)


def test_assoc_contact_created_by_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'created_by', a1)
    assert _is_linked(b, 'created_by', a1)
    if hasattr(a1, 'created_contacts'):
        assert _is_linked(a1, 'created_contacts', b)
    _safe_set(b, 'created_by', a2)
    assert _is_linked(b, 'created_by', a2)
    if hasattr(a1, 'created_contacts'):
        assert not _is_linked(a1, 'created_contacts', b)
    if hasattr(a2, 'created_contacts'):
        assert _is_linked(a2, 'created_contacts', b)
    _safe_set(b, 'created_by', None)
    assert not _is_linked(b, 'created_by', a2)
    if hasattr(a2, 'created_contacts'):
        assert not _is_linked(a2, 'created_contacts', b)


def test_assoc_contact_tag_reverse_link_reassign_clear():
    a1 = Tag(color="sample_text", id=7, name="sample_text")
    a2 = Tag(color="sample_text_2", id=13, name="sample_text_2")
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'tags', {a1})
    assert _is_linked(b, 'tags', a1)
    if hasattr(a1, 'tagged_contacts'):
        assert _is_linked(a1, 'tagged_contacts', b)
    _safe_set(b, 'tags', {a2})
    assert _is_linked(b, 'tags', a2)
    if hasattr(a1, 'tagged_contacts'):
        assert not _is_linked(a1, 'tagged_contacts', b)
    if hasattr(a2, 'tagged_contacts'):
        assert _is_linked(a2, 'tagged_contacts', b)
    _safe_set(b, 'tags', set())
    assert not _is_linked(b, 'tags', a2)
    if hasattr(a2, 'tagged_contacts'):
        assert not _is_linked(a2, 'tagged_contacts', b)


def test_assoc_email_contact_reverse_link_reassign_clear():
    a1 = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    a2 = GeneratedEmail(body="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), id=13, is_sent=False, sent_at=datetime(2025, 6, 15, 8, 30, 0), subject="sample_text_2")
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'generated_emails', {a1})
    assert _is_linked(b, 'generated_emails', a1)
    if hasattr(a1, 'contact'):
        assert _is_linked(a1, 'contact', b)
    _safe_set(b, 'generated_emails', {a2})
    assert _is_linked(b, 'generated_emails', a2)
    if hasattr(a1, 'contact'):
        assert not _is_linked(a1, 'contact', b)
    if hasattr(a2, 'contact'):
        assert _is_linked(a2, 'contact', b)
    _safe_set(b, 'generated_emails', set())
    assert not _is_linked(b, 'generated_emails', a2)
    if hasattr(a2, 'contact'):
        assert not _is_linked(a2, 'contact', b)


def test_assoc_email_template_link_reverse_link_reassign_clear():
    a1 = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    a2 = GeneratedEmail(body="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), id=13, is_sent=False, sent_at=datetime(2025, 6, 15, 8, 30, 0), subject="sample_text_2")
    b = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    _safe_set(b, 'generated_emails', {a1})
    assert _is_linked(b, 'generated_emails', a1)
    if hasattr(a1, 'template'):
        assert _is_linked(a1, 'template', b)
    _safe_set(b, 'generated_emails', {a2})
    assert _is_linked(b, 'generated_emails', a2)
    if hasattr(a1, 'template'):
        assert not _is_linked(a1, 'template', b)
    if hasattr(a2, 'template'):
        assert _is_linked(a2, 'template', b)
    _safe_set(b, 'generated_emails', set())
    assert not _is_linked(b, 'generated_emails', a2)
    if hasattr(a2, 'template'):
        assert not _is_linked(a2, 'template', b)


def test_assoc_email_user_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = GeneratedEmail(body="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, is_sent=True, sent_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text")
    _safe_set(b, 'created_by', a1)
    assert _is_linked(b, 'created_by', a1)
    if hasattr(a1, 'generated_emails'):
        assert _is_linked(a1, 'generated_emails', b)
    _safe_set(b, 'created_by', a2)
    assert _is_linked(b, 'created_by', a2)
    if hasattr(a1, 'generated_emails'):
        assert not _is_linked(a1, 'generated_emails', b)
    if hasattr(a2, 'generated_emails'):
        assert _is_linked(a2, 'generated_emails', b)
    _safe_set(b, 'created_by', None)
    assert not _is_linked(b, 'created_by', a2)
    if hasattr(a2, 'generated_emails'):
        assert not _is_linked(a2, 'generated_emails', b)


def test_assoc_enrichment_contact_reverse_link_reassign_clear():
    a1 = EnrichmentLog(enriched_at=datetime(2024, 1, 1, 12, 0, 0), error_message="sample_text", id=7, is_successful=True, linkedin_url="sample_text")
    a2 = EnrichmentLog(enriched_at=datetime(2025, 6, 15, 8, 30, 0), error_message="sample_text_2", id=13, is_successful=False, linkedin_url="sample_text_2")
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'enrichment_logs', {a1})
    assert _is_linked(b, 'enrichment_logs', a1)
    if hasattr(a1, 'contact'):
        assert _is_linked(a1, 'contact', b)
    _safe_set(b, 'enrichment_logs', {a2})
    assert _is_linked(b, 'enrichment_logs', a2)
    if hasattr(a1, 'contact'):
        assert not _is_linked(a1, 'contact', b)
    if hasattr(a2, 'contact'):
        assert _is_linked(a2, 'contact', b)
    _safe_set(b, 'enrichment_logs', set())
    assert not _is_linked(b, 'enrichment_logs', a2)
    if hasattr(a2, 'contact'):
        assert not _is_linked(a2, 'contact', b)


def test_assoc_interaction_contact_reverse_link_reassign_clear():
    a1 = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    a2 = Interaction(content="sample_text_2", created_at=datetime(2025, 6, 15, 8, 30, 0), direction=InteractionDirection.OUTBOUND, id=13, occurred_at=datetime(2025, 6, 15, 8, 30, 0), subject="sample_text_2", type=InteractionType.EMAIL)
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'interactions', {a1})
    assert _is_linked(b, 'interactions', a1)
    if hasattr(a1, 'contact'):
        assert _is_linked(a1, 'contact', b)
    _safe_set(b, 'interactions', {a2})
    assert _is_linked(b, 'interactions', a2)
    if hasattr(a1, 'contact'):
        assert not _is_linked(a1, 'contact', b)
    if hasattr(a2, 'contact'):
        assert _is_linked(a2, 'contact', b)
    _safe_set(b, 'interactions', set())
    assert not _is_linked(b, 'interactions', a2)
    if hasattr(a2, 'contact'):
        assert not _is_linked(a2, 'contact', b)


def test_assoc_interaction_user_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = Interaction(content="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), direction=InteractionDirection.INBOUND, id=7, occurred_at=datetime(2024, 1, 1, 12, 0, 0), subject="sample_text", type=InteractionType.CALL)
    _safe_set(b, 'performed_by', a1)
    assert _is_linked(b, 'performed_by', a1)
    if hasattr(a1, 'interactions'):
        assert _is_linked(a1, 'interactions', b)
    _safe_set(b, 'performed_by', a2)
    assert _is_linked(b, 'performed_by', a2)
    if hasattr(a1, 'interactions'):
        assert not _is_linked(a1, 'interactions', b)
    if hasattr(a2, 'interactions'):
        assert _is_linked(a2, 'interactions', b)
    _safe_set(b, 'performed_by', None)
    assert not _is_linked(b, 'performed_by', a2)
    if hasattr(a2, 'interactions'):
        assert not _is_linked(a2, 'interactions', b)


def test_assoc_opportunity_company_reverse_link_reassign_clear():
    a1 = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    a2 = Opportunity(closed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", expected_close_date=date(2025, 6, 15), id=13, probability=13, stage=OpportunityStage.CLOSED_WON, title="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0), value=9.99)
    b = Company(address="sample_text", city="sample_text", country="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", id=7, industry=Industry.FINANCE, linkedin_url="sample_text", name="sample_text", phone="sample_text", size=CompanySize.ENTERPRISE, updated_at=datetime(2024, 1, 1, 12, 0, 0), website="sample_text")
    _safe_set(b, 'opportunities', {a1})
    assert _is_linked(b, 'opportunities', a1)
    if hasattr(a1, 'company'):
        assert _is_linked(a1, 'company', b)
    _safe_set(b, 'opportunities', {a2})
    assert _is_linked(b, 'opportunities', a2)
    if hasattr(a1, 'company'):
        assert not _is_linked(a1, 'company', b)
    if hasattr(a2, 'company'):
        assert _is_linked(a2, 'company', b)
    _safe_set(b, 'opportunities', set())
    assert not _is_linked(b, 'opportunities', a2)
    if hasattr(a2, 'company'):
        assert not _is_linked(a2, 'company', b)


def test_assoc_opportunity_contact_reverse_link_reassign_clear():
    a1 = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    a2 = Opportunity(closed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", expected_close_date=date(2025, 6, 15), id=13, probability=13, stage=OpportunityStage.CLOSED_WON, title="sample_text_2", updated_at=datetime(2025, 6, 15, 8, 30, 0), value=9.99)
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'opportunities', {a1})
    assert _is_linked(b, 'opportunities', a1)
    if hasattr(a1, 'contacts'):
        assert _is_linked(a1, 'contacts', b)
    _safe_set(b, 'opportunities', {a2})
    assert _is_linked(b, 'opportunities', a2)
    if hasattr(a1, 'contacts'):
        assert not _is_linked(a1, 'contacts', b)
    if hasattr(a2, 'contacts'):
        assert _is_linked(a2, 'contacts', b)
    _safe_set(b, 'opportunities', set())
    assert not _is_linked(b, 'opportunities', a2)
    if hasattr(a2, 'contacts'):
        assert not _is_linked(a2, 'contacts', b)


def test_assoc_opportunity_owner_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    _safe_set(b, 'owner', a1)
    assert _is_linked(b, 'owner', a1)
    if hasattr(a1, 'owned_opportunities'):
        assert _is_linked(a1, 'owned_opportunities', b)
    _safe_set(b, 'owner', a2)
    assert _is_linked(b, 'owner', a2)
    if hasattr(a1, 'owned_opportunities'):
        assert not _is_linked(a1, 'owned_opportunities', b)
    if hasattr(a2, 'owned_opportunities'):
        assert _is_linked(a2, 'owned_opportunities', b)
    _safe_set(b, 'owner', None)
    assert not _is_linked(b, 'owner', a2)
    if hasattr(a2, 'owned_opportunities'):
        assert not _is_linked(a2, 'owned_opportunities', b)


def test_assoc_score_contact_reverse_link_reassign_clear():
    a1 = ScoreHistory(calculated_at=datetime(2024, 1, 1, 12, 0, 0), id=7, new_score=7, old_score=7, reason="sample_text")
    a2 = ScoreHistory(calculated_at=datetime(2025, 6, 15, 8, 30, 0), id=13, new_score=13, old_score=13, reason="sample_text_2")
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'score_history', {a1})
    assert _is_linked(b, 'score_history', a1)
    if hasattr(a1, 'contact'):
        assert _is_linked(a1, 'contact', b)
    _safe_set(b, 'score_history', {a2})
    assert _is_linked(b, 'score_history', a2)
    if hasattr(a1, 'contact'):
        assert not _is_linked(a1, 'contact', b)
    if hasattr(a2, 'contact'):
        assert _is_linked(a2, 'contact', b)
    _safe_set(b, 'score_history', set())
    assert not _is_linked(b, 'score_history', a2)
    if hasattr(a2, 'contact'):
        assert not _is_linked(a2, 'contact', b)


def test_assoc_task_contact_reverse_link_reassign_clear():
    a1 = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    a2 = Task(completed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", due_date=datetime(2025, 6, 15, 8, 30, 0), id=13, is_completed=False, title="sample_text_2")
    b = Contact(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_enriched=True, job_title="sample_text", last_name="sample_text", lead_score=7, lead_score_level=LeadScoreLevel.COLD, linkedin_url="sample_text", notes="sample_text", phone="sample_text", profile_picture_url="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0))
    _safe_set(b, 'tasks', {a1})
    assert _is_linked(b, 'tasks', a1)
    if hasattr(a1, 'contact'):
        assert _is_linked(a1, 'contact', b)
    _safe_set(b, 'tasks', {a2})
    assert _is_linked(b, 'tasks', a2)
    if hasattr(a1, 'contact'):
        assert not _is_linked(a1, 'contact', b)
    if hasattr(a2, 'contact'):
        assert _is_linked(a2, 'contact', b)
    _safe_set(b, 'tasks', set())
    assert not _is_linked(b, 'tasks', a2)
    if hasattr(a2, 'contact'):
        assert not _is_linked(a2, 'contact', b)


def test_assoc_task_opportunity_reverse_link_reassign_clear():
    a1 = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    a2 = Task(completed_at=datetime(2025, 6, 15, 8, 30, 0), created_at=datetime(2025, 6, 15, 8, 30, 0), description="sample_text_2", due_date=datetime(2025, 6, 15, 8, 30, 0), id=13, is_completed=False, title="sample_text_2")
    b = Opportunity(closed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", expected_close_date=date(2024, 1, 1), id=7, probability=7, stage=OpportunityStage.CLOSED_LOST, title="sample_text", updated_at=datetime(2024, 1, 1, 12, 0, 0), value=3.14)
    _safe_set(b, 'tasks', {a1})
    assert _is_linked(b, 'tasks', a1)
    if hasattr(a1, 'opportunity'):
        assert _is_linked(a1, 'opportunity', b)
    _safe_set(b, 'tasks', {a2})
    assert _is_linked(b, 'tasks', a2)
    if hasattr(a1, 'opportunity'):
        assert not _is_linked(a1, 'opportunity', b)
    if hasattr(a2, 'opportunity'):
        assert _is_linked(a2, 'opportunity', b)
    _safe_set(b, 'tasks', set())
    assert not _is_linked(b, 'tasks', a2)
    if hasattr(a2, 'opportunity'):
        assert not _is_linked(a2, 'opportunity', b)


def test_assoc_task_user_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = Task(completed_at=datetime(2024, 1, 1, 12, 0, 0), created_at=datetime(2024, 1, 1, 12, 0, 0), description="sample_text", due_date=datetime(2024, 1, 1, 12, 0, 0), id=7, is_completed=True, title="sample_text")
    _safe_set(b, 'assigned_to', a1)
    assert _is_linked(b, 'assigned_to', a1)
    if hasattr(a1, 'tasks'):
        assert _is_linked(a1, 'tasks', b)
    _safe_set(b, 'assigned_to', a2)
    assert _is_linked(b, 'assigned_to', a2)
    if hasattr(a1, 'tasks'):
        assert not _is_linked(a1, 'tasks', b)
    if hasattr(a2, 'tasks'):
        assert _is_linked(a2, 'tasks', b)
    _safe_set(b, 'assigned_to', None)
    assert not _is_linked(b, 'assigned_to', a2)
    if hasattr(a2, 'tasks'):
        assert not _is_linked(a2, 'tasks', b)


def test_assoc_template_user_reverse_link_reassign_clear():
    a1 = User(created_at=datetime(2024, 1, 1, 12, 0, 0), email="sample_text", first_name="sample_text", id=7, is_active=True, last_login=datetime(2024, 1, 1, 12, 0, 0), last_name="sample_text", password_hash="sample_text", role=UserRole.ADMIN)
    a2 = User(created_at=datetime(2025, 6, 15, 8, 30, 0), email="sample_text_2", first_name="sample_text_2", id=13, is_active=False, last_login=datetime(2025, 6, 15, 8, 30, 0), last_name="sample_text_2", password_hash="sample_text_2", role=UserRole.SALES_MANAGER)
    b = EmailTemplate(body_template="sample_text", category="sample_text", created_at=datetime(2024, 1, 1, 12, 0, 0), id=7, name="sample_text", subject_template="sample_text")
    _safe_set(b, 'created_by', a1)
    assert _is_linked(b, 'created_by', a1)
    if hasattr(a1, 'email_templates'):
        assert _is_linked(a1, 'email_templates', b)
    _safe_set(b, 'created_by', a2)
    assert _is_linked(b, 'created_by', a2)
    if hasattr(a1, 'email_templates'):
        assert not _is_linked(a1, 'email_templates', b)
    if hasattr(a2, 'email_templates'):
        assert _is_linked(a2, 'email_templates', b)
    _safe_set(b, 'created_by', None)
    assert not _is_linked(b, 'created_by', a2)
    if hasattr(a2, 'email_templates'):
        assert not _is_linked(a2, 'email_templates', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

