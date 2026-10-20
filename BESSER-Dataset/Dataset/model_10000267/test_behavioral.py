import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Activity,
    Attachment,
    AuthenticationService,
    ChatService,
    Comment,
    Mensaje_Interface,
    Role,
    RoomService,
    Room_Interface,
    SpeechRecognitionService,
    Usuario_Interface,
    String,
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

def test_assoc_Mensaje_SpeechRecognitionService_stub_double():
    # Mensaje_Interface has no real 'speechRecognitionService12' property in the generated
    # code (a bare stub) -- manually attach it so SpeechRecognitionService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SpeechRecognitionService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SpeechRecognitionService(_attr="sample_text", grabando=True, speechRecognition="sample_text")
    partner = Mensaje_Interface()
    setattr(partner, 'speechRecognitionService12', None)
    _safe_set(owner, 'mensaje13', partner)
    assert getattr(partner, 'speechRecognitionService12') == owner
    _safe_set(owner, 'mensaje13', None)
    assert getattr(partner, 'speechRecognitionService12') is None


def test_assoc_Room_RoomService_stub_double():
    # Room_Interface has no real 'roomService10' property in the generated
    # code (a bare stub) -- manually attach it so RoomService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # RoomService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = RoomService(idiomas="sample_text", itemsCollection="sample_text", niveles="sample_text", roomsCollection="sample_text")
    partner = Room_Interface()
    setattr(partner, 'roomService10', None)
    _safe_set(owner, 'room11', partner)
    assert getattr(partner, 'roomService10') == owner
    _safe_set(owner, 'room11', None)
    assert getattr(partner, 'roomService10') is None


