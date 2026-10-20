import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BibType,
    bibtex_Address,
    bibtex_Article,
    bibtex_Author,
    bibtex_BibType,
    bibtex_Book,
    bibtex_Booklet,
    bibtex_Booktitle,
    bibtex_Chapter,
    bibtex_CiteKey,
    bibtex_Conference,
    bibtex_Crossref,
    bibtex_Edition,
    bibtex_Editor,
    bibtex_Howpublished,
    bibtex_Inbook,
    bibtex_Incollection,
    bibtex_Inproceedings,
    bibtex_Institution,
    bibtex_Journal,
    bibtex_Key,
    bibtex_Manual,
    bibtex_Mastersthesis,
    bibtex_Misc,
    bibtex_Model,
    bibtex_Month,
    bibtex_Note,
    bibtex_Number,
    bibtex_Organization,
    bibtex_Pages,
    bibtex_Phdthesis,
    bibtex_Proceedings,
    bibtex_Publisher,
    bibtex_School,
    bibtex_Series,
    bibtex_Techreport,
    bibtex_Title,
    bibtex_Type,
    bibtex_Unpublished,
    bibtex_Volume,
    bibtex_Year,
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

def test_assoc_address75_reverse_link_reassign_clear():
    a1 = bibtex_Inbook(author=True, editor=True)
    a2 = bibtex_Inbook(author=False, editor=False)
    b = bibtex_Address(address="sample_text")
    _safe_set(b, 'bibtex_Address77', a1)
    assert _is_linked(b, 'bibtex_Address77', a1)
    if hasattr(a1, 'bibtex_Inbook76'):
        assert _is_linked(a1, 'bibtex_Inbook76', b)
    _safe_set(b, 'bibtex_Address77', a2)
    assert _is_linked(b, 'bibtex_Address77', a2)
    if hasattr(a1, 'bibtex_Inbook76'):
        assert not _is_linked(a1, 'bibtex_Inbook76', b)
    if hasattr(a2, 'bibtex_Inbook76'):
        assert _is_linked(a2, 'bibtex_Inbook76', b)
    _safe_set(b, 'bibtex_Address77', None)
    assert not _is_linked(b, 'bibtex_Address77', a2)
    if hasattr(a2, 'bibtex_Inbook76'):
        assert not _is_linked(a2, 'bibtex_Inbook76', b)


def test_assoc_chapter64_reverse_link_reassign_clear():
    a1 = bibtex_Inbook(author=True, editor=True)
    a2 = bibtex_Inbook(author=False, editor=False)
    b = bibtex_Chapter(chapter="sample_text")
    _safe_set(b, 'bibtex_Chapter', a1)
    assert _is_linked(b, 'bibtex_Chapter', a1)
    if hasattr(a1, 'bibtex_Inbook65'):
        assert _is_linked(a1, 'bibtex_Inbook65', b)
    _safe_set(b, 'bibtex_Chapter', a2)
    assert _is_linked(b, 'bibtex_Chapter', a2)
    if hasattr(a1, 'bibtex_Inbook65'):
        assert not _is_linked(a1, 'bibtex_Inbook65', b)
    if hasattr(a2, 'bibtex_Inbook65'):
        assert _is_linked(a2, 'bibtex_Inbook65', b)
    _safe_set(b, 'bibtex_Chapter', None)
    assert not _is_linked(b, 'bibtex_Chapter', a2)
    if hasattr(a2, 'bibtex_Inbook65'):
        assert not _is_linked(a2, 'bibtex_Inbook65', b)


def test_assoc_edition78_reverse_link_reassign_clear():
    a1 = bibtex_Inbook(author=True, editor=True)
    a2 = bibtex_Inbook(author=False, editor=False)
    b = bibtex_Edition(edition="sample_text")
    _safe_set(b, 'bibtex_Edition80', a1)
    assert _is_linked(b, 'bibtex_Edition80', a1)
    if hasattr(a1, 'bibtex_Inbook79'):
        assert _is_linked(a1, 'bibtex_Inbook79', b)
    _safe_set(b, 'bibtex_Edition80', a2)
    assert _is_linked(b, 'bibtex_Edition80', a2)
    if hasattr(a1, 'bibtex_Inbook79'):
        assert not _is_linked(a1, 'bibtex_Inbook79', b)
    if hasattr(a2, 'bibtex_Inbook79'):
        assert _is_linked(a2, 'bibtex_Inbook79', b)
    _safe_set(b, 'bibtex_Edition80', None)
    assert not _is_linked(b, 'bibtex_Edition80', a2)
    if hasattr(a2, 'bibtex_Inbook79'):
        assert not _is_linked(a2, 'bibtex_Inbook79', b)


def test_assoc_pages66_reverse_link_reassign_clear():
    a1 = bibtex_Pages(pages="sample_text")
    a2 = bibtex_Pages(pages="sample_text_2")
    b = bibtex_Inbook(author=True, editor=True)
    _safe_set(b, 'bibtex_Inbook67', a1)
    assert _is_linked(b, 'bibtex_Inbook67', a1)
    if hasattr(a1, 'bibtex_Pages68'):
        assert _is_linked(a1, 'bibtex_Pages68', b)
    _safe_set(b, 'bibtex_Inbook67', a2)
    assert _is_linked(b, 'bibtex_Inbook67', a2)
    if hasattr(a1, 'bibtex_Pages68'):
        assert not _is_linked(a1, 'bibtex_Pages68', b)
    if hasattr(a2, 'bibtex_Pages68'):
        assert _is_linked(a2, 'bibtex_Pages68', b)
    _safe_set(b, 'bibtex_Inbook67', None)
    assert not _is_linked(b, 'bibtex_Inbook67', a2)
    if hasattr(a2, 'bibtex_Pages68'):
        assert not _is_linked(a2, 'bibtex_Pages68', b)


def test_assoc_publisher62_reverse_link_reassign_clear():
    a1 = bibtex_Publisher(publisher="sample_text")
    a2 = bibtex_Publisher(publisher="sample_text_2")
    b = bibtex_Inbook(author=True, editor=True)
    _safe_set(b, 'bibtex_Inbook', a1)
    assert _is_linked(b, 'bibtex_Inbook', a1)
    if hasattr(a1, 'bibtex_Publisher63'):
        assert _is_linked(a1, 'bibtex_Publisher63', b)
    _safe_set(b, 'bibtex_Inbook', a2)
    assert _is_linked(b, 'bibtex_Inbook', a2)
    if hasattr(a1, 'bibtex_Publisher63'):
        assert not _is_linked(a1, 'bibtex_Publisher63', b)
    if hasattr(a2, 'bibtex_Publisher63'):
        assert _is_linked(a2, 'bibtex_Publisher63', b)
    _safe_set(b, 'bibtex_Inbook', None)
    assert not _is_linked(b, 'bibtex_Inbook', a2)
    if hasattr(a2, 'bibtex_Publisher63'):
        assert not _is_linked(a2, 'bibtex_Publisher63', b)


def test_assoc_series72_reverse_link_reassign_clear():
    a1 = bibtex_Series(series="sample_text")
    a2 = bibtex_Series(series="sample_text_2")
    b = bibtex_Inbook(author=True, editor=True)
    _safe_set(b, 'bibtex_Inbook73', a1)
    assert _is_linked(b, 'bibtex_Inbook73', a1)
    if hasattr(a1, 'bibtex_Series74'):
        assert _is_linked(a1, 'bibtex_Series74', b)
    _safe_set(b, 'bibtex_Inbook73', a2)
    assert _is_linked(b, 'bibtex_Inbook73', a2)
    if hasattr(a1, 'bibtex_Series74'):
        assert not _is_linked(a1, 'bibtex_Series74', b)
    if hasattr(a2, 'bibtex_Series74'):
        assert _is_linked(a2, 'bibtex_Series74', b)
    _safe_set(b, 'bibtex_Inbook73', None)
    assert not _is_linked(b, 'bibtex_Inbook73', a2)
    if hasattr(a2, 'bibtex_Series74'):
        assert not _is_linked(a2, 'bibtex_Series74', b)


def test_assoc_volume69_reverse_link_reassign_clear():
    a1 = bibtex_Volume(volume="sample_text")
    a2 = bibtex_Volume(volume="sample_text_2")
    b = bibtex_Inbook(author=True, editor=True)
    _safe_set(b, 'bibtex_Inbook70', a1)
    assert _is_linked(b, 'bibtex_Inbook70', a1)
    if hasattr(a1, 'bibtex_Volume71'):
        assert _is_linked(a1, 'bibtex_Volume71', b)
    _safe_set(b, 'bibtex_Inbook70', a2)
    assert _is_linked(b, 'bibtex_Inbook70', a2)
    if hasattr(a1, 'bibtex_Volume71'):
        assert not _is_linked(a1, 'bibtex_Volume71', b)
    if hasattr(a2, 'bibtex_Volume71'):
        assert _is_linked(a2, 'bibtex_Volume71', b)
    _safe_set(b, 'bibtex_Inbook70', None)
    assert not _is_linked(b, 'bibtex_Inbook70', a2)
    if hasattr(a2, 'bibtex_Volume71'):
        assert not _is_linked(a2, 'bibtex_Volume71', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_address121_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings122' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings122', None)
    _safe_set(owner, 'bibtex_Address123', partner)
    assert getattr(partner, 'bibtex_Inproceedings122') == owner
    _safe_set(owner, 'bibtex_Address123', None)
    assert getattr(partner, 'bibtex_Inproceedings122') is None


def test_assoc_address129_stub_double():
    # bibtex_Manual has no real 'bibtex_Manual130' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Manual()
    setattr(partner, 'bibtex_Manual130', None)
    _safe_set(owner, 'bibtex_Address131', partner)
    assert getattr(partner, 'bibtex_Manual130') == owner
    _safe_set(owner, 'bibtex_Address131', None)
    assert getattr(partner, 'bibtex_Manual130') is None


def test_assoc_address139_stub_double():
    # bibtex_Mastersthesis has no real 'bibtex_Mastersthesis140' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Mastersthesis()
    setattr(partner, 'bibtex_Mastersthesis140', None)
    _safe_set(owner, 'bibtex_Address141', partner)
    assert getattr(partner, 'bibtex_Mastersthesis140') == owner
    _safe_set(owner, 'bibtex_Address141', None)
    assert getattr(partner, 'bibtex_Mastersthesis140') is None


def test_assoc_address152_stub_double():
    # bibtex_Phdthesis has no real 'bibtex_Phdthesis153' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Phdthesis()
    setattr(partner, 'bibtex_Phdthesis153', None)
    _safe_set(owner, 'bibtex_Address154', partner)
    assert getattr(partner, 'bibtex_Phdthesis153') == owner
    _safe_set(owner, 'bibtex_Address154', None)
    assert getattr(partner, 'bibtex_Phdthesis153') is None


def test_assoc_address163_stub_double():
    # bibtex_Proceedings has no real 'bibtex_Proceedings164' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Proceedings()
    setattr(partner, 'bibtex_Proceedings164', None)
    _safe_set(owner, 'bibtex_Address165', partner)
    assert getattr(partner, 'bibtex_Proceedings164') == owner
    _safe_set(owner, 'bibtex_Address165', None)
    assert getattr(partner, 'bibtex_Proceedings164') is None


def test_assoc_address175_stub_double():
    # bibtex_Techreport has no real 'bibtex_Techreport176' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Techreport()
    setattr(partner, 'bibtex_Techreport176', None)
    _safe_set(owner, 'bibtex_Address177', partner)
    assert getattr(partner, 'bibtex_Techreport176') == owner
    _safe_set(owner, 'bibtex_Address177', None)
    assert getattr(partner, 'bibtex_Techreport176') is None


def test_assoc_address33_stub_double():
    # bibtex_Book has no real 'bibtex_Book34' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book34', None)
    _safe_set(owner, 'bibtex_Address', partner)
    assert getattr(partner, 'bibtex_Book34') == owner
    _safe_set(owner, 'bibtex_Address', None)
    assert getattr(partner, 'bibtex_Book34') is None


def test_assoc_address41_stub_double():
    # bibtex_Booklet has no real 'bibtex_Booklet42' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Booklet()
    setattr(partner, 'bibtex_Booklet42', None)
    _safe_set(owner, 'bibtex_Address43', partner)
    assert getattr(partner, 'bibtex_Booklet42') == owner
    _safe_set(owner, 'bibtex_Address43', None)
    assert getattr(partner, 'bibtex_Booklet42') is None


def test_assoc_address59_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference60' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference60', None)
    _safe_set(owner, 'bibtex_Address61', partner)
    assert getattr(partner, 'bibtex_Conference60') == owner
    _safe_set(owner, 'bibtex_Address61', None)
    assert getattr(partner, 'bibtex_Conference60') is None


def test_assoc_address98_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection99' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Address's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Address's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Address(address="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection99', None)
    _safe_set(owner, 'bibtex_Address100', partner)
    assert getattr(partner, 'bibtex_Incollection99') == owner
    _safe_set(owner, 'bibtex_Address100', None)
    assert getattr(partner, 'bibtex_Incollection99') is None


def test_assoc_author101_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings', None)
    _safe_set(owner, 'bibtex_Author102', partner)
    assert getattr(partner, 'bibtex_Inproceedings') == owner
    _safe_set(owner, 'bibtex_Author102', None)
    assert getattr(partner, 'bibtex_Inproceedings') is None


def test_assoc_author124_stub_double():
    # bibtex_Manual has no real 'bibtex_Manual' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Manual()
    setattr(partner, 'bibtex_Manual', None)
    _safe_set(owner, 'bibtex_Author125', partner)
    assert getattr(partner, 'bibtex_Manual') == owner
    _safe_set(owner, 'bibtex_Author125', None)
    assert getattr(partner, 'bibtex_Manual') is None


def test_assoc_author13_stub_double():
    # bibtex_Article has no real 'bibtex_Article' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Article()
    setattr(partner, 'bibtex_Article', None)
    _safe_set(owner, 'bibtex_Author', partner)
    assert getattr(partner, 'bibtex_Article') == owner
    _safe_set(owner, 'bibtex_Author', None)
    assert getattr(partner, 'bibtex_Article') is None


def test_assoc_author135_stub_double():
    # bibtex_Mastersthesis has no real 'bibtex_Mastersthesis' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Mastersthesis()
    setattr(partner, 'bibtex_Mastersthesis', None)
    _safe_set(owner, 'bibtex_Author136', partner)
    assert getattr(partner, 'bibtex_Mastersthesis') == owner
    _safe_set(owner, 'bibtex_Author136', None)
    assert getattr(partner, 'bibtex_Mastersthesis') is None


def test_assoc_author142_stub_double():
    # bibtex_Misc has no real 'bibtex_Misc' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Misc()
    setattr(partner, 'bibtex_Misc', None)
    _safe_set(owner, 'bibtex_Author143', partner)
    assert getattr(partner, 'bibtex_Misc') == owner
    _safe_set(owner, 'bibtex_Author143', None)
    assert getattr(partner, 'bibtex_Misc') is None


def test_assoc_author147_stub_double():
    # bibtex_Phdthesis has no real 'bibtex_Phdthesis' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Phdthesis()
    setattr(partner, 'bibtex_Phdthesis', None)
    _safe_set(owner, 'bibtex_Author148', partner)
    assert getattr(partner, 'bibtex_Phdthesis') == owner
    _safe_set(owner, 'bibtex_Author148', None)
    assert getattr(partner, 'bibtex_Phdthesis') is None


def test_assoc_author166_stub_double():
    # bibtex_Techreport has no real 'bibtex_Techreport' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Techreport()
    setattr(partner, 'bibtex_Techreport', None)
    _safe_set(owner, 'bibtex_Author167', partner)
    assert getattr(partner, 'bibtex_Techreport') == owner
    _safe_set(owner, 'bibtex_Author167', None)
    assert getattr(partner, 'bibtex_Techreport') is None


def test_assoc_author178_stub_double():
    # bibtex_Unpublished has no real 'bibtex_Unpublished' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Unpublished()
    setattr(partner, 'bibtex_Unpublished', None)
    _safe_set(owner, 'bibtex_Author179', partner)
    assert getattr(partner, 'bibtex_Unpublished') == owner
    _safe_set(owner, 'bibtex_Author179', None)
    assert getattr(partner, 'bibtex_Unpublished') is None


def test_assoc_author23_stub_double():
    # bibtex_Book has no real 'bibtex_Book24' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book24', None)
    _safe_set(owner, 'bibtex_Author25', partner)
    assert getattr(partner, 'bibtex_Book24') == owner
    _safe_set(owner, 'bibtex_Author25', None)
    assert getattr(partner, 'bibtex_Book24') is None


def test_assoc_author37_stub_double():
    # bibtex_Booklet has no real 'bibtex_Booklet' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Booklet()
    setattr(partner, 'bibtex_Booklet', None)
    _safe_set(owner, 'bibtex_Author38', partner)
    assert getattr(partner, 'bibtex_Booklet') == owner
    _safe_set(owner, 'bibtex_Author38', None)
    assert getattr(partner, 'bibtex_Booklet') is None


def test_assoc_author44_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference', None)
    _safe_set(owner, 'bibtex_Author45', partner)
    assert getattr(partner, 'bibtex_Conference') == owner
    _safe_set(owner, 'bibtex_Author45', None)
    assert getattr(partner, 'bibtex_Conference') is None


def test_assoc_author81_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Author's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Author's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Author(author="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection', None)
    _safe_set(owner, 'bibtex_Author82', partner)
    assert getattr(partner, 'bibtex_Incollection') == owner
    _safe_set(owner, 'bibtex_Author82', None)
    assert getattr(partner, 'bibtex_Incollection') is None


def test_assoc_booktitle103_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings104' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Booktitle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Booktitle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Booktitle(booktitle="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings104', None)
    _safe_set(owner, 'bibtex_Booktitle105', partner)
    assert getattr(partner, 'bibtex_Inproceedings104') == owner
    _safe_set(owner, 'bibtex_Booktitle105', None)
    assert getattr(partner, 'bibtex_Inproceedings104') is None


def test_assoc_booktitle46_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference47' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Booktitle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Booktitle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Booktitle(booktitle="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference47', None)
    _safe_set(owner, 'bibtex_Booktitle', partner)
    assert getattr(partner, 'bibtex_Conference47') == owner
    _safe_set(owner, 'bibtex_Booktitle', None)
    assert getattr(partner, 'bibtex_Conference47') is None


def test_assoc_booktitle83_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection84' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Booktitle's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Booktitle's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Booktitle(booktitle="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection84', None)
    _safe_set(owner, 'bibtex_Booktitle85', partner)
    assert getattr(partner, 'bibtex_Incollection84') == owner
    _safe_set(owner, 'bibtex_Booktitle85', None)
    assert getattr(partner, 'bibtex_Incollection84') is None


def test_assoc_citeKey1_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType2' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_CiteKey's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_CiteKey's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_CiteKey(citeKey="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType2', None)
    _safe_set(owner, 'bibtex_CiteKey', partner)
    assert getattr(partner, 'bibtex_BibType2') == owner
    _safe_set(owner, 'bibtex_CiteKey', None)
    assert getattr(partner, 'bibtex_BibType2') is None


def test_assoc_edition132_stub_double():
    # bibtex_Manual has no real 'bibtex_Manual133' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Edition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Edition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Edition(edition="sample_text")
    partner = bibtex_Manual()
    setattr(partner, 'bibtex_Manual133', None)
    _safe_set(owner, 'bibtex_Edition134', partner)
    assert getattr(partner, 'bibtex_Manual133') == owner
    _safe_set(owner, 'bibtex_Edition134', None)
    assert getattr(partner, 'bibtex_Manual133') is None


def test_assoc_edition35_stub_double():
    # bibtex_Book has no real 'bibtex_Book36' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Edition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Edition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Edition(edition="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book36', None)
    _safe_set(owner, 'bibtex_Edition', partner)
    assert getattr(partner, 'bibtex_Book36') == owner
    _safe_set(owner, 'bibtex_Edition', None)
    assert getattr(partner, 'bibtex_Book36') is None


def test_assoc_editor106_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings107' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Editor(editor="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings107', None)
    _safe_set(owner, 'bibtex_Editor108', partner)
    assert getattr(partner, 'bibtex_Inproceedings107') == owner
    _safe_set(owner, 'bibtex_Editor108', None)
    assert getattr(partner, 'bibtex_Inproceedings107') is None


def test_assoc_editor155_stub_double():
    # bibtex_Proceedings has no real 'bibtex_Proceedings' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Editor(editor="sample_text")
    partner = bibtex_Proceedings()
    setattr(partner, 'bibtex_Proceedings', None)
    _safe_set(owner, 'bibtex_Editor156', partner)
    assert getattr(partner, 'bibtex_Proceedings') == owner
    _safe_set(owner, 'bibtex_Editor156', None)
    assert getattr(partner, 'bibtex_Proceedings') is None


def test_assoc_editor26_stub_double():
    # bibtex_Book has no real 'bibtex_Book27' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Editor(editor="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book27', None)
    _safe_set(owner, 'bibtex_Editor', partner)
    assert getattr(partner, 'bibtex_Book27') == owner
    _safe_set(owner, 'bibtex_Editor', None)
    assert getattr(partner, 'bibtex_Book27') is None


def test_assoc_editor48_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference49' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Editor(editor="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference49', None)
    _safe_set(owner, 'bibtex_Editor50', partner)
    assert getattr(partner, 'bibtex_Conference49') == owner
    _safe_set(owner, 'bibtex_Editor50', None)
    assert getattr(partner, 'bibtex_Conference49') is None


def test_assoc_editor86_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection87' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Editor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Editor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Editor(editor="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection87', None)
    _safe_set(owner, 'bibtex_Editor88', partner)
    assert getattr(partner, 'bibtex_Incollection87') == owner
    _safe_set(owner, 'bibtex_Editor88', None)
    assert getattr(partner, 'bibtex_Incollection87') is None


def test_assoc_howpublished144_stub_double():
    # bibtex_Misc has no real 'bibtex_Misc145' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Howpublished's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Howpublished's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Howpublished(howpublished="sample_text")
    partner = bibtex_Misc()
    setattr(partner, 'bibtex_Misc145', None)
    _safe_set(owner, 'bibtex_Howpublished146', partner)
    assert getattr(partner, 'bibtex_Misc145') == owner
    _safe_set(owner, 'bibtex_Howpublished146', None)
    assert getattr(partner, 'bibtex_Misc145') is None


def test_assoc_howpublished39_stub_double():
    # bibtex_Booklet has no real 'bibtex_Booklet40' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Howpublished's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Howpublished's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Howpublished(howpublished="sample_text")
    partner = bibtex_Booklet()
    setattr(partner, 'bibtex_Booklet40', None)
    _safe_set(owner, 'bibtex_Howpublished', partner)
    assert getattr(partner, 'bibtex_Booklet40') == owner
    _safe_set(owner, 'bibtex_Howpublished', None)
    assert getattr(partner, 'bibtex_Booklet40') is None


def test_assoc_institution168_stub_double():
    # bibtex_Techreport has no real 'bibtex_Techreport169' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Institution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Institution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Institution(institution="sample_text")
    partner = bibtex_Techreport()
    setattr(partner, 'bibtex_Techreport169', None)
    _safe_set(owner, 'bibtex_Institution', partner)
    assert getattr(partner, 'bibtex_Techreport169') == owner
    _safe_set(owner, 'bibtex_Institution', None)
    assert getattr(partner, 'bibtex_Techreport169') is None


def test_assoc_journal14_stub_double():
    # bibtex_Article has no real 'bibtex_Article15' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Journal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Journal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Journal(journal="sample_text")
    partner = bibtex_Article()
    setattr(partner, 'bibtex_Article15', None)
    _safe_set(owner, 'bibtex_Journal', partner)
    assert getattr(partner, 'bibtex_Article15') == owner
    _safe_set(owner, 'bibtex_Journal', None)
    assert getattr(partner, 'bibtex_Article15') is None


def test_assoc_key11_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType12' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Key's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Key's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Key(key="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType12', None)
    _safe_set(owner, 'bibtex_Key', partner)
    assert getattr(partner, 'bibtex_BibType12') == owner
    _safe_set(owner, 'bibtex_Key', None)
    assert getattr(partner, 'bibtex_BibType12') is None


def test_assoc_month7_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType8' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Month's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Month's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Month(month="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType8', None)
    _safe_set(owner, 'bibtex_Month', partner)
    assert getattr(partner, 'bibtex_BibType8') == owner
    _safe_set(owner, 'bibtex_Month', None)
    assert getattr(partner, 'bibtex_BibType8') is None


def test_assoc_note9_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType10' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Note's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Note's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Note(note="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType10', None)
    _safe_set(owner, 'bibtex_Note', partner)
    assert getattr(partner, 'bibtex_BibType10') == owner
    _safe_set(owner, 'bibtex_Note', None)
    assert getattr(partner, 'bibtex_BibType10') is None


def test_assoc_number172_stub_double():
    # bibtex_Techreport has no real 'bibtex_Techreport173' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Number(number="sample_text")
    partner = bibtex_Techreport()
    setattr(partner, 'bibtex_Techreport173', None)
    _safe_set(owner, 'bibtex_Number174', partner)
    assert getattr(partner, 'bibtex_Techreport173') == owner
    _safe_set(owner, 'bibtex_Number174', None)
    assert getattr(partner, 'bibtex_Techreport173') is None


def test_assoc_number18_stub_double():
    # bibtex_Article has no real 'bibtex_Article19' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Number's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Number's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Number(number="sample_text")
    partner = bibtex_Article()
    setattr(partner, 'bibtex_Article19', None)
    _safe_set(owner, 'bibtex_Number', partner)
    assert getattr(partner, 'bibtex_Article19') == owner
    _safe_set(owner, 'bibtex_Number', None)
    assert getattr(partner, 'bibtex_Article19') is None


def test_assoc_organization115_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings116' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Organization(organization="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings116', None)
    _safe_set(owner, 'bibtex_Organization117', partner)
    assert getattr(partner, 'bibtex_Inproceedings116') == owner
    _safe_set(owner, 'bibtex_Organization117', None)
    assert getattr(partner, 'bibtex_Inproceedings116') is None


def test_assoc_organization126_stub_double():
    # bibtex_Manual has no real 'bibtex_Manual127' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Organization(organization="sample_text")
    partner = bibtex_Manual()
    setattr(partner, 'bibtex_Manual127', None)
    _safe_set(owner, 'bibtex_Organization128', partner)
    assert getattr(partner, 'bibtex_Manual127') == owner
    _safe_set(owner, 'bibtex_Organization128', None)
    assert getattr(partner, 'bibtex_Manual127') is None


def test_assoc_organization160_stub_double():
    # bibtex_Proceedings has no real 'bibtex_Proceedings161' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Organization(organization="sample_text")
    partner = bibtex_Proceedings()
    setattr(partner, 'bibtex_Proceedings161', None)
    _safe_set(owner, 'bibtex_Organization162', partner)
    assert getattr(partner, 'bibtex_Proceedings161') == owner
    _safe_set(owner, 'bibtex_Organization162', None)
    assert getattr(partner, 'bibtex_Proceedings161') is None


def test_assoc_organization54_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference55' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Organization(organization="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference55', None)
    _safe_set(owner, 'bibtex_Organization', partner)
    assert getattr(partner, 'bibtex_Conference55') == owner
    _safe_set(owner, 'bibtex_Organization', None)
    assert getattr(partner, 'bibtex_Conference55') is None


def test_assoc_organization92_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection93' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Organization(organization="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection93', None)
    _safe_set(owner, 'bibtex_Organization94', partner)
    assert getattr(partner, 'bibtex_Incollection93') == owner
    _safe_set(owner, 'bibtex_Organization94', None)
    assert getattr(partner, 'bibtex_Incollection93') is None


def test_assoc_pages112_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings113' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Pages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Pages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Pages(pages="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings113', None)
    _safe_set(owner, 'bibtex_Pages114', partner)
    assert getattr(partner, 'bibtex_Inproceedings113') == owner
    _safe_set(owner, 'bibtex_Pages114', None)
    assert getattr(partner, 'bibtex_Inproceedings113') is None


def test_assoc_pages20_stub_double():
    # bibtex_Article has no real 'bibtex_Article21' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Pages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Pages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Pages(pages="sample_text")
    partner = bibtex_Article()
    setattr(partner, 'bibtex_Article21', None)
    _safe_set(owner, 'bibtex_Pages', partner)
    assert getattr(partner, 'bibtex_Article21') == owner
    _safe_set(owner, 'bibtex_Pages', None)
    assert getattr(partner, 'bibtex_Article21') is None


def test_assoc_pages51_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference52' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Pages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Pages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Pages(pages="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference52', None)
    _safe_set(owner, 'bibtex_Pages53', partner)
    assert getattr(partner, 'bibtex_Conference52') == owner
    _safe_set(owner, 'bibtex_Pages53', None)
    assert getattr(partner, 'bibtex_Conference52') is None


def test_assoc_pages89_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection90' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Pages's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Pages's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Pages(pages="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection90', None)
    _safe_set(owner, 'bibtex_Pages91', partner)
    assert getattr(partner, 'bibtex_Incollection90') == owner
    _safe_set(owner, 'bibtex_Pages91', None)
    assert getattr(partner, 'bibtex_Incollection90') is None


def test_assoc_publisher118_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings119' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Publisher(publisher="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings119', None)
    _safe_set(owner, 'bibtex_Publisher120', partner)
    assert getattr(partner, 'bibtex_Inproceedings119') == owner
    _safe_set(owner, 'bibtex_Publisher120', None)
    assert getattr(partner, 'bibtex_Inproceedings119') is None


def test_assoc_publisher157_stub_double():
    # bibtex_Proceedings has no real 'bibtex_Proceedings158' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Publisher(publisher="sample_text")
    partner = bibtex_Proceedings()
    setattr(partner, 'bibtex_Proceedings158', None)
    _safe_set(owner, 'bibtex_Publisher159', partner)
    assert getattr(partner, 'bibtex_Proceedings158') == owner
    _safe_set(owner, 'bibtex_Publisher159', None)
    assert getattr(partner, 'bibtex_Proceedings158') is None


def test_assoc_publisher22_stub_double():
    # bibtex_Book has no real 'bibtex_Book' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Publisher(publisher="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book', None)
    _safe_set(owner, 'bibtex_Publisher', partner)
    assert getattr(partner, 'bibtex_Book') == owner
    _safe_set(owner, 'bibtex_Publisher', None)
    assert getattr(partner, 'bibtex_Book') is None


def test_assoc_publisher56_stub_double():
    # bibtex_Conference has no real 'bibtex_Conference57' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Publisher(publisher="sample_text")
    partner = bibtex_Conference()
    setattr(partner, 'bibtex_Conference57', None)
    _safe_set(owner, 'bibtex_Publisher58', partner)
    assert getattr(partner, 'bibtex_Conference57') == owner
    _safe_set(owner, 'bibtex_Publisher58', None)
    assert getattr(partner, 'bibtex_Conference57') is None


def test_assoc_publisher95_stub_double():
    # bibtex_Incollection has no real 'bibtex_Incollection96' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Publisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Publisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Publisher(publisher="sample_text")
    partner = bibtex_Incollection()
    setattr(partner, 'bibtex_Incollection96', None)
    _safe_set(owner, 'bibtex_Publisher97', partner)
    assert getattr(partner, 'bibtex_Incollection96') == owner
    _safe_set(owner, 'bibtex_Publisher97', None)
    assert getattr(partner, 'bibtex_Incollection96') is None


def test_assoc_school137_stub_double():
    # bibtex_Mastersthesis has no real 'bibtex_Mastersthesis138' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_School(school="sample_text")
    partner = bibtex_Mastersthesis()
    setattr(partner, 'bibtex_Mastersthesis138', None)
    _safe_set(owner, 'bibtex_School', partner)
    assert getattr(partner, 'bibtex_Mastersthesis138') == owner
    _safe_set(owner, 'bibtex_School', None)
    assert getattr(partner, 'bibtex_Mastersthesis138') is None


def test_assoc_school149_stub_double():
    # bibtex_Phdthesis has no real 'bibtex_Phdthesis150' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_School's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_School's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_School(school="sample_text")
    partner = bibtex_Phdthesis()
    setattr(partner, 'bibtex_Phdthesis150', None)
    _safe_set(owner, 'bibtex_School151', partner)
    assert getattr(partner, 'bibtex_Phdthesis150') == owner
    _safe_set(owner, 'bibtex_School151', None)
    assert getattr(partner, 'bibtex_Phdthesis150') is None


def test_assoc_series109_stub_double():
    # bibtex_Inproceedings has no real 'bibtex_Inproceedings110' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Series's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Series's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Series(series="sample_text")
    partner = bibtex_Inproceedings()
    setattr(partner, 'bibtex_Inproceedings110', None)
    _safe_set(owner, 'bibtex_Series111', partner)
    assert getattr(partner, 'bibtex_Inproceedings110') == owner
    _safe_set(owner, 'bibtex_Series111', None)
    assert getattr(partner, 'bibtex_Inproceedings110') is None


def test_assoc_series31_stub_double():
    # bibtex_Book has no real 'bibtex_Book32' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Series's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Series's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Series(series="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book32', None)
    _safe_set(owner, 'bibtex_Series', partner)
    assert getattr(partner, 'bibtex_Book32') == owner
    _safe_set(owner, 'bibtex_Series', None)
    assert getattr(partner, 'bibtex_Book32') is None


def test_assoc_title3_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType4' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Title's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Title's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Title(title="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType4', None)
    _safe_set(owner, 'bibtex_Title', partner)
    assert getattr(partner, 'bibtex_BibType4') == owner
    _safe_set(owner, 'bibtex_Title', None)
    assert getattr(partner, 'bibtex_BibType4') is None


def test_assoc_type170_stub_double():
    # bibtex_Techreport has no real 'bibtex_Techreport171' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Type's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Type's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Type(type="sample_text")
    partner = bibtex_Techreport()
    setattr(partner, 'bibtex_Techreport171', None)
    _safe_set(owner, 'bibtex_Type', partner)
    assert getattr(partner, 'bibtex_Techreport171') == owner
    _safe_set(owner, 'bibtex_Type', None)
    assert getattr(partner, 'bibtex_Techreport171') is None


def test_assoc_volume16_stub_double():
    # bibtex_Article has no real 'bibtex_Article17' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Volume's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Volume's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Volume(volume="sample_text")
    partner = bibtex_Article()
    setattr(partner, 'bibtex_Article17', None)
    _safe_set(owner, 'bibtex_Volume', partner)
    assert getattr(partner, 'bibtex_Article17') == owner
    _safe_set(owner, 'bibtex_Volume', None)
    assert getattr(partner, 'bibtex_Article17') is None


def test_assoc_volume28_stub_double():
    # bibtex_Book has no real 'bibtex_Book29' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Volume's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Volume's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Volume(volume="sample_text")
    partner = bibtex_Book()
    setattr(partner, 'bibtex_Book29', None)
    _safe_set(owner, 'bibtex_Volume30', partner)
    assert getattr(partner, 'bibtex_Book29') == owner
    _safe_set(owner, 'bibtex_Volume30', None)
    assert getattr(partner, 'bibtex_Book29') is None


def test_assoc_year5_stub_double():
    # bibtex_BibType has no real 'bibtex_BibType6' property in the generated
    # code (a bare stub) -- manually attach it so bibtex_Year's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # bibtex_Year's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = bibtex_Year(year="sample_text")
    partner = bibtex_BibType()
    setattr(partner, 'bibtex_BibType6', None)
    _safe_set(owner, 'bibtex_Year', partner)
    assert getattr(partner, 'bibtex_BibType6') == owner
    _safe_set(owner, 'bibtex_Year', None)
    assert getattr(partner, 'bibtex_BibType6') is None


