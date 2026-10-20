from python_code import build_AliasedRequiredCapability

def test_build_AliasedRequiredCapability___init__():
    assert build_AliasedRequiredCapability.__init__(build_AliasedRequiredCapability(''), '') == None


from python_code import build_BPropertySet
from python_code import build_BuildConcernContext

def test_build_BuildConcernContext___init__():
    assert build_BuildConcernContext.__init__(build_BuildConcernContext('', build_BuildConcernContext=build_BPropertySet()), '', build_BuildConcernContext=build_BPropertySet()) == None


from python_code import build_BuildUnitRepository

def test_build_BuildUnitRepository___init__():
    assert build_BuildUnitRepository.__init__(build_BuildUnitRepository()) == None

def test_build_BuildUnitRepository_initialize():
    assert build_BuildUnitRepository.initialize(build_BuildUnitRepository(), '', '', '') == None

def test_build_BuildUnitRepository_resolve():
    assert build_BuildUnitRepository.resolve(build_BuildUnitRepository(), '', '', '') == None


from python_code import build_BuilderWrapper

def test_build_BuilderWrapper___init__():
    assert build_BuilderWrapper.__init__(build_BuilderWrapper(False, False, False, True, False, False), False, False, False, False, False, False) == None


from python_code import build_BExpression
from python_code import build_Capability
from python_code import build_EffectiveCapabilityFacade
from python_code import build_IProvidedCapabilityContainer

def test_build_Capability___init__():
    assert build_Capability.__init__(build_Capability('', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()), '', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()) == None

def test_build_Capability_satisfies():
    assert build_Capability.satisfies(build_Capability('', build_Capability=build_BExpression(), build_Capability159=build_IProvidedCapabilityContainer(), build_Capability207=build_EffectiveCapabilityFacade()), 0) == None


from python_code import build_NameSpacePredicate

def test_build_NameSpacePredicate___init__():
    assert build_NameSpacePredicate.__init__(build_NameSpacePredicate(''), '') == None


from python_code import build_ResolutionInfo

def test_build_ResolutionInfo___init__():
    assert build_ResolutionInfo.__init__(build_ResolutionInfo(''), '') == None


from python_code import build_BExpression
from python_code import build_UnitConcernContext

def test_build_UnitConcernContext___init__():
    assert build_UnitConcernContext.__init__(build_UnitConcernContext('', '', build_UnitConcernContext=set(), build_UnitConcernContext95=build_BExpression(), build_UnitConcernContext98=set(), build_UnitConcernContext101=set(), build_UnitConcernContext104=set()), '\x00', '', build_UnitConcernContext=set(), build_UnitConcernContext95=build_BExpression(), build_UnitConcernContext98=set(), build_UnitConcernContext101=set(), build_UnitConcernContext104=set()) == None


from python_code import build_CompoundUnitProvider
from python_code import build_DelegatingUnitProvider
from python_code import build_UnitProvider

def test_build_UnitProvider___init__():
    assert build_UnitProvider.__init__(build_UnitProvider('', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()), '', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()) == None

def test_build_UnitProvider_resolve():
    assert build_UnitProvider.resolve(build_UnitProvider('', build_UnitProvider=build_CompoundUnitProvider(), build_UnitProvider245=build_DelegatingUnitProvider()), 0) == None


from python_code import build_VersionedCapability

def test_build_VersionedCapability___init__():
    assert build_VersionedCapability.__init__(build_VersionedCapability(''), '') == None

