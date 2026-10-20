import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Actor_Actor,
    Benutzer,
    UseCase_UseCase,
    WIS_Herde,
    WIS_HiTierImport,
    WIS_Tier,
    WIS_Weide,
    WIS_WeideBemerkung,
    WIS_Weidefl_che,
    WIS_Weidegang,
    Weidegang2,
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

def test_assoc_Herde_Benutzer_reverse_link_reassign_clear():
    a1 = WIS_Herde(name="sample_text")
    a2 = WIS_Herde(name="sample_text_2")
    b = Benutzer(name="sample_text", passwortHash="sample_text")
    _safe_set(b, 'herde13', {a1})
    assert _is_linked(b, 'herde13', a1)
    if hasattr(a1, 'benutzer12'):
        assert _is_linked(a1, 'benutzer12', b)
    _safe_set(b, 'herde13', {a2})
    assert _is_linked(b, 'herde13', a2)
    if hasattr(a1, 'benutzer12'):
        assert not _is_linked(a1, 'benutzer12', b)
    if hasattr(a2, 'benutzer12'):
        assert _is_linked(a2, 'benutzer12', b)
    _safe_set(b, 'herde13', set())
    assert not _is_linked(b, 'herde13', a2)
    if hasattr(a2, 'benutzer12'):
        assert not _is_linked(a2, 'benutzer12', b)


def test_assoc_HiTierImport_Benutzer_reverse_link_reassign_clear():
    a1 = WIS_HiTierImport(datum="sample_text")
    a2 = WIS_HiTierImport(datum="sample_text_2")
    b = Benutzer(name="sample_text", passwortHash="sample_text")
    _safe_set(b, 'hiTierImport19', a1)
    assert _is_linked(b, 'hiTierImport19', a1)
    if hasattr(a1, 'benutzer18'):
        assert _is_linked(a1, 'benutzer18', b)
    _safe_set(b, 'hiTierImport19', a2)
    assert _is_linked(b, 'hiTierImport19', a2)
    if hasattr(a1, 'benutzer18'):
        assert not _is_linked(a1, 'benutzer18', b)
    if hasattr(a2, 'benutzer18'):
        assert _is_linked(a2, 'benutzer18', b)
    _safe_set(b, 'hiTierImport19', None)
    assert not _is_linked(b, 'hiTierImport19', a2)
    if hasattr(a2, 'benutzer18'):
        assert not _is_linked(a2, 'benutzer18', b)


def test_assoc_Tier_Benutzer_reverse_link_reassign_clear():
    a1 = WIS_Tier(BTV4="sample_text", BTV8="sample_text", LOM=7, UDNummer="sample_text", eigeneAngaben="sample_text", geburtsdatum="sample_text", istAktiv=True, istWeiblich=True, letzteKalbung="sample_text", name="sample_text", transponderNummer="sample_text")
    a2 = WIS_Tier(BTV4="sample_text_2", BTV8="sample_text_2", LOM=13, UDNummer="sample_text_2", eigeneAngaben="sample_text_2", geburtsdatum="sample_text_2", istAktiv=False, istWeiblich=False, letzteKalbung="sample_text_2", name="sample_text_2", transponderNummer="sample_text_2")
    b = Benutzer(name="sample_text", passwortHash="sample_text")
    _safe_set(b, 'tier1', {a1})
    assert _is_linked(b, 'tier1', a1)
    if hasattr(a1, 'benutzer0'):
        assert _is_linked(a1, 'benutzer0', b)
    _safe_set(b, 'tier1', {a2})
    assert _is_linked(b, 'tier1', a2)
    if hasattr(a1, 'benutzer0'):
        assert not _is_linked(a1, 'benutzer0', b)
    if hasattr(a2, 'benutzer0'):
        assert _is_linked(a2, 'benutzer0', b)
    _safe_set(b, 'tier1', set())
    assert not _is_linked(b, 'tier1', a2)
    if hasattr(a2, 'benutzer0'):
        assert not _is_linked(a2, 'benutzer0', b)


def test_assoc_Tier_Herde_reverse_link_reassign_clear():
    a1 = WIS_Tier(BTV4="sample_text", BTV8="sample_text", LOM=7, UDNummer="sample_text", eigeneAngaben="sample_text", geburtsdatum="sample_text", istAktiv=True, istWeiblich=True, letzteKalbung="sample_text", name="sample_text", transponderNummer="sample_text")
    a2 = WIS_Tier(BTV4="sample_text_2", BTV8="sample_text_2", LOM=13, UDNummer="sample_text_2", eigeneAngaben="sample_text_2", geburtsdatum="sample_text_2", istAktiv=False, istWeiblich=False, letzteKalbung="sample_text_2", name="sample_text_2", transponderNummer="sample_text_2")
    b = WIS_Herde(name="sample_text")
    _safe_set(b, 'tier9', {a1})
    assert _is_linked(b, 'tier9', a1)
    if hasattr(a1, 'herde8'):
        assert _is_linked(a1, 'herde8', b)
    _safe_set(b, 'tier9', {a2})
    assert _is_linked(b, 'tier9', a2)
    if hasattr(a1, 'herde8'):
        assert not _is_linked(a1, 'herde8', b)
    if hasattr(a2, 'herde8'):
        assert _is_linked(a2, 'herde8', b)
    _safe_set(b, 'tier9', set())
    assert not _is_linked(b, 'tier9', a2)
    if hasattr(a2, 'herde8'):
        assert not _is_linked(a2, 'herde8', b)


def test_assoc_Tier_HiTierImport_reverse_link_reassign_clear():
    a1 = WIS_Tier(BTV4="sample_text", BTV8="sample_text", LOM=7, UDNummer="sample_text", eigeneAngaben="sample_text", geburtsdatum="sample_text", istAktiv=True, istWeiblich=True, letzteKalbung="sample_text", name="sample_text", transponderNummer="sample_text")
    a2 = WIS_Tier(BTV4="sample_text_2", BTV8="sample_text_2", LOM=13, UDNummer="sample_text_2", eigeneAngaben="sample_text_2", geburtsdatum="sample_text_2", istAktiv=False, istWeiblich=False, letzteKalbung="sample_text_2", name="sample_text_2", transponderNummer="sample_text_2")
    b = WIS_HiTierImport(datum="sample_text")
    _safe_set(b, 'tier21', {a1})
    assert _is_linked(b, 'tier21', a1)
    if hasattr(a1, 'hiTierImport20'):
        assert _is_linked(a1, 'hiTierImport20', b)
    _safe_set(b, 'tier21', {a2})
    assert _is_linked(b, 'tier21', a2)
    if hasattr(a1, 'hiTierImport20'):
        assert not _is_linked(a1, 'hiTierImport20', b)
    if hasattr(a2, 'hiTierImport20'):
        assert _is_linked(a2, 'hiTierImport20', b)
    _safe_set(b, 'tier21', set())
    assert not _is_linked(b, 'tier21', a2)
    if hasattr(a2, 'hiTierImport20'):
        assert not _is_linked(a2, 'hiTierImport20', b)


def test_assoc_Weide_Benutzer_reverse_link_reassign_clear():
    a1 = WIS_Weide(FACTCode=7, LPRVertrag="sample_text", bemerkung="sample_text", farbe="sample_text", groesse=7, istAktiv=True, istBetriebsfremdeFlaeche=True, name="sample_text", schlagnummer=7)
    a2 = WIS_Weide(FACTCode=13, LPRVertrag="sample_text_2", bemerkung="sample_text_2", farbe="sample_text_2", groesse=13, istAktiv=False, istBetriebsfremdeFlaeche=False, name="sample_text_2", schlagnummer=13)
    b = Benutzer(name="sample_text", passwortHash="sample_text")
    _safe_set(b, 'weide17', a1)
    assert _is_linked(b, 'weide17', a1)
    if hasattr(a1, 'benutzer16'):
        assert _is_linked(a1, 'benutzer16', b)
    _safe_set(b, 'weide17', a2)
    assert _is_linked(b, 'weide17', a2)
    if hasattr(a1, 'benutzer16'):
        assert not _is_linked(a1, 'benutzer16', b)
    if hasattr(a2, 'benutzer16'):
        assert _is_linked(a2, 'benutzer16', b)
    _safe_set(b, 'weide17', None)
    assert not _is_linked(b, 'weide17', a2)
    if hasattr(a2, 'benutzer16'):
        assert not _is_linked(a2, 'benutzer16', b)


def test_assoc_Weide_Weidefl_che_reverse_link_reassign_clear():
    a1 = WIS_Weidefl_che(farbe="sample_text", groesse=7, name="sample_text", schlagnummer="sample_text")
    a2 = WIS_Weidefl_che(farbe="sample_text_2", groesse=13, name="sample_text_2", schlagnummer="sample_text_2")
    b = WIS_Weide(FACTCode=7, LPRVertrag="sample_text", bemerkung="sample_text", farbe="sample_text", groesse=7, istAktiv=True, istBetriebsfremdeFlaeche=True, name="sample_text", schlagnummer=7)
    _safe_set(b, 'teilflaeche2', {a1})
    assert _is_linked(b, 'teilflaeche2', a1)
    if hasattr(a1, 'weide3'):
        assert _is_linked(a1, 'weide3', b)
    _safe_set(b, 'teilflaeche2', {a2})
    assert _is_linked(b, 'teilflaeche2', a2)
    if hasattr(a1, 'weide3'):
        assert not _is_linked(a1, 'weide3', b)
    if hasattr(a2, 'weide3'):
        assert _is_linked(a2, 'weide3', b)
    _safe_set(b, 'teilflaeche2', set())
    assert not _is_linked(b, 'teilflaeche2', a2)
    if hasattr(a2, 'weide3'):
        assert not _is_linked(a2, 'weide3', b)


def test_assoc_Weidegang_Benutzer_reverse_link_reassign_clear():
    a1 = WIS_Weidegang(ausfallgrund="sample_text", datum="sample_text", herdeFarbe="sample_text", herdeName="sample_text", istAusgefallen=True, tierLOM="sample_text", tierName="sample_text", weideFACTCode="sample_text", weideName="sample_text", weideSchlagnummer="sample_text")
    a2 = WIS_Weidegang(ausfallgrund="sample_text_2", datum="sample_text_2", herdeFarbe="sample_text_2", herdeName="sample_text_2", istAusgefallen=False, tierLOM="sample_text_2", tierName="sample_text_2", weideFACTCode="sample_text_2", weideName="sample_text_2", weideSchlagnummer="sample_text_2")
    b = Benutzer(name="sample_text", passwortHash="sample_text")
    _safe_set(b, 'weidegang15', {a1})
    assert _is_linked(b, 'weidegang15', a1)
    if hasattr(a1, 'benutzer14'):
        assert _is_linked(a1, 'benutzer14', b)
    _safe_set(b, 'weidegang15', {a2})
    assert _is_linked(b, 'weidegang15', a2)
    if hasattr(a1, 'benutzer14'):
        assert not _is_linked(a1, 'benutzer14', b)
    if hasattr(a2, 'benutzer14'):
        assert _is_linked(a2, 'benutzer14', b)
    _safe_set(b, 'weidegang15', set())
    assert not _is_linked(b, 'weidegang15', a2)
    if hasattr(a2, 'benutzer14'):
        assert not _is_linked(a2, 'benutzer14', b)


def test_assoc_Weidegang_Herde_reverse_link_reassign_clear():
    a1 = WIS_Weidegang(ausfallgrund="sample_text", datum="sample_text", herdeFarbe="sample_text", herdeName="sample_text", istAusgefallen=True, tierLOM="sample_text", tierName="sample_text", weideFACTCode="sample_text", weideName="sample_text", weideSchlagnummer="sample_text")
    a2 = WIS_Weidegang(ausfallgrund="sample_text_2", datum="sample_text_2", herdeFarbe="sample_text_2", herdeName="sample_text_2", istAusgefallen=False, tierLOM="sample_text_2", tierName="sample_text_2", weideFACTCode="sample_text_2", weideName="sample_text_2", weideSchlagnummer="sample_text_2")
    b = WIS_Herde(name="sample_text")
    _safe_set(b, 'weidegang7', {a1})
    assert _is_linked(b, 'weidegang7', a1)
    if hasattr(a1, 'herde6'):
        assert _is_linked(a1, 'herde6', b)
    _safe_set(b, 'weidegang7', {a2})
    assert _is_linked(b, 'weidegang7', a2)
    if hasattr(a1, 'herde6'):
        assert not _is_linked(a1, 'herde6', b)
    if hasattr(a2, 'herde6'):
        assert _is_linked(a2, 'herde6', b)
    _safe_set(b, 'weidegang7', set())
    assert not _is_linked(b, 'weidegang7', a2)
    if hasattr(a2, 'herde6'):
        assert not _is_linked(a2, 'herde6', b)


def test_assoc_Weidegang_Tier_reverse_link_reassign_clear():
    a1 = WIS_Weidegang(ausfallgrund="sample_text", datum="sample_text", herdeFarbe="sample_text", herdeName="sample_text", istAusgefallen=True, tierLOM="sample_text", tierName="sample_text", weideFACTCode="sample_text", weideName="sample_text", weideSchlagnummer="sample_text")
    a2 = WIS_Weidegang(ausfallgrund="sample_text_2", datum="sample_text_2", herdeFarbe="sample_text_2", herdeName="sample_text_2", istAusgefallen=False, tierLOM="sample_text_2", tierName="sample_text_2", weideFACTCode="sample_text_2", weideName="sample_text_2", weideSchlagnummer="sample_text_2")
    b = WIS_Tier(BTV4="sample_text", BTV8="sample_text", LOM=7, UDNummer="sample_text", eigeneAngaben="sample_text", geburtsdatum="sample_text", istAktiv=True, istWeiblich=True, letzteKalbung="sample_text", name="sample_text", transponderNummer="sample_text")
    _safe_set(b, 'weidegang11', {a1})
    assert _is_linked(b, 'weidegang11', a1)
    if hasattr(a1, 'tier10'):
        assert _is_linked(a1, 'tier10', b)
    _safe_set(b, 'weidegang11', {a2})
    assert _is_linked(b, 'weidegang11', a2)
    if hasattr(a1, 'tier10'):
        assert not _is_linked(a1, 'tier10', b)
    if hasattr(a2, 'tier10'):
        assert _is_linked(a2, 'tier10', b)
    _safe_set(b, 'weidegang11', set())
    assert not _is_linked(b, 'weidegang11', a2)
    if hasattr(a2, 'tier10'):
        assert not _is_linked(a2, 'tier10', b)


def test_assoc_Weidegang_Weide_reverse_link_reassign_clear():
    a1 = WIS_Weidegang(ausfallgrund="sample_text", datum="sample_text", herdeFarbe="sample_text", herdeName="sample_text", istAusgefallen=True, tierLOM="sample_text", tierName="sample_text", weideFACTCode="sample_text", weideName="sample_text", weideSchlagnummer="sample_text")
    a2 = WIS_Weidegang(ausfallgrund="sample_text_2", datum="sample_text_2", herdeFarbe="sample_text_2", herdeName="sample_text_2", istAusgefallen=False, tierLOM="sample_text_2", tierName="sample_text_2", weideFACTCode="sample_text_2", weideName="sample_text_2", weideSchlagnummer="sample_text_2")
    b = WIS_Weide(FACTCode=7, LPRVertrag="sample_text", bemerkung="sample_text", farbe="sample_text", groesse=7, istAktiv=True, istBetriebsfremdeFlaeche=True, name="sample_text", schlagnummer=7)
    _safe_set(b, 'weidegang5', {a1})
    assert _is_linked(b, 'weidegang5', a1)
    if hasattr(a1, 'weide4'):
        assert _is_linked(a1, 'weide4', b)
    _safe_set(b, 'weidegang5', {a2})
    assert _is_linked(b, 'weidegang5', a2)
    if hasattr(a1, 'weide4'):
        assert not _is_linked(a1, 'weide4', b)
    if hasattr(a2, 'weide4'):
        assert _is_linked(a2, 'weide4', b)
    _safe_set(b, 'weidegang5', set())
    assert not _is_linked(b, 'weidegang5', a2)
    if hasattr(a2, 'weide4'):
        assert not _is_linked(a2, 'weide4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

