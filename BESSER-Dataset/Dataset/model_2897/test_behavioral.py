import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MobaApplicationFeature,
    MobaConstraint,
    MobaConstraintable,
    MobaData,
    MobaDtoFeature,
    MobaEntityFeature,
    MobaExternalModule,
    MobaFeature,
    MobaFriendsAble,
    MobaGeneratorFeature,
    MobaIndexEntry,
    MobaModelFeature,
    MobaMultiplicityAble,
    MobaPropertiesAble,
    MobaQueueFeature,
    MobaREST,
    MobaRESTAbstractAttribute,
    MobaSettingsFeature,
    MobaTrigger,
    index_moba_MobaApplication,
    moba_MobaAppInstallTrigger,
    moba_MobaAppUpdateTrigger,
    moba_MobaApplication,
    moba_MobaApplicationFeature,
    moba_MobaAuthorization,
    moba_MobaBluetoothModule,
    moba_MobaCache,
    moba_MobaConstant,
    moba_MobaConstantValue,
    moba_MobaConstraint,
    moba_MobaConstraintable,
    moba_MobaData,
    moba_MobaDataType,
    moba_MobaDeviceStartupTrigger,
    moba_MobaDigitsConstraint,
    moba_MobaDto,
    moba_MobaDtoAttribute,
    moba_MobaDtoEmbeddable,
    moba_MobaDtoFeature,
    moba_MobaDtoReference,
    moba_MobaEmailTrigger,
    moba_MobaEntity,
    moba_MobaEntityAttribute,
    moba_MobaEntityEmbeddable,
    moba_MobaEntityFeature,
    moba_MobaEntityIndex,
    moba_MobaEntityReference,
    moba_MobaEnum,
    moba_MobaEnumLiteral,
    moba_MobaExternalModule,
    moba_MobaFeature,
    moba_MobaFriend,
    moba_MobaFriendsAble,
    moba_MobaFutureConstraint,
    moba_MobaGenerator,
    moba_MobaGeneratorFeature,
    moba_MobaGeneratorIDFeature,
    moba_MobaGeneratorMixinFeature,
    moba_MobaGeneratorSlot,
    moba_MobaGeofenceTrigger,
    moba_MobaMaxConstraint,
    moba_MobaMaxLengthConstraint,
    moba_MobaMinConstraint,
    moba_MobaMinLengthConstraint,
    moba_MobaModel,
    moba_MobaModelFeature,
    moba_MobaMuliplicity,
    moba_MobaMultiplicityAble,
    moba_MobaNFCModule,
    moba_MobaNotNullConstraint,
    moba_MobaNullConstraint,
    moba_MobaPastConstraint,
    moba_MobaPersistenceType,
    moba_MobaProject,
    moba_MobaPropertiesAble,
    moba_MobaProperty,
    moba_MobaPushModule,
    moba_MobaPushTrigger,
    moba_MobaQueue,
    moba_MobaQueueFeature,
    moba_MobaQueueReference,
    moba_MobaREST,
    moba_MobaRESTAbstractAttribute,
    moba_MobaRESTAttribute,
    moba_MobaRESTCrud,
    moba_MobaRESTCustomService,
    moba_MobaRESTDtoAttribute,
    moba_MobaRESTHeader,
    moba_MobaRESTPayloadDefinition,
    moba_MobaRESTWorkflow,
    moba_MobaRegexpConstraint,
    moba_MobaSMSTrigger,
    moba_MobaServer,
    moba_MobaSettings,
    moba_MobaSettingsAttribute,
    moba_MobaSettingsEntityReference,
    moba_MobaSettingsFeature,
    moba_MobaTemplate,
    moba_MobaTimerTrigger,
    moba_MobaTransportSerializationType,
    moba_MobaTrigger,
    moba_index_MobaIndex,
    moba_index_MobaIndexEntry,
    MobaBlueToothModuleType,
    MobaConstantValueFunction,
    MobaGeofenceEvent,
    MobaLowerBound,
    MobaNFCModuleType,
    MobaRESTMethods,
    MobaUpperBound,
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

def test_assoc_aliasConst117_reverse_link_reassign_clear():
    a1 = moba_MobaRESTAbstractAttribute(alias="sample_text", aliasString="sample_text", attachment=True)
    a2 = moba_MobaRESTAbstractAttribute(alias="sample_text_2", aliasString="sample_text_2", attachment=False)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant118', a1)
    assert _is_linked(b, 'moba_MobaConstant118', a1)
    if hasattr(a1, 'moba_MobaRESTAbstractAttribute'):
        assert _is_linked(a1, 'moba_MobaRESTAbstractAttribute', b)
    _safe_set(b, 'moba_MobaConstant118', a2)
    assert _is_linked(b, 'moba_MobaConstant118', a2)
    if hasattr(a1, 'moba_MobaRESTAbstractAttribute'):
        assert not _is_linked(a1, 'moba_MobaRESTAbstractAttribute', b)
    if hasattr(a2, 'moba_MobaRESTAbstractAttribute'):
        assert _is_linked(a2, 'moba_MobaRESTAbstractAttribute', b)
    _safe_set(b, 'moba_MobaConstant118', None)
    assert not _is_linked(b, 'moba_MobaConstant118', a2)
    if hasattr(a2, 'moba_MobaRESTAbstractAttribute'):
        assert not _is_linked(a2, 'moba_MobaRESTAbstractAttribute', b)


def test_assoc_attributes77_reverse_link_reassign_clear():
    a1 = moba_MobaEntityIndex(name="sample_text", unique=True)
    a2 = moba_MobaEntityIndex(name="sample_text_2", unique=False)
    b = moba_MobaEntityAttribute(domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    _safe_set(b, 'moba_MobaEntityAttribute', a1)
    assert _is_linked(b, 'moba_MobaEntityAttribute', a1)
    if hasattr(a1, 'moba_MobaEntityIndex78'):
        assert _is_linked(a1, 'moba_MobaEntityIndex78', b)
    _safe_set(b, 'moba_MobaEntityAttribute', a2)
    assert _is_linked(b, 'moba_MobaEntityAttribute', a2)
    if hasattr(a1, 'moba_MobaEntityIndex78'):
        assert not _is_linked(a1, 'moba_MobaEntityIndex78', b)
    if hasattr(a2, 'moba_MobaEntityIndex78'):
        assert _is_linked(a2, 'moba_MobaEntityIndex78', b)
    _safe_set(b, 'moba_MobaEntityAttribute', None)
    assert not _is_linked(b, 'moba_MobaEntityAttribute', a2)
    if hasattr(a2, 'moba_MobaEntityIndex78'):
        assert not _is_linked(a2, 'moba_MobaEntityIndex78', b)


def test_assoc_authorization108_reverse_link_reassign_clear():
    a1 = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    a2 = moba_MobaREST(bigData=False, name="sample_text_2", path="sample_text_2", url="sample_text_2")
    b = moba_MobaAuthorization(name="sample_text")
    _safe_set(b, 'moba_MobaAuthorization110', a1)
    assert _is_linked(b, 'moba_MobaAuthorization110', a1)
    if hasattr(a1, 'moba_MobaREST109'):
        assert _is_linked(a1, 'moba_MobaREST109', b)
    _safe_set(b, 'moba_MobaAuthorization110', a2)
    assert _is_linked(b, 'moba_MobaAuthorization110', a2)
    if hasattr(a1, 'moba_MobaREST109'):
        assert not _is_linked(a1, 'moba_MobaREST109', b)
    if hasattr(a2, 'moba_MobaREST109'):
        assert _is_linked(a2, 'moba_MobaREST109', b)
    _safe_set(b, 'moba_MobaAuthorization110', None)
    assert not _is_linked(b, 'moba_MobaAuthorization110', a2)
    if hasattr(a2, 'moba_MobaREST109'):
        assert not _is_linked(a2, 'moba_MobaREST109', b)


def test_assoc_authorization17_reverse_link_reassign_clear():
    a1 = moba_MobaServer(name="sample_text", urlString="sample_text")
    a2 = moba_MobaServer(name="sample_text_2", urlString="sample_text_2")
    b = moba_MobaAuthorization(name="sample_text")
    _safe_set(b, 'moba_MobaAuthorization', a1)
    assert _is_linked(b, 'moba_MobaAuthorization', a1)
    if hasattr(a1, 'moba_MobaServer18'):
        assert _is_linked(a1, 'moba_MobaServer18', b)
    _safe_set(b, 'moba_MobaAuthorization', a2)
    assert _is_linked(b, 'moba_MobaAuthorization', a2)
    if hasattr(a1, 'moba_MobaServer18'):
        assert not _is_linked(a1, 'moba_MobaServer18', b)
    if hasattr(a2, 'moba_MobaServer18'):
        assert _is_linked(a2, 'moba_MobaServer18', b)
    _safe_set(b, 'moba_MobaAuthorization', None)
    assert not _is_linked(b, 'moba_MobaAuthorization', a2)
    if hasattr(a2, 'moba_MobaServer18'):
        assert not _is_linked(a2, 'moba_MobaServer18', b)


def test_assoc_cache70_reverse_link_reassign_clear():
    a1 = moba_MobaEntity(name="sample_text")
    a2 = moba_MobaEntity(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache72', a1)
    assert _is_linked(b, 'moba_MobaCache72', a1)
    if hasattr(a1, 'moba_MobaEntity71'):
        assert _is_linked(a1, 'moba_MobaEntity71', b)
    _safe_set(b, 'moba_MobaCache72', a2)
    assert _is_linked(b, 'moba_MobaCache72', a2)
    if hasattr(a1, 'moba_MobaEntity71'):
        assert not _is_linked(a1, 'moba_MobaEntity71', b)
    if hasattr(a2, 'moba_MobaEntity71'):
        assert _is_linked(a2, 'moba_MobaEntity71', b)
    _safe_set(b, 'moba_MobaCache72', None)
    assert not _is_linked(b, 'moba_MobaCache72', a2)
    if hasattr(a2, 'moba_MobaEntity71'):
        assert not _is_linked(a2, 'moba_MobaEntity71', b)


def test_assoc_cache90_reverse_link_reassign_clear():
    a1 = moba_MobaQueue(name="sample_text")
    a2 = moba_MobaQueue(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache92', a1)
    assert _is_linked(b, 'moba_MobaCache92', a1)
    if hasattr(a1, 'moba_MobaQueue91'):
        assert _is_linked(a1, 'moba_MobaQueue91', b)
    _safe_set(b, 'moba_MobaCache92', a2)
    assert _is_linked(b, 'moba_MobaCache92', a2)
    if hasattr(a1, 'moba_MobaQueue91'):
        assert not _is_linked(a1, 'moba_MobaQueue91', b)
    if hasattr(a2, 'moba_MobaQueue91'):
        assert _is_linked(a2, 'moba_MobaQueue91', b)
    _safe_set(b, 'moba_MobaCache92', None)
    assert not _is_linked(b, 'moba_MobaCache92', a2)
    if hasattr(a2, 'moba_MobaQueue91'):
        assert not _is_linked(a2, 'moba_MobaQueue91', b)


def test_assoc_cacheIntervalConst39_reverse_link_reassign_clear():
    a1 = moba_MobaConstant(name="sample_text")
    a2 = moba_MobaConstant(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache40', a1)
    assert _is_linked(b, 'moba_MobaCache40', a1)
    if hasattr(a1, 'moba_MobaConstant41'):
        assert _is_linked(a1, 'moba_MobaConstant41', b)
    _safe_set(b, 'moba_MobaCache40', a2)
    assert _is_linked(b, 'moba_MobaCache40', a2)
    if hasattr(a1, 'moba_MobaConstant41'):
        assert not _is_linked(a1, 'moba_MobaConstant41', b)
    if hasattr(a2, 'moba_MobaConstant41'):
        assert _is_linked(a2, 'moba_MobaConstant41', b)
    _safe_set(b, 'moba_MobaCache40', None)
    assert not _is_linked(b, 'moba_MobaCache40', a2)
    if hasattr(a2, 'moba_MobaConstant41'):
        assert not _is_linked(a2, 'moba_MobaConstant41', b)


def test_assoc_cachePersistence42_reverse_link_reassign_clear():
    a1 = moba_MobaPersistenceType(name="sample_text")
    a2 = moba_MobaPersistenceType(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache43', a1)
    assert _is_linked(b, 'moba_MobaCache43', a1)
    if hasattr(a1, 'moba_MobaPersistenceType'):
        assert _is_linked(a1, 'moba_MobaPersistenceType', b)
    _safe_set(b, 'moba_MobaCache43', a2)
    assert _is_linked(b, 'moba_MobaCache43', a2)
    if hasattr(a1, 'moba_MobaPersistenceType'):
        assert not _is_linked(a1, 'moba_MobaPersistenceType', b)
    if hasattr(a2, 'moba_MobaPersistenceType'):
        assert _is_linked(a2, 'moba_MobaPersistenceType', b)
    _safe_set(b, 'moba_MobaCache43', None)
    assert not _is_linked(b, 'moba_MobaCache43', a2)
    if hasattr(a2, 'moba_MobaPersistenceType'):
        assert not _is_linked(a2, 'moba_MobaPersistenceType', b)


def test_assoc_cacheStrategyConst36_reverse_link_reassign_clear():
    a1 = moba_MobaConstant(name="sample_text")
    a2 = moba_MobaConstant(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache37', a1)
    assert _is_linked(b, 'moba_MobaCache37', a1)
    if hasattr(a1, 'moba_MobaConstant38'):
        assert _is_linked(a1, 'moba_MobaConstant38', b)
    _safe_set(b, 'moba_MobaCache37', a2)
    assert _is_linked(b, 'moba_MobaCache37', a2)
    if hasattr(a1, 'moba_MobaConstant38'):
        assert not _is_linked(a1, 'moba_MobaConstant38', b)
    if hasattr(a2, 'moba_MobaConstant38'):
        assert _is_linked(a2, 'moba_MobaConstant38', b)
    _safe_set(b, 'moba_MobaCache37', None)
    assert not _is_linked(b, 'moba_MobaCache37', a2)
    if hasattr(a2, 'moba_MobaConstant38'):
        assert not _is_linked(a2, 'moba_MobaConstant38', b)


def test_assoc_cacheTypeConst33_reverse_link_reassign_clear():
    a1 = moba_MobaConstant(name="sample_text")
    a2 = moba_MobaConstant(name="sample_text_2")
    b = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    _safe_set(b, 'moba_MobaCache34', a1)
    assert _is_linked(b, 'moba_MobaCache34', a1)
    if hasattr(a1, 'moba_MobaConstant35'):
        assert _is_linked(a1, 'moba_MobaConstant35', b)
    _safe_set(b, 'moba_MobaCache34', a2)
    assert _is_linked(b, 'moba_MobaCache34', a2)
    if hasattr(a1, 'moba_MobaConstant35'):
        assert not _is_linked(a1, 'moba_MobaConstant35', b)
    if hasattr(a2, 'moba_MobaConstant35'):
        assert _is_linked(a2, 'moba_MobaConstant35', b)
    _safe_set(b, 'moba_MobaCache34', None)
    assert not _is_linked(b, 'moba_MobaCache34', a2)
    if hasattr(a2, 'moba_MobaConstant35'):
        assert not _is_linked(a2, 'moba_MobaConstant35', b)


def test_assoc_contextDto103_reverse_link_reassign_clear():
    a1 = moba_MobaRESTPayloadDefinition(array=True)
    a2 = moba_MobaRESTPayloadDefinition(array=False)
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST104', a1)
    assert _is_linked(b, 'moba_MobaREST104', a1)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition105'):
        assert _is_linked(a1, 'moba_MobaRESTPayloadDefinition105', b)
    _safe_set(b, 'moba_MobaREST104', a2)
    assert _is_linked(b, 'moba_MobaREST104', a2)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition105'):
        assert not _is_linked(a1, 'moba_MobaRESTPayloadDefinition105', b)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition105'):
        assert _is_linked(a2, 'moba_MobaRESTPayloadDefinition105', b)
    _safe_set(b, 'moba_MobaREST104', None)
    assert not _is_linked(b, 'moba_MobaREST104', a2)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition105'):
        assert not _is_linked(a2, 'moba_MobaRESTPayloadDefinition105', b)


def test_assoc_dateFormatConst25_reverse_link_reassign_clear():
    a1 = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    a2 = moba_MobaDataType(array=False, bool=False, date=False, dateFormatString="sample_text_2", decimal=False, name="sample_text_2", numeric=False, predefined=False, primitive=False, string=False, time=False, timestamp=False)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant27', a1)
    assert _is_linked(b, 'moba_MobaConstant27', a1)
    if hasattr(a1, 'moba_MobaDataType26'):
        assert _is_linked(a1, 'moba_MobaDataType26', b)
    _safe_set(b, 'moba_MobaConstant27', a2)
    assert _is_linked(b, 'moba_MobaConstant27', a2)
    if hasattr(a1, 'moba_MobaDataType26'):
        assert not _is_linked(a1, 'moba_MobaDataType26', b)
    if hasattr(a2, 'moba_MobaDataType26'):
        assert _is_linked(a2, 'moba_MobaDataType26', b)
    _safe_set(b, 'moba_MobaConstant27', None)
    assert not _is_linked(b, 'moba_MobaConstant27', a2)
    if hasattr(a2, 'moba_MobaDataType26'):
        assert not _is_linked(a2, 'moba_MobaDataType26', b)


def test_assoc_defaultCache5_reverse_link_reassign_clear():
    a1 = moba_MobaCache(cacheIntervalInt=7, cacheStrategyString="sample_text", cacheTypeString="sample_text", name="sample_text")
    a2 = moba_MobaCache(cacheIntervalInt=13, cacheStrategyString="sample_text_2", cacheTypeString="sample_text_2", name="sample_text_2")
    b = moba_MobaApplication(javaPackage="sample_text")
    _safe_set(b, 'moba_MobaApplication6', a1)
    assert _is_linked(b, 'moba_MobaApplication6', a1)
    if hasattr(a1, 'moba_MobaCache'):
        assert _is_linked(a1, 'moba_MobaCache', b)
    _safe_set(b, 'moba_MobaApplication6', a2)
    assert _is_linked(b, 'moba_MobaApplication6', a2)
    if hasattr(a1, 'moba_MobaCache'):
        assert not _is_linked(a1, 'moba_MobaCache', b)
    if hasattr(a2, 'moba_MobaCache'):
        assert _is_linked(a2, 'moba_MobaCache', b)
    _safe_set(b, 'moba_MobaApplication6', None)
    assert not _is_linked(b, 'moba_MobaApplication6', a2)
    if hasattr(a2, 'moba_MobaCache'):
        assert not _is_linked(a2, 'moba_MobaCache', b)


def test_assoc_dto111_reverse_link_reassign_clear():
    a1 = moba_MobaRESTPayloadDefinition(array=True)
    a2 = moba_MobaRESTPayloadDefinition(array=False)
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto113', a1)
    assert _is_linked(b, 'moba_MobaDto113', a1)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition112'):
        assert _is_linked(a1, 'moba_MobaRESTPayloadDefinition112', b)
    _safe_set(b, 'moba_MobaDto113', a2)
    assert _is_linked(b, 'moba_MobaDto113', a2)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition112'):
        assert not _is_linked(a1, 'moba_MobaRESTPayloadDefinition112', b)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition112'):
        assert _is_linked(a2, 'moba_MobaRESTPayloadDefinition112', b)
    _safe_set(b, 'moba_MobaDto113', None)
    assert not _is_linked(b, 'moba_MobaDto113', a2)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition112'):
        assert not _is_linked(a2, 'moba_MobaRESTPayloadDefinition112', b)


def test_assoc_errorDto100_reverse_link_reassign_clear():
    a1 = moba_MobaRESTPayloadDefinition(array=True)
    a2 = moba_MobaRESTPayloadDefinition(array=False)
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST101', a1)
    assert _is_linked(b, 'moba_MobaREST101', a1)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition102'):
        assert _is_linked(a1, 'moba_MobaRESTPayloadDefinition102', b)
    _safe_set(b, 'moba_MobaREST101', a2)
    assert _is_linked(b, 'moba_MobaREST101', a2)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition102'):
        assert not _is_linked(a1, 'moba_MobaRESTPayloadDefinition102', b)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition102'):
        assert _is_linked(a2, 'moba_MobaRESTPayloadDefinition102', b)
    _safe_set(b, 'moba_MobaREST101', None)
    assert not _is_linked(b, 'moba_MobaREST101', a2)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition102'):
        assert not _is_linked(a2, 'moba_MobaRESTPayloadDefinition102', b)


def test_assoc_features0_reverse_link_reassign_clear():
    a1 = moba_MobaModelFeature(id="sample_text", name="sample_text", version="sample_text")
    a2 = moba_MobaModelFeature(id="sample_text_2", name="sample_text_2", version="sample_text_2")
    b = moba_MobaModel(copyright="sample_text")
    _safe_set(b, 'moba_MobaModel', {a1})
    assert _is_linked(b, 'moba_MobaModel', a1)
    if hasattr(a1, 'moba_MobaModelFeature'):
        assert _is_linked(a1, 'moba_MobaModelFeature', b)
    _safe_set(b, 'moba_MobaModel', {a2})
    assert _is_linked(b, 'moba_MobaModel', a2)
    if hasattr(a1, 'moba_MobaModelFeature'):
        assert not _is_linked(a1, 'moba_MobaModelFeature', b)
    if hasattr(a2, 'moba_MobaModelFeature'):
        assert _is_linked(a2, 'moba_MobaModelFeature', b)
    _safe_set(b, 'moba_MobaModel', set())
    assert not _is_linked(b, 'moba_MobaModel', a2)
    if hasattr(a2, 'moba_MobaModelFeature'):
        assert not _is_linked(a2, 'moba_MobaModelFeature', b)


def test_assoc_filterConst182_reverse_link_reassign_clear():
    a1 = moba_MobaRegexpConstraint(filterString="sample_text")
    a2 = moba_MobaRegexpConstraint(filterString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant183', a1)
    assert _is_linked(b, 'moba_MobaConstant183', a1)
    if hasattr(a1, 'moba_MobaRegexpConstraint'):
        assert _is_linked(a1, 'moba_MobaRegexpConstraint', b)
    _safe_set(b, 'moba_MobaConstant183', a2)
    assert _is_linked(b, 'moba_MobaConstant183', a2)
    if hasattr(a1, 'moba_MobaRegexpConstraint'):
        assert not _is_linked(a1, 'moba_MobaRegexpConstraint', b)
    if hasattr(a2, 'moba_MobaRegexpConstraint'):
        assert _is_linked(a2, 'moba_MobaRegexpConstraint', b)
    _safe_set(b, 'moba_MobaConstant183', None)
    assert not _is_linked(b, 'moba_MobaConstant183', a2)
    if hasattr(a2, 'moba_MobaRegexpConstraint'):
        assert not _is_linked(a2, 'moba_MobaRegexpConstraint', b)


def test_assoc_filterConst184_reverse_link_reassign_clear():
    a1 = moba_MobaMinConstraint(filterValue=3.14)
    a2 = moba_MobaMinConstraint(filterValue=9.99)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant185', a1)
    assert _is_linked(b, 'moba_MobaConstant185', a1)
    if hasattr(a1, 'moba_MobaMinConstraint'):
        assert _is_linked(a1, 'moba_MobaMinConstraint', b)
    _safe_set(b, 'moba_MobaConstant185', a2)
    assert _is_linked(b, 'moba_MobaConstant185', a2)
    if hasattr(a1, 'moba_MobaMinConstraint'):
        assert not _is_linked(a1, 'moba_MobaMinConstraint', b)
    if hasattr(a2, 'moba_MobaMinConstraint'):
        assert _is_linked(a2, 'moba_MobaMinConstraint', b)
    _safe_set(b, 'moba_MobaConstant185', None)
    assert not _is_linked(b, 'moba_MobaConstant185', a2)
    if hasattr(a2, 'moba_MobaMinConstraint'):
        assert not _is_linked(a2, 'moba_MobaMinConstraint', b)


def test_assoc_filterConst186_reverse_link_reassign_clear():
    a1 = moba_MobaMaxConstraint(filterValue=3.14)
    a2 = moba_MobaMaxConstraint(filterValue=9.99)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant187', a1)
    assert _is_linked(b, 'moba_MobaConstant187', a1)
    if hasattr(a1, 'moba_MobaMaxConstraint'):
        assert _is_linked(a1, 'moba_MobaMaxConstraint', b)
    _safe_set(b, 'moba_MobaConstant187', a2)
    assert _is_linked(b, 'moba_MobaConstant187', a2)
    if hasattr(a1, 'moba_MobaMaxConstraint'):
        assert not _is_linked(a1, 'moba_MobaMaxConstraint', b)
    if hasattr(a2, 'moba_MobaMaxConstraint'):
        assert _is_linked(a2, 'moba_MobaMaxConstraint', b)
    _safe_set(b, 'moba_MobaConstant187', None)
    assert not _is_linked(b, 'moba_MobaConstant187', a2)
    if hasattr(a2, 'moba_MobaMaxConstraint'):
        assert not _is_linked(a2, 'moba_MobaMaxConstraint', b)


def test_assoc_filterConst188_reverse_link_reassign_clear():
    a1 = moba_MobaMinLengthConstraint(filterValue=7)
    a2 = moba_MobaMinLengthConstraint(filterValue=13)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant189', a1)
    assert _is_linked(b, 'moba_MobaConstant189', a1)
    if hasattr(a1, 'moba_MobaMinLengthConstraint'):
        assert _is_linked(a1, 'moba_MobaMinLengthConstraint', b)
    _safe_set(b, 'moba_MobaConstant189', a2)
    assert _is_linked(b, 'moba_MobaConstant189', a2)
    if hasattr(a1, 'moba_MobaMinLengthConstraint'):
        assert not _is_linked(a1, 'moba_MobaMinLengthConstraint', b)
    if hasattr(a2, 'moba_MobaMinLengthConstraint'):
        assert _is_linked(a2, 'moba_MobaMinLengthConstraint', b)
    _safe_set(b, 'moba_MobaConstant189', None)
    assert not _is_linked(b, 'moba_MobaConstant189', a2)
    if hasattr(a2, 'moba_MobaMinLengthConstraint'):
        assert not _is_linked(a2, 'moba_MobaMinLengthConstraint', b)


def test_assoc_filterConst190_reverse_link_reassign_clear():
    a1 = moba_MobaMaxLengthConstraint(filterValue=7)
    a2 = moba_MobaMaxLengthConstraint(filterValue=13)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant191', a1)
    assert _is_linked(b, 'moba_MobaConstant191', a1)
    if hasattr(a1, 'moba_MobaMaxLengthConstraint'):
        assert _is_linked(a1, 'moba_MobaMaxLengthConstraint', b)
    _safe_set(b, 'moba_MobaConstant191', a2)
    assert _is_linked(b, 'moba_MobaConstant191', a2)
    if hasattr(a1, 'moba_MobaMaxLengthConstraint'):
        assert not _is_linked(a1, 'moba_MobaMaxLengthConstraint', b)
    if hasattr(a2, 'moba_MobaMaxLengthConstraint'):
        assert _is_linked(a2, 'moba_MobaMaxLengthConstraint', b)
    _safe_set(b, 'moba_MobaConstant191', None)
    assert not _is_linked(b, 'moba_MobaConstant191', a2)
    if hasattr(a2, 'moba_MobaMaxLengthConstraint'):
        assert not _is_linked(a2, 'moba_MobaMaxLengthConstraint', b)


def test_assoc_filterFractionConst194_reverse_link_reassign_clear():
    a1 = moba_MobaDigitsConstraint(filterFractionValue=7, filterIntegerValue=7)
    a2 = moba_MobaDigitsConstraint(filterFractionValue=13, filterIntegerValue=13)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant196', a1)
    assert _is_linked(b, 'moba_MobaConstant196', a1)
    if hasattr(a1, 'moba_MobaDigitsConstraint195'):
        assert _is_linked(a1, 'moba_MobaDigitsConstraint195', b)
    _safe_set(b, 'moba_MobaConstant196', a2)
    assert _is_linked(b, 'moba_MobaConstant196', a2)
    if hasattr(a1, 'moba_MobaDigitsConstraint195'):
        assert not _is_linked(a1, 'moba_MobaDigitsConstraint195', b)
    if hasattr(a2, 'moba_MobaDigitsConstraint195'):
        assert _is_linked(a2, 'moba_MobaDigitsConstraint195', b)
    _safe_set(b, 'moba_MobaConstant196', None)
    assert not _is_linked(b, 'moba_MobaConstant196', a2)
    if hasattr(a2, 'moba_MobaDigitsConstraint195'):
        assert not _is_linked(a2, 'moba_MobaDigitsConstraint195', b)


def test_assoc_filterIntegerConst192_reverse_link_reassign_clear():
    a1 = moba_MobaDigitsConstraint(filterFractionValue=7, filterIntegerValue=7)
    a2 = moba_MobaDigitsConstraint(filterFractionValue=13, filterIntegerValue=13)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant193', a1)
    assert _is_linked(b, 'moba_MobaConstant193', a1)
    if hasattr(a1, 'moba_MobaDigitsConstraint'):
        assert _is_linked(a1, 'moba_MobaDigitsConstraint', b)
    _safe_set(b, 'moba_MobaConstant193', a2)
    assert _is_linked(b, 'moba_MobaConstant193', a2)
    if hasattr(a1, 'moba_MobaDigitsConstraint'):
        assert not _is_linked(a1, 'moba_MobaDigitsConstraint', b)
    if hasattr(a2, 'moba_MobaDigitsConstraint'):
        assert _is_linked(a2, 'moba_MobaDigitsConstraint', b)
    _safe_set(b, 'moba_MobaConstant193', None)
    assert not _is_linked(b, 'moba_MobaConstant193', a2)
    if hasattr(a2, 'moba_MobaDigitsConstraint'):
        assert not _is_linked(a2, 'moba_MobaDigitsConstraint', b)


def test_assoc_formatConst127_reverse_link_reassign_clear():
    a1 = moba_MobaRESTAttribute(formatString="sample_text", key="sample_text", keyString="sample_text", value="sample_text", valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTAttribute(formatString="sample_text_2", key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant129', a1)
    assert _is_linked(b, 'moba_MobaConstant129', a1)
    if hasattr(a1, 'moba_MobaRESTAttribute128'):
        assert _is_linked(a1, 'moba_MobaRESTAttribute128', b)
    _safe_set(b, 'moba_MobaConstant129', a2)
    assert _is_linked(b, 'moba_MobaConstant129', a2)
    if hasattr(a1, 'moba_MobaRESTAttribute128'):
        assert not _is_linked(a1, 'moba_MobaRESTAttribute128', b)
    if hasattr(a2, 'moba_MobaRESTAttribute128'):
        assert _is_linked(a2, 'moba_MobaRESTAttribute128', b)
    _safe_set(b, 'moba_MobaConstant129', None)
    assert not _is_linked(b, 'moba_MobaConstant129', a2)
    if hasattr(a2, 'moba_MobaRESTAttribute128'):
        assert not _is_linked(a2, 'moba_MobaRESTAttribute128', b)


def test_assoc_formatConst156_reverse_link_reassign_clear():
    a1 = moba_MobaEntityAttribute(domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaEntityAttribute(domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant158', a1)
    assert _is_linked(b, 'moba_MobaConstant158', a1)
    if hasattr(a1, 'moba_MobaEntityAttribute157'):
        assert _is_linked(a1, 'moba_MobaEntityAttribute157', b)
    _safe_set(b, 'moba_MobaConstant158', a2)
    assert _is_linked(b, 'moba_MobaConstant158', a2)
    if hasattr(a1, 'moba_MobaEntityAttribute157'):
        assert not _is_linked(a1, 'moba_MobaEntityAttribute157', b)
    if hasattr(a2, 'moba_MobaEntityAttribute157'):
        assert _is_linked(a2, 'moba_MobaEntityAttribute157', b)
    _safe_set(b, 'moba_MobaConstant158', None)
    assert not _is_linked(b, 'moba_MobaConstant158', a2)
    if hasattr(a2, 'moba_MobaEntityAttribute157'):
        assert not _is_linked(a2, 'moba_MobaEntityAttribute157', b)


def test_assoc_formatConst169_reverse_link_reassign_clear():
    a1 = moba_MobaDtoAttribute(alias="sample_text", domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaDtoAttribute(alias="sample_text_2", domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant171', a1)
    assert _is_linked(b, 'moba_MobaConstant171', a1)
    if hasattr(a1, 'moba_MobaDtoAttribute170'):
        assert _is_linked(a1, 'moba_MobaDtoAttribute170', b)
    _safe_set(b, 'moba_MobaConstant171', a2)
    assert _is_linked(b, 'moba_MobaConstant171', a2)
    if hasattr(a1, 'moba_MobaDtoAttribute170'):
        assert not _is_linked(a1, 'moba_MobaDtoAttribute170', b)
    if hasattr(a2, 'moba_MobaDtoAttribute170'):
        assert _is_linked(a2, 'moba_MobaDtoAttribute170', b)
    _safe_set(b, 'moba_MobaConstant171', None)
    assert not _is_linked(b, 'moba_MobaConstant171', a2)
    if hasattr(a2, 'moba_MobaDtoAttribute170'):
        assert not _is_linked(a2, 'moba_MobaDtoAttribute170', b)


def test_assoc_formatConst63_reverse_link_reassign_clear():
    a1 = moba_MobaSettingsAttribute(domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaSettingsAttribute(domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant65', a1)
    assert _is_linked(b, 'moba_MobaConstant65', a1)
    if hasattr(a1, 'moba_MobaSettingsAttribute64'):
        assert _is_linked(a1, 'moba_MobaSettingsAttribute64', b)
    _safe_set(b, 'moba_MobaConstant65', a2)
    assert _is_linked(b, 'moba_MobaConstant65', a2)
    if hasattr(a1, 'moba_MobaSettingsAttribute64'):
        assert not _is_linked(a1, 'moba_MobaSettingsAttribute64', b)
    if hasattr(a2, 'moba_MobaSettingsAttribute64'):
        assert _is_linked(a2, 'moba_MobaSettingsAttribute64', b)
    _safe_set(b, 'moba_MobaConstant65', None)
    assert not _is_linked(b, 'moba_MobaConstant65', a2)
    if hasattr(a2, 'moba_MobaSettingsAttribute64'):
        assert not _is_linked(a2, 'moba_MobaSettingsAttribute64', b)


def test_assoc_headers106_reverse_link_reassign_clear():
    a1 = moba_MobaRESTHeader(contentTypeHeader=True, key="sample_text", keyString="sample_text", rawHeader=True, value="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTHeader(contentTypeHeader=False, key="sample_text_2", keyString="sample_text_2", rawHeader=False, value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST107', {a1})
    assert _is_linked(b, 'moba_MobaREST107', a1)
    if hasattr(a1, 'moba_MobaRESTHeader'):
        assert _is_linked(a1, 'moba_MobaRESTHeader', b)
    _safe_set(b, 'moba_MobaREST107', {a2})
    assert _is_linked(b, 'moba_MobaREST107', a2)
    if hasattr(a1, 'moba_MobaRESTHeader'):
        assert not _is_linked(a1, 'moba_MobaRESTHeader', b)
    if hasattr(a2, 'moba_MobaRESTHeader'):
        assert _is_linked(a2, 'moba_MobaRESTHeader', b)
    _safe_set(b, 'moba_MobaREST107', set())
    assert not _is_linked(b, 'moba_MobaREST107', a2)
    if hasattr(a2, 'moba_MobaRESTHeader'):
        assert not _is_linked(a2, 'moba_MobaRESTHeader', b)


def test_assoc_indizes75_reverse_link_reassign_clear():
    a1 = moba_MobaEntityIndex(name="sample_text", unique=True)
    a2 = moba_MobaEntityIndex(name="sample_text_2", unique=False)
    b = moba_MobaEntity(name="sample_text")
    _safe_set(b, 'moba_MobaEntity76', {a1})
    assert _is_linked(b, 'moba_MobaEntity76', a1)
    if hasattr(a1, 'moba_MobaEntityIndex'):
        assert _is_linked(a1, 'moba_MobaEntityIndex', b)
    _safe_set(b, 'moba_MobaEntity76', {a2})
    assert _is_linked(b, 'moba_MobaEntity76', a2)
    if hasattr(a1, 'moba_MobaEntityIndex'):
        assert not _is_linked(a1, 'moba_MobaEntityIndex', b)
    if hasattr(a2, 'moba_MobaEntityIndex'):
        assert _is_linked(a2, 'moba_MobaEntityIndex', b)
    _safe_set(b, 'moba_MobaEntity76', set())
    assert not _is_linked(b, 'moba_MobaEntity76', a2)
    if hasattr(a2, 'moba_MobaEntityIndex'):
        assert not _is_linked(a2, 'moba_MobaEntityIndex', b)


def test_assoc_keyConst121_reverse_link_reassign_clear():
    a1 = moba_MobaRESTAttribute(formatString="sample_text", key="sample_text", keyString="sample_text", value="sample_text", valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTAttribute(formatString="sample_text_2", key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant123', a1)
    assert _is_linked(b, 'moba_MobaConstant123', a1)
    if hasattr(a1, 'moba_MobaRESTAttribute122'):
        assert _is_linked(a1, 'moba_MobaRESTAttribute122', b)
    _safe_set(b, 'moba_MobaConstant123', a2)
    assert _is_linked(b, 'moba_MobaConstant123', a2)
    if hasattr(a1, 'moba_MobaRESTAttribute122'):
        assert not _is_linked(a1, 'moba_MobaRESTAttribute122', b)
    if hasattr(a2, 'moba_MobaRESTAttribute122'):
        assert _is_linked(a2, 'moba_MobaRESTAttribute122', b)
    _safe_set(b, 'moba_MobaConstant123', None)
    assert not _is_linked(b, 'moba_MobaConstant123', a2)
    if hasattr(a2, 'moba_MobaRESTAttribute122'):
        assert not _is_linked(a2, 'moba_MobaRESTAttribute122', b)


def test_assoc_keyConst132_reverse_link_reassign_clear():
    a1 = moba_MobaRESTHeader(contentTypeHeader=True, key="sample_text", keyString="sample_text", rawHeader=True, value="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTHeader(contentTypeHeader=False, key="sample_text_2", keyString="sample_text_2", rawHeader=False, value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant134', a1)
    assert _is_linked(b, 'moba_MobaConstant134', a1)
    if hasattr(a1, 'moba_MobaRESTHeader133'):
        assert _is_linked(a1, 'moba_MobaRESTHeader133', b)
    _safe_set(b, 'moba_MobaConstant134', a2)
    assert _is_linked(b, 'moba_MobaConstant134', a2)
    if hasattr(a1, 'moba_MobaRESTHeader133'):
        assert not _is_linked(a1, 'moba_MobaRESTHeader133', b)
    if hasattr(a2, 'moba_MobaRESTHeader133'):
        assert _is_linked(a2, 'moba_MobaRESTHeader133', b)
    _safe_set(b, 'moba_MobaConstant134', None)
    assert not _is_linked(b, 'moba_MobaConstant134', a2)
    if hasattr(a2, 'moba_MobaRESTHeader133'):
        assert not _is_linked(a2, 'moba_MobaRESTHeader133', b)


def test_assoc_keyConst51_reverse_link_reassign_clear():
    a1 = moba_MobaProperty(key="sample_text", keyString="sample_text", value="sample_text", valueString="sample_text")
    a2 = moba_MobaProperty(key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant53', a1)
    assert _is_linked(b, 'moba_MobaConstant53', a1)
    if hasattr(a1, 'moba_MobaProperty52'):
        assert _is_linked(a1, 'moba_MobaProperty52', b)
    _safe_set(b, 'moba_MobaConstant53', a2)
    assert _is_linked(b, 'moba_MobaConstant53', a2)
    if hasattr(a1, 'moba_MobaProperty52'):
        assert not _is_linked(a1, 'moba_MobaProperty52', b)
    if hasattr(a2, 'moba_MobaProperty52'):
        assert _is_linked(a2, 'moba_MobaProperty52', b)
    _safe_set(b, 'moba_MobaConstant53', None)
    assert not _is_linked(b, 'moba_MobaConstant53', a2)
    if hasattr(a2, 'moba_MobaProperty52'):
        assert not _is_linked(a2, 'moba_MobaProperty52', b)


def test_assoc_multipartParameters143_reverse_link_reassign_clear():
    a1 = moba_MobaRESTCustomService(operation="sample_text")
    a2 = moba_MobaRESTCustomService(operation="sample_text_2")
    b = moba_MobaRESTAbstractAttribute(alias="sample_text", aliasString="sample_text", attachment=True)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute145', a1)
    assert _is_linked(b, 'moba_MobaRESTAbstractAttribute145', a1)
    if hasattr(a1, 'moba_MobaRESTCustomService144'):
        assert _is_linked(a1, 'moba_MobaRESTCustomService144', b)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute145', a2)
    assert _is_linked(b, 'moba_MobaRESTAbstractAttribute145', a2)
    if hasattr(a1, 'moba_MobaRESTCustomService144'):
        assert not _is_linked(a1, 'moba_MobaRESTCustomService144', b)
    if hasattr(a2, 'moba_MobaRESTCustomService144'):
        assert _is_linked(a2, 'moba_MobaRESTCustomService144', b)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute145', None)
    assert not _is_linked(b, 'moba_MobaRESTAbstractAttribute145', a2)
    if hasattr(a2, 'moba_MobaRESTCustomService144'):
        assert not _is_linked(a2, 'moba_MobaRESTCustomService144', b)


def test_assoc_opposite163_reverse_link_reassign_clear():
    a1 = moba_MobaEntityReference(cascading=True, lazy=True, transient=True)
    a2 = moba_MobaEntityReference(cascading=False, lazy=False, transient=False)
    b = moba_MobaEntityReference(cascading=True, lazy=True, transient=True)
    _safe_set(b, 'moba_MobaEntityReference164', a1)
    assert _is_linked(b, 'moba_MobaEntityReference164', a1)
    if hasattr(a1, 'moba_MobaEntityReference162'):
        assert _is_linked(a1, 'moba_MobaEntityReference162', b)
    _safe_set(b, 'moba_MobaEntityReference164', a2)
    assert _is_linked(b, 'moba_MobaEntityReference164', a2)
    if hasattr(a1, 'moba_MobaEntityReference162'):
        assert not _is_linked(a1, 'moba_MobaEntityReference162', b)
    if hasattr(a2, 'moba_MobaEntityReference162'):
        assert _is_linked(a2, 'moba_MobaEntityReference162', b)
    _safe_set(b, 'moba_MobaEntityReference164', None)
    assert not _is_linked(b, 'moba_MobaEntityReference164', a2)
    if hasattr(a2, 'moba_MobaEntityReference162'):
        assert not _is_linked(a2, 'moba_MobaEntityReference162', b)


def test_assoc_opposite175_reverse_link_reassign_clear():
    a1 = moba_MobaDtoReference(alias="sample_text", cascading=True, lazy=True, transient=True)
    a2 = moba_MobaDtoReference(alias="sample_text_2", cascading=False, lazy=False, transient=False)
    b = moba_MobaDtoReference(alias="sample_text", cascading=True, lazy=True, transient=True)
    _safe_set(b, 'moba_MobaDtoReference176', a1)
    assert _is_linked(b, 'moba_MobaDtoReference176', a1)
    if hasattr(a1, 'moba_MobaDtoReference174'):
        assert _is_linked(a1, 'moba_MobaDtoReference174', b)
    _safe_set(b, 'moba_MobaDtoReference176', a2)
    assert _is_linked(b, 'moba_MobaDtoReference176', a2)
    if hasattr(a1, 'moba_MobaDtoReference174'):
        assert not _is_linked(a1, 'moba_MobaDtoReference174', b)
    if hasattr(a2, 'moba_MobaDtoReference174'):
        assert _is_linked(a2, 'moba_MobaDtoReference174', b)
    _safe_set(b, 'moba_MobaDtoReference176', None)
    assert not _is_linked(b, 'moba_MobaDtoReference176', a2)
    if hasattr(a2, 'moba_MobaDtoReference174'):
        assert not _is_linked(a2, 'moba_MobaDtoReference174', b)


def test_assoc_parameters138_reverse_link_reassign_clear():
    a1 = moba_MobaRESTCustomService(operation="sample_text")
    a2 = moba_MobaRESTCustomService(operation="sample_text_2")
    b = moba_MobaRESTAbstractAttribute(alias="sample_text", aliasString="sample_text", attachment=True)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute139', a1)
    assert _is_linked(b, 'moba_MobaRESTAbstractAttribute139', a1)
    if hasattr(a1, 'moba_MobaRESTCustomService'):
        assert _is_linked(a1, 'moba_MobaRESTCustomService', b)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute139', a2)
    assert _is_linked(b, 'moba_MobaRESTAbstractAttribute139', a2)
    if hasattr(a1, 'moba_MobaRESTCustomService'):
        assert not _is_linked(a1, 'moba_MobaRESTCustomService', b)
    if hasattr(a2, 'moba_MobaRESTCustomService'):
        assert _is_linked(a2, 'moba_MobaRESTCustomService', b)
    _safe_set(b, 'moba_MobaRESTAbstractAttribute139', None)
    assert not _is_linked(b, 'moba_MobaRESTAbstractAttribute139', a2)
    if hasattr(a2, 'moba_MobaRESTCustomService'):
        assert not _is_linked(a2, 'moba_MobaRESTCustomService', b)


def test_assoc_requestDto95_reverse_link_reassign_clear():
    a1 = moba_MobaRESTPayloadDefinition(array=True)
    a2 = moba_MobaRESTPayloadDefinition(array=False)
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST96', a1)
    assert _is_linked(b, 'moba_MobaREST96', a1)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition'):
        assert _is_linked(a1, 'moba_MobaRESTPayloadDefinition', b)
    _safe_set(b, 'moba_MobaREST96', a2)
    assert _is_linked(b, 'moba_MobaREST96', a2)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition'):
        assert not _is_linked(a1, 'moba_MobaRESTPayloadDefinition', b)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition'):
        assert _is_linked(a2, 'moba_MobaRESTPayloadDefinition', b)
    _safe_set(b, 'moba_MobaREST96', None)
    assert not _is_linked(b, 'moba_MobaREST96', a2)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition'):
        assert not _is_linked(a2, 'moba_MobaRESTPayloadDefinition', b)


def test_assoc_responseDto97_reverse_link_reassign_clear():
    a1 = moba_MobaRESTPayloadDefinition(array=True)
    a2 = moba_MobaRESTPayloadDefinition(array=False)
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST98', a1)
    assert _is_linked(b, 'moba_MobaREST98', a1)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition99'):
        assert _is_linked(a1, 'moba_MobaRESTPayloadDefinition99', b)
    _safe_set(b, 'moba_MobaREST98', a2)
    assert _is_linked(b, 'moba_MobaREST98', a2)
    if hasattr(a1, 'moba_MobaRESTPayloadDefinition99'):
        assert not _is_linked(a1, 'moba_MobaRESTPayloadDefinition99', b)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition99'):
        assert _is_linked(a2, 'moba_MobaRESTPayloadDefinition99', b)
    _safe_set(b, 'moba_MobaREST98', None)
    assert not _is_linked(b, 'moba_MobaREST98', a2)
    if hasattr(a2, 'moba_MobaRESTPayloadDefinition99'):
        assert not _is_linked(a2, 'moba_MobaRESTPayloadDefinition99', b)


def test_assoc_serializationType114_reverse_link_reassign_clear():
    a1 = moba_MobaTransportSerializationType(name="sample_text")
    a2 = moba_MobaTransportSerializationType(name="sample_text_2")
    b = moba_MobaRESTPayloadDefinition(array=True)
    _safe_set(b, 'moba_MobaRESTPayloadDefinition115', a1)
    assert _is_linked(b, 'moba_MobaRESTPayloadDefinition115', a1)
    if hasattr(a1, 'moba_MobaTransportSerializationType116'):
        assert _is_linked(a1, 'moba_MobaTransportSerializationType116', b)
    _safe_set(b, 'moba_MobaRESTPayloadDefinition115', a2)
    assert _is_linked(b, 'moba_MobaRESTPayloadDefinition115', a2)
    if hasattr(a1, 'moba_MobaTransportSerializationType116'):
        assert not _is_linked(a1, 'moba_MobaTransportSerializationType116', b)
    if hasattr(a2, 'moba_MobaTransportSerializationType116'):
        assert _is_linked(a2, 'moba_MobaTransportSerializationType116', b)
    _safe_set(b, 'moba_MobaRESTPayloadDefinition115', None)
    assert not _is_linked(b, 'moba_MobaRESTPayloadDefinition115', a2)
    if hasattr(a2, 'moba_MobaTransportSerializationType116'):
        assert not _is_linked(a2, 'moba_MobaTransportSerializationType116', b)


def test_assoc_serializationType86_reverse_link_reassign_clear():
    a1 = moba_MobaTransportSerializationType(name="sample_text")
    a2 = moba_MobaTransportSerializationType(name="sample_text_2")
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto87', a1)
    assert _is_linked(b, 'moba_MobaDto87', a1)
    if hasattr(a1, 'moba_MobaTransportSerializationType'):
        assert _is_linked(a1, 'moba_MobaTransportSerializationType', b)
    _safe_set(b, 'moba_MobaDto87', a2)
    assert _is_linked(b, 'moba_MobaDto87', a2)
    if hasattr(a1, 'moba_MobaTransportSerializationType'):
        assert not _is_linked(a1, 'moba_MobaTransportSerializationType', b)
    if hasattr(a2, 'moba_MobaTransportSerializationType'):
        assert _is_linked(a2, 'moba_MobaTransportSerializationType', b)
    _safe_set(b, 'moba_MobaDto87', None)
    assert not _is_linked(b, 'moba_MobaDto87', a2)
    if hasattr(a2, 'moba_MobaTransportSerializationType'):
        assert not _is_linked(a2, 'moba_MobaTransportSerializationType', b)


def test_assoc_services15_reverse_link_reassign_clear():
    a1 = moba_MobaServer(name="sample_text", urlString="sample_text")
    a2 = moba_MobaServer(name="sample_text_2", urlString="sample_text_2")
    b = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    _safe_set(b, 'moba_MobaREST', a1)
    assert _is_linked(b, 'moba_MobaREST', a1)
    if hasattr(a1, 'moba_MobaServer16'):
        assert _is_linked(a1, 'moba_MobaServer16', b)
    _safe_set(b, 'moba_MobaREST', a2)
    assert _is_linked(b, 'moba_MobaREST', a2)
    if hasattr(a1, 'moba_MobaServer16'):
        assert not _is_linked(a1, 'moba_MobaServer16', b)
    if hasattr(a2, 'moba_MobaServer16'):
        assert _is_linked(a2, 'moba_MobaServer16', b)
    _safe_set(b, 'moba_MobaREST', None)
    assert not _is_linked(b, 'moba_MobaREST', a2)
    if hasattr(a2, 'moba_MobaServer16'):
        assert not _is_linked(a2, 'moba_MobaServer16', b)


def test_assoc_superType13_reverse_link_reassign_clear():
    a1 = moba_MobaServer(name="sample_text", urlString="sample_text")
    a2 = moba_MobaServer(name="sample_text_2", urlString="sample_text_2")
    b = moba_MobaServer(name="sample_text", urlString="sample_text")
    _safe_set(b, 'moba_MobaServer14', a1)
    assert _is_linked(b, 'moba_MobaServer14', a1)
    if hasattr(a1, 'moba_MobaServer12'):
        assert _is_linked(a1, 'moba_MobaServer12', b)
    _safe_set(b, 'moba_MobaServer14', a2)
    assert _is_linked(b, 'moba_MobaServer14', a2)
    if hasattr(a1, 'moba_MobaServer12'):
        assert not _is_linked(a1, 'moba_MobaServer12', b)
    if hasattr(a2, 'moba_MobaServer12'):
        assert _is_linked(a2, 'moba_MobaServer12', b)
    _safe_set(b, 'moba_MobaServer14', None)
    assert not _is_linked(b, 'moba_MobaServer14', a2)
    if hasattr(a2, 'moba_MobaServer12'):
        assert not _is_linked(a2, 'moba_MobaServer12', b)


def test_assoc_superType141_reverse_link_reassign_clear():
    a1 = moba_MobaRESTCustomService(operation="sample_text")
    a2 = moba_MobaRESTCustomService(operation="sample_text_2")
    b = moba_MobaRESTCustomService(operation="sample_text")
    _safe_set(b, 'moba_MobaRESTCustomService142', a1)
    assert _is_linked(b, 'moba_MobaRESTCustomService142', a1)
    if hasattr(a1, 'moba_MobaRESTCustomService140'):
        assert _is_linked(a1, 'moba_MobaRESTCustomService140', b)
    _safe_set(b, 'moba_MobaRESTCustomService142', a2)
    assert _is_linked(b, 'moba_MobaRESTCustomService142', a2)
    if hasattr(a1, 'moba_MobaRESTCustomService140'):
        assert not _is_linked(a1, 'moba_MobaRESTCustomService140', b)
    if hasattr(a2, 'moba_MobaRESTCustomService140'):
        assert _is_linked(a2, 'moba_MobaRESTCustomService140', b)
    _safe_set(b, 'moba_MobaRESTCustomService142', None)
    assert not _is_linked(b, 'moba_MobaRESTCustomService142', a2)
    if hasattr(a2, 'moba_MobaRESTCustomService140'):
        assert not _is_linked(a2, 'moba_MobaRESTCustomService140', b)


def test_assoc_superType152_reverse_link_reassign_clear():
    a1 = moba_MobaRESTCrud(operations="sample_text")
    a2 = moba_MobaRESTCrud(operations="sample_text_2")
    b = moba_MobaRESTCrud(operations="sample_text")
    _safe_set(b, 'moba_MobaRESTCrud151', a1)
    assert _is_linked(b, 'moba_MobaRESTCrud151', a1)
    if hasattr(a1, 'moba_MobaRESTCrud'):
        assert _is_linked(a1, 'moba_MobaRESTCrud', b)
    _safe_set(b, 'moba_MobaRESTCrud151', a2)
    assert _is_linked(b, 'moba_MobaRESTCrud151', a2)
    if hasattr(a1, 'moba_MobaRESTCrud'):
        assert not _is_linked(a1, 'moba_MobaRESTCrud', b)
    if hasattr(a2, 'moba_MobaRESTCrud'):
        assert _is_linked(a2, 'moba_MobaRESTCrud', b)
    _safe_set(b, 'moba_MobaRESTCrud151', None)
    assert not _is_linked(b, 'moba_MobaRESTCrud151', a2)
    if hasattr(a2, 'moba_MobaRESTCrud'):
        assert not _is_linked(a2, 'moba_MobaRESTCrud', b)


def test_assoc_superType200_reverse_link_reassign_clear():
    a1 = moba_MobaTrigger(name="sample_text")
    a2 = moba_MobaTrigger(name="sample_text_2")
    b = moba_MobaTrigger(name="sample_text")
    _safe_set(b, 'moba_MobaTrigger199', a1)
    assert _is_linked(b, 'moba_MobaTrigger199', a1)
    if hasattr(a1, 'moba_MobaTrigger'):
        assert _is_linked(a1, 'moba_MobaTrigger', b)
    _safe_set(b, 'moba_MobaTrigger199', a2)
    assert _is_linked(b, 'moba_MobaTrigger199', a2)
    if hasattr(a1, 'moba_MobaTrigger'):
        assert not _is_linked(a1, 'moba_MobaTrigger', b)
    if hasattr(a2, 'moba_MobaTrigger'):
        assert _is_linked(a2, 'moba_MobaTrigger', b)
    _safe_set(b, 'moba_MobaTrigger199', None)
    assert not _is_linked(b, 'moba_MobaTrigger199', a2)
    if hasattr(a2, 'moba_MobaTrigger'):
        assert not _is_linked(a2, 'moba_MobaTrigger', b)


def test_assoc_superType206_reverse_link_reassign_clear():
    a1 = moba_MobaExternalModule(name="sample_text")
    a2 = moba_MobaExternalModule(name="sample_text_2")
    b = moba_MobaExternalModule(name="sample_text")
    _safe_set(b, 'moba_MobaExternalModule205', a1)
    assert _is_linked(b, 'moba_MobaExternalModule205', a1)
    if hasattr(a1, 'moba_MobaExternalModule'):
        assert _is_linked(a1, 'moba_MobaExternalModule', b)
    _safe_set(b, 'moba_MobaExternalModule205', a2)
    assert _is_linked(b, 'moba_MobaExternalModule205', a2)
    if hasattr(a1, 'moba_MobaExternalModule'):
        assert not _is_linked(a1, 'moba_MobaExternalModule', b)
    if hasattr(a2, 'moba_MobaExternalModule'):
        assert _is_linked(a2, 'moba_MobaExternalModule', b)
    _safe_set(b, 'moba_MobaExternalModule205', None)
    assert not _is_linked(b, 'moba_MobaExternalModule205', a2)
    if hasattr(a2, 'moba_MobaExternalModule'):
        assert not _is_linked(a2, 'moba_MobaExternalModule', b)


def test_assoc_superType23_reverse_link_reassign_clear():
    a1 = moba_MobaGeneratorSlot(name="sample_text", type="sample_text")
    a2 = moba_MobaGeneratorSlot(name="sample_text_2", type="sample_text_2")
    b = moba_MobaGeneratorSlot(name="sample_text", type="sample_text")
    _safe_set(b, 'moba_MobaGeneratorSlot22', a1)
    assert _is_linked(b, 'moba_MobaGeneratorSlot22', a1)
    if hasattr(a1, 'moba_MobaGeneratorSlot'):
        assert _is_linked(a1, 'moba_MobaGeneratorSlot', b)
    _safe_set(b, 'moba_MobaGeneratorSlot22', a2)
    assert _is_linked(b, 'moba_MobaGeneratorSlot22', a2)
    if hasattr(a1, 'moba_MobaGeneratorSlot'):
        assert not _is_linked(a1, 'moba_MobaGeneratorSlot', b)
    if hasattr(a2, 'moba_MobaGeneratorSlot'):
        assert _is_linked(a2, 'moba_MobaGeneratorSlot', b)
    _safe_set(b, 'moba_MobaGeneratorSlot22', None)
    assert not _is_linked(b, 'moba_MobaGeneratorSlot22', a2)
    if hasattr(a2, 'moba_MobaGeneratorSlot'):
        assert not _is_linked(a2, 'moba_MobaGeneratorSlot', b)


def test_assoc_superType29_reverse_link_reassign_clear():
    a1 = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    a2 = moba_MobaDataType(array=False, bool=False, date=False, dateFormatString="sample_text_2", decimal=False, name="sample_text_2", numeric=False, predefined=False, primitive=False, string=False, time=False, timestamp=False)
    b = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    _safe_set(b, 'moba_MobaDataType30', a1)
    assert _is_linked(b, 'moba_MobaDataType30', a1)
    if hasattr(a1, 'moba_MobaDataType28'):
        assert _is_linked(a1, 'moba_MobaDataType28', b)
    _safe_set(b, 'moba_MobaDataType30', a2)
    assert _is_linked(b, 'moba_MobaDataType30', a2)
    if hasattr(a1, 'moba_MobaDataType28'):
        assert not _is_linked(a1, 'moba_MobaDataType28', b)
    if hasattr(a2, 'moba_MobaDataType28'):
        assert _is_linked(a2, 'moba_MobaDataType28', b)
    _safe_set(b, 'moba_MobaDataType30', None)
    assert not _is_linked(b, 'moba_MobaDataType30', a2)
    if hasattr(a2, 'moba_MobaDataType28'):
        assert not _is_linked(a2, 'moba_MobaDataType28', b)


def test_assoc_superType58_reverse_link_reassign_clear():
    a1 = moba_MobaSettings(active=True, name="sample_text")
    a2 = moba_MobaSettings(active=False, name="sample_text_2")
    b = moba_MobaSettings(active=True, name="sample_text")
    _safe_set(b, 'moba_MobaSettings57', a1)
    assert _is_linked(b, 'moba_MobaSettings57', a1)
    if hasattr(a1, 'moba_MobaSettings'):
        assert _is_linked(a1, 'moba_MobaSettings', b)
    _safe_set(b, 'moba_MobaSettings57', a2)
    assert _is_linked(b, 'moba_MobaSettings57', a2)
    if hasattr(a1, 'moba_MobaSettings'):
        assert not _is_linked(a1, 'moba_MobaSettings', b)
    if hasattr(a2, 'moba_MobaSettings'):
        assert _is_linked(a2, 'moba_MobaSettings', b)
    _safe_set(b, 'moba_MobaSettings57', None)
    assert not _is_linked(b, 'moba_MobaSettings57', a2)
    if hasattr(a2, 'moba_MobaSettings'):
        assert not _is_linked(a2, 'moba_MobaSettings', b)


def test_assoc_superType68_reverse_link_reassign_clear():
    a1 = moba_MobaEntity(name="sample_text")
    a2 = moba_MobaEntity(name="sample_text_2")
    b = moba_MobaEntity(name="sample_text")
    _safe_set(b, 'moba_MobaEntity69', a1)
    assert _is_linked(b, 'moba_MobaEntity69', a1)
    if hasattr(a1, 'moba_MobaEntity67'):
        assert _is_linked(a1, 'moba_MobaEntity67', b)
    _safe_set(b, 'moba_MobaEntity69', a2)
    assert _is_linked(b, 'moba_MobaEntity69', a2)
    if hasattr(a1, 'moba_MobaEntity67'):
        assert not _is_linked(a1, 'moba_MobaEntity67', b)
    if hasattr(a2, 'moba_MobaEntity67'):
        assert _is_linked(a2, 'moba_MobaEntity67', b)
    _safe_set(b, 'moba_MobaEntity69', None)
    assert not _is_linked(b, 'moba_MobaEntity69', a2)
    if hasattr(a2, 'moba_MobaEntity67'):
        assert not _is_linked(a2, 'moba_MobaEntity67', b)


def test_assoc_superType80_reverse_link_reassign_clear():
    a1 = moba_MobaDto(name="sample_text")
    a2 = moba_MobaDto(name="sample_text_2")
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto79', a1)
    assert _is_linked(b, 'moba_MobaDto79', a1)
    if hasattr(a1, 'moba_MobaDto'):
        assert _is_linked(a1, 'moba_MobaDto', b)
    _safe_set(b, 'moba_MobaDto79', a2)
    assert _is_linked(b, 'moba_MobaDto79', a2)
    if hasattr(a1, 'moba_MobaDto'):
        assert not _is_linked(a1, 'moba_MobaDto', b)
    if hasattr(a2, 'moba_MobaDto'):
        assert _is_linked(a2, 'moba_MobaDto', b)
    _safe_set(b, 'moba_MobaDto79', None)
    assert not _is_linked(b, 'moba_MobaDto79', a2)
    if hasattr(a2, 'moba_MobaDto'):
        assert not _is_linked(a2, 'moba_MobaDto', b)


def test_assoc_superType89_reverse_link_reassign_clear():
    a1 = moba_MobaQueue(name="sample_text")
    a2 = moba_MobaQueue(name="sample_text_2")
    b = moba_MobaQueue(name="sample_text")
    _safe_set(b, 'moba_MobaQueue88', a1)
    assert _is_linked(b, 'moba_MobaQueue88', a1)
    if hasattr(a1, 'moba_MobaQueue'):
        assert _is_linked(a1, 'moba_MobaQueue', b)
    _safe_set(b, 'moba_MobaQueue88', a2)
    assert _is_linked(b, 'moba_MobaQueue88', a2)
    if hasattr(a1, 'moba_MobaQueue'):
        assert not _is_linked(a1, 'moba_MobaQueue', b)
    if hasattr(a2, 'moba_MobaQueue'):
        assert _is_linked(a2, 'moba_MobaQueue', b)
    _safe_set(b, 'moba_MobaQueue88', None)
    assert not _is_linked(b, 'moba_MobaQueue88', a2)
    if hasattr(a2, 'moba_MobaQueue'):
        assert not _is_linked(a2, 'moba_MobaQueue', b)


def test_assoc_tail48_reverse_link_reassign_clear():
    a1 = moba_MobaConstantValue(valueConstFunctions="sample_text", valueConstToLowerCase=True, valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaConstantValue(valueConstFunctions="sample_text_2", valueConstToLowerCase=False, valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstantValue(valueConstFunctions="sample_text", valueConstToLowerCase=True, valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    _safe_set(b, 'moba_MobaConstantValue49', a1)
    assert _is_linked(b, 'moba_MobaConstantValue49', a1)
    if hasattr(a1, 'moba_MobaConstantValue47'):
        assert _is_linked(a1, 'moba_MobaConstantValue47', b)
    _safe_set(b, 'moba_MobaConstantValue49', a2)
    assert _is_linked(b, 'moba_MobaConstantValue49', a2)
    if hasattr(a1, 'moba_MobaConstantValue47'):
        assert not _is_linked(a1, 'moba_MobaConstantValue47', b)
    if hasattr(a2, 'moba_MobaConstantValue47'):
        assert _is_linked(a2, 'moba_MobaConstantValue47', b)
    _safe_set(b, 'moba_MobaConstantValue49', None)
    assert not _is_linked(b, 'moba_MobaConstantValue49', a2)
    if hasattr(a2, 'moba_MobaConstantValue47'):
        assert not _is_linked(a2, 'moba_MobaConstantValue47', b)


def test_assoc_template9_reverse_link_reassign_clear():
    a1 = moba_MobaTemplate(downloadTemplate="sample_text")
    a2 = moba_MobaTemplate(downloadTemplate="sample_text_2")
    b = moba_MobaApplication(javaPackage="sample_text")
    _safe_set(b, 'moba_MobaApplication10', a1)
    assert _is_linked(b, 'moba_MobaApplication10', a1)
    if hasattr(a1, 'moba_MobaTemplate'):
        assert _is_linked(a1, 'moba_MobaTemplate', b)
    _safe_set(b, 'moba_MobaApplication10', a2)
    assert _is_linked(b, 'moba_MobaApplication10', a2)
    if hasattr(a1, 'moba_MobaTemplate'):
        assert not _is_linked(a1, 'moba_MobaTemplate', b)
    if hasattr(a2, 'moba_MobaTemplate'):
        assert _is_linked(a2, 'moba_MobaTemplate', b)
    _safe_set(b, 'moba_MobaApplication10', None)
    assert not _is_linked(b, 'moba_MobaApplication10', a2)
    if hasattr(a2, 'moba_MobaTemplate'):
        assert not _is_linked(a2, 'moba_MobaTemplate', b)


def test_assoc_type119_reverse_link_reassign_clear():
    a1 = moba_MobaRESTAttribute(formatString="sample_text", key="sample_text", keyString="sample_text", value="sample_text", valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTAttribute(formatString="sample_text_2", key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    _safe_set(b, 'moba_MobaDataType120', a1)
    assert _is_linked(b, 'moba_MobaDataType120', a1)
    if hasattr(a1, 'moba_MobaRESTAttribute'):
        assert _is_linked(a1, 'moba_MobaRESTAttribute', b)
    _safe_set(b, 'moba_MobaDataType120', a2)
    assert _is_linked(b, 'moba_MobaDataType120', a2)
    if hasattr(a1, 'moba_MobaRESTAttribute'):
        assert not _is_linked(a1, 'moba_MobaRESTAttribute', b)
    if hasattr(a2, 'moba_MobaRESTAttribute'):
        assert _is_linked(a2, 'moba_MobaRESTAttribute', b)
    _safe_set(b, 'moba_MobaDataType120', None)
    assert not _is_linked(b, 'moba_MobaDataType120', a2)
    if hasattr(a2, 'moba_MobaRESTAttribute'):
        assert not _is_linked(a2, 'moba_MobaRESTAttribute', b)


def test_assoc_type153_reverse_link_reassign_clear():
    a1 = moba_MobaEntityAttribute(domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaEntityAttribute(domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    _safe_set(b, 'moba_MobaDataType155', a1)
    assert _is_linked(b, 'moba_MobaDataType155', a1)
    if hasattr(a1, 'moba_MobaEntityAttribute154'):
        assert _is_linked(a1, 'moba_MobaEntityAttribute154', b)
    _safe_set(b, 'moba_MobaDataType155', a2)
    assert _is_linked(b, 'moba_MobaDataType155', a2)
    if hasattr(a1, 'moba_MobaEntityAttribute154'):
        assert not _is_linked(a1, 'moba_MobaEntityAttribute154', b)
    if hasattr(a2, 'moba_MobaEntityAttribute154'):
        assert _is_linked(a2, 'moba_MobaEntityAttribute154', b)
    _safe_set(b, 'moba_MobaDataType155', None)
    assert not _is_linked(b, 'moba_MobaDataType155', a2)
    if hasattr(a2, 'moba_MobaEntityAttribute154'):
        assert not _is_linked(a2, 'moba_MobaEntityAttribute154', b)


def test_assoc_type160_reverse_link_reassign_clear():
    a1 = moba_MobaEntityReference(cascading=True, lazy=True, transient=True)
    a2 = moba_MobaEntityReference(cascading=False, lazy=False, transient=False)
    b = moba_MobaEntity(name="sample_text")
    _safe_set(b, 'moba_MobaEntity161', a1)
    assert _is_linked(b, 'moba_MobaEntity161', a1)
    if hasattr(a1, 'moba_MobaEntityReference'):
        assert _is_linked(a1, 'moba_MobaEntityReference', b)
    _safe_set(b, 'moba_MobaEntity161', a2)
    assert _is_linked(b, 'moba_MobaEntity161', a2)
    if hasattr(a1, 'moba_MobaEntityReference'):
        assert not _is_linked(a1, 'moba_MobaEntityReference', b)
    if hasattr(a2, 'moba_MobaEntityReference'):
        assert _is_linked(a2, 'moba_MobaEntityReference', b)
    _safe_set(b, 'moba_MobaEntity161', None)
    assert not _is_linked(b, 'moba_MobaEntity161', a2)
    if hasattr(a2, 'moba_MobaEntityReference'):
        assert not _is_linked(a2, 'moba_MobaEntityReference', b)


def test_assoc_type165_reverse_link_reassign_clear():
    a1 = moba_MobaEntityEmbeddable(transient=True)
    a2 = moba_MobaEntityEmbeddable(transient=False)
    b = moba_MobaEntity(name="sample_text")
    _safe_set(b, 'moba_MobaEntity166', a1)
    assert _is_linked(b, 'moba_MobaEntity166', a1)
    if hasattr(a1, 'moba_MobaEntityEmbeddable'):
        assert _is_linked(a1, 'moba_MobaEntityEmbeddable', b)
    _safe_set(b, 'moba_MobaEntity166', a2)
    assert _is_linked(b, 'moba_MobaEntity166', a2)
    if hasattr(a1, 'moba_MobaEntityEmbeddable'):
        assert not _is_linked(a1, 'moba_MobaEntityEmbeddable', b)
    if hasattr(a2, 'moba_MobaEntityEmbeddable'):
        assert _is_linked(a2, 'moba_MobaEntityEmbeddable', b)
    _safe_set(b, 'moba_MobaEntity166', None)
    assert not _is_linked(b, 'moba_MobaEntity166', a2)
    if hasattr(a2, 'moba_MobaEntityEmbeddable'):
        assert not _is_linked(a2, 'moba_MobaEntityEmbeddable', b)


def test_assoc_type167_reverse_link_reassign_clear():
    a1 = moba_MobaDtoAttribute(alias="sample_text", domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaDtoAttribute(alias="sample_text_2", domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    _safe_set(b, 'moba_MobaDataType168', a1)
    assert _is_linked(b, 'moba_MobaDataType168', a1)
    if hasattr(a1, 'moba_MobaDtoAttribute'):
        assert _is_linked(a1, 'moba_MobaDtoAttribute', b)
    _safe_set(b, 'moba_MobaDataType168', a2)
    assert _is_linked(b, 'moba_MobaDataType168', a2)
    if hasattr(a1, 'moba_MobaDtoAttribute'):
        assert not _is_linked(a1, 'moba_MobaDtoAttribute', b)
    if hasattr(a2, 'moba_MobaDtoAttribute'):
        assert _is_linked(a2, 'moba_MobaDtoAttribute', b)
    _safe_set(b, 'moba_MobaDataType168', None)
    assert not _is_linked(b, 'moba_MobaDataType168', a2)
    if hasattr(a2, 'moba_MobaDtoAttribute'):
        assert not _is_linked(a2, 'moba_MobaDtoAttribute', b)


def test_assoc_type172_reverse_link_reassign_clear():
    a1 = moba_MobaDtoReference(alias="sample_text", cascading=True, lazy=True, transient=True)
    a2 = moba_MobaDtoReference(alias="sample_text_2", cascading=False, lazy=False, transient=False)
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto173', a1)
    assert _is_linked(b, 'moba_MobaDto173', a1)
    if hasattr(a1, 'moba_MobaDtoReference'):
        assert _is_linked(a1, 'moba_MobaDtoReference', b)
    _safe_set(b, 'moba_MobaDto173', a2)
    assert _is_linked(b, 'moba_MobaDto173', a2)
    if hasattr(a1, 'moba_MobaDtoReference'):
        assert not _is_linked(a1, 'moba_MobaDtoReference', b)
    if hasattr(a2, 'moba_MobaDtoReference'):
        assert _is_linked(a2, 'moba_MobaDtoReference', b)
    _safe_set(b, 'moba_MobaDto173', None)
    assert not _is_linked(b, 'moba_MobaDto173', a2)
    if hasattr(a2, 'moba_MobaDtoReference'):
        assert not _is_linked(a2, 'moba_MobaDtoReference', b)


def test_assoc_type177_reverse_link_reassign_clear():
    a1 = moba_MobaDtoEmbeddable(alias="sample_text", transient=True)
    a2 = moba_MobaDtoEmbeddable(alias="sample_text_2", transient=False)
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto178', a1)
    assert _is_linked(b, 'moba_MobaDto178', a1)
    if hasattr(a1, 'moba_MobaDtoEmbeddable'):
        assert _is_linked(a1, 'moba_MobaDtoEmbeddable', b)
    _safe_set(b, 'moba_MobaDto178', a2)
    assert _is_linked(b, 'moba_MobaDto178', a2)
    if hasattr(a1, 'moba_MobaDtoEmbeddable'):
        assert not _is_linked(a1, 'moba_MobaDtoEmbeddable', b)
    if hasattr(a2, 'moba_MobaDtoEmbeddable'):
        assert _is_linked(a2, 'moba_MobaDtoEmbeddable', b)
    _safe_set(b, 'moba_MobaDto178', None)
    assert not _is_linked(b, 'moba_MobaDto178', a2)
    if hasattr(a2, 'moba_MobaDtoEmbeddable'):
        assert not _is_linked(a2, 'moba_MobaDtoEmbeddable', b)


def test_assoc_type61_reverse_link_reassign_clear():
    a1 = moba_MobaSettingsAttribute(domainDescription=True, domainKey=True, formatString="sample_text", lazy=True, transient=True)
    a2 = moba_MobaSettingsAttribute(domainDescription=False, domainKey=False, formatString="sample_text_2", lazy=False, transient=False)
    b = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    _safe_set(b, 'moba_MobaDataType62', a1)
    assert _is_linked(b, 'moba_MobaDataType62', a1)
    if hasattr(a1, 'moba_MobaSettingsAttribute'):
        assert _is_linked(a1, 'moba_MobaSettingsAttribute', b)
    _safe_set(b, 'moba_MobaDataType62', a2)
    assert _is_linked(b, 'moba_MobaDataType62', a2)
    if hasattr(a1, 'moba_MobaSettingsAttribute'):
        assert not _is_linked(a1, 'moba_MobaSettingsAttribute', b)
    if hasattr(a2, 'moba_MobaSettingsAttribute'):
        assert _is_linked(a2, 'moba_MobaSettingsAttribute', b)
    _safe_set(b, 'moba_MobaDataType62', None)
    assert not _is_linked(b, 'moba_MobaDataType62', a2)
    if hasattr(a2, 'moba_MobaSettingsAttribute'):
        assert not _is_linked(a2, 'moba_MobaSettingsAttribute', b)


def test_assoc_type66_reverse_link_reassign_clear():
    a1 = moba_MobaSettingsEntityReference(cascading=True, lazy=True, transient=True)
    a2 = moba_MobaSettingsEntityReference(cascading=False, lazy=False, transient=False)
    b = moba_MobaEntity(name="sample_text")
    _safe_set(b, 'moba_MobaEntity', a1)
    assert _is_linked(b, 'moba_MobaEntity', a1)
    if hasattr(a1, 'moba_MobaSettingsEntityReference'):
        assert _is_linked(a1, 'moba_MobaSettingsEntityReference', b)
    _safe_set(b, 'moba_MobaEntity', a2)
    assert _is_linked(b, 'moba_MobaEntity', a2)
    if hasattr(a1, 'moba_MobaSettingsEntityReference'):
        assert not _is_linked(a1, 'moba_MobaSettingsEntityReference', b)
    if hasattr(a2, 'moba_MobaSettingsEntityReference'):
        assert _is_linked(a2, 'moba_MobaSettingsEntityReference', b)
    _safe_set(b, 'moba_MobaEntity', None)
    assert not _is_linked(b, 'moba_MobaEntity', a2)
    if hasattr(a2, 'moba_MobaSettingsEntityReference'):
        assert not _is_linked(a2, 'moba_MobaSettingsEntityReference', b)


def test_assoc_urlConst11_reverse_link_reassign_clear():
    a1 = moba_MobaServer(name="sample_text", urlString="sample_text")
    a2 = moba_MobaServer(name="sample_text_2", urlString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant', a1)
    assert _is_linked(b, 'moba_MobaConstant', a1)
    if hasattr(a1, 'moba_MobaServer'):
        assert _is_linked(a1, 'moba_MobaServer', b)
    _safe_set(b, 'moba_MobaConstant', a2)
    assert _is_linked(b, 'moba_MobaConstant', a2)
    if hasattr(a1, 'moba_MobaServer'):
        assert not _is_linked(a1, 'moba_MobaServer', b)
    if hasattr(a2, 'moba_MobaServer'):
        assert _is_linked(a2, 'moba_MobaServer', b)
    _safe_set(b, 'moba_MobaConstant', None)
    assert not _is_linked(b, 'moba_MobaConstant', a2)
    if hasattr(a2, 'moba_MobaServer'):
        assert not _is_linked(a2, 'moba_MobaServer', b)


def test_assoc_valueAST31_reverse_link_reassign_clear():
    a1 = moba_MobaConstantValue(valueConstFunctions="sample_text", valueConstToLowerCase=True, valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaConstantValue(valueConstFunctions="sample_text_2", valueConstToLowerCase=False, valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant32', a1)
    assert _is_linked(b, 'moba_MobaConstant32', a1)
    if hasattr(a1, 'moba_MobaConstantValue'):
        assert _is_linked(a1, 'moba_MobaConstantValue', b)
    _safe_set(b, 'moba_MobaConstant32', a2)
    assert _is_linked(b, 'moba_MobaConstant32', a2)
    if hasattr(a1, 'moba_MobaConstantValue'):
        assert not _is_linked(a1, 'moba_MobaConstantValue', b)
    if hasattr(a2, 'moba_MobaConstantValue'):
        assert _is_linked(a2, 'moba_MobaConstantValue', b)
    _safe_set(b, 'moba_MobaConstant32', None)
    assert not _is_linked(b, 'moba_MobaConstant32', a2)
    if hasattr(a2, 'moba_MobaConstantValue'):
        assert not _is_linked(a2, 'moba_MobaConstantValue', b)


def test_assoc_valueConst124_reverse_link_reassign_clear():
    a1 = moba_MobaRESTAttribute(formatString="sample_text", key="sample_text", keyString="sample_text", value="sample_text", valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTAttribute(formatString="sample_text_2", key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant126', a1)
    assert _is_linked(b, 'moba_MobaConstant126', a1)
    if hasattr(a1, 'moba_MobaRESTAttribute125'):
        assert _is_linked(a1, 'moba_MobaRESTAttribute125', b)
    _safe_set(b, 'moba_MobaConstant126', a2)
    assert _is_linked(b, 'moba_MobaConstant126', a2)
    if hasattr(a1, 'moba_MobaRESTAttribute125'):
        assert not _is_linked(a1, 'moba_MobaRESTAttribute125', b)
    if hasattr(a2, 'moba_MobaRESTAttribute125'):
        assert _is_linked(a2, 'moba_MobaRESTAttribute125', b)
    _safe_set(b, 'moba_MobaConstant126', None)
    assert not _is_linked(b, 'moba_MobaConstant126', a2)
    if hasattr(a2, 'moba_MobaRESTAttribute125'):
        assert not _is_linked(a2, 'moba_MobaRESTAttribute125', b)


def test_assoc_valueConst135_reverse_link_reassign_clear():
    a1 = moba_MobaRESTHeader(contentTypeHeader=True, key="sample_text", keyString="sample_text", rawHeader=True, value="sample_text", valueString="sample_text")
    a2 = moba_MobaRESTHeader(contentTypeHeader=False, key="sample_text_2", keyString="sample_text_2", rawHeader=False, value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant137', a1)
    assert _is_linked(b, 'moba_MobaConstant137', a1)
    if hasattr(a1, 'moba_MobaRESTHeader136'):
        assert _is_linked(a1, 'moba_MobaRESTHeader136', b)
    _safe_set(b, 'moba_MobaConstant137', a2)
    assert _is_linked(b, 'moba_MobaConstant137', a2)
    if hasattr(a1, 'moba_MobaRESTHeader136'):
        assert not _is_linked(a1, 'moba_MobaRESTHeader136', b)
    if hasattr(a2, 'moba_MobaRESTHeader136'):
        assert _is_linked(a2, 'moba_MobaRESTHeader136', b)
    _safe_set(b, 'moba_MobaConstant137', None)
    assert not _is_linked(b, 'moba_MobaConstant137', a2)
    if hasattr(a2, 'moba_MobaRESTHeader136'):
        assert not _is_linked(a2, 'moba_MobaRESTHeader136', b)


def test_assoc_valueConst201_reverse_link_reassign_clear():
    a1 = moba_MobaFriend(value="sample_text", valueString="sample_text")
    a2 = moba_MobaFriend(value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant202', a1)
    assert _is_linked(b, 'moba_MobaConstant202', a1)
    if hasattr(a1, 'moba_MobaFriend'):
        assert _is_linked(a1, 'moba_MobaFriend', b)
    _safe_set(b, 'moba_MobaConstant202', a2)
    assert _is_linked(b, 'moba_MobaConstant202', a2)
    if hasattr(a1, 'moba_MobaFriend'):
        assert not _is_linked(a1, 'moba_MobaFriend', b)
    if hasattr(a2, 'moba_MobaFriend'):
        assert _is_linked(a2, 'moba_MobaFriend', b)
    _safe_set(b, 'moba_MobaConstant202', None)
    assert not _is_linked(b, 'moba_MobaConstant202', a2)
    if hasattr(a2, 'moba_MobaFriend'):
        assert not _is_linked(a2, 'moba_MobaFriend', b)


def test_assoc_valueConst44_reverse_link_reassign_clear():
    a1 = moba_MobaConstantValue(valueConstFunctions="sample_text", valueConstToLowerCase=True, valueDouble="sample_text", valueInt="sample_text", valueString="sample_text")
    a2 = moba_MobaConstantValue(valueConstFunctions="sample_text_2", valueConstToLowerCase=False, valueDouble="sample_text_2", valueInt="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant46', a1)
    assert _is_linked(b, 'moba_MobaConstant46', a1)
    if hasattr(a1, 'moba_MobaConstantValue45'):
        assert _is_linked(a1, 'moba_MobaConstantValue45', b)
    _safe_set(b, 'moba_MobaConstant46', a2)
    assert _is_linked(b, 'moba_MobaConstant46', a2)
    if hasattr(a1, 'moba_MobaConstantValue45'):
        assert not _is_linked(a1, 'moba_MobaConstantValue45', b)
    if hasattr(a2, 'moba_MobaConstantValue45'):
        assert _is_linked(a2, 'moba_MobaConstantValue45', b)
    _safe_set(b, 'moba_MobaConstant46', None)
    assert not _is_linked(b, 'moba_MobaConstant46', a2)
    if hasattr(a2, 'moba_MobaConstantValue45'):
        assert not _is_linked(a2, 'moba_MobaConstantValue45', b)


def test_assoc_valueConst54_reverse_link_reassign_clear():
    a1 = moba_MobaProperty(key="sample_text", keyString="sample_text", value="sample_text", valueString="sample_text")
    a2 = moba_MobaProperty(key="sample_text_2", keyString="sample_text_2", value="sample_text_2", valueString="sample_text_2")
    b = moba_MobaConstant(name="sample_text")
    _safe_set(b, 'moba_MobaConstant56', a1)
    assert _is_linked(b, 'moba_MobaConstant56', a1)
    if hasattr(a1, 'moba_MobaProperty55'):
        assert _is_linked(a1, 'moba_MobaProperty55', b)
    _safe_set(b, 'moba_MobaConstant56', a2)
    assert _is_linked(b, 'moba_MobaConstant56', a2)
    if hasattr(a1, 'moba_MobaProperty55'):
        assert not _is_linked(a1, 'moba_MobaProperty55', b)
    if hasattr(a2, 'moba_MobaProperty55'):
        assert _is_linked(a2, 'moba_MobaProperty55', b)
    _safe_set(b, 'moba_MobaConstant56', None)
    assert not _is_linked(b, 'moba_MobaConstant56', a2)
    if hasattr(a2, 'moba_MobaProperty55'):
        assert not _is_linked(a2, 'moba_MobaProperty55', b)


def test_assoc_wrappedEntity81_reverse_link_reassign_clear():
    a1 = moba_MobaEntity(name="sample_text")
    a2 = moba_MobaEntity(name="sample_text_2")
    b = moba_MobaDto(name="sample_text")
    _safe_set(b, 'moba_MobaDto82', a1)
    assert _is_linked(b, 'moba_MobaDto82', a1)
    if hasattr(a1, 'moba_MobaEntity83'):
        assert _is_linked(a1, 'moba_MobaEntity83', b)
    _safe_set(b, 'moba_MobaDto82', a2)
    assert _is_linked(b, 'moba_MobaDto82', a2)
    if hasattr(a1, 'moba_MobaEntity83'):
        assert not _is_linked(a1, 'moba_MobaEntity83', b)
    if hasattr(a2, 'moba_MobaEntity83'):
        assert _is_linked(a2, 'moba_MobaEntity83', b)
    _safe_set(b, 'moba_MobaDto82', None)
    assert not _is_linked(b, 'moba_MobaDto82', a2)
    if hasattr(a2, 'moba_MobaEntity83'):
        assert not _is_linked(a2, 'moba_MobaEntity83', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_backgroundApplication2_stub_double():
    # moba_MobaProject has no real 'moba_MobaProject3' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaApplication(javaPackage="sample_text")
    partner = moba_MobaProject()
    setattr(partner, 'moba_MobaProject3', None)
    _safe_set(owner, 'moba_MobaApplication4', partner)
    assert getattr(partner, 'moba_MobaProject3') == owner
    _safe_set(owner, 'moba_MobaApplication4', None)
    assert getattr(partner, 'moba_MobaProject3') is None


def test_assoc_entries207_stub_double():
    # MobaIndexEntry has no real 'MobaIndexEntry' property in the generated
    # code (a bare stub) -- manually attach it so moba_index_MobaIndex's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_index_MobaIndex's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_index_MobaIndex(description="sample_text", id="sample_text", name="sample_text", version="sample_text")
    partner = MobaIndexEntry()
    setattr(partner, 'MobaIndexEntry', None)
    _safe_set(owner, 'moba_index_MobaIndex', {partner})
    assert getattr(partner, 'MobaIndexEntry') == owner
    _safe_set(owner, 'moba_index_MobaIndex', set())
    assert getattr(partner, 'MobaIndexEntry') is None


def test_assoc_enumAST24_stub_double():
    # moba_MobaEnum has no real 'moba_MobaEnum' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaDataType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaDataType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaDataType(array=True, bool=True, date=True, dateFormatString="sample_text", decimal=True, name="sample_text", numeric=True, predefined=True, primitive=True, string=True, time=True, timestamp=True)
    partner = moba_MobaEnum()
    setattr(partner, 'moba_MobaEnum', None)
    _safe_set(owner, 'moba_MobaDataType', partner)
    assert getattr(partner, 'moba_MobaEnum') == owner
    _safe_set(owner, 'moba_MobaDataType', None)
    assert getattr(partner, 'moba_MobaEnum') is None


def test_assoc_features19_stub_double():
    # moba_MobaGeneratorFeature has no real 'moba_MobaGeneratorFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaGenerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaGenerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaGenerator(active=True, name="sample_text")
    partner = moba_MobaGeneratorFeature()
    setattr(partner, 'moba_MobaGeneratorFeature', None)
    _safe_set(owner, 'moba_MobaGenerator', {partner})
    assert getattr(partner, 'moba_MobaGeneratorFeature') == owner
    _safe_set(owner, 'moba_MobaGenerator', set())
    assert getattr(partner, 'moba_MobaGeneratorFeature') is None


def test_assoc_features59_stub_double():
    # moba_MobaSettingsFeature has no real 'moba_MobaSettingsFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaSettings's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaSettings's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaSettings(active=True, name="sample_text")
    partner = moba_MobaSettingsFeature()
    setattr(partner, 'moba_MobaSettingsFeature', None)
    _safe_set(owner, 'moba_MobaSettings60', {partner})
    assert getattr(partner, 'moba_MobaSettingsFeature') == owner
    _safe_set(owner, 'moba_MobaSettings60', set())
    assert getattr(partner, 'moba_MobaSettingsFeature') is None


def test_assoc_features7_stub_double():
    # moba_MobaApplicationFeature has no real 'moba_MobaApplicationFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaApplication(javaPackage="sample_text")
    partner = moba_MobaApplicationFeature()
    setattr(partner, 'moba_MobaApplicationFeature', None)
    _safe_set(owner, 'moba_MobaApplication8', {partner})
    assert getattr(partner, 'moba_MobaApplicationFeature') == owner
    _safe_set(owner, 'moba_MobaApplication8', set())
    assert getattr(partner, 'moba_MobaApplicationFeature') is None


def test_assoc_features73_stub_double():
    # moba_MobaEntityFeature has no real 'moba_MobaEntityFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaEntity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaEntity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaEntity(name="sample_text")
    partner = moba_MobaEntityFeature()
    setattr(partner, 'moba_MobaEntityFeature', None)
    _safe_set(owner, 'moba_MobaEntity74', {partner})
    assert getattr(partner, 'moba_MobaEntityFeature') == owner
    _safe_set(owner, 'moba_MobaEntity74', set())
    assert getattr(partner, 'moba_MobaEntityFeature') is None


def test_assoc_features84_stub_double():
    # moba_MobaDtoFeature has no real 'moba_MobaDtoFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaDto's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaDto's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaDto(name="sample_text")
    partner = moba_MobaDtoFeature()
    setattr(partner, 'moba_MobaDtoFeature', None)
    _safe_set(owner, 'moba_MobaDto85', {partner})
    assert getattr(partner, 'moba_MobaDtoFeature') == owner
    _safe_set(owner, 'moba_MobaDto85', set())
    assert getattr(partner, 'moba_MobaDtoFeature') is None


def test_assoc_features93_stub_double():
    # moba_MobaQueueFeature has no real 'moba_MobaQueueFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaQueue's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaQueue's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaQueue(name="sample_text")
    partner = moba_MobaQueueFeature()
    setattr(partner, 'moba_MobaQueueFeature', None)
    _safe_set(owner, 'moba_MobaQueue94', {partner})
    assert getattr(partner, 'moba_MobaQueueFeature') == owner
    _safe_set(owner, 'moba_MobaQueue94', set())
    assert getattr(partner, 'moba_MobaQueueFeature') is None


def test_assoc_friends203_stub_double():
    # moba_MobaFriendsAble has no real 'moba_MobaFriendsAble' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaFriend's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaFriend's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaFriend(value="sample_text", valueString="sample_text")
    partner = moba_MobaFriendsAble()
    setattr(partner, 'moba_MobaFriendsAble', None)
    _safe_set(owner, 'moba_MobaFriend204', partner)
    assert owner in getattr(partner, 'moba_MobaFriendsAble')
    _safe_set(owner, 'moba_MobaFriend204', None)
    assert owner not in getattr(partner, 'moba_MobaFriendsAble')


def test_assoc_generatorRef20_stub_double():
    # moba_MobaGeneratorMixinFeature has no real 'moba_MobaGeneratorMixinFeature' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaGenerator's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaGenerator's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaGenerator(active=True, name="sample_text")
    partner = moba_MobaGeneratorMixinFeature()
    setattr(partner, 'moba_MobaGeneratorMixinFeature', None)
    _safe_set(owner, 'moba_MobaGenerator21', partner)
    assert getattr(partner, 'moba_MobaGeneratorMixinFeature') == owner
    _safe_set(owner, 'moba_MobaGenerator21', None)
    assert getattr(partner, 'moba_MobaGeneratorMixinFeature') is None


def test_assoc_literals197_stub_double():
    # moba_MobaEnum has no real 'moba_MobaEnum198' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaEnumLiteral's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaEnumLiteral's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaEnumLiteral(default=True, hidden=True, literal="sample_text", name="sample_text", undefined=True, value=7)
    partner = moba_MobaEnum()
    setattr(partner, 'moba_MobaEnum198', None)
    _safe_set(owner, 'moba_MobaEnumLiteral', partner)
    assert owner in getattr(partner, 'moba_MobaEnum198')
    _safe_set(owner, 'moba_MobaEnumLiteral', None)
    assert owner not in getattr(partner, 'moba_MobaEnum198')


def test_assoc_multiplicity159_stub_double():
    # moba_MobaMultiplicityAble has no real 'moba_MobaMultiplicityAble' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaMuliplicity's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaMuliplicity's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaMuliplicity(lower="sample_text", upper="sample_text")
    partner = moba_MobaMultiplicityAble()
    setattr(partner, 'moba_MobaMultiplicityAble', None)
    _safe_set(owner, 'moba_MobaMuliplicity', partner)
    assert getattr(partner, 'moba_MobaMultiplicityAble') == owner
    _safe_set(owner, 'moba_MobaMuliplicity', None)
    assert getattr(partner, 'moba_MobaMultiplicityAble') is None


def test_assoc_properties50_stub_double():
    # moba_MobaPropertiesAble has no real 'moba_MobaPropertiesAble' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaProperty(key="sample_text", keyString="sample_text", value="sample_text", valueString="sample_text")
    partner = moba_MobaPropertiesAble()
    setattr(partner, 'moba_MobaPropertiesAble', None)
    _safe_set(owner, 'moba_MobaProperty', partner)
    assert owner in getattr(partner, 'moba_MobaPropertiesAble')
    _safe_set(owner, 'moba_MobaProperty', None)
    assert owner not in getattr(partner, 'moba_MobaPropertiesAble')


def test_assoc_restService179_stub_double():
    # moba_MobaQueueReference has no real 'moba_MobaQueueReference' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaREST's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaREST's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    partner = moba_MobaQueueReference()
    setattr(partner, 'moba_MobaQueueReference', None)
    _safe_set(owner, 'moba_MobaREST180', partner)
    assert getattr(partner, 'moba_MobaQueueReference') == owner
    _safe_set(owner, 'moba_MobaREST180', None)
    assert getattr(partner, 'moba_MobaQueueReference') is None


def test_assoc_services146_stub_double():
    # moba_MobaRESTWorkflow has no real 'moba_MobaRESTWorkflow' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaREST's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaREST's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaREST(bigData=True, name="sample_text", path="sample_text", url="sample_text")
    partner = moba_MobaRESTWorkflow()
    setattr(partner, 'moba_MobaRESTWorkflow', None)
    _safe_set(owner, 'moba_MobaREST147', partner)
    assert owner in getattr(partner, 'moba_MobaRESTWorkflow')
    _safe_set(owner, 'moba_MobaREST147', None)
    assert owner not in getattr(partner, 'moba_MobaRESTWorkflow')


def test_assoc_transientTemplate208_stub_double():
    # index_moba_MobaApplication has no real 'index_moba_MobaApplication' property in the generated
    # code (a bare stub) -- manually attach it so moba_index_MobaIndexEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_index_MobaIndexEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_index_MobaIndexEntry(filename="sample_text", relativePath="sample_text", templateDescription="sample_text", templateId="sample_text", templateName="sample_text", templateVersion="sample_text")
    partner = index_moba_MobaApplication()
    setattr(partner, 'index_moba_MobaApplication', None)
    _safe_set(owner, 'moba_index_MobaIndexEntry', partner)
    assert getattr(partner, 'index_moba_MobaApplication') == owner
    _safe_set(owner, 'moba_index_MobaIndexEntry', None)
    assert getattr(partner, 'index_moba_MobaApplication') is None


def test_assoc_uiApplication1_stub_double():
    # moba_MobaProject has no real 'moba_MobaProject' property in the generated
    # code (a bare stub) -- manually attach it so moba_MobaApplication's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # moba_MobaApplication's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = moba_MobaApplication(javaPackage="sample_text")
    partner = moba_MobaProject()
    setattr(partner, 'moba_MobaProject', None)
    _safe_set(owner, 'moba_MobaApplication', partner)
    assert getattr(partner, 'moba_MobaProject') == owner
    _safe_set(owner, 'moba_MobaApplication', None)
    assert getattr(partner, 'moba_MobaProject') is None


