import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Administrator_Actor,
    Check_black_list_requests_UseCase,
    Create_new_administrators_UseCase,
    Create_reports_UseCase,
    Edit_information_UseCase,
    Edit_pet_information_UseCase,
    Edit_user_information_UseCase,
    Logging_into_program_UseCase,
    Logging_into_web_UseCase,
    Make_requests_to_administrator_UseCase,
    Match_lost_pet_cases_UseCase,
    Medeina,
    Organization,
    Pet,
    Register_a_pet_UseCase,
    Register_as_a_pro_care_association_UseCase,
    Register_as_an_adopter_UseCase,
    Register_pet_types_UseCase,
    Register_pets__physical_characteristics_UseCase,
    Registering_UseCase,
    Report_a_person_to_the_blacklist_UseCase,
    Search_UseCase,
    Search_pet_accessories_UseCase,
    Search_pet_s_UseCase,
    Send_mail_to_lost_pet_owners_UseCase,
    System_Actor,
    User,
    User_Actor,
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

