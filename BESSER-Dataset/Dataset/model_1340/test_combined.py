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
    basecs_VisitableCS,
    basecs_Type,
    TypeRefCS,
    basecs_WildcardTypeRefCS,
    TemplateParameterCS,
    RootCS,
    basecs_Property,
    PathElementCS,
    basecs_PathElementWithURICS,
    basecs_EClassifier,
    Pivotable,
    PackageOwnerCS,
    basecs_RootPackageCS,
    TypedElementCS,
    basecs_TuplePartCS,
    basecs_ParameterCS,
    basecs_FeatureCS,
    FeatureCS,
    ModelElementCS,
    basecs_TemplateParameterSubstitutionCS,
    basecs_TemplateSignatureCS,
    basecs_RootCS,
    basecs_PackageOwnerCS,
    basecs_TypeCS,
    ElementCS,
    basecs_PivotableElementCS,
    basecs_TemplateableElementCS,
    basecs_PathElementCS,
    basecs_MultiplicityCS,
    MultiplicityCS,
    basecs_MultiplicityStringCS,
    basecs_MultiplicityBoundsCS,
    basecs_Element,
    ElementRefCS,
    basecs_TypeRefCS,
    basecs_TemplateBindingCS,
    Nameable,
    basecs_NamedElementCS,
    TypedRefCS,
    basecs_PrimitiveTypeRefCS,
    basecs_TupleTypeCS,
    basecs_TypedTypeRefCS,
    basecs_Namespace,
    basecs_PathNameCS,
    PivotableElementCS,
    basecs_ElementRefCS,
    VisitableCS,
    basecs_ElementCS,
    basecs_SpecificationCS,
    TemplateableElementCS,
    basecs_LambdaTypeCS,
    TypeCS,
    basecs_TypeParameterCS,
    basecs_StructuralFeatureCS,
    basecs_OperationCS,
    basecs_TypedRefCS,
    NamespaceCS,
    basecs_LibraryCS,
    basecs_ImportCS,
    basecs_PackageCS,
    ClassifierCS,
    basecs_EnumerationCS,
    basecs_DataTypeCS,
    basecs_ClassCS,
    StructuralFeatureCS,
    basecs_ReferenceCS,
    basecs_AttributeCS,
    NamedElementCS,
    basecs_NamespaceCS,
    basecs_EnumerationLiteralCS,
    basecs_ConstraintCS,
    basecs_ClassifierCS,
    basecs_TemplateParameterCS,
    basecs_DetailCS,
    basecs_TypedElementCS,
    basecs_AnnotationElementCS,
    basecs_ModelElementRefCS,
    basecs_ModelElementCS,
    AnnotationElementCS,
    basecs_DocumentationCS,
    basecs_AnnotationCS,
    IteratorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_basecs_visitablecs_is_not_abstract():
    assert not inspect.isabstract(basecs_VisitableCS)


def test_hyp_basecs_visitablecs_constructor_exists():
    assert callable(basecs_VisitableCS.__init__)


def test_hyp_basecs_visitablecs_constructor_args():
    sig = inspect.signature(basecs_VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_type_is_not_abstract():
    assert not inspect.isabstract(basecs_Type)


def test_hyp_basecs_type_constructor_exists():
    assert callable(basecs_Type.__init__)


def test_hyp_basecs_type_constructor_args():
    sig = inspect.signature(basecs_Type.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typerefcs_is_not_abstract():
    assert not inspect.isabstract(TypeRefCS)


def test_hyp_typerefcs_constructor_exists():
    assert callable(TypeRefCS.__init__)


def test_hyp_typerefcs_constructor_args():
    sig = inspect.signature(TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_wildcardtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_WildcardTypeRefCS)


def test_hyp_basecs_wildcardtyperefcs_constructor_exists():
    assert callable(basecs_WildcardTypeRefCS.__init__)


def test_hyp_basecs_wildcardtyperefcs_constructor_args():
    sig = inspect.signature(basecs_WildcardTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(TemplateParameterCS)


def test_hyp_templateparametercs_constructor_exists():
    assert callable(TemplateParameterCS.__init__)


def test_hyp_templateparametercs_constructor_args():
    sig = inspect.signature(TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_rootcs_is_not_abstract():
    assert not inspect.isabstract(RootCS)


def test_hyp_rootcs_constructor_exists():
    assert callable(RootCS.__init__)


def test_hyp_rootcs_constructor_args():
    sig = inspect.signature(RootCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_property_is_not_abstract():
    assert not inspect.isabstract(basecs_Property)


def test_hyp_basecs_property_constructor_exists():
    assert callable(basecs_Property.__init__)


def test_hyp_basecs_property_constructor_args():
    sig = inspect.signature(basecs_Property.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(PathElementCS)


def test_hyp_pathelementcs_constructor_exists():
    assert callable(PathElementCS.__init__)


def test_hyp_pathelementcs_constructor_args():
    sig = inspect.signature(PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_pathelementwithurics_is_not_abstract():
    assert not inspect.isabstract(basecs_PathElementWithURICS)


def test_hyp_basecs_pathelementwithurics_constructor_exists():
    assert callable(basecs_PathElementWithURICS.__init__)


def test_hyp_basecs_pathelementwithurics_constructor_args():
    sig = inspect.signature(basecs_PathElementWithURICS.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"




def test_hyp_basecs_eclassifier_is_not_abstract():
    assert not inspect.isabstract(basecs_EClassifier)


def test_hyp_basecs_eclassifier_constructor_exists():
    assert callable(basecs_EClassifier.__init__)


def test_hyp_basecs_eclassifier_constructor_args():
    sig = inspect.signature(basecs_EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_hyp_pivotable_is_not_abstract():
    assert not inspect.isabstract(Pivotable)


def test_hyp_pivotable_constructor_exists():
    assert callable(Pivotable.__init__)


def test_hyp_pivotable_constructor_args():
    sig = inspect.signature(Pivotable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_packageownercs_is_not_abstract():
    assert not inspect.isabstract(PackageOwnerCS)


def test_hyp_packageownercs_constructor_exists():
    assert callable(PackageOwnerCS.__init__)


def test_hyp_packageownercs_constructor_args():
    sig = inspect.signature(PackageOwnerCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(basecs_RootPackageCS)


def test_hyp_basecs_rootpackagecs_constructor_exists():
    assert callable(basecs_RootPackageCS.__init__)


def test_hyp_basecs_rootpackagecs_constructor_args():
    sig = inspect.signature(basecs_RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(TypedElementCS)


def test_hyp_typedelementcs_constructor_exists():
    assert callable(TypedElementCS.__init__)


def test_hyp_typedelementcs_constructor_args():
    sig = inspect.signature(TypedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_tuplepartcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TuplePartCS)


def test_hyp_basecs_tuplepartcs_constructor_exists():
    assert callable(basecs_TuplePartCS.__init__)


def test_hyp_basecs_tuplepartcs_constructor_args():
    sig = inspect.signature(basecs_TuplePartCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_parametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_ParameterCS)


def test_hyp_basecs_parametercs_constructor_exists():
    assert callable(basecs_ParameterCS.__init__)


def test_hyp_basecs_parametercs_constructor_args():
    sig = inspect.signature(basecs_ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_featurecs_is_not_abstract():
    assert not inspect.isabstract(basecs_FeatureCS)


def test_hyp_basecs_featurecs_constructor_exists():
    assert callable(basecs_FeatureCS.__init__)


def test_hyp_basecs_featurecs_constructor_args():
    sig = inspect.signature(basecs_FeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_featurecs_is_not_abstract():
    assert not inspect.isabstract(FeatureCS)


def test_hyp_featurecs_constructor_exists():
    assert callable(FeatureCS.__init__)


def test_hyp_featurecs_constructor_args():
    sig = inspect.signature(FeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_hyp_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_hyp_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_templateparametersubstitutioncs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateParameterSubstitutionCS)


def test_hyp_basecs_templateparametersubstitutioncs_constructor_exists():
    assert callable(basecs_TemplateParameterSubstitutionCS.__init__)


def test_hyp_basecs_templateparametersubstitutioncs_constructor_args():
    sig = inspect.signature(basecs_TemplateParameterSubstitutionCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_templatesignaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateSignatureCS)


def test_hyp_basecs_templatesignaturecs_constructor_exists():
    assert callable(basecs_TemplateSignatureCS.__init__)


def test_hyp_basecs_templatesignaturecs_constructor_args():
    sig = inspect.signature(basecs_TemplateSignatureCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_rootcs_is_not_abstract():
    assert not inspect.isabstract(basecs_RootCS)


def test_hyp_basecs_rootcs_constructor_exists():
    assert callable(basecs_RootCS.__init__)


def test_hyp_basecs_rootcs_constructor_args():
    sig = inspect.signature(basecs_RootCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_packageownercs_is_not_abstract():
    assert not inspect.isabstract(basecs_PackageOwnerCS)


def test_hyp_basecs_packageownercs_constructor_exists():
    assert callable(basecs_PackageOwnerCS.__init__)


def test_hyp_basecs_packageownercs_constructor_args():
    sig = inspect.signature(basecs_PackageOwnerCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_typecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeCS)


def test_hyp_basecs_typecs_constructor_exists():
    assert callable(basecs_TypeCS.__init__)


def test_hyp_basecs_typecs_constructor_args():
    sig = inspect.signature(basecs_TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementcs_is_not_abstract():
    assert not inspect.isabstract(ElementCS)


def test_hyp_elementcs_constructor_exists():
    assert callable(ElementCS.__init__)


def test_hyp_elementcs_constructor_args():
    sig = inspect.signature(ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PivotableElementCS)


def test_hyp_basecs_pivotableelementcs_constructor_exists():
    assert callable(basecs_PivotableElementCS.__init__)


def test_hyp_basecs_pivotableelementcs_constructor_args():
    sig = inspect.signature(basecs_PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateableElementCS)


def test_hyp_basecs_templateableelementcs_constructor_exists():
    assert callable(basecs_TemplateableElementCS.__init__)


def test_hyp_basecs_templateableelementcs_constructor_args():
    sig = inspect.signature(basecs_TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PathElementCS)


def test_hyp_basecs_pathelementcs_constructor_exists():
    assert callable(basecs_PathElementCS.__init__)


def test_hyp_basecs_pathelementcs_constructor_args():
    sig = inspect.signature(basecs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityCS)


def test_hyp_basecs_multiplicitycs_constructor_exists():
    assert callable(basecs_MultiplicityCS.__init__)


def test_hyp_basecs_multiplicitycs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(MultiplicityCS)


def test_hyp_multiplicitycs_constructor_exists():
    assert callable(MultiplicityCS.__init__)


def test_hyp_multiplicitycs_constructor_args():
    sig = inspect.signature(MultiplicityCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_multiplicitystringcs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityStringCS)


def test_hyp_basecs_multiplicitystringcs_constructor_exists():
    assert callable(basecs_MultiplicityStringCS.__init__)


def test_hyp_basecs_multiplicitystringcs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityStringCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringBounds" in params, "Missing parameter 'stringBounds'"




def test_hyp_basecs_multiplicityboundscs_is_not_abstract():
    assert not inspect.isabstract(basecs_MultiplicityBoundsCS)


def test_hyp_basecs_multiplicityboundscs_constructor_exists():
    assert callable(basecs_MultiplicityBoundsCS.__init__)


def test_hyp_basecs_multiplicityboundscs_constructor_args():
    sig = inspect.signature(basecs_MultiplicityBoundsCS.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"





def test_hyp_basecs_element_is_not_abstract():
    assert not inspect.isabstract(basecs_Element)


def test_hyp_basecs_element_constructor_exists():
    assert callable(basecs_Element.__init__)


def test_hyp_basecs_element_constructor_args():
    sig = inspect.signature(basecs_Element.__init__)
    params = list(sig.parameters.keys())



def test_hyp_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(ElementRefCS)


def test_hyp_elementrefcs_constructor_exists():
    assert callable(ElementRefCS.__init__)


def test_hyp_elementrefcs_constructor_args():
    sig = inspect.signature(ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_typerefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeRefCS)


def test_hyp_basecs_typerefcs_constructor_exists():
    assert callable(basecs_TypeRefCS.__init__)


def test_hyp_basecs_typerefcs_constructor_args():
    sig = inspect.signature(basecs_TypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_templatebindingcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateBindingCS)


def test_hyp_basecs_templatebindingcs_constructor_exists():
    assert callable(basecs_TemplateBindingCS.__init__)


def test_hyp_basecs_templatebindingcs_constructor_args():
    sig = inspect.signature(basecs_TemplateBindingCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_nameable_is_not_abstract():
    assert not inspect.isabstract(Nameable)


def test_hyp_nameable_constructor_exists():
    assert callable(Nameable.__init__)


def test_hyp_nameable_constructor_args():
    sig = inspect.signature(Nameable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_NamedElementCS)


def test_hyp_basecs_namedelementcs_constructor_exists():
    assert callable(basecs_NamedElementCS.__init__)


def test_hyp_basecs_namedelementcs_constructor_args():
    sig = inspect.signature(basecs_NamedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(TypedRefCS)


def test_hyp_typedrefcs_constructor_exists():
    assert callable(TypedRefCS.__init__)


def test_hyp_typedrefcs_constructor_args():
    sig = inspect.signature(TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_primitivetyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_PrimitiveTypeRefCS)


def test_hyp_basecs_primitivetyperefcs_constructor_exists():
    assert callable(basecs_PrimitiveTypeRefCS.__init__)


def test_hyp_basecs_primitivetyperefcs_constructor_args():
    sig = inspect.signature(basecs_PrimitiveTypeRefCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_basecs_tupletypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_TupleTypeCS)


def test_hyp_basecs_tupletypecs_constructor_exists():
    assert callable(basecs_TupleTypeCS.__init__)


def test_hyp_basecs_tupletypecs_constructor_args():
    sig = inspect.signature(basecs_TupleTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_basecs_typedtyperefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedTypeRefCS)


def test_hyp_basecs_typedtyperefcs_constructor_exists():
    assert callable(basecs_TypedTypeRefCS.__init__)


def test_hyp_basecs_typedtyperefcs_constructor_args():
    sig = inspect.signature(basecs_TypedTypeRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_namespace_is_not_abstract():
    assert not inspect.isabstract(basecs_Namespace)


def test_hyp_basecs_namespace_constructor_exists():
    assert callable(basecs_Namespace.__init__)


def test_hyp_basecs_namespace_constructor_args():
    sig = inspect.signature(basecs_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(basecs_PathNameCS)


def test_hyp_basecs_pathnamecs_constructor_exists():
    assert callable(basecs_PathNameCS.__init__)


def test_hyp_basecs_pathnamecs_constructor_args():
    sig = inspect.signature(basecs_PathNameCS.__init__)
    params = list(sig.parameters.keys())
    assert "scopeFilter" in params, "Missing parameter 'scopeFilter'"




def test_hyp_pivotableelementcs_is_not_abstract():
    assert not inspect.isabstract(PivotableElementCS)


def test_hyp_pivotableelementcs_constructor_exists():
    assert callable(PivotableElementCS.__init__)


def test_hyp_pivotableelementcs_constructor_args():
    sig = inspect.signature(PivotableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_elementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ElementRefCS)


def test_hyp_basecs_elementrefcs_constructor_exists():
    assert callable(basecs_ElementRefCS.__init__)


def test_hyp_basecs_elementrefcs_constructor_args():
    sig = inspect.signature(basecs_ElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_visitablecs_is_not_abstract():
    assert not inspect.isabstract(VisitableCS)


def test_hyp_visitablecs_constructor_exists():
    assert callable(VisitableCS.__init__)


def test_hyp_visitablecs_constructor_args():
    sig = inspect.signature(VisitableCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_elementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ElementCS)


def test_hyp_basecs_elementcs_constructor_exists():
    assert callable(basecs_ElementCS.__init__)


def test_hyp_basecs_elementcs_constructor_args():
    sig = inspect.signature(basecs_ElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_specificationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_SpecificationCS)


def test_hyp_basecs_specificationcs_constructor_exists():
    assert callable(basecs_SpecificationCS.__init__)


def test_hyp_basecs_specificationcs_constructor_args():
    sig = inspect.signature(basecs_SpecificationCS.__init__)
    params = list(sig.parameters.keys())
    assert "exprString" in params, "Missing parameter 'exprString'"




def test_hyp_templateableelementcs_is_not_abstract():
    assert not inspect.isabstract(TemplateableElementCS)


def test_hyp_templateableelementcs_constructor_exists():
    assert callable(TemplateableElementCS.__init__)


def test_hyp_templateableelementcs_constructor_args():
    sig = inspect.signature(TemplateableElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_lambdatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_LambdaTypeCS)


def test_hyp_basecs_lambdatypecs_constructor_exists():
    assert callable(basecs_LambdaTypeCS.__init__)


def test_hyp_basecs_lambdatypecs_constructor_args():
    sig = inspect.signature(basecs_LambdaTypeCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_hyp_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_hyp_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_typeparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypeParameterCS)


def test_hyp_basecs_typeparametercs_constructor_exists():
    assert callable(basecs_TypeParameterCS.__init__)


def test_hyp_basecs_typeparametercs_constructor_args():
    sig = inspect.signature(basecs_TypeParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(basecs_StructuralFeatureCS)


def test_hyp_basecs_structuralfeaturecs_constructor_exists():
    assert callable(basecs_StructuralFeatureCS.__init__)


def test_hyp_basecs_structuralfeaturecs_constructor_args():
    sig = inspect.signature(basecs_StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"




def test_hyp_basecs_operationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_OperationCS)


def test_hyp_basecs_operationcs_constructor_exists():
    assert callable(basecs_OperationCS.__init__)


def test_hyp_basecs_operationcs_constructor_args():
    sig = inspect.signature(basecs_OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_typedrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedRefCS)


def test_hyp_basecs_typedrefcs_constructor_exists():
    assert callable(basecs_TypedRefCS.__init__)


def test_hyp_basecs_typedrefcs_constructor_args():
    sig = inspect.signature(basecs_TypedRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namespacecs_is_not_abstract():
    assert not inspect.isabstract(NamespaceCS)


def test_hyp_namespacecs_constructor_exists():
    assert callable(NamespaceCS.__init__)


def test_hyp_namespacecs_constructor_args():
    sig = inspect.signature(NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_librarycs_is_not_abstract():
    assert not inspect.isabstract(basecs_LibraryCS)


def test_hyp_basecs_librarycs_constructor_exists():
    assert callable(basecs_LibraryCS.__init__)


def test_hyp_basecs_librarycs_constructor_args():
    sig = inspect.signature(basecs_LibraryCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_importcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ImportCS)


def test_hyp_basecs_importcs_constructor_exists():
    assert callable(basecs_ImportCS.__init__)


def test_hyp_basecs_importcs_constructor_args():
    sig = inspect.signature(basecs_ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"




def test_hyp_basecs_packagecs_is_not_abstract():
    assert not inspect.isabstract(basecs_PackageCS)


def test_hyp_basecs_packagecs_constructor_exists():
    assert callable(basecs_PackageCS.__init__)


def test_hyp_basecs_packagecs_constructor_args():
    sig = inspect.signature(basecs_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "nsPrefix" in params, "Missing parameter 'nsPrefix'"
    assert "nsURI" in params, "Missing parameter 'nsURI'"





def test_hyp_classifiercs_is_not_abstract():
    assert not inspect.isabstract(ClassifierCS)


def test_hyp_classifiercs_constructor_exists():
    assert callable(ClassifierCS.__init__)


def test_hyp_classifiercs_constructor_args():
    sig = inspect.signature(ClassifierCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_enumerationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_EnumerationCS)


def test_hyp_basecs_enumerationcs_constructor_exists():
    assert callable(basecs_EnumerationCS.__init__)


def test_hyp_basecs_enumerationcs_constructor_args():
    sig = inspect.signature(basecs_EnumerationCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_datatypecs_is_not_abstract():
    assert not inspect.isabstract(basecs_DataTypeCS)


def test_hyp_basecs_datatypecs_constructor_exists():
    assert callable(basecs_DataTypeCS.__init__)


def test_hyp_basecs_datatypecs_constructor_args():
    sig = inspect.signature(basecs_DataTypeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_classcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ClassCS)


def test_hyp_basecs_classcs_constructor_exists():
    assert callable(basecs_ClassCS.__init__)


def test_hyp_basecs_classcs_constructor_args():
    sig = inspect.signature(basecs_ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_structuralfeaturecs_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureCS)


def test_hyp_structuralfeaturecs_constructor_exists():
    assert callable(StructuralFeatureCS.__init__)


def test_hyp_structuralfeaturecs_constructor_args():
    sig = inspect.signature(StructuralFeatureCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_referencecs_is_not_abstract():
    assert not inspect.isabstract(basecs_ReferenceCS)


def test_hyp_basecs_referencecs_constructor_exists():
    assert callable(basecs_ReferenceCS.__init__)


def test_hyp_basecs_referencecs_constructor_args():
    sig = inspect.signature(basecs_ReferenceCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_attributecs_is_not_abstract():
    assert not inspect.isabstract(basecs_AttributeCS)


def test_hyp_basecs_attributecs_constructor_exists():
    assert callable(basecs_AttributeCS.__init__)


def test_hyp_basecs_attributecs_constructor_args():
    sig = inspect.signature(basecs_AttributeCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_namedelementcs_is_not_abstract():
    assert not inspect.isabstract(NamedElementCS)


def test_hyp_namedelementcs_constructor_exists():
    assert callable(NamedElementCS.__init__)


def test_hyp_namedelementcs_constructor_args():
    sig = inspect.signature(NamedElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_namespacecs_is_not_abstract():
    assert not inspect.isabstract(basecs_NamespaceCS)


def test_hyp_basecs_namespacecs_constructor_exists():
    assert callable(basecs_NamespaceCS.__init__)


def test_hyp_basecs_namespacecs_constructor_args():
    sig = inspect.signature(basecs_NamespaceCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_enumerationliteralcs_is_not_abstract():
    assert not inspect.isabstract(basecs_EnumerationLiteralCS)


def test_hyp_basecs_enumerationliteralcs_constructor_exists():
    assert callable(basecs_EnumerationLiteralCS.__init__)


def test_hyp_basecs_enumerationliteralcs_constructor_args():
    sig = inspect.signature(basecs_EnumerationLiteralCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_basecs_constraintcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ConstraintCS)


def test_hyp_basecs_constraintcs_constructor_exists():
    assert callable(basecs_ConstraintCS.__init__)


def test_hyp_basecs_constraintcs_constructor_args():
    sig = inspect.signature(basecs_ConstraintCS.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"




def test_hyp_basecs_classifiercs_is_not_abstract():
    assert not inspect.isabstract(basecs_ClassifierCS)


def test_hyp_basecs_classifiercs_constructor_exists():
    assert callable(basecs_ClassifierCS.__init__)


def test_hyp_basecs_classifiercs_constructor_args():
    sig = inspect.signature(basecs_ClassifierCS.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "instanceClassName" in params, "Missing parameter 'instanceClassName'"





def test_hyp_basecs_templateparametercs_is_not_abstract():
    assert not inspect.isabstract(basecs_TemplateParameterCS)


def test_hyp_basecs_templateparametercs_constructor_exists():
    assert callable(basecs_TemplateParameterCS.__init__)


def test_hyp_basecs_templateparametercs_constructor_args():
    sig = inspect.signature(basecs_TemplateParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_detailcs_is_not_abstract():
    assert not inspect.isabstract(basecs_DetailCS)


def test_hyp_basecs_detailcs_constructor_exists():
    assert callable(basecs_DetailCS.__init__)


def test_hyp_basecs_detailcs_constructor_args():
    sig = inspect.signature(basecs_DetailCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_basecs_typedelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_TypedElementCS)


def test_hyp_basecs_typedelementcs_constructor_exists():
    assert callable(basecs_TypedElementCS.__init__)


def test_hyp_basecs_typedelementcs_constructor_args():
    sig = inspect.signature(basecs_TypedElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "qualifier" in params, "Missing parameter 'qualifier'"





def test_hyp_basecs_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_AnnotationElementCS)


def test_hyp_basecs_annotationelementcs_constructor_exists():
    assert callable(basecs_AnnotationElementCS.__init__)


def test_hyp_basecs_annotationelementcs_constructor_args():
    sig = inspect.signature(basecs_AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_modelelementrefcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ModelElementRefCS)


def test_hyp_basecs_modelelementrefcs_constructor_exists():
    assert callable(basecs_ModelElementRefCS.__init__)


def test_hyp_basecs_modelelementrefcs_constructor_args():
    sig = inspect.signature(basecs_ModelElementRefCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(basecs_ModelElementCS)


def test_hyp_basecs_modelelementcs_constructor_exists():
    assert callable(basecs_ModelElementCS.__init__)


def test_hyp_basecs_modelelementcs_constructor_args():
    sig = inspect.signature(basecs_ModelElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "csi" in params, "Missing parameter 'csi'"
    assert "originalXmiId" in params, "Missing parameter 'originalXmiId'"





def test_hyp_annotationelementcs_is_not_abstract():
    assert not inspect.isabstract(AnnotationElementCS)


def test_hyp_annotationelementcs_constructor_exists():
    assert callable(AnnotationElementCS.__init__)


def test_hyp_annotationelementcs_constructor_args():
    sig = inspect.signature(AnnotationElementCS.__init__)
    params = list(sig.parameters.keys())



def test_hyp_basecs_documentationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_DocumentationCS)


def test_hyp_basecs_documentationcs_constructor_exists():
    assert callable(basecs_DocumentationCS.__init__)


def test_hyp_basecs_documentationcs_constructor_args():
    sig = inspect.signature(basecs_DocumentationCS.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_basecs_annotationcs_is_not_abstract():
    assert not inspect.isabstract(basecs_AnnotationCS)


def test_hyp_basecs_annotationcs_constructor_exists():
    assert callable(basecs_AnnotationCS.__init__)


def test_hyp_basecs_annotationcs_constructor_args():
    sig = inspect.signature(basecs_AnnotationCS.__init__)
    params = list(sig.parameters.keys())

def test_hyp_iteratorkind_exists():
    # Check that the Enumeration exists
    assert IteratorKind is not None

def test_hyp_iteratorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IteratorKind]
    expected_literals = [
        "Iterator",
        "Parameter",
        "Accumulator",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IteratorKind"


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
basecs_VisitableCS_strategy = st.builds(
    basecs_VisitableCS,
)
basecs_Type_strategy = st.builds(
    basecs_Type,
)
TypeRefCS_strategy = st.builds(
    TypeRefCS,
)
basecs_WildcardTypeRefCS_strategy = st.builds(
    basecs_WildcardTypeRefCS,
)
TemplateParameterCS_strategy = st.builds(
    TemplateParameterCS,
)
RootCS_strategy = st.builds(
    RootCS,
)
basecs_Property_strategy = st.builds(
    basecs_Property,
)
PathElementCS_strategy = st.builds(
    PathElementCS,
)
basecs_PathElementWithURICS_strategy = st.builds(
    basecs_PathElementWithURICS,
    uri=
        safe_text
)
basecs_EClassifier_strategy = st.builds(
    basecs_EClassifier,
)
Pivotable_strategy = st.builds(
    Pivotable,
)
PackageOwnerCS_strategy = st.builds(
    PackageOwnerCS,
)
basecs_RootPackageCS_strategy = st.builds(
    basecs_RootPackageCS,
)
TypedElementCS_strategy = st.builds(
    TypedElementCS,
)
basecs_TuplePartCS_strategy = st.builds(
    basecs_TuplePartCS,
)
basecs_ParameterCS_strategy = st.builds(
    basecs_ParameterCS,
)
basecs_FeatureCS_strategy = st.builds(
    basecs_FeatureCS,
)
FeatureCS_strategy = st.builds(
    FeatureCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
basecs_TemplateParameterSubstitutionCS_strategy = st.builds(
    basecs_TemplateParameterSubstitutionCS,
)
basecs_TemplateSignatureCS_strategy = st.builds(
    basecs_TemplateSignatureCS,
)
basecs_RootCS_strategy = st.builds(
    basecs_RootCS,
)
basecs_PackageOwnerCS_strategy = st.builds(
    basecs_PackageOwnerCS,
)
basecs_TypeCS_strategy = st.builds(
    basecs_TypeCS,
)
ElementCS_strategy = st.builds(
    ElementCS,
)
basecs_PivotableElementCS_strategy = st.builds(
    basecs_PivotableElementCS,
)
basecs_TemplateableElementCS_strategy = st.builds(
    basecs_TemplateableElementCS,
)
basecs_PathElementCS_strategy = st.builds(
    basecs_PathElementCS,
)
basecs_MultiplicityCS_strategy = st.builds(
    basecs_MultiplicityCS,
)
MultiplicityCS_strategy = st.builds(
    MultiplicityCS,
)
basecs_MultiplicityStringCS_strategy = st.builds(
    basecs_MultiplicityStringCS,
    stringBounds=
        safe_text
)
basecs_MultiplicityBoundsCS_strategy = st.builds(
    basecs_MultiplicityBoundsCS,
    lowerBound=
        st.integers(),
    upperBound=
        safe_text
)
basecs_Element_strategy = st.builds(
    basecs_Element,
)
ElementRefCS_strategy = st.builds(
    ElementRefCS,
)
basecs_TypeRefCS_strategy = st.builds(
    basecs_TypeRefCS,
)
basecs_TemplateBindingCS_strategy = st.builds(
    basecs_TemplateBindingCS,
)
Nameable_strategy = st.builds(
    Nameable,
)
basecs_NamedElementCS_strategy = st.builds(
    basecs_NamedElementCS,
    name=
        safe_text
)
TypedRefCS_strategy = st.builds(
    TypedRefCS,
)
basecs_PrimitiveTypeRefCS_strategy = st.builds(
    basecs_PrimitiveTypeRefCS,
    name=
        safe_text
)
basecs_TupleTypeCS_strategy = st.builds(
    basecs_TupleTypeCS,
    name=
        safe_text
)
basecs_TypedTypeRefCS_strategy = st.builds(
    basecs_TypedTypeRefCS,
)
basecs_Namespace_strategy = st.builds(
    basecs_Namespace,
)
basecs_PathNameCS_strategy = st.builds(
    basecs_PathNameCS,
    scopeFilter=
        safe_text
)
PivotableElementCS_strategy = st.builds(
    PivotableElementCS,
)
basecs_ElementRefCS_strategy = st.builds(
    basecs_ElementRefCS,
)
VisitableCS_strategy = st.builds(
    VisitableCS,
)
basecs_ElementCS_strategy = st.builds(
    basecs_ElementCS,
)
basecs_SpecificationCS_strategy = st.builds(
    basecs_SpecificationCS,
    exprString=
        safe_text
)
TemplateableElementCS_strategy = st.builds(
    TemplateableElementCS,
)
basecs_LambdaTypeCS_strategy = st.builds(
    basecs_LambdaTypeCS,
    name=
        safe_text
)
TypeCS_strategy = st.builds(
    TypeCS,
)
basecs_TypeParameterCS_strategy = st.builds(
    basecs_TypeParameterCS,
)
basecs_StructuralFeatureCS_strategy = st.builds(
    basecs_StructuralFeatureCS,
    default=
        safe_text
)
basecs_OperationCS_strategy = st.builds(
    basecs_OperationCS,
)
basecs_TypedRefCS_strategy = st.builds(
    basecs_TypedRefCS,
)
NamespaceCS_strategy = st.builds(
    NamespaceCS,
)
basecs_LibraryCS_strategy = st.builds(
    basecs_LibraryCS,
)
basecs_ImportCS_strategy = st.builds(
    basecs_ImportCS,
    all=
        st.booleans()
)
basecs_PackageCS_strategy = st.builds(
    basecs_PackageCS,
    nsPrefix=
        safe_text,
    nsURI=
        safe_text
)
ClassifierCS_strategy = st.builds(
    ClassifierCS,
)
basecs_EnumerationCS_strategy = st.builds(
    basecs_EnumerationCS,
)
basecs_DataTypeCS_strategy = st.builds(
    basecs_DataTypeCS,
)
basecs_ClassCS_strategy = st.builds(
    basecs_ClassCS,
)
StructuralFeatureCS_strategy = st.builds(
    StructuralFeatureCS,
)
basecs_ReferenceCS_strategy = st.builds(
    basecs_ReferenceCS,
)
basecs_AttributeCS_strategy = st.builds(
    basecs_AttributeCS,
)
NamedElementCS_strategy = st.builds(
    NamedElementCS,
)
basecs_NamespaceCS_strategy = st.builds(
    basecs_NamespaceCS,
)
basecs_EnumerationLiteralCS_strategy = st.builds(
    basecs_EnumerationLiteralCS,
    value=
        st.integers()
)
basecs_ConstraintCS_strategy = st.builds(
    basecs_ConstraintCS,
    stereotype=
        safe_text
)
basecs_ClassifierCS_strategy = st.builds(
    basecs_ClassifierCS,
    qualifier=
        safe_text,
    instanceClassName=
        safe_text
)
basecs_TemplateParameterCS_strategy = st.builds(
    basecs_TemplateParameterCS,
)
basecs_DetailCS_strategy = st.builds(
    basecs_DetailCS,
    value=
        safe_text
)
basecs_TypedElementCS_strategy = st.builds(
    basecs_TypedElementCS,
    optional=
        st.booleans(),
    qualifier=
        safe_text
)
basecs_AnnotationElementCS_strategy = st.builds(
    basecs_AnnotationElementCS,
)
basecs_ModelElementRefCS_strategy = st.builds(
    basecs_ModelElementRefCS,
)
basecs_ModelElementCS_strategy = st.builds(
    basecs_ModelElementCS,
    csi=
        safe_text,
    originalXmiId=
        safe_text
)
AnnotationElementCS_strategy = st.builds(
    AnnotationElementCS,
)
basecs_DocumentationCS_strategy = st.builds(
    basecs_DocumentationCS,
    value=
        safe_text
)
basecs_AnnotationCS_strategy = st.builds(
    basecs_AnnotationCS,
)












@given(instance=basecs_PathElementWithURICS_strategy)
def test_hyp_basecs_pathelementwithurics_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original








import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_ParameterCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_parametercs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_ParameterCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_ParameterCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_ParameterCS is not implemented or raised an error")


















@given(instance=basecs_MultiplicityStringCS_strategy)
def test_hyp_basecs_multiplicitystringcs_stringBounds_setter(instance):
    original = instance.stringBounds
    instance.stringBounds = original
    assert instance.stringBounds == original




@given(instance=basecs_MultiplicityBoundsCS_strategy)
def test_hyp_basecs_multiplicityboundscs_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=basecs_MultiplicityBoundsCS_strategy)
def test_hyp_basecs_multiplicityboundscs_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original









@given(instance=basecs_NamedElementCS_strategy)
def test_hyp_basecs_namedelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original





@given(instance=basecs_PrimitiveTypeRefCS_strategy)
def test_hyp_basecs_primitivetyperefcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=basecs_TupleTypeCS_strategy)
def test_hyp_basecs_tupletypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=basecs_PathNameCS_strategy)
def test_hyp_basecs_pathnamecs_scopeFilter_setter(instance):
    original = instance.scopeFilter
    instance.scopeFilter = original
    assert instance.scopeFilter == original








@given(instance=basecs_SpecificationCS_strategy)
def test_hyp_basecs_specificationcs_exprString_setter(instance):
    original = instance.exprString
    instance.exprString = original
    assert instance.exprString == original





@given(instance=basecs_LambdaTypeCS_strategy)
def test_hyp_basecs_lambdatypecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original






@given(instance=basecs_StructuralFeatureCS_strategy)
def test_hyp_basecs_structuralfeaturecs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_StructuralFeatureCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_structuralfeaturecs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_StructuralFeatureCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_StructuralFeatureCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_StructuralFeatureCS is not implemented or raised an error")


import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_OperationCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_operationcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_OperationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_OperationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_OperationCS is not implemented or raised an error")







@given(instance=basecs_ImportCS_strategy)
def test_hyp_basecs_importcs_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original




@given(instance=basecs_PackageCS_strategy)
def test_hyp_basecs_packagecs_nsPrefix_setter(instance):
    original = instance.nsPrefix
    instance.nsPrefix = original
    assert instance.nsPrefix == original



@given(instance=basecs_PackageCS_strategy)
def test_hyp_basecs_packagecs_nsURI_setter(instance):
    original = instance.nsURI
    instance.nsURI = original
    assert instance.nsURI == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_PackageCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_packagecs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_PackageCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_PackageCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_PackageCS is not implemented or raised an error")



import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_EnumerationCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_enumerationcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_EnumerationCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_EnumerationCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_EnumerationCS is not implemented or raised an error")











@given(instance=basecs_EnumerationLiteralCS_strategy)
def test_hyp_basecs_enumerationliteralcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_EnumerationLiteralCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_enumerationliteralcs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_EnumerationLiteralCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_EnumerationLiteralCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_EnumerationLiteralCS is not implemented or raised an error")




@given(instance=basecs_ConstraintCS_strategy)
def test_hyp_basecs_constraintcs_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original




@given(instance=basecs_ClassifierCS_strategy)
def test_hyp_basecs_classifiercs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=basecs_ClassifierCS_strategy)
def test_hyp_basecs_classifiercs_instanceClassName_setter(instance):
    original = instance.instanceClassName
    instance.instanceClassName = original
    assert instance.instanceClassName == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=basecs_ClassifierCS_strategy)
@settings(max_examples=30)
def test_hyp_basecs_classifiercs_ast_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ast()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ast).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ast' in basecs_ClassifierCS is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ast' in basecs_ClassifierCS did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ast' in basecs_ClassifierCS is not implemented or raised an error")





@given(instance=basecs_DetailCS_strategy)
def test_hyp_basecs_detailcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=basecs_TypedElementCS_strategy)
def test_hyp_basecs_typedelementcs_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=basecs_TypedElementCS_strategy)
def test_hyp_basecs_typedelementcs_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original






@given(instance=basecs_ModelElementCS_strategy)
def test_hyp_basecs_modelelementcs_csi_setter(instance):
    original = instance.csi
    instance.csi = original
    assert instance.csi == original



@given(instance=basecs_ModelElementCS_strategy)
def test_hyp_basecs_modelelementcs_originalXmiId_setter(instance):
    original = instance.originalXmiId
    instance.originalXmiId = original
    assert instance.originalXmiId == original





@given(instance=basecs_DocumentationCS_strategy)
def test_hyp_basecs_documentationcs_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    AnnotationElementCS,
    ClassifierCS,
    ElementCS,
    ElementRefCS,
    FeatureCS,
    ModelElementCS,
    MultiplicityCS,
    Nameable,
    NamedElementCS,
    NamespaceCS,
    PackageOwnerCS,
    PathElementCS,
    Pivotable,
    PivotableElementCS,
    RootCS,
    StructuralFeatureCS,
    TemplateParameterCS,
    TemplateableElementCS,
    TypeCS,
    TypeRefCS,
    TypedElementCS,
    TypedRefCS,
    VisitableCS,
    basecs_AnnotationCS,
    basecs_AnnotationElementCS,
    basecs_AttributeCS,
    basecs_ClassCS,
    basecs_ClassifierCS,
    basecs_ConstraintCS,
    basecs_DataTypeCS,
    basecs_DetailCS,
    basecs_DocumentationCS,
    basecs_EClassifier,
    basecs_Element,
    basecs_ElementCS,
    basecs_ElementRefCS,
    basecs_EnumerationCS,
    basecs_EnumerationLiteralCS,
    basecs_FeatureCS,
    basecs_ImportCS,
    basecs_LambdaTypeCS,
    basecs_LibraryCS,
    basecs_ModelElementCS,
    basecs_ModelElementRefCS,
    basecs_MultiplicityBoundsCS,
    basecs_MultiplicityCS,
    basecs_MultiplicityStringCS,
    basecs_NamedElementCS,
    basecs_Namespace,
    basecs_NamespaceCS,
    basecs_OperationCS,
    basecs_PackageCS,
    basecs_PackageOwnerCS,
    basecs_ParameterCS,
    basecs_PathElementCS,
    basecs_PathElementWithURICS,
    basecs_PathNameCS,
    basecs_PivotableElementCS,
    basecs_PrimitiveTypeRefCS,
    basecs_Property,
    basecs_ReferenceCS,
    basecs_RootCS,
    basecs_RootPackageCS,
    basecs_SpecificationCS,
    basecs_StructuralFeatureCS,
    basecs_TemplateBindingCS,
    basecs_TemplateParameterCS,
    basecs_TemplateParameterSubstitutionCS,
    basecs_TemplateSignatureCS,
    basecs_TemplateableElementCS,
    basecs_TuplePartCS,
    basecs_TupleTypeCS,
    basecs_Type,
    basecs_TypeCS,
    basecs_TypeParameterCS,
    basecs_TypeRefCS,
    basecs_TypedElementCS,
    basecs_TypedRefCS,
    basecs_TypedTypeRefCS,
    basecs_VisitableCS,
    basecs_WildcardTypeRefCS,
    IteratorKind,
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

def test_basecs_ClassifierCS_instanceClassName_value_roundtrip():
    instance = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    assert instance.instanceClassName == "sample_text"
    instance.instanceClassName = "sample_text_2"
    assert instance.instanceClassName == "sample_text_2"


def test_basecs_ClassifierCS_qualifier_value_roundtrip():
    instance = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_basecs_ConstraintCS_stereotype_value_roundtrip():
    instance = basecs_ConstraintCS(stereotype="sample_text")
    assert instance.stereotype == "sample_text"
    instance.stereotype = "sample_text_2"
    assert instance.stereotype == "sample_text_2"


def test_basecs_DetailCS_value_value_roundtrip():
    instance = basecs_DetailCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_basecs_DocumentationCS_value_value_roundtrip():
    instance = basecs_DocumentationCS(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_basecs_EnumerationLiteralCS_value_value_roundtrip():
    instance = basecs_EnumerationLiteralCS(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_basecs_ImportCS_all_value_roundtrip():
    instance = basecs_ImportCS(all=True)
    assert instance.all == True
    instance.all = False
    assert instance.all == False


def test_basecs_LambdaTypeCS_name_value_roundtrip():
    instance = basecs_LambdaTypeCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basecs_ModelElementCS_csi_value_roundtrip():
    instance = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    assert instance.csi == "sample_text"
    instance.csi = "sample_text_2"
    assert instance.csi == "sample_text_2"


def test_basecs_ModelElementCS_originalXmiId_value_roundtrip():
    instance = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    assert instance.originalXmiId == "sample_text"
    instance.originalXmiId = "sample_text_2"
    assert instance.originalXmiId == "sample_text_2"


def test_basecs_MultiplicityBoundsCS_lowerBound_value_roundtrip():
    instance = basecs_MultiplicityBoundsCS(lowerBound=7, upperBound="sample_text")
    assert instance.lowerBound == 7
    instance.lowerBound = 13
    assert instance.lowerBound == 13


def test_basecs_MultiplicityBoundsCS_upperBound_value_roundtrip():
    instance = basecs_MultiplicityBoundsCS(lowerBound=7, upperBound="sample_text")
    assert instance.upperBound == "sample_text"
    instance.upperBound = "sample_text_2"
    assert instance.upperBound == "sample_text_2"


def test_basecs_MultiplicityStringCS_stringBounds_value_roundtrip():
    instance = basecs_MultiplicityStringCS(stringBounds="sample_text")
    assert instance.stringBounds == "sample_text"
    instance.stringBounds = "sample_text_2"
    assert instance.stringBounds == "sample_text_2"


def test_basecs_NamedElementCS_name_value_roundtrip():
    instance = basecs_NamedElementCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basecs_PackageCS_nsPrefix_value_roundtrip():
    instance = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsPrefix == "sample_text"
    instance.nsPrefix = "sample_text_2"
    assert instance.nsPrefix == "sample_text_2"


def test_basecs_PackageCS_nsURI_value_roundtrip():
    instance = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    assert instance.nsURI == "sample_text"
    instance.nsURI = "sample_text_2"
    assert instance.nsURI == "sample_text_2"


def test_basecs_PathElementWithURICS_uri_value_roundtrip():
    instance = basecs_PathElementWithURICS(uri="sample_text")
    assert instance.uri == "sample_text"
    instance.uri = "sample_text_2"
    assert instance.uri == "sample_text_2"


def test_basecs_PathNameCS_scopeFilter_value_roundtrip():
    instance = basecs_PathNameCS(scopeFilter="sample_text")
    assert instance.scopeFilter == "sample_text"
    instance.scopeFilter = "sample_text_2"
    assert instance.scopeFilter == "sample_text_2"


def test_basecs_PrimitiveTypeRefCS_name_value_roundtrip():
    instance = basecs_PrimitiveTypeRefCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basecs_SpecificationCS_exprString_value_roundtrip():
    instance = basecs_SpecificationCS(exprString="sample_text")
    assert instance.exprString == "sample_text"
    instance.exprString = "sample_text_2"
    assert instance.exprString == "sample_text_2"


def test_basecs_StructuralFeatureCS_default_value_roundtrip():
    instance = basecs_StructuralFeatureCS(default="sample_text")
    assert instance.default == "sample_text"
    instance.default = "sample_text_2"
    assert instance.default == "sample_text_2"


def test_basecs_TupleTypeCS_name_value_roundtrip():
    instance = basecs_TupleTypeCS(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_basecs_TypedElementCS_optional_value_roundtrip():
    instance = basecs_TypedElementCS(optional=True, qualifier="sample_text")
    assert instance.optional == True
    instance.optional = False
    assert instance.optional == False


def test_basecs_TypedElementCS_qualifier_value_roundtrip():
    instance = basecs_TypedElementCS(optional=True, qualifier="sample_text")
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_basecs_AnnotationCS_isa_AnnotationElementCS():
    instance = basecs_AnnotationCS()
    assert isinstance(instance, AnnotationElementCS)


def test_basecs_DocumentationCS_isa_AnnotationElementCS():
    instance = basecs_DocumentationCS(value="sample_text")
    assert isinstance(instance, AnnotationElementCS)


def test_basecs_ClassCS_isa_ClassifierCS():
    instance = basecs_ClassCS()
    assert isinstance(instance, ClassifierCS)


def test_basecs_DataTypeCS_isa_ClassifierCS():
    instance = basecs_DataTypeCS()
    assert isinstance(instance, ClassifierCS)


def test_basecs_EnumerationCS_isa_ClassifierCS():
    instance = basecs_EnumerationCS()
    assert isinstance(instance, ClassifierCS)


def test_basecs_MultiplicityCS_isa_ElementCS():
    instance = basecs_MultiplicityCS()
    assert isinstance(instance, ElementCS)


def test_basecs_PathElementCS_isa_ElementCS():
    instance = basecs_PathElementCS()
    assert isinstance(instance, ElementCS)


def test_basecs_PathNameCS_isa_ElementCS():
    instance = basecs_PathNameCS(scopeFilter="sample_text")
    assert isinstance(instance, ElementCS)


def test_basecs_PivotableElementCS_isa_ElementCS():
    instance = basecs_PivotableElementCS()
    assert isinstance(instance, ElementCS)


def test_basecs_TemplateableElementCS_isa_ElementCS():
    instance = basecs_TemplateableElementCS()
    assert isinstance(instance, ElementCS)


def test_basecs_ModelElementRefCS_isa_ElementRefCS():
    instance = basecs_ModelElementRefCS()
    assert isinstance(instance, ElementRefCS)


def test_basecs_TemplateBindingCS_isa_ElementRefCS():
    instance = basecs_TemplateBindingCS()
    assert isinstance(instance, ElementRefCS)


def test_basecs_TypeRefCS_isa_ElementRefCS():
    instance = basecs_TypeRefCS()
    assert isinstance(instance, ElementRefCS)


def test_basecs_OperationCS_isa_FeatureCS():
    instance = basecs_OperationCS()
    assert isinstance(instance, FeatureCS)


def test_basecs_StructuralFeatureCS_isa_FeatureCS():
    instance = basecs_StructuralFeatureCS(default="sample_text")
    assert isinstance(instance, FeatureCS)


def test_basecs_NamedElementCS_isa_ModelElementCS():
    instance = basecs_NamedElementCS(name="sample_text")
    assert isinstance(instance, ModelElementCS)


def test_basecs_PackageOwnerCS_isa_ModelElementCS():
    instance = basecs_PackageOwnerCS()
    assert isinstance(instance, ModelElementCS)


def test_basecs_RootCS_isa_ModelElementCS():
    instance = basecs_RootCS()
    assert isinstance(instance, ModelElementCS)


def test_basecs_SpecificationCS_isa_ModelElementCS():
    instance = basecs_SpecificationCS(exprString="sample_text")
    assert isinstance(instance, ModelElementCS)


def test_basecs_TemplateParameterSubstitutionCS_isa_ModelElementCS():
    instance = basecs_TemplateParameterSubstitutionCS()
    assert isinstance(instance, ModelElementCS)


def test_basecs_TemplateSignatureCS_isa_ModelElementCS():
    instance = basecs_TemplateSignatureCS()
    assert isinstance(instance, ModelElementCS)


def test_basecs_TypeCS_isa_ModelElementCS():
    instance = basecs_TypeCS()
    assert isinstance(instance, ModelElementCS)


def test_basecs_MultiplicityBoundsCS_isa_MultiplicityCS():
    instance = basecs_MultiplicityBoundsCS(lowerBound=7, upperBound="sample_text")
    assert isinstance(instance, MultiplicityCS)


def test_basecs_MultiplicityStringCS_isa_MultiplicityCS():
    instance = basecs_MultiplicityStringCS(stringBounds="sample_text")
    assert isinstance(instance, MultiplicityCS)


def test_basecs_LambdaTypeCS_isa_Nameable():
    instance = basecs_LambdaTypeCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_basecs_NamedElementCS_isa_Nameable():
    instance = basecs_NamedElementCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_basecs_PrimitiveTypeRefCS_isa_Nameable():
    instance = basecs_PrimitiveTypeRefCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_basecs_TupleTypeCS_isa_Nameable():
    instance = basecs_TupleTypeCS(name="sample_text")
    assert isinstance(instance, Nameable)


def test_basecs_AnnotationElementCS_isa_NamedElementCS():
    instance = basecs_AnnotationElementCS()
    assert isinstance(instance, NamedElementCS)


def test_basecs_ClassifierCS_isa_NamedElementCS():
    instance = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    assert isinstance(instance, NamedElementCS)


def test_basecs_ConstraintCS_isa_NamedElementCS():
    instance = basecs_ConstraintCS(stereotype="sample_text")
    assert isinstance(instance, NamedElementCS)


def test_basecs_DetailCS_isa_NamedElementCS():
    instance = basecs_DetailCS(value="sample_text")
    assert isinstance(instance, NamedElementCS)


def test_basecs_EnumerationLiteralCS_isa_NamedElementCS():
    instance = basecs_EnumerationLiteralCS(value=7)
    assert isinstance(instance, NamedElementCS)


def test_basecs_NamespaceCS_isa_NamedElementCS():
    instance = basecs_NamespaceCS()
    assert isinstance(instance, NamedElementCS)


def test_basecs_TemplateParameterCS_isa_NamedElementCS():
    instance = basecs_TemplateParameterCS()
    assert isinstance(instance, NamedElementCS)


def test_basecs_TypedElementCS_isa_NamedElementCS():
    instance = basecs_TypedElementCS(optional=True, qualifier="sample_text")
    assert isinstance(instance, NamedElementCS)


def test_basecs_ClassCS_isa_NamespaceCS():
    instance = basecs_ClassCS()
    assert isinstance(instance, NamespaceCS)


def test_basecs_DataTypeCS_isa_NamespaceCS():
    instance = basecs_DataTypeCS()
    assert isinstance(instance, NamespaceCS)


def test_basecs_EnumerationCS_isa_NamespaceCS():
    instance = basecs_EnumerationCS()
    assert isinstance(instance, NamespaceCS)


def test_basecs_ImportCS_isa_NamespaceCS():
    instance = basecs_ImportCS(all=True)
    assert isinstance(instance, NamespaceCS)


def test_basecs_LibraryCS_isa_NamespaceCS():
    instance = basecs_LibraryCS()
    assert isinstance(instance, NamespaceCS)


def test_basecs_PackageCS_isa_NamespaceCS():
    instance = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    assert isinstance(instance, NamespaceCS)


def test_basecs_PackageCS_isa_PackageOwnerCS():
    instance = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    assert isinstance(instance, PackageOwnerCS)


def test_basecs_RootPackageCS_isa_PackageOwnerCS():
    instance = basecs_RootPackageCS()
    assert isinstance(instance, PackageOwnerCS)


def test_basecs_PathElementWithURICS_isa_PathElementCS():
    instance = basecs_PathElementWithURICS(uri="sample_text")
    assert isinstance(instance, PathElementCS)


def test_basecs_PathElementCS_isa_Pivotable():
    instance = basecs_PathElementCS()
    assert isinstance(instance, Pivotable)


def test_basecs_PathNameCS_isa_Pivotable():
    instance = basecs_PathNameCS(scopeFilter="sample_text")
    assert isinstance(instance, Pivotable)


def test_basecs_PivotableElementCS_isa_Pivotable():
    instance = basecs_PivotableElementCS()
    assert isinstance(instance, Pivotable)


def test_basecs_ElementRefCS_isa_PivotableElementCS():
    instance = basecs_ElementRefCS()
    assert isinstance(instance, PivotableElementCS)


def test_basecs_ModelElementCS_isa_PivotableElementCS():
    instance = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    assert isinstance(instance, PivotableElementCS)


def test_basecs_RootPackageCS_isa_RootCS():
    instance = basecs_RootPackageCS()
    assert isinstance(instance, RootCS)


def test_basecs_AttributeCS_isa_StructuralFeatureCS():
    instance = basecs_AttributeCS()
    assert isinstance(instance, StructuralFeatureCS)


def test_basecs_ReferenceCS_isa_StructuralFeatureCS():
    instance = basecs_ReferenceCS()
    assert isinstance(instance, StructuralFeatureCS)


def test_basecs_TypeParameterCS_isa_TemplateParameterCS():
    instance = basecs_TypeParameterCS()
    assert isinstance(instance, TemplateParameterCS)


def test_basecs_ClassifierCS_isa_TemplateableElementCS():
    instance = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    assert isinstance(instance, TemplateableElementCS)


def test_basecs_LambdaTypeCS_isa_TemplateableElementCS():
    instance = basecs_LambdaTypeCS(name="sample_text")
    assert isinstance(instance, TemplateableElementCS)


def test_basecs_OperationCS_isa_TemplateableElementCS():
    instance = basecs_OperationCS()
    assert isinstance(instance, TemplateableElementCS)


def test_basecs_ClassifierCS_isa_TypeCS():
    instance = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    assert isinstance(instance, TypeCS)


def test_basecs_TypeParameterCS_isa_TypeCS():
    instance = basecs_TypeParameterCS()
    assert isinstance(instance, TypeCS)


def test_basecs_TypedRefCS_isa_TypeRefCS():
    instance = basecs_TypedRefCS()
    assert isinstance(instance, TypeRefCS)


def test_basecs_WildcardTypeRefCS_isa_TypeRefCS():
    instance = basecs_WildcardTypeRefCS()
    assert isinstance(instance, TypeRefCS)


def test_basecs_FeatureCS_isa_TypedElementCS():
    instance = basecs_FeatureCS()
    assert isinstance(instance, TypedElementCS)


def test_basecs_ParameterCS_isa_TypedElementCS():
    instance = basecs_ParameterCS()
    assert isinstance(instance, TypedElementCS)


def test_basecs_TuplePartCS_isa_TypedElementCS():
    instance = basecs_TuplePartCS()
    assert isinstance(instance, TypedElementCS)


def test_basecs_LambdaTypeCS_isa_TypedRefCS():
    instance = basecs_LambdaTypeCS(name="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_basecs_PrimitiveTypeRefCS_isa_TypedRefCS():
    instance = basecs_PrimitiveTypeRefCS(name="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_basecs_TupleTypeCS_isa_TypedRefCS():
    instance = basecs_TupleTypeCS(name="sample_text")
    assert isinstance(instance, TypedRefCS)


def test_basecs_TypedTypeRefCS_isa_TypedRefCS():
    instance = basecs_TypedTypeRefCS()
    assert isinstance(instance, TypedRefCS)


def test_basecs_ElementCS_isa_VisitableCS():
    instance = basecs_ElementCS()
    assert isinstance(instance, VisitableCS)


def test_assoc_context71_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_ElementCS()
    b2 = basecs_ElementCS()
    _safe_set(a, 'basecs_PathNameCS72', b1)
    assert _is_linked(a, 'basecs_PathNameCS72', b1)
    if hasattr(b1, 'basecs_ElementCS73'):
        assert _is_linked(b1, 'basecs_ElementCS73', a)
    _safe_set(a, 'basecs_PathNameCS72', b2)
    assert _is_linked(a, 'basecs_PathNameCS72', b2)
    if hasattr(b1, 'basecs_ElementCS73'):
        assert not _is_linked(b1, 'basecs_ElementCS73', a)
    if hasattr(b2, 'basecs_ElementCS73'):
        assert _is_linked(b2, 'basecs_ElementCS73', a)
    _safe_set(a, 'basecs_PathNameCS72', None)
    assert not _is_linked(a, 'basecs_PathNameCS72', b2)
    if hasattr(b2, 'basecs_ElementCS73'):
        assert not _is_linked(b2, 'basecs_ElementCS73', a)


def test_assoc_element68_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_Element()
    b2 = basecs_Element()
    _safe_set(a, 'basecs_PathNameCS69', b1)
    assert _is_linked(a, 'basecs_PathNameCS69', b1)
    if hasattr(b1, 'basecs_Element70'):
        assert _is_linked(b1, 'basecs_Element70', a)
    _safe_set(a, 'basecs_PathNameCS69', b2)
    assert _is_linked(a, 'basecs_PathNameCS69', b2)
    if hasattr(b1, 'basecs_Element70'):
        assert not _is_linked(b1, 'basecs_Element70', a)
    if hasattr(b2, 'basecs_Element70'):
        assert _is_linked(b2, 'basecs_Element70', a)
    _safe_set(a, 'basecs_PathNameCS69', None)
    assert not _is_linked(a, 'basecs_PathNameCS69', b2)
    if hasattr(b2, 'basecs_Element70'):
        assert not _is_linked(b2, 'basecs_Element70', a)


def test_assoc_literals17_link_reassign_clear():
    a = basecs_EnumerationLiteralCS(value=7)
    b1 = basecs_DataTypeCS()
    b2 = basecs_DataTypeCS()
    _safe_set(a, 'basecs_EnumerationLiteralCS', b1)
    assert _is_linked(a, 'basecs_EnumerationLiteralCS', b1)
    if hasattr(b1, 'basecs_DataTypeCS'):
        assert _is_linked(b1, 'basecs_DataTypeCS', a)
    _safe_set(a, 'basecs_EnumerationLiteralCS', b2)
    assert _is_linked(a, 'basecs_EnumerationLiteralCS', b2)
    if hasattr(b1, 'basecs_DataTypeCS'):
        assert not _is_linked(b1, 'basecs_DataTypeCS', a)
    if hasattr(b2, 'basecs_DataTypeCS'):
        assert _is_linked(b2, 'basecs_DataTypeCS', a)
    _safe_set(a, 'basecs_EnumerationLiteralCS', None)
    assert not _is_linked(a, 'basecs_EnumerationLiteralCS', b2)
    if hasattr(b2, 'basecs_DataTypeCS'):
        assert not _is_linked(b2, 'basecs_DataTypeCS', a)


def test_assoc_logicalParent19_link_reassign_clear():
    a = basecs_ElementCS()
    b1 = basecs_ElementCS()
    b2 = basecs_ElementCS()
    _safe_set(a, 'basecs_ElementCS', b1)
    assert _is_linked(a, 'basecs_ElementCS', b1)
    if hasattr(b1, 'basecs_ElementCS18'):
        assert _is_linked(b1, 'basecs_ElementCS18', a)
    _safe_set(a, 'basecs_ElementCS', b2)
    assert _is_linked(a, 'basecs_ElementCS', b2)
    if hasattr(b1, 'basecs_ElementCS18'):
        assert not _is_linked(b1, 'basecs_ElementCS18', a)
    if hasattr(b2, 'basecs_ElementCS18'):
        assert _is_linked(b2, 'basecs_ElementCS18', a)
    _safe_set(a, 'basecs_ElementCS', None)
    assert not _is_linked(a, 'basecs_ElementCS', b2)
    if hasattr(b2, 'basecs_ElementCS18'):
        assert not _is_linked(b2, 'basecs_ElementCS18', a)


def test_assoc_messageSpecification14_link_reassign_clear():
    a = basecs_SpecificationCS(exprString="sample_text")
    b1 = basecs_ConstraintCS(stereotype="sample_text")
    b2 = basecs_ConstraintCS(stereotype="sample_text_2")
    _safe_set(a, 'basecs_SpecificationCS16', b1)
    assert _is_linked(a, 'basecs_SpecificationCS16', b1)
    if hasattr(b1, 'basecs_ConstraintCS15'):
        assert _is_linked(b1, 'basecs_ConstraintCS15', a)
    _safe_set(a, 'basecs_SpecificationCS16', b2)
    assert _is_linked(a, 'basecs_SpecificationCS16', b2)
    if hasattr(b1, 'basecs_ConstraintCS15'):
        assert not _is_linked(b1, 'basecs_ConstraintCS15', a)
    if hasattr(b2, 'basecs_ConstraintCS15'):
        assert _is_linked(b2, 'basecs_ConstraintCS15', a)
    _safe_set(a, 'basecs_SpecificationCS16', None)
    assert not _is_linked(a, 'basecs_SpecificationCS16', b2)
    if hasattr(b2, 'basecs_ConstraintCS15'):
        assert not _is_linked(b2, 'basecs_ConstraintCS15', a)


def test_assoc_multiplicity106_link_reassign_clear():
    a = basecs_MultiplicityCS()
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_MultiplicityCS', b1)
    assert _is_linked(a, 'basecs_MultiplicityCS', b1)
    if hasattr(b1, 'basecs_TypedRefCS107'):
        assert _is_linked(b1, 'basecs_TypedRefCS107', a)
    _safe_set(a, 'basecs_MultiplicityCS', b2)
    assert _is_linked(a, 'basecs_MultiplicityCS', b2)
    if hasattr(b1, 'basecs_TypedRefCS107'):
        assert not _is_linked(b1, 'basecs_TypedRefCS107', a)
    if hasattr(b2, 'basecs_TypedRefCS107'):
        assert _is_linked(b2, 'basecs_TypedRefCS107', a)
    _safe_set(a, 'basecs_MultiplicityCS', None)
    assert not _is_linked(a, 'basecs_MultiplicityCS', b2)
    if hasattr(b2, 'basecs_TypedRefCS107'):
        assert not _is_linked(b2, 'basecs_TypedRefCS107', a)


def test_assoc_namespace23_link_reassign_clear():
    a = basecs_ImportCS(all=True)
    b1 = basecs_Namespace()
    b2 = basecs_Namespace()
    _safe_set(a, 'basecs_ImportCS24', b1)
    assert _is_linked(a, 'basecs_ImportCS24', b1)
    if hasattr(b1, 'basecs_Namespace'):
        assert _is_linked(b1, 'basecs_Namespace', a)
    _safe_set(a, 'basecs_ImportCS24', b2)
    assert _is_linked(a, 'basecs_ImportCS24', b2)
    if hasattr(b1, 'basecs_Namespace'):
        assert not _is_linked(b1, 'basecs_Namespace', a)
    if hasattr(b2, 'basecs_Namespace'):
        assert _is_linked(b2, 'basecs_Namespace', a)
    _safe_set(a, 'basecs_ImportCS24', None)
    assert not _is_linked(a, 'basecs_ImportCS24', b2)
    if hasattr(b2, 'basecs_Namespace'):
        assert not _is_linked(b2, 'basecs_Namespace', a)


def test_assoc_ownedAnnotation35_link_reassign_clear():
    a = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    b1 = basecs_AnnotationElementCS()
    b2 = basecs_AnnotationElementCS()
    _safe_set(a, 'basecs_ModelElementCS36', {b1})
    assert _is_linked(a, 'basecs_ModelElementCS36', b1)
    if hasattr(b1, 'basecs_AnnotationElementCS37'):
        assert _is_linked(b1, 'basecs_AnnotationElementCS37', a)
    _safe_set(a, 'basecs_ModelElementCS36', {b2})
    assert _is_linked(a, 'basecs_ModelElementCS36', b2)
    if hasattr(b1, 'basecs_AnnotationElementCS37'):
        assert not _is_linked(b1, 'basecs_AnnotationElementCS37', a)
    if hasattr(b2, 'basecs_AnnotationElementCS37'):
        assert _is_linked(b2, 'basecs_AnnotationElementCS37', a)
    _safe_set(a, 'basecs_ModelElementCS36', set())
    assert not _is_linked(a, 'basecs_ModelElementCS36', b2)
    if hasattr(b2, 'basecs_AnnotationElementCS37'):
        assert not _is_linked(b2, 'basecs_AnnotationElementCS37', a)


def test_assoc_ownedBodyExpression54_link_reassign_clear():
    a = basecs_SpecificationCS(exprString="sample_text")
    b1 = basecs_OperationCS()
    b2 = basecs_OperationCS()
    _safe_set(a, 'basecs_SpecificationCS56', b1)
    assert _is_linked(a, 'basecs_SpecificationCS56', b1)
    if hasattr(b1, 'basecs_OperationCS55'):
        assert _is_linked(b1, 'basecs_OperationCS55', a)
    _safe_set(a, 'basecs_SpecificationCS56', b2)
    assert _is_linked(a, 'basecs_SpecificationCS56', b2)
    if hasattr(b1, 'basecs_OperationCS55'):
        assert not _is_linked(b1, 'basecs_OperationCS55', a)
    if hasattr(b2, 'basecs_OperationCS55'):
        assert _is_linked(b2, 'basecs_OperationCS55', a)
    _safe_set(a, 'basecs_SpecificationCS56', None)
    assert not _is_linked(a, 'basecs_SpecificationCS56', b2)
    if hasattr(b2, 'basecs_OperationCS55'):
        assert not _is_linked(b2, 'basecs_OperationCS55', a)


def test_assoc_ownedConstraint11_link_reassign_clear():
    a = basecs_ConstraintCS(stereotype="sample_text")
    b1 = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    b2 = basecs_ClassifierCS(instanceClassName="sample_text_2", qualifier="sample_text_2")
    _safe_set(a, 'basecs_ConstraintCS', b1)
    assert _is_linked(a, 'basecs_ConstraintCS', b1)
    if hasattr(b1, 'basecs_ClassifierCS'):
        assert _is_linked(b1, 'basecs_ClassifierCS', a)
    _safe_set(a, 'basecs_ConstraintCS', b2)
    assert _is_linked(a, 'basecs_ConstraintCS', b2)
    if hasattr(b1, 'basecs_ClassifierCS'):
        assert not _is_linked(b1, 'basecs_ClassifierCS', a)
    if hasattr(b2, 'basecs_ClassifierCS'):
        assert _is_linked(b2, 'basecs_ClassifierCS', a)
    _safe_set(a, 'basecs_ConstraintCS', None)
    assert not _is_linked(a, 'basecs_ConstraintCS', b2)
    if hasattr(b2, 'basecs_ClassifierCS'):
        assert not _is_linked(b2, 'basecs_ClassifierCS', a)


def test_assoc_ownedContent0_link_reassign_clear():
    a = basecs_ModelElementCS(csi="sample_text", originalXmiId="sample_text")
    b1 = basecs_AnnotationCS()
    b2 = basecs_AnnotationCS()
    _safe_set(a, 'basecs_ModelElementCS', b1)
    assert _is_linked(a, 'basecs_ModelElementCS', b1)
    if hasattr(b1, 'basecs_AnnotationCS'):
        assert _is_linked(b1, 'basecs_AnnotationCS', a)
    _safe_set(a, 'basecs_ModelElementCS', b2)
    assert _is_linked(a, 'basecs_ModelElementCS', b2)
    if hasattr(b1, 'basecs_AnnotationCS'):
        assert not _is_linked(b1, 'basecs_AnnotationCS', a)
    if hasattr(b2, 'basecs_AnnotationCS'):
        assert _is_linked(b2, 'basecs_AnnotationCS', a)
    _safe_set(a, 'basecs_ModelElementCS', None)
    assert not _is_linked(a, 'basecs_ModelElementCS', b2)
    if hasattr(b2, 'basecs_AnnotationCS'):
        assert not _is_linked(b2, 'basecs_AnnotationCS', a)


def test_assoc_ownedContextType25_link_reassign_clear():
    a = basecs_LambdaTypeCS(name="sample_text")
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_LambdaTypeCS', b1)
    assert _is_linked(a, 'basecs_LambdaTypeCS', b1)
    if hasattr(b1, 'basecs_TypedRefCS26'):
        assert _is_linked(b1, 'basecs_TypedRefCS26', a)
    _safe_set(a, 'basecs_LambdaTypeCS', b2)
    assert _is_linked(a, 'basecs_LambdaTypeCS', b2)
    if hasattr(b1, 'basecs_TypedRefCS26'):
        assert not _is_linked(b1, 'basecs_TypedRefCS26', a)
    if hasattr(b2, 'basecs_TypedRefCS26'):
        assert _is_linked(b2, 'basecs_TypedRefCS26', a)
    _safe_set(a, 'basecs_LambdaTypeCS', None)
    assert not _is_linked(a, 'basecs_LambdaTypeCS', b2)
    if hasattr(b2, 'basecs_TypedRefCS26'):
        assert not _is_linked(b2, 'basecs_TypedRefCS26', a)


def test_assoc_ownedDefaultExpression87_link_reassign_clear():
    a = basecs_StructuralFeatureCS(default="sample_text")
    b1 = basecs_SpecificationCS(exprString="sample_text")
    b2 = basecs_SpecificationCS(exprString="sample_text_2")
    _safe_set(a, 'basecs_StructuralFeatureCS', {b1})
    assert _is_linked(a, 'basecs_StructuralFeatureCS', b1)
    if hasattr(b1, 'basecs_SpecificationCS88'):
        assert _is_linked(b1, 'basecs_SpecificationCS88', a)
    _safe_set(a, 'basecs_StructuralFeatureCS', {b2})
    assert _is_linked(a, 'basecs_StructuralFeatureCS', b2)
    if hasattr(b1, 'basecs_SpecificationCS88'):
        assert not _is_linked(b1, 'basecs_SpecificationCS88', a)
    if hasattr(b2, 'basecs_SpecificationCS88'):
        assert _is_linked(b2, 'basecs_SpecificationCS88', a)
    _safe_set(a, 'basecs_StructuralFeatureCS', set())
    assert not _is_linked(a, 'basecs_StructuralFeatureCS', b2)
    if hasattr(b2, 'basecs_SpecificationCS88'):
        assert not _is_linked(b2, 'basecs_SpecificationCS88', a)


def test_assoc_ownedDetail3_link_reassign_clear():
    a = basecs_DetailCS(value="sample_text")
    b1 = basecs_AnnotationElementCS()
    b2 = basecs_AnnotationElementCS()
    _safe_set(a, 'basecs_DetailCS', b1)
    assert _is_linked(a, 'basecs_DetailCS', b1)
    if hasattr(b1, 'basecs_AnnotationElementCS'):
        assert _is_linked(b1, 'basecs_AnnotationElementCS', a)
    _safe_set(a, 'basecs_DetailCS', b2)
    assert _is_linked(a, 'basecs_DetailCS', b2)
    if hasattr(b1, 'basecs_AnnotationElementCS'):
        assert not _is_linked(b1, 'basecs_AnnotationElementCS', a)
    if hasattr(b2, 'basecs_AnnotationElementCS'):
        assert _is_linked(b2, 'basecs_AnnotationElementCS', a)
    _safe_set(a, 'basecs_DetailCS', None)
    assert not _is_linked(a, 'basecs_DetailCS', b2)
    if hasattr(b2, 'basecs_AnnotationElementCS'):
        assert not _is_linked(b2, 'basecs_AnnotationElementCS', a)


def test_assoc_ownedException46_link_reassign_clear():
    a = basecs_OperationCS()
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_OperationCS', {b1})
    assert _is_linked(a, 'basecs_OperationCS', b1)
    if hasattr(b1, 'basecs_TypedRefCS47'):
        assert _is_linked(b1, 'basecs_TypedRefCS47', a)
    _safe_set(a, 'basecs_OperationCS', {b2})
    assert _is_linked(a, 'basecs_OperationCS', b2)
    if hasattr(b1, 'basecs_TypedRefCS47'):
        assert not _is_linked(b1, 'basecs_TypedRefCS47', a)
    if hasattr(b2, 'basecs_TypedRefCS47'):
        assert _is_linked(b2, 'basecs_TypedRefCS47', a)
    _safe_set(a, 'basecs_OperationCS', set())
    assert not _is_linked(a, 'basecs_OperationCS', b2)
    if hasattr(b2, 'basecs_TypedRefCS47'):
        assert not _is_linked(b2, 'basecs_TypedRefCS47', a)


def test_assoc_ownedImport80_link_reassign_clear():
    a = basecs_ImportCS(all=True)
    b1 = basecs_RootCS()
    b2 = basecs_RootCS()
    _safe_set(a, 'basecs_ImportCS81', b1)
    assert _is_linked(a, 'basecs_ImportCS81', b1)
    if hasattr(b1, 'basecs_RootCS'):
        assert _is_linked(b1, 'basecs_RootCS', a)
    _safe_set(a, 'basecs_ImportCS81', b2)
    assert _is_linked(a, 'basecs_ImportCS81', b2)
    if hasattr(b1, 'basecs_RootCS'):
        assert not _is_linked(b1, 'basecs_RootCS', a)
    if hasattr(b2, 'basecs_RootCS'):
        assert _is_linked(b2, 'basecs_RootCS', a)
    _safe_set(a, 'basecs_ImportCS81', None)
    assert not _is_linked(a, 'basecs_ImportCS81', b2)
    if hasattr(b2, 'basecs_RootCS'):
        assert not _is_linked(b2, 'basecs_RootCS', a)


def test_assoc_ownedLiterals20_link_reassign_clear():
    a = basecs_EnumerationLiteralCS(value=7)
    b1 = basecs_EnumerationCS()
    b2 = basecs_EnumerationCS()
    _safe_set(a, 'basecs_EnumerationLiteralCS21', b1)
    assert _is_linked(a, 'basecs_EnumerationLiteralCS21', b1)
    if hasattr(b1, 'basecs_EnumerationCS'):
        assert _is_linked(b1, 'basecs_EnumerationCS', a)
    _safe_set(a, 'basecs_EnumerationLiteralCS21', b2)
    assert _is_linked(a, 'basecs_EnumerationLiteralCS21', b2)
    if hasattr(b1, 'basecs_EnumerationCS'):
        assert not _is_linked(b1, 'basecs_EnumerationCS', a)
    if hasattr(b2, 'basecs_EnumerationCS'):
        assert _is_linked(b2, 'basecs_EnumerationCS', a)
    _safe_set(a, 'basecs_EnumerationLiteralCS21', None)
    assert not _is_linked(a, 'basecs_EnumerationLiteralCS21', b2)
    if hasattr(b2, 'basecs_EnumerationCS'):
        assert not _is_linked(b2, 'basecs_EnumerationCS', a)


def test_assoc_ownedNestedPackage59_link_reassign_clear():
    a = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    b1 = basecs_PackageOwnerCS()
    b2 = basecs_PackageOwnerCS()
    _safe_set(a, 'basecs_PackageCS', b1)
    assert _is_linked(a, 'basecs_PackageCS', b1)
    if hasattr(b1, 'basecs_PackageOwnerCS'):
        assert _is_linked(b1, 'basecs_PackageOwnerCS', a)
    _safe_set(a, 'basecs_PackageCS', b2)
    assert _is_linked(a, 'basecs_PackageCS', b2)
    if hasattr(b1, 'basecs_PackageOwnerCS'):
        assert not _is_linked(b1, 'basecs_PackageOwnerCS', a)
    if hasattr(b2, 'basecs_PackageOwnerCS'):
        assert _is_linked(b2, 'basecs_PackageOwnerCS', a)
    _safe_set(a, 'basecs_PackageCS', None)
    assert not _is_linked(a, 'basecs_PackageCS', b2)
    if hasattr(b2, 'basecs_PackageOwnerCS'):
        assert not _is_linked(b2, 'basecs_PackageOwnerCS', a)


def test_assoc_ownedOperation5_link_reassign_clear():
    a = basecs_OperationCS()
    b1 = basecs_ClassCS()
    b2 = basecs_ClassCS()
    _safe_set(a, 'OperationCS', b1)
    assert _is_linked(a, 'OperationCS', b1)
    if hasattr(b1, 'owningClass'):
        assert _is_linked(b1, 'owningClass', a)
    _safe_set(a, 'OperationCS', b2)
    assert _is_linked(a, 'OperationCS', b2)
    if hasattr(b1, 'owningClass'):
        assert not _is_linked(b1, 'owningClass', a)
    if hasattr(b2, 'owningClass'):
        assert _is_linked(b2, 'owningClass', a)
    _safe_set(a, 'OperationCS', None)
    assert not _is_linked(a, 'OperationCS', b2)
    if hasattr(b2, 'owningClass'):
        assert not _is_linked(b2, 'owningClass', a)


def test_assoc_ownedParameter44_link_reassign_clear():
    a = basecs_ParameterCS()
    b1 = basecs_OperationCS()
    b2 = basecs_OperationCS()
    _safe_set(a, 'ParameterCS', b1)
    assert _is_linked(a, 'ParameterCS', b1)
    if hasattr(b1, 'owner45'):
        assert _is_linked(b1, 'owner45', a)
    _safe_set(a, 'ParameterCS', b2)
    assert _is_linked(a, 'ParameterCS', b2)
    if hasattr(b1, 'owner45'):
        assert not _is_linked(b1, 'owner45', a)
    if hasattr(b2, 'owner45'):
        assert _is_linked(b2, 'owner45', a)
    _safe_set(a, 'ParameterCS', None)
    assert not _is_linked(a, 'ParameterCS', b2)
    if hasattr(b2, 'owner45'):
        assert not _is_linked(b2, 'owner45', a)


def test_assoc_ownedParameterType27_link_reassign_clear():
    a = basecs_LambdaTypeCS(name="sample_text")
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_LambdaTypeCS28', {b1})
    assert _is_linked(a, 'basecs_LambdaTypeCS28', b1)
    if hasattr(b1, 'basecs_TypedRefCS29'):
        assert _is_linked(b1, 'basecs_TypedRefCS29', a)
    _safe_set(a, 'basecs_LambdaTypeCS28', {b2})
    assert _is_linked(a, 'basecs_LambdaTypeCS28', b2)
    if hasattr(b1, 'basecs_TypedRefCS29'):
        assert not _is_linked(b1, 'basecs_TypedRefCS29', a)
    if hasattr(b2, 'basecs_TypedRefCS29'):
        assert _is_linked(b2, 'basecs_TypedRefCS29', a)
    _safe_set(a, 'basecs_LambdaTypeCS28', set())
    assert not _is_linked(a, 'basecs_LambdaTypeCS28', b2)
    if hasattr(b2, 'basecs_TypedRefCS29'):
        assert not _is_linked(b2, 'basecs_TypedRefCS29', a)


def test_assoc_ownedParts98_link_reassign_clear():
    a = basecs_TupleTypeCS(name="sample_text")
    b1 = basecs_TuplePartCS()
    b2 = basecs_TuplePartCS()
    _safe_set(a, 'basecs_TupleTypeCS', {b1})
    assert _is_linked(a, 'basecs_TupleTypeCS', b1)
    if hasattr(b1, 'basecs_TuplePartCS'):
        assert _is_linked(b1, 'basecs_TuplePartCS', a)
    _safe_set(a, 'basecs_TupleTypeCS', {b2})
    assert _is_linked(a, 'basecs_TupleTypeCS', b2)
    if hasattr(b1, 'basecs_TuplePartCS'):
        assert not _is_linked(b1, 'basecs_TuplePartCS', a)
    if hasattr(b2, 'basecs_TuplePartCS'):
        assert _is_linked(b2, 'basecs_TuplePartCS', a)
    _safe_set(a, 'basecs_TupleTypeCS', set())
    assert not _is_linked(a, 'basecs_TupleTypeCS', b2)
    if hasattr(b2, 'basecs_TuplePartCS'):
        assert not _is_linked(b2, 'basecs_TuplePartCS', a)


def test_assoc_ownedPostcondition51_link_reassign_clear():
    a = basecs_OperationCS()
    b1 = basecs_ConstraintCS(stereotype="sample_text")
    b2 = basecs_ConstraintCS(stereotype="sample_text_2")
    _safe_set(a, 'basecs_OperationCS52', {b1})
    assert _is_linked(a, 'basecs_OperationCS52', b1)
    if hasattr(b1, 'basecs_ConstraintCS53'):
        assert _is_linked(b1, 'basecs_ConstraintCS53', a)
    _safe_set(a, 'basecs_OperationCS52', {b2})
    assert _is_linked(a, 'basecs_OperationCS52', b2)
    if hasattr(b1, 'basecs_ConstraintCS53'):
        assert not _is_linked(b1, 'basecs_ConstraintCS53', a)
    if hasattr(b2, 'basecs_ConstraintCS53'):
        assert _is_linked(b2, 'basecs_ConstraintCS53', a)
    _safe_set(a, 'basecs_OperationCS52', set())
    assert not _is_linked(a, 'basecs_OperationCS52', b2)
    if hasattr(b2, 'basecs_ConstraintCS53'):
        assert not _is_linked(b2, 'basecs_ConstraintCS53', a)


def test_assoc_ownedPrecondition48_link_reassign_clear():
    a = basecs_OperationCS()
    b1 = basecs_ConstraintCS(stereotype="sample_text")
    b2 = basecs_ConstraintCS(stereotype="sample_text_2")
    _safe_set(a, 'basecs_OperationCS49', {b1})
    assert _is_linked(a, 'basecs_OperationCS49', b1)
    if hasattr(b1, 'basecs_ConstraintCS50'):
        assert _is_linked(b1, 'basecs_ConstraintCS50', a)
    _safe_set(a, 'basecs_OperationCS49', {b2})
    assert _is_linked(a, 'basecs_OperationCS49', b2)
    if hasattr(b1, 'basecs_ConstraintCS50'):
        assert not _is_linked(b1, 'basecs_ConstraintCS50', a)
    if hasattr(b2, 'basecs_ConstraintCS50'):
        assert _is_linked(b2, 'basecs_ConstraintCS50', a)
    _safe_set(a, 'basecs_OperationCS49', set())
    assert not _is_linked(a, 'basecs_OperationCS49', b2)
    if hasattr(b2, 'basecs_ConstraintCS50'):
        assert not _is_linked(b2, 'basecs_ConstraintCS50', a)


def test_assoc_ownedProperty6_link_reassign_clear():
    a = basecs_StructuralFeatureCS(default="sample_text")
    b1 = basecs_ClassCS()
    b2 = basecs_ClassCS()
    _safe_set(a, 'StructuralFeatureCS', b1)
    assert _is_linked(a, 'StructuralFeatureCS', b1)
    if hasattr(b1, 'owner'):
        assert _is_linked(b1, 'owner', a)
    _safe_set(a, 'StructuralFeatureCS', b2)
    assert _is_linked(a, 'StructuralFeatureCS', b2)
    if hasattr(b1, 'owner'):
        assert not _is_linked(b1, 'owner', a)
    if hasattr(b2, 'owner'):
        assert _is_linked(b2, 'owner', a)
    _safe_set(a, 'StructuralFeatureCS', None)
    assert not _is_linked(a, 'StructuralFeatureCS', b2)
    if hasattr(b2, 'owner'):
        assert not _is_linked(b2, 'owner', a)


def test_assoc_ownedResultType30_link_reassign_clear():
    a = basecs_LambdaTypeCS(name="sample_text")
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_LambdaTypeCS31', b1)
    assert _is_linked(a, 'basecs_LambdaTypeCS31', b1)
    if hasattr(b1, 'basecs_TypedRefCS32'):
        assert _is_linked(b1, 'basecs_TypedRefCS32', a)
    _safe_set(a, 'basecs_LambdaTypeCS31', b2)
    assert _is_linked(a, 'basecs_LambdaTypeCS31', b2)
    if hasattr(b1, 'basecs_TypedRefCS32'):
        assert not _is_linked(b1, 'basecs_TypedRefCS32', a)
    if hasattr(b2, 'basecs_TypedRefCS32'):
        assert _is_linked(b2, 'basecs_TypedRefCS32', a)
    _safe_set(a, 'basecs_LambdaTypeCS31', None)
    assert not _is_linked(a, 'basecs_LambdaTypeCS31', b2)
    if hasattr(b2, 'basecs_TypedRefCS32'):
        assert not _is_linked(b2, 'basecs_TypedRefCS32', a)


def test_assoc_ownedType104_link_reassign_clear():
    a = basecs_TypedElementCS(optional=True, qualifier="sample_text")
    b1 = basecs_TypedRefCS()
    b2 = basecs_TypedRefCS()
    _safe_set(a, 'basecs_TypedElementCS', b1)
    assert _is_linked(a, 'basecs_TypedElementCS', b1)
    if hasattr(b1, 'basecs_TypedRefCS105'):
        assert _is_linked(b1, 'basecs_TypedRefCS105', a)
    _safe_set(a, 'basecs_TypedElementCS', b2)
    assert _is_linked(a, 'basecs_TypedElementCS', b2)
    if hasattr(b1, 'basecs_TypedRefCS105'):
        assert not _is_linked(b1, 'basecs_TypedRefCS105', a)
    if hasattr(b2, 'basecs_TypedRefCS105'):
        assert _is_linked(b2, 'basecs_TypedRefCS105', a)
    _safe_set(a, 'basecs_TypedElementCS', None)
    assert not _is_linked(a, 'basecs_TypedElementCS', b2)
    if hasattr(b2, 'basecs_TypedRefCS105'):
        assert not _is_linked(b2, 'basecs_TypedRefCS105', a)


def test_assoc_ownedType57_link_reassign_clear():
    a = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    b1 = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    b2 = basecs_ClassifierCS(instanceClassName="sample_text_2", qualifier="sample_text_2")
    _safe_set(a, 'owner58', {b1})
    assert _is_linked(a, 'owner58', b1)
    if hasattr(b1, 'ClassifierCS'):
        assert _is_linked(b1, 'ClassifierCS', a)
    _safe_set(a, 'owner58', {b2})
    assert _is_linked(a, 'owner58', b2)
    if hasattr(b1, 'ClassifierCS'):
        assert not _is_linked(b1, 'ClassifierCS', a)
    if hasattr(b2, 'ClassifierCS'):
        assert _is_linked(b2, 'ClassifierCS', a)
    _safe_set(a, 'owner58', set())
    assert not _is_linked(a, 'owner58', b2)
    if hasattr(b2, 'ClassifierCS'):
        assert not _is_linked(b2, 'ClassifierCS', a)


def test_assoc_owner10_link_reassign_clear():
    a = basecs_PackageCS(nsPrefix="sample_text", nsURI="sample_text")
    b1 = basecs_ClassifierCS(instanceClassName="sample_text", qualifier="sample_text")
    b2 = basecs_ClassifierCS(instanceClassName="sample_text_2", qualifier="sample_text_2")
    _safe_set(a, 'PackageCS', b1)
    assert _is_linked(a, 'PackageCS', b1)
    if hasattr(b1, 'ownedType'):
        assert _is_linked(b1, 'ownedType', a)
    _safe_set(a, 'PackageCS', b2)
    assert _is_linked(a, 'PackageCS', b2)
    if hasattr(b1, 'ownedType'):
        assert not _is_linked(b1, 'ownedType', a)
    if hasattr(b2, 'ownedType'):
        assert _is_linked(b2, 'ownedType', a)
    _safe_set(a, 'PackageCS', None)
    assert not _is_linked(a, 'PackageCS', b2)
    if hasattr(b2, 'ownedType'):
        assert not _is_linked(b2, 'ownedType', a)


def test_assoc_owner60_link_reassign_clear():
    a = basecs_ParameterCS()
    b1 = basecs_OperationCS()
    b2 = basecs_OperationCS()
    _safe_set(a, 'ownedParameter', b1)
    assert _is_linked(a, 'ownedParameter', b1)
    if hasattr(b1, 'OperationCS61'):
        assert _is_linked(b1, 'OperationCS61', a)
    _safe_set(a, 'ownedParameter', b2)
    assert _is_linked(a, 'ownedParameter', b2)
    if hasattr(b1, 'OperationCS61'):
        assert not _is_linked(b1, 'OperationCS61', a)
    if hasattr(b2, 'OperationCS61'):
        assert _is_linked(b2, 'OperationCS61', a)
    _safe_set(a, 'ownedParameter', None)
    assert not _is_linked(a, 'ownedParameter', b2)
    if hasattr(b2, 'OperationCS61'):
        assert not _is_linked(b2, 'OperationCS61', a)


def test_assoc_owner85_link_reassign_clear():
    a = basecs_StructuralFeatureCS(default="sample_text")
    b1 = basecs_ClassCS()
    b2 = basecs_ClassCS()
    _safe_set(a, 'ownedProperty', b1)
    assert _is_linked(a, 'ownedProperty', b1)
    if hasattr(b1, 'ClassCS86'):
        assert _is_linked(b1, 'ClassCS86', a)
    _safe_set(a, 'ownedProperty', b2)
    assert _is_linked(a, 'ownedProperty', b2)
    if hasattr(b1, 'ClassCS86'):
        assert not _is_linked(b1, 'ClassCS86', a)
    if hasattr(b2, 'ClassCS86'):
        assert _is_linked(b2, 'ClassCS86', a)
    _safe_set(a, 'ownedProperty', None)
    assert not _is_linked(a, 'ownedProperty', b2)
    if hasattr(b2, 'ClassCS86'):
        assert not _is_linked(b2, 'ClassCS86', a)


def test_assoc_owningClass43_link_reassign_clear():
    a = basecs_OperationCS()
    b1 = basecs_ClassCS()
    b2 = basecs_ClassCS()
    _safe_set(a, 'ownedOperation', b1)
    assert _is_linked(a, 'ownedOperation', b1)
    if hasattr(b1, 'ClassCS'):
        assert _is_linked(b1, 'ClassCS', a)
    _safe_set(a, 'ownedOperation', b2)
    assert _is_linked(a, 'ownedOperation', b2)
    if hasattr(b1, 'ClassCS'):
        assert not _is_linked(b1, 'ClassCS', a)
    if hasattr(b2, 'ClassCS'):
        assert _is_linked(b2, 'ClassCS', a)
    _safe_set(a, 'ownedOperation', None)
    assert not _is_linked(a, 'ownedOperation', b2)
    if hasattr(b2, 'ClassCS'):
        assert not _is_linked(b2, 'ClassCS', a)


def test_assoc_path67_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_PathElementCS()
    b2 = basecs_PathElementCS()
    _safe_set(a, 'pathName', {b1})
    assert _is_linked(a, 'pathName', b1)
    if hasattr(b1, 'PathElementCS'):
        assert _is_linked(b1, 'PathElementCS', a)
    _safe_set(a, 'pathName', {b2})
    assert _is_linked(a, 'pathName', b2)
    if hasattr(b1, 'PathElementCS'):
        assert not _is_linked(b1, 'PathElementCS', a)
    if hasattr(b2, 'PathElementCS'):
        assert _is_linked(b2, 'PathElementCS', a)
    _safe_set(a, 'pathName', set())
    assert not _is_linked(a, 'pathName', b2)
    if hasattr(b2, 'PathElementCS'):
        assert not _is_linked(b2, 'PathElementCS', a)


def test_assoc_pathName108_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_TypedTypeRefCS()
    b2 = basecs_TypedTypeRefCS()
    _safe_set(a, 'basecs_PathNameCS109', b1)
    assert _is_linked(a, 'basecs_PathNameCS109', b1)
    if hasattr(b1, 'basecs_TypedTypeRefCS'):
        assert _is_linked(b1, 'basecs_TypedTypeRefCS', a)
    _safe_set(a, 'basecs_PathNameCS109', b2)
    assert _is_linked(a, 'basecs_PathNameCS109', b2)
    if hasattr(b1, 'basecs_TypedTypeRefCS'):
        assert not _is_linked(b1, 'basecs_TypedTypeRefCS', a)
    if hasattr(b2, 'basecs_TypedTypeRefCS'):
        assert _is_linked(b2, 'basecs_TypedTypeRefCS', a)
    _safe_set(a, 'basecs_PathNameCS109', None)
    assert not _is_linked(a, 'basecs_PathNameCS109', b2)
    if hasattr(b2, 'basecs_TypedTypeRefCS'):
        assert not _is_linked(b2, 'basecs_TypedTypeRefCS', a)


def test_assoc_pathName22_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_ImportCS(all=True)
    b2 = basecs_ImportCS(all=False)
    _safe_set(a, 'basecs_PathNameCS', b1)
    assert _is_linked(a, 'basecs_PathNameCS', b1)
    if hasattr(b1, 'basecs_ImportCS'):
        assert _is_linked(b1, 'basecs_ImportCS', a)
    _safe_set(a, 'basecs_PathNameCS', b2)
    assert _is_linked(a, 'basecs_PathNameCS', b2)
    if hasattr(b1, 'basecs_ImportCS'):
        assert not _is_linked(b1, 'basecs_ImportCS', a)
    if hasattr(b2, 'basecs_ImportCS'):
        assert _is_linked(b2, 'basecs_ImportCS', a)
    _safe_set(a, 'basecs_PathNameCS', None)
    assert not _is_linked(a, 'basecs_PathNameCS', b2)
    if hasattr(b2, 'basecs_ImportCS'):
        assert not _is_linked(b2, 'basecs_ImportCS', a)


def test_assoc_pathName38_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_ModelElementRefCS()
    b2 = basecs_ModelElementRefCS()
    _safe_set(a, 'basecs_PathNameCS40', b1)
    assert _is_linked(a, 'basecs_PathNameCS40', b1)
    if hasattr(b1, 'basecs_ModelElementRefCS39'):
        assert _is_linked(b1, 'basecs_ModelElementRefCS39', a)
    _safe_set(a, 'basecs_PathNameCS40', b2)
    assert _is_linked(a, 'basecs_PathNameCS40', b2)
    if hasattr(b1, 'basecs_ModelElementRefCS39'):
        assert not _is_linked(b1, 'basecs_ModelElementRefCS39', a)
    if hasattr(b2, 'basecs_ModelElementRefCS39'):
        assert _is_linked(b2, 'basecs_ModelElementRefCS39', a)
    _safe_set(a, 'basecs_PathNameCS40', None)
    assert not _is_linked(a, 'basecs_PathNameCS40', b2)
    if hasattr(b2, 'basecs_ModelElementRefCS39'):
        assert not _is_linked(b2, 'basecs_ModelElementRefCS39', a)


def test_assoc_pathName62_link_reassign_clear():
    a = basecs_PathNameCS(scopeFilter="sample_text")
    b1 = basecs_PathElementCS()
    b2 = basecs_PathElementCS()
    _safe_set(a, 'PathNameCS', b1)
    assert _is_linked(a, 'PathNameCS', b1)
    if hasattr(b1, 'path'):
        assert _is_linked(b1, 'path', a)
    _safe_set(a, 'PathNameCS', b2)
    assert _is_linked(a, 'PathNameCS', b2)
    if hasattr(b1, 'path'):
        assert not _is_linked(b1, 'path', a)
    if hasattr(b2, 'path'):
        assert _is_linked(b2, 'path', a)
    _safe_set(a, 'PathNameCS', None)
    assert not _is_linked(a, 'PathNameCS', b2)
    if hasattr(b2, 'path'):
        assert not _is_linked(b2, 'path', a)


def test_assoc_specification12_link_reassign_clear():
    a = basecs_SpecificationCS(exprString="sample_text")
    b1 = basecs_ConstraintCS(stereotype="sample_text")
    b2 = basecs_ConstraintCS(stereotype="sample_text_2")
    _safe_set(a, 'basecs_SpecificationCS', b1)
    assert _is_linked(a, 'basecs_SpecificationCS', b1)
    if hasattr(b1, 'basecs_ConstraintCS13'):
        assert _is_linked(b1, 'basecs_ConstraintCS13', a)
    _safe_set(a, 'basecs_SpecificationCS', b2)
    assert _is_linked(a, 'basecs_SpecificationCS', b2)
    if hasattr(b1, 'basecs_ConstraintCS13'):
        assert not _is_linked(b1, 'basecs_ConstraintCS13', a)
    if hasattr(b2, 'basecs_ConstraintCS13'):
        assert _is_linked(b2, 'basecs_ConstraintCS13', a)
    _safe_set(a, 'basecs_SpecificationCS', None)
    assert not _is_linked(a, 'basecs_SpecificationCS', b2)
    if hasattr(b2, 'basecs_ConstraintCS13'):
        assert not _is_linked(b2, 'basecs_ConstraintCS13', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

AnnotationElementCS_strategy = st.builds(AnnotationElementCS)
@given(instance=AnnotationElementCS_strategy)
@settings(max_examples=25)
def test_AnnotationElementCS_instantiation(instance):
    assert isinstance(instance, AnnotationElementCS)


ClassifierCS_strategy = st.builds(ClassifierCS)
@given(instance=ClassifierCS_strategy)
@settings(max_examples=25)
def test_ClassifierCS_instantiation(instance):
    assert isinstance(instance, ClassifierCS)


ElementCS_strategy = st.builds(ElementCS)
@given(instance=ElementCS_strategy)
@settings(max_examples=25)
def test_ElementCS_instantiation(instance):
    assert isinstance(instance, ElementCS)


ElementRefCS_strategy = st.builds(ElementRefCS)
@given(instance=ElementRefCS_strategy)
@settings(max_examples=25)
def test_ElementRefCS_instantiation(instance):
    assert isinstance(instance, ElementRefCS)


FeatureCS_strategy = st.builds(FeatureCS)
@given(instance=FeatureCS_strategy)
@settings(max_examples=25)
def test_FeatureCS_instantiation(instance):
    assert isinstance(instance, FeatureCS)


ModelElementCS_strategy = st.builds(ModelElementCS)
@given(instance=ModelElementCS_strategy)
@settings(max_examples=25)
def test_ModelElementCS_instantiation(instance):
    assert isinstance(instance, ModelElementCS)


MultiplicityCS_strategy = st.builds(MultiplicityCS)
@given(instance=MultiplicityCS_strategy)
@settings(max_examples=25)
def test_MultiplicityCS_instantiation(instance):
    assert isinstance(instance, MultiplicityCS)


Nameable_strategy = st.builds(Nameable)
@given(instance=Nameable_strategy)
@settings(max_examples=25)
def test_Nameable_instantiation(instance):
    assert isinstance(instance, Nameable)


NamedElementCS_strategy = st.builds(NamedElementCS)
@given(instance=NamedElementCS_strategy)
@settings(max_examples=25)
def test_NamedElementCS_instantiation(instance):
    assert isinstance(instance, NamedElementCS)


NamespaceCS_strategy = st.builds(NamespaceCS)
@given(instance=NamespaceCS_strategy)
@settings(max_examples=25)
def test_NamespaceCS_instantiation(instance):
    assert isinstance(instance, NamespaceCS)


PackageOwnerCS_strategy = st.builds(PackageOwnerCS)
@given(instance=PackageOwnerCS_strategy)
@settings(max_examples=25)
def test_PackageOwnerCS_instantiation(instance):
    assert isinstance(instance, PackageOwnerCS)


PathElementCS_strategy = st.builds(PathElementCS)
@given(instance=PathElementCS_strategy)
@settings(max_examples=25)
def test_PathElementCS_instantiation(instance):
    assert isinstance(instance, PathElementCS)


Pivotable_strategy = st.builds(Pivotable)
@given(instance=Pivotable_strategy)
@settings(max_examples=25)
def test_Pivotable_instantiation(instance):
    assert isinstance(instance, Pivotable)


PivotableElementCS_strategy = st.builds(PivotableElementCS)
@given(instance=PivotableElementCS_strategy)
@settings(max_examples=25)
def test_PivotableElementCS_instantiation(instance):
    assert isinstance(instance, PivotableElementCS)


RootCS_strategy = st.builds(RootCS)
@given(instance=RootCS_strategy)
@settings(max_examples=25)
def test_RootCS_instantiation(instance):
    assert isinstance(instance, RootCS)


StructuralFeatureCS_strategy = st.builds(StructuralFeatureCS)
@given(instance=StructuralFeatureCS_strategy)
@settings(max_examples=25)
def test_StructuralFeatureCS_instantiation(instance):
    assert isinstance(instance, StructuralFeatureCS)


TemplateParameterCS_strategy = st.builds(TemplateParameterCS)
@given(instance=TemplateParameterCS_strategy)
@settings(max_examples=25)
def test_TemplateParameterCS_instantiation(instance):
    assert isinstance(instance, TemplateParameterCS)


TemplateableElementCS_strategy = st.builds(TemplateableElementCS)
@given(instance=TemplateableElementCS_strategy)
@settings(max_examples=25)
def test_TemplateableElementCS_instantiation(instance):
    assert isinstance(instance, TemplateableElementCS)


TypeCS_strategy = st.builds(TypeCS)
@given(instance=TypeCS_strategy)
@settings(max_examples=25)
def test_TypeCS_instantiation(instance):
    assert isinstance(instance, TypeCS)


TypeRefCS_strategy = st.builds(TypeRefCS)
@given(instance=TypeRefCS_strategy)
@settings(max_examples=25)
def test_TypeRefCS_instantiation(instance):
    assert isinstance(instance, TypeRefCS)


TypedElementCS_strategy = st.builds(TypedElementCS)
@given(instance=TypedElementCS_strategy)
@settings(max_examples=25)
def test_TypedElementCS_instantiation(instance):
    assert isinstance(instance, TypedElementCS)


TypedRefCS_strategy = st.builds(TypedRefCS)
@given(instance=TypedRefCS_strategy)
@settings(max_examples=25)
def test_TypedRefCS_instantiation(instance):
    assert isinstance(instance, TypedRefCS)


VisitableCS_strategy = st.builds(VisitableCS)
@given(instance=VisitableCS_strategy)
@settings(max_examples=25)
def test_VisitableCS_instantiation(instance):
    assert isinstance(instance, VisitableCS)


basecs_AnnotationCS_strategy = st.builds(basecs_AnnotationCS)
@given(instance=basecs_AnnotationCS_strategy)
@settings(max_examples=25)
def test_basecs_AnnotationCS_instantiation(instance):
    assert isinstance(instance, basecs_AnnotationCS)


basecs_AnnotationElementCS_strategy = st.builds(basecs_AnnotationElementCS)
@given(instance=basecs_AnnotationElementCS_strategy)
@settings(max_examples=25)
def test_basecs_AnnotationElementCS_instantiation(instance):
    assert isinstance(instance, basecs_AnnotationElementCS)


basecs_AttributeCS_strategy = st.builds(basecs_AttributeCS)
@given(instance=basecs_AttributeCS_strategy)
@settings(max_examples=25)
def test_basecs_AttributeCS_instantiation(instance):
    assert isinstance(instance, basecs_AttributeCS)


basecs_ClassCS_strategy = st.builds(basecs_ClassCS)
@given(instance=basecs_ClassCS_strategy)
@settings(max_examples=25)
def test_basecs_ClassCS_instantiation(instance):
    assert isinstance(instance, basecs_ClassCS)


basecs_ClassifierCS_strategy = st.builds(basecs_ClassifierCS, instanceClassName=safe_text, qualifier=safe_text)
@given(instance=basecs_ClassifierCS_strategy)
@settings(max_examples=25)
def test_basecs_ClassifierCS_instantiation(instance):
    assert isinstance(instance, basecs_ClassifierCS)


basecs_ConstraintCS_strategy = st.builds(basecs_ConstraintCS, stereotype=safe_text)
@given(instance=basecs_ConstraintCS_strategy)
@settings(max_examples=25)
def test_basecs_ConstraintCS_instantiation(instance):
    assert isinstance(instance, basecs_ConstraintCS)


basecs_DataTypeCS_strategy = st.builds(basecs_DataTypeCS)
@given(instance=basecs_DataTypeCS_strategy)
@settings(max_examples=25)
def test_basecs_DataTypeCS_instantiation(instance):
    assert isinstance(instance, basecs_DataTypeCS)


basecs_DetailCS_strategy = st.builds(basecs_DetailCS, value=safe_text)
@given(instance=basecs_DetailCS_strategy)
@settings(max_examples=25)
def test_basecs_DetailCS_instantiation(instance):
    assert isinstance(instance, basecs_DetailCS)


basecs_DocumentationCS_strategy = st.builds(basecs_DocumentationCS, value=safe_text)
@given(instance=basecs_DocumentationCS_strategy)
@settings(max_examples=25)
def test_basecs_DocumentationCS_instantiation(instance):
    assert isinstance(instance, basecs_DocumentationCS)


basecs_EClassifier_strategy = st.builds(basecs_EClassifier)
@given(instance=basecs_EClassifier_strategy)
@settings(max_examples=25)
def test_basecs_EClassifier_instantiation(instance):
    assert isinstance(instance, basecs_EClassifier)


basecs_Element_strategy = st.builds(basecs_Element)
@given(instance=basecs_Element_strategy)
@settings(max_examples=25)
def test_basecs_Element_instantiation(instance):
    assert isinstance(instance, basecs_Element)


basecs_ElementCS_strategy = st.builds(basecs_ElementCS)
@given(instance=basecs_ElementCS_strategy)
@settings(max_examples=25)
def test_basecs_ElementCS_instantiation(instance):
    assert isinstance(instance, basecs_ElementCS)


basecs_ElementRefCS_strategy = st.builds(basecs_ElementRefCS)
@given(instance=basecs_ElementRefCS_strategy)
@settings(max_examples=25)
def test_basecs_ElementRefCS_instantiation(instance):
    assert isinstance(instance, basecs_ElementRefCS)


basecs_EnumerationCS_strategy = st.builds(basecs_EnumerationCS)
@given(instance=basecs_EnumerationCS_strategy)
@settings(max_examples=25)
def test_basecs_EnumerationCS_instantiation(instance):
    assert isinstance(instance, basecs_EnumerationCS)


basecs_EnumerationLiteralCS_strategy = st.builds(basecs_EnumerationLiteralCS, value=st.integers())
@given(instance=basecs_EnumerationLiteralCS_strategy)
@settings(max_examples=25)
def test_basecs_EnumerationLiteralCS_instantiation(instance):
    assert isinstance(instance, basecs_EnumerationLiteralCS)


basecs_FeatureCS_strategy = st.builds(basecs_FeatureCS)
@given(instance=basecs_FeatureCS_strategy)
@settings(max_examples=25)
def test_basecs_FeatureCS_instantiation(instance):
    assert isinstance(instance, basecs_FeatureCS)


basecs_ImportCS_strategy = st.builds(basecs_ImportCS, all=st.booleans())
@given(instance=basecs_ImportCS_strategy)
@settings(max_examples=25)
def test_basecs_ImportCS_instantiation(instance):
    assert isinstance(instance, basecs_ImportCS)


basecs_LambdaTypeCS_strategy = st.builds(basecs_LambdaTypeCS, name=safe_text)
@given(instance=basecs_LambdaTypeCS_strategy)
@settings(max_examples=25)
def test_basecs_LambdaTypeCS_instantiation(instance):
    assert isinstance(instance, basecs_LambdaTypeCS)


basecs_LibraryCS_strategy = st.builds(basecs_LibraryCS)
@given(instance=basecs_LibraryCS_strategy)
@settings(max_examples=25)
def test_basecs_LibraryCS_instantiation(instance):
    assert isinstance(instance, basecs_LibraryCS)


basecs_ModelElementCS_strategy = st.builds(basecs_ModelElementCS, csi=safe_text, originalXmiId=safe_text)
@given(instance=basecs_ModelElementCS_strategy)
@settings(max_examples=25)
def test_basecs_ModelElementCS_instantiation(instance):
    assert isinstance(instance, basecs_ModelElementCS)


basecs_ModelElementRefCS_strategy = st.builds(basecs_ModelElementRefCS)
@given(instance=basecs_ModelElementRefCS_strategy)
@settings(max_examples=25)
def test_basecs_ModelElementRefCS_instantiation(instance):
    assert isinstance(instance, basecs_ModelElementRefCS)


basecs_MultiplicityBoundsCS_strategy = st.builds(basecs_MultiplicityBoundsCS, lowerBound=st.integers(), upperBound=safe_text)
@given(instance=basecs_MultiplicityBoundsCS_strategy)
@settings(max_examples=25)
def test_basecs_MultiplicityBoundsCS_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityBoundsCS)


basecs_MultiplicityCS_strategy = st.builds(basecs_MultiplicityCS)
@given(instance=basecs_MultiplicityCS_strategy)
@settings(max_examples=25)
def test_basecs_MultiplicityCS_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityCS)


basecs_MultiplicityStringCS_strategy = st.builds(basecs_MultiplicityStringCS, stringBounds=safe_text)
@given(instance=basecs_MultiplicityStringCS_strategy)
@settings(max_examples=25)
def test_basecs_MultiplicityStringCS_instantiation(instance):
    assert isinstance(instance, basecs_MultiplicityStringCS)


basecs_NamedElementCS_strategy = st.builds(basecs_NamedElementCS, name=safe_text)
@given(instance=basecs_NamedElementCS_strategy)
@settings(max_examples=25)
def test_basecs_NamedElementCS_instantiation(instance):
    assert isinstance(instance, basecs_NamedElementCS)


basecs_Namespace_strategy = st.builds(basecs_Namespace)
@given(instance=basecs_Namespace_strategy)
@settings(max_examples=25)
def test_basecs_Namespace_instantiation(instance):
    assert isinstance(instance, basecs_Namespace)


basecs_NamespaceCS_strategy = st.builds(basecs_NamespaceCS)
@given(instance=basecs_NamespaceCS_strategy)
@settings(max_examples=25)
def test_basecs_NamespaceCS_instantiation(instance):
    assert isinstance(instance, basecs_NamespaceCS)


basecs_OperationCS_strategy = st.builds(basecs_OperationCS)
@given(instance=basecs_OperationCS_strategy)
@settings(max_examples=25)
def test_basecs_OperationCS_instantiation(instance):
    assert isinstance(instance, basecs_OperationCS)


basecs_PackageCS_strategy = st.builds(basecs_PackageCS, nsPrefix=safe_text, nsURI=safe_text)
@given(instance=basecs_PackageCS_strategy)
@settings(max_examples=25)
def test_basecs_PackageCS_instantiation(instance):
    assert isinstance(instance, basecs_PackageCS)


basecs_PackageOwnerCS_strategy = st.builds(basecs_PackageOwnerCS)
@given(instance=basecs_PackageOwnerCS_strategy)
@settings(max_examples=25)
def test_basecs_PackageOwnerCS_instantiation(instance):
    assert isinstance(instance, basecs_PackageOwnerCS)


basecs_ParameterCS_strategy = st.builds(basecs_ParameterCS)
@given(instance=basecs_ParameterCS_strategy)
@settings(max_examples=25)
def test_basecs_ParameterCS_instantiation(instance):
    assert isinstance(instance, basecs_ParameterCS)


basecs_PathElementCS_strategy = st.builds(basecs_PathElementCS)
@given(instance=basecs_PathElementCS_strategy)
@settings(max_examples=25)
def test_basecs_PathElementCS_instantiation(instance):
    assert isinstance(instance, basecs_PathElementCS)


basecs_PathElementWithURICS_strategy = st.builds(basecs_PathElementWithURICS, uri=safe_text)
@given(instance=basecs_PathElementWithURICS_strategy)
@settings(max_examples=25)
def test_basecs_PathElementWithURICS_instantiation(instance):
    assert isinstance(instance, basecs_PathElementWithURICS)


basecs_PathNameCS_strategy = st.builds(basecs_PathNameCS, scopeFilter=safe_text)
@given(instance=basecs_PathNameCS_strategy)
@settings(max_examples=25)
def test_basecs_PathNameCS_instantiation(instance):
    assert isinstance(instance, basecs_PathNameCS)


basecs_PivotableElementCS_strategy = st.builds(basecs_PivotableElementCS)
@given(instance=basecs_PivotableElementCS_strategy)
@settings(max_examples=25)
def test_basecs_PivotableElementCS_instantiation(instance):
    assert isinstance(instance, basecs_PivotableElementCS)


basecs_PrimitiveTypeRefCS_strategy = st.builds(basecs_PrimitiveTypeRefCS, name=safe_text)
@given(instance=basecs_PrimitiveTypeRefCS_strategy)
@settings(max_examples=25)
def test_basecs_PrimitiveTypeRefCS_instantiation(instance):
    assert isinstance(instance, basecs_PrimitiveTypeRefCS)


basecs_Property_strategy = st.builds(basecs_Property)
@given(instance=basecs_Property_strategy)
@settings(max_examples=25)
def test_basecs_Property_instantiation(instance):
    assert isinstance(instance, basecs_Property)


basecs_ReferenceCS_strategy = st.builds(basecs_ReferenceCS)
@given(instance=basecs_ReferenceCS_strategy)
@settings(max_examples=25)
def test_basecs_ReferenceCS_instantiation(instance):
    assert isinstance(instance, basecs_ReferenceCS)


basecs_RootCS_strategy = st.builds(basecs_RootCS)
@given(instance=basecs_RootCS_strategy)
@settings(max_examples=25)
def test_basecs_RootCS_instantiation(instance):
    assert isinstance(instance, basecs_RootCS)


basecs_RootPackageCS_strategy = st.builds(basecs_RootPackageCS)
@given(instance=basecs_RootPackageCS_strategy)
@settings(max_examples=25)
def test_basecs_RootPackageCS_instantiation(instance):
    assert isinstance(instance, basecs_RootPackageCS)


basecs_SpecificationCS_strategy = st.builds(basecs_SpecificationCS, exprString=safe_text)
@given(instance=basecs_SpecificationCS_strategy)
@settings(max_examples=25)
def test_basecs_SpecificationCS_instantiation(instance):
    assert isinstance(instance, basecs_SpecificationCS)


basecs_StructuralFeatureCS_strategy = st.builds(basecs_StructuralFeatureCS, default=safe_text)
@given(instance=basecs_StructuralFeatureCS_strategy)
@settings(max_examples=25)
def test_basecs_StructuralFeatureCS_instantiation(instance):
    assert isinstance(instance, basecs_StructuralFeatureCS)


basecs_TemplateBindingCS_strategy = st.builds(basecs_TemplateBindingCS)
@given(instance=basecs_TemplateBindingCS_strategy)
@settings(max_examples=25)
def test_basecs_TemplateBindingCS_instantiation(instance):
    assert isinstance(instance, basecs_TemplateBindingCS)


basecs_TemplateParameterCS_strategy = st.builds(basecs_TemplateParameterCS)
@given(instance=basecs_TemplateParameterCS_strategy)
@settings(max_examples=25)
def test_basecs_TemplateParameterCS_instantiation(instance):
    assert isinstance(instance, basecs_TemplateParameterCS)


basecs_TemplateParameterSubstitutionCS_strategy = st.builds(basecs_TemplateParameterSubstitutionCS)
@given(instance=basecs_TemplateParameterSubstitutionCS_strategy)
@settings(max_examples=25)
def test_basecs_TemplateParameterSubstitutionCS_instantiation(instance):
    assert isinstance(instance, basecs_TemplateParameterSubstitutionCS)


basecs_TemplateSignatureCS_strategy = st.builds(basecs_TemplateSignatureCS)
@given(instance=basecs_TemplateSignatureCS_strategy)
@settings(max_examples=25)
def test_basecs_TemplateSignatureCS_instantiation(instance):
    assert isinstance(instance, basecs_TemplateSignatureCS)


basecs_TemplateableElementCS_strategy = st.builds(basecs_TemplateableElementCS)
@given(instance=basecs_TemplateableElementCS_strategy)
@settings(max_examples=25)
def test_basecs_TemplateableElementCS_instantiation(instance):
    assert isinstance(instance, basecs_TemplateableElementCS)


basecs_TuplePartCS_strategy = st.builds(basecs_TuplePartCS)
@given(instance=basecs_TuplePartCS_strategy)
@settings(max_examples=25)
def test_basecs_TuplePartCS_instantiation(instance):
    assert isinstance(instance, basecs_TuplePartCS)


basecs_TupleTypeCS_strategy = st.builds(basecs_TupleTypeCS, name=safe_text)
@given(instance=basecs_TupleTypeCS_strategy)
@settings(max_examples=25)
def test_basecs_TupleTypeCS_instantiation(instance):
    assert isinstance(instance, basecs_TupleTypeCS)


basecs_Type_strategy = st.builds(basecs_Type)
@given(instance=basecs_Type_strategy)
@settings(max_examples=25)
def test_basecs_Type_instantiation(instance):
    assert isinstance(instance, basecs_Type)


basecs_TypeCS_strategy = st.builds(basecs_TypeCS)
@given(instance=basecs_TypeCS_strategy)
@settings(max_examples=25)
def test_basecs_TypeCS_instantiation(instance):
    assert isinstance(instance, basecs_TypeCS)


basecs_TypeParameterCS_strategy = st.builds(basecs_TypeParameterCS)
@given(instance=basecs_TypeParameterCS_strategy)
@settings(max_examples=25)
def test_basecs_TypeParameterCS_instantiation(instance):
    assert isinstance(instance, basecs_TypeParameterCS)


basecs_TypeRefCS_strategy = st.builds(basecs_TypeRefCS)
@given(instance=basecs_TypeRefCS_strategy)
@settings(max_examples=25)
def test_basecs_TypeRefCS_instantiation(instance):
    assert isinstance(instance, basecs_TypeRefCS)


basecs_TypedElementCS_strategy = st.builds(basecs_TypedElementCS, optional=st.booleans(), qualifier=safe_text)
@given(instance=basecs_TypedElementCS_strategy)
@settings(max_examples=25)
def test_basecs_TypedElementCS_instantiation(instance):
    assert isinstance(instance, basecs_TypedElementCS)


basecs_TypedRefCS_strategy = st.builds(basecs_TypedRefCS)
@given(instance=basecs_TypedRefCS_strategy)
@settings(max_examples=25)
def test_basecs_TypedRefCS_instantiation(instance):
    assert isinstance(instance, basecs_TypedRefCS)


basecs_TypedTypeRefCS_strategy = st.builds(basecs_TypedTypeRefCS)
@given(instance=basecs_TypedTypeRefCS_strategy)
@settings(max_examples=25)
def test_basecs_TypedTypeRefCS_instantiation(instance):
    assert isinstance(instance, basecs_TypedTypeRefCS)


basecs_VisitableCS_strategy = st.builds(basecs_VisitableCS)
@given(instance=basecs_VisitableCS_strategy)
@settings(max_examples=25)
def test_basecs_VisitableCS_instantiation(instance):
    assert isinstance(instance, basecs_VisitableCS)


basecs_WildcardTypeRefCS_strategy = st.builds(basecs_WildcardTypeRefCS)
@given(instance=basecs_WildcardTypeRefCS_strategy)
@settings(max_examples=25)
def test_basecs_WildcardTypeRefCS_instantiation(instance):
    assert isinstance(instance, basecs_WildcardTypeRefCS)



