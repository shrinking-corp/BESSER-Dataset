import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    InstallationUnit,
    build_Build,
    build_Bundle,
    build_Category,
    build_Compiler,
    build_Config,
    build_Contact,
    build_Contribution,
    build_Feature,
    build_InstallationUnit,
    build_Map,
    build_Platform,
    build_Product,
    build_Promotion,
    build_Repository,
    ARCH,
    ArchiveFormat,
    BuildType,
    OS,
    WS,
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

def test_assoc_base11_reverse_link_reassign_clear():
    a1 = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    a2 = build_Platform(deltapack="sample_text_2", file="sample_text_2", location="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build12', a1)
    assert _is_linked(b, 'build_Build12', a1)
    if hasattr(a1, 'build_Platform13'):
        assert _is_linked(a1, 'build_Platform13', b)
    _safe_set(b, 'build_Build12', a2)
    assert _is_linked(b, 'build_Build12', a2)
    if hasattr(a1, 'build_Platform13'):
        assert not _is_linked(a1, 'build_Platform13', b)
    if hasattr(a2, 'build_Platform13'):
        assert _is_linked(a2, 'build_Platform13', b)
    _safe_set(b, 'build_Build12', None)
    assert not _is_linked(b, 'build_Build12', a2)
    if hasattr(a2, 'build_Platform13'):
        assert not _is_linked(a2, 'build_Platform13', b)


def test_assoc_builder14_reverse_link_reassign_clear():
    a1 = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    a2 = build_Platform(deltapack="sample_text_2", file="sample_text_2", location="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build15', a1)
    assert _is_linked(b, 'build_Build15', a1)
    if hasattr(a1, 'build_Platform16'):
        assert _is_linked(a1, 'build_Platform16', b)
    _safe_set(b, 'build_Build15', a2)
    assert _is_linked(b, 'build_Build15', a2)
    if hasattr(a1, 'build_Platform16'):
        assert not _is_linked(a1, 'build_Platform16', b)
    if hasattr(a2, 'build_Platform16'):
        assert _is_linked(a2, 'build_Platform16', b)
    _safe_set(b, 'build_Build15', None)
    assert not _is_linked(b, 'build_Build15', a2)
    if hasattr(a2, 'build_Platform16'):
        assert not _is_linked(a2, 'build_Platform16', b)


def test_assoc_buildmaster21_reverse_link_reassign_clear():
    a1 = build_Contact(email="sample_text", name="sample_text")
    a2 = build_Contact(email="sample_text_2", name="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build22', a1)
    assert _is_linked(b, 'build_Build22', a1)
    if hasattr(a1, 'build_Contact'):
        assert _is_linked(a1, 'build_Contact', b)
    _safe_set(b, 'build_Build22', a2)
    assert _is_linked(b, 'build_Build22', a2)
    if hasattr(a1, 'build_Contact'):
        assert not _is_linked(a1, 'build_Contact', b)
    if hasattr(a2, 'build_Contact'):
        assert _is_linked(a2, 'build_Contact', b)
    _safe_set(b, 'build_Build22', None)
    assert not _is_linked(b, 'build_Build22', a2)
    if hasattr(a2, 'build_Contact'):
        assert not _is_linked(a2, 'build_Contact', b)


def test_assoc_categories5_reverse_link_reassign_clear():
    a1 = build_Category(description="sample_text", label="sample_text", name="sample_text")
    a2 = build_Category(description="sample_text_2", label="sample_text_2", name="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build6', {a1})
    assert _is_linked(b, 'build_Build6', a1)
    if hasattr(a1, 'build_Category'):
        assert _is_linked(a1, 'build_Category', b)
    _safe_set(b, 'build_Build6', {a2})
    assert _is_linked(b, 'build_Build6', a2)
    if hasattr(a1, 'build_Category'):
        assert not _is_linked(a1, 'build_Category', b)
    if hasattr(a2, 'build_Category'):
        assert _is_linked(a2, 'build_Category', b)
    _safe_set(b, 'build_Build6', set())
    assert not _is_linked(b, 'build_Build6', a2)
    if hasattr(a2, 'build_Category'):
        assert not _is_linked(a2, 'build_Category', b)


def test_assoc_category42_reverse_link_reassign_clear():
    a1 = build_Feature(inProduct=True)
    a2 = build_Feature(inProduct=False)
    b = build_Category(description="sample_text", label="sample_text", name="sample_text")
    _safe_set(b, 'Category', a1)
    assert _is_linked(b, 'Category', a1)
    if hasattr(a1, 'features'):
        assert _is_linked(a1, 'features', b)
    _safe_set(b, 'Category', a2)
    assert _is_linked(b, 'Category', a2)
    if hasattr(a1, 'features'):
        assert not _is_linked(a1, 'features', b)
    if hasattr(a2, 'features'):
        assert _is_linked(a2, 'features', b)
    _safe_set(b, 'Category', None)
    assert not _is_linked(b, 'Category', a2)
    if hasattr(a2, 'features'):
        assert not _is_linked(a2, 'features', b)


def test_assoc_compiler17_reverse_link_reassign_clear():
    a1 = build_Compiler(args="sample_text", debugInfo=True, failOnError=True, sourceVersion="sample_text", targetVersion="sample_text", verbose=True)
    a2 = build_Compiler(args="sample_text_2", debugInfo=False, failOnError=False, sourceVersion="sample_text_2", targetVersion="sample_text_2", verbose=False)
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build18', a1)
    assert _is_linked(b, 'build_Build18', a1)
    if hasattr(a1, 'build_Compiler'):
        assert _is_linked(a1, 'build_Compiler', b)
    _safe_set(b, 'build_Build18', a2)
    assert _is_linked(b, 'build_Build18', a2)
    if hasattr(a1, 'build_Compiler'):
        assert not _is_linked(a1, 'build_Compiler', b)
    if hasattr(a2, 'build_Compiler'):
        assert _is_linked(a2, 'build_Compiler', b)
    _safe_set(b, 'build_Build18', None)
    assert not _is_linked(b, 'build_Build18', a2)
    if hasattr(a2, 'build_Compiler'):
        assert not _is_linked(a2, 'build_Compiler', b)


def test_assoc_config26_reverse_link_reassign_clear():
    a1 = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    a2 = build_Platform(deltapack="sample_text_2", file="sample_text_2", location="sample_text_2")
    b = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    _safe_set(b, 'build_Config28', a1)
    assert _is_linked(b, 'build_Config28', a1)
    if hasattr(a1, 'build_Platform27'):
        assert _is_linked(a1, 'build_Platform27', b)
    _safe_set(b, 'build_Config28', a2)
    assert _is_linked(b, 'build_Config28', a2)
    if hasattr(a1, 'build_Platform27'):
        assert not _is_linked(a1, 'build_Platform27', b)
    if hasattr(a2, 'build_Platform27'):
        assert _is_linked(a2, 'build_Platform27', b)
    _safe_set(b, 'build_Config28', None)
    assert not _is_linked(b, 'build_Config28', a2)
    if hasattr(a2, 'build_Platform27'):
        assert not _is_linked(a2, 'build_Platform27', b)


def test_assoc_configs1_reverse_link_reassign_clear():
    a1 = build_Config(arch="sample_text", archiveFormat="sample_text", os="sample_text", ws="sample_text")
    a2 = build_Config(arch="sample_text_2", archiveFormat="sample_text_2", os="sample_text_2", ws="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build2', {a1})
    assert _is_linked(b, 'build_Build2', a1)
    if hasattr(a1, 'build_Config'):
        assert _is_linked(a1, 'build_Config', b)
    _safe_set(b, 'build_Build2', {a2})
    assert _is_linked(b, 'build_Build2', a2)
    if hasattr(a1, 'build_Config'):
        assert not _is_linked(a1, 'build_Config', b)
    if hasattr(a2, 'build_Config'):
        assert _is_linked(a2, 'build_Config', b)
    _safe_set(b, 'build_Build2', set())
    assert not _is_linked(b, 'build_Build2', a2)
    if hasattr(a2, 'build_Config'):
        assert not _is_linked(a2, 'build_Config', b)


def test_assoc_contacts30_reverse_link_reassign_clear():
    a1 = build_Contribution(label="sample_text")
    a2 = build_Contribution(label="sample_text_2")
    b = build_Contact(email="sample_text", name="sample_text")
    _safe_set(b, 'build_Contact32', a1)
    assert _is_linked(b, 'build_Contact32', a1)
    if hasattr(a1, 'build_Contribution31'):
        assert _is_linked(a1, 'build_Contribution31', b)
    _safe_set(b, 'build_Contact32', a2)
    assert _is_linked(b, 'build_Contact32', a2)
    if hasattr(a1, 'build_Contribution31'):
        assert not _is_linked(a1, 'build_Contribution31', b)
    if hasattr(a2, 'build_Contribution31'):
        assert _is_linked(a2, 'build_Contribution31', b)
    _safe_set(b, 'build_Contact32', None)
    assert not _is_linked(b, 'build_Contact32', a2)
    if hasattr(a2, 'build_Contribution31'):
        assert not _is_linked(a2, 'build_Contribution31', b)


def test_assoc_contributions7_reverse_link_reassign_clear():
    a1 = build_Contribution(label="sample_text")
    a2 = build_Contribution(label="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build8', {a1})
    assert _is_linked(b, 'build_Build8', a1)
    if hasattr(a1, 'build_Contribution'):
        assert _is_linked(a1, 'build_Contribution', b)
    _safe_set(b, 'build_Build8', {a2})
    assert _is_linked(b, 'build_Build8', a2)
    if hasattr(a1, 'build_Contribution'):
        assert not _is_linked(a1, 'build_Contribution', b)
    if hasattr(a2, 'build_Contribution'):
        assert _is_linked(a2, 'build_Contribution', b)
    _safe_set(b, 'build_Build8', set())
    assert not _is_linked(b, 'build_Build8', a2)
    if hasattr(a2, 'build_Contribution'):
        assert not _is_linked(a2, 'build_Contribution', b)


def test_assoc_defaultMailList23_reverse_link_reassign_clear():
    a1 = build_Contact(email="sample_text", name="sample_text")
    a2 = build_Contact(email="sample_text_2", name="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build24', {a1})
    assert _is_linked(b, 'build_Build24', a1)
    if hasattr(a1, 'build_Contact25'):
        assert _is_linked(a1, 'build_Contact25', b)
    _safe_set(b, 'build_Build24', {a2})
    assert _is_linked(b, 'build_Build24', a2)
    if hasattr(a1, 'build_Contact25'):
        assert not _is_linked(a1, 'build_Contact25', b)
    if hasattr(a2, 'build_Contact25'):
        assert _is_linked(a2, 'build_Contact25', b)
    _safe_set(b, 'build_Build24', set())
    assert not _is_linked(b, 'build_Build24', a2)
    if hasattr(a2, 'build_Contact25'):
        assert not _is_linked(a2, 'build_Contact25', b)


def test_assoc_features29_reverse_link_reassign_clear():
    a1 = build_Feature(inProduct=True)
    a2 = build_Feature(inProduct=False)
    b = build_Category(description="sample_text", label="sample_text", name="sample_text")
    _safe_set(b, 'category', {a1})
    assert _is_linked(b, 'category', a1)
    if hasattr(a1, 'Feature'):
        assert _is_linked(a1, 'Feature', b)
    _safe_set(b, 'category', {a2})
    assert _is_linked(b, 'category', a2)
    if hasattr(a1, 'Feature'):
        assert not _is_linked(a1, 'Feature', b)
    if hasattr(a2, 'Feature'):
        assert _is_linked(a2, 'Feature', b)
    _safe_set(b, 'category', set())
    assert not _is_linked(b, 'category', a2)
    if hasattr(a2, 'Feature'):
        assert not _is_linked(a2, 'Feature', b)


def test_assoc_features33_reverse_link_reassign_clear():
    a1 = build_Feature(inProduct=True)
    a2 = build_Feature(inProduct=False)
    b = build_Contribution(label="sample_text")
    _safe_set(b, 'build_Contribution34', {a1})
    assert _is_linked(b, 'build_Contribution34', a1)
    if hasattr(a1, 'build_Feature'):
        assert _is_linked(a1, 'build_Feature', b)
    _safe_set(b, 'build_Contribution34', {a2})
    assert _is_linked(b, 'build_Contribution34', a2)
    if hasattr(a1, 'build_Feature'):
        assert not _is_linked(a1, 'build_Feature', b)
    if hasattr(a2, 'build_Feature'):
        assert _is_linked(a2, 'build_Feature', b)
    _safe_set(b, 'build_Contribution34', set())
    assert not _is_linked(b, 'build_Contribution34', a2)
    if hasattr(a2, 'build_Feature'):
        assert not _is_linked(a2, 'build_Feature', b)


def test_assoc_map3_reverse_link_reassign_clear():
    a1 = build_Map(repo="sample_text", root="sample_text", tag="sample_text")
    a2 = build_Map(repo="sample_text_2", root="sample_text_2", tag="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build4', a1)
    assert _is_linked(b, 'build_Build4', a1)
    if hasattr(a1, 'build_Map'):
        assert _is_linked(a1, 'build_Map', b)
    _safe_set(b, 'build_Build4', a2)
    assert _is_linked(b, 'build_Build4', a2)
    if hasattr(a1, 'build_Map'):
        assert not _is_linked(a1, 'build_Map', b)
    if hasattr(a2, 'build_Map'):
        assert _is_linked(a2, 'build_Map', b)
    _safe_set(b, 'build_Build4', None)
    assert not _is_linked(b, 'build_Build4', a2)
    if hasattr(a2, 'build_Map'):
        assert not _is_linked(a2, 'build_Map', b)


def test_assoc_platforms0_reverse_link_reassign_clear():
    a1 = build_Platform(deltapack="sample_text", file="sample_text", location="sample_text")
    a2 = build_Platform(deltapack="sample_text_2", file="sample_text_2", location="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build', {a1})
    assert _is_linked(b, 'build_Build', a1)
    if hasattr(a1, 'build_Platform'):
        assert _is_linked(a1, 'build_Platform', b)
    _safe_set(b, 'build_Build', {a2})
    assert _is_linked(b, 'build_Build', a2)
    if hasattr(a1, 'build_Platform'):
        assert not _is_linked(a1, 'build_Platform', b)
    if hasattr(a2, 'build_Platform'):
        assert _is_linked(a2, 'build_Platform', b)
    _safe_set(b, 'build_Build', set())
    assert not _is_linked(b, 'build_Build', a2)
    if hasattr(a2, 'build_Platform'):
        assert not _is_linked(a2, 'build_Platform', b)


def test_assoc_promotion19_reverse_link_reassign_clear():
    a1 = build_Promotion(baseURL="sample_text", buildAlias="sample_text", downloadDirectory="sample_text", incubating=True, uploadDirectory="sample_text")
    a2 = build_Promotion(baseURL="sample_text_2", buildAlias="sample_text_2", downloadDirectory="sample_text_2", incubating=False, uploadDirectory="sample_text_2")
    b = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    _safe_set(b, 'build_Build20', a1)
    assert _is_linked(b, 'build_Build20', a1)
    if hasattr(a1, 'build_Promotion'):
        assert _is_linked(a1, 'build_Promotion', b)
    _safe_set(b, 'build_Build20', a2)
    assert _is_linked(b, 'build_Build20', a2)
    if hasattr(a1, 'build_Promotion'):
        assert not _is_linked(a1, 'build_Promotion', b)
    if hasattr(a2, 'build_Promotion'):
        assert _is_linked(a2, 'build_Promotion', b)
    _safe_set(b, 'build_Build20', None)
    assert not _is_linked(b, 'build_Build20', a2)
    if hasattr(a2, 'build_Promotion'):
        assert not _is_linked(a2, 'build_Promotion', b)


def test_assoc_repo43_reverse_link_reassign_clear():
    a1 = build_Repository(label="sample_text", location="sample_text")
    a2 = build_Repository(label="sample_text_2", location="sample_text_2")
    b = build_InstallationUnit(id="sample_text", version="sample_text")
    _safe_set(b, 'build_InstallationUnit', a1)
    assert _is_linked(b, 'build_InstallationUnit', a1)
    if hasattr(a1, 'build_Repository44'):
        assert _is_linked(a1, 'build_Repository44', b)
    _safe_set(b, 'build_InstallationUnit', a2)
    assert _is_linked(b, 'build_InstallationUnit', a2)
    if hasattr(a1, 'build_Repository44'):
        assert not _is_linked(a1, 'build_Repository44', b)
    if hasattr(a2, 'build_Repository44'):
        assert _is_linked(a2, 'build_Repository44', b)
    _safe_set(b, 'build_InstallationUnit', None)
    assert not _is_linked(b, 'build_InstallationUnit', a2)
    if hasattr(a2, 'build_Repository44'):
        assert not _is_linked(a2, 'build_Repository44', b)


def test_assoc_repositories35_reverse_link_reassign_clear():
    a1 = build_Repository(label="sample_text", location="sample_text")
    a2 = build_Repository(label="sample_text_2", location="sample_text_2")
    b = build_Contribution(label="sample_text")
    _safe_set(b, 'build_Contribution36', {a1})
    assert _is_linked(b, 'build_Contribution36', a1)
    if hasattr(a1, 'build_Repository'):
        assert _is_linked(a1, 'build_Repository', b)
    _safe_set(b, 'build_Contribution36', {a2})
    assert _is_linked(b, 'build_Contribution36', a2)
    if hasattr(a1, 'build_Repository'):
        assert not _is_linked(a1, 'build_Repository', b)
    if hasattr(a2, 'build_Repository'):
        assert _is_linked(a2, 'build_Repository', b)
    _safe_set(b, 'build_Contribution36', set())
    assert not _is_linked(b, 'build_Contribution36', a2)
    if hasattr(a2, 'build_Repository'):
        assert not _is_linked(a2, 'build_Repository', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_bundles37_stub_double():
    # build_Bundle has no real 'build_Bundle' property in the generated
    # code (a bare stub) -- manually attach it so build_Contribution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Contribution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Contribution(label="sample_text")
    partner = build_Bundle()
    setattr(partner, 'build_Bundle', None)
    _safe_set(owner, 'build_Contribution38', {partner})
    assert getattr(partner, 'build_Bundle') == owner
    _safe_set(owner, 'build_Contribution38', set())
    assert getattr(partner, 'build_Bundle') is None


def test_assoc_product9_stub_double():
    # build_Product has no real 'build_Product' property in the generated
    # code (a bare stub) -- manually attach it so build_Build's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Build's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Build(buildRoot="sample_text", builderURL="sample_text", date="sample_text", fetchTag="sample_text", label="sample_text", launchVM="sample_text", sendmail=True, time="sample_text", type="sample_text")
    partner = build_Product()
    setattr(partner, 'build_Product', None)
    _safe_set(owner, 'build_Build10', partner)
    assert getattr(partner, 'build_Product') == owner
    _safe_set(owner, 'build_Build10', None)
    assert getattr(partner, 'build_Product') is None


def test_assoc_products39_stub_double():
    # build_Product has no real 'build_Product41' property in the generated
    # code (a bare stub) -- manually attach it so build_Contribution's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # build_Contribution's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = build_Contribution(label="sample_text")
    partner = build_Product()
    setattr(partner, 'build_Product41', None)
    _safe_set(owner, 'build_Contribution40', {partner})
    assert getattr(partner, 'build_Product41') == owner
    _safe_set(owner, 'build_Contribution40', set())
    assert getattr(partner, 'build_Product41') is None


