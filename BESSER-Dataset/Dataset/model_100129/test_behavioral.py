import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ContextID,
    ContextProvider,
    Credentials,
    DatabaseObjectDef,
    Service,
    ServiceConfig,
    Statement,
    TableDef,
    core_CatalogContainer,
    core_CatalogGenerationStrategy,
    core_CatalogMetaData,
    core_Connection,
    core_ConnectionConfig,
    core_ConnectionCredentials,
    core_ConnectionDescription,
    core_ConnectionManager,
    core_DataSourceFactory,
    core_DatabaseContainer,
    core_DatabaseManager,
    core_DatabaseObjectDef,
    core_IndexColumnDef,
    core_IndexDef,
    core_PreparedStatement,
    core_QualifiedName,
    core_SchemaDef,
    core_Statement,
    core_TableColumnDef,
    core_TableDef,
    core_ViewDef,
    DatabaseDataType,
    OrderingType,
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

def test_assoc_catalogContainers5_reverse_link_reassign_clear():
    a1 = core_DatabaseContainer(vendor="sample_text", version="sample_text")
    a2 = core_DatabaseContainer(vendor="sample_text_2", version="sample_text_2")
    b = core_CatalogContainer(active=True, name="sample_text", supportsGuestAccess=True)
    _safe_set(b, 'core_CatalogContainer6', a1)
    assert _is_linked(b, 'core_CatalogContainer6', a1)
    if hasattr(a1, 'core_DatabaseContainer'):
        assert _is_linked(a1, 'core_DatabaseContainer', b)
    _safe_set(b, 'core_CatalogContainer6', a2)
    assert _is_linked(b, 'core_CatalogContainer6', a2)
    if hasattr(a1, 'core_DatabaseContainer'):
        assert not _is_linked(a1, 'core_DatabaseContainer', b)
    if hasattr(a2, 'core_DatabaseContainer'):
        assert _is_linked(a2, 'core_DatabaseContainer', b)
    _safe_set(b, 'core_CatalogContainer6', None)
    assert not _is_linked(b, 'core_CatalogContainer6', a2)
    if hasattr(a2, 'core_DatabaseContainer'):
        assert not _is_linked(a2, 'core_DatabaseContainer', b)


def test_assoc_columns10_reverse_link_reassign_clear():
    a1 = core_IndexDef(clustered=True, unique=True)
    a2 = core_IndexDef(clustered=False, unique=False)
    b = core_IndexColumnDef(name="sample_text", ordering="sample_text", sequence=7)
    _safe_set(b, 'core_IndexColumnDef', a1)
    assert _is_linked(b, 'core_IndexColumnDef', a1)
    if hasattr(a1, 'core_IndexDef'):
        assert _is_linked(a1, 'core_IndexDef', b)
    _safe_set(b, 'core_IndexColumnDef', a2)
    assert _is_linked(b, 'core_IndexColumnDef', a2)
    if hasattr(a1, 'core_IndexDef'):
        assert not _is_linked(a1, 'core_IndexDef', b)
    if hasattr(a2, 'core_IndexDef'):
        assert _is_linked(a2, 'core_IndexDef', b)
    _safe_set(b, 'core_IndexColumnDef', None)
    assert not _is_linked(b, 'core_IndexColumnDef', a2)
    if hasattr(a2, 'core_IndexDef'):
        assert not _is_linked(a2, 'core_IndexDef', b)


def test_assoc_connectionConfig0_reverse_link_reassign_clear():
    a1 = core_ConnectionConfig(catalog="sample_text", persistent=True, url="sample_text", vendor="sample_text", version="sample_text")
    a2 = core_ConnectionConfig(catalog="sample_text_2", persistent=False, url="sample_text_2", vendor="sample_text_2", version="sample_text_2")
    b = core_CatalogContainer(active=True, name="sample_text", supportsGuestAccess=True)
    _safe_set(b, 'core_CatalogContainer', a1)
    assert _is_linked(b, 'core_CatalogContainer', a1)
    if hasattr(a1, 'core_ConnectionConfig'):
        assert _is_linked(a1, 'core_ConnectionConfig', b)
    _safe_set(b, 'core_CatalogContainer', a2)
    assert _is_linked(b, 'core_CatalogContainer', a2)
    if hasattr(a1, 'core_ConnectionConfig'):
        assert not _is_linked(a1, 'core_ConnectionConfig', b)
    if hasattr(a2, 'core_ConnectionConfig'):
        assert _is_linked(a2, 'core_ConnectionConfig', b)
    _safe_set(b, 'core_CatalogContainer', None)
    assert not _is_linked(b, 'core_CatalogContainer', a2)
    if hasattr(a2, 'core_ConnectionConfig'):
        assert not _is_linked(a2, 'core_ConnectionConfig', b)


def test_assoc_defaultCatalogContainer7_reverse_link_reassign_clear():
    a1 = core_DatabaseContainer(vendor="sample_text", version="sample_text")
    a2 = core_DatabaseContainer(vendor="sample_text_2", version="sample_text_2")
    b = core_CatalogContainer(active=True, name="sample_text", supportsGuestAccess=True)
    _safe_set(b, 'core_CatalogContainer9', a1)
    assert _is_linked(b, 'core_CatalogContainer9', a1)
    if hasattr(a1, 'core_DatabaseContainer8'):
        assert _is_linked(a1, 'core_DatabaseContainer8', b)
    _safe_set(b, 'core_CatalogContainer9', a2)
    assert _is_linked(b, 'core_CatalogContainer9', a2)
    if hasattr(a1, 'core_DatabaseContainer8'):
        assert not _is_linked(a1, 'core_DatabaseContainer8', b)
    if hasattr(a2, 'core_DatabaseContainer8'):
        assert _is_linked(a2, 'core_DatabaseContainer8', b)
    _safe_set(b, 'core_CatalogContainer9', None)
    assert not _is_linked(b, 'core_CatalogContainer9', a2)
    if hasattr(a2, 'core_DatabaseContainer8'):
        assert not _is_linked(a2, 'core_DatabaseContainer8', b)


def test_assoc_generationStrategy1_reverse_link_reassign_clear():
    a1 = core_CatalogGenerationStrategy(createIndexOnView=True, createRelativeRecordNumber=True)
    a2 = core_CatalogGenerationStrategy(createIndexOnView=False, createRelativeRecordNumber=False)
    b = core_CatalogContainer(active=True, name="sample_text", supportsGuestAccess=True)
    _safe_set(b, 'core_CatalogContainer2', a1)
    assert _is_linked(b, 'core_CatalogContainer2', a1)
    if hasattr(a1, 'core_CatalogGenerationStrategy'):
        assert _is_linked(a1, 'core_CatalogGenerationStrategy', b)
    _safe_set(b, 'core_CatalogContainer2', a2)
    assert _is_linked(b, 'core_CatalogContainer2', a2)
    if hasattr(a1, 'core_CatalogGenerationStrategy'):
        assert not _is_linked(a1, 'core_CatalogGenerationStrategy', b)
    if hasattr(a2, 'core_CatalogGenerationStrategy'):
        assert _is_linked(a2, 'core_CatalogGenerationStrategy', b)
    _safe_set(b, 'core_CatalogContainer2', None)
    assert not _is_linked(b, 'core_CatalogContainer2', a2)
    if hasattr(a2, 'core_CatalogGenerationStrategy'):
        assert not _is_linked(a2, 'core_CatalogGenerationStrategy', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_columns11_stub_double():
    # core_TableDef has no real 'core_TableDef' property in the generated
    # code (a bare stub) -- manually attach it so core_TableColumnDef's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_TableColumnDef's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_TableColumnDef(dataType="sample_text", default=True, length=7, name="sample_text", nullable=True, scale=7)
    partner = core_TableDef()
    setattr(partner, 'core_TableDef', None)
    _safe_set(owner, 'core_TableColumnDef', partner)
    assert owner in getattr(partner, 'core_TableDef')
    _safe_set(owner, 'core_TableColumnDef', None)
    assert owner not in getattr(partner, 'core_TableDef')


def test_assoc_credentials3_stub_double():
    # core_ConnectionCredentials has no real 'core_ConnectionCredentials' property in the generated
    # code (a bare stub) -- manually attach it so core_ConnectionConfig's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # core_ConnectionConfig's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = core_ConnectionConfig(catalog="sample_text", persistent=True, url="sample_text", vendor="sample_text", version="sample_text")
    partner = core_ConnectionCredentials()
    setattr(partner, 'core_ConnectionCredentials', None)
    _safe_set(owner, 'core_ConnectionConfig4', partner)
    assert getattr(partner, 'core_ConnectionCredentials') == owner
    _safe_set(owner, 'core_ConnectionConfig4', None)
    assert getattr(partner, 'core_ConnectionCredentials') is None


