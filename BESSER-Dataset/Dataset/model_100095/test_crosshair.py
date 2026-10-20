from python_code import setup_ApiBaselineTask

def test_setup_ApiBaselineTask___init__():
    assert setup_ApiBaselineTask.__init__(setup_ApiBaselineTask('', '', '\x00\x00'), '', '', '') == None


from python_code import setup_BasicMaterializationTask

def test_setup_BasicMaterializationTask___init__():
    assert setup_BasicMaterializationTask.__init__(setup_BasicMaterializationTask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_BuckminsterImportTask

def test_setup_BuckminsterImportTask___init__():
    assert setup_BuckminsterImportTask.__init__(setup_BuckminsterImportTask(''), '') == None


from python_code import setup_Component
from python_code import setup_MaterializationTask

def test_setup_Component___init__():
    assert setup_Component.__init__(setup_Component('', '', '\x00\x00', setup_Component=setup_MaterializationTask()), '', '', '', setup_Component=setup_MaterializationTask()) == None


from python_code import setup_ComponentDefinition

def test_setup_ComponentDefinition___init__():
    assert setup_ComponentDefinition.__init__(setup_ComponentDefinition('', '\x00'), '\x00\x00', '') == None


from python_code import setup_CompoundSetupTask

def test_setup_CompoundSetupTask___init__():
    assert setup_CompoundSetupTask.__init__(setup_CompoundSetupTask(''), '') == None


from python_code import setup_ContextVariableTask

def test_setup_ContextVariableTask___init__():
    assert setup_ContextVariableTask.__init__(setup_ContextVariableTask('', '', '', False, '', setup_ContextVariableTask=set()), '', '', '', False, '', setup_ContextVariableTask=set()) == None


from python_code import setup_EclipseIniTask

def test_setup_EclipseIniTask___init__():
    assert setup_EclipseIniTask.__init__(setup_EclipseIniTask('', '', False), '\x00', '', False) == None


from python_code import setup_EclipsePreferenceTask

def test_setup_EclipsePreferenceTask___init__():
    assert setup_EclipsePreferenceTask.__init__(setup_EclipsePreferenceTask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_FileAssociationTask

def test_setup_FileAssociationTask___init__():
    assert setup_FileAssociationTask.__init__(setup_FileAssociationTask('\x00\x00', '', setup_FileAssociationTask=set()), '', '', setup_FileAssociationTask=set()) == None


from python_code import setup_FileAssociationsTask
from python_code import setup_FileMapping

def test_setup_FileMapping___init__():
    assert setup_FileMapping.__init__(setup_FileMapping('\x00\x00', '', setup_FileMapping=setup_FileAssociationsTask(), setup_FileMapping57=set()), '', '', setup_FileMapping=setup_FileAssociationsTask(), setup_FileMapping57=set()) == None


from python_code import setup_GitCloneTask

def test_setup_GitCloneTask___init__():
    assert setup_GitCloneTask.__init__(setup_GitCloneTask('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import setup_Index
from python_code import setup_MetaIndex

def test_setup_Index___init__():
    assert setup_Index.__init__(setup_Index('', '', '\x00\x00', setup_Index=setup_MetaIndex()), '', '', '', setup_Index=setup_MetaIndex()) == None


from python_code import setup_JRETask

def test_setup_JRETask___init__():
    assert setup_JRETask.__init__(setup_JRETask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_KeyBindingTask

def test_setup_KeyBindingTask___init__():
    assert setup_KeyBindingTask.__init__(setup_KeyBindingTask('', '', '', '', '\x00', setup_KeyBindingTask=set(), setup_KeyBindingTask63=set()), '', '', '', '', '', setup_KeyBindingTask=set(), setup_KeyBindingTask63=set()) == None


from python_code import setup_LinkLocationTask

def test_setup_LinkLocationTask___init__():
    assert setup_LinkLocationTask.__init__(setup_LinkLocationTask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_ManualSourceLocator

def test_setup_ManualSourceLocator___init__():
    assert setup_ManualSourceLocator.__init__(setup_ManualSourceLocator('', '', '\x00\x00'), '', '', '') == None


from python_code import setup_MylynBuildsTask

def test_setup_MylynBuildsTask___init__():
    assert setup_MylynBuildsTask.__init__(setup_MylynBuildsTask('', '', '', '', setup_MylynBuildsTask=set()), '', '', '', '', setup_MylynBuildsTask=set()) == None


from python_code import setup_MylynQueryTask

def test_setup_MylynQueryTask___init__():
    assert setup_MylynQueryTask.__init__(setup_MylynQueryTask('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import setup_Preferences

def test_setup_Preferences___init__():
    assert setup_Preferences.__init__(setup_Preferences('', '\x00'), '\x00\x00', '') == None


from python_code import setup_ProjectSetImportTask

def test_setup_ProjectSetImportTask___init__():
    assert setup_ProjectSetImportTask.__init__(setup_ProjectSetImportTask(''), '') == None


from python_code import setup_RedirectionTask

def test_setup_RedirectionTask___init__():
    assert setup_RedirectionTask.__init__(setup_RedirectionTask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_ResourceCopyTask

def test_setup_ResourceCopyTask___init__():
    assert setup_ResourceCopyTask.__init__(setup_ResourceCopyTask('', '\x00'), '\x00\x00', '') == None


from python_code import setup_ResourceCreationTask

def test_setup_ResourceCreationTask___init__():
    assert setup_ResourceCreationTask.__init__(setup_ResourceCreationTask('', '', '\x00\x00'), '', '', '') == None


from python_code import setup_ScopeRoot

def test_setup_ScopeRoot___init__():
    assert setup_ScopeRoot.__init__(setup_ScopeRoot()) == None

def test_setup_ScopeRoot_getScope():
    assert setup_ScopeRoot.getScope(setup_ScopeRoot()) == None

def test_setup_ScopeRoot_getParentScopeRoot():
    assert setup_ScopeRoot.getParentScopeRoot(setup_ScopeRoot()) == None


from python_code import setup_TargetPlatformTask

def test_setup_TargetPlatformTask___init__():
    assert setup_TargetPlatformTask.__init__(setup_TargetPlatformTask(''), '') == None

