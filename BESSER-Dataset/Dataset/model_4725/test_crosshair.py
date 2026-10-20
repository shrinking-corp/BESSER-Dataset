from python_code import asmeta_basicterms_CollectionTerm

def test_asmeta_basicterms_CollectionTerm___init__():
    assert asmeta_basicterms_CollectionTerm.__init__(asmeta_basicterms_CollectionTerm(''), '') == None


from python_code import asmeta_basicterms_ConstantTerm

def test_asmeta_basicterms_ConstantTerm___init__():
    assert asmeta_basicterms_ConstantTerm.__init__(asmeta_basicterms_ConstantTerm(''), '') == None


from python_code import asmeta_basicterms_Term
from python_code import domains_Domain

def test_asmeta_basicterms_Term___init__():
    assert asmeta_basicterms_Term.__init__(asmeta_basicterms_Term(asmeta_basicterms_Term=domains_Domain(), term=set()), asmeta_basicterms_Term=domains_Domain(), term=set()) == None

def test_asmeta_basicterms_Term_compatible():
    assert asmeta_basicterms_Term.compatible(asmeta_basicterms_Term(asmeta_basicterms_Term=domains_Domain(), term=set())) == None


from python_code import asmeta_basicterms_TupleTerm

def test_asmeta_basicterms_TupleTerm___init__():
    assert asmeta_basicterms_TupleTerm.__init__(asmeta_basicterms_TupleTerm('', '\x00'), '\x00\x00', '') == None


from python_code import asmeta_basicterms_VariableTerm
from python_code import furtherterms_FiniteQuantificationTerm

def test_asmeta_basicterms_VariableTerm___init__():
    assert asmeta_basicterms_VariableTerm.__init__(asmeta_basicterms_VariableTerm('', '\x00', variable=furtherterms_FiniteQuantificationTerm()), '\x00\x00', '', variable=furtherterms_FiniteQuantificationTerm()) == None


from python_code import asmeta_basictransitionrules_BlockRule

def test_asmeta_basictransitionrules_BlockRule___init__():
    assert asmeta_basictransitionrules_BlockRule.__init__(asmeta_basictransitionrules_BlockRule(''), '') == None


from python_code import asmeta_basictransitionrules_ChooseRule
from python_code import basicterms_Term
from python_code import basictransitionrules_Rule

def test_asmeta_basictransitionrules_ChooseRule___init__():
    assert asmeta_basictransitionrules_ChooseRule.__init__(asmeta_basictransitionrules_ChooseRule('', asmeta_basictransitionrules_ChooseRule=basictransitionrules_Rule(), asmeta_basictransitionrules_ChooseRule178=basictransitionrules_Rule(), asmeta_basictransitionrules_ChooseRule181=basicterms_Term(), asmeta_basictransitionrules_ChooseRule184=set()), '', asmeta_basictransitionrules_ChooseRule=basictransitionrules_Rule(), asmeta_basictransitionrules_ChooseRule178=basictransitionrules_Rule(), asmeta_basictransitionrules_ChooseRule181=basicterms_Term(), asmeta_basictransitionrules_ChooseRule184=set()) == None


from python_code import asmeta_basictransitionrules_ForallRule
from python_code import basicterms_Term
from python_code import basictransitionrules_Rule

def test_asmeta_basictransitionrules_ForallRule___init__():
    assert asmeta_basictransitionrules_ForallRule.__init__(asmeta_basictransitionrules_ForallRule('', asmeta_basictransitionrules_ForallRule=set(), asmeta_basictransitionrules_ForallRule199=basicterms_Term(), asmeta_basictransitionrules_ForallRule202=basictransitionrules_Rule()), '', asmeta_basictransitionrules_ForallRule=set(), asmeta_basictransitionrules_ForallRule199=basicterms_Term(), asmeta_basictransitionrules_ForallRule202=basictransitionrules_Rule()) == None


from python_code import asmeta_basictransitionrules_MacroCallRule
from python_code import basictransitionrules_MacroDeclaration

def test_asmeta_basictransitionrules_MacroCallRule___init__():
    assert asmeta_basictransitionrules_MacroCallRule.__init__(asmeta_basictransitionrules_MacroCallRule('', asmeta_basictransitionrules_MacroCallRule=basictransitionrules_MacroDeclaration()), '', asmeta_basictransitionrules_MacroCallRule=basictransitionrules_MacroDeclaration()) == None


from python_code import asmeta_basictransitionrules_TermAsRule
from python_code import basicterms_Term

def test_asmeta_basictransitionrules_TermAsRule___init__():
    assert asmeta_basictransitionrules_TermAsRule.__init__(asmeta_basictransitionrules_TermAsRule('', termAsRule=basicterms_Term()), '', termAsRule=basicterms_Term()) == None


from python_code import FunctionDefinition
from python_code import Signature
from python_code import asmeta_definitions_Function
from python_code import domains_Domain

def test_asmeta_definitions_Function___init__():
    assert asmeta_definitions_Function.__init__(asmeta_definitions_Function('', asmeta_definitions_Function=domains_Domain(), asmeta_definitions_Function248=domains_Domain(), definedFunction=FunctionDefinition(), constrainedFunction=set(), function=Signature()), '', asmeta_definitions_Function=domains_Domain(), asmeta_definitions_Function248=domains_Domain(), definedFunction=FunctionDefinition(), constrainedFunction=set(), function=Signature()) == None


from python_code import Body
from python_code import asmeta_definitions_RuleDeclaration
from python_code import basictransitionrules_Rule

def test_asmeta_definitions_RuleDeclaration___init__():
    assert asmeta_definitions_RuleDeclaration.__init__(asmeta_definitions_RuleDeclaration('', asmeta_definitions_RuleDeclaration=set(), constrainedRule=set(), asmeta_definitions_RuleDeclaration229=basictransitionrules_Rule(), ruleDeclaration=Body()), '', asmeta_definitions_RuleDeclaration=set(), constrainedRule=set(), asmeta_definitions_RuleDeclaration229=basictransitionrules_Rule(), ruleDeclaration=Body()) == None


from python_code import asmeta_derivedtransitionrules_CaseRule
from python_code import basicterms_Term
from python_code import basictransitionrules_Rule

def test_asmeta_derivedtransitionrules_CaseRule___init__():
    assert asmeta_derivedtransitionrules_CaseRule.__init__(asmeta_derivedtransitionrules_CaseRule('', asmeta_derivedtransitionrules_CaseRule=basicterms_Term(), asmeta_derivedtransitionrules_CaseRule169=set(), asmeta_derivedtransitionrules_CaseRule172=basictransitionrules_Rule()), '', asmeta_derivedtransitionrules_CaseRule=basicterms_Term(), asmeta_derivedtransitionrules_CaseRule169=set(), asmeta_derivedtransitionrules_CaseRule172=basictransitionrules_Rule()) == None


from python_code import asmeta_domains_AbstractTd

def test_asmeta_domains_AbstractTd___init__():
    assert asmeta_domains_AbstractTd.__init__(asmeta_domains_AbstractTd(''), '') == None


from python_code import DomainDefinition
from python_code import asmeta_domains_ConcreteDomain
from python_code import domains_TypeDomain

def test_asmeta_domains_ConcreteDomain___init__():
    assert asmeta_domains_ConcreteDomain.__init__(asmeta_domains_ConcreteDomain('', initializedDomain=set(), definedDomain=DomainDefinition(), asmeta_domains_ConcreteDomain=domains_TypeDomain()), '', initializedDomain=set(), definedDomain=DomainDefinition(), asmeta_domains_ConcreteDomain=domains_TypeDomain()) == None


from python_code import Signature
from python_code import asmeta_domains_Domain

def test_asmeta_domains_Domain___init__():
    assert asmeta_domains_Domain.__init__(asmeta_domains_Domain(constrainedDomain=set(), domain=Signature()), constrainedDomain=set(), domain=Signature()) == None

def test_asmeta_domains_Domain_compatible():
    assert asmeta_domains_Domain.compatible(asmeta_domains_Domain(constrainedDomain=set(), domain=Signature())) == None


from python_code import asmeta_domains_EnumElement

def test_asmeta_domains_EnumElement___init__():
    assert asmeta_domains_EnumElement.__init__(asmeta_domains_EnumElement(''), '') == None


from python_code import asmeta_domains_ProductDomain

def test_asmeta_domains_ProductDomain___init__():
    assert asmeta_domains_ProductDomain.__init__(asmeta_domains_ProductDomain(''), '') == None


from python_code import asmeta_domains_RuleDomain

def test_asmeta_domains_RuleDomain___init__():
    assert asmeta_domains_RuleDomain.__init__(asmeta_domains_RuleDomain(''), '') == None


from python_code import asmeta_furtherterms_CaseTerm
from python_code import basicterms_Term

def test_asmeta_furtherterms_CaseTerm___init__():
    assert asmeta_furtherterms_CaseTerm.__init__(asmeta_furtherterms_CaseTerm('', asmeta_furtherterms_CaseTerm=set(), asmeta_furtherterms_CaseTerm29=basicterms_Term(), asmeta_furtherterms_CaseTerm32=basicterms_Term()), '', asmeta_furtherterms_CaseTerm=set(), asmeta_furtherterms_CaseTerm29=basicterms_Term(), asmeta_furtherterms_CaseTerm32=basicterms_Term()) == None


from python_code import asmeta_furtherterms_ComprehensionTerm
from python_code import basicterms_Term

def test_asmeta_furtherterms_ComprehensionTerm___init__():
    assert asmeta_furtherterms_ComprehensionTerm.__init__(asmeta_furtherterms_ComprehensionTerm('', asmeta_furtherterms_ComprehensionTerm=set(), asmeta_furtherterms_ComprehensionTerm21=basicterms_Term(), asmeta_furtherterms_ComprehensionTerm24=basicterms_Term()), '', asmeta_furtherterms_ComprehensionTerm=set(), asmeta_furtherterms_ComprehensionTerm21=basicterms_Term(), asmeta_furtherterms_ComprehensionTerm24=basicterms_Term()) == None


from python_code import asmeta_furtherterms_FiniteQuantificationTerm
from python_code import basicterms_Term

def test_asmeta_furtherterms_FiniteQuantificationTerm___init__():
    assert asmeta_furtherterms_FiniteQuantificationTerm.__init__(asmeta_furtherterms_FiniteQuantificationTerm('', finiteQuantificationTerm=set(), asmeta_furtherterms_FiniteQuantificationTerm=basicterms_Term()), '', finiteQuantificationTerm=set(), asmeta_furtherterms_FiniteQuantificationTerm=basicterms_Term()) == None


from python_code import asmeta_furtherterms_SequenceTerm

def test_asmeta_furtherterms_SequenceTerm___init__():
    assert asmeta_furtherterms_SequenceTerm.__init__(asmeta_furtherterms_SequenceTerm(''), '') == None


from python_code import Body
from python_code import Header
from python_code import Initialization
from python_code import asmeta_structure_Asm
from python_code import basictransitionrules_MacroDeclaration

def test_asmeta_structure_Asm___init__():
    assert asmeta_structure_Asm.__init__(asmeta_structure_Asm('', asmeta_structure_Asm=set(), asm=Initialization(), asm127=Body(), asm129=Header(), asmeta_structure_Asm132=basictransitionrules_MacroDeclaration()), '', asmeta_structure_Asm=set(), asm=Initialization(), asm127=Body(), asm129=Header(), asmeta_structure_Asm132=basictransitionrules_MacroDeclaration()) == None


from python_code import asmeta_structure_ImportClause

def test_asmeta_structure_ImportClause___init__():
    assert asmeta_structure_ImportClause.__init__(asmeta_structure_ImportClause('', asmeta_structure_ImportClause=set(), asmeta_structure_ImportClause91=set(), asmeta_structure_ImportClause94=set()), '', asmeta_structure_ImportClause=set(), asmeta_structure_ImportClause91=set(), asmeta_structure_ImportClause94=set()) == None


from python_code import asmeta_structure_NamedElement

def test_asmeta_structure_NamedElement___init__():
    assert asmeta_structure_NamedElement.__init__(asmeta_structure_NamedElement(''), '') == None


from python_code import asmeta_turbotransitionrules_SeqRule

def test_asmeta_turbotransitionrules_SeqRule___init__():
    assert asmeta_turbotransitionrules_SeqRule.__init__(asmeta_turbotransitionrules_SeqRule(''), '') == None


from python_code import asmeta_turbotransitionrules_TurboCallRule
from python_code import turbotransitionrules_TurboDeclaration

def test_asmeta_turbotransitionrules_TurboCallRule___init__():
    assert asmeta_turbotransitionrules_TurboCallRule.__init__(asmeta_turbotransitionrules_TurboCallRule('', asmeta_turbotransitionrules_TurboCallRule=turbotransitionrules_TurboDeclaration()), '', asmeta_turbotransitionrules_TurboCallRule=turbotransitionrules_TurboDeclaration()) == None

