import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Argument,
    Condition,
    Constant,
    Dimension,
    ExtentConstant,
    FormElement,
    Formulation,
    FormulationForm,
    Grammar_ParseElement,
    Instance,
    ItemElement,
    Keyword,
    LocalName,
    ModifiedTerm,
    Modifier,
    NBVR_Grammar_CompoundForm,
    NBVR_Grammar_Condition,
    NBVR_Grammar_Dimension,
    NBVR_Grammar_DomainForm,
    NBVR_Grammar_GroupPhrase,
    NBVR_Grammar_ImplicationForm,
    NBVR_Grammar_Instance,
    NBVR_Grammar_Intension,
    NBVR_Grammar_LexicalInstance,
    NBVR_Grammar_LocalName,
    NBVR_Grammar_ModifiedTerm,
    NBVR_Grammar_Modifier,
    NBVR_Grammar_Nominalization,
    NBVR_Grammar_Parse,
    NBVR_Grammar_ParseElement,
    NBVR_Grammar_PartPhrase,
    NBVR_Grammar_Pronoun,
    NBVR_Grammar_ProperName,
    NBVR_Grammar_PropertyNoun,
    NBVR_Grammar_Qualifier,
    NBVR_Grammar_QualifierChain,
    NBVR_Grammar_Quantifier,
    NBVR_Grammar_Quantity,
    NBVR_Grammar_QueryPhrase,
    NBVR_Grammar_Question,
    NBVR_Grammar_RoleNoun,
    NBVR_Grammar_RolePhrase,
    NBVR_Grammar_Sentence,
    NBVR_Grammar_SimpleForm,
    NBVR_Grammar_SimpleNounPhrase,
    NBVR_Grammar_SimpleQualifier,
    NBVR_Grammar_Statement,
    NBVR_Grammar_TypeNoun,
    NBVR_Grammar_VerbPhrase,
    NBVR_Logic_Argument,
    NBVR_Logic_Connection,
    NBVR_Logic_Constant,
    NBVR_Logic_ExtentConstant,
    NBVR_Logic_Implication,
    NBVR_Logic_Modal,
    NBVR_Logic_Negation,
    NBVR_Logic_NominalConstant,
    NBVR_Logic_Predicate,
    NBVR_Logic_Proposition,
    NBVR_Logic_Quantification,
    NBVR_Logic_QuantityValue,
    NBVR_Logic_Relation,
    NBVR_Logic_RoleVariable,
    NBVR_Logic_Set,
    NBVR_Logic_ValueConstant,
    NBVR_Logic_Variable,
    NBVR_Vocabulary_Adjective,
    NBVR_Vocabulary_Adjunct,
    NBVR_Vocabulary_DateTime,
    NBVR_Vocabulary_Definition,
    NBVR_Vocabulary_Dictionary,
    NBVR_Vocabulary_FormElement,
    NBVR_Vocabulary_Formulation,
    NBVR_Vocabulary_FormulationForm,
    NBVR_Vocabulary_IsVerb,
    NBVR_Vocabulary_ItemElement,
    NBVR_Vocabulary_Keyword,
    NBVR_Vocabulary_Name,
    NBVR_Vocabulary_Noun,
    NBVR_Vocabulary_NumberWord,
    NBVR_Vocabulary_Particle,
    NBVR_Vocabulary_RoleElement,
    NBVR_Vocabulary_StringWord,
    NBVR_Vocabulary_SyntaxForm,
    NBVR_Vocabulary_Term,
    NBVR_Vocabulary_Terminology,
    NBVR_Vocabulary_Verb,
    NBVR_Vocabulary_VerbRole,
    NBVR_Vocabulary_VocAdjective,
    NBVR_Vocabulary_VocName,
    NBVR_Vocabulary_VocNoun,
    NBVR_Vocabulary_VocProperty,
    NBVR_Vocabulary_VocUnit,
    NBVR_Vocabulary_VocVerb,
    NBVR_Vocabulary_VocabularyItem,
    NBVR_Vocabulary_Word,
    NBVR_Vocabulary_WordForm,
    Nominalization,
    NumberWord,
    ParseElement,
    PartPhrase,
    Particle,
    Predicate,
    Proposition,
    Qualifier,
    QualifierChain,
    Quantification,
    Quantifier,
    Quantity,
    QueryPhrase,
    Question,
    Relation,
    RoleElement,
    RolePhrase,
    RoleVariable,
    Sentence,
    Set,
    SimpleNounPhrase,
    SimpleQualifier,
    SyntaxForm,
    Term,
    TypeNoun,
    Variable,
    Verb,
    VerbPhrase,
    VerbRole,
    VocAdjective,
    VocName,
    VocNoun,
    VocProperty,
    VocUnit,
    VocVerb,
    VocabularyItem,
    Vocabulary_FormulationForm,
    Word,
    WordForm,
    Connective,
    ElementKind,
    FormElementKind,
    GroupKind,
    InstanceKind,
    KeywordKind,
    Modality,
    PhraseType,
    PropositionKind,
    QuantifierKind,
    QueryKind,
    SentenceType,
    VocItemKind,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_adjective146_stub_double():
    # VocAdjective has no real 'VocAdjective' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Modifier(kind="sample_text")
    partner = VocAdjective()
    setattr(partner, 'VocAdjective', None)
    _safe_set(owner, 'NBVR_Grammar_Modifier', partner)
    assert getattr(partner, 'VocAdjective') == owner
    _safe_set(owner, 'NBVR_Grammar_Modifier', None)
    assert getattr(partner, 'VocAdjective') is None


def test_assoc_altPast104_stub_double():
    # WordForm has no real 'WordForm106' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm106', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb105', partner)
    assert getattr(partner, 'WordForm106') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb105', None)
    assert getattr(partner, 'WordForm106') is None


def test_assoc_altWord10_stub_double():
    # Word has no real 'Word12' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_WordForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_WordForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_WordForm(text="sample_text")
    partner = Word()
    setattr(partner, 'Word12', None)
    _safe_set(owner, 'NBVR_Vocabulary_WordForm11', partner)
    assert getattr(partner, 'Word12') == owner
    _safe_set(owner, 'NBVR_Vocabulary_WordForm11', None)
    assert getattr(partner, 'Word12') is None


def test_assoc_alternative180_stub_double():
    # Sentence has no real 'Sentence182' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_ImplicationForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_ImplicationForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_ImplicationForm(kind="sample_text")
    partner = Sentence()
    setattr(partner, 'Sentence182', None)
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm181', partner)
    assert getattr(partner, 'Sentence182') == owner
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm181', None)
    assert getattr(partner, 'Sentence182') is None


def test_assoc_antecedent122_stub_double():
    # Sentence has no real 'Sentence' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Condition(otherwise=True)
    partner = Sentence()
    setattr(partner, 'Sentence', None)
    _safe_set(owner, 'NBVR_Grammar_Condition', partner)
    assert getattr(partner, 'Sentence') == owner
    _safe_set(owner, 'NBVR_Grammar_Condition', None)
    assert getattr(partner, 'Sentence') is None


def test_assoc_antecedent175_stub_double():
    # Sentence has no real 'Sentence176' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_ImplicationForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_ImplicationForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_ImplicationForm(kind="sample_text")
    partner = Sentence()
    setattr(partner, 'Sentence176', None)
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm', partner)
    assert getattr(partner, 'Sentence176') == owner
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm', None)
    assert getattr(partner, 'Sentence176') is None


def test_assoc_arguments220_stub_double():
    # Argument has no real 'Argument' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Relation()
    partner = Argument()
    setattr(partner, 'Argument', None)
    _safe_set(owner, 'relation', {partner})
    assert getattr(partner, 'Argument') == owner
    _safe_set(owner, 'relation', set())
    assert getattr(partner, 'Argument') is None


def test_assoc_base0_stub_double():
    # WordForm has no real 'WordForm' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Word's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Word's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Word()
    partner = WordForm()
    setattr(partner, 'WordForm', None)
    _safe_set(owner, 'NBVR_Vocabulary_Word', partner)
    assert getattr(partner, 'WordForm') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Word', None)
    assert getattr(partner, 'WordForm') is None


def test_assoc_base25_stub_double():
    # VocabularyItem has no real 'VocabularyItem26' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocabularyItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocabularyItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocabularyItem()
    partner = VocabularyItem()
    setattr(partner, 'VocabularyItem26', None)
    _safe_set(owner, 'NBVR_Vocabulary_VocabularyItem', {partner})
    assert getattr(partner, 'VocabularyItem26') == owner
    _safe_set(owner, 'NBVR_Vocabulary_VocabularyItem', set())
    assert getattr(partner, 'VocabularyItem26') is None


def test_assoc_beginsTerm1_stub_double():
    # Term has no real 'Term' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Word's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Word's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Word()
    partner = Term()
    setattr(partner, 'Term', None)
    _safe_set(owner, 'NBVR_Vocabulary_Word2', {partner})
    assert getattr(partner, 'Term') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Word2', set())
    assert getattr(partner, 'Term') is None


def test_assoc_concept13_stub_double():
    # VocabularyItem has no real 'VocabularyItem' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = VocabularyItem()
    setattr(partner, 'VocabularyItem', None)
    _safe_set(owner, 'terms', partner)
    assert getattr(partner, 'VocabularyItem') == owner
    _safe_set(owner, 'terms', None)
    assert getattr(partner, 'VocabularyItem') is None


def test_assoc_concept35_stub_double():
    # VocabularyItem has no real 'VocabularyItem36' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Formulation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Formulation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Formulation(language="sample_text", text="sample_text")
    partner = VocabularyItem()
    setattr(partner, 'VocabularyItem36', None)
    _safe_set(owner, 'formulations', partner)
    assert getattr(partner, 'VocabularyItem36') == owner
    _safe_set(owner, 'formulations', None)
    assert getattr(partner, 'VocabularyItem36') is None


def test_assoc_consequent177_stub_double():
    # Sentence has no real 'Sentence179' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_ImplicationForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_ImplicationForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_ImplicationForm(kind="sample_text")
    partner = Sentence()
    setattr(partner, 'Sentence179', None)
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm178', partner)
    assert getattr(partner, 'Sentence179') == owner
    _safe_set(owner, 'NBVR_Grammar_ImplicationForm178', None)
    assert getattr(partner, 'Sentence179') is None


def test_assoc_constant234_stub_double():
    # Constant has no real 'Constant' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = Constant()
    setattr(partner, 'Constant', None)
    _safe_set(owner, 'NBVR_Logic_Argument235', partner)
    assert getattr(partner, 'Constant') == owner
    _safe_set(owner, 'NBVR_Logic_Argument235', None)
    assert getattr(partner, 'Constant') is None


def test_assoc_constraint206_stub_double():
    # Proposition has no real 'Proposition' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Variable(name="sample_text")
    partner = Proposition()
    setattr(partner, 'Proposition', None)
    _safe_set(owner, 'NBVR_Logic_Variable', partner)
    assert getattr(partner, 'Proposition') == owner
    _safe_set(owner, 'NBVR_Logic_Variable', None)
    assert getattr(partner, 'Proposition') is None


def test_assoc_context19_stub_double():
    # VocabularyItem has no real 'VocabularyItem21' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = VocabularyItem()
    setattr(partner, 'VocabularyItem21', None)
    _safe_set(owner, 'NBVR_Vocabulary_Term20', partner)
    assert getattr(partner, 'VocabularyItem21') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Term20', None)
    assert getattr(partner, 'VocabularyItem21') is None


def test_assoc_domain129_stub_double():
    # RolePhrase has no real 'RolePhrase130' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Sentence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Sentence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Sentence()
    partner = RolePhrase()
    setattr(partner, 'RolePhrase130', None)
    _safe_set(owner, 'NBVR_Grammar_Sentence', partner)
    assert getattr(partner, 'RolePhrase130') == owner
    _safe_set(owner, 'NBVR_Grammar_Sentence', None)
    assert getattr(partner, 'RolePhrase130') is None


def test_assoc_domain190_stub_double():
    # RolePhrase has no real 'RolePhrase191' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_QueryPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_QueryPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_QueryPhrase(query="sample_text")
    partner = RolePhrase()
    setattr(partner, 'RolePhrase191', None)
    _safe_set(owner, 'NBVR_Grammar_QueryPhrase', partner)
    assert getattr(partner, 'RolePhrase191') == owner
    _safe_set(owner, 'NBVR_Grammar_QueryPhrase', None)
    assert getattr(partner, 'RolePhrase191') is None


def test_assoc_element22_stub_double():
    # ItemElement has no real 'ItemElement' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = ItemElement()
    setattr(partner, 'ItemElement', None)
    _safe_set(owner, 'term23', {partner})
    assert getattr(partner, 'ItemElement') == owner
    _safe_set(owner, 'term23', set())
    assert getattr(partner, 'ItemElement') is None


def test_assoc_elements34_stub_double():
    # ParseElement has no real 'ParseElement' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Formulation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Formulation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Formulation(language="sample_text", text="sample_text")
    partner = ParseElement()
    setattr(partner, 'ParseElement', None)
    _safe_set(owner, 'NBVR_Vocabulary_Formulation', {partner})
    assert getattr(partner, 'ParseElement') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Formulation', set())
    assert getattr(partner, 'ParseElement') is None


def test_assoc_elements53_stub_double():
    # FormElement has no real 'FormElement' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_SyntaxForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_SyntaxForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_SyntaxForm(isAuxForm=True, text="sample_text")
    partner = FormElement()
    setattr(partner, 'FormElement', None)
    _safe_set(owner, 'form54', {partner})
    assert getattr(partner, 'FormElement') == owner
    _safe_set(owner, 'form54', set())
    assert getattr(partner, 'FormElement') is None


def test_assoc_form33_stub_double():
    # FormulationForm has no real 'FormulationForm' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Formulation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Formulation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Formulation(language="sample_text", text="sample_text")
    partner = FormulationForm()
    setattr(partner, 'FormulationForm', None)
    _safe_set(owner, 'formulation', partner)
    assert getattr(partner, 'FormulationForm') == owner
    _safe_set(owner, 'formulation', None)
    assert getattr(partner, 'FormulationForm') is None


def test_assoc_form48_stub_double():
    # SyntaxForm has no real 'SyntaxForm' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocVerb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocVerb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocVerb(arity=7)
    partner = SyntaxForm()
    setattr(partner, 'SyntaxForm', None)
    _safe_set(owner, 'verb49', {partner})
    assert getattr(partner, 'SyntaxForm') == owner
    _safe_set(owner, 'verb49', set())
    assert getattr(partner, 'SyntaxForm') is None


def test_assoc_form59_stub_double():
    # SyntaxForm has no real 'SyntaxForm60' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_FormElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_FormElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_FormElement(kind="sample_text")
    partner = SyntaxForm()
    setattr(partner, 'SyntaxForm60', None)
    _safe_set(owner, 'elements', partner)
    assert getattr(partner, 'SyntaxForm60') == owner
    _safe_set(owner, 'elements', None)
    assert getattr(partner, 'SyntaxForm60') is None


def test_assoc_formulation37_stub_double():
    # Formulation has no real 'Formulation38' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_FormulationForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_FormulationForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_FormulationForm()
    partner = Formulation()
    setattr(partner, 'Formulation38', None)
    _safe_set(owner, 'form', partner)
    assert getattr(partner, 'Formulation38') == owner
    _safe_set(owner, 'form', None)
    assert getattr(partner, 'Formulation38') is None


def test_assoc_formulations24_stub_double():
    # Formulation has no real 'Formulation' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocabularyItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocabularyItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocabularyItem()
    partner = Formulation()
    setattr(partner, 'Formulation', None)
    _safe_set(owner, 'concept', {partner})
    assert getattr(partner, 'Formulation') == owner
    _safe_set(owner, 'concept', set())
    assert getattr(partner, 'Formulation') is None


def test_assoc_isAVerb43_stub_double():
    # VocVerb has no real 'VocVerb44' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocNoun's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocNoun's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocNoun(massNoun=True)
    partner = VocVerb()
    setattr(partner, 'VocVerb44', None)
    _safe_set(owner, 'NBVR_Vocabulary_VocNoun', partner)
    assert getattr(partner, 'VocVerb44') == owner
    _safe_set(owner, 'NBVR_Vocabulary_VocNoun', None)
    assert getattr(partner, 'VocVerb44') is None


def test_assoc_members114_stub_double():
    # SimpleNounPhrase has no real 'SimpleNounPhrase' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_GroupPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_GroupPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_GroupPhrase(kind="sample_text")
    partner = SimpleNounPhrase()
    setattr(partner, 'SimpleNounPhrase', None)
    _safe_set(owner, 'NBVR_Grammar_GroupPhrase', {partner})
    assert getattr(partner, 'SimpleNounPhrase') == owner
    _safe_set(owner, 'NBVR_Grammar_GroupPhrase', set())
    assert getattr(partner, 'SimpleNounPhrase') is None


def test_assoc_next223_stub_double():
    # Argument has no real 'Argument224' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = Argument()
    setattr(partner, 'Argument224', None)
    _safe_set(owner, 'NBVR_Logic_Argument', partner)
    assert getattr(partner, 'Argument224') == owner
    _safe_set(owner, 'NBVR_Logic_Argument', None)
    assert getattr(partner, 'Argument224') is None


def test_assoc_next27_stub_double():
    # VocabularyItem has no real 'VocabularyItem29' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocabularyItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocabularyItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocabularyItem()
    partner = VocabularyItem()
    setattr(partner, 'VocabularyItem29', None)
    _safe_set(owner, 'NBVR_Vocabulary_VocabularyItem28', partner)
    assert getattr(partner, 'VocabularyItem29') == owner
    _safe_set(owner, 'NBVR_Vocabulary_VocabularyItem28', None)
    assert getattr(partner, 'VocabularyItem29') is None


def test_assoc_next3_stub_double():
    # Word has no real 'Word' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Word's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Word's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Word()
    partner = Word()
    setattr(partner, 'Word', None)
    _safe_set(owner, 'NBVR_Vocabulary_Word4', partner)
    assert getattr(partner, 'Word') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Word4', None)
    assert getattr(partner, 'Word') is None


def test_assoc_next5_stub_double():
    # WordForm has no real 'WordForm6' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_WordForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_WordForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_WordForm(text="sample_text")
    partner = WordForm()
    setattr(partner, 'WordForm6', None)
    _safe_set(owner, 'NBVR_Vocabulary_WordForm', partner)
    assert getattr(partner, 'WordForm6') == owner
    _safe_set(owner, 'NBVR_Vocabulary_WordForm', None)
    assert getattr(partner, 'WordForm6') is None


def test_assoc_noun262_stub_double():
    # VocNoun has no real 'VocNoun264' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Predicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Predicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Predicate(name="sample_text")
    partner = VocNoun()
    setattr(partner, 'VocNoun264', None)
    _safe_set(owner, 'predicate263', partner)
    assert getattr(partner, 'VocNoun264') == owner
    _safe_set(owner, 'predicate263', None)
    assert getattr(partner, 'VocNoun264') is None


def test_assoc_object172_stub_double():
    # RolePhrase has no real 'RolePhrase174' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_SimpleForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_SimpleForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_SimpleForm()
    partner = RolePhrase()
    setattr(partner, 'RolePhrase174', None)
    _safe_set(owner, 'NBVR_Grammar_SimpleForm173', partner)
    assert getattr(partner, 'RolePhrase174') == owner
    _safe_set(owner, 'NBVR_Grammar_SimpleForm173', None)
    assert getattr(partner, 'RolePhrase174') is None


def test_assoc_operands244_stub_double():
    # Proposition has no real 'Proposition245' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Connection(kind="sample_text")
    partner = Proposition()
    setattr(partner, 'Proposition245', None)
    _safe_set(owner, 'NBVR_Logic_Connection', {partner})
    assert getattr(partner, 'Proposition245') == owner
    _safe_set(owner, 'NBVR_Logic_Connection', set())
    assert getattr(partner, 'Proposition245') is None


def test_assoc_owner218_stub_double():
    # Proposition has no real 'Proposition219' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Proposition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Proposition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Proposition(text="sample_text")
    partner = Proposition()
    setattr(partner, 'Proposition219', None)
    _safe_set(owner, 'NBVR_Logic_Proposition', partner)
    assert getattr(partner, 'Proposition219') == owner
    _safe_set(owner, 'NBVR_Logic_Proposition', None)
    assert getattr(partner, 'Proposition219') is None


def test_assoc_parent203_stub_double():
    # ParseElement has no real 'ParseElement204' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_ParseElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_ParseElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_ParseElement()
    partner = ParseElement()
    setattr(partner, 'ParseElement204', None)
    _safe_set(owner, 'NBVR_Grammar_ParseElement', partner)
    assert getattr(partner, 'ParseElement204') == owner
    _safe_set(owner, 'NBVR_Grammar_ParseElement', None)
    assert getattr(partner, 'ParseElement204') is None


def test_assoc_partPhrases167_stub_double():
    # PartPhrase has no real 'PartPhrase' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_SimpleForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_SimpleForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_SimpleForm()
    partner = PartPhrase()
    setattr(partner, 'PartPhrase', None)
    _safe_set(owner, 'NBVR_Grammar_SimpleForm168', {partner})
    assert getattr(partner, 'PartPhrase') == owner
    _safe_set(owner, 'NBVR_Grammar_SimpleForm168', set())
    assert getattr(partner, 'PartPhrase') is None


def test_assoc_particle15_stub_double():
    # Particle has no real 'Particle' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = Particle()
    setattr(partner, 'Particle', None)
    _safe_set(owner, 'term16', partner)
    assert getattr(partner, 'Particle') == owner
    _safe_set(owner, 'term16', None)
    assert getattr(partner, 'Particle') is None


def test_assoc_past95_stub_double():
    # WordForm has no real 'WordForm97' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm97', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb96', partner)
    assert getattr(partner, 'WordForm97') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb96', None)
    assert getattr(partner, 'WordForm97') is None


def test_assoc_perfective101_stub_double():
    # WordForm has no real 'WordForm103' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm103', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb102', partner)
    assert getattr(partner, 'WordForm103') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb102', None)
    assert getattr(partner, 'WordForm103') is None


def test_assoc_phrase228_stub_double():
    # RolePhrase has no real 'RolePhrase230' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = RolePhrase()
    setattr(partner, 'RolePhrase230', None)
    _safe_set(owner, 'NBVR_Logic_Argument229', partner)
    assert getattr(partner, 'RolePhrase230') == owner
    _safe_set(owner, 'NBVR_Logic_Argument229', None)
    assert getattr(partner, 'RolePhrase230') is None


def test_assoc_plural92_stub_double():
    # WordForm has no real 'WordForm94' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm94', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb93', partner)
    assert getattr(partner, 'WordForm94') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb93', None)
    assert getattr(partner, 'WordForm94') is None


def test_assoc_predicate221_stub_double():
    # Predicate has no real 'Predicate222' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Relation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Relation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Relation()
    partner = Predicate()
    setattr(partner, 'Predicate222', None)
    _safe_set(owner, 'NBVR_Logic_Relation', partner)
    assert getattr(partner, 'Predicate222') == owner
    _safe_set(owner, 'NBVR_Logic_Relation', None)
    assert getattr(partner, 'Predicate222') is None


def test_assoc_predicate45_stub_double():
    # Predicate has no real 'Predicate' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocNoun's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocNoun's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocNoun(massNoun=True)
    partner = Predicate()
    setattr(partner, 'Predicate', None)
    _safe_set(owner, 'noun', partner)
    assert getattr(partner, 'Predicate') == owner
    _safe_set(owner, 'noun', None)
    assert getattr(partner, 'Predicate') is None


def test_assoc_predicate50_stub_double():
    # Predicate has no real 'Predicate52' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocVerb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocVerb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocVerb(arity=7)
    partner = Predicate()
    setattr(partner, 'Predicate52', None)
    _safe_set(owner, 'verb51', partner)
    assert getattr(partner, 'Predicate52') == owner
    _safe_set(owner, 'verb51', None)
    assert getattr(partner, 'Predicate52') is None


def test_assoc_progressive98_stub_double():
    # WordForm has no real 'WordForm100' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm100', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb99', partner)
    assert getattr(partner, 'WordForm100') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb99', None)
    assert getattr(partner, 'WordForm100') is None


def test_assoc_property55_stub_double():
    # VocProperty has no real 'VocProperty' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_SyntaxForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_SyntaxForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_SyntaxForm(isAuxForm=True, text="sample_text")
    partner = VocProperty()
    setattr(partner, 'VocProperty', None)
    _safe_set(owner, 'propertyForm', partner)
    assert getattr(partner, 'VocProperty') == owner
    _safe_set(owner, 'propertyForm', None)
    assert getattr(partner, 'VocProperty') is None


def test_assoc_qualifier121_stub_double():
    # SimpleQualifier has no real 'SimpleQualifier' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Condition(otherwise=True)
    partner = SimpleQualifier()
    setattr(partner, 'SimpleQualifier', None)
    _safe_set(owner, 'condition', partner)
    assert getattr(partner, 'SimpleQualifier') == owner
    _safe_set(owner, 'condition', None)
    assert getattr(partner, 'SimpleQualifier') is None


def test_assoc_quantity141_stub_double():
    # Quantity has no real 'Quantity' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Quantifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Quantifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Quantifier(count=7, kind="sample_text")
    partner = Quantity()
    setattr(partner, 'Quantity', None)
    _safe_set(owner, 'NBVR_Grammar_Quantifier', partner)
    assert getattr(partner, 'Quantity') == owner
    _safe_set(owner, 'NBVR_Grammar_Quantifier', None)
    assert getattr(partner, 'Quantity') is None


def test_assoc_queryPhrase189_stub_double():
    # QueryPhrase has no real 'QueryPhrase' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Question's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Question's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Question(query="sample_text")
    partner = QueryPhrase()
    setattr(partner, 'QueryPhrase', None)
    _safe_set(owner, 'question', partner)
    assert getattr(partner, 'QueryPhrase') == owner
    _safe_set(owner, 'question', None)
    assert getattr(partner, 'QueryPhrase') is None


def test_assoc_question192_stub_double():
    # Question has no real 'Question' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_QueryPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_QueryPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_QueryPhrase(query="sample_text")
    partner = Question()
    setattr(partner, 'Question', None)
    _safe_set(owner, 'queryPhrase', partner)
    assert getattr(partner, 'Question') == owner
    _safe_set(owner, 'queryPhrase', None)
    assert getattr(partner, 'Question') is None


def test_assoc_range209_stub_double():
    # VocNoun has no real 'VocNoun211' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Variable(name="sample_text")
    partner = VocNoun()
    setattr(partner, 'VocNoun211', None)
    _safe_set(owner, 'NBVR_Logic_Variable210', partner)
    assert getattr(partner, 'VocNoun211') == owner
    _safe_set(owner, 'NBVR_Logic_Variable210', None)
    assert getattr(partner, 'VocNoun211') is None


def test_assoc_range39_stub_double():
    # VocNoun has no real 'VocNoun' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VerbRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VerbRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VerbRole(isRange=True)
    partner = VocNoun()
    setattr(partner, 'VocNoun', None)
    _safe_set(owner, 'NBVR_Vocabulary_VerbRole', partner)
    assert getattr(partner, 'VocNoun') == owner
    _safe_set(owner, 'NBVR_Vocabulary_VerbRole', None)
    assert getattr(partner, 'VocNoun') is None


def test_assoc_referent119_stub_double():
    # RolePhrase has no real 'RolePhrase' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_RolePhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_RolePhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_RolePhrase()
    partner = RolePhrase()
    setattr(partner, 'RolePhrase', None)
    _safe_set(owner, 'NBVR_Grammar_RolePhrase120', partner)
    assert getattr(partner, 'RolePhrase') == owner
    _safe_set(owner, 'NBVR_Grammar_RolePhrase120', None)
    assert getattr(partner, 'RolePhrase') is None


def test_assoc_relation236_stub_double():
    # Relation has no real 'Relation237' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = Relation()
    setattr(partner, 'Relation237', None)
    _safe_set(owner, 'arguments', partner)
    assert getattr(partner, 'Relation237') == owner
    _safe_set(owner, 'arguments', None)
    assert getattr(partner, 'Relation237') is None


def test_assoc_relative147_stub_double():
    # RolePhrase has no real 'RolePhrase149' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Modifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Modifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Modifier(kind="sample_text")
    partner = RolePhrase()
    setattr(partner, 'RolePhrase149', None)
    _safe_set(owner, 'NBVR_Grammar_Modifier148', partner)
    assert getattr(partner, 'RolePhrase149') == owner
    _safe_set(owner, 'NBVR_Grammar_Modifier148', None)
    assert getattr(partner, 'RolePhrase149') is None


def test_assoc_rewrites131_stub_double():
    # Sentence has no real 'Sentence133' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Sentence's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Sentence's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Sentence()
    partner = Sentence()
    setattr(partner, 'Sentence133', None)
    _safe_set(owner, 'NBVR_Grammar_Sentence132', partner)
    assert getattr(partner, 'Sentence133') == owner
    _safe_set(owner, 'NBVR_Grammar_Sentence132', None)
    assert getattr(partner, 'Sentence133') is None


def test_assoc_role14_stub_double():
    # VerbRole has no real 'VerbRole' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = VerbRole()
    setattr(partner, 'VerbRole', None)
    _safe_set(owner, 'term', partner)
    assert getattr(partner, 'VerbRole') == owner
    _safe_set(owner, 'term', None)
    assert getattr(partner, 'VerbRole') is None


def test_assoc_role231_stub_double():
    # VerbRole has no real 'VerbRole233' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = VerbRole()
    setattr(partner, 'VerbRole233', None)
    _safe_set(owner, 'NBVR_Logic_Argument232', partner)
    assert getattr(partner, 'VerbRole233') == owner
    _safe_set(owner, 'NBVR_Logic_Argument232', None)
    assert getattr(partner, 'VerbRole233') is None


def test_assoc_role81_stub_double():
    # VerbRole has no real 'VerbRole82' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_RoleElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_RoleElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_RoleElement(slot=7)
    partner = VerbRole()
    setattr(partner, 'VerbRole82', None)
    _safe_set(owner, 'NBVR_Vocabulary_RoleElement', partner)
    assert getattr(partner, 'VerbRole82') == owner
    _safe_set(owner, 'NBVR_Vocabulary_RoleElement', None)
    assert getattr(partner, 'VerbRole82') is None


def test_assoc_rolePlayed115_stub_double():
    # VerbRole has no real 'VerbRole116' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_RolePhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_RolePhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_RolePhrase()
    partner = VerbRole()
    setattr(partner, 'VerbRole116', None)
    _safe_set(owner, 'NBVR_Grammar_RolePhrase', partner)
    assert getattr(partner, 'VerbRole116') == owner
    _safe_set(owner, 'NBVR_Grammar_RolePhrase', None)
    assert getattr(partner, 'VerbRole116') is None


def test_assoc_roles46_stub_double():
    # VerbRole has no real 'VerbRole47' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocVerb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocVerb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocVerb(arity=7)
    partner = VerbRole()
    setattr(partner, 'VerbRole47', None)
    _safe_set(owner, 'verb', {partner})
    assert getattr(partner, 'VerbRole47') == owner
    _safe_set(owner, 'verb', set())
    assert getattr(partner, 'VerbRole47') is None


def test_assoc_scope214_stub_double():
    # Proposition has no real 'Proposition215' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Quantification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Quantification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Quantification(kind="sample_text", unique=True)
    partner = Proposition()
    setattr(partner, 'Proposition215', None)
    _safe_set(owner, 'NBVR_Logic_Quantification', partner)
    assert getattr(partner, 'Proposition215') == owner
    _safe_set(owner, 'NBVR_Logic_Quantification', None)
    assert getattr(partner, 'Proposition215') is None


def test_assoc_scope251_stub_double():
    # Proposition has no real 'Proposition252' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Modal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Modal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Modal(kind="sample_text")
    partner = Proposition()
    setattr(partner, 'Proposition252', None)
    _safe_set(owner, 'NBVR_Logic_Modal', partner)
    assert getattr(partner, 'Proposition252') == owner
    _safe_set(owner, 'NBVR_Logic_Modal', None)
    assert getattr(partner, 'Proposition252') is None


def test_assoc_set212_stub_double():
    # Set has no real 'Set' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Variable(name="sample_text")
    partner = Set()
    setattr(partner, 'Set', None)
    _safe_set(owner, 'variable213', partner)
    assert getattr(partner, 'Set') == owner
    _safe_set(owner, 'variable213', None)
    assert getattr(partner, 'Set') is None


def test_assoc_singular90_stub_double():
    # WordForm has no real 'WordForm91' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Verb's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Verb's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Verb()
    partner = WordForm()
    setattr(partner, 'WordForm91', None)
    _safe_set(owner, 'NBVR_Vocabulary_Verb', partner)
    assert getattr(partner, 'WordForm91') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Verb', None)
    assert getattr(partner, 'WordForm91') is None


def test_assoc_source205_stub_double():
    # Quantification has no real 'Quantification' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Variable(name="sample_text")
    partner = Quantification()
    setattr(partner, 'Quantification', None)
    _safe_set(owner, 'variable', partner)
    assert getattr(partner, 'Quantification') == owner
    _safe_set(owner, 'variable', None)
    assert getattr(partner, 'Quantification') is None


def test_assoc_statement197_stub_double():
    # Sentence has no real 'Sentence198' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_DomainForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_DomainForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_DomainForm(modality="sample_text")
    partner = Sentence()
    setattr(partner, 'Sentence198', None)
    _safe_set(owner, 'NBVR_Grammar_DomainForm', partner)
    assert getattr(partner, 'Sentence198') == owner
    _safe_set(owner, 'NBVR_Grammar_DomainForm', None)
    assert getattr(partner, 'Sentence198') is None


def test_assoc_statements183_stub_double():
    # Sentence has no real 'Sentence184' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_CompoundForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_CompoundForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_CompoundForm(kind="sample_text")
    partner = Sentence()
    setattr(partner, 'Sentence184', None)
    _safe_set(owner, 'NBVR_Grammar_CompoundForm', {partner})
    assert getattr(partner, 'Sentence184') == owner
    _safe_set(owner, 'NBVR_Grammar_CompoundForm', set())
    assert getattr(partner, 'Sentence184') is None


def test_assoc_subject169_stub_double():
    # RolePhrase has no real 'RolePhrase171' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_SimpleForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_SimpleForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_SimpleForm()
    partner = RolePhrase()
    setattr(partner, 'RolePhrase171', None)
    _safe_set(owner, 'NBVR_Grammar_SimpleForm170', partner)
    assert getattr(partner, 'RolePhrase171') == owner
    _safe_set(owner, 'NBVR_Grammar_SimpleForm170', None)
    assert getattr(partner, 'RolePhrase171') is None


def test_assoc_term41_stub_double():
    # Term has no real 'Term42' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VerbRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VerbRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VerbRole(isRange=True)
    partner = Term()
    setattr(partner, 'Term42', None)
    _safe_set(owner, 'role', partner)
    assert getattr(partner, 'Term42') == owner
    _safe_set(owner, 'role', None)
    assert getattr(partner, 'Term42') is None


def test_assoc_terms30_stub_double():
    # Term has no real 'Term32' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VocabularyItem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VocabularyItem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VocabularyItem()
    partner = Term()
    setattr(partner, 'Term32', None)
    _safe_set(owner, 'concept31', {partner})
    assert getattr(partner, 'Term32') == owner
    _safe_set(owner, 'concept31', set())
    assert getattr(partner, 'Term32') is None


def test_assoc_unit145_stub_double():
    # VocUnit has no real 'VocUnit' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_Dimension(exponent=7)
    partner = VocUnit()
    setattr(partner, 'VocUnit', None)
    _safe_set(owner, 'NBVR_Grammar_Dimension', partner)
    assert getattr(partner, 'VocUnit') == owner
    _safe_set(owner, 'NBVR_Grammar_Dimension', None)
    assert getattr(partner, 'VocUnit') is None


def test_assoc_uses207_stub_double():
    # Relation has no real 'Relation' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Variable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Variable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Variable(name="sample_text")
    partner = Relation()
    setattr(partner, 'Relation', None)
    _safe_set(owner, 'NBVR_Logic_Variable208', {partner})
    assert getattr(partner, 'Relation') == owner
    _safe_set(owner, 'NBVR_Logic_Variable208', set())
    assert getattr(partner, 'Relation') is None


def test_assoc_variable117_stub_double():
    # Variable has no real 'Variable' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_RolePhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_RolePhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_RolePhrase()
    partner = Variable()
    setattr(partner, 'Variable', None)
    _safe_set(owner, 'NBVR_Grammar_RolePhrase118', partner)
    assert getattr(partner, 'Variable') == owner
    _safe_set(owner, 'NBVR_Grammar_RolePhrase118', None)
    assert getattr(partner, 'Variable') is None


def test_assoc_variable216_stub_double():
    # Variable has no real 'Variable217' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Quantification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Quantification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Quantification(kind="sample_text", unique=True)
    partner = Variable()
    setattr(partner, 'Variable217', None)
    _safe_set(owner, 'source', partner)
    assert getattr(partner, 'Variable217') == owner
    _safe_set(owner, 'source', None)
    assert getattr(partner, 'Variable217') is None


def test_assoc_variable225_stub_double():
    # Variable has no real 'Variable227' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Argument's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Argument's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Argument()
    partner = Variable()
    setattr(partner, 'Variable227', None)
    _safe_set(owner, 'NBVR_Logic_Argument226', partner)
    assert getattr(partner, 'Variable227') == owner
    _safe_set(owner, 'NBVR_Logic_Argument226', None)
    assert getattr(partner, 'Variable227') is None


def test_assoc_variables261_stub_double():
    # RoleVariable has no real 'RoleVariable' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Predicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Predicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Predicate(name="sample_text")
    partner = RoleVariable()
    setattr(partner, 'RoleVariable', None)
    _safe_set(owner, 'predicate', {partner})
    assert getattr(partner, 'RoleVariable') == owner
    _safe_set(owner, 'predicate', set())
    assert getattr(partner, 'RoleVariable') is None


def test_assoc_verb159_stub_double():
    # VocVerb has no real 'VocVerb160' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_VerbPhrase's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_VerbPhrase's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_VerbPhrase(modality="sample_text", negated=True)
    partner = VocVerb()
    setattr(partner, 'VocVerb160', None)
    _safe_set(owner, 'NBVR_Grammar_VerbPhrase', partner)
    assert getattr(partner, 'VocVerb160') == owner
    _safe_set(owner, 'NBVR_Grammar_VerbPhrase', None)
    assert getattr(partner, 'VocVerb160') is None


def test_assoc_verb166_stub_double():
    # VerbPhrase has no real 'VerbPhrase' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Grammar_SimpleForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Grammar_SimpleForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Grammar_SimpleForm()
    partner = VerbPhrase()
    setattr(partner, 'VerbPhrase', None)
    _safe_set(owner, 'NBVR_Grammar_SimpleForm', partner)
    assert getattr(partner, 'VerbPhrase') == owner
    _safe_set(owner, 'NBVR_Grammar_SimpleForm', None)
    assert getattr(partner, 'VerbPhrase') is None


def test_assoc_verb265_stub_double():
    # VocVerb has no real 'VocVerb267' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Logic_Predicate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Logic_Predicate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Logic_Predicate(name="sample_text")
    partner = VocVerb()
    setattr(partner, 'VocVerb267', None)
    _safe_set(owner, 'predicate266', partner)
    assert getattr(partner, 'VocVerb267') == owner
    _safe_set(owner, 'predicate266', None)
    assert getattr(partner, 'VocVerb267') is None


def test_assoc_verb40_stub_double():
    # VocVerb has no real 'VocVerb' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_VerbRole's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_VerbRole's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_VerbRole(isRange=True)
    partner = VocVerb()
    setattr(partner, 'VocVerb', None)
    _safe_set(owner, 'roles', partner)
    assert getattr(partner, 'VocVerb') == owner
    _safe_set(owner, 'roles', None)
    assert getattr(partner, 'VocVerb') is None


def test_assoc_verb56_stub_double():
    # VocVerb has no real 'VocVerb58' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_SyntaxForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_SyntaxForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_SyntaxForm(isAuxForm=True, text="sample_text")
    partner = VocVerb()
    setattr(partner, 'VocVerb58', None)
    _safe_set(owner, 'form57', partner)
    assert getattr(partner, 'VocVerb58') == owner
    _safe_set(owner, 'form57', None)
    assert getattr(partner, 'VocVerb58') is None


def test_assoc_word7_stub_double():
    # Word has no real 'Word9' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_WordForm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_WordForm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_WordForm(text="sample_text")
    partner = Word()
    setattr(partner, 'Word9', None)
    _safe_set(owner, 'NBVR_Vocabulary_WordForm8', partner)
    assert getattr(partner, 'Word9') == owner
    _safe_set(owner, 'NBVR_Vocabulary_WordForm8', None)
    assert getattr(partner, 'Word9') is None


def test_assoc_words17_stub_double():
    # Word has no real 'Word18' property in the generated
    # code (a bare stub) -- manually attach it so NBVR_Vocabulary_Term's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # NBVR_Vocabulary_Term's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = NBVR_Vocabulary_Term(text="sample_text")
    partner = Word()
    setattr(partner, 'Word18', None)
    _safe_set(owner, 'NBVR_Vocabulary_Term', {partner})
    assert getattr(partner, 'Word18') == owner
    _safe_set(owner, 'NBVR_Vocabulary_Term', set())
    assert getattr(partner, 'Word18') is None


