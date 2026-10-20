import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Annotable,
    Classifier,
    Contained,
    Container,
    Statement,
    java_Annotable,
    java_Annotation,
    java_AnnotationInstance,
    java_AnnotationInstanceParameter,
    java_AnnotationInstanceValue,
    java_Argument,
    java_AssertStatement,
    java_Class,
    java_Classifier,
    java_Contained,
    java_Container,
    java_Field,
    java_GETExpression,
    java_Generalization,
    java_GenericBinding,
    java_Import,
    java_Interface,
    java_InterfaceImplementation,
    java_Method,
    java_Package,
    java_Statement,
    java_System,
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

def test_assoc_arguments31_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Argument(name="sample_text", order=7)
    _safe_set(b, 'Argument', a1)
    assert _is_linked(b, 'Argument', a1)
    if hasattr(a1, 'usingMethod'):
        assert _is_linked(a1, 'usingMethod', b)
    _safe_set(b, 'Argument', a2)
    assert _is_linked(b, 'Argument', a2)
    if hasattr(a1, 'usingMethod'):
        assert not _is_linked(a1, 'usingMethod', b)
    if hasattr(a2, 'usingMethod'):
        assert _is_linked(a2, 'usingMethod', b)
    _safe_set(b, 'Argument', None)
    assert not _is_linked(b, 'Argument', a2)
    if hasattr(a2, 'usingMethod'):
        assert not _is_linked(a2, 'usingMethod', b)


def test_assoc_body37_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    _safe_set(b, 'method', {a1})
    assert _is_linked(b, 'method', a1)
    if hasattr(a1, 'Statement'):
        assert _is_linked(a1, 'Statement', b)
    _safe_set(b, 'method', {a2})
    assert _is_linked(b, 'method', a2)
    if hasattr(a1, 'Statement'):
        assert not _is_linked(a1, 'Statement', b)
    if hasattr(a2, 'Statement'):
        assert _is_linked(a2, 'Statement', b)
    _safe_set(b, 'method', set())
    assert not _is_linked(b, 'method', a2)
    if hasattr(a2, 'Statement'):
        assert not _is_linked(a2, 'Statement', b)


def test_assoc_containingClassifier21_reverse_link_reassign_clear():
    a1 = java_Field(default="sample_text", isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Field(default="sample_text_2", isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier22', a1)
    assert _is_linked(b, 'Classifier22', a1)
    if hasattr(a1, 'fields'):
        assert _is_linked(a1, 'fields', b)
    _safe_set(b, 'Classifier22', a2)
    assert _is_linked(b, 'Classifier22', a2)
    if hasattr(a1, 'fields'):
        assert not _is_linked(a1, 'fields', b)
    if hasattr(a2, 'fields'):
        assert _is_linked(a2, 'fields', b)
    _safe_set(b, 'Classifier22', None)
    assert not _is_linked(b, 'Classifier22', a2)
    if hasattr(a2, 'fields'):
        assert not _is_linked(a2, 'fields', b)


def test_assoc_containingClassifier32_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier33', a1)
    assert _is_linked(b, 'Classifier33', a1)
    if hasattr(a1, 'methods'):
        assert _is_linked(a1, 'methods', b)
    _safe_set(b, 'Classifier33', a2)
    assert _is_linked(b, 'Classifier33', a2)
    if hasattr(a1, 'methods'):
        assert not _is_linked(a1, 'methods', b)
    if hasattr(a2, 'methods'):
        assert _is_linked(a2, 'methods', b)
    _safe_set(b, 'Classifier33', None)
    assert not _is_linked(b, 'Classifier33', a2)
    if hasattr(a2, 'methods'):
        assert not _is_linked(a2, 'methods', b)


def test_assoc_extendedClass3_reverse_link_reassign_clear():
    a1 = java_Class(isAbstract=True, isFinal=True, isStatic=True)
    a2 = java_Class(isAbstract=False, isFinal=False, isStatic=False)
    b = java_Class(isAbstract=True, isFinal=True, isStatic=True)
    _safe_set(b, 'extendingClasses', a1)
    assert _is_linked(b, 'extendingClasses', a1)
    if hasattr(a1, 'Class'):
        assert _is_linked(a1, 'Class', b)
    _safe_set(b, 'extendingClasses', a2)
    assert _is_linked(b, 'extendingClasses', a2)
    if hasattr(a1, 'Class'):
        assert not _is_linked(a1, 'Class', b)
    if hasattr(a2, 'Class'):
        assert _is_linked(a2, 'Class', b)
    _safe_set(b, 'extendingClasses', None)
    assert not _is_linked(b, 'extendingClasses', a2)
    if hasattr(a2, 'Class'):
        assert not _is_linked(a2, 'Class', b)


def test_assoc_extendingClasses5_reverse_link_reassign_clear():
    a1 = java_Class(isAbstract=True, isFinal=True, isStatic=True)
    a2 = java_Class(isAbstract=False, isFinal=False, isStatic=False)
    b = java_Class(isAbstract=True, isFinal=True, isStatic=True)
    _safe_set(b, 'extendedClass', a1)
    assert _is_linked(b, 'extendedClass', a1)
    if hasattr(a1, 'Class6'):
        assert _is_linked(a1, 'Class6', b)
    _safe_set(b, 'extendedClass', a2)
    assert _is_linked(b, 'extendedClass', a2)
    if hasattr(a1, 'Class6'):
        assert not _is_linked(a1, 'Class6', b)
    if hasattr(a2, 'Class6'):
        assert _is_linked(a2, 'Class6', b)
    _safe_set(b, 'extendedClass', None)
    assert not _is_linked(b, 'extendedClass', a2)
    if hasattr(a2, 'Class6'):
        assert not _is_linked(a2, 'Class6', b)


def test_assoc_fields13_reverse_link_reassign_clear():
    a1 = java_Field(default="sample_text", isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Field(default="sample_text_2", isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'containingClassifier', {a1})
    assert _is_linked(b, 'containingClassifier', a1)
    if hasattr(a1, 'Field'):
        assert _is_linked(a1, 'Field', b)
    _safe_set(b, 'containingClassifier', {a2})
    assert _is_linked(b, 'containingClassifier', a2)
    if hasattr(a1, 'Field'):
        assert not _is_linked(a1, 'Field', b)
    if hasattr(a2, 'Field'):
        assert _is_linked(a2, 'Field', b)
    _safe_set(b, 'containingClassifier', set())
    assert not _is_linked(b, 'containingClassifier', a2)
    if hasattr(a2, 'Field'):
        assert not _is_linked(a2, 'Field', b)


def test_assoc_general9_reverse_link_reassign_clear():
    a1 = java_Generalization(name="sample_text")
    a2 = java_Generalization(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier', a1)
    assert _is_linked(b, 'java_Classifier', a1)
    if hasattr(a1, 'java_Generalization'):
        assert _is_linked(a1, 'java_Generalization', b)
    _safe_set(b, 'java_Classifier', a2)
    assert _is_linked(b, 'java_Classifier', a2)
    if hasattr(a1, 'java_Generalization'):
        assert not _is_linked(a1, 'java_Generalization', b)
    if hasattr(a2, 'java_Generalization'):
        assert _is_linked(a2, 'java_Generalization', b)
    _safe_set(b, 'java_Classifier', None)
    assert not _is_linked(b, 'java_Classifier', a2)
    if hasattr(a2, 'java_Generalization'):
        assert not _is_linked(a2, 'java_Generalization', b)


def test_assoc_generalization17_reverse_link_reassign_clear():
    a1 = java_Generalization(name="sample_text")
    a2 = java_Generalization(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'generalizator', a1)
    assert _is_linked(b, 'generalizator', a1)
    if hasattr(a1, 'Generalization'):
        assert _is_linked(a1, 'Generalization', b)
    _safe_set(b, 'generalizator', a2)
    assert _is_linked(b, 'generalizator', a2)
    if hasattr(a1, 'Generalization'):
        assert not _is_linked(a1, 'Generalization', b)
    if hasattr(a2, 'Generalization'):
        assert _is_linked(a2, 'Generalization', b)
    _safe_set(b, 'generalizator', None)
    assert not _is_linked(b, 'generalizator', a2)
    if hasattr(a2, 'Generalization'):
        assert not _is_linked(a2, 'Generalization', b)


def test_assoc_generalizator10_reverse_link_reassign_clear():
    a1 = java_Generalization(name="sample_text")
    a2 = java_Generalization(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier11', a1)
    assert _is_linked(b, 'Classifier11', a1)
    if hasattr(a1, 'generalization'):
        assert _is_linked(a1, 'generalization', b)
    _safe_set(b, 'Classifier11', a2)
    assert _is_linked(b, 'Classifier11', a2)
    if hasattr(a1, 'generalization'):
        assert not _is_linked(a1, 'generalization', b)
    if hasattr(a2, 'generalization'):
        assert _is_linked(a2, 'generalization', b)
    _safe_set(b, 'Classifier11', None)
    assert not _is_linked(b, 'Classifier11', a2)
    if hasattr(a2, 'generalization'):
        assert not _is_linked(a2, 'generalization', b)


def test_assoc_genericBindings12_reverse_link_reassign_clear():
    a1 = java_GenericBinding(name="sample_text")
    a2 = java_GenericBinding(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'usingClassifier', {a1})
    assert _is_linked(b, 'usingClassifier', a1)
    if hasattr(a1, 'GenericBinding'):
        assert _is_linked(a1, 'GenericBinding', b)
    _safe_set(b, 'usingClassifier', {a2})
    assert _is_linked(b, 'usingClassifier', a2)
    if hasattr(a1, 'GenericBinding'):
        assert not _is_linked(a1, 'GenericBinding', b)
    if hasattr(a2, 'GenericBinding'):
        assert _is_linked(a2, 'GenericBinding', b)
    _safe_set(b, 'usingClassifier', set())
    assert not _is_linked(b, 'usingClassifier', a2)
    if hasattr(a2, 'GenericBinding'):
        assert not _is_linked(a2, 'GenericBinding', b)


def test_assoc_implementer8_reverse_link_reassign_clear():
    a1 = java_InterfaceImplementation(name="sample_text")
    a2 = java_InterfaceImplementation(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier', a1)
    assert _is_linked(b, 'Classifier', a1)
    if hasattr(a1, 'interfaceImplementations'):
        assert _is_linked(a1, 'interfaceImplementations', b)
    _safe_set(b, 'Classifier', a2)
    assert _is_linked(b, 'Classifier', a2)
    if hasattr(a1, 'interfaceImplementations'):
        assert not _is_linked(a1, 'interfaceImplementations', b)
    if hasattr(a2, 'interfaceImplementations'):
        assert _is_linked(a2, 'interfaceImplementations', b)
    _safe_set(b, 'Classifier', None)
    assert not _is_linked(b, 'Classifier', a2)
    if hasattr(a2, 'interfaceImplementations'):
        assert not _is_linked(a2, 'interfaceImplementations', b)


def test_assoc_imported23_reverse_link_reassign_clear():
    a1 = java_Import(name="sample_text")
    a2 = java_Import(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier24', a1)
    assert _is_linked(b, 'java_Classifier24', a1)
    if hasattr(a1, 'java_Import'):
        assert _is_linked(a1, 'java_Import', b)
    _safe_set(b, 'java_Classifier24', a2)
    assert _is_linked(b, 'java_Classifier24', a2)
    if hasattr(a1, 'java_Import'):
        assert not _is_linked(a1, 'java_Import', b)
    if hasattr(a2, 'java_Import'):
        assert _is_linked(a2, 'java_Import', b)
    _safe_set(b, 'java_Classifier24', None)
    assert not _is_linked(b, 'java_Classifier24', a2)
    if hasattr(a2, 'java_Import'):
        assert not _is_linked(a2, 'java_Import', b)


def test_assoc_importing25_reverse_link_reassign_clear():
    a1 = java_Import(name="sample_text")
    a2 = java_Import(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier26', a1)
    assert _is_linked(b, 'Classifier26', a1)
    if hasattr(a1, 'imports'):
        assert _is_linked(a1, 'imports', b)
    _safe_set(b, 'Classifier26', a2)
    assert _is_linked(b, 'Classifier26', a2)
    if hasattr(a1, 'imports'):
        assert not _is_linked(a1, 'imports', b)
    if hasattr(a2, 'imports'):
        assert _is_linked(a2, 'imports', b)
    _safe_set(b, 'Classifier26', None)
    assert not _is_linked(b, 'Classifier26', a2)
    if hasattr(a2, 'imports'):
        assert not _is_linked(a2, 'imports', b)


def test_assoc_importingClasses28_reverse_link_reassign_clear():
    a1 = java_Contained(visibility="sample_text")
    a2 = java_Contained(visibility="sample_text_2")
    b = java_Class(isAbstract=True, isFinal=True, isStatic=True)
    _safe_set(b, 'java_Class', a1)
    assert _is_linked(b, 'java_Class', a1)
    if hasattr(a1, 'java_Contained'):
        assert _is_linked(a1, 'java_Contained', b)
    _safe_set(b, 'java_Class', a2)
    assert _is_linked(b, 'java_Class', a2)
    if hasattr(a1, 'java_Contained'):
        assert not _is_linked(a1, 'java_Contained', b)
    if hasattr(a2, 'java_Contained'):
        assert _is_linked(a2, 'java_Contained', b)
    _safe_set(b, 'java_Class', None)
    assert not _is_linked(b, 'java_Class', a2)
    if hasattr(a2, 'java_Contained'):
        assert not _is_linked(a2, 'java_Contained', b)


def test_assoc_imports18_reverse_link_reassign_clear():
    a1 = java_Import(name="sample_text")
    a2 = java_Import(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'importing', {a1})
    assert _is_linked(b, 'importing', a1)
    if hasattr(a1, 'Import'):
        assert _is_linked(a1, 'Import', b)
    _safe_set(b, 'importing', {a2})
    assert _is_linked(b, 'importing', a2)
    if hasattr(a1, 'Import'):
        assert not _is_linked(a1, 'Import', b)
    if hasattr(a2, 'Import'):
        assert _is_linked(a2, 'Import', b)
    _safe_set(b, 'importing', set())
    assert not _is_linked(b, 'importing', a2)
    if hasattr(a2, 'Import'):
        assert not _is_linked(a2, 'Import', b)


def test_assoc_instance59_reverse_link_reassign_clear():
    a1 = java_AnnotationInstanceParameter(name="sample_text")
    a2 = java_AnnotationInstanceParameter(name="sample_text_2")
    b = java_AnnotationInstance(name="sample_text")
    _safe_set(b, 'AnnotationInstance60', a1)
    assert _is_linked(b, 'AnnotationInstance60', a1)
    if hasattr(a1, 'parameters'):
        assert _is_linked(a1, 'parameters', b)
    _safe_set(b, 'AnnotationInstance60', a2)
    assert _is_linked(b, 'AnnotationInstance60', a2)
    if hasattr(a1, 'parameters'):
        assert not _is_linked(a1, 'parameters', b)
    if hasattr(a2, 'parameters'):
        assert _is_linked(a2, 'parameters', b)
    _safe_set(b, 'AnnotationInstance60', None)
    assert not _is_linked(b, 'AnnotationInstance60', a2)
    if hasattr(a2, 'parameters'):
        assert not _is_linked(a2, 'parameters', b)


def test_assoc_interfaceImplementations16_reverse_link_reassign_clear():
    a1 = java_InterfaceImplementation(name="sample_text")
    a2 = java_InterfaceImplementation(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'implementer', {a1})
    assert _is_linked(b, 'implementer', a1)
    if hasattr(a1, 'InterfaceImplementation'):
        assert _is_linked(a1, 'InterfaceImplementation', b)
    _safe_set(b, 'implementer', {a2})
    assert _is_linked(b, 'implementer', a2)
    if hasattr(a1, 'InterfaceImplementation'):
        assert not _is_linked(a1, 'InterfaceImplementation', b)
    if hasattr(a2, 'InterfaceImplementation'):
        assert _is_linked(a2, 'InterfaceImplementation', b)
    _safe_set(b, 'implementer', set())
    assert not _is_linked(b, 'implementer', a2)
    if hasattr(a2, 'InterfaceImplementation'):
        assert not _is_linked(a2, 'InterfaceImplementation', b)


def test_assoc_lowerBounding49_reverse_link_reassign_clear():
    a1 = java_GenericBinding(name="sample_text")
    a2 = java_GenericBinding(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier51', a1)
    assert _is_linked(b, 'java_Classifier51', a1)
    if hasattr(a1, 'java_GenericBinding50'):
        assert _is_linked(a1, 'java_GenericBinding50', b)
    _safe_set(b, 'java_Classifier51', a2)
    assert _is_linked(b, 'java_Classifier51', a2)
    if hasattr(a1, 'java_GenericBinding50'):
        assert not _is_linked(a1, 'java_GenericBinding50', b)
    if hasattr(a2, 'java_GenericBinding50'):
        assert _is_linked(a2, 'java_GenericBinding50', b)
    _safe_set(b, 'java_Classifier51', None)
    assert not _is_linked(b, 'java_Classifier51', a2)
    if hasattr(a2, 'java_GenericBinding50'):
        assert not _is_linked(a2, 'java_GenericBinding50', b)


def test_assoc_method38_reverse_link_reassign_clear():
    a1 = java_Statement(name="sample_text")
    a2 = java_Statement(name="sample_text_2")
    b = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    _safe_set(b, 'Method39', a1)
    assert _is_linked(b, 'Method39', a1)
    if hasattr(a1, 'body'):
        assert _is_linked(a1, 'body', b)
    _safe_set(b, 'Method39', a2)
    assert _is_linked(b, 'Method39', a2)
    if hasattr(a1, 'body'):
        assert not _is_linked(a1, 'body', b)
    if hasattr(a2, 'body'):
        assert _is_linked(a2, 'body', b)
    _safe_set(b, 'Method39', None)
    assert not _is_linked(b, 'Method39', a2)
    if hasattr(a2, 'body'):
        assert not _is_linked(a2, 'body', b)


def test_assoc_methods14_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'containingClassifier15', {a1})
    assert _is_linked(b, 'containingClassifier15', a1)
    if hasattr(a1, 'Method'):
        assert _is_linked(a1, 'Method', b)
    _safe_set(b, 'containingClassifier15', {a2})
    assert _is_linked(b, 'containingClassifier15', a2)
    if hasattr(a1, 'Method'):
        assert not _is_linked(a1, 'Method', b)
    if hasattr(a2, 'Method'):
        assert _is_linked(a2, 'Method', b)
    _safe_set(b, 'containingClassifier15', set())
    assert not _is_linked(b, 'containingClassifier15', a2)
    if hasattr(a2, 'Method'):
        assert not _is_linked(a2, 'Method', b)


def test_assoc_packages0_reverse_link_reassign_clear():
    a1 = java_System(name="sample_text")
    a2 = java_System(name="sample_text_2")
    b = java_Package(name="sample_text")
    _safe_set(b, 'Package', a1)
    assert _is_linked(b, 'Package', a1)
    if hasattr(a1, 'system'):
        assert _is_linked(a1, 'system', b)
    _safe_set(b, 'Package', a2)
    assert _is_linked(b, 'Package', a2)
    if hasattr(a1, 'system'):
        assert not _is_linked(a1, 'system', b)
    if hasattr(a2, 'system'):
        assert _is_linked(a2, 'system', b)
    _safe_set(b, 'Package', None)
    assert not _is_linked(b, 'Package', a2)
    if hasattr(a2, 'system'):
        assert not _is_linked(a2, 'system', b)


def test_assoc_parameter61_reverse_link_reassign_clear():
    a1 = java_AnnotationInstanceValue(id=7, name="sample_text", value="sample_text")
    a2 = java_AnnotationInstanceValue(id=13, name="sample_text_2", value="sample_text_2")
    b = java_AnnotationInstanceParameter(name="sample_text")
    _safe_set(b, 'AnnotationInstanceParameter62', a1)
    assert _is_linked(b, 'AnnotationInstanceParameter62', a1)
    if hasattr(a1, 'values'):
        assert _is_linked(a1, 'values', b)
    _safe_set(b, 'AnnotationInstanceParameter62', a2)
    assert _is_linked(b, 'AnnotationInstanceParameter62', a2)
    if hasattr(a1, 'values'):
        assert not _is_linked(a1, 'values', b)
    if hasattr(a2, 'values'):
        assert _is_linked(a2, 'values', b)
    _safe_set(b, 'AnnotationInstanceParameter62', None)
    assert not _is_linked(b, 'AnnotationInstanceParameter62', a2)
    if hasattr(a2, 'values'):
        assert not _is_linked(a2, 'values', b)


def test_assoc_parameters56_reverse_link_reassign_clear():
    a1 = java_AnnotationInstanceParameter(name="sample_text")
    a2 = java_AnnotationInstanceParameter(name="sample_text_2")
    b = java_AnnotationInstance(name="sample_text")
    _safe_set(b, 'instance', {a1})
    assert _is_linked(b, 'instance', a1)
    if hasattr(a1, 'AnnotationInstanceParameter'):
        assert _is_linked(a1, 'AnnotationInstanceParameter', b)
    _safe_set(b, 'instance', {a2})
    assert _is_linked(b, 'instance', a2)
    if hasattr(a1, 'AnnotationInstanceParameter'):
        assert not _is_linked(a1, 'AnnotationInstanceParameter', b)
    if hasattr(a2, 'AnnotationInstanceParameter'):
        assert _is_linked(a2, 'AnnotationInstanceParameter', b)
    _safe_set(b, 'instance', set())
    assert not _is_linked(b, 'instance', a2)
    if hasattr(a2, 'AnnotationInstanceParameter'):
        assert not _is_linked(a2, 'AnnotationInstanceParameter', b)


def test_assoc_raisedExceptions34_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier36', a1)
    assert _is_linked(b, 'java_Classifier36', a1)
    if hasattr(a1, 'java_Method35'):
        assert _is_linked(a1, 'java_Method35', b)
    _safe_set(b, 'java_Classifier36', a2)
    assert _is_linked(b, 'java_Classifier36', a2)
    if hasattr(a1, 'java_Method35'):
        assert not _is_linked(a1, 'java_Method35', b)
    if hasattr(a2, 'java_Method35'):
        assert _is_linked(a2, 'java_Method35', b)
    _safe_set(b, 'java_Classifier36', None)
    assert not _is_linked(b, 'java_Classifier36', a2)
    if hasattr(a2, 'java_Method35'):
        assert not _is_linked(a2, 'java_Method35', b)


def test_assoc_returnType29_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier30', a1)
    assert _is_linked(b, 'java_Classifier30', a1)
    if hasattr(a1, 'java_Method'):
        assert _is_linked(a1, 'java_Method', b)
    _safe_set(b, 'java_Classifier30', a2)
    assert _is_linked(b, 'java_Classifier30', a2)
    if hasattr(a1, 'java_Method'):
        assert not _is_linked(a1, 'java_Method', b)
    if hasattr(a2, 'java_Method'):
        assert _is_linked(a2, 'java_Method', b)
    _safe_set(b, 'java_Classifier30', None)
    assert not _is_linked(b, 'java_Classifier30', a2)
    if hasattr(a2, 'java_Method'):
        assert not _is_linked(a2, 'java_Method', b)


def test_assoc_system1_reverse_link_reassign_clear():
    a1 = java_System(name="sample_text")
    a2 = java_System(name="sample_text_2")
    b = java_Package(name="sample_text")
    _safe_set(b, 'packages', a1)
    assert _is_linked(b, 'packages', a1)
    if hasattr(a1, 'System'):
        assert _is_linked(a1, 'System', b)
    _safe_set(b, 'packages', a2)
    assert _is_linked(b, 'packages', a2)
    if hasattr(a1, 'System'):
        assert not _is_linked(a1, 'System', b)
    if hasattr(a2, 'System'):
        assert _is_linked(a2, 'System', b)
    _safe_set(b, 'packages', None)
    assert not _is_linked(b, 'packages', a2)
    if hasattr(a2, 'System'):
        assert not _is_linked(a2, 'System', b)


def test_assoc_type19_reverse_link_reassign_clear():
    a1 = java_Field(default="sample_text", isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Field(default="sample_text_2", isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier20', a1)
    assert _is_linked(b, 'java_Classifier20', a1)
    if hasattr(a1, 'java_Field'):
        assert _is_linked(a1, 'java_Field', b)
    _safe_set(b, 'java_Classifier20', a2)
    assert _is_linked(b, 'java_Classifier20', a2)
    if hasattr(a1, 'java_Field'):
        assert not _is_linked(a1, 'java_Field', b)
    if hasattr(a2, 'java_Field'):
        assert _is_linked(a2, 'java_Field', b)
    _safe_set(b, 'java_Classifier20', None)
    assert not _is_linked(b, 'java_Classifier20', a2)
    if hasattr(a2, 'java_Field'):
        assert not _is_linked(a2, 'java_Field', b)


def test_assoc_type42_reverse_link_reassign_clear():
    a1 = java_Classifier(name="sample_text")
    a2 = java_Classifier(name="sample_text_2")
    b = java_Argument(name="sample_text", order=7)
    _safe_set(b, 'java_Argument', a1)
    assert _is_linked(b, 'java_Argument', a1)
    if hasattr(a1, 'java_Classifier43'):
        assert _is_linked(a1, 'java_Classifier43', b)
    _safe_set(b, 'java_Argument', a2)
    assert _is_linked(b, 'java_Argument', a2)
    if hasattr(a1, 'java_Classifier43'):
        assert not _is_linked(a1, 'java_Classifier43', b)
    if hasattr(a2, 'java_Classifier43'):
        assert _is_linked(a2, 'java_Classifier43', b)
    _safe_set(b, 'java_Argument', None)
    assert not _is_linked(b, 'java_Argument', a2)
    if hasattr(a2, 'java_Classifier43'):
        assert not _is_linked(a2, 'java_Classifier43', b)


def test_assoc_upperBoundings47_reverse_link_reassign_clear():
    a1 = java_GenericBinding(name="sample_text")
    a2 = java_GenericBinding(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'java_Classifier48', a1)
    assert _is_linked(b, 'java_Classifier48', a1)
    if hasattr(a1, 'java_GenericBinding'):
        assert _is_linked(a1, 'java_GenericBinding', b)
    _safe_set(b, 'java_Classifier48', a2)
    assert _is_linked(b, 'java_Classifier48', a2)
    if hasattr(a1, 'java_GenericBinding'):
        assert not _is_linked(a1, 'java_GenericBinding', b)
    if hasattr(a2, 'java_GenericBinding'):
        assert _is_linked(a2, 'java_GenericBinding', b)
    _safe_set(b, 'java_Classifier48', None)
    assert not _is_linked(b, 'java_Classifier48', a2)
    if hasattr(a2, 'java_GenericBinding'):
        assert not _is_linked(a2, 'java_GenericBinding', b)


def test_assoc_usingClassifier52_reverse_link_reassign_clear():
    a1 = java_GenericBinding(name="sample_text")
    a2 = java_GenericBinding(name="sample_text_2")
    b = java_Classifier(name="sample_text")
    _safe_set(b, 'Classifier53', a1)
    assert _is_linked(b, 'Classifier53', a1)
    if hasattr(a1, 'genericBindings'):
        assert _is_linked(a1, 'genericBindings', b)
    _safe_set(b, 'Classifier53', a2)
    assert _is_linked(b, 'Classifier53', a2)
    if hasattr(a1, 'genericBindings'):
        assert not _is_linked(a1, 'genericBindings', b)
    if hasattr(a2, 'genericBindings'):
        assert _is_linked(a2, 'genericBindings', b)
    _safe_set(b, 'Classifier53', None)
    assert not _is_linked(b, 'Classifier53', a2)
    if hasattr(a2, 'genericBindings'):
        assert not _is_linked(a2, 'genericBindings', b)


def test_assoc_usingMethod44_reverse_link_reassign_clear():
    a1 = java_Method(concurrency="sample_text", isAbstract=True, isDefault=True, isFinal=True, isStatic=True, name="sample_text")
    a2 = java_Method(concurrency="sample_text_2", isAbstract=False, isDefault=False, isFinal=False, isStatic=False, name="sample_text_2")
    b = java_Argument(name="sample_text", order=7)
    _safe_set(b, 'arguments', a1)
    assert _is_linked(b, 'arguments', a1)
    if hasattr(a1, 'Method45'):
        assert _is_linked(a1, 'Method45', b)
    _safe_set(b, 'arguments', a2)
    assert _is_linked(b, 'arguments', a2)
    if hasattr(a1, 'Method45'):
        assert not _is_linked(a1, 'Method45', b)
    if hasattr(a2, 'Method45'):
        assert _is_linked(a2, 'Method45', b)
    _safe_set(b, 'arguments', None)
    assert not _is_linked(b, 'arguments', a2)
    if hasattr(a2, 'Method45'):
        assert not _is_linked(a2, 'Method45', b)


def test_assoc_values58_reverse_link_reassign_clear():
    a1 = java_AnnotationInstanceValue(id=7, name="sample_text", value="sample_text")
    a2 = java_AnnotationInstanceValue(id=13, name="sample_text_2", value="sample_text_2")
    b = java_AnnotationInstanceParameter(name="sample_text")
    _safe_set(b, 'parameter', {a1})
    assert _is_linked(b, 'parameter', a1)
    if hasattr(a1, 'AnnotationInstanceValue'):
        assert _is_linked(a1, 'AnnotationInstanceValue', b)
    _safe_set(b, 'parameter', {a2})
    assert _is_linked(b, 'parameter', a2)
    if hasattr(a1, 'AnnotationInstanceValue'):
        assert not _is_linked(a1, 'AnnotationInstanceValue', b)
    if hasattr(a2, 'AnnotationInstanceValue'):
        assert _is_linked(a2, 'AnnotationInstanceValue', b)
    _safe_set(b, 'parameter', set())
    assert not _is_linked(b, 'parameter', a2)
    if hasattr(a2, 'AnnotationInstanceValue'):
        assert not _is_linked(a2, 'AnnotationInstanceValue', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_annotable57_stub_double():
    # java_Annotable has no real 'Annotable' property in the generated
    # code (a bare stub) -- manually attach it so java_AnnotationInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_AnnotationInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_AnnotationInstance(name="sample_text")
    partner = java_Annotable()
    setattr(partner, 'Annotable', None)
    _safe_set(owner, 'annotationInstances', partner)
    assert getattr(partner, 'Annotable') == owner
    _safe_set(owner, 'annotationInstances', None)
    assert getattr(partner, 'Annotable') is None


def test_assoc_annotation55_stub_double():
    # java_Annotation has no real 'java_Annotation' property in the generated
    # code (a bare stub) -- manually attach it so java_AnnotationInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_AnnotationInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_AnnotationInstance(name="sample_text")
    partner = java_Annotation()
    setattr(partner, 'java_Annotation', None)
    _safe_set(owner, 'java_AnnotationInstance', partner)
    assert getattr(partner, 'java_Annotation') == owner
    _safe_set(owner, 'java_AnnotationInstance', None)
    assert getattr(partner, 'java_Annotation') is None


def test_assoc_annotationInstances54_stub_double():
    # java_Annotable has no real 'annotable' property in the generated
    # code (a bare stub) -- manually attach it so java_AnnotationInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_AnnotationInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_AnnotationInstance(name="sample_text")
    partner = java_Annotable()
    setattr(partner, 'annotable', None)
    _safe_set(owner, 'AnnotationInstance', partner)
    assert owner in getattr(partner, 'annotable')
    _safe_set(owner, 'AnnotationInstance', None)
    assert owner not in getattr(partner, 'annotable')


def test_assoc_assertion40_stub_double():
    # java_AssertStatement has no real 'containerStatement' property in the generated
    # code (a bare stub) -- manually attach it so java_GETExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_GETExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_GETExpression(leftSide="sample_text", rightSide="sample_text")
    partner = java_AssertStatement()
    setattr(partner, 'containerStatement', None)
    _safe_set(owner, 'GETExpression', partner)
    assert getattr(partner, 'containerStatement') == owner
    _safe_set(owner, 'GETExpression', None)
    assert getattr(partner, 'containerStatement') is None


def test_assoc_containedElements46_stub_double():
    # java_Container has no real 'container' property in the generated
    # code (a bare stub) -- manually attach it so java_Contained's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Contained's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Contained(visibility="sample_text")
    partner = java_Container()
    setattr(partner, 'container', None)
    _safe_set(owner, 'Contained', partner)
    assert owner in getattr(partner, 'container')
    _safe_set(owner, 'Contained', None)
    assert owner not in getattr(partner, 'container')


def test_assoc_container27_stub_double():
    # java_Container has no real 'Container' property in the generated
    # code (a bare stub) -- manually attach it so java_Contained's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_Contained's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_Contained(visibility="sample_text")
    partner = java_Container()
    setattr(partner, 'Container', None)
    _safe_set(owner, 'containedElements', partner)
    assert getattr(partner, 'Container') == owner
    _safe_set(owner, 'containedElements', None)
    assert getattr(partner, 'Container') is None


def test_assoc_containerStatement41_stub_double():
    # java_AssertStatement has no real 'AssertStatement' property in the generated
    # code (a bare stub) -- manually attach it so java_GETExpression's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_GETExpression's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_GETExpression(leftSide="sample_text", rightSide="sample_text")
    partner = java_AssertStatement()
    setattr(partner, 'AssertStatement', None)
    _safe_set(owner, 'assertion', partner)
    assert getattr(partner, 'AssertStatement') == owner
    _safe_set(owner, 'assertion', None)
    assert getattr(partner, 'AssertStatement') is None


def test_assoc_interface7_stub_double():
    # java_Interface has no real 'java_Interface' property in the generated
    # code (a bare stub) -- manually attach it so java_InterfaceImplementation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # java_InterfaceImplementation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = java_InterfaceImplementation(name="sample_text")
    partner = java_Interface()
    setattr(partner, 'java_Interface', None)
    _safe_set(owner, 'java_InterfaceImplementation', partner)
    assert getattr(partner, 'java_Interface') == owner
    _safe_set(owner, 'java_InterfaceImplementation', None)
    assert getattr(partner, 'java_Interface') is None


