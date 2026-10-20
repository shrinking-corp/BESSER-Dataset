from python_code import pivot_BooleanLiteralExp

def test_pivot_BooleanLiteralExp___init__():
    assert pivot_BooleanLiteralExp.__init__(pivot_BooleanLiteralExp(''), '') == None

def test_pivot_BooleanLiteralExp_TypeIsBoolean():
    assert pivot_BooleanLiteralExp.TypeIsBoolean(pivot_BooleanLiteralExp(''), 0, '\x00\x00') == None


from python_code import pivot_CallExp
from python_code import pivot_OCLExpression

def test_pivot_CallExp___init__():
    assert pivot_CallExp.__init__(pivot_CallExp('', pivot_CallExp=pivot_OCLExpression()), '', pivot_CallExp=pivot_OCLExpression()) == None


from python_code import pivot_CollectionItem
from python_code import pivot_OCLExpression

def test_pivot_CollectionItem___init__():
    assert pivot_CollectionItem.__init__(pivot_CollectionItem(pivot_CollectionItem=pivot_OCLExpression()), pivot_CollectionItem=pivot_OCLExpression()) == None

def test_pivot_CollectionItem_TypeIsItemType():
    assert pivot_CollectionItem.TypeIsItemType(pivot_CollectionItem(pivot_CollectionItem=pivot_OCLExpression()), '', '') == None


from python_code import pivot_ConstructorExp

def test_pivot_ConstructorExp___init__():
    assert pivot_ConstructorExp.__init__(pivot_ConstructorExp('', pivot_ConstructorExp=set()), '', pivot_ConstructorExp=set()) == None


from python_code import pivot_Annotation
from python_code import pivot_Detail

def test_pivot_Detail___init__():
    assert pivot_Detail.__init__(pivot_Detail('', pivot_Detail=pivot_Annotation()), '', pivot_Detail=pivot_Annotation()) == None


from python_code import pivot_Feature

def test_pivot_Feature___init__():
    assert pivot_Feature.__init__(pivot_Feature('', '\x00'), '\x00\x00', '') == None


from python_code import pivot_FeatureCallExp

def test_pivot_FeatureCallExp___init__():
    assert pivot_FeatureCallExp.__init__(pivot_FeatureCallExp(''), '') == None


from python_code import pivot_IfExp
from python_code import pivot_OCLExpression

def test_pivot_IfExp___init__():
    assert pivot_IfExp.__init__(pivot_IfExp(pivot_IfExp=pivot_OCLExpression(), pivot_IfExp74=pivot_OCLExpression(), pivot_IfExp77=pivot_OCLExpression()), pivot_IfExp=pivot_OCLExpression(), pivot_IfExp74=pivot_OCLExpression(), pivot_IfExp77=pivot_OCLExpression()) == None

def test_pivot_IfExp_ConditionTypeIsBoolean():
    assert pivot_IfExp.ConditionTypeIsBoolean(pivot_IfExp(pivot_IfExp=pivot_OCLExpression(), pivot_IfExp74=pivot_OCLExpression(), pivot_IfExp77=pivot_OCLExpression()), '', '') == None


from python_code import pivot_IntegerLiteralExp

def test_pivot_IntegerLiteralExp___init__():
    assert pivot_IntegerLiteralExp.__init__(pivot_IntegerLiteralExp(''), '') == None

def test_pivot_IntegerLiteralExp_TypeIsInteger():
    assert pivot_IntegerLiteralExp.TypeIsInteger(pivot_IntegerLiteralExp(''), 0, '\x00\x00') == None


from python_code import pivot_IteratorExp

def test_pivot_IteratorExp___init__():
    assert pivot_IteratorExp.__init__(pivot_IteratorExp()) == None

def test_pivot_IteratorExp_ClosureSourceElementTypeIsBodyElementType():
    assert pivot_IteratorExp.ClosureSourceElementTypeIsBodyElementType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ClosureHasOneIterator():
    assert pivot_IteratorExp.ClosureHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_IsUniqueHasOneIterator():
    assert pivot_IteratorExp.IsUniqueHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_OneHasOneIterator():
    assert pivot_IteratorExp.OneHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectTypeIsUnordered():
    assert pivot_IteratorExp.CollectTypeIsUnordered(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_AnyBodyTypeIsBoolean():
    assert pivot_IteratorExp.AnyBodyTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_AnyHasOneIterator():
    assert pivot_IteratorExp.AnyHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_SortedByIteratorTypeIsComparable():
    assert pivot_IteratorExp.SortedByIteratorTypeIsComparable(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_IteratorTypeIsSourceElementType():
    assert pivot_IteratorExp.IteratorTypeIsSourceElementType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectElementTypeIsSourceElementType():
    assert pivot_IteratorExp.CollectElementTypeIsSourceElementType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_OneTypeIsBoolean():
    assert pivot_IteratorExp.OneTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_SortedByHasOneIterator():
    assert pivot_IteratorExp.SortedByHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectNestedTypeIsBodyType():
    assert pivot_IteratorExp.CollectNestedTypeIsBodyType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_RejectOrSelectTypeIsBoolean():
    assert pivot_IteratorExp.RejectOrSelectTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_RejectOrSelectTypeIsSourceType():
    assert pivot_IteratorExp.RejectOrSelectTypeIsSourceType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ForAllTypeIsBoolean():
    assert pivot_IteratorExp.ForAllTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_RejectOrSelectHasOneIterator():
    assert pivot_IteratorExp.RejectOrSelectHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ForAllBodyTypeIsBoolean():
    assert pivot_IteratorExp.ForAllBodyTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectHasOneIterator():
    assert pivot_IteratorExp.CollectHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_AnyTypeIsSourceElementType():
    assert pivot_IteratorExp.AnyTypeIsSourceElementType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectNestedHasOneIterator():
    assert pivot_IteratorExp.CollectNestedHasOneIterator(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_SortedByIsOrderedIfSourceIsOrdered():
    assert pivot_IteratorExp.SortedByIsOrderedIfSourceIsOrdered(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ClosureBodyTypeIsConformanttoIteratorType():
    assert pivot_IteratorExp.ClosureBodyTypeIsConformanttoIteratorType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_CollectNestedTypeIsBag():
    assert pivot_IteratorExp.CollectNestedTypeIsBag(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ClosureTypeIsUniqueCollection():
    assert pivot_IteratorExp.ClosureTypeIsUniqueCollection(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ExistsBodyTypeIsBoolean():
    assert pivot_IteratorExp.ExistsBodyTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_IsUniqueTypeIsBoolean():
    assert pivot_IteratorExp.IsUniqueTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_OneBodyTypeIsBoolean():
    assert pivot_IteratorExp.OneBodyTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_SortedByElementTypeIsSourceElementType():
    assert pivot_IteratorExp.SortedByElementTypeIsSourceElementType(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ExistsTypeIsBoolean():
    assert pivot_IteratorExp.ExistsTypeIsBoolean(pivot_IteratorExp(), '', '') == None

def test_pivot_IteratorExp_ClosureElementTypeIsSourceElementType():
    assert pivot_IteratorExp.ClosureElementTypeIsSourceElementType(pivot_IteratorExp(), '', '') == None


from python_code import pivot_CallOperationAction
from python_code import pivot_MessageExp
from python_code import pivot_OCLExpression
from python_code import pivot_SendSignalAction

def test_pivot_MessageExp___init__():
    assert pivot_MessageExp.__init__(pivot_MessageExp(pivot_MessageExp=pivot_OCLExpression(), pivot_MessageExp112=set(), pivot_MessageExp115=pivot_CallOperationAction(), pivot_MessageExp118=pivot_SendSignalAction()), pivot_MessageExp=pivot_OCLExpression(), pivot_MessageExp112=set(), pivot_MessageExp115=pivot_CallOperationAction(), pivot_MessageExp118=pivot_SendSignalAction()) == None

def test_pivot_MessageExp_TargetIsNotACollection():
    assert pivot_MessageExp.TargetIsNotACollection(pivot_MessageExp(pivot_MessageExp=pivot_OCLExpression(), pivot_MessageExp112=set(), pivot_MessageExp115=pivot_CallOperationAction(), pivot_MessageExp118=pivot_SendSignalAction()), 0, '\x00\x00') == None

def test_pivot_MessageExp_OneCallOrOneSend():
    assert pivot_MessageExp.OneCallOrOneSend(pivot_MessageExp(pivot_MessageExp=pivot_OCLExpression(), pivot_MessageExp112=set(), pivot_MessageExp115=pivot_CallOperationAction(), pivot_MessageExp118=pivot_SendSignalAction()), 0, '\x00\x00') == None


from python_code import pivot_NamedElement

def test_pivot_NamedElement___init__():
    assert pivot_NamedElement.__init__(pivot_NamedElement('\x00\x00', '', pivot_NamedElement=set()), '', '', pivot_NamedElement=set()) == None


from python_code import pivot_ParameterableElement
from python_code import pivot_TemplateParameter
from python_code import pivot_TemplateParameterSubstitution

def test_pivot_ParameterableElement___init__():
    assert pivot_ParameterableElement.__init__(pivot_ParameterableElement(ownedParameteredElement=pivot_TemplateParameter(), parameteredElement=pivot_TemplateParameter(), pivot_ParameterableElement282=pivot_TemplateParameterSubstitution(), pivot_ParameterableElement285=pivot_TemplateParameterSubstitution(), ParameterableElement=pivot_TemplateParameter(), ParameterableElement273=pivot_TemplateParameter(), pivot_ParameterableElement=pivot_TemplateParameter(), pivot_ParameterableElement277=pivot_TemplateParameter()), ownedParameteredElement=pivot_TemplateParameter(), parameteredElement=pivot_TemplateParameter(), pivot_ParameterableElement282=pivot_TemplateParameterSubstitution(), pivot_ParameterableElement285=pivot_TemplateParameterSubstitution(), ParameterableElement=pivot_TemplateParameter(), ParameterableElement273=pivot_TemplateParameter(), pivot_ParameterableElement=pivot_TemplateParameter(), pivot_ParameterableElement277=pivot_TemplateParameter()) == None

def test_pivot_ParameterableElement_isCompatibleWith():
    assert pivot_ParameterableElement.isCompatibleWith(pivot_ParameterableElement(ownedParameteredElement=pivot_TemplateParameter(), parameteredElement=pivot_TemplateParameter(), pivot_ParameterableElement282=pivot_TemplateParameterSubstitution(), pivot_ParameterableElement285=pivot_TemplateParameterSubstitution(), ParameterableElement=pivot_TemplateParameter(), ParameterableElement273=pivot_TemplateParameter(), pivot_ParameterableElement=pivot_TemplateParameter(), pivot_ParameterableElement277=pivot_TemplateParameter()), '') == None

def test_pivot_ParameterableElement_isTemplateParameter():
    assert pivot_ParameterableElement.isTemplateParameter(pivot_ParameterableElement(ownedParameteredElement=pivot_TemplateParameter(), parameteredElement=pivot_TemplateParameter(), pivot_ParameterableElement282=pivot_TemplateParameterSubstitution(), pivot_ParameterableElement285=pivot_TemplateParameterSubstitution(), ParameterableElement=pivot_TemplateParameter(), ParameterableElement273=pivot_TemplateParameter(), pivot_ParameterableElement=pivot_TemplateParameter(), pivot_ParameterableElement277=pivot_TemplateParameter())) == None


from python_code import pivot_RealLiteralExp

def test_pivot_RealLiteralExp___init__():
    assert pivot_RealLiteralExp.__init__(pivot_RealLiteralExp(''), '') == None


from python_code import pivot_ReferringElement

def test_pivot_ReferringElement___init__():
    assert pivot_ReferringElement.__init__(pivot_ReferringElement()) == None

def test_pivot_ReferringElement_getReferredElement():
    assert pivot_ReferringElement.getReferredElement(pivot_ReferringElement()) == None


from python_code import pivot_SelfType

def test_pivot_SelfType___init__():
    assert pivot_SelfType.__init__(pivot_SelfType()) == None

def test_pivot_SelfType_specializeIn():
    assert pivot_SelfType.specializeIn(pivot_SelfType(), '', '') == None


from python_code import pivot_StringLiteralExp

def test_pivot_StringLiteralExp___init__():
    assert pivot_StringLiteralExp.__init__(pivot_StringLiteralExp(''), '') == None


from python_code import pivot_TemplateParameterType

def test_pivot_TemplateParameterType___init__():
    assert pivot_TemplateParameterType.__init__(pivot_TemplateParameterType(''), '') == None


from python_code import pivot_TypeTemplateParameter

def test_pivot_TypeTemplateParameter___init__():
    assert pivot_TypeTemplateParameter.__init__(pivot_TypeTemplateParameter('', pivot_TypeTemplateParameter=set()), '', pivot_TypeTemplateParameter=set()) == None


from python_code import pivot_TypedMultiplicityElement

def test_pivot_TypedMultiplicityElement___init__():
    assert pivot_TypedMultiplicityElement.__init__(pivot_TypedMultiplicityElement()) == None

def test_pivot_TypedMultiplicityElement_CompatibleBody():
    assert pivot_TypedMultiplicityElement.CompatibleBody(pivot_TypedMultiplicityElement(), '') == None

def test_pivot_TypedMultiplicityElement_makeParameter():
    assert pivot_TypedMultiplicityElement.makeParameter(pivot_TypedMultiplicityElement()) == None


from python_code import pivot_UnlimitedNaturalLiteralExp

def test_pivot_UnlimitedNaturalLiteralExp___init__():
    assert pivot_UnlimitedNaturalLiteralExp.__init__(pivot_UnlimitedNaturalLiteralExp(''), '') == None


from python_code import pivot_ValueSpecification

def test_pivot_ValueSpecification___init__():
    assert pivot_ValueSpecification.__init__(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_stringValue():
    assert pivot_ValueSpecification.stringValue(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_integerValue():
    assert pivot_ValueSpecification.integerValue(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_unlimitedValue():
    assert pivot_ValueSpecification.unlimitedValue(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_isNull():
    assert pivot_ValueSpecification.isNull(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_isComputable():
    assert pivot_ValueSpecification.isComputable(pivot_ValueSpecification()) == None

def test_pivot_ValueSpecification_booleanValue():
    assert pivot_ValueSpecification.booleanValue(pivot_ValueSpecification()) == None


from python_code import pivot_VariableDeclaration
from python_code import pivot_VariableExp

def test_pivot_VariableExp___init__():
    assert pivot_VariableExp.__init__(pivot_VariableExp('', pivot_VariableExp=pivot_VariableDeclaration()), '', pivot_VariableExp=pivot_VariableDeclaration()) == None

