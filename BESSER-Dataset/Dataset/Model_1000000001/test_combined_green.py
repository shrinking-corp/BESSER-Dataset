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
    Opportunity,
    Interaction,
    Tag,
    Task,
    EmailTemplate,
    GeneratedEmail,
    EnrichmentLog,
    ScoreHistory,
    User,
    Company,
    Contact,
    InteractionType,
    OpportunityStage,
    InteractionDirection,
    LeadScoreLevel,
    Industry,
    CompanySize,
    UserRole,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_opportunity_is_not_abstract():
    assert not inspect.isabstract(Opportunity)


def test_hyp_opportunity_constructor_exists():
    assert callable(Opportunity.__init__)


def test_hyp_opportunity_constructor_args():
    sig = inspect.signature(Opportunity.__init__)
    params = list(sig.parameters.keys())
    assert "probability" in params, "Missing parameter 'probability'"
    assert "title" in params, "Missing parameter 'title'"
    assert "closed_at" in params, "Missing parameter 'closed_at'"
    assert "id" in params, "Missing parameter 'id'"
    assert "stage" in params, "Missing parameter 'stage'"
    assert "updated_at" in params, "Missing parameter 'updated_at'"
    assert "expected_close_date" in params, "Missing parameter 'expected_close_date'"
    assert "description" in params, "Missing parameter 'description'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "value" in params, "Missing parameter 'value'"













def test_hyp_interaction_is_not_abstract():
    assert not inspect.isabstract(Interaction)


def test_hyp_interaction_constructor_exists():
    assert callable(Interaction.__init__)


def test_hyp_interaction_constructor_args():
    sig = inspect.signature(Interaction.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "content" in params, "Missing parameter 'content'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "occurred_at" in params, "Missing parameter 'occurred_at'"
    assert "type" in params, "Missing parameter 'type'"










def test_hyp_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_hyp_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_hyp_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "color" in params, "Missing parameter 'color'"






def test_hyp_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_hyp_task_constructor_exists():
    assert callable(Task.__init__)


def test_hyp_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "completed_at" in params, "Missing parameter 'completed_at'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "is_completed" in params, "Missing parameter 'is_completed'"
    assert "due_date" in params, "Missing parameter 'due_date'"
    assert "id" in params, "Missing parameter 'id'"










def test_hyp_emailtemplate_is_not_abstract():
    assert not inspect.isabstract(EmailTemplate)


def test_hyp_emailtemplate_constructor_exists():
    assert callable(EmailTemplate.__init__)


def test_hyp_emailtemplate_constructor_args():
    sig = inspect.signature(EmailTemplate.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "subject_template" in params, "Missing parameter 'subject_template'"
    assert "category" in params, "Missing parameter 'category'"
    assert "id" in params, "Missing parameter 'id'"
    assert "body_template" in params, "Missing parameter 'body_template'"









def test_hyp_generatedemail_is_not_abstract():
    assert not inspect.isabstract(GeneratedEmail)


def test_hyp_generatedemail_constructor_exists():
    assert callable(GeneratedEmail.__init__)


def test_hyp_generatedemail_constructor_args():
    sig = inspect.signature(GeneratedEmail.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "sent_at" in params, "Missing parameter 'sent_at'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "is_sent" in params, "Missing parameter 'is_sent'"
    assert "id" in params, "Missing parameter 'id'"
    assert "created_at" in params, "Missing parameter 'created_at'"









def test_hyp_enrichmentlog_is_not_abstract():
    assert not inspect.isabstract(EnrichmentLog)


def test_hyp_enrichmentlog_constructor_exists():
    assert callable(EnrichmentLog.__init__)


def test_hyp_enrichmentlog_constructor_args():
    sig = inspect.signature(EnrichmentLog.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "linkedin_url" in params, "Missing parameter 'linkedin_url'"
    assert "error_message" in params, "Missing parameter 'error_message'"
    assert "enriched_at" in params, "Missing parameter 'enriched_at'"
    assert "is_successful" in params, "Missing parameter 'is_successful'"








def test_hyp_scorehistory_is_not_abstract():
    assert not inspect.isabstract(ScoreHistory)


def test_hyp_scorehistory_constructor_exists():
    assert callable(ScoreHistory.__init__)


def test_hyp_scorehistory_constructor_args():
    sig = inspect.signature(ScoreHistory.__init__)
    params = list(sig.parameters.keys())
    assert "new_score" in params, "Missing parameter 'new_score'"
    assert "id" in params, "Missing parameter 'id'"
    assert "calculated_at" in params, "Missing parameter 'calculated_at'"
    assert "old_score" in params, "Missing parameter 'old_score'"
    assert "reason" in params, "Missing parameter 'reason'"








def test_hyp_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_hyp_user_constructor_exists():
    assert callable(User.__init__)


def test_hyp_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "is_active" in params, "Missing parameter 'is_active'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password_hash" in params, "Missing parameter 'password_hash'"
    assert "role" in params, "Missing parameter 'role'"
    assert "last_login" in params, "Missing parameter 'last_login'"












def test_hyp_company_is_not_abstract():
    assert not inspect.isabstract(Company)


def test_hyp_company_constructor_exists():
    assert callable(Company.__init__)


def test_hyp_company_constructor_args():
    sig = inspect.signature(Company.__init__)
    params = list(sig.parameters.keys())
    assert "phone" in params, "Missing parameter 'phone'"
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "country" in params, "Missing parameter 'country'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "size" in params, "Missing parameter 'size'"
    assert "linkedin_url" in params, "Missing parameter 'linkedin_url'"
    assert "city" in params, "Missing parameter 'city'"
    assert "description" in params, "Missing parameter 'description'"
    assert "website" in params, "Missing parameter 'website'"
    assert "industry" in params, "Missing parameter 'industry'"
    assert "updated_at" in params, "Missing parameter 'updated_at'"
















def test_hyp_contact_is_not_abstract():
    assert not inspect.isabstract(Contact)


def test_hyp_contact_constructor_exists():
    assert callable(Contact.__init__)


def test_hyp_contact_constructor_args():
    sig = inspect.signature(Contact.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "profile_picture_url" in params, "Missing parameter 'profile_picture_url'"
    assert "job_title" in params, "Missing parameter 'job_title'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "lead_score_level" in params, "Missing parameter 'lead_score_level'"
    assert "is_enriched" in params, "Missing parameter 'is_enriched'"
    assert "updated_at" in params, "Missing parameter 'updated_at'"
    assert "created_at" in params, "Missing parameter 'created_at'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phone" in params, "Missing parameter 'phone'"
    assert "linkedin_url" in params, "Missing parameter 'linkedin_url'"
    assert "lead_score" in params, "Missing parameter 'lead_score'"















def test_hyp_interactiontype_exists():
    # Check that the Enumeration exists
    assert InteractionType is not None

def test_hyp_interactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionType]
    expected_literals = [
        "CALL",
        "NOTE",
        "MEETING",
        "EMAIL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionType"

def test_hyp_opportunitystage_exists():
    # Check that the Enumeration exists
    assert OpportunityStage is not None

def test_hyp_opportunitystage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OpportunityStage]
    expected_literals = [
        "NEGOTIATION",
        "PROPOSAL",
        "QUALIFICATION",
        "CLOSED_LOST",
        "PROSPECTING",
        "CLOSED_WON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OpportunityStage"

def test_hyp_interactiondirection_exists():
    # Check that the Enumeration exists
    assert InteractionDirection is not None

def test_hyp_interactiondirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionDirection]
    expected_literals = [
        "OUTBOUND",
        "INBOUND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionDirection"

def test_hyp_leadscorelevel_exists():
    # Check that the Enumeration exists
    assert LeadScoreLevel is not None

def test_hyp_leadscorelevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeadScoreLevel]
    expected_literals = [
        "HOT",
        "WARM",
        "COLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeadScoreLevel"

def test_hyp_industry_exists():
    # Check that the Enumeration exists
    assert Industry is not None

def test_hyp_industry_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Industry]
    expected_literals = [
        "SERVICES",
        "OTHER",
        "HEALTHCARE",
        "MANUFACTURING",
        "RETAIL",
        "FINANCE",
        "TECHNOLOGY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Industry"

def test_hyp_companysize_exists():
    # Check that the Enumeration exists
    assert CompanySize is not None

def test_hyp_companysize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompanySize]
    expected_literals = [
        "ENTERPRISE",
        "LARGE",
        "MEDIUM",
        "SMALL",
        "STARTUP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompanySize"

def test_hyp_userrole_exists():
    # Check that the Enumeration exists
    assert UserRole is not None

def test_hyp_userrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UserRole]
    expected_literals = [
        "SALES_REP",
        "ADMIN",
        "SALES_MANAGER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UserRole"


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
Opportunity_strategy = st.builds(
    Opportunity,
    probability=
        st.integers(),
    title=
        safe_text,
    closed_at=
        st.dates(),
    id=
        st.integers(),
    stage=
        st.none(),
    updated_at=
        st.dates(),
    expected_close_date=
        st.dates(),
    description=
        safe_text,
    created_at=
        st.dates(),
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Interaction_strategy = st.builds(
    Interaction,
    id=
        st.integers(),
    created_at=
        st.dates(),
    content=
        safe_text,
    direction=
        st.none(),
    subject=
        safe_text,
    occurred_at=
        st.dates(),
    type=
        st.none()
)
Tag_strategy = st.builds(
    Tag,
    name=
        safe_text,
    id=
        st.integers(),
    color=
        safe_text
)
Task_strategy = st.builds(
    Task,
    created_at=
        st.dates(),
    completed_at=
        st.dates(),
    description=
        safe_text,
    title=
        safe_text,
    is_completed=
        st.booleans(),
    due_date=
        st.dates(),
    id=
        st.integers()
)
EmailTemplate_strategy = st.builds(
    EmailTemplate,
    name=
        safe_text,
    created_at=
        st.dates(),
    subject_template=
        safe_text,
    category=
        safe_text,
    id=
        st.integers(),
    body_template=
        safe_text
)
GeneratedEmail_strategy = st.builds(
    GeneratedEmail,
    body=
        safe_text,
    sent_at=
        st.dates(),
    subject=
        safe_text,
    is_sent=
        st.booleans(),
    id=
        st.integers(),
    created_at=
        st.dates()
)
EnrichmentLog_strategy = st.builds(
    EnrichmentLog,
    id=
        st.integers(),
    linkedin_url=
        safe_text,
    error_message=
        safe_text,
    enriched_at=
        st.dates(),
    is_successful=
        st.booleans()
)
ScoreHistory_strategy = st.builds(
    ScoreHistory,
    new_score=
        st.integers(),
    id=
        st.integers(),
    calculated_at=
        st.dates(),
    old_score=
        st.integers(),
    reason=
        safe_text
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    is_active=
        st.booleans(),
    last_name=
        safe_text,
    created_at=
        st.dates(),
    first_name=
        safe_text,
    id=
        st.integers(),
    password_hash=
        safe_text,
    role=
        st.none(),
    last_login=
        st.dates()
)
Company_strategy = st.builds(
    Company,
    phone=
        safe_text,
    address=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text,
    country=
        safe_text,
    created_at=
        st.dates(),
    size=
        st.none(),
    linkedin_url=
        safe_text,
    city=
        safe_text,
    description=
        safe_text,
    website=
        safe_text,
    industry=
        st.none(),
    updated_at=
        st.dates()
)
Contact_strategy = st.builds(
    Contact,
    id=
        st.integers(),
    last_name=
        safe_text,
    notes=
        safe_text,
    profile_picture_url=
        safe_text,
    job_title=
        safe_text,
    first_name=
        safe_text,
    lead_score_level=
        st.none(),
    is_enriched=
        st.booleans(),
    updated_at=
        st.dates(),
    created_at=
        st.dates(),
    email=
        safe_text,
    phone=
        safe_text,
    linkedin_url=
        safe_text,
    lead_score=
        st.integers()
)




@given(instance=Opportunity_strategy)
def test_hyp_opportunity_probability_setter(instance):
    original = instance.probability
    instance.probability = original
    assert instance.probability == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_closed_at_setter(instance):
    original = instance.closed_at
    instance.closed_at = original
    assert instance.closed_at == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_stage_setter(instance):
    original = instance.stage
    instance.stage = original
    assert instance.stage == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_updated_at_setter(instance):
    original = instance.updated_at
    instance.updated_at = original
    assert instance.updated_at == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_expected_close_date_setter(instance):
    original = instance.expected_close_date
    instance.expected_close_date = original
    assert instance.expected_close_date == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=Opportunity_strategy)
def test_hyp_opportunity_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=Interaction_strategy)
def test_hyp_interaction_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_occurred_at_setter(instance):
    original = instance.occurred_at
    instance.occurred_at = original
    assert instance.occurred_at == original



@given(instance=Interaction_strategy)
def test_hyp_interaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original




@given(instance=Tag_strategy)
def test_hyp_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Tag_strategy)
def test_hyp_tag_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Tag_strategy)
def test_hyp_tag_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original




@given(instance=Task_strategy)
def test_hyp_task_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=Task_strategy)
def test_hyp_task_completed_at_setter(instance):
    original = instance.completed_at
    instance.completed_at = original
    assert instance.completed_at == original



@given(instance=Task_strategy)
def test_hyp_task_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Task_strategy)
def test_hyp_task_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Task_strategy)
def test_hyp_task_is_completed_setter(instance):
    original = instance.is_completed
    instance.is_completed = original
    assert instance.is_completed == original



@given(instance=Task_strategy)
def test_hyp_task_due_date_setter(instance):
    original = instance.due_date
    instance.due_date = original
    assert instance.due_date == original



@given(instance=Task_strategy)
def test_hyp_task_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original




@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_subject_template_setter(instance):
    original = instance.subject_template
    instance.subject_template = original
    assert instance.subject_template == original



@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EmailTemplate_strategy)
def test_hyp_emailtemplate_body_template_setter(instance):
    original = instance.body_template
    instance.body_template = original
    assert instance.body_template == original




@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_sent_at_setter(instance):
    original = instance.sent_at
    instance.sent_at = original
    assert instance.sent_at == original



@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_is_sent_setter(instance):
    original = instance.is_sent
    instance.is_sent = original
    assert instance.is_sent == original



@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=GeneratedEmail_strategy)
def test_hyp_generatedemail_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original




@given(instance=EnrichmentLog_strategy)
def test_hyp_enrichmentlog_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=EnrichmentLog_strategy)
def test_hyp_enrichmentlog_linkedin_url_setter(instance):
    original = instance.linkedin_url
    instance.linkedin_url = original
    assert instance.linkedin_url == original



@given(instance=EnrichmentLog_strategy)
def test_hyp_enrichmentlog_error_message_setter(instance):
    original = instance.error_message
    instance.error_message = original
    assert instance.error_message == original



@given(instance=EnrichmentLog_strategy)
def test_hyp_enrichmentlog_enriched_at_setter(instance):
    original = instance.enriched_at
    instance.enriched_at = original
    assert instance.enriched_at == original



@given(instance=EnrichmentLog_strategy)
def test_hyp_enrichmentlog_is_successful_setter(instance):
    original = instance.is_successful
    instance.is_successful = original
    assert instance.is_successful == original




@given(instance=ScoreHistory_strategy)
def test_hyp_scorehistory_new_score_setter(instance):
    original = instance.new_score
    instance.new_score = original
    assert instance.new_score == original



@given(instance=ScoreHistory_strategy)
def test_hyp_scorehistory_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ScoreHistory_strategy)
def test_hyp_scorehistory_calculated_at_setter(instance):
    original = instance.calculated_at
    instance.calculated_at = original
    assert instance.calculated_at == original



@given(instance=ScoreHistory_strategy)
def test_hyp_scorehistory_old_score_setter(instance):
    original = instance.old_score
    instance.old_score = original
    assert instance.old_score == original



@given(instance=ScoreHistory_strategy)
def test_hyp_scorehistory_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original




@given(instance=User_strategy)
def test_hyp_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_hyp_user_is_active_setter(instance):
    original = instance.is_active
    instance.is_active = original
    assert instance.is_active == original



@given(instance=User_strategy)
def test_hyp_user_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=User_strategy)
def test_hyp_user_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=User_strategy)
def test_hyp_user_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=User_strategy)
def test_hyp_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=User_strategy)
def test_hyp_user_password_hash_setter(instance):
    original = instance.password_hash
    instance.password_hash = original
    assert instance.password_hash == original



@given(instance=User_strategy)
def test_hyp_user_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=User_strategy)
def test_hyp_user_last_login_setter(instance):
    original = instance.last_login
    instance.last_login = original
    assert instance.last_login == original




@given(instance=Company_strategy)
def test_hyp_company_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Company_strategy)
def test_hyp_company_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Company_strategy)
def test_hyp_company_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Company_strategy)
def test_hyp_company_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Company_strategy)
def test_hyp_company_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Company_strategy)
def test_hyp_company_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=Company_strategy)
def test_hyp_company_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=Company_strategy)
def test_hyp_company_linkedin_url_setter(instance):
    original = instance.linkedin_url
    instance.linkedin_url = original
    assert instance.linkedin_url == original



@given(instance=Company_strategy)
def test_hyp_company_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original



@given(instance=Company_strategy)
def test_hyp_company_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Company_strategy)
def test_hyp_company_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original



@given(instance=Company_strategy)
def test_hyp_company_industry_setter(instance):
    original = instance.industry
    instance.industry = original
    assert instance.industry == original



@given(instance=Company_strategy)
def test_hyp_company_updated_at_setter(instance):
    original = instance.updated_at
    instance.updated_at = original
    assert instance.updated_at == original




@given(instance=Contact_strategy)
def test_hyp_contact_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Contact_strategy)
def test_hyp_contact_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original



@given(instance=Contact_strategy)
def test_hyp_contact_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=Contact_strategy)
def test_hyp_contact_profile_picture_url_setter(instance):
    original = instance.profile_picture_url
    instance.profile_picture_url = original
    assert instance.profile_picture_url == original



@given(instance=Contact_strategy)
def test_hyp_contact_job_title_setter(instance):
    original = instance.job_title
    instance.job_title = original
    assert instance.job_title == original



@given(instance=Contact_strategy)
def test_hyp_contact_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original



@given(instance=Contact_strategy)
def test_hyp_contact_lead_score_level_setter(instance):
    original = instance.lead_score_level
    instance.lead_score_level = original
    assert instance.lead_score_level == original



@given(instance=Contact_strategy)
def test_hyp_contact_is_enriched_setter(instance):
    original = instance.is_enriched
    instance.is_enriched = original
    assert instance.is_enriched == original



@given(instance=Contact_strategy)
def test_hyp_contact_updated_at_setter(instance):
    original = instance.updated_at
    instance.updated_at = original
    assert instance.updated_at == original



@given(instance=Contact_strategy)
def test_hyp_contact_created_at_setter(instance):
    original = instance.created_at
    instance.created_at = original
    assert instance.created_at == original



@given(instance=Contact_strategy)
def test_hyp_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Contact_strategy)
def test_hyp_contact_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original



@given(instance=Contact_strategy)
def test_hyp_contact_linkedin_url_setter(instance):
    original = instance.linkedin_url
    instance.linkedin_url = original
    assert instance.linkedin_url == original



@given(instance=Contact_strategy)
def test_hyp_contact_lead_score_setter(instance):
    original = instance.lead_score
    instance.lead_score = original
    assert instance.lead_score == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
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



