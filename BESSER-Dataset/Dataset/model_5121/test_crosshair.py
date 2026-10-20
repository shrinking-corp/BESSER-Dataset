from python_code import diva_AndTerm

def test_diva_AndTerm___init__():
    assert diva_AndTerm.__init__(diva_AndTerm()) == None

def test_diva_AndTerm_accept():
    assert diva_AndTerm.accept(diva_AndTerm(), '', '') == None


from python_code import diva_Annotation
from python_code import diva_DiVAModelElement

def test_diva_Annotation___init__():
    assert diva_Annotation.__init__(diva_Annotation('', '\x00', diva_Annotation=diva_DiVAModelElement()), '\x00\x00', '', diva_Annotation=diva_DiVAModelElement()) == None

def test_diva_Annotation_accept():
    assert diva_Annotation.accept(diva_Annotation('', '', diva_Annotation=diva_DiVAModelElement()), '', '') == None


from python_code import diva_BoolVariableValue

def test_diva_BoolVariableValue___init__():
    assert diva_BoolVariableValue.__init__(diva_BoolVariableValue(True), False) == None

def test_diva_BoolVariableValue_accept():
    assert diva_BoolVariableValue.accept(diva_BoolVariableValue(False), 0, '\x00\x00') == None


from python_code import diva_BooleanTerm

def test_diva_BooleanTerm___init__():
    assert diva_BooleanTerm.__init__(diva_BooleanTerm()) == None

def test_diva_BooleanTerm_accept():
    assert diva_BooleanTerm.accept(diva_BooleanTerm(), '', '') == None


from python_code import diva_BooleanVariable

def test_diva_BooleanVariable___init__():
    assert diva_BooleanVariable.__init__(diva_BooleanVariable()) == None

def test_diva_BooleanVariable_accept():
    assert diva_BooleanVariable.accept(diva_BooleanVariable(), '', '') == None


from python_code import diva_EnumVariable

def test_diva_EnumVariable___init__():
    assert diva_EnumVariable.__init__(diva_EnumVariable(diva_EnumVariable=set()), diva_EnumVariable=set()) == None

def test_diva_EnumVariable_accept():
    assert diva_EnumVariable.accept(diva_EnumVariable(diva_EnumVariable=set()), 0, '\x00\x00') == None


from python_code import diva_NamedElement

def test_diva_NamedElement___init__():
    assert diva_NamedElement.__init__(diva_NamedElement('', '\x00'), '\x00\x00', '') == None


from python_code import diva_NotTerm
from python_code import diva_Term

def test_diva_NotTerm___init__():
    assert diva_NotTerm.__init__(diva_NotTerm(diva_NotTerm=diva_Term()), diva_NotTerm=diva_Term()) == None

def test_diva_NotTerm_accept():
    assert diva_NotTerm.accept(diva_NotTerm(diva_NotTerm=diva_Term()), '', '') == None


from python_code import diva_OrTerm

def test_diva_OrTerm___init__():
    assert diva_OrTerm.__init__(diva_OrTerm()) == None

def test_diva_OrTerm_accept():
    assert diva_OrTerm.accept(diva_OrTerm(), '', '') == None


from python_code import diva_visitors_TopDownVisitor

def test_diva_visitors_TopDownVisitor___init__():
    assert diva_visitors_TopDownVisitor.__init__(diva_visitors_TopDownVisitor()) == None

def test_diva_visitors_TopDownVisitor_visitVariant():
    assert diva_visitors_TopDownVisitor.visitVariant(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitPropertyValue():
    assert diva_visitors_TopDownVisitor.visitPropertyValue(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitOrTerm():
    assert diva_visitors_TopDownVisitor.visitOrTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitNotTerm():
    assert diva_visitors_TopDownVisitor.visitNotTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitVariabilityModel():
    assert diva_visitors_TopDownVisitor.visitVariabilityModel(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitConfiguration():
    assert diva_visitors_TopDownVisitor.visitConfiguration(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitEnumVariableValue():
    assert diva_visitors_TopDownVisitor.visitEnumVariableValue(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitContextExpression():
    assert diva_visitors_TopDownVisitor.visitContextExpression(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitEnumLiteral():
    assert diva_visitors_TopDownVisitor.visitEnumLiteral(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitConfigVariant():
    assert diva_visitors_TopDownVisitor.visitConfigVariant(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitBaseModel():
    assert diva_visitors_TopDownVisitor.visitBaseModel(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitBooleanVariable():
    assert diva_visitors_TopDownVisitor.visitBooleanVariable(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitDimension():
    assert diva_visitors_TopDownVisitor.visitDimension(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitBoolVariableValue():
    assert diva_visitors_TopDownVisitor.visitBoolVariableValue(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitVariantTerm():
    assert diva_visitors_TopDownVisitor.visitVariantTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitScore():
    assert diva_visitors_TopDownVisitor.visitScore(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitEnumTerm():
    assert diva_visitors_TopDownVisitor.visitEnumTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitEnumVariable():
    assert diva_visitors_TopDownVisitor.visitEnumVariable(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitInvariant():
    assert diva_visitors_TopDownVisitor.visitInvariant(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitPropertyPriority():
    assert diva_visitors_TopDownVisitor.visitPropertyPriority(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitProperty():
    assert diva_visitors_TopDownVisitor.visitProperty(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitAndTerm():
    assert diva_visitors_TopDownVisitor.visitAndTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitScenario():
    assert diva_visitors_TopDownVisitor.visitScenario(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitAnnotation():
    assert diva_visitors_TopDownVisitor.visitAnnotation(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitMultiplicityConstraint():
    assert diva_visitors_TopDownVisitor.visitMultiplicityConstraint(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitAspectModel():
    assert diva_visitors_TopDownVisitor.visitAspectModel(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitBooleanTerm():
    assert diva_visitors_TopDownVisitor.visitBooleanTerm(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitVariantExpression():
    assert diva_visitors_TopDownVisitor.visitVariantExpression(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitContext():
    assert diva_visitors_TopDownVisitor.visitContext(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitExpression():
    assert diva_visitors_TopDownVisitor.visitExpression(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitPriority():
    assert diva_visitors_TopDownVisitor.visitPriority(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitPriorityRule():
    assert diva_visitors_TopDownVisitor.visitPriorityRule(diva_visitors_TopDownVisitor(), '', '') == None

def test_diva_visitors_TopDownVisitor_visitSimulationModel():
    assert diva_visitors_TopDownVisitor.visitSimulationModel(diva_visitors_TopDownVisitor(), '', '') == None


from python_code import diva_visitors_Visitable

def test_diva_visitors_Visitable___init__():
    assert diva_visitors_Visitable.__init__(diva_visitors_Visitable()) == None

def test_diva_visitors_Visitable_accept():
    assert diva_visitors_Visitable.accept(diva_visitors_Visitable(), '', '') == None


from python_code import diva_visitors_Visitor

def test_diva_visitors_Visitor___init__():
    assert diva_visitors_Visitor.__init__(diva_visitors_Visitor()) == None

def test_diva_visitors_Visitor_visitVariantTerm():
    assert diva_visitors_Visitor.visitVariantTerm(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitPropertyValue():
    assert diva_visitors_Visitor.visitPropertyValue(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitInvariant():
    assert diva_visitors_Visitor.visitInvariant(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitOrTerm():
    assert diva_visitors_Visitor.visitOrTerm(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitBooleanVariable():
    assert diva_visitors_Visitor.visitBooleanVariable(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitExpression():
    assert diva_visitors_Visitor.visitExpression(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitBoolVariableValue():
    assert diva_visitors_Visitor.visitBoolVariableValue(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitPriorityRule():
    assert diva_visitors_Visitor.visitPriorityRule(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitDimension():
    assert diva_visitors_Visitor.visitDimension(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitProperty():
    assert diva_visitors_Visitor.visitProperty(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitEnumVariableValue():
    assert diva_visitors_Visitor.visitEnumVariableValue(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitEnumLiteral():
    assert diva_visitors_Visitor.visitEnumLiteral(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitScenario():
    assert diva_visitors_Visitor.visitScenario(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitAnnotation():
    assert diva_visitors_Visitor.visitAnnotation(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitBooleanTerm():
    assert diva_visitors_Visitor.visitBooleanTerm(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitEnumTerm():
    assert diva_visitors_Visitor.visitEnumTerm(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitContextExpression():
    assert diva_visitors_Visitor.visitContextExpression(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitConfigVariant():
    assert diva_visitors_Visitor.visitConfigVariant(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitScore():
    assert diva_visitors_Visitor.visitScore(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitSimulationModel():
    assert diva_visitors_Visitor.visitSimulationModel(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitVariantExpression():
    assert diva_visitors_Visitor.visitVariantExpression(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitVariabilityModel():
    assert diva_visitors_Visitor.visitVariabilityModel(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitEnumVariable():
    assert diva_visitors_Visitor.visitEnumVariable(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitVariant():
    assert diva_visitors_Visitor.visitVariant(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitBaseModel():
    assert diva_visitors_Visitor.visitBaseModel(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitConfiguration():
    assert diva_visitors_Visitor.visitConfiguration(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitAspectModel():
    assert diva_visitors_Visitor.visitAspectModel(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitPriority():
    assert diva_visitors_Visitor.visitPriority(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitMultiplicityConstraint():
    assert diva_visitors_Visitor.visitMultiplicityConstraint(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitPropertyPriority():
    assert diva_visitors_Visitor.visitPropertyPriority(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitContext():
    assert diva_visitors_Visitor.visitContext(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitAndTerm():
    assert diva_visitors_Visitor.visitAndTerm(diva_visitors_Visitor(), '', '') == None

def test_diva_visitors_Visitor_visitNotTerm():
    assert diva_visitors_Visitor.visitNotTerm(diva_visitors_Visitor(), '', '') == None

