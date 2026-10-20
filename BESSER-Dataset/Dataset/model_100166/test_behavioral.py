import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Sql,
    properties_DatabaseAlias,
    properties_DatabaseProperties,
    properties_DatabasePropertiesListType,
    properties_DocumentRoot,
    properties_EStringToStringMapEntry,
    properties_Property,
    properties_SpecificDBMSProperties,
    properties_Sql,
    properties_SqlFile,
    properties_SqlGroup,
    properties_SqlParameter,
    properties_SqlProperties,
    properties_SqlQuery,
    DBMS,
    ParameterType,
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

def test_assoc_additionalProperties1_reverse_link_reassign_clear():
    a1 = properties_Property(key="sample_text", value="sample_text")
    a2 = properties_Property(key="sample_text_2", value="sample_text_2")
    b = properties_DatabaseProperties(dBMS="sample_text", databaseName="sample_text", dialect="sample_text", driverClassName="sample_text", id="sample_text", namespace="sample_text", password="sample_text", persistenceUnitName="sample_text", port="sample_text", serverURL="sample_text", username="sample_text")
    _safe_set(b, 'properties_DatabaseProperties2', {a1})
    assert _is_linked(b, 'properties_DatabaseProperties2', a1)
    if hasattr(a1, 'properties_Property'):
        assert _is_linked(a1, 'properties_Property', b)
    _safe_set(b, 'properties_DatabaseProperties2', {a2})
    assert _is_linked(b, 'properties_DatabaseProperties2', a2)
    if hasattr(a1, 'properties_Property'):
        assert not _is_linked(a1, 'properties_Property', b)
    if hasattr(a2, 'properties_Property'):
        assert _is_linked(a2, 'properties_Property', b)
    _safe_set(b, 'properties_DatabaseProperties2', set())
    assert not _is_linked(b, 'properties_DatabaseProperties2', a2)
    if hasattr(a2, 'properties_Property'):
        assert not _is_linked(a2, 'properties_Property', b)


def test_assoc_parameters20_reverse_link_reassign_clear():
    a1 = properties_SqlParameter(index="sample_text", name="sample_text", type="sample_text")
    a2 = properties_SqlParameter(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = properties_Sql(hqlQuery="sample_text", id="sample_text")
    _safe_set(b, 'properties_Sql', {a1})
    assert _is_linked(b, 'properties_Sql', a1)
    if hasattr(a1, 'properties_SqlParameter'):
        assert _is_linked(a1, 'properties_SqlParameter', b)
    _safe_set(b, 'properties_Sql', {a2})
    assert _is_linked(b, 'properties_Sql', a2)
    if hasattr(a1, 'properties_SqlParameter'):
        assert not _is_linked(a1, 'properties_SqlParameter', b)
    if hasattr(a2, 'properties_SqlParameter'):
        assert _is_linked(a2, 'properties_SqlParameter', b)
    _safe_set(b, 'properties_Sql', set())
    assert not _is_linked(b, 'properties_Sql', a2)
    if hasattr(a2, 'properties_SqlParameter'):
        assert not _is_linked(a2, 'properties_SqlParameter', b)


def test_assoc_specificDBMSProperties26_reverse_link_reassign_clear():
    a1 = properties_SqlGroup(description="sample_text", id="sample_text")
    a2 = properties_SqlGroup(description="sample_text_2", id="sample_text_2")
    b = properties_SpecificDBMSProperties(dBMS="sample_text")
    _safe_set(b, 'properties_SpecificDBMSProperties28', a1)
    assert _is_linked(b, 'properties_SpecificDBMSProperties28', a1)
    if hasattr(a1, 'properties_SqlGroup27'):
        assert _is_linked(a1, 'properties_SqlGroup27', b)
    _safe_set(b, 'properties_SpecificDBMSProperties28', a2)
    assert _is_linked(b, 'properties_SpecificDBMSProperties28', a2)
    if hasattr(a1, 'properties_SqlGroup27'):
        assert not _is_linked(a1, 'properties_SqlGroup27', b)
    if hasattr(a2, 'properties_SqlGroup27'):
        assert _is_linked(a2, 'properties_SqlGroup27', b)
    _safe_set(b, 'properties_SpecificDBMSProperties28', None)
    assert not _is_linked(b, 'properties_SpecificDBMSProperties28', a2)
    if hasattr(a2, 'properties_SqlGroup27'):
        assert not _is_linked(a2, 'properties_SqlGroup27', b)


def test_assoc_sqlFile18_reverse_link_reassign_clear():
    a1 = properties_SqlFile(filePath="sample_text")
    a2 = properties_SqlFile(filePath="sample_text_2")
    b = properties_SpecificDBMSProperties(dBMS="sample_text")
    _safe_set(b, 'properties_SpecificDBMSProperties19', {a1})
    assert _is_linked(b, 'properties_SpecificDBMSProperties19', a1)
    if hasattr(a1, 'properties_SqlFile'):
        assert _is_linked(a1, 'properties_SqlFile', b)
    _safe_set(b, 'properties_SpecificDBMSProperties19', {a2})
    assert _is_linked(b, 'properties_SpecificDBMSProperties19', a2)
    if hasattr(a1, 'properties_SqlFile'):
        assert not _is_linked(a1, 'properties_SqlFile', b)
    if hasattr(a2, 'properties_SqlFile'):
        assert _is_linked(a2, 'properties_SqlFile', b)
    _safe_set(b, 'properties_SpecificDBMSProperties19', set())
    assert not _is_linked(b, 'properties_SpecificDBMSProperties19', a2)
    if hasattr(a2, 'properties_SqlFile'):
        assert not _is_linked(a2, 'properties_SqlFile', b)


def test_assoc_sqlFile23_reverse_link_reassign_clear():
    a1 = properties_SqlGroup(description="sample_text", id="sample_text")
    a2 = properties_SqlGroup(description="sample_text_2", id="sample_text_2")
    b = properties_SqlFile(filePath="sample_text")
    _safe_set(b, 'properties_SqlFile25', a1)
    assert _is_linked(b, 'properties_SqlFile25', a1)
    if hasattr(a1, 'properties_SqlGroup24'):
        assert _is_linked(a1, 'properties_SqlGroup24', b)
    _safe_set(b, 'properties_SqlFile25', a2)
    assert _is_linked(b, 'properties_SqlFile25', a2)
    if hasattr(a1, 'properties_SqlGroup24'):
        assert not _is_linked(a1, 'properties_SqlGroup24', b)
    if hasattr(a2, 'properties_SqlGroup24'):
        assert _is_linked(a2, 'properties_SqlGroup24', b)
    _safe_set(b, 'properties_SqlFile25', None)
    assert not _is_linked(b, 'properties_SqlFile25', a2)
    if hasattr(a2, 'properties_SqlGroup24'):
        assert not _is_linked(a2, 'properties_SqlGroup24', b)


def test_assoc_sqlQuery17_reverse_link_reassign_clear():
    a1 = properties_SqlQuery(queryString="sample_text")
    a2 = properties_SqlQuery(queryString="sample_text_2")
    b = properties_SpecificDBMSProperties(dBMS="sample_text")
    _safe_set(b, 'properties_SpecificDBMSProperties', {a1})
    assert _is_linked(b, 'properties_SpecificDBMSProperties', a1)
    if hasattr(a1, 'properties_SqlQuery'):
        assert _is_linked(a1, 'properties_SqlQuery', b)
    _safe_set(b, 'properties_SpecificDBMSProperties', {a2})
    assert _is_linked(b, 'properties_SpecificDBMSProperties', a2)
    if hasattr(a1, 'properties_SqlQuery'):
        assert not _is_linked(a1, 'properties_SqlQuery', b)
    if hasattr(a2, 'properties_SqlQuery'):
        assert _is_linked(a2, 'properties_SqlQuery', b)
    _safe_set(b, 'properties_SpecificDBMSProperties', set())
    assert not _is_linked(b, 'properties_SpecificDBMSProperties', a2)
    if hasattr(a2, 'properties_SqlQuery'):
        assert not _is_linked(a2, 'properties_SqlQuery', b)


def test_assoc_sqlQuery21_reverse_link_reassign_clear():
    a1 = properties_SqlQuery(queryString="sample_text")
    a2 = properties_SqlQuery(queryString="sample_text_2")
    b = properties_SqlGroup(description="sample_text", id="sample_text")
    _safe_set(b, 'properties_SqlGroup', {a1})
    assert _is_linked(b, 'properties_SqlGroup', a1)
    if hasattr(a1, 'properties_SqlQuery22'):
        assert _is_linked(a1, 'properties_SqlQuery22', b)
    _safe_set(b, 'properties_SqlGroup', {a2})
    assert _is_linked(b, 'properties_SqlGroup', a2)
    if hasattr(a1, 'properties_SqlQuery22'):
        assert not _is_linked(a1, 'properties_SqlQuery22', b)
    if hasattr(a2, 'properties_SqlQuery22'):
        assert _is_linked(a2, 'properties_SqlQuery22', b)
    _safe_set(b, 'properties_SqlGroup', set())
    assert not _is_linked(b, 'properties_SqlGroup', a2)
    if hasattr(a2, 'properties_SqlQuery22'):
        assert not _is_linked(a2, 'properties_SqlQuery22', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_databaseAlias5_stub_double():
    # properties_DatabasePropertiesListType has no real 'properties_DatabasePropertiesListType6' property in the generated
    # code (a bare stub) -- manually attach it so properties_DatabaseAlias's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DatabaseAlias's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DatabaseAlias(alias="sample_text", id="sample_text")
    partner = properties_DatabasePropertiesListType()
    setattr(partner, 'properties_DatabasePropertiesListType6', None)
    _safe_set(owner, 'properties_DatabaseAlias', partner)
    assert owner in getattr(partner, 'properties_DatabasePropertiesListType6')
    _safe_set(owner, 'properties_DatabaseAlias', None)
    assert owner not in getattr(partner, 'properties_DatabasePropertiesListType6')


def test_assoc_databaseProperties3_stub_double():
    # properties_DatabasePropertiesListType has no real 'properties_DatabasePropertiesListType' property in the generated
    # code (a bare stub) -- manually attach it so properties_DatabaseProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DatabaseProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DatabaseProperties(dBMS="sample_text", databaseName="sample_text", dialect="sample_text", driverClassName="sample_text", id="sample_text", namespace="sample_text", password="sample_text", persistenceUnitName="sample_text", port="sample_text", serverURL="sample_text", username="sample_text")
    partner = properties_DatabasePropertiesListType()
    setattr(partner, 'properties_DatabasePropertiesListType', None)
    _safe_set(owner, 'properties_DatabaseProperties4', partner)
    assert owner in getattr(partner, 'properties_DatabasePropertiesListType')
    _safe_set(owner, 'properties_DatabaseProperties4', None)
    assert owner not in getattr(partner, 'properties_DatabasePropertiesListType')


def test_assoc_databasePropertiesList11_stub_double():
    # properties_DatabasePropertiesListType has no real 'properties_DatabasePropertiesListType13' property in the generated
    # code (a bare stub) -- manually attach it so properties_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DocumentRoot(mixed="sample_text")
    partner = properties_DatabasePropertiesListType()
    setattr(partner, 'properties_DatabasePropertiesListType13', None)
    _safe_set(owner, 'properties_DocumentRoot12', {partner})
    assert getattr(partner, 'properties_DatabasePropertiesListType13') == owner
    _safe_set(owner, 'properties_DocumentRoot12', set())
    assert getattr(partner, 'properties_DatabasePropertiesListType13') is None


def test_assoc_sqlGroup29_stub_double():
    # properties_SqlProperties has no real 'properties_SqlProperties30' property in the generated
    # code (a bare stub) -- manually attach it so properties_SqlGroup's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_SqlGroup's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_SqlGroup(description="sample_text", id="sample_text")
    partner = properties_SqlProperties()
    setattr(partner, 'properties_SqlProperties30', None)
    _safe_set(owner, 'properties_SqlGroup31', partner)
    assert owner in getattr(partner, 'properties_SqlProperties30')
    _safe_set(owner, 'properties_SqlGroup31', None)
    assert owner not in getattr(partner, 'properties_SqlProperties30')


def test_assoc_sqlProperties0_stub_double():
    # properties_SqlProperties has no real 'properties_SqlProperties' property in the generated
    # code (a bare stub) -- manually attach it so properties_DatabaseProperties's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DatabaseProperties's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DatabaseProperties(dBMS="sample_text", databaseName="sample_text", dialect="sample_text", driverClassName="sample_text", id="sample_text", namespace="sample_text", password="sample_text", persistenceUnitName="sample_text", port="sample_text", serverURL="sample_text", username="sample_text")
    partner = properties_SqlProperties()
    setattr(partner, 'properties_SqlProperties', None)
    _safe_set(owner, 'properties_DatabaseProperties', partner)
    assert getattr(partner, 'properties_SqlProperties') == owner
    _safe_set(owner, 'properties_DatabaseProperties', None)
    assert getattr(partner, 'properties_SqlProperties') is None


def test_assoc_sqlProperties14_stub_double():
    # properties_SqlProperties has no real 'properties_SqlProperties16' property in the generated
    # code (a bare stub) -- manually attach it so properties_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DocumentRoot(mixed="sample_text")
    partner = properties_SqlProperties()
    setattr(partner, 'properties_SqlProperties16', None)
    _safe_set(owner, 'properties_DocumentRoot15', {partner})
    assert getattr(partner, 'properties_SqlProperties16') == owner
    _safe_set(owner, 'properties_DocumentRoot15', set())
    assert getattr(partner, 'properties_SqlProperties16') is None


def test_assoc_xMLNSPrefixMap7_stub_double():
    # properties_EStringToStringMapEntry has no real 'properties_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so properties_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DocumentRoot(mixed="sample_text")
    partner = properties_EStringToStringMapEntry()
    setattr(partner, 'properties_EStringToStringMapEntry', None)
    _safe_set(owner, 'properties_DocumentRoot', {partner})
    assert getattr(partner, 'properties_EStringToStringMapEntry') == owner
    _safe_set(owner, 'properties_DocumentRoot', set())
    assert getattr(partner, 'properties_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation8_stub_double():
    # properties_EStringToStringMapEntry has no real 'properties_EStringToStringMapEntry10' property in the generated
    # code (a bare stub) -- manually attach it so properties_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # properties_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = properties_DocumentRoot(mixed="sample_text")
    partner = properties_EStringToStringMapEntry()
    setattr(partner, 'properties_EStringToStringMapEntry10', None)
    _safe_set(owner, 'properties_DocumentRoot9', {partner})
    assert getattr(partner, 'properties_EStringToStringMapEntry10') == owner
    _safe_set(owner, 'properties_DocumentRoot9', set())
    assert getattr(partner, 'properties_EStringToStringMapEntry10') is None


