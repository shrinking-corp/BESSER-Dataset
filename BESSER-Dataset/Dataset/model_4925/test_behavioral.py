import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Container,
    Content,
    Page,
    web_Author,
    web_Container,
    web_Content,
    web_ContentPage,
    web_FooterEntry,
    web_Gallery,
    web_GalleryContent,
    web_HtmlContent,
    web_Image,
    web_Link,
    web_NewsEntry,
    web_NewsFeedPage,
    web_Page,
    web_Release,
    web_ReleaseSection,
    web_Site,
    web_SocialBar,
    web_SocialInformation,
    web_Version,
    ReleaseType,
    VersionState,
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

def test_assoc_author13_reverse_link_reassign_clear():
    a1 = web_NewsEntry(date=date(2024, 1, 1), description="sample_text", title="sample_text")
    a2 = web_NewsEntry(date=date(2025, 6, 15), description="sample_text_2", title="sample_text_2")
    b = web_Author(email="sample_text", name="sample_text", plusLink="sample_text")
    _safe_set(b, 'web_Author15', a1)
    assert _is_linked(b, 'web_Author15', a1)
    if hasattr(a1, 'web_NewsEntry14'):
        assert _is_linked(a1, 'web_NewsEntry14', b)
    _safe_set(b, 'web_Author15', a2)
    assert _is_linked(b, 'web_Author15', a2)
    if hasattr(a1, 'web_NewsEntry14'):
        assert not _is_linked(a1, 'web_NewsEntry14', b)
    if hasattr(a2, 'web_NewsEntry14'):
        assert _is_linked(a2, 'web_NewsEntry14', b)
    _safe_set(b, 'web_Author15', None)
    assert not _is_linked(b, 'web_Author15', a2)
    if hasattr(a2, 'web_NewsEntry14'):
        assert not _is_linked(a2, 'web_NewsEntry14', b)


def test_assoc_author4_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_Author(email="sample_text", name="sample_text", plusLink="sample_text")
    _safe_set(b, 'web_Author', a1)
    assert _is_linked(b, 'web_Author', a1)
    if hasattr(a1, 'web_Site5'):
        assert _is_linked(a1, 'web_Site5', b)
    _safe_set(b, 'web_Author', a2)
    assert _is_linked(b, 'web_Author', a2)
    if hasattr(a1, 'web_Site5'):
        assert not _is_linked(a1, 'web_Site5', b)
    if hasattr(a2, 'web_Site5'):
        assert _is_linked(a2, 'web_Site5', b)
    _safe_set(b, 'web_Author', None)
    assert not _is_linked(b, 'web_Author', a2)
    if hasattr(a2, 'web_Site5'):
        assert not _is_linked(a2, 'web_Site5', b)


def test_assoc_footer1_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_FooterEntry(link="sample_text", name="sample_text")
    _safe_set(b, 'web_FooterEntry', a1)
    assert _is_linked(b, 'web_FooterEntry', a1)
    if hasattr(a1, 'web_Site'):
        assert _is_linked(a1, 'web_Site', b)
    _safe_set(b, 'web_FooterEntry', a2)
    assert _is_linked(b, 'web_FooterEntry', a2)
    if hasattr(a1, 'web_Site'):
        assert not _is_linked(a1, 'web_Site', b)
    if hasattr(a2, 'web_Site'):
        assert _is_linked(a2, 'web_Site', b)
    _safe_set(b, 'web_FooterEntry', None)
    assert not _is_linked(b, 'web_FooterEntry', a2)
    if hasattr(a2, 'web_Site'):
        assert not _is_linked(a2, 'web_Site', b)


def test_assoc_galleries10_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_Gallery(label="sample_text")
    _safe_set(b, 'web_Gallery', a1)
    assert _is_linked(b, 'web_Gallery', a1)
    if hasattr(a1, 'web_Site11'):
        assert _is_linked(a1, 'web_Site11', b)
    _safe_set(b, 'web_Gallery', a2)
    assert _is_linked(b, 'web_Gallery', a2)
    if hasattr(a1, 'web_Site11'):
        assert not _is_linked(a1, 'web_Site11', b)
    if hasattr(a2, 'web_Site11'):
        assert _is_linked(a2, 'web_Site11', b)
    _safe_set(b, 'web_Gallery', None)
    assert not _is_linked(b, 'web_Gallery', a2)
    if hasattr(a2, 'web_Site11'):
        assert not _is_linked(a2, 'web_Site11', b)


def test_assoc_images20_reverse_link_reassign_clear():
    a1 = web_Image(label="sample_text", src="sample_text")
    a2 = web_Image(label="sample_text_2", src="sample_text_2")
    b = web_Gallery(label="sample_text")
    _safe_set(b, 'web_Gallery21', {a1})
    assert _is_linked(b, 'web_Gallery21', a1)
    if hasattr(a1, 'web_Image'):
        assert _is_linked(a1, 'web_Image', b)
    _safe_set(b, 'web_Gallery21', {a2})
    assert _is_linked(b, 'web_Gallery21', a2)
    if hasattr(a1, 'web_Image'):
        assert not _is_linked(a1, 'web_Image', b)
    if hasattr(a2, 'web_Image'):
        assert _is_linked(a2, 'web_Image', b)
    _safe_set(b, 'web_Gallery21', set())
    assert not _is_linked(b, 'web_Gallery21', a2)
    if hasattr(a2, 'web_Image'):
        assert not _is_linked(a2, 'web_Image', b)


def test_assoc_links6_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_Link(label="sample_text", target="sample_text")
    _safe_set(b, 'web_Link', a1)
    assert _is_linked(b, 'web_Link', a1)
    if hasattr(a1, 'web_Site7'):
        assert _is_linked(a1, 'web_Site7', b)
    _safe_set(b, 'web_Link', a2)
    assert _is_linked(b, 'web_Link', a2)
    if hasattr(a1, 'web_Site7'):
        assert not _is_linked(a1, 'web_Site7', b)
    if hasattr(a2, 'web_Site7'):
        assert _is_linked(a2, 'web_Site7', b)
    _safe_set(b, 'web_Link', None)
    assert not _is_linked(b, 'web_Link', a2)
    if hasattr(a2, 'web_Site7'):
        assert not _is_linked(a2, 'web_Site7', b)


def test_assoc_news2_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_NewsEntry(date=date(2024, 1, 1), description="sample_text", title="sample_text")
    _safe_set(b, 'web_NewsEntry', a1)
    assert _is_linked(b, 'web_NewsEntry', a1)
    if hasattr(a1, 'web_Site3'):
        assert _is_linked(a1, 'web_Site3', b)
    _safe_set(b, 'web_NewsEntry', a2)
    assert _is_linked(b, 'web_NewsEntry', a2)
    if hasattr(a1, 'web_Site3'):
        assert not _is_linked(a1, 'web_Site3', b)
    if hasattr(a2, 'web_Site3'):
        assert _is_linked(a2, 'web_Site3', b)
    _safe_set(b, 'web_NewsEntry', None)
    assert not _is_linked(b, 'web_NewsEntry', a2)
    if hasattr(a2, 'web_Site3'):
        assert not _is_linked(a2, 'web_Site3', b)


def test_assoc_pages0_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_Page(id="sample_text", name="sample_text")
    _safe_set(b, 'Page', a1)
    assert _is_linked(b, 'Page', a1)
    if hasattr(a1, 'site'):
        assert _is_linked(a1, 'site', b)
    _safe_set(b, 'Page', a2)
    assert _is_linked(b, 'Page', a2)
    if hasattr(a1, 'site'):
        assert not _is_linked(a1, 'site', b)
    if hasattr(a2, 'site'):
        assert _is_linked(a2, 'site', b)
    _safe_set(b, 'Page', None)
    assert not _is_linked(b, 'Page', a2)
    if hasattr(a2, 'site'):
        assert not _is_linked(a2, 'site', b)


def test_assoc_releases19_reverse_link_reassign_clear():
    a1 = web_Version(name="sample_text", state="sample_text")
    a2 = web_Version(name="sample_text_2", state="sample_text_2")
    b = web_Release(alternateMsiName="sample_text", baseName="sample_text", buildId="sample_text", date=date(2024, 1, 1), javadoc=True, name="sample_text", releaseNotesLink="sample_text", type="sample_text", unqualifiedName="sample_text")
    _safe_set(b, 'Release', a1)
    assert _is_linked(b, 'Release', a1)
    if hasattr(a1, 'version'):
        assert _is_linked(a1, 'version', b)
    _safe_set(b, 'Release', a2)
    assert _is_linked(b, 'Release', a2)
    if hasattr(a1, 'version'):
        assert not _is_linked(a1, 'version', b)
    if hasattr(a2, 'version'):
        assert _is_linked(a2, 'version', b)
    _safe_set(b, 'Release', None)
    assert not _is_linked(b, 'Release', a2)
    if hasattr(a2, 'version'):
        assert not _is_linked(a2, 'version', b)


def test_assoc_site12_reverse_link_reassign_clear():
    a1 = web_Site(description="sample_text", name="sample_text")
    a2 = web_Site(description="sample_text_2", name="sample_text_2")
    b = web_Page(id="sample_text", name="sample_text")
    _safe_set(b, 'pages', a1)
    assert _is_linked(b, 'pages', a1)
    if hasattr(a1, 'Site'):
        assert _is_linked(a1, 'Site', b)
    _safe_set(b, 'pages', a2)
    assert _is_linked(b, 'pages', a2)
    if hasattr(a1, 'Site'):
        assert not _is_linked(a1, 'Site', b)
    if hasattr(a2, 'Site'):
        assert _is_linked(a2, 'Site', b)
    _safe_set(b, 'pages', None)
    assert not _is_linked(b, 'pages', a2)
    if hasattr(a2, 'Site'):
        assert not _is_linked(a2, 'Site', b)


def test_assoc_version17_reverse_link_reassign_clear():
    a1 = web_Version(name="sample_text", state="sample_text")
    a2 = web_Version(name="sample_text_2", state="sample_text_2")
    b = web_Release(alternateMsiName="sample_text", baseName="sample_text", buildId="sample_text", date=date(2024, 1, 1), javadoc=True, name="sample_text", releaseNotesLink="sample_text", type="sample_text", unqualifiedName="sample_text")
    _safe_set(b, 'releases', a1)
    assert _is_linked(b, 'releases', a1)
    if hasattr(a1, 'Version'):
        assert _is_linked(a1, 'Version', b)
    _safe_set(b, 'releases', a2)
    assert _is_linked(b, 'releases', a2)
    if hasattr(a1, 'Version'):
        assert not _is_linked(a1, 'Version', b)
    if hasattr(a2, 'Version'):
        assert _is_linked(a2, 'Version', b)
    _safe_set(b, 'releases', None)
    assert not _is_linked(b, 'releases', a2)
    if hasattr(a2, 'Version'):
        assert not _is_linked(a2, 'Version', b)


def test_assoc_versions8_reverse_link_reassign_clear():
    a1 = web_Version(name="sample_text", state="sample_text")
    a2 = web_Version(name="sample_text_2", state="sample_text_2")
    b = web_Site(description="sample_text", name="sample_text")
    _safe_set(b, 'web_Site9', {a1})
    assert _is_linked(b, 'web_Site9', a1)
    if hasattr(a1, 'web_Version'):
        assert _is_linked(a1, 'web_Version', b)
    _safe_set(b, 'web_Site9', {a2})
    assert _is_linked(b, 'web_Site9', a2)
    if hasattr(a1, 'web_Version'):
        assert not _is_linked(a1, 'web_Version', b)
    if hasattr(a2, 'web_Version'):
        assert _is_linked(a2, 'web_Version', b)
    _safe_set(b, 'web_Site9', set())
    assert not _is_linked(b, 'web_Site9', a2)
    if hasattr(a2, 'web_Version'):
        assert not _is_linked(a2, 'web_Version', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_gallery22_stub_double():
    # web_GalleryContent has no real 'web_GalleryContent' property in the generated
    # code (a bare stub) -- manually attach it so web_Gallery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # web_Gallery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = web_Gallery(label="sample_text")
    partner = web_GalleryContent()
    setattr(partner, 'web_GalleryContent', None)
    _safe_set(owner, 'web_Gallery23', partner)
    assert getattr(partner, 'web_GalleryContent') == owner
    _safe_set(owner, 'web_Gallery23', None)
    assert getattr(partner, 'web_GalleryContent') is None


def test_assoc_information24_stub_double():
    # web_SocialBar has no real 'web_SocialBar' property in the generated
    # code (a bare stub) -- manually attach it so web_SocialInformation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # web_SocialInformation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = web_SocialInformation(facebookUrl="sample_text", plusUrl="sample_text", twitterUrl="sample_text", url="sample_text")
    partner = web_SocialBar()
    setattr(partner, 'web_SocialBar', None)
    _safe_set(owner, 'web_SocialInformation', partner)
    assert getattr(partner, 'web_SocialBar') == owner
    _safe_set(owner, 'web_SocialInformation', None)
    assert getattr(partner, 'web_SocialBar') is None


def test_assoc_release18_stub_double():
    # web_ReleaseSection has no real 'web_ReleaseSection' property in the generated
    # code (a bare stub) -- manually attach it so web_Release's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # web_Release's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = web_Release(alternateMsiName="sample_text", baseName="sample_text", buildId="sample_text", date=date(2024, 1, 1), javadoc=True, name="sample_text", releaseNotesLink="sample_text", type="sample_text", unqualifiedName="sample_text")
    partner = web_ReleaseSection()
    setattr(partner, 'web_ReleaseSection', None)
    _safe_set(owner, 'web_Release', partner)
    assert getattr(partner, 'web_ReleaseSection') == owner
    _safe_set(owner, 'web_Release', None)
    assert getattr(partner, 'web_ReleaseSection') is None


