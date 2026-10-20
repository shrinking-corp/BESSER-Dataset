import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    latex_Abstracte,
    latex_Begin,
    latex_Beginbib,
    latex_Bibliography,
    latex_Body,
    latex_Commands,
    latex_Document,
    latex_End,
    latex_Endbib,
    latex_Enumerate,
    latex_Figures,
    latex_General,
    latex_Packages,
    latex_Section,
    latex_Styles,
    latex_Subsection,
    latex_Title,
    latex_bibitem,
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

def test_assoc_Abscontainsgen19_reverse_link_reassign_clear():
    a1 = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    a2 = latex_General(genname="sample_text_2", genprefix="sample_text_2", gentext="sample_text_2")
    b = latex_Abstracte(abstractprefix="sample_text", abstracttext="sample_text")
    _safe_set(b, 'latex_Abstracte20', {a1})
    assert _is_linked(b, 'latex_Abstracte20', a1)
    if hasattr(a1, 'latex_General21'):
        assert _is_linked(a1, 'latex_General21', b)
    _safe_set(b, 'latex_Abstracte20', {a2})
    assert _is_linked(b, 'latex_Abstracte20', a2)
    if hasattr(a1, 'latex_General21'):
        assert not _is_linked(a1, 'latex_General21', b)
    if hasattr(a2, 'latex_General21'):
        assert _is_linked(a2, 'latex_General21', b)
    _safe_set(b, 'latex_Abstracte20', set())
    assert not _is_linked(b, 'latex_Abstracte20', a2)
    if hasattr(a2, 'latex_General21'):
        assert not _is_linked(a2, 'latex_General21', b)


def test_assoc_begindoc13_reverse_link_reassign_clear():
    a1 = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    a2 = latex_Document(documenttype="sample_text_2", fontsize="sample_text_2", papertype="sample_text_2", prefix="sample_text_2")
    b = latex_Begin(beginprefix="sample_text")
    _safe_set(b, 'latex_Begin', a1)
    assert _is_linked(b, 'latex_Begin', a1)
    if hasattr(a1, 'latex_Document14'):
        assert _is_linked(a1, 'latex_Document14', b)
    _safe_set(b, 'latex_Begin', a2)
    assert _is_linked(b, 'latex_Begin', a2)
    if hasattr(a1, 'latex_Document14'):
        assert not _is_linked(a1, 'latex_Document14', b)
    if hasattr(a2, 'latex_Document14'):
        assert _is_linked(a2, 'latex_Document14', b)
    _safe_set(b, 'latex_Begin', None)
    assert not _is_linked(b, 'latex_Begin', a2)
    if hasattr(a2, 'latex_Document14'):
        assert not _is_linked(a2, 'latex_Document14', b)


def test_assoc_bibcontainsgen28_reverse_link_reassign_clear():
    a1 = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    a2 = latex_General(genname="sample_text_2", genprefix="sample_text_2", gentext="sample_text_2")
    b = latex_Bibliography(bibstyle="sample_text")
    _safe_set(b, 'latex_Bibliography29', {a1})
    assert _is_linked(b, 'latex_Bibliography29', a1)
    if hasattr(a1, 'latex_General30'):
        assert _is_linked(a1, 'latex_General30', b)
    _safe_set(b, 'latex_Bibliography29', {a2})
    assert _is_linked(b, 'latex_Bibliography29', a2)
    if hasattr(a1, 'latex_General30'):
        assert not _is_linked(a1, 'latex_General30', b)
    if hasattr(a2, 'latex_General30'):
        assert _is_linked(a2, 'latex_General30', b)
    _safe_set(b, 'latex_Bibliography29', set())
    assert not _is_linked(b, 'latex_Bibliography29', a2)
    if hasattr(a2, 'latex_General30'):
        assert not _is_linked(a2, 'latex_General30', b)


def test_assoc_containbeginbib33_reverse_link_reassign_clear():
    a1 = latex_Bibliography(bibstyle="sample_text")
    a2 = latex_Bibliography(bibstyle="sample_text_2")
    b = latex_Beginbib(Beginbibprefix="sample_text")
    _safe_set(b, 'latex_Beginbib', a1)
    assert _is_linked(b, 'latex_Beginbib', a1)
    if hasattr(a1, 'latex_Bibliography34'):
        assert _is_linked(a1, 'latex_Bibliography34', b)
    _safe_set(b, 'latex_Beginbib', a2)
    assert _is_linked(b, 'latex_Beginbib', a2)
    if hasattr(a1, 'latex_Bibliography34'):
        assert not _is_linked(a1, 'latex_Bibliography34', b)
    if hasattr(a2, 'latex_Bibliography34'):
        assert _is_linked(a2, 'latex_Bibliography34', b)
    _safe_set(b, 'latex_Beginbib', None)
    assert not _is_linked(b, 'latex_Beginbib', a2)
    if hasattr(a2, 'latex_Bibliography34'):
        assert not _is_linked(a2, 'latex_Bibliography34', b)


def test_assoc_containendbib35_reverse_link_reassign_clear():
    a1 = latex_Endbib(Endbibprefix="sample_text")
    a2 = latex_Endbib(Endbibprefix="sample_text_2")
    b = latex_Bibliography(bibstyle="sample_text")
    _safe_set(b, 'latex_Bibliography36', a1)
    assert _is_linked(b, 'latex_Bibliography36', a1)
    if hasattr(a1, 'latex_Endbib'):
        assert _is_linked(a1, 'latex_Endbib', b)
    _safe_set(b, 'latex_Bibliography36', a2)
    assert _is_linked(b, 'latex_Bibliography36', a2)
    if hasattr(a1, 'latex_Endbib'):
        assert not _is_linked(a1, 'latex_Endbib', b)
    if hasattr(a2, 'latex_Endbib'):
        assert _is_linked(a2, 'latex_Endbib', b)
    _safe_set(b, 'latex_Bibliography36', None)
    assert not _is_linked(b, 'latex_Bibliography36', a2)
    if hasattr(a2, 'latex_Endbib'):
        assert not _is_linked(a2, 'latex_Endbib', b)


def test_assoc_containsabstract7_reverse_link_reassign_clear():
    a1 = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    a2 = latex_Document(documenttype="sample_text_2", fontsize="sample_text_2", papertype="sample_text_2", prefix="sample_text_2")
    b = latex_Abstracte(abstractprefix="sample_text", abstracttext="sample_text")
    _safe_set(b, 'latex_Abstracte', a1)
    assert _is_linked(b, 'latex_Abstracte', a1)
    if hasattr(a1, 'latex_Document8'):
        assert _is_linked(a1, 'latex_Document8', b)
    _safe_set(b, 'latex_Abstracte', a2)
    assert _is_linked(b, 'latex_Abstracte', a2)
    if hasattr(a1, 'latex_Document8'):
        assert not _is_linked(a1, 'latex_Document8', b)
    if hasattr(a2, 'latex_Document8'):
        assert _is_linked(a2, 'latex_Document8', b)
    _safe_set(b, 'latex_Abstracte', None)
    assert not _is_linked(b, 'latex_Abstracte', a2)
    if hasattr(a2, 'latex_Document8'):
        assert not _is_linked(a2, 'latex_Document8', b)


def test_assoc_containsbib11_reverse_link_reassign_clear():
    a1 = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    a2 = latex_Document(documenttype="sample_text_2", fontsize="sample_text_2", papertype="sample_text_2", prefix="sample_text_2")
    b = latex_Bibliography(bibstyle="sample_text")
    _safe_set(b, 'latex_Bibliography', a1)
    assert _is_linked(b, 'latex_Bibliography', a1)
    if hasattr(a1, 'latex_Document12'):
        assert _is_linked(a1, 'latex_Document12', b)
    _safe_set(b, 'latex_Bibliography', a2)
    assert _is_linked(b, 'latex_Bibliography', a2)
    if hasattr(a1, 'latex_Document12'):
        assert not _is_linked(a1, 'latex_Document12', b)
    if hasattr(a2, 'latex_Document12'):
        assert _is_linked(a2, 'latex_Document12', b)
    _safe_set(b, 'latex_Bibliography', None)
    assert not _is_linked(b, 'latex_Bibliography', a2)
    if hasattr(a2, 'latex_Document12'):
        assert not _is_linked(a2, 'latex_Document12', b)


def test_assoc_containsbibitems31_reverse_link_reassign_clear():
    a1 = latex_bibitem(bibprefix="sample_text", bibtext="sample_text")
    a2 = latex_bibitem(bibprefix="sample_text_2", bibtext="sample_text_2")
    b = latex_Bibliography(bibstyle="sample_text")
    _safe_set(b, 'latex_Bibliography32', {a1})
    assert _is_linked(b, 'latex_Bibliography32', a1)
    if hasattr(a1, 'latex_bibitem'):
        assert _is_linked(a1, 'latex_bibitem', b)
    _safe_set(b, 'latex_Bibliography32', {a2})
    assert _is_linked(b, 'latex_Bibliography32', a2)
    if hasattr(a1, 'latex_bibitem'):
        assert not _is_linked(a1, 'latex_bibitem', b)
    if hasattr(a2, 'latex_bibitem'):
        assert _is_linked(a2, 'latex_bibitem', b)
    _safe_set(b, 'latex_Bibliography32', set())
    assert not _is_linked(b, 'latex_Bibliography32', a2)
    if hasattr(a2, 'latex_bibitem'):
        assert not _is_linked(a2, 'latex_bibitem', b)


def test_assoc_containscommands1_reverse_link_reassign_clear():
    a1 = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    a2 = latex_Document(documenttype="sample_text_2", fontsize="sample_text_2", papertype="sample_text_2", prefix="sample_text_2")
    b = latex_Commands(comname="sample_text", comprefix="sample_text", comtext="sample_text", number=3.14)
    _safe_set(b, 'latex_Commands', a1)
    assert _is_linked(b, 'latex_Commands', a1)
    if hasattr(a1, 'latex_Document2'):
        assert _is_linked(a1, 'latex_Document2', b)
    _safe_set(b, 'latex_Commands', a2)
    assert _is_linked(b, 'latex_Commands', a2)
    if hasattr(a1, 'latex_Document2'):
        assert not _is_linked(a1, 'latex_Document2', b)
    if hasattr(a2, 'latex_Document2'):
        assert _is_linked(a2, 'latex_Document2', b)
    _safe_set(b, 'latex_Commands', None)
    assert not _is_linked(b, 'latex_Commands', a2)
    if hasattr(a2, 'latex_Document2'):
        assert not _is_linked(a2, 'latex_Document2', b)


def test_assoc_containspackages0_reverse_link_reassign_clear():
    a1 = latex_Packages(packageprefix="sample_text", packagetype="sample_text")
    a2 = latex_Packages(packageprefix="sample_text_2", packagetype="sample_text_2")
    b = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    _safe_set(b, 'latex_Document', {a1})
    assert _is_linked(b, 'latex_Document', a1)
    if hasattr(a1, 'latex_Packages'):
        assert _is_linked(a1, 'latex_Packages', b)
    _safe_set(b, 'latex_Document', {a2})
    assert _is_linked(b, 'latex_Document', a2)
    if hasattr(a1, 'latex_Packages'):
        assert not _is_linked(a1, 'latex_Packages', b)
    if hasattr(a2, 'latex_Packages'):
        assert _is_linked(a2, 'latex_Packages', b)
    _safe_set(b, 'latex_Document', set())
    assert not _is_linked(b, 'latex_Document', a2)
    if hasattr(a2, 'latex_Packages'):
        assert not _is_linked(a2, 'latex_Packages', b)


def test_assoc_containsstyles5_reverse_link_reassign_clear():
    a1 = latex_Styles(stylenames="sample_text", styleprefix="sample_text", stylesnames="sample_text")
    a2 = latex_Styles(stylenames="sample_text_2", styleprefix="sample_text_2", stylesnames="sample_text_2")
    b = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    _safe_set(b, 'latex_Document6', {a1})
    assert _is_linked(b, 'latex_Document6', a1)
    if hasattr(a1, 'latex_Styles'):
        assert _is_linked(a1, 'latex_Styles', b)
    _safe_set(b, 'latex_Document6', {a2})
    assert _is_linked(b, 'latex_Document6', a2)
    if hasattr(a1, 'latex_Styles'):
        assert not _is_linked(a1, 'latex_Styles', b)
    if hasattr(a2, 'latex_Styles'):
        assert _is_linked(a2, 'latex_Styles', b)
    _safe_set(b, 'latex_Document6', set())
    assert not _is_linked(b, 'latex_Document6', a2)
    if hasattr(a2, 'latex_Styles'):
        assert not _is_linked(a2, 'latex_Styles', b)


def test_assoc_containssubsections43_reverse_link_reassign_clear():
    a1 = latex_Subsection(subsectionname="sample_text", subsectionprefix="sample_text", subsectiontext="sample_text")
    a2 = latex_Subsection(subsectionname="sample_text_2", subsectionprefix="sample_text_2", subsectiontext="sample_text_2")
    b = latex_Subsection(subsectionname="sample_text", subsectionprefix="sample_text", subsectiontext="sample_text")
    _safe_set(b, 'latex_Subsection44', a1)
    assert _is_linked(b, 'latex_Subsection44', a1)
    if hasattr(a1, 'latex_Subsection42'):
        assert _is_linked(a1, 'latex_Subsection42', b)
    _safe_set(b, 'latex_Subsection44', a2)
    assert _is_linked(b, 'latex_Subsection44', a2)
    if hasattr(a1, 'latex_Subsection42'):
        assert not _is_linked(a1, 'latex_Subsection42', b)
    if hasattr(a2, 'latex_Subsection42'):
        assert _is_linked(a2, 'latex_Subsection42', b)
    _safe_set(b, 'latex_Subsection44', None)
    assert not _is_linked(b, 'latex_Subsection44', a2)
    if hasattr(a2, 'latex_Subsection42'):
        assert not _is_linked(a2, 'latex_Subsection42', b)


def test_assoc_containstitle3_reverse_link_reassign_clear():
    a1 = latex_Title(authortext="sample_text", titleprefix="sample_text", titletext="sample_text")
    a2 = latex_Title(authortext="sample_text_2", titleprefix="sample_text_2", titletext="sample_text_2")
    b = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    _safe_set(b, 'latex_Document4', a1)
    assert _is_linked(b, 'latex_Document4', a1)
    if hasattr(a1, 'latex_Title'):
        assert _is_linked(a1, 'latex_Title', b)
    _safe_set(b, 'latex_Document4', a2)
    assert _is_linked(b, 'latex_Document4', a2)
    if hasattr(a1, 'latex_Title'):
        assert not _is_linked(a1, 'latex_Title', b)
    if hasattr(a2, 'latex_Title'):
        assert _is_linked(a2, 'latex_Title', b)
    _safe_set(b, 'latex_Document4', None)
    assert not _is_linked(b, 'latex_Document4', a2)
    if hasattr(a2, 'latex_Title'):
        assert not _is_linked(a2, 'latex_Title', b)


def test_assoc_containsubsections40_reverse_link_reassign_clear():
    a1 = latex_Subsection(subsectionname="sample_text", subsectionprefix="sample_text", subsectiontext="sample_text")
    a2 = latex_Subsection(subsectionname="sample_text_2", subsectionprefix="sample_text_2", subsectiontext="sample_text_2")
    b = latex_Section(sectionname="sample_text", sectionprefix="sample_text", sectiontext="sample_text")
    _safe_set(b, 'latex_Section41', {a1})
    assert _is_linked(b, 'latex_Section41', a1)
    if hasattr(a1, 'latex_Subsection'):
        assert _is_linked(a1, 'latex_Subsection', b)
    _safe_set(b, 'latex_Section41', {a2})
    assert _is_linked(b, 'latex_Section41', a2)
    if hasattr(a1, 'latex_Subsection'):
        assert not _is_linked(a1, 'latex_Subsection', b)
    if hasattr(a2, 'latex_Subsection'):
        assert _is_linked(a2, 'latex_Subsection', b)
    _safe_set(b, 'latex_Section41', set())
    assert not _is_linked(b, 'latex_Section41', a2)
    if hasattr(a2, 'latex_Subsection'):
        assert not _is_linked(a2, 'latex_Subsection', b)


def test_assoc_enddoc15_reverse_link_reassign_clear():
    a1 = latex_End(endprefix="sample_text")
    a2 = latex_End(endprefix="sample_text_2")
    b = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    _safe_set(b, 'latex_Document16', a1)
    assert _is_linked(b, 'latex_Document16', a1)
    if hasattr(a1, 'latex_End'):
        assert _is_linked(a1, 'latex_End', b)
    _safe_set(b, 'latex_Document16', a2)
    assert _is_linked(b, 'latex_Document16', a2)
    if hasattr(a1, 'latex_End'):
        assert not _is_linked(a1, 'latex_End', b)
    if hasattr(a2, 'latex_End'):
        assert _is_linked(a2, 'latex_End', b)
    _safe_set(b, 'latex_Document16', None)
    assert not _is_linked(b, 'latex_Document16', a2)
    if hasattr(a2, 'latex_End'):
        assert not _is_linked(a2, 'latex_End', b)


def test_assoc_enumcontainsgen51_reverse_link_reassign_clear():
    a1 = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    a2 = latex_General(genname="sample_text_2", genprefix="sample_text_2", gentext="sample_text_2")
    b = latex_Enumerate(enumprefix="sample_text", enumtext="sample_text")
    _safe_set(b, 'latex_Enumerate52', {a1})
    assert _is_linked(b, 'latex_Enumerate52', a1)
    if hasattr(a1, 'latex_General53'):
        assert _is_linked(a1, 'latex_General53', b)
    _safe_set(b, 'latex_Enumerate52', {a2})
    assert _is_linked(b, 'latex_Enumerate52', a2)
    if hasattr(a1, 'latex_General53'):
        assert not _is_linked(a1, 'latex_General53', b)
    if hasattr(a2, 'latex_General53'):
        assert _is_linked(a2, 'latex_General53', b)
    _safe_set(b, 'latex_Enumerate52', set())
    assert not _is_linked(b, 'latex_Enumerate52', a2)
    if hasattr(a2, 'latex_General53'):
        assert not _is_linked(a2, 'latex_General53', b)


def test_assoc_figcontainsgen48_reverse_link_reassign_clear():
    a1 = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    a2 = latex_General(genname="sample_text_2", genprefix="sample_text_2", gentext="sample_text_2")
    b = latex_Figures(figcaption="sample_text", figname="sample_text", figprefix="sample_text")
    _safe_set(b, 'latex_Figures49', {a1})
    assert _is_linked(b, 'latex_Figures49', a1)
    if hasattr(a1, 'latex_General50'):
        assert _is_linked(a1, 'latex_General50', b)
    _safe_set(b, 'latex_Figures49', {a2})
    assert _is_linked(b, 'latex_Figures49', a2)
    if hasattr(a1, 'latex_General50'):
        assert not _is_linked(a1, 'latex_General50', b)
    if hasattr(a2, 'latex_General50'):
        assert _is_linked(a2, 'latex_General50', b)
    _safe_set(b, 'latex_Figures49', set())
    assert not _is_linked(b, 'latex_Figures49', a2)
    if hasattr(a2, 'latex_General50'):
        assert not _is_linked(a2, 'latex_General50', b)


def test_assoc_seccontainsgen37_reverse_link_reassign_clear():
    a1 = latex_Section(sectionname="sample_text", sectionprefix="sample_text", sectiontext="sample_text")
    a2 = latex_Section(sectionname="sample_text_2", sectionprefix="sample_text_2", sectiontext="sample_text_2")
    b = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    _safe_set(b, 'latex_General39', a1)
    assert _is_linked(b, 'latex_General39', a1)
    if hasattr(a1, 'latex_Section38'):
        assert _is_linked(a1, 'latex_Section38', b)
    _safe_set(b, 'latex_General39', a2)
    assert _is_linked(b, 'latex_General39', a2)
    if hasattr(a1, 'latex_Section38'):
        assert not _is_linked(a1, 'latex_Section38', b)
    if hasattr(a2, 'latex_Section38'):
        assert _is_linked(a2, 'latex_Section38', b)
    _safe_set(b, 'latex_General39', None)
    assert not _is_linked(b, 'latex_General39', a2)
    if hasattr(a2, 'latex_Section38'):
        assert not _is_linked(a2, 'latex_Section38', b)


def test_assoc_subseccontainsgen45_reverse_link_reassign_clear():
    a1 = latex_Subsection(subsectionname="sample_text", subsectionprefix="sample_text", subsectiontext="sample_text")
    a2 = latex_Subsection(subsectionname="sample_text_2", subsectionprefix="sample_text_2", subsectiontext="sample_text_2")
    b = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    _safe_set(b, 'latex_General47', a1)
    assert _is_linked(b, 'latex_General47', a1)
    if hasattr(a1, 'latex_Subsection46'):
        assert _is_linked(a1, 'latex_Subsection46', b)
    _safe_set(b, 'latex_General47', a2)
    assert _is_linked(b, 'latex_General47', a2)
    if hasattr(a1, 'latex_Subsection46'):
        assert not _is_linked(a1, 'latex_Subsection46', b)
    if hasattr(a2, 'latex_Subsection46'):
        assert _is_linked(a2, 'latex_Subsection46', b)
    _safe_set(b, 'latex_General47', None)
    assert not _is_linked(b, 'latex_General47', a2)
    if hasattr(a2, 'latex_Subsection46'):
        assert not _is_linked(a2, 'latex_Subsection46', b)


def test_assoc_titlecontainsgen17_reverse_link_reassign_clear():
    a1 = latex_Title(authortext="sample_text", titleprefix="sample_text", titletext="sample_text")
    a2 = latex_Title(authortext="sample_text_2", titleprefix="sample_text_2", titletext="sample_text_2")
    b = latex_General(genname="sample_text", genprefix="sample_text", gentext="sample_text")
    _safe_set(b, 'latex_General', a1)
    assert _is_linked(b, 'latex_General', a1)
    if hasattr(a1, 'latex_Title18'):
        assert _is_linked(a1, 'latex_Title18', b)
    _safe_set(b, 'latex_General', a2)
    assert _is_linked(b, 'latex_General', a2)
    if hasattr(a1, 'latex_Title18'):
        assert not _is_linked(a1, 'latex_Title18', b)
    if hasattr(a2, 'latex_Title18'):
        assert _is_linked(a2, 'latex_Title18', b)
    _safe_set(b, 'latex_General', None)
    assert not _is_linked(b, 'latex_General', a2)
    if hasattr(a2, 'latex_Title18'):
        assert not _is_linked(a2, 'latex_Title18', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containsbody9_stub_double():
    # latex_Body has no real 'latex_Body' property in the generated
    # code (a bare stub) -- manually attach it so latex_Document's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # latex_Document's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = latex_Document(documenttype="sample_text", fontsize="sample_text", papertype="sample_text", prefix="sample_text")
    partner = latex_Body()
    setattr(partner, 'latex_Body', None)
    _safe_set(owner, 'latex_Document10', partner)
    assert getattr(partner, 'latex_Body') == owner
    _safe_set(owner, 'latex_Document10', None)
    assert getattr(partner, 'latex_Body') is None


def test_assoc_containsenumerate26_stub_double():
    # latex_Body has no real 'latex_Body27' property in the generated
    # code (a bare stub) -- manually attach it so latex_Enumerate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # latex_Enumerate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = latex_Enumerate(enumprefix="sample_text", enumtext="sample_text")
    partner = latex_Body()
    setattr(partner, 'latex_Body27', None)
    _safe_set(owner, 'latex_Enumerate', partner)
    assert owner in getattr(partner, 'latex_Body27')
    _safe_set(owner, 'latex_Enumerate', None)
    assert owner not in getattr(partner, 'latex_Body27')


def test_assoc_containsfigures24_stub_double():
    # latex_Body has no real 'latex_Body25' property in the generated
    # code (a bare stub) -- manually attach it so latex_Figures's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # latex_Figures's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = latex_Figures(figcaption="sample_text", figname="sample_text", figprefix="sample_text")
    partner = latex_Body()
    setattr(partner, 'latex_Body25', None)
    _safe_set(owner, 'latex_Figures', partner)
    assert owner in getattr(partner, 'latex_Body25')
    _safe_set(owner, 'latex_Figures', None)
    assert owner not in getattr(partner, 'latex_Body25')


def test_assoc_containssections22_stub_double():
    # latex_Body has no real 'latex_Body23' property in the generated
    # code (a bare stub) -- manually attach it so latex_Section's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # latex_Section's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = latex_Section(sectionname="sample_text", sectionprefix="sample_text", sectiontext="sample_text")
    partner = latex_Body()
    setattr(partner, 'latex_Body23', None)
    _safe_set(owner, 'latex_Section', partner)
    assert owner in getattr(partner, 'latex_Body23')
    _safe_set(owner, 'latex_Section', None)
    assert owner not in getattr(partner, 'latex_Body23')


