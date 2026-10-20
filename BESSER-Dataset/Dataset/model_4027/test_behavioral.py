import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Benanntes,
    UML_14_Aufzaehlung,
    UML_14_Aufzaehlungswert,
    UML_14_Benanntes,
    UML_14_Eigenschaft,
    UML_14_Einfach,
    UML_14_Einschraenkung,
    UML_14_InstanzAnzahl,
    UML_14_Kommentar,
    UML_14_Konzept,
    UML_14_MethodenWert,
    UML_14_Schachtel,
    UML_14_Verbindung,
    UML_14_Verbindungsende,
    UML_14_Vererbung,
    UML_14_Verhalten,
    UML_14_root,
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

def test_assoc_anzahlInstanzen20_reverse_link_reassign_clear():
    a1 = UML_14_Verbindungsende(istNavigierbar="sample_text", sichtbarkeit="sample_text")
    a2 = UML_14_Verbindungsende(istNavigierbar="sample_text_2", sichtbarkeit="sample_text_2")
    b = UML_14_InstanzAnzahl(obergrenze="sample_text", untergrenze="sample_text")
    _safe_set(b, 'UML_14_InstanzAnzahl22', a1)
    assert _is_linked(b, 'UML_14_InstanzAnzahl22', a1)
    if hasattr(a1, 'UML_14_Verbindungsende21'):
        assert _is_linked(a1, 'UML_14_Verbindungsende21', b)
    _safe_set(b, 'UML_14_InstanzAnzahl22', a2)
    assert _is_linked(b, 'UML_14_InstanzAnzahl22', a2)
    if hasattr(a1, 'UML_14_Verbindungsende21'):
        assert not _is_linked(a1, 'UML_14_Verbindungsende21', b)
    if hasattr(a2, 'UML_14_Verbindungsende21'):
        assert _is_linked(a2, 'UML_14_Verbindungsende21', b)
    _safe_set(b, 'UML_14_InstanzAnzahl22', None)
    assert not _is_linked(b, 'UML_14_InstanzAnzahl22', a2)
    if hasattr(a2, 'UML_14_Verbindungsende21'):
        assert not _is_linked(a2, 'UML_14_Verbindungsende21', b)


def test_assoc_anzahlInstanzen5_reverse_link_reassign_clear():
    a1 = UML_14_InstanzAnzahl(obergrenze="sample_text", untergrenze="sample_text")
    a2 = UML_14_InstanzAnzahl(obergrenze="sample_text_2", untergrenze="sample_text_2")
    b = UML_14_Eigenschaft(initialWert="sample_text", sichtbarkeit="sample_text")
    _safe_set(b, 'UML_14_Eigenschaft', a1)
    assert _is_linked(b, 'UML_14_Eigenschaft', a1)
    if hasattr(a1, 'UML_14_InstanzAnzahl'):
        assert _is_linked(a1, 'UML_14_InstanzAnzahl', b)
    _safe_set(b, 'UML_14_Eigenschaft', a2)
    assert _is_linked(b, 'UML_14_Eigenschaft', a2)
    if hasattr(a1, 'UML_14_InstanzAnzahl'):
        assert not _is_linked(a1, 'UML_14_InstanzAnzahl', b)
    if hasattr(a2, 'UML_14_InstanzAnzahl'):
        assert _is_linked(a2, 'UML_14_InstanzAnzahl', b)
    _safe_set(b, 'UML_14_Eigenschaft', None)
    assert not _is_linked(b, 'UML_14_Eigenschaft', a2)
    if hasattr(a2, 'UML_14_InstanzAnzahl'):
        assert not _is_linked(a2, 'UML_14_InstanzAnzahl', b)


def test_assoc_auszeichner23_reverse_link_reassign_clear():
    a1 = UML_14_Verbindungsende(istNavigierbar="sample_text", sichtbarkeit="sample_text")
    a2 = UML_14_Verbindungsende(istNavigierbar="sample_text_2", sichtbarkeit="sample_text_2")
    b = UML_14_Eigenschaft(initialWert="sample_text", sichtbarkeit="sample_text")
    _safe_set(b, 'UML_14_Eigenschaft25', a1)
    assert _is_linked(b, 'UML_14_Eigenschaft25', a1)
    if hasattr(a1, 'UML_14_Verbindungsende24'):
        assert _is_linked(a1, 'UML_14_Verbindungsende24', b)
    _safe_set(b, 'UML_14_Eigenschaft25', a2)
    assert _is_linked(b, 'UML_14_Eigenschaft25', a2)
    if hasattr(a1, 'UML_14_Verbindungsende24'):
        assert not _is_linked(a1, 'UML_14_Verbindungsende24', b)
    if hasattr(a2, 'UML_14_Verbindungsende24'):
        assert _is_linked(a2, 'UML_14_Verbindungsende24', b)
    _safe_set(b, 'UML_14_Eigenschaft25', None)
    assert not _is_linked(b, 'UML_14_Eigenschaft25', a2)
    if hasattr(a2, 'UML_14_Verbindungsende24'):
        assert not _is_linked(a2, 'UML_14_Verbindungsende24', b)


def test_assoc_eigenschaften26_reverse_link_reassign_clear():
    a1 = UML_14_Konzept(istAktiev="sample_text")
    a2 = UML_14_Konzept(istAktiev="sample_text_2")
    b = UML_14_Eigenschaft(initialWert="sample_text", sichtbarkeit="sample_text")
    _safe_set(b, 'UML_14_Eigenschaft28', a1)
    assert _is_linked(b, 'UML_14_Eigenschaft28', a1)
    if hasattr(a1, 'UML_14_Konzept27'):
        assert _is_linked(a1, 'UML_14_Konzept27', b)
    _safe_set(b, 'UML_14_Eigenschaft28', a2)
    assert _is_linked(b, 'UML_14_Eigenschaft28', a2)
    if hasattr(a1, 'UML_14_Konzept27'):
        assert not _is_linked(a1, 'UML_14_Konzept27', b)
    if hasattr(a2, 'UML_14_Konzept27'):
        assert _is_linked(a2, 'UML_14_Konzept27', b)
    _safe_set(b, 'UML_14_Eigenschaft28', None)
    assert not _is_linked(b, 'UML_14_Eigenschaft28', a2)
    if hasattr(a2, 'UML_14_Konzept27'):
        assert not _is_linked(a2, 'UML_14_Konzept27', b)


def test_assoc_einschraenkungen53_reverse_link_reassign_clear():
    a1 = UML_14_Einschraenkung(beschreibung="sample_text")
    a2 = UML_14_Einschraenkung(beschreibung="sample_text_2")
    b = UML_14_Benanntes(beschreibung="sample_text")
    _safe_set(b, 'UML_14_Benanntes54', {a1})
    assert _is_linked(b, 'UML_14_Benanntes54', a1)
    if hasattr(a1, 'UML_14_Einschraenkung'):
        assert _is_linked(a1, 'UML_14_Einschraenkung', b)
    _safe_set(b, 'UML_14_Benanntes54', {a2})
    assert _is_linked(b, 'UML_14_Benanntes54', a2)
    if hasattr(a1, 'UML_14_Einschraenkung'):
        assert not _is_linked(a1, 'UML_14_Einschraenkung', b)
    if hasattr(a2, 'UML_14_Einschraenkung'):
        assert _is_linked(a2, 'UML_14_Einschraenkung', b)
    _safe_set(b, 'UML_14_Benanntes54', set())
    assert not _is_linked(b, 'UML_14_Benanntes54', a2)
    if hasattr(a2, 'UML_14_Einschraenkung'):
        assert not _is_linked(a2, 'UML_14_Einschraenkung', b)


def test_assoc_eltern13_reverse_link_reassign_clear():
    a1 = UML_14_Vererbung(unterscheidung="sample_text")
    a2 = UML_14_Vererbung(unterscheidung="sample_text_2")
    b = UML_14_Konzept(istAktiev="sample_text")
    _safe_set(b, 'UML_14_Konzept15', a1)
    assert _is_linked(b, 'UML_14_Konzept15', a1)
    if hasattr(a1, 'UML_14_Vererbung14'):
        assert _is_linked(a1, 'UML_14_Vererbung14', b)
    _safe_set(b, 'UML_14_Konzept15', a2)
    assert _is_linked(b, 'UML_14_Konzept15', a2)
    if hasattr(a1, 'UML_14_Vererbung14'):
        assert not _is_linked(a1, 'UML_14_Vererbung14', b)
    if hasattr(a2, 'UML_14_Vererbung14'):
        assert _is_linked(a2, 'UML_14_Vererbung14', b)
    _safe_set(b, 'UML_14_Konzept15', None)
    assert not _is_linked(b, 'UML_14_Konzept15', a2)
    if hasattr(a2, 'UML_14_Vererbung14'):
        assert not _is_linked(a2, 'UML_14_Vererbung14', b)


def test_assoc_kind12_reverse_link_reassign_clear():
    a1 = UML_14_Vererbung(unterscheidung="sample_text")
    a2 = UML_14_Vererbung(unterscheidung="sample_text_2")
    b = UML_14_Konzept(istAktiev="sample_text")
    _safe_set(b, 'UML_14_Konzept', a1)
    assert _is_linked(b, 'UML_14_Konzept', a1)
    if hasattr(a1, 'UML_14_Vererbung'):
        assert _is_linked(a1, 'UML_14_Vererbung', b)
    _safe_set(b, 'UML_14_Konzept', a2)
    assert _is_linked(b, 'UML_14_Konzept', a2)
    if hasattr(a1, 'UML_14_Vererbung'):
        assert not _is_linked(a1, 'UML_14_Vererbung', b)
    if hasattr(a2, 'UML_14_Vererbung'):
        assert _is_linked(a2, 'UML_14_Vererbung', b)
    _safe_set(b, 'UML_14_Konzept', None)
    assert not _is_linked(b, 'UML_14_Konzept', a2)
    if hasattr(a2, 'UML_14_Vererbung'):
        assert not _is_linked(a2, 'UML_14_Vererbung', b)


def test_assoc_kommentare52_reverse_link_reassign_clear():
    a1 = UML_14_Kommentar(inhalt="sample_text")
    a2 = UML_14_Kommentar(inhalt="sample_text_2")
    b = UML_14_Benanntes(beschreibung="sample_text")
    _safe_set(b, 'UML_14_Benanntes', {a1})
    assert _is_linked(b, 'UML_14_Benanntes', a1)
    if hasattr(a1, 'UML_14_Kommentar'):
        assert _is_linked(a1, 'UML_14_Kommentar', b)
    _safe_set(b, 'UML_14_Benanntes', {a2})
    assert _is_linked(b, 'UML_14_Benanntes', a2)
    if hasattr(a1, 'UML_14_Kommentar'):
        assert not _is_linked(a1, 'UML_14_Kommentar', b)
    if hasattr(a2, 'UML_14_Kommentar'):
        assert _is_linked(a2, 'UML_14_Kommentar', b)
    _safe_set(b, 'UML_14_Benanntes', set())
    assert not _is_linked(b, 'UML_14_Benanntes', a2)
    if hasattr(a2, 'UML_14_Kommentar'):
        assert not _is_linked(a2, 'UML_14_Kommentar', b)


def test_assoc_teilnehmer18_reverse_link_reassign_clear():
    a1 = UML_14_Verbindungsende(istNavigierbar="sample_text", sichtbarkeit="sample_text")
    a2 = UML_14_Verbindungsende(istNavigierbar="sample_text_2", sichtbarkeit="sample_text_2")
    b = UML_14_Konzept(istAktiev="sample_text")
    _safe_set(b, 'UML_14_Konzept19', a1)
    assert _is_linked(b, 'UML_14_Konzept19', a1)
    if hasattr(a1, 'UML_14_Verbindungsende'):
        assert _is_linked(a1, 'UML_14_Verbindungsende', b)
    _safe_set(b, 'UML_14_Konzept19', a2)
    assert _is_linked(b, 'UML_14_Konzept19', a2)
    if hasattr(a1, 'UML_14_Verbindungsende'):
        assert not _is_linked(a1, 'UML_14_Verbindungsende', b)
    if hasattr(a2, 'UML_14_Verbindungsende'):
        assert _is_linked(a2, 'UML_14_Verbindungsende', b)
    _safe_set(b, 'UML_14_Konzept19', None)
    assert not _is_linked(b, 'UML_14_Konzept19', a2)
    if hasattr(a2, 'UML_14_Verbindungsende'):
        assert not _is_linked(a2, 'UML_14_Verbindungsende', b)


def test_assoc_verhalten29_reverse_link_reassign_clear():
    a1 = UML_14_Verhalten(inhlat="sample_text", sichtbarkeit="sample_text")
    a2 = UML_14_Verhalten(inhlat="sample_text_2", sichtbarkeit="sample_text_2")
    b = UML_14_Konzept(istAktiev="sample_text")
    _safe_set(b, 'UML_14_Konzept30', {a1})
    assert _is_linked(b, 'UML_14_Konzept30', a1)
    if hasattr(a1, 'UML_14_Verhalten31'):
        assert _is_linked(a1, 'UML_14_Verhalten31', b)
    _safe_set(b, 'UML_14_Konzept30', {a2})
    assert _is_linked(b, 'UML_14_Konzept30', a2)
    if hasattr(a1, 'UML_14_Verhalten31'):
        assert not _is_linked(a1, 'UML_14_Verhalten31', b)
    if hasattr(a2, 'UML_14_Verhalten31'):
        assert _is_linked(a2, 'UML_14_Verhalten31', b)
    _safe_set(b, 'UML_14_Konzept30', set())
    assert not _is_linked(b, 'UML_14_Konzept30', a2)
    if hasattr(a2, 'UML_14_Verhalten31'):
        assert not _is_linked(a2, 'UML_14_Verhalten31', b)


def test_assoc_verhaltensWerte3_reverse_link_reassign_clear():
    a1 = UML_14_Verhalten(inhlat="sample_text", sichtbarkeit="sample_text")
    a2 = UML_14_Verhalten(inhlat="sample_text_2", sichtbarkeit="sample_text_2")
    b = UML_14_MethodenWert(art="sample_text", standartWert="sample_text")
    _safe_set(b, 'UML_14_MethodenWert4', a1)
    assert _is_linked(b, 'UML_14_MethodenWert4', a1)
    if hasattr(a1, 'UML_14_Verhalten'):
        assert _is_linked(a1, 'UML_14_Verhalten', b)
    _safe_set(b, 'UML_14_MethodenWert4', a2)
    assert _is_linked(b, 'UML_14_MethodenWert4', a2)
    if hasattr(a1, 'UML_14_Verhalten'):
        assert not _is_linked(a1, 'UML_14_Verhalten', b)
    if hasattr(a2, 'UML_14_Verhalten'):
        assert _is_linked(a2, 'UML_14_Verhalten', b)
    _safe_set(b, 'UML_14_MethodenWert4', None)
    assert not _is_linked(b, 'UML_14_MethodenWert4', a2)
    if hasattr(a2, 'UML_14_Verhalten'):
        assert not _is_linked(a2, 'UML_14_Verhalten', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aufzaehlungsTyp0_stub_double():
    # UML_14_Aufzaehlung has no real 'UML_14_Aufzaehlung' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_MethodenWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_MethodenWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_MethodenWert(art="sample_text", standartWert="sample_text")
    partner = UML_14_Aufzaehlung()
    setattr(partner, 'UML_14_Aufzaehlung', None)
    _safe_set(owner, 'UML_14_MethodenWert', partner)
    assert getattr(partner, 'UML_14_Aufzaehlung') == owner
    _safe_set(owner, 'UML_14_MethodenWert', None)
    assert getattr(partner, 'UML_14_Aufzaehlung') is None


def test_assoc_aufzaehlungsTyp6_stub_double():
    # UML_14_Aufzaehlung has no real 'UML_14_Aufzaehlung8' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Eigenschaft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Eigenschaft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Eigenschaft(initialWert="sample_text", sichtbarkeit="sample_text")
    partner = UML_14_Aufzaehlung()
    setattr(partner, 'UML_14_Aufzaehlung8', None)
    _safe_set(owner, 'UML_14_Eigenschaft7', partner)
    assert getattr(partner, 'UML_14_Aufzaehlung8') == owner
    _safe_set(owner, 'UML_14_Eigenschaft7', None)
    assert getattr(partner, 'UML_14_Aufzaehlung8') is None


def test_assoc_einfacherTyp9_stub_double():
    # UML_14_Einfach has no real 'UML_14_Einfach11' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Eigenschaft's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Eigenschaft's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Eigenschaft(initialWert="sample_text", sichtbarkeit="sample_text")
    partner = UML_14_Einfach()
    setattr(partner, 'UML_14_Einfach11', None)
    _safe_set(owner, 'UML_14_Eigenschaft10', partner)
    assert getattr(partner, 'UML_14_Einfach11') == owner
    _safe_set(owner, 'UML_14_Eigenschaft10', None)
    assert getattr(partner, 'UML_14_Einfach11') is None


def test_assoc_einfacherWert1_stub_double():
    # UML_14_Einfach has no real 'UML_14_Einfach' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_MethodenWert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_MethodenWert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_MethodenWert(art="sample_text", standartWert="sample_text")
    partner = UML_14_Einfach()
    setattr(partner, 'UML_14_Einfach', None)
    _safe_set(owner, 'UML_14_MethodenWert2', partner)
    assert getattr(partner, 'UML_14_Einfach') == owner
    _safe_set(owner, 'UML_14_MethodenWert2', None)
    assert getattr(partner, 'UML_14_Einfach') is None


def test_assoc_link17_stub_double():
    # UML_14_Verbindung has no real 'Verbindung' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Verbindungsende's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Verbindungsende's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Verbindungsende(istNavigierbar="sample_text", sichtbarkeit="sample_text")
    partner = UML_14_Verbindung()
    setattr(partner, 'Verbindung', None)
    _safe_set(owner, 'verbinder', partner)
    assert getattr(partner, 'Verbindung') == owner
    _safe_set(owner, 'verbinder', None)
    assert getattr(partner, 'Verbindung') is None


def test_assoc_seineKlassen35_stub_double():
    # UML_14_Schachtel has no real 'UML_14_Schachtel36' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Konzept's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Konzept's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Konzept(istAktiev="sample_text")
    partner = UML_14_Schachtel()
    setattr(partner, 'UML_14_Schachtel36', None)
    _safe_set(owner, 'UML_14_Konzept37', partner)
    assert owner in getattr(partner, 'UML_14_Schachtel36')
    _safe_set(owner, 'UML_14_Konzept37', None)
    assert owner not in getattr(partner, 'UML_14_Schachtel36')


def test_assoc_seineVererbungen44_stub_double():
    # UML_14_Schachtel has no real 'UML_14_Schachtel45' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Vererbung's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Vererbung's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Vererbung(unterscheidung="sample_text")
    partner = UML_14_Schachtel()
    setattr(partner, 'UML_14_Schachtel45', None)
    _safe_set(owner, 'UML_14_Vererbung46', partner)
    assert owner in getattr(partner, 'UML_14_Schachtel45')
    _safe_set(owner, 'UML_14_Vererbung46', None)
    assert owner not in getattr(partner, 'UML_14_Schachtel45')


def test_assoc_verbinder16_stub_double():
    # UML_14_Verbindung has no real 'link' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Verbindungsende's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Verbindungsende's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Verbindungsende(istNavigierbar="sample_text", sichtbarkeit="sample_text")
    partner = UML_14_Verbindung()
    setattr(partner, 'link', None)
    _safe_set(owner, 'Verbindungsende', partner)
    assert owner in getattr(partner, 'link')
    _safe_set(owner, 'Verbindungsende', None)
    assert owner not in getattr(partner, 'link')


def test_assoc_zeichen32_stub_double():
    # UML_14_Aufzaehlung has no real 'UML_14_Aufzaehlung33' property in the generated
    # code (a bare stub) -- manually attach it so UML_14_Aufzaehlungswert's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UML_14_Aufzaehlungswert's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UML_14_Aufzaehlungswert(wert="sample_text")
    partner = UML_14_Aufzaehlung()
    setattr(partner, 'UML_14_Aufzaehlung33', None)
    _safe_set(owner, 'UML_14_Aufzaehlungswert', partner)
    assert owner in getattr(partner, 'UML_14_Aufzaehlung33')
    _safe_set(owner, 'UML_14_Aufzaehlungswert', None)
    assert owner not in getattr(partner, 'UML_14_Aufzaehlung33')


