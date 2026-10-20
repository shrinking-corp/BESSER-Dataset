from python_code import build_IClosure

def test_build_IClosure___init__():
    assert build_IClosure.__init__(build_IClosure(False, build_IClosure=set()), False, build_IClosure=set()) == None


from python_code import build_IArtifactsPart
from python_code import build_IGenericUnit
from python_code import build_IPathGroup
from python_code import build_IProducedPart
from python_code import build_ResultingPathGroup

def test_build_IPathGroup___init__():
    assert build_IPathGroup.__init__(build_IPathGroup('', '\x00', build_IPathGroup=build_IArtifactsPart(), build_IPathGroup25=build_IProducedPart(), build_IPathGroup37=build_IGenericUnit(), build_IPathGroup32=build_ResultingPathGroup()), '\x00\x00', '', build_IPathGroup=build_IArtifactsPart(), build_IPathGroup25=build_IProducedPart(), build_IPathGroup37=build_IGenericUnit(), build_IPathGroup32=build_ResultingPathGroup()) == None


from python_code import build_IPrerequisites

def test_build_IPrerequisites___init__():
    assert build_IPrerequisites.__init__(build_IPrerequisites('\x00\x00', '', build_IPrerequisites=set()), '', '', build_IPrerequisites=set()) == None


from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BooleanAdvice
from python_code import build_command_BuildUnitCommand
from python_code import build_context_IBuildContext

def test_build_command_BooleanAdvice___init__():
    assert build_command_BooleanAdvice.__init__(build_command_BooleanAdvice(False, IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), False, IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()) == None


from python_code import IFilter
from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BuildUnitCommand
from python_code import build_command_FilterAdvice
from python_code import build_context_IBuildContext

def test_build_command_FilterAdvice___init__():
    assert build_command_FilterAdvice.__init__(build_command_FilterAdvice('', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=IFilter(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(True, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), '', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=IFilter(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()) == None


from python_code import ResolutionOptions
from python_code import build_command_IUnitRequest

def test_build_command_IUnitRequest___init__():
    assert build_command_IUnitRequest.__init__(build_command_IUnitRequest('', '', '\x00\x00', build_command_IUnitRequest=ResolutionOptions()), '', '', '', build_command_IUnitRequest=ResolutionOptions()) == None


from python_code import build_command_InvokeCommand

def test_build_command_InvokeCommand___init__():
    assert build_command_InvokeCommand.__init__(build_command_InvokeCommand(''), '') == None


from python_code import build_command_NewInstanceAdvice

def test_build_command_NewInstanceAdvice___init__():
    assert build_command_NewInstanceAdvice.__init__(build_command_NewInstanceAdvice(''), '') == None


from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BuildUnitCommand
from python_code import build_command_StringAdvice
from python_code import build_context_IBuildContext

def test_build_command_StringAdvice___init__():
    assert build_command_StringAdvice.__init__(build_command_StringAdvice('\x00\x00', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(True, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), '', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()) == None


from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BuildUnitCommand
from python_code import build_command_VersionAdvice
from python_code import build_context_IBuildContext

def test_build_command_VersionAdvice___init__():
    assert build_command_VersionAdvice.__init__(build_command_VersionAdvice('\x00\x00', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(True, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), '', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()) == None


from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BuildUnitCommand
from python_code import build_command_VersionRangeAdvice
from python_code import build_context_IBuildContext

def test_build_command_VersionRangeAdvice___init__():
    assert build_command_VersionRangeAdvice.__init__(build_command_VersionRangeAdvice('\x00\x00', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(True, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), '', IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()) == None


from python_code import IMaterializer
from python_code import build_context_ImportOptions

def test_build_context_ImportOptions___init__():
    assert build_context_ImportOptions.__init__(build_context_ImportOptions('', '', '', False, False, '', build_context_ImportOptions=IMaterializer()), '', '', '\x00', False, False, '', build_context_ImportOptions=IMaterializer()) == None


from python_code import build_context_ResolutionOptions

def test_build_context_ResolutionOptions___init__():
    assert build_context_ResolutionOptions.__init__(build_context_ResolutionOptions('\x00', '', '', '', '', '', False, '', '', '', False), '', '', '', '', '', '', False, '', '', '', False) == None


from python_code import build_filter_IFilter

def test_build_filter_IFilter___init__():
    assert build_filter_IFilter.__init__(build_filter_IFilter()) == None

def test_build_filter_IFilter_match():
    assert build_filter_IFilter.match(build_filter_IFilter(), '', '') == None


from python_code import IFilter
from python_code import build_IClosure
from python_code import build_command_AdviceGroup
from python_code import build_command_BuildUnitCommand
from python_code import build_command_FilterAdvice
from python_code import build_context_IBuildContext
from python_code import build_filter_FilterGroup
from python_code import build_filter_SinglePropertyFilter

def test_build_filter_SinglePropertyFilter___init__():
    assert build_filter_SinglePropertyFilter.__init__(build_filter_SinglePropertyFilter('', IFilter98=build_filter_FilterGroup(), IFilter94=build_command_FilterAdvice('', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=IFilter(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), IFilter=build_command_FilterAdvice('', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=build_filter_FilterGroup(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(True, build_IClosure=set()), IAdvise96=build_command_AdviceGroup())), '', IFilter98=build_filter_FilterGroup(), IFilter94=build_command_FilterAdvice('', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=IFilter(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup()), IFilter=build_command_FilterAdvice('\x00', build_command_FilterAdvice=IFilter(), build_command_FilterAdvice93=IFilter(), IAdvise45=build_context_IBuildContext(), IAdvise87=build_command_BuildUnitCommand(), IAdvise=build_IClosure(False, build_IClosure=set()), IAdvise96=build_command_AdviceGroup())) == None


from python_code import build_properties_Format

def test_build_properties_Format___init__():
    assert build_properties_Format.__init__(build_properties_Format(''), '') == None


from python_code import build_properties_IExpr

def test_build_properties_IExpr___init__():
    assert build_properties_IExpr.__init__(build_properties_IExpr()) == None

def test_build_properties_IExpr_eval():
    assert build_properties_IExpr.eval(build_properties_IExpr(), '') == None


from python_code import IExpr
from python_code import build_properties_IFunction
from python_code import build_properties_Literal
from python_code import build_resolver_IResolver

def test_build_properties_Literal___init__():
    assert build_properties_Literal.__init__(build_properties_Literal('\x00\x00', IExpr=build_resolver_IResolver(False, '', build_resolver_IResolver=IExpr()), IExpr75=build_properties_IFunction()), '', IExpr=build_resolver_IResolver(False, '', build_resolver_IResolver=IExpr()), IExpr75=build_properties_IFunction()) == None


from python_code import build_properties_Match

def test_build_properties_Match___init__():
    assert build_properties_Match.__init__(build_properties_Match('', '', False), '\x00', '', False) == None


from python_code import build_properties_Split

def test_build_properties_Split___init__():
    assert build_properties_Split.__init__(build_properties_Split('', '', 0), '\x00', '', 0) == None


from python_code import build_resolver_IEFSBasedAccess

def test_build_resolver_IEFSBasedAccess___init__():
    assert build_resolver_IEFSBasedAccess.__init__(build_resolver_IEFSBasedAccess()) == None

def test_build_resolver_IEFSBasedAccess_getFileStore():
    assert build_resolver_IEFSBasedAccess.getFileStore(build_resolver_IEFSBasedAccess()) == None


from python_code import build_resolver_IMetaDataTranslator

def test_build_resolver_IMetaDataTranslator___init__():
    assert build_resolver_IMetaDataTranslator.__init__(build_resolver_IMetaDataTranslator()) == None

def test_build_resolver_IMetaDataTranslator_resolve():
    assert build_resolver_IMetaDataTranslator.resolve(build_resolver_IMetaDataTranslator(), '') == None


from python_code import build_resolver_IMetaDataTranslatorFactory

def test_build_resolver_IMetaDataTranslatorFactory___init__():
    assert build_resolver_IMetaDataTranslatorFactory.__init__(build_resolver_IMetaDataTranslatorFactory()) == None

def test_build_resolver_IMetaDataTranslatorFactory_getTranslator():
    assert build_resolver_IMetaDataTranslatorFactory.getTranslator(build_resolver_IMetaDataTranslatorFactory(), '', '') == None


from python_code import IExpr
from python_code import build_resolver_IResolver

def test_build_resolver_IResolver___init__():
    assert build_resolver_IResolver.__init__(build_resolver_IResolver(False, '', build_resolver_IResolver=IExpr()), False, '', build_resolver_IResolver=IExpr()) == None

def test_build_resolver_IResolver_resolve():
    assert build_resolver_IResolver.resolve(build_resolver_IResolver(False, '', build_resolver_IResolver=IExpr()), '\x00\x00') == None


from python_code import build_resolver_IResourceMap

def test_build_resolver_IResourceMap___init__():
    assert build_resolver_IResourceMap.__init__(build_resolver_IResourceMap()) == None

def test_build_resolver_IResourceMap_lookup():
    assert build_resolver_IResourceMap.lookup(build_resolver_IResourceMap(), '') == None


from python_code import build_command_BuildUnitCommand
from python_code import build_context_IBuildContext
from python_code import build_resolver_P2Resolver
from python_code import build_resolver_ResolverGroup
from python_code import build_runtime_ResolverExtension

def test_build_resolver_P2Resolver___init__():
    assert build_resolver_P2Resolver.__init__(build_resolver_P2Resolver(IResolver72=build_resolver_ResolverGroup(), IResolver84=build_command_BuildUnitCommand(), IResolver69=build_runtime_ResolverExtension(), IResolver=build_context_IBuildContext()), IResolver72=build_resolver_ResolverGroup(), IResolver84=build_command_BuildUnitCommand(), IResolver69=build_runtime_ResolverExtension(), IResolver=build_context_IBuildContext()) == None

def test_build_resolver_P2Resolver_resolve():
    assert build_resolver_P2Resolver.resolve(build_resolver_P2Resolver(IResolver72=build_resolver_ResolverGroup(), IResolver84=build_command_BuildUnitCommand(), IResolver69=build_runtime_ResolverExtension(), IResolver=build_context_IBuildContext()), '') == None


from python_code import build_runtime_IHumanSelectable

def test_build_runtime_IHumanSelectable___init__():
    assert build_runtime_IHumanSelectable.__init__(build_runtime_IHumanSelectable('', '\x00'), '\x00\x00', '') == None

