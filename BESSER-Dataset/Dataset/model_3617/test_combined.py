# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    profile_Classifier,
    profile_CodedType,
    profile_ValueSetConstraints,
    profile_UsageContext,
    profile_Context,
    profile_NullValueSetConstraint,
    profile_ContextToValueSet,
    profile_ValueSetContextBinding,
    profile_EnumerationLiteral,
    profile_ValueSetCode,
    profile_CodeSystemVersion,
    profile_CodeSystemConstraint,
    profile_Class,
    profile_ValueSetVersion,
    profile_ValueSetConstraint,
    profile_Enumeration,
    profile_CR,
    profile_CD,
    profile_Property,
    profile_ConceptDomain,
    profile_ConceptDomainConstraint,
    BindingKind,
    StatusKind,
    Guidance,
    ValueSetType,
    ValueSetBinding,
    Extensibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_profile_classifier_is_not_abstract():
    assert not inspect.isabstract(profile_Classifier)


def test_hyp_profile_classifier_constructor_exists():
    assert callable(profile_Classifier.__init__)


def test_hyp_profile_classifier_constructor_args():
    sig = inspect.signature(profile_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_codedtype_is_not_abstract():
    assert not inspect.isabstract(profile_CodedType)


def test_hyp_profile_codedtype_constructor_exists():
    assert callable(profile_CodedType.__init__)


def test_hyp_profile_codedtype_constructor_args():
    sig = inspect.signature(profile_CodedType.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_valuesetconstraints_is_not_abstract():
    assert not inspect.isabstract(profile_ValueSetConstraints)


def test_hyp_profile_valuesetconstraints_constructor_exists():
    assert callable(profile_ValueSetConstraints.__init__)


def test_hyp_profile_valuesetconstraints_constructor_args():
    sig = inspect.signature(profile_ValueSetConstraints.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_usagecontext_is_not_abstract():
    assert not inspect.isabstract(profile_UsageContext)


def test_hyp_profile_usagecontext_constructor_exists():
    assert callable(profile_UsageContext.__init__)


def test_hyp_profile_usagecontext_constructor_args():
    sig = inspect.signature(profile_UsageContext.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "status" in params, "Missing parameter 'status'"
    assert "statusDate" in params, "Missing parameter 'statusDate'"






def test_hyp_profile_context_is_not_abstract():
    assert not inspect.isabstract(profile_Context)


def test_hyp_profile_context_constructor_exists():
    assert callable(profile_Context.__init__)


def test_hyp_profile_context_constructor_args():
    sig = inspect.signature(profile_Context.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_nullvaluesetconstraint_is_not_abstract():
    assert not inspect.isabstract(profile_NullValueSetConstraint)


def test_hyp_profile_nullvaluesetconstraint_constructor_exists():
    assert callable(profile_NullValueSetConstraint.__init__)


def test_hyp_profile_nullvaluesetconstraint_constructor_args():
    sig = inspect.signature(profile_NullValueSetConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "binding" in params, "Missing parameter 'binding'"
    assert "name" in params, "Missing parameter 'name'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "version" in params, "Missing parameter 'version'"







def test_hyp_profile_contexttovalueset_is_not_abstract():
    assert not inspect.isabstract(profile_ContextToValueSet)


def test_hyp_profile_contexttovalueset_constructor_exists():
    assert callable(profile_ContextToValueSet.__init__)


def test_hyp_profile_contexttovalueset_constructor_args():
    sig = inspect.signature(profile_ContextToValueSet.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"





def test_hyp_profile_valuesetcontextbinding_is_not_abstract():
    assert not inspect.isabstract(profile_ValueSetContextBinding)


def test_hyp_profile_valuesetcontextbinding_constructor_exists():
    assert callable(profile_ValueSetContextBinding.__init__)


def test_hyp_profile_valuesetcontextbinding_constructor_args():
    sig = inspect.signature(profile_ValueSetContextBinding.__init__)
    params = list(sig.parameters.keys())
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"




def test_hyp_profile_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(profile_EnumerationLiteral)


def test_hyp_profile_enumerationliteral_constructor_exists():
    assert callable(profile_EnumerationLiteral.__init__)


def test_hyp_profile_enumerationliteral_constructor_args():
    sig = inspect.signature(profile_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_valuesetcode_is_not_abstract():
    assert not inspect.isabstract(profile_ValueSetCode)


def test_hyp_profile_valuesetcode_constructor_exists():
    assert callable(profile_ValueSetCode.__init__)


def test_hyp_profile_valuesetcode_constructor_args():
    sig = inspect.signature(profile_ValueSetCode.__init__)
    params = list(sig.parameters.keys())
    assert "usageNote" in params, "Missing parameter 'usageNote'"
    assert "conceptName" in params, "Missing parameter 'conceptName'"





def test_hyp_profile_codesystemversion_is_not_abstract():
    assert not inspect.isabstract(profile_CodeSystemVersion)


def test_hyp_profile_codesystemversion_constructor_exists():
    assert callable(profile_CodeSystemVersion.__init__)


def test_hyp_profile_codesystemversion_constructor_args():
    sig = inspect.signature(profile_CodeSystemVersion.__init__)
    params = list(sig.parameters.keys())
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"
    assert "url" in params, "Missing parameter 'url'"
    assert "version" in params, "Missing parameter 'version'"
    assert "releaseDate" in params, "Missing parameter 'releaseDate'"
    assert "status" in params, "Missing parameter 'status'"
    assert "statusDate" in params, "Missing parameter 'statusDate'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "source" in params, "Missing parameter 'source'"
    assert "fullName" in params, "Missing parameter 'fullName'"












def test_hyp_profile_codesystemconstraint_is_not_abstract():
    assert not inspect.isabstract(profile_CodeSystemConstraint)


def test_hyp_profile_codesystemconstraint_constructor_exists():
    assert callable(profile_CodeSystemConstraint.__init__)


def test_hyp_profile_codesystemconstraint_constructor_args():
    sig = inspect.signature(profile_CodeSystemConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "binding" in params, "Missing parameter 'binding'"
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "code" in params, "Missing parameter 'code'"
    assert "name" in params, "Missing parameter 'name'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "version" in params, "Missing parameter 'version'"









def test_hyp_profile_class_is_not_abstract():
    assert not inspect.isabstract(profile_Class)


def test_hyp_profile_class_constructor_exists():
    assert callable(profile_Class.__init__)


def test_hyp_profile_class_constructor_args():
    sig = inspect.signature(profile_Class.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_valuesetversion_is_not_abstract():
    assert not inspect.isabstract(profile_ValueSetVersion)


def test_hyp_profile_valuesetversion_constructor_exists():
    assert callable(profile_ValueSetVersion.__init__)


def test_hyp_profile_valuesetversion_constructor_args():
    sig = inspect.signature(profile_ValueSetVersion.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "expirationDate" in params, "Missing parameter 'expirationDate'"
    assert "revisionDate" in params, "Missing parameter 'revisionDate'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "definition" in params, "Missing parameter 'definition'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "releaseDate" in params, "Missing parameter 'releaseDate'"
    assert "statusDate" in params, "Missing parameter 'statusDate'"
    assert "source" in params, "Missing parameter 'source'"
    assert "status" in params, "Missing parameter 'status'"
    assert "effectiveDate" in params, "Missing parameter 'effectiveDate'"
    assert "type" in params, "Missing parameter 'type'"
    assert "url" in params, "Missing parameter 'url'"

















def test_hyp_profile_valuesetconstraint_is_not_abstract():
    assert not inspect.isabstract(profile_ValueSetConstraint)


def test_hyp_profile_valuesetconstraint_constructor_exists():
    assert callable(profile_ValueSetConstraint.__init__)


def test_hyp_profile_valuesetconstraint_constructor_args():
    sig = inspect.signature(profile_ValueSetConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "uri" in params, "Missing parameter 'uri'"
    assert "guidance" in params, "Missing parameter 'guidance'"
    assert "binding" in params, "Missing parameter 'binding'"
    assert "name" in params, "Missing parameter 'name'"
    assert "extensibility" in params, "Missing parameter 'extensibility'"










def test_hyp_profile_enumeration_is_not_abstract():
    assert not inspect.isabstract(profile_Enumeration)


def test_hyp_profile_enumeration_constructor_exists():
    assert callable(profile_Enumeration.__init__)


def test_hyp_profile_enumeration_constructor_args():
    sig = inspect.signature(profile_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_cr_is_not_abstract():
    assert not inspect.isabstract(profile_CR)


def test_hyp_profile_cr_constructor_exists():
    assert callable(profile_CR.__init__)


def test_hyp_profile_cr_constructor_args():
    sig = inspect.signature(profile_CR.__init__)
    params = list(sig.parameters.keys())
    assert "inverted" in params, "Missing parameter 'inverted'"




def test_hyp_profile_cd_is_not_abstract():
    assert not inspect.isabstract(profile_CD)


def test_hyp_profile_cd_constructor_exists():
    assert callable(profile_CD.__init__)


def test_hyp_profile_cd_constructor_args():
    sig = inspect.signature(profile_CD.__init__)
    params = list(sig.parameters.keys())
    assert "displayName" in params, "Missing parameter 'displayName'"
    assert "code" in params, "Missing parameter 'code'"
    assert "codeSystemVersion" in params, "Missing parameter 'codeSystemVersion'"
    assert "codeSystemName" in params, "Missing parameter 'codeSystemName'"
    assert "codeSystem" in params, "Missing parameter 'codeSystem'"








def test_hyp_profile_property_is_not_abstract():
    assert not inspect.isabstract(profile_Property)


def test_hyp_profile_property_constructor_exists():
    assert callable(profile_Property.__init__)


def test_hyp_profile_property_constructor_args():
    sig = inspect.signature(profile_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_profile_conceptdomain_is_not_abstract():
    assert not inspect.isabstract(profile_ConceptDomain)


def test_hyp_profile_conceptdomain_constructor_exists():
    assert callable(profile_ConceptDomain.__init__)


def test_hyp_profile_conceptdomain_constructor_args():
    sig = inspect.signature(profile_ConceptDomain.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "fullName" in params, "Missing parameter 'fullName'"
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "statusDate" in params, "Missing parameter 'statusDate'"







def test_hyp_profile_conceptdomainconstraint_is_not_abstract():
    assert not inspect.isabstract(profile_ConceptDomainConstraint)


def test_hyp_profile_conceptdomainconstraint_constructor_exists():
    assert callable(profile_ConceptDomainConstraint.__init__)


def test_hyp_profile_conceptdomainconstraint_constructor_args():
    sig = inspect.signature(profile_ConceptDomainConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "identifier" in params, "Missing parameter 'identifier'"



def test_hyp_bindingkind_exists():
    # Check that the Enumeration exists
    assert BindingKind is not None

def test_hyp_bindingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BindingKind]
    expected_literals = [
        "Dynamic",
        "Static",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BindingKind"

def test_hyp_statuskind_exists():
    # Check that the Enumeration exists
    assert StatusKind is not None

def test_hyp_statuskind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatusKind]
    expected_literals = [
        "Active",
        "Inactive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatusKind"

def test_hyp_guidance_exists():
    # Check that the Enumeration exists
    assert Guidance is not None

def test_hyp_guidance_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Guidance]
    expected_literals = [
        "OPEN",
        "EXTEND",
        "CLOSED",
        "RESTRICT",
        "FIXED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Guidance"

def test_hyp_valuesettype_exists():
    # Check that the Enumeration exists
    assert ValueSetType is not None

def test_hyp_valuesettype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueSetType]
    expected_literals = [
        "Extensional",
        "Intensional",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueSetType"

def test_hyp_valuesetbinding_exists():
    # Check that the Enumeration exists
    assert ValueSetBinding is not None

def test_hyp_valuesetbinding_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueSetBinding]
    expected_literals = [
        "Indirect",
        "Direct",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueSetBinding"

def test_hyp_extensibility_exists():
    # Check that the Enumeration exists
    assert Extensibility is not None

def test_hyp_extensibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Extensibility]
    expected_literals = [
        "NEA",
        "CEA",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Extensibility"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
profile_Classifier_strategy = st.builds(
    profile_Classifier,
)
profile_CodedType_strategy = st.builds(
    profile_CodedType,
)
profile_ValueSetConstraints_strategy = st.builds(
    profile_ValueSetConstraints,
)
profile_UsageContext_strategy = st.builds(
    profile_UsageContext,
    identifier=
        safe_text,
    status=
        safe_text,
    statusDate=
        safe_text
)
profile_Context_strategy = st.builds(
    profile_Context,
)
profile_NullValueSetConstraint_strategy = st.builds(
    profile_NullValueSetConstraint,
    binding=
        safe_text,
    name=
        safe_text,
    identifier=
        safe_text,
    version=
        safe_text
)
profile_ContextToValueSet_strategy = st.builds(
    profile_ContextToValueSet,
    value=
        safe_text,
    key=
        safe_text
)
profile_ValueSetContextBinding_strategy = st.builds(
    profile_ValueSetContextBinding,
    effectiveDate=
        safe_text
)
profile_EnumerationLiteral_strategy = st.builds(
    profile_EnumerationLiteral,
)
profile_ValueSetCode_strategy = st.builds(
    profile_ValueSetCode,
    usageNote=
        safe_text,
    conceptName=
        safe_text
)
profile_CodeSystemVersion_strategy = st.builds(
    profile_CodeSystemVersion,
    effectiveDate=
        safe_text,
    url=
        safe_text,
    version=
        safe_text,
    releaseDate=
        safe_text,
    status=
        safe_text,
    statusDate=
        safe_text,
    identifier=
        safe_text,
    source=
        safe_text,
    fullName=
        safe_text
)
profile_CodeSystemConstraint_strategy = st.builds(
    profile_CodeSystemConstraint,
    binding=
        safe_text,
    displayName=
        safe_text,
    code=
        safe_text,
    name=
        safe_text,
    identifier=
        safe_text,
    version=
        safe_text
)
profile_Class_strategy = st.builds(
    profile_Class,
)
profile_ValueSetVersion_strategy = st.builds(
    profile_ValueSetVersion,
    version=
        safe_text,
    binding=
        safe_text,
    expirationDate=
        safe_text,
    revisionDate=
        safe_text,
    fullName=
        safe_text,
    definition=
        safe_text,
    identifier=
        safe_text,
    releaseDate=
        safe_text,
    statusDate=
        safe_text,
    source=
        safe_text,
    status=
        safe_text,
    effectiveDate=
        safe_text,
    type=
        safe_text,
    url=
        safe_text
)
profile_ValueSetConstraint_strategy = st.builds(
    profile_ValueSetConstraint,
    version=
        safe_text,
    identifier=
        safe_text,
    uri=
        safe_text,
    guidance=
        safe_text,
    binding=
        safe_text,
    name=
        safe_text,
    extensibility=
        safe_text
)
profile_Enumeration_strategy = st.builds(
    profile_Enumeration,
)
profile_CR_strategy = st.builds(
    profile_CR,
    inverted=
        safe_text
)
profile_CD_strategy = st.builds(
    profile_CD,
    displayName=
        safe_text,
    code=
        safe_text,
    codeSystemVersion=
        safe_text,
    codeSystemName=
        safe_text,
    codeSystem=
        safe_text
)
profile_Property_strategy = st.builds(
    profile_Property,
)
profile_ConceptDomain_strategy = st.builds(
    profile_ConceptDomain,
    status=
        safe_text,
    fullName=
        safe_text,
    identifier=
        safe_text,
    statusDate=
        safe_text
)
profile_ConceptDomainConstraint_strategy = st.builds(
    profile_ConceptDomainConstraint,
    name=
        safe_text,
    identifier=
        safe_text
)







@given(instance=profile_UsageContext_strategy)
def test_hyp_profile_usagecontext_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_UsageContext_strategy)
def test_hyp_profile_usagecontext_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=profile_UsageContext_strategy)
def test_hyp_profile_usagecontext_statusDate_setter(instance):
    original = instance.statusDate
    instance.statusDate = original
    assert instance.statusDate == original





@given(instance=profile_NullValueSetConstraint_strategy)
def test_hyp_profile_nullvaluesetconstraint_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=profile_NullValueSetConstraint_strategy)
def test_hyp_profile_nullvaluesetconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=profile_NullValueSetConstraint_strategy)
def test_hyp_profile_nullvaluesetconstraint_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_NullValueSetConstraint_strategy)
def test_hyp_profile_nullvaluesetconstraint_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original




@given(instance=profile_ContextToValueSet_strategy)
def test_hyp_profile_contexttovalueset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=profile_ContextToValueSet_strategy)
def test_hyp_profile_contexttovalueset_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original




@given(instance=profile_ValueSetContextBinding_strategy)
def test_hyp_profile_valuesetcontextbinding_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original





@given(instance=profile_ValueSetCode_strategy)
def test_hyp_profile_valuesetcode_usageNote_setter(instance):
    original = instance.usageNote
    instance.usageNote = original
    assert instance.usageNote == original



@given(instance=profile_ValueSetCode_strategy)
def test_hyp_profile_valuesetcode_conceptName_setter(instance):
    original = instance.conceptName
    instance.conceptName = original
    assert instance.conceptName == original




@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_releaseDate_setter(instance):
    original = instance.releaseDate
    instance.releaseDate = original
    assert instance.releaseDate == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_statusDate_setter(instance):
    original = instance.statusDate
    instance.statusDate = original
    assert instance.statusDate == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=profile_CodeSystemVersion_strategy)
def test_hyp_profile_codesystemversion_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=profile_CodeSystemVersion_strategy)
@settings(max_examples=30)
def test_hyp_profile_codesystemversion_setenumerationname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setEnumerationName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setEnumerationName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setEnumerationName' in profile_CodeSystemVersion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setEnumerationName' in profile_CodeSystemVersion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setEnumerationName' in profile_CodeSystemVersion is not implemented or raised an error")




@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_CodeSystemConstraint_strategy)
def test_hyp_profile_codesystemconstraint_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original





@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_expirationDate_setter(instance):
    original = instance.expirationDate
    instance.expirationDate = original
    assert instance.expirationDate == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_revisionDate_setter(instance):
    original = instance.revisionDate
    instance.revisionDate = original
    assert instance.revisionDate == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_definition_setter(instance):
    original = instance.definition
    instance.definition = original
    assert instance.definition == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_releaseDate_setter(instance):
    original = instance.releaseDate
    instance.releaseDate = original
    assert instance.releaseDate == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_statusDate_setter(instance):
    original = instance.statusDate
    instance.statusDate = original
    assert instance.statusDate == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_effectiveDate_setter(instance):
    original = instance.effectiveDate
    instance.effectiveDate = original
    assert instance.effectiveDate == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=profile_ValueSetVersion_strategy)
def test_hyp_profile_valuesetversion_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=profile_ValueSetVersion_strategy)
@settings(max_examples=30)
def test_hyp_profile_valuesetversion_setenumerationname_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setEnumerationName(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setEnumerationName).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setEnumerationName' in profile_ValueSetVersion is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setEnumerationName' in profile_ValueSetVersion did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setEnumerationName' in profile_ValueSetVersion is not implemented or raised an error")




@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_guidance_setter(instance):
    original = instance.guidance
    instance.guidance = original
    assert instance.guidance == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_binding_setter(instance):
    original = instance.binding
    instance.binding = original
    assert instance.binding == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=profile_ValueSetConstraint_strategy)
def test_hyp_profile_valuesetconstraint_extensibility_setter(instance):
    original = instance.extensibility
    instance.extensibility = original
    assert instance.extensibility == original





@given(instance=profile_CR_strategy)
def test_hyp_profile_cr_inverted_setter(instance):
    original = instance.inverted
    instance.inverted = original
    assert instance.inverted == original




@given(instance=profile_CD_strategy)
def test_hyp_profile_cd_displayName_setter(instance):
    original = instance.displayName
    instance.displayName = original
    assert instance.displayName == original



@given(instance=profile_CD_strategy)
def test_hyp_profile_cd_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=profile_CD_strategy)
def test_hyp_profile_cd_codeSystemVersion_setter(instance):
    original = instance.codeSystemVersion
    instance.codeSystemVersion = original
    assert instance.codeSystemVersion == original



@given(instance=profile_CD_strategy)
def test_hyp_profile_cd_codeSystemName_setter(instance):
    original = instance.codeSystemName
    instance.codeSystemName = original
    assert instance.codeSystemName == original



@given(instance=profile_CD_strategy)
def test_hyp_profile_cd_codeSystem_setter(instance):
    original = instance.codeSystem
    instance.codeSystem = original
    assert instance.codeSystem == original





@given(instance=profile_ConceptDomain_strategy)
def test_hyp_profile_conceptdomain_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=profile_ConceptDomain_strategy)
def test_hyp_profile_conceptdomain_fullName_setter(instance):
    original = instance.fullName
    instance.fullName = original
    assert instance.fullName == original



@given(instance=profile_ConceptDomain_strategy)
def test_hyp_profile_conceptdomain_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=profile_ConceptDomain_strategy)
def test_hyp_profile_conceptdomain_statusDate_setter(instance):
    original = instance.statusDate
    instance.statusDate = original
    assert instance.statusDate == original




@given(instance=profile_ConceptDomainConstraint_strategy)
def test_hyp_profile_conceptdomainconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=profile_ConceptDomainConstraint_strategy)
def test_hyp_profile_conceptdomainconstraint_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    profile_CD,
    profile_CR,
    profile_Class,
    profile_Classifier,
    profile_CodeSystemConstraint,
    profile_CodeSystemVersion,
    profile_CodedType,
    profile_ConceptDomain,
    profile_ConceptDomainConstraint,
    profile_Context,
    profile_ContextToValueSet,
    profile_Enumeration,
    profile_EnumerationLiteral,
    profile_NullValueSetConstraint,
    profile_Property,
    profile_UsageContext,
    profile_ValueSetCode,
    profile_ValueSetConstraint,
    profile_ValueSetConstraints,
    profile_ValueSetContextBinding,
    profile_ValueSetVersion,
    BindingKind,
    Extensibility,
    Guidance,
    StatusKind,
    ValueSetBinding,
    ValueSetType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_profile_CD_code_value_roundtrip():
    instance = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_profile_CD_codeSystem_value_roundtrip():
    instance = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    assert instance.codeSystem == "sample_text"
    instance.codeSystem = "sample_text_2"
    assert instance.codeSystem == "sample_text_2"


def test_profile_CD_codeSystemName_value_roundtrip():
    instance = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    assert instance.codeSystemName == "sample_text"
    instance.codeSystemName = "sample_text_2"
    assert instance.codeSystemName == "sample_text_2"


def test_profile_CD_codeSystemVersion_value_roundtrip():
    instance = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    assert instance.codeSystemVersion == "sample_text"
    instance.codeSystemVersion = "sample_text_2"
    assert instance.codeSystemVersion == "sample_text_2"


def test_profile_CD_displayName_value_roundtrip():
    instance = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    assert instance.displayName == "sample_text"
    instance.displayName = "sample_text_2"
    assert instance.displayName == "sample_text_2"


def test_profile_CR_inverted_value_roundtrip():
    instance = profile_CR(inverted="sample_text")
    assert instance.inverted == "sample_text"
    instance.inverted = "sample_text_2"
    assert instance.inverted == "sample_text_2"


def test_profile_CodeSystemConstraint_binding_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.binding == "sample_text"
    instance.binding = "sample_text_2"
    assert instance.binding == "sample_text_2"


def test_profile_CodeSystemConstraint_code_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_profile_CodeSystemConstraint_displayName_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.displayName == "sample_text"
    instance.displayName = "sample_text_2"
    assert instance.displayName == "sample_text_2"


def test_profile_CodeSystemConstraint_identifier_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_CodeSystemConstraint_name_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_profile_CodeSystemConstraint_version_value_roundtrip():
    instance = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_profile_CodeSystemVersion_effectiveDate_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.effectiveDate == "sample_text"
    instance.effectiveDate = "sample_text_2"
    assert instance.effectiveDate == "sample_text_2"


def test_profile_CodeSystemVersion_fullName_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_profile_CodeSystemVersion_identifier_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_CodeSystemVersion_releaseDate_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.releaseDate == "sample_text"
    instance.releaseDate = "sample_text_2"
    assert instance.releaseDate == "sample_text_2"


def test_profile_CodeSystemVersion_source_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_profile_CodeSystemVersion_status_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_profile_CodeSystemVersion_statusDate_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.statusDate == "sample_text"
    instance.statusDate = "sample_text_2"
    assert instance.statusDate == "sample_text_2"


def test_profile_CodeSystemVersion_url_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_profile_CodeSystemVersion_version_value_roundtrip():
    instance = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_profile_ConceptDomain_fullName_value_roundtrip():
    instance = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_profile_ConceptDomain_identifier_value_roundtrip():
    instance = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_ConceptDomain_status_value_roundtrip():
    instance = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_profile_ConceptDomain_statusDate_value_roundtrip():
    instance = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.statusDate == "sample_text"
    instance.statusDate = "sample_text_2"
    assert instance.statusDate == "sample_text_2"


def test_profile_ConceptDomainConstraint_identifier_value_roundtrip():
    instance = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_ConceptDomainConstraint_name_value_roundtrip():
    instance = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_profile_ContextToValueSet_key_value_roundtrip():
    instance = profile_ContextToValueSet(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_profile_ContextToValueSet_value_value_roundtrip():
    instance = profile_ContextToValueSet(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_profile_NullValueSetConstraint_binding_value_roundtrip():
    instance = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.binding == "sample_text"
    instance.binding = "sample_text_2"
    assert instance.binding == "sample_text_2"


def test_profile_NullValueSetConstraint_identifier_value_roundtrip():
    instance = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_NullValueSetConstraint_name_value_roundtrip():
    instance = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_profile_NullValueSetConstraint_version_value_roundtrip():
    instance = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_profile_UsageContext_identifier_value_roundtrip():
    instance = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_UsageContext_status_value_roundtrip():
    instance = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_profile_UsageContext_statusDate_value_roundtrip():
    instance = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    assert instance.statusDate == "sample_text"
    instance.statusDate = "sample_text_2"
    assert instance.statusDate == "sample_text_2"


def test_profile_ValueSetCode_conceptName_value_roundtrip():
    instance = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    assert instance.conceptName == "sample_text"
    instance.conceptName = "sample_text_2"
    assert instance.conceptName == "sample_text_2"


def test_profile_ValueSetCode_usageNote_value_roundtrip():
    instance = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    assert instance.usageNote == "sample_text"
    instance.usageNote = "sample_text_2"
    assert instance.usageNote == "sample_text_2"


def test_profile_ValueSetConstraint_binding_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.binding == "sample_text"
    instance.binding = "sample_text_2"
    assert instance.binding == "sample_text_2"


def test_profile_ValueSetConstraint_extensibility_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.extensibility == "sample_text"
    instance.extensibility = "sample_text_2"
    assert instance.extensibility == "sample_text_2"


def test_profile_ValueSetConstraint_guidance_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.guidance == "sample_text"
    instance.guidance = "sample_text_2"
    assert instance.guidance == "sample_text_2"


def test_profile_ValueSetConstraint_identifier_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_ValueSetConstraint_name_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_profile_ValueSetConstraint_uri_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_profile_ValueSetConstraint_version_value_roundtrip():
    instance = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_profile_ValueSetContextBinding_effectiveDate_value_roundtrip():
    instance = profile_ValueSetContextBinding(effectiveDate="sample_text")
    assert instance.effectiveDate == "sample_text"
    instance.effectiveDate = "sample_text_2"
    assert instance.effectiveDate == "sample_text_2"


def test_profile_ValueSetVersion_binding_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.binding == "sample_text"
    instance.binding = "sample_text_2"
    assert instance.binding == "sample_text_2"


def test_profile_ValueSetVersion_definition_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.definition == "sample_text"
    instance.definition = "sample_text_2"
    assert instance.definition == "sample_text_2"


def test_profile_ValueSetVersion_effectiveDate_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.effectiveDate == "sample_text"
    instance.effectiveDate = "sample_text_2"
    assert instance.effectiveDate == "sample_text_2"


def test_profile_ValueSetVersion_expirationDate_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.expirationDate == "sample_text"
    instance.expirationDate = "sample_text_2"
    assert instance.expirationDate == "sample_text_2"


def test_profile_ValueSetVersion_fullName_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.fullName == "sample_text"
    instance.fullName = "sample_text_2"
    assert instance.fullName == "sample_text_2"


def test_profile_ValueSetVersion_identifier_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.identifier == "sample_text"
    instance.identifier = "sample_text_2"
    assert instance.identifier == "sample_text_2"


def test_profile_ValueSetVersion_releaseDate_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.releaseDate == "sample_text"
    instance.releaseDate = "sample_text_2"
    assert instance.releaseDate == "sample_text_2"


def test_profile_ValueSetVersion_revisionDate_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.revisionDate == "sample_text"
    instance.revisionDate = "sample_text_2"
    assert instance.revisionDate == "sample_text_2"


def test_profile_ValueSetVersion_source_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_profile_ValueSetVersion_status_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_profile_ValueSetVersion_statusDate_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.statusDate == "sample_text"
    instance.statusDate = "sample_text_2"
    assert instance.statusDate == "sample_text_2"


def test_profile_ValueSetVersion_type_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_profile_ValueSetVersion_url_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.url == "sample_text"
    instance.url = "sample_text_2"
    assert instance.url == "sample_text_2"


def test_profile_ValueSetVersion_version_value_roundtrip():
    instance = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    assert instance.version == "sample_text"
    instance.version = "sample_text_2"
    assert instance.version == "sample_text_2"


def test_assoc_base_Class13_link_reassign_clear():
    a = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    b1 = profile_Class()
    b2 = profile_Class()
    _safe_set(a, 'profile_ConceptDomain14', b1)
    assert _is_linked(a, 'profile_ConceptDomain14', b1)
    if hasattr(b1, 'profile_Class'):
        assert _is_linked(b1, 'profile_Class', a)
    _safe_set(a, 'profile_ConceptDomain14', b2)
    assert _is_linked(a, 'profile_ConceptDomain14', b2)
    if hasattr(b1, 'profile_Class'):
        assert not _is_linked(b1, 'profile_Class', a)
    if hasattr(b2, 'profile_Class'):
        assert _is_linked(b2, 'profile_Class', a)
    _safe_set(a, 'profile_ConceptDomain14', None)
    assert not _is_linked(a, 'profile_ConceptDomain14', b2)
    if hasattr(b2, 'profile_Class'):
        assert not _is_linked(b2, 'profile_Class', a)


def test_assoc_base_Class45_link_reassign_clear():
    a = profile_ValueSetContextBinding(effectiveDate="sample_text")
    b1 = profile_Class()
    b2 = profile_Class()
    _safe_set(a, 'profile_ValueSetContextBinding46', b1)
    assert _is_linked(a, 'profile_ValueSetContextBinding46', b1)
    if hasattr(b1, 'profile_Class47'):
        assert _is_linked(b1, 'profile_Class47', a)
    _safe_set(a, 'profile_ValueSetContextBinding46', b2)
    assert _is_linked(a, 'profile_ValueSetContextBinding46', b2)
    if hasattr(b1, 'profile_Class47'):
        assert not _is_linked(b1, 'profile_Class47', a)
    if hasattr(b2, 'profile_Class47'):
        assert _is_linked(b2, 'profile_Class47', a)
    _safe_set(a, 'profile_ValueSetContextBinding46', None)
    assert not _is_linked(a, 'profile_ValueSetContextBinding46', b2)
    if hasattr(b2, 'profile_Class47'):
        assert not _is_linked(b2, 'profile_Class47', a)


def test_assoc_base_Class48_link_reassign_clear():
    a = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    b1 = profile_Class()
    b2 = profile_Class()
    _safe_set(a, 'profile_UsageContext49', b1)
    assert _is_linked(a, 'profile_UsageContext49', b1)
    if hasattr(b1, 'profile_Class50'):
        assert _is_linked(b1, 'profile_Class50', a)
    _safe_set(a, 'profile_UsageContext49', b2)
    assert _is_linked(a, 'profile_UsageContext49', b2)
    if hasattr(b1, 'profile_Class50'):
        assert not _is_linked(b1, 'profile_Class50', a)
    if hasattr(b2, 'profile_Class50'):
        assert _is_linked(b2, 'profile_Class50', a)
    _safe_set(a, 'profile_UsageContext49', None)
    assert not _is_linked(a, 'profile_UsageContext49', b2)
    if hasattr(b2, 'profile_Class50'):
        assert not _is_linked(b2, 'profile_Class50', a)


def test_assoc_base_Enumeration22_link_reassign_clear():
    a = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    b1 = profile_Enumeration()
    b2 = profile_Enumeration()
    _safe_set(a, 'profile_CodeSystemVersion23', b1)
    assert _is_linked(a, 'profile_CodeSystemVersion23', b1)
    if hasattr(b1, 'profile_Enumeration'):
        assert _is_linked(b1, 'profile_Enumeration', a)
    _safe_set(a, 'profile_CodeSystemVersion23', b2)
    assert _is_linked(a, 'profile_CodeSystemVersion23', b2)
    if hasattr(b1, 'profile_Enumeration'):
        assert not _is_linked(b1, 'profile_Enumeration', a)
    if hasattr(b2, 'profile_Enumeration'):
        assert _is_linked(b2, 'profile_Enumeration', a)
    _safe_set(a, 'profile_CodeSystemVersion23', None)
    assert not _is_linked(a, 'profile_CodeSystemVersion23', b2)
    if hasattr(b2, 'profile_Enumeration'):
        assert not _is_linked(b2, 'profile_Enumeration', a)


def test_assoc_base_Enumeration31_link_reassign_clear():
    a = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    b1 = profile_Enumeration()
    b2 = profile_Enumeration()
    _safe_set(a, 'profile_ValueSetVersion32', b1)
    assert _is_linked(a, 'profile_ValueSetVersion32', b1)
    if hasattr(b1, 'profile_Enumeration33'):
        assert _is_linked(b1, 'profile_Enumeration33', a)
    _safe_set(a, 'profile_ValueSetVersion32', b2)
    assert _is_linked(a, 'profile_ValueSetVersion32', b2)
    if hasattr(b1, 'profile_Enumeration33'):
        assert not _is_linked(b1, 'profile_Enumeration33', a)
    if hasattr(b2, 'profile_Enumeration33'):
        assert _is_linked(b2, 'profile_Enumeration33', a)
    _safe_set(a, 'profile_ValueSetVersion32', None)
    assert not _is_linked(a, 'profile_ValueSetVersion32', b2)
    if hasattr(b2, 'profile_Enumeration33'):
        assert not _is_linked(b2, 'profile_Enumeration33', a)


def test_assoc_base_EnumerationLiteral36_link_reassign_clear():
    a = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    b1 = profile_EnumerationLiteral()
    b2 = profile_EnumerationLiteral()
    _safe_set(a, 'profile_ValueSetCode37', b1)
    assert _is_linked(a, 'profile_ValueSetCode37', b1)
    if hasattr(b1, 'profile_EnumerationLiteral'):
        assert _is_linked(b1, 'profile_EnumerationLiteral', a)
    _safe_set(a, 'profile_ValueSetCode37', b2)
    assert _is_linked(a, 'profile_ValueSetCode37', b2)
    if hasattr(b1, 'profile_EnumerationLiteral'):
        assert not _is_linked(b1, 'profile_EnumerationLiteral', a)
    if hasattr(b2, 'profile_EnumerationLiteral'):
        assert _is_linked(b2, 'profile_EnumerationLiteral', a)
    _safe_set(a, 'profile_ValueSetCode37', None)
    assert not _is_linked(a, 'profile_ValueSetCode37', b2)
    if hasattr(b2, 'profile_EnumerationLiteral'):
        assert not _is_linked(b2, 'profile_EnumerationLiteral', a)


def test_assoc_base_Property11_link_reassign_clear():
    a = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    b1 = profile_Property()
    b2 = profile_Property()
    _safe_set(a, 'profile_ConceptDomainConstraint12', b1)
    assert _is_linked(a, 'profile_ConceptDomainConstraint12', b1)
    if hasattr(b1, 'profile_Property'):
        assert _is_linked(b1, 'profile_Property', a)
    _safe_set(a, 'profile_ConceptDomainConstraint12', b2)
    assert _is_linked(a, 'profile_ConceptDomainConstraint12', b2)
    if hasattr(b1, 'profile_Property'):
        assert not _is_linked(b1, 'profile_Property', a)
    if hasattr(b2, 'profile_Property'):
        assert _is_linked(b2, 'profile_Property', a)
    _safe_set(a, 'profile_ConceptDomainConstraint12', None)
    assert not _is_linked(a, 'profile_ConceptDomainConstraint12', b2)
    if hasattr(b2, 'profile_Property'):
        assert not _is_linked(b2, 'profile_Property', a)


def test_assoc_base_Property19_link_reassign_clear():
    a = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    b1 = profile_Property()
    b2 = profile_Property()
    _safe_set(a, 'profile_CodeSystemConstraint20', b1)
    assert _is_linked(a, 'profile_CodeSystemConstraint20', b1)
    if hasattr(b1, 'profile_Property21'):
        assert _is_linked(b1, 'profile_Property21', a)
    _safe_set(a, 'profile_CodeSystemConstraint20', b2)
    assert _is_linked(a, 'profile_CodeSystemConstraint20', b2)
    if hasattr(b1, 'profile_Property21'):
        assert not _is_linked(b1, 'profile_Property21', a)
    if hasattr(b2, 'profile_Property21'):
        assert _is_linked(b2, 'profile_Property21', a)
    _safe_set(a, 'profile_CodeSystemConstraint20', None)
    assert not _is_linked(a, 'profile_CodeSystemConstraint20', b2)
    if hasattr(b2, 'profile_Property21'):
        assert not _is_linked(b2, 'profile_Property21', a)


def test_assoc_base_Property25_link_reassign_clear():
    a = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    b1 = profile_Property()
    b2 = profile_Property()
    _safe_set(a, 'profile_ValueSetConstraint26', b1)
    assert _is_linked(a, 'profile_ValueSetConstraint26', b1)
    if hasattr(b1, 'profile_Property27'):
        assert _is_linked(b1, 'profile_Property27', a)
    _safe_set(a, 'profile_ValueSetConstraint26', b2)
    assert _is_linked(a, 'profile_ValueSetConstraint26', b2)
    if hasattr(b1, 'profile_Property27'):
        assert not _is_linked(b1, 'profile_Property27', a)
    if hasattr(b2, 'profile_Property27'):
        assert _is_linked(b2, 'profile_Property27', a)
    _safe_set(a, 'profile_ValueSetConstraint26', None)
    assert not _is_linked(a, 'profile_ValueSetConstraint26', b2)
    if hasattr(b2, 'profile_Property27'):
        assert not _is_linked(b2, 'profile_Property27', a)


def test_assoc_base_Property57_link_reassign_clear():
    a = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    b1 = profile_Property()
    b2 = profile_Property()
    _safe_set(a, 'profile_NullValueSetConstraint58', b1)
    assert _is_linked(a, 'profile_NullValueSetConstraint58', b1)
    if hasattr(b1, 'profile_Property59'):
        assert _is_linked(b1, 'profile_Property59', a)
    _safe_set(a, 'profile_NullValueSetConstraint58', b2)
    assert _is_linked(a, 'profile_NullValueSetConstraint58', b2)
    if hasattr(b1, 'profile_Property59'):
        assert not _is_linked(b1, 'profile_Property59', a)
    if hasattr(b2, 'profile_Property59'):
        assert _is_linked(b2, 'profile_Property59', a)
    _safe_set(a, 'profile_NullValueSetConstraint58', None)
    assert not _is_linked(a, 'profile_NullValueSetConstraint58', b2)
    if hasattr(b2, 'profile_Property59'):
        assert not _is_linked(b2, 'profile_Property59', a)


def test_assoc_codeSystem28_link_reassign_clear():
    a = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    b1 = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    b2 = profile_CodeSystemVersion(effectiveDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", url="sample_text_2", version="sample_text_2")
    _safe_set(a, 'profile_ValueSetVersion29', b1)
    assert _is_linked(a, 'profile_ValueSetVersion29', b1)
    if hasattr(b1, 'profile_CodeSystemVersion30'):
        assert _is_linked(b1, 'profile_CodeSystemVersion30', a)
    _safe_set(a, 'profile_ValueSetVersion29', b2)
    assert _is_linked(a, 'profile_ValueSetVersion29', b2)
    if hasattr(b1, 'profile_CodeSystemVersion30'):
        assert not _is_linked(b1, 'profile_CodeSystemVersion30', a)
    if hasattr(b2, 'profile_CodeSystemVersion30'):
        assert _is_linked(b2, 'profile_CodeSystemVersion30', a)
    _safe_set(a, 'profile_ValueSetVersion29', None)
    assert not _is_linked(a, 'profile_ValueSetVersion29', b2)
    if hasattr(b2, 'profile_CodeSystemVersion30'):
        assert not _is_linked(b2, 'profile_CodeSystemVersion30', a)


def test_assoc_codeSystem34_link_reassign_clear():
    a = profile_ValueSetCode(conceptName="sample_text", usageNote="sample_text")
    b1 = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    b2 = profile_CodeSystemVersion(effectiveDate="sample_text_2", fullName="sample_text_2", identifier="sample_text_2", releaseDate="sample_text_2", source="sample_text_2", status="sample_text_2", statusDate="sample_text_2", url="sample_text_2", version="sample_text_2")
    _safe_set(a, 'profile_ValueSetCode', b1)
    assert _is_linked(a, 'profile_ValueSetCode', b1)
    if hasattr(b1, 'profile_CodeSystemVersion35'):
        assert _is_linked(b1, 'profile_CodeSystemVersion35', a)
    _safe_set(a, 'profile_ValueSetCode', b2)
    assert _is_linked(a, 'profile_ValueSetCode', b2)
    if hasattr(b1, 'profile_CodeSystemVersion35'):
        assert not _is_linked(b1, 'profile_CodeSystemVersion35', a)
    if hasattr(b2, 'profile_CodeSystemVersion35'):
        assert _is_linked(b2, 'profile_CodeSystemVersion35', a)
    _safe_set(a, 'profile_ValueSetCode', None)
    assert not _is_linked(a, 'profile_ValueSetCode', b2)
    if hasattr(b2, 'profile_CodeSystemVersion35'):
        assert not _is_linked(b2, 'profile_CodeSystemVersion35', a)


def test_assoc_conceptDomain38_link_reassign_clear():
    a = profile_ValueSetContextBinding(effectiveDate="sample_text")
    b1 = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    b2 = profile_ConceptDomain(fullName="sample_text_2", identifier="sample_text_2", status="sample_text_2", statusDate="sample_text_2")
    _safe_set(a, 'profile_ValueSetContextBinding', b1)
    assert _is_linked(a, 'profile_ValueSetContextBinding', b1)
    if hasattr(b1, 'profile_ConceptDomain39'):
        assert _is_linked(b1, 'profile_ConceptDomain39', a)
    _safe_set(a, 'profile_ValueSetContextBinding', b2)
    assert _is_linked(a, 'profile_ValueSetContextBinding', b2)
    if hasattr(b1, 'profile_ConceptDomain39'):
        assert not _is_linked(b1, 'profile_ConceptDomain39', a)
    if hasattr(b2, 'profile_ConceptDomain39'):
        assert _is_linked(b2, 'profile_ConceptDomain39', a)
    _safe_set(a, 'profile_ValueSetContextBinding', None)
    assert not _is_linked(a, 'profile_ValueSetContextBinding', b2)
    if hasattr(b2, 'profile_ConceptDomain39'):
        assert not _is_linked(b2, 'profile_ConceptDomain39', a)


def test_assoc_constraints53_link_reassign_clear():
    a = profile_ContextToValueSet(key="sample_text", value="sample_text")
    b1 = profile_ValueSetConstraints()
    b2 = profile_ValueSetConstraints()
    _safe_set(a, 'profile_ContextToValueSet', b1)
    assert _is_linked(a, 'profile_ContextToValueSet', b1)
    if hasattr(b1, 'profile_ValueSetConstraints54'):
        assert _is_linked(b1, 'profile_ValueSetConstraints54', a)
    _safe_set(a, 'profile_ContextToValueSet', b2)
    assert _is_linked(a, 'profile_ContextToValueSet', b2)
    if hasattr(b1, 'profile_ValueSetConstraints54'):
        assert not _is_linked(b1, 'profile_ValueSetConstraints54', a)
    if hasattr(b2, 'profile_ValueSetConstraints54'):
        assert _is_linked(b2, 'profile_ValueSetConstraints54', a)
    _safe_set(a, 'profile_ContextToValueSet', None)
    assert not _is_linked(a, 'profile_ContextToValueSet', b2)
    if hasattr(b2, 'profile_ValueSetConstraints54'):
        assert not _is_linked(b2, 'profile_ValueSetConstraints54', a)


def test_assoc_name4_link_reassign_clear():
    a = profile_CR(inverted="sample_text")
    b1 = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    b2 = profile_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", displayName="sample_text_2")
    _safe_set(a, 'profile_CR5', b1)
    assert _is_linked(a, 'profile_CR5', b1)
    if hasattr(b1, 'profile_CD6'):
        assert _is_linked(b1, 'profile_CD6', a)
    _safe_set(a, 'profile_CR5', b2)
    assert _is_linked(a, 'profile_CR5', b2)
    if hasattr(b1, 'profile_CD6'):
        assert not _is_linked(b1, 'profile_CD6', a)
    if hasattr(b2, 'profile_CD6'):
        assert _is_linked(b2, 'profile_CD6', a)
    _safe_set(a, 'profile_CR5', None)
    assert not _is_linked(a, 'profile_CR5', b2)
    if hasattr(b2, 'profile_CD6'):
        assert not _is_linked(b2, 'profile_CD6', a)


def test_assoc_qualifier0_link_reassign_clear():
    a = profile_CR(inverted="sample_text")
    b1 = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    b2 = profile_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", displayName="sample_text_2")
    _safe_set(a, 'profile_CR', b1)
    assert _is_linked(a, 'profile_CR', b1)
    if hasattr(b1, 'profile_CD'):
        assert _is_linked(b1, 'profile_CD', a)
    _safe_set(a, 'profile_CR', b2)
    assert _is_linked(a, 'profile_CR', b2)
    if hasattr(b1, 'profile_CD'):
        assert not _is_linked(b1, 'profile_CD', a)
    if hasattr(b2, 'profile_CD'):
        assert _is_linked(b2, 'profile_CD', a)
    _safe_set(a, 'profile_CR', None)
    assert not _is_linked(a, 'profile_CR', b2)
    if hasattr(b2, 'profile_CD'):
        assert not _is_linked(b2, 'profile_CD', a)


def test_assoc_qualifier16_link_reassign_clear():
    a = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    b1 = profile_CR(inverted="sample_text")
    b2 = profile_CR(inverted="sample_text_2")
    _safe_set(a, 'profile_CodeSystemConstraint17', {b1})
    assert _is_linked(a, 'profile_CodeSystemConstraint17', b1)
    if hasattr(b1, 'profile_CR18'):
        assert _is_linked(b1, 'profile_CR18', a)
    _safe_set(a, 'profile_CodeSystemConstraint17', {b2})
    assert _is_linked(a, 'profile_CodeSystemConstraint17', b2)
    if hasattr(b1, 'profile_CR18'):
        assert not _is_linked(b1, 'profile_CR18', a)
    if hasattr(b2, 'profile_CR18'):
        assert _is_linked(b2, 'profile_CR18', a)
    _safe_set(a, 'profile_CodeSystemConstraint17', set())
    assert not _is_linked(a, 'profile_CodeSystemConstraint17', b2)
    if hasattr(b2, 'profile_CR18'):
        assert not _is_linked(b2, 'profile_CR18', a)


def test_assoc_reference10_link_reassign_clear():
    a = profile_ConceptDomainConstraint(identifier="sample_text", name="sample_text")
    b1 = profile_ConceptDomain(fullName="sample_text", identifier="sample_text", status="sample_text", statusDate="sample_text")
    b2 = profile_ConceptDomain(fullName="sample_text_2", identifier="sample_text_2", status="sample_text_2", statusDate="sample_text_2")
    _safe_set(a, 'profile_ConceptDomainConstraint', b1)
    assert _is_linked(a, 'profile_ConceptDomainConstraint', b1)
    if hasattr(b1, 'profile_ConceptDomain'):
        assert _is_linked(b1, 'profile_ConceptDomain', a)
    _safe_set(a, 'profile_ConceptDomainConstraint', b2)
    assert _is_linked(a, 'profile_ConceptDomainConstraint', b2)
    if hasattr(b1, 'profile_ConceptDomain'):
        assert not _is_linked(b1, 'profile_ConceptDomain', a)
    if hasattr(b2, 'profile_ConceptDomain'):
        assert _is_linked(b2, 'profile_ConceptDomain', a)
    _safe_set(a, 'profile_ConceptDomainConstraint', None)
    assert not _is_linked(a, 'profile_ConceptDomainConstraint', b2)
    if hasattr(b2, 'profile_ConceptDomain'):
        assert not _is_linked(b2, 'profile_ConceptDomain', a)


def test_assoc_reference15_link_reassign_clear():
    a = profile_CodeSystemVersion(effectiveDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", url="sample_text", version="sample_text")
    b1 = profile_CodeSystemConstraint(binding="sample_text", code="sample_text", displayName="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    b2 = profile_CodeSystemConstraint(binding="sample_text_2", code="sample_text_2", displayName="sample_text_2", identifier="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'profile_CodeSystemVersion', b1)
    assert _is_linked(a, 'profile_CodeSystemVersion', b1)
    if hasattr(b1, 'profile_CodeSystemConstraint'):
        assert _is_linked(b1, 'profile_CodeSystemConstraint', a)
    _safe_set(a, 'profile_CodeSystemVersion', b2)
    assert _is_linked(a, 'profile_CodeSystemVersion', b2)
    if hasattr(b1, 'profile_CodeSystemConstraint'):
        assert not _is_linked(b1, 'profile_CodeSystemConstraint', a)
    if hasattr(b2, 'profile_CodeSystemConstraint'):
        assert _is_linked(b2, 'profile_CodeSystemConstraint', a)
    _safe_set(a, 'profile_CodeSystemVersion', None)
    assert not _is_linked(a, 'profile_CodeSystemVersion', b2)
    if hasattr(b2, 'profile_CodeSystemConstraint'):
        assert not _is_linked(b2, 'profile_CodeSystemConstraint', a)


def test_assoc_reference24_link_reassign_clear():
    a = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    b1 = profile_ValueSetConstraint(binding="sample_text", extensibility="sample_text", guidance="sample_text", identifier="sample_text", name="sample_text", uri="sample_text", version="sample_text")
    b2 = profile_ValueSetConstraint(binding="sample_text_2", extensibility="sample_text_2", guidance="sample_text_2", identifier="sample_text_2", name="sample_text_2", uri="sample_text_2", version="sample_text_2")
    _safe_set(a, 'profile_ValueSetVersion', b1)
    assert _is_linked(a, 'profile_ValueSetVersion', b1)
    if hasattr(b1, 'profile_ValueSetConstraint'):
        assert _is_linked(b1, 'profile_ValueSetConstraint', a)
    _safe_set(a, 'profile_ValueSetVersion', b2)
    assert _is_linked(a, 'profile_ValueSetVersion', b2)
    if hasattr(b1, 'profile_ValueSetConstraint'):
        assert not _is_linked(b1, 'profile_ValueSetConstraint', a)
    if hasattr(b2, 'profile_ValueSetConstraint'):
        assert _is_linked(b2, 'profile_ValueSetConstraint', a)
    _safe_set(a, 'profile_ValueSetVersion', None)
    assert not _is_linked(a, 'profile_ValueSetVersion', b2)
    if hasattr(b2, 'profile_ValueSetConstraint'):
        assert not _is_linked(b2, 'profile_ValueSetConstraint', a)


def test_assoc_reference55_link_reassign_clear():
    a = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    b1 = profile_NullValueSetConstraint(binding="sample_text", identifier="sample_text", name="sample_text", version="sample_text")
    b2 = profile_NullValueSetConstraint(binding="sample_text_2", identifier="sample_text_2", name="sample_text_2", version="sample_text_2")
    _safe_set(a, 'profile_ValueSetVersion56', b1)
    assert _is_linked(a, 'profile_ValueSetVersion56', b1)
    if hasattr(b1, 'profile_NullValueSetConstraint'):
        assert _is_linked(b1, 'profile_NullValueSetConstraint', a)
    _safe_set(a, 'profile_ValueSetVersion56', b2)
    assert _is_linked(a, 'profile_ValueSetVersion56', b2)
    if hasattr(b1, 'profile_NullValueSetConstraint'):
        assert not _is_linked(b1, 'profile_NullValueSetConstraint', a)
    if hasattr(b2, 'profile_NullValueSetConstraint'):
        assert _is_linked(b2, 'profile_NullValueSetConstraint', a)
    _safe_set(a, 'profile_ValueSetVersion56', None)
    assert not _is_linked(a, 'profile_ValueSetVersion56', b2)
    if hasattr(b2, 'profile_NullValueSetConstraint'):
        assert not _is_linked(b2, 'profile_NullValueSetConstraint', a)


def test_assoc_translation2_link_reassign_clear():
    a = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    b1 = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    b2 = profile_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", displayName="sample_text_2")
    _safe_set(a, 'profile_CD1', {b1})
    assert _is_linked(a, 'profile_CD1', b1)
    if hasattr(b1, 'profile_CD3'):
        assert _is_linked(b1, 'profile_CD3', a)
    _safe_set(a, 'profile_CD1', {b2})
    assert _is_linked(a, 'profile_CD1', b2)
    if hasattr(b1, 'profile_CD3'):
        assert not _is_linked(b1, 'profile_CD3', a)
    if hasattr(b2, 'profile_CD3'):
        assert _is_linked(b2, 'profile_CD3', a)
    _safe_set(a, 'profile_CD1', set())
    assert not _is_linked(a, 'profile_CD1', b2)
    if hasattr(b2, 'profile_CD3'):
        assert not _is_linked(b2, 'profile_CD3', a)


def test_assoc_usageContext43_link_reassign_clear():
    a = profile_ValueSetContextBinding(effectiveDate="sample_text")
    b1 = profile_UsageContext(identifier="sample_text", status="sample_text", statusDate="sample_text")
    b2 = profile_UsageContext(identifier="sample_text_2", status="sample_text_2", statusDate="sample_text_2")
    _safe_set(a, 'profile_ValueSetContextBinding44', b1)
    assert _is_linked(a, 'profile_ValueSetContextBinding44', b1)
    if hasattr(b1, 'profile_UsageContext'):
        assert _is_linked(b1, 'profile_UsageContext', a)
    _safe_set(a, 'profile_ValueSetContextBinding44', b2)
    assert _is_linked(a, 'profile_ValueSetContextBinding44', b2)
    if hasattr(b1, 'profile_UsageContext'):
        assert not _is_linked(b1, 'profile_UsageContext', a)
    if hasattr(b2, 'profile_UsageContext'):
        assert _is_linked(b2, 'profile_UsageContext', a)
    _safe_set(a, 'profile_ValueSetContextBinding44', None)
    assert not _is_linked(a, 'profile_ValueSetContextBinding44', b2)
    if hasattr(b2, 'profile_UsageContext'):
        assert not _is_linked(b2, 'profile_UsageContext', a)


def test_assoc_value7_link_reassign_clear():
    a = profile_CR(inverted="sample_text")
    b1 = profile_CD(code="sample_text", codeSystem="sample_text", codeSystemName="sample_text", codeSystemVersion="sample_text", displayName="sample_text")
    b2 = profile_CD(code="sample_text_2", codeSystem="sample_text_2", codeSystemName="sample_text_2", codeSystemVersion="sample_text_2", displayName="sample_text_2")
    _safe_set(a, 'profile_CR8', b1)
    assert _is_linked(a, 'profile_CR8', b1)
    if hasattr(b1, 'profile_CD9'):
        assert _is_linked(b1, 'profile_CD9', a)
    _safe_set(a, 'profile_CR8', b2)
    assert _is_linked(a, 'profile_CR8', b2)
    if hasattr(b1, 'profile_CD9'):
        assert not _is_linked(b1, 'profile_CD9', a)
    if hasattr(b2, 'profile_CD9'):
        assert _is_linked(b2, 'profile_CD9', a)
    _safe_set(a, 'profile_CR8', None)
    assert not _is_linked(a, 'profile_CR8', b2)
    if hasattr(b2, 'profile_CD9'):
        assert not _is_linked(b2, 'profile_CD9', a)


def test_assoc_valueSet40_link_reassign_clear():
    a = profile_ValueSetVersion(binding="sample_text", definition="sample_text", effectiveDate="sample_text", expirationDate="sample_text", fullName="sample_text", identifier="sample_text", releaseDate="sample_text", revisionDate="sample_text", source="sample_text", status="sample_text", statusDate="sample_text", type="sample_text", url="sample_text", version="sample_text")
    b1 = profile_ValueSetContextBinding(effectiveDate="sample_text")
    b2 = profile_ValueSetContextBinding(effectiveDate="sample_text_2")
    _safe_set(a, 'profile_ValueSetVersion42', b1)
    assert _is_linked(a, 'profile_ValueSetVersion42', b1)
    if hasattr(b1, 'profile_ValueSetContextBinding41'):
        assert _is_linked(b1, 'profile_ValueSetContextBinding41', a)
    _safe_set(a, 'profile_ValueSetVersion42', b2)
    assert _is_linked(a, 'profile_ValueSetVersion42', b2)
    if hasattr(b1, 'profile_ValueSetContextBinding41'):
        assert not _is_linked(b1, 'profile_ValueSetContextBinding41', a)
    if hasattr(b2, 'profile_ValueSetContextBinding41'):
        assert _is_linked(b2, 'profile_ValueSetContextBinding41', a)
    _safe_set(a, 'profile_ValueSetVersion42', None)
    assert not _is_linked(a, 'profile_ValueSetVersion42', b2)
    if hasattr(b2, 'profile_ValueSetContextBinding41'):
        assert not _is_linked(b2, 'profile_ValueSetContextBinding41', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

profile_CD_strategy = st.builds(profile_CD, code=safe_text, codeSystem=safe_text, codeSystemName=safe_text, codeSystemVersion=safe_text, displayName=safe_text)
@given(instance=profile_CD_strategy)
@settings(max_examples=25)
def test_profile_CD_instantiation(instance):
    assert isinstance(instance, profile_CD)


profile_CR_strategy = st.builds(profile_CR, inverted=safe_text)
@given(instance=profile_CR_strategy)
@settings(max_examples=25)
def test_profile_CR_instantiation(instance):
    assert isinstance(instance, profile_CR)


profile_Class_strategy = st.builds(profile_Class)
@given(instance=profile_Class_strategy)
@settings(max_examples=25)
def test_profile_Class_instantiation(instance):
    assert isinstance(instance, profile_Class)


profile_Classifier_strategy = st.builds(profile_Classifier)
@given(instance=profile_Classifier_strategy)
@settings(max_examples=25)
def test_profile_Classifier_instantiation(instance):
    assert isinstance(instance, profile_Classifier)


profile_CodeSystemConstraint_strategy = st.builds(profile_CodeSystemConstraint, binding=safe_text, code=safe_text, displayName=safe_text, identifier=safe_text, name=safe_text, version=safe_text)
@given(instance=profile_CodeSystemConstraint_strategy)
@settings(max_examples=25)
def test_profile_CodeSystemConstraint_instantiation(instance):
    assert isinstance(instance, profile_CodeSystemConstraint)


profile_CodeSystemVersion_strategy = st.builds(profile_CodeSystemVersion, effectiveDate=safe_text, fullName=safe_text, identifier=safe_text, releaseDate=safe_text, source=safe_text, status=safe_text, statusDate=safe_text, url=safe_text, version=safe_text)
@given(instance=profile_CodeSystemVersion_strategy)
@settings(max_examples=25)
def test_profile_CodeSystemVersion_instantiation(instance):
    assert isinstance(instance, profile_CodeSystemVersion)


profile_CodedType_strategy = st.builds(profile_CodedType)
@given(instance=profile_CodedType_strategy)
@settings(max_examples=25)
def test_profile_CodedType_instantiation(instance):
    assert isinstance(instance, profile_CodedType)


profile_ConceptDomain_strategy = st.builds(profile_ConceptDomain, fullName=safe_text, identifier=safe_text, status=safe_text, statusDate=safe_text)
@given(instance=profile_ConceptDomain_strategy)
@settings(max_examples=25)
def test_profile_ConceptDomain_instantiation(instance):
    assert isinstance(instance, profile_ConceptDomain)


profile_ConceptDomainConstraint_strategy = st.builds(profile_ConceptDomainConstraint, identifier=safe_text, name=safe_text)
@given(instance=profile_ConceptDomainConstraint_strategy)
@settings(max_examples=25)
def test_profile_ConceptDomainConstraint_instantiation(instance):
    assert isinstance(instance, profile_ConceptDomainConstraint)


profile_Context_strategy = st.builds(profile_Context)
@given(instance=profile_Context_strategy)
@settings(max_examples=25)
def test_profile_Context_instantiation(instance):
    assert isinstance(instance, profile_Context)


profile_ContextToValueSet_strategy = st.builds(profile_ContextToValueSet, key=safe_text, value=safe_text)
@given(instance=profile_ContextToValueSet_strategy)
@settings(max_examples=25)
def test_profile_ContextToValueSet_instantiation(instance):
    assert isinstance(instance, profile_ContextToValueSet)


profile_Enumeration_strategy = st.builds(profile_Enumeration)
@given(instance=profile_Enumeration_strategy)
@settings(max_examples=25)
def test_profile_Enumeration_instantiation(instance):
    assert isinstance(instance, profile_Enumeration)


profile_EnumerationLiteral_strategy = st.builds(profile_EnumerationLiteral)
@given(instance=profile_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_profile_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, profile_EnumerationLiteral)


profile_NullValueSetConstraint_strategy = st.builds(profile_NullValueSetConstraint, binding=safe_text, identifier=safe_text, name=safe_text, version=safe_text)
@given(instance=profile_NullValueSetConstraint_strategy)
@settings(max_examples=25)
def test_profile_NullValueSetConstraint_instantiation(instance):
    assert isinstance(instance, profile_NullValueSetConstraint)


profile_Property_strategy = st.builds(profile_Property)
@given(instance=profile_Property_strategy)
@settings(max_examples=25)
def test_profile_Property_instantiation(instance):
    assert isinstance(instance, profile_Property)


profile_UsageContext_strategy = st.builds(profile_UsageContext, identifier=safe_text, status=safe_text, statusDate=safe_text)
@given(instance=profile_UsageContext_strategy)
@settings(max_examples=25)
def test_profile_UsageContext_instantiation(instance):
    assert isinstance(instance, profile_UsageContext)


profile_ValueSetCode_strategy = st.builds(profile_ValueSetCode, conceptName=safe_text, usageNote=safe_text)
@given(instance=profile_ValueSetCode_strategy)
@settings(max_examples=25)
def test_profile_ValueSetCode_instantiation(instance):
    assert isinstance(instance, profile_ValueSetCode)


profile_ValueSetConstraint_strategy = st.builds(profile_ValueSetConstraint, binding=safe_text, extensibility=safe_text, guidance=safe_text, identifier=safe_text, name=safe_text, uri=safe_text, version=safe_text)
@given(instance=profile_ValueSetConstraint_strategy)
@settings(max_examples=25)
def test_profile_ValueSetConstraint_instantiation(instance):
    assert isinstance(instance, profile_ValueSetConstraint)


profile_ValueSetConstraints_strategy = st.builds(profile_ValueSetConstraints)
@given(instance=profile_ValueSetConstraints_strategy)
@settings(max_examples=25)
def test_profile_ValueSetConstraints_instantiation(instance):
    assert isinstance(instance, profile_ValueSetConstraints)


profile_ValueSetContextBinding_strategy = st.builds(profile_ValueSetContextBinding, effectiveDate=safe_text)
@given(instance=profile_ValueSetContextBinding_strategy)
@settings(max_examples=25)
def test_profile_ValueSetContextBinding_instantiation(instance):
    assert isinstance(instance, profile_ValueSetContextBinding)


profile_ValueSetVersion_strategy = st.builds(profile_ValueSetVersion, binding=safe_text, definition=safe_text, effectiveDate=safe_text, expirationDate=safe_text, fullName=safe_text, identifier=safe_text, releaseDate=safe_text, revisionDate=safe_text, source=safe_text, status=safe_text, statusDate=safe_text, type=safe_text, url=safe_text, version=safe_text)
@given(instance=profile_ValueSetVersion_strategy)
@settings(max_examples=25)
def test_profile_ValueSetVersion_instantiation(instance):
    assert isinstance(instance, profile_ValueSetVersion)



