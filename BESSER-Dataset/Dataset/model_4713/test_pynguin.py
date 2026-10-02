#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    Argument,
    Condition,
    Connective,
    Constant,
    Dimension,
    ElementKind,
    Enum,
    ExtentConstant,
    FormElement,
    FormElementKind,
    Formulation,
    FormulationForm,
    Grammar_ParseElement,
    GroupKind,
    Instance,
    InstanceKind,
    ItemElement,
    Keyword,
    KeywordKind,
    LocalName,
    Modality,
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
    PhraseType,
    Predicate,
    Proposition,
    PropositionKind,
    Qualifier,
    QualifierChain,
    Quantification,
    Quantifier,
    QuantifierKind,
    Quantity,
    QueryKind,
    QueryPhrase,
    Question,
    Relation,
    RoleElement,
    RolePhrase,
    RoleVariable,
    Sentence,
    SentenceType,
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
    VocItemKind,
    VocName,
    VocNoun,
    VocProperty,
    VocUnit,
    VocVerb,
    VocabularyItem,
    Vocabulary_FormulationForm,
    Word,
    WordForm,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_6 = python_code_.NBVR_Grammar_Sentence()
    var_6.getType()
    var_9 = python_code_.Modifier
    var_10 = python_code_.NBVR_Logic_Predicate(name=var_9, predicate266=var_9)
    assert isinstance(var_10, python_code_.NBVR_Logic_Predicate)
    var_18 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_18.isPrimitive()
    var_20 = python_code_.NBVR_Vocabulary_Word()
    var_20.isIs()


def test_1():
    var_11 = python_code_.NBVR_Grammar_Sentence()
    var_11.getType()
    var_14 = python_code_.Modifier
    var_15 = python_code_.NBVR_Logic_Predicate(name=var_14, predicate266=var_14)
    assert isinstance(var_15, python_code_.NBVR_Logic_Predicate)
    var_36 = "_NBVR_Logic_Quantification__NBVR_Logic_Quantification K_Why"
    var_37 = python_code_.NBVR_Logic_QuantityValue(factor=var_36, unit=True)
    assert isinstance(var_37, python_code_.NBVR_Logic_QuantityValue)
    var_41 = python_code_.NBVR_Vocabulary_FormulationForm()
    var_41.isStructured()
    python_code_.NBVR_Logic_Predicate(name=True)
    var_44 = python_code_.NBVR_Grammar_ParseElement()
    var_45 = python_code_.NBVR_Grammar_Qualifier(ParseElement204=var_44)
    assert isinstance(var_45, python_code_.NBVR_Grammar_Qualifier)
    var_45.isSimple()


def test_2():
    var_0 = python_code_.NBVR_Grammar_Sentence
    var_1 = python_code_.Word()
    var_2 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_1)
    assert isinstance(var_2, python_code_.NBVR_Vocabulary_Word)
    var_3 = python_code_.NBVR_Grammar_LocalName()
    var_4 = lambda *args, **kwargs: -2585
    var_5 = python_code_.NBVR_Vocabulary_Keyword(
        kind=[
            "_NBVR_Vocabulary_VerbRole__NBVR_Vocabulary_VerbRole_NBVR_Logic_Modal__NBVR_Logic_ModalAnaphor",
            False,
        ],
        Word9=var_0,
        Word=var_2,
        Word200=var_3,
        Word186=var_4,
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_Keyword)
    var_8 = '`ERj?[DR" d9$8B%t'
    var_9 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_8, NBVR_Grammar_ImplicationForm181=458.92
    )
    assert isinstance(var_9, python_code_.NBVR_Grammar_ImplicationForm)
    var_12 = python_code_.NBVR_Logic_Argument(
        NBVR_Logic_Argument=var_0,
        NBVR_Logic_Argument226=None,
        NBVR_Logic_Argument229=var_0,
        NBVR_Logic_Argument235=complex(-364.7269, -782.23933),
    )
    assert isinstance(var_12, python_code_.NBVR_Logic_Argument)


def test_3():
    var_6 = python_code_.NBVR_Grammar_Sentence()
    var_6.getType()
    var_9 = python_code_.Modifier
    var_10 = python_code_.NBVR_Logic_Predicate(name=var_9, predicate266=var_9)
    assert isinstance(var_10, python_code_.NBVR_Logic_Predicate)
    var_18 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_18.isPrimitive()
    var_20 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_18)
    assert isinstance(var_20, python_code_.NBVR_Vocabulary_Word)
    var_20.isIs()
    var_34 = '`ERj?[DR" d9$8B%t'
    var_35 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_34, NBVR_Grammar_ImplicationForm181=458.92
    )
    assert isinstance(var_35, python_code_.NBVR_Grammar_ImplicationForm)
    var_36 = python_code_.NBVR_Logic_Argument(
        NBVR_Logic_Argument=var_9,
        NBVR_Logic_Argument226=None,
        NBVR_Logic_Argument229=var_9,
        NBVR_Logic_Argument235=complex(-364.7269, -782.23933),
    )
    assert isinstance(var_36, python_code_.NBVR_Logic_Argument)
    var_38 = python_code_.Quantification()
    var_39 = python_code_.VocNoun()
    python_code_.NBVR_Logic_Variable(
        name={"IV`": True},
        variable=var_38,
        NBVR_Logic_Variable210=var_39,
        variable213={1022, 3436.41, -922.22},
    )
    var_41 = python_code_.NBVR_Logic_Argument(NBVR_Logic_Argument232=-383.57)
    assert isinstance(var_41, python_code_.NBVR_Logic_Argument)


def test_4():
    var_0 = python_code_.ParseElement()
    var_1 = python_code_.NBVR_Grammar_QualifierChain()
    var_2 = "Interrogative"
    var_3 = True
    python_code_.NBVR_Grammar_VerbPhrase(modality=var_2, negated=var_3)
    var_6 = python_code_.NBVR_Vocabulary_FormElement(kind=var_0)
    assert isinstance(var_6, python_code_.NBVR_Vocabulary_FormElement)
    var_7 = python_code_.NBVR_Vocabulary_VocVerb(
        arity=complex(-3672.870607, 956.5195), VocabularyItem110=var_1
    )
    assert isinstance(var_7, python_code_.NBVR_Vocabulary_VocVerb)


def test_5():
    python_code_.NBVR_Vocabulary_VocName()
    var_42 = "K_Which K_But SyntaxForm _NBVR_Logic_Relation__NBVR_Logic_Relation"
    var_43 = python_code_.NBVR_Logic_QuantityValue(
        factor=var_42, unit=[True, "Any", "hvwn(wbpYq&J{"]
    )
    assert isinstance(var_43, python_code_.NBVR_Logic_QuantityValue)
    var_44 = -949
    var_49 = python_code_.NBVR_Logic_Proposition(text="VocabularyItem29")
    assert isinstance(var_49, python_code_.NBVR_Logic_Proposition)
    python_code_.NBVR_Grammar_Instance()
    var_54 = python_code_.NBVR_Vocabulary_RoleElement(slot=var_44)
    assert isinstance(var_54, python_code_.NBVR_Vocabulary_RoleElement)


def test_6():
    var_0 = python_code_.Proposition()
    var_3 = python_code_.NBVR_Grammar_DomainForm(
        modality=b"\x07\xcfZ,\xf3X3j\x08\xc4B#w", Sentence=var_0
    )
    assert isinstance(var_3, python_code_.NBVR_Grammar_DomainForm)
    var_8 = python_code_.NBVR_Grammar_Intension()
    var_9 = "NBVR_Grammar_CompoundFormAntipreference"
    var_10 = python_code_.NBVR_Logic_Modal(
        kind=var_9, Proposition219=complex(-633.078, -1171.7913), Proposition247=-646
    )
    assert isinstance(var_10, python_code_.NBVR_Logic_Modal)
    var_11 = "s=h~\\Zy\\E"
    var_12 = python_code_.NBVR_Logic_Proposition(text=var_11, FormulationForm=var_8)
    assert isinstance(var_12, python_code_.NBVR_Logic_Proposition)
    var_13 = var_12.getType()
    var_14 = python_code_.NBVR_Logic_Argument
    var_15 = python_code_.NBVR_Logic_Implication()
    var_16 = python_code_.NBVR_Logic_Connection(
        kind={},
        NBVR_Logic_Connection=var_13,
        Proposition219=var_14,
        Proposition=var_14,
        Proposition250=var_15,
    )
    assert isinstance(var_16, python_code_.NBVR_Logic_Connection)
    var_18 = python_code_.VerbRole()
    var_19 = python_code_.NBVR_Vocabulary_RoleElement(
        slot=b"\xf8", NBVR_Vocabulary_RoleElement=var_18, FormElement=var_3
    )
    assert isinstance(var_19, python_code_.NBVR_Vocabulary_RoleElement)
    var_22 = python_code_.NBVR_Grammar_Instance()
    var_22.getKind()


def test_7():
    var_0 = python_code_.NBVR_Grammar_Dimension(exponent="i}2x]BdBA&6*Lz( 9")
    var_1 = python_code_.NBVR_Logic_Proposition(text=True, FormulationForm=var_0)
    assert isinstance(var_1, python_code_.NBVR_Logic_Proposition)
    var_1.getType()
    var_3 = python_code_.Word()
    var_4 = python_code_.Predicate
    var_5 = python_code_.NBVR_Vocabulary_SyntaxForm(
        text=var_4, isAuxForm=var_3, form57=var_0
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_SyntaxForm)
    var_8 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_3)
    assert isinstance(var_8, python_code_.NBVR_Vocabulary_Word)
    var_8.isNumber()
    var_38 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_38.isPrimitive()
    var_40 = python_code_.NBVR_Vocabulary_Word()
    var_40.isIs()


def test_8():
    var_0 = python_code_.NBVR_Grammar_Dimension(exponent="i}2x]BdBA&6*Lz( 9")
    var_1 = python_code_.NBVR_Logic_Proposition(text=True, FormulationForm=var_0)
    assert isinstance(var_1, python_code_.NBVR_Logic_Proposition)
    var_1.getType()
    var_3 = python_code_.Word()
    var_5 = python_code_.NBVR_Vocabulary_SyntaxForm(
        text='l/M|6s7+7|T" hYc', isAuxForm=False, form54=set()
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_SyntaxForm)
    python_code_.NBVR_Vocabulary_VocabularyItem()
    var_8 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_3)
    assert isinstance(var_8, python_code_.NBVR_Vocabulary_Word)
    var_40 = '`ERj?[DR" d9$8B%t'
    var_41 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_40, NBVR_Grammar_ImplicationForm181=458.92
    )
    assert isinstance(var_41, python_code_.NBVR_Grammar_ImplicationForm)


def test_9():
    var_2 = python_code_.Variable
    var_3 = python_code_.NBVR_Logic_ValueConstant(name=var_2)
    assert isinstance(var_3, python_code_.NBVR_Logic_ValueConstant)
    python_code_.NBVR_Vocabulary_VerbRole(isRange=-580.33)
    python_code_.NBVR_Vocabulary_FormulationForm()


def test_10():
    python_code_.NBVR_Vocabulary_VocName()
    var_2 = python_code_.Instance()
    var_3 = "dz}2"
    var_4 = python_code_.NBVR_Vocabulary_Formulation(text=var_3, language=var_2)
    var_4.isStructured()
    python_code_.NBVR_Vocabulary_FormulationForm()
    var_36 = python_code_.NBVR_Grammar_SimpleForm(
        NBVR_Grammar_SimpleForm170=None, Sentence=None, Sentence176=var_3
    )
    assert isinstance(var_36, python_code_.NBVR_Grammar_SimpleForm)
    var_36.getModality()


@pytest.mark.xfail(strict=True)
def test_11():
    var_0 = lambda *args, **kwargs: 4285
    python_code_.NBVR_Vocabulary_VocabularyItem(concept31=var_0)


@pytest.mark.xfail(strict=True)
def test_12():
    var_0 = python_code_.ExtentConstant()
    var_2 = python_code_.Relation
    var_3 = python_code_.NBVR_Logic_ValueConstant(name=var_2)
    assert isinstance(var_3, python_code_.NBVR_Logic_ValueConstant)
    python_code_.NBVR_Vocabulary_VerbRole(isRange=-580.33)
    var_5 = "K_Which K_But SyntaxForm _NBVR_Logic_Relation__NBVR_Logic_Relation"
    var_6 = python_code_.NBVR_Logic_QuantityValue(
        factor=var_5, unit=[True, "Any", "hvwn(wbpYq&J{"]
    )
    assert isinstance(var_6, python_code_.NBVR_Logic_QuantityValue)
    var_7 = -974
    var_8 = python_code_.NBVR_Grammar_Quantifier(kind=var_0, count=var_7)
    assert isinstance(var_8, python_code_.NBVR_Grammar_Quantifier)
    var_9 = python_code_.NBVR_Vocabulary_Name()
    var_13 = python_code_.NBVR_Vocabulary_Formulation(
        text=var_8, language="<y_VOlyJD?^lh\nOi \t["
    )
    var_14 = python_code_.NBVR_Logic_Proposition(
        text=var_9, FormulationForm=("SubjectRole",)
    )
    assert isinstance(var_14, python_code_.NBVR_Logic_Proposition)
    python_code_.NBVR_Grammar_Instance()
    var_20 = python_code_.NBVR_Vocabulary_RoleElement(slot=var_7)
    assert isinstance(var_20, python_code_.NBVR_Vocabulary_RoleElement)
    var_23 = python_code_.FormulationForm()
    var_24 = python_code_.NBVR_Logic_Negation()
    var_25 = python_code_.NBVR_Logic_Modal(
        kind={},
        NBVR_Logic_Modal=var_2,
        Proposition219=var_14,
        Proposition254=var_24,
        Proposition260=var_13,
        Proposition247=var_23,
    )
    assert isinstance(var_25, python_code_.NBVR_Logic_Modal)
    var_26 = python_code_.NBVR_Grammar_Sentence()
    var_26.getType()
    var_29 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_9)
    assert isinstance(var_29, python_code_.NBVR_Vocabulary_Word)
    var_30 = var_29.isKeyword()
    python_code_.NBVR_Vocabulary_VocabularyItem(
        concept=var_2, NBVR_Vocabulary_VocabularyItem=var_30
    )


def test_13():
    var_31 = python_code_.NBVR_Grammar_QualifierChain()
    var_36 = python_code_.NBVR_Vocabulary_VocVerb(
        arity=complex(-3672.870607, 956.5195), VocabularyItem110=var_31
    )
    assert isinstance(var_36, python_code_.NBVR_Vocabulary_VocVerb)


def test_14():
    var_7 = python_code_.NBVR_Grammar_Condition(otherwise=True)
    assert isinstance(var_7, python_code_.NBVR_Grammar_Condition)
    var_54 = python_code_.NBVR_Vocabulary_Dictionary()
    var_55 = "Q{PjM:JO%i5>57"
    var_56 = python_code_.NBVR_Vocabulary_Adjective()
    var_57 = python_code_.NBVR_Vocabulary_WordForm(
        text=var_55, NBVR_Vocabulary_WordForm8=var_56
    )
    var_58 = python_code_.NBVR_Vocabulary_Verb(Word108=var_54, Word9=var_57)
    assert isinstance(var_58, python_code_.NBVR_Vocabulary_Verb)
    var_59 = ""
    python_code_.NBVR_Grammar_VerbPhrase(modality=var_59, negated=var_7)


def test_15():
    var_1 = python_code_.Modifier()
    var_2 = python_code_.VocProperty()
    var_3 = python_code_.NBVR_Vocabulary_DateTime()
    python_code_.NBVR_Vocabulary_WordForm(
        text=var_2, NBVR_Vocabulary_WordForm8=var_3, NBVR_Vocabulary_WordForm=var_2
    )
    var_5 = python_code_.NBVR_Vocabulary_Terminology()
    var_6 = python_code_.NBVR_Vocabulary_VocName(
        VocabularyItem110=var_5, VocabularyItem=var_1, VocabularyItem21=var_3
    )
    assert isinstance(var_6, python_code_.NBVR_Vocabulary_VocName)
    var_7 = lambda *args, **kwargs: -2355
    var_8 = python_code_.WordForm()
    var_9 = python_code_.NBVR_Vocabulary_Word(
        NBVR_Vocabulary_Word=var_8, NBVR_Vocabulary_Word4=var_2
    )
    assert isinstance(var_9, python_code_.NBVR_Vocabulary_Word)
    var_10 = var_6.isUnit()
    var_11 = python_code_.NBVR_Vocabulary_Term(text={}, term23=var_10)
    var_12 = python_code_.NBVR_Vocabulary_Keyword(
        kind=var_7,
        Word=var_9,
        Word12="Sentence182-K_Why-K_Only-_NBVR_Logic_Variable__NBVR_Logic_Variable210",
        Word186=True,
        Word18=var_11,
    )
    assert isinstance(var_12, python_code_.NBVR_Vocabulary_Keyword)
    var_13 = python_code_.NBVR_Grammar_CompoundForm(
        kind=-255.81, Sentence198=None, Sentence125=var_7
    )
    assert isinstance(var_13, python_code_.NBVR_Grammar_CompoundForm)


def test_16():
    var_1 = python_code_.ModifiedTerm()
    var_3 = python_code_.SimpleQualifier()
    var_4 = lambda *args, **kwargs: True
    var_5 = "mz|;Ez\tv*J(-gm*~N"
    var_6 = python_code_.NBVR_Vocabulary_Formulation(
        text=var_5, language={-2884.95, "fBm_iX;lER$kM`CE", -914.93}
    )
    var_7 = python_code_.NBVR_Grammar_Condition(
        otherwise={}, condition=var_3, NBVR_Grammar_Condition=var_4, ParseElement=var_6
    )
    assert isinstance(var_7, python_code_.NBVR_Grammar_Condition)
    var_8 = python_code_.Sentence()
    var_9 = python_code_.NBVR_Grammar_Sentence(NBVR_Grammar_Sentence132=var_1)
    assert isinstance(var_9, python_code_.NBVR_Grammar_Sentence)
    var_10 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_5, Sentence133=var_4, Sentence=var_4
    )
    assert isinstance(var_10, python_code_.NBVR_Grammar_ImplicationForm)
    var_11 = python_code_.WordForm()
    var_12 = python_code_.NBVR_Vocabulary_Dictionary()
    var_13 = python_code_.NBVR_Vocabulary_WordForm(text=var_3)
    var_14 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb=-2049,
        NBVR_Vocabulary_Verb96=None,
        NBVR_Vocabulary_Verb99=var_11,
        NBVR_Vocabulary_Verb105=var_11,
        Word108=var_12,
        Word12=var_13,
    )
    assert isinstance(var_14, python_code_.NBVR_Vocabulary_Verb)
    var_15 = var_14.isPerfective(NBVR_wf=var_3)
    var_16 = False
    var_17 = python_code_.NBVR_Grammar_Condition(otherwise=var_16, condition=[])
    var_18 = python_code_.NBVR_Grammar_CompoundForm(
        kind=var_4,
        NBVR_Grammar_CompoundForm=var_15,
        Sentence=var_17,
        Sentence198=var_4,
        Sentence179=var_11,
    )
    assert isinstance(var_18, python_code_.NBVR_Grammar_CompoundForm)
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_4,
        NBVR_Grammar_ImplicationForm181=var_8,
        NBVR_Grammar_ImplicationForm178=var_1,
        Sentence133=var_9,
        Sentence179=var_4,
        Sentence176=var_10,
        Sentence184=var_5,
    )
    var_30 = python_code_.NBVR_Logic_Constant(kind=var_9)
    assert isinstance(var_30, python_code_.NBVR_Logic_Constant)


def test_17():
    var_23 = python_code_.NBVR_Vocabulary_Word()
    var_23.isIs()


def test_18():
    var_1 = python_code_.NBVR_Vocabulary_VocName()
    var_2 = python_code_.Instance()
    var_3 = "dz}2"
    var_4 = python_code_.NBVR_Vocabulary_Formulation(text=var_3, language=var_2)
    var_5 = var_4.isStructured()
    python_code_.NBVR_Vocabulary_FormulationForm()
    var_10 = python_code_.NBVR_Grammar_PartPhrase
    python_code_.NBVR_Logic_Argument(
        NBVR_Logic_Argument=var_5,
        NBVR_Logic_Argument229=var_1,
        NBVR_Logic_Argument235=var_10,
    )
    var_14 = python_code_.WordForm()
    var_15 = python_code_.NBVR_Grammar_LocalName()
    var_16 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb93=var_14, Word200=var_15
    )
    assert isinstance(var_16, python_code_.NBVR_Vocabulary_Verb)
    var_16.isProgressive(NBVR_wf=())


def test_19():
    var_6 = python_code_.NBVR_Grammar_Sentence()
    var_6.getType()
    var_9 = python_code_.Modifier
    var_10 = python_code_.NBVR_Logic_Predicate(name=var_9, predicate266=var_9)
    assert isinstance(var_10, python_code_.NBVR_Logic_Predicate)
    var_11 = python_code_.WordForm()
    var_12 = python_code_.NBVR_Grammar_LocalName()
    var_13 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb99=var_11, Word9=[True], Word200=var_12, Word18=()
    )
    assert isinstance(var_13, python_code_.NBVR_Vocabulary_Verb)
    var_13.isProgressive(NBVR_wf=complex(-397.88, -421.0))
    var_18 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_18.isPrimitive()
    var_20 = python_code_.NBVR_Vocabulary_Word()
    var_20.isIs()


def test_20():
    var_2 = "Interrogatve"
    var_11 = python_code_.NBVR_Logic_Modal(
        kind=var_2, Proposition219=complex(-633.078, -1171.7913), Proposition247=-646
    )
    assert isinstance(var_11, python_code_.NBVR_Logic_Modal)
    var_18 = python_code_.NBVR_Grammar_Instance()
    var_18.getKind()


def test_21():
    var_0 = python_code_.ExtentConstant()
    var_2 = python_code_.Relation
    var_3 = python_code_.NBVR_Logic_ValueConstant(name=var_2)
    assert isinstance(var_3, python_code_.NBVR_Logic_ValueConstant)
    python_code_.NBVR_Vocabulary_VerbRole(isRange=-580.33)
    var_5 = "K_Which K_But SyntaxForm _NBVR_Logic_Relation__NBVR_Logic_Relation"
    var_6 = python_code_.NBVR_Logic_QuantityValue(
        factor=var_5, unit=[True, "Any", "hvwn(wbpYq&J{"]
    )
    assert isinstance(var_6, python_code_.NBVR_Logic_QuantityValue)
    var_7 = -974
    var_8 = python_code_.NBVR_Grammar_Quantifier(kind=var_0, count=var_7)
    assert isinstance(var_8, python_code_.NBVR_Grammar_Quantifier)
    var_9 = python_code_.NBVR_Vocabulary_Name()
    var_13 = python_code_.NBVR_Vocabulary_Formulation(
        text=var_8, language="<y_VOlyJD?^lh\nOi \t["
    )
    var_14 = python_code_.NBVR_Logic_Proposition(
        text=var_9, FormulationForm=("SubjectRole",)
    )
    assert isinstance(var_14, python_code_.NBVR_Logic_Proposition)
    python_code_.NBVR_Grammar_Instance()
    var_20 = python_code_.NBVR_Vocabulary_RoleElement(slot=var_7)
    assert isinstance(var_20, python_code_.NBVR_Vocabulary_RoleElement)
    var_23 = python_code_.FormulationForm()
    var_24 = python_code_.NBVR_Logic_Negation()
    var_25 = python_code_.NBVR_Logic_Modal(
        kind={},
        NBVR_Logic_Modal=var_2,
        Proposition219=var_14,
        Proposition254=var_24,
        Proposition260=var_13,
        Proposition247=var_23,
    )
    assert isinstance(var_25, python_code_.NBVR_Logic_Modal)
    var_26 = python_code_.NBVR_Grammar_Sentence()
    var_26.getType()
    var_29 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_9)
    assert isinstance(var_29, python_code_.NBVR_Vocabulary_Word)
    var_29.isKeyword()


def test_22():
    var_49 = "Interrogative"
    var_50 = True
    python_code_.NBVR_Grammar_VerbPhrase(modality=var_49, negated=var_50)


def test_23():
    var_0 = python_code_.NBVR_Grammar_Sentence
    var_1 = python_code_.Word()
    var_2 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_1)
    assert isinstance(var_2, python_code_.NBVR_Vocabulary_Word)
    var_3 = python_code_.NBVR_Grammar_LocalName()
    var_4 = lambda *args, **kwargs: -2585
    var_5 = python_code_.NBVR_Vocabulary_Keyword(
        kind=[
            "_NBVR_Vocabulary_VerbRole__NBVR_Vocabulary_VerbRole_NBVR_Logic_Modal__NBVR_Logic_ModalAnaphor",
            False,
        ],
        Word9=var_0,
        Word=var_2,
        Word200=var_3,
        Word186=var_4,
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_Keyword)
    var_6 = "66UvJm~4eoWd`A"
    var_7 = python_code_.Sentence()
    var_8 = '`ERj?[DR" d9$8B%t'
    var_9 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_8, NBVR_Grammar_ImplicationForm181=458.92
    )
    assert isinstance(var_9, python_code_.NBVR_Grammar_ImplicationForm)
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=b"i3\xc3\x1cs\\\xfa:\xa5\xe8\xe1'\xf4\xf3\xc8",
        NBVR_Grammar_ImplicationForm=var_7,
        Sentence198=var_4,
        Sentence179=var_9,
        Sentence125=var_5,
        Sentence184=var_4,
    )
    var_11 = python_code_.NBVR_Grammar_DomainForm(
        modality=var_6, Sentence133=var_5, Sentence182=var_9, Sentence188=var_5
    )
    assert isinstance(var_11, python_code_.NBVR_Grammar_DomainForm)


def test_24():
    var_1 = python_code_.ModifiedTerm()
    var_2 = "Predicate52"
    var_3 = python_code_.SimpleQualifier()
    var_4 = lambda *args, **kwargs: True
    var_5 = "mz|BEz\tv*J(-gm*~N"
    var_6 = python_code_.NBVR_Vocabulary_Formulation(
        text="_NBVR_Vocabulary_Verb__NBVR_Vocabulary_Verb-K_Unless-_NBVR_Vocabulary_VocabularyItem__concept31-_NBVR_Logic_Argument__arguments",
        language=var_2,
        formulations=None,
    )
    var_7 = python_code_.NBVR_Grammar_Condition(
        otherwise={}, condition=var_3, NBVR_Grammar_Condition=var_4, ParseElement=var_6
    )
    assert isinstance(var_7, python_code_.NBVR_Grammar_Condition)
    var_8 = python_code_.Sentence()
    var_10 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_5, Sentence133=var_4, Sentence=var_4
    )
    assert isinstance(var_10, python_code_.NBVR_Grammar_ImplicationForm)
    var_16 = False
    python_code_.NBVR_Grammar_Condition(otherwise=var_16, condition=[])
    python_code_.NBVR_Grammar_ImplicationForm(
        kind="",
        NBVR_Grammar_ImplicationForm181=var_8,
        Sentence133=None,
        Sentence198=None,
        Sentence125=None,
    )
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_2,
        NBVR_Grammar_ImplicationForm178=var_1,
        Sentence=var_7,
        Sentence182=var_10,
        Sentence184=var_4,
    )


def test_25():
    var_0 = python_code_.NBVR_Grammar_Sentence
    var_1 = python_code_.Word()
    var_2 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_1)
    assert isinstance(var_2, python_code_.NBVR_Vocabulary_Word)
    var_13 = "RolePhrase191 NBVR_Grammar_RolePhrase VocProperty Exactly1"
    var_14 = "G\\TV(vE"
    var_15 = python_code_.NBVR_Grammar_DomainForm(
        modality=var_14, NBVR_Grammar_DomainForm=var_0, Sentence=var_0
    )
    assert isinstance(var_15, python_code_.NBVR_Grammar_DomainForm)
    var_16 = python_code_.NBVR_Grammar_ImplicationForm(kind=var_13, Sentence198=var_15)
    assert isinstance(var_16, python_code_.NBVR_Grammar_ImplicationForm)
    var_20 = "_NBVRLogic_Quantification__NBVR_Logic_Quantification K_Why"
    var_21 = python_code_.NBVR_Logic_QuantityValue(factor=var_20, unit=True)
    assert isinstance(var_21, python_code_.NBVR_Logic_QuantityValue)
    var_25 = python_code_.NBVR_Vocabulary_FormulationForm()
    var_25.isStructured()
    var_27 = python_code_.NBVR_Logic_Predicate(name=True)
    assert isinstance(var_27, python_code_.NBVR_Logic_Predicate)
    var_28 = python_code_.NBVR_Grammar_ParseElement()
    var_29 = python_code_.NBVR_Grammar_Qualifier(ParseElement204=var_28)
    assert isinstance(var_29, python_code_.NBVR_Grammar_Qualifier)
    var_29.isSimple()
    var_2.isNumber()


def test_26():
    var_2 = python_code_.VocProperty()
    var_7 = lambda *args, **kwargs: -2355
    var_8 = python_code_.WordForm()
    var_9 = python_code_.NBVR_Vocabulary_Word(
        NBVR_Vocabulary_Word=var_8, NBVR_Vocabulary_Word4=var_2
    )
    assert isinstance(var_9, python_code_.NBVR_Vocabulary_Word)
    var_13 = python_code_.NBVR_Grammar_CompoundForm(
        kind=-255.81, Sentence198=None, Sentence125=var_7
    )
    assert isinstance(var_13, python_code_.NBVR_Grammar_CompoundForm)


def test_27():
    var_1 = python_code_.NBVR_Grammar_CompoundForm
    var_2 = python_code_.NBVR_Grammar_Sentence(NBVR_Grammar_Sentence=var_1)
    assert isinstance(var_2, python_code_.NBVR_Grammar_Sentence)
    var_4 = True
    var_5 = python_code_.NBVR_Grammar_Condition(otherwise=var_4)
    assert isinstance(var_5, python_code_.NBVR_Grammar_Condition)


def test_28():
    var_1 = python_code_.ModifiedTerm()
    var_3 = python_code_.SimpleQualifier()
    var_4 = lambda *args, **kwargs: True
    var_5 = "mz|;Ez\tv*J(-gm*~N"
    var_6 = python_code_.NBVR_Vocabulary_Formulation(
        text=var_5, language={-2884.95, "fBm_iX;lER$kM`CE", -914.93}
    )
    var_7 = python_code_.NBVR_Grammar_Condition(
        otherwise={}, condition=var_3, NBVR_Grammar_Condition=var_4, ParseElement=var_6
    )
    assert isinstance(var_7, python_code_.NBVR_Grammar_Condition)
    var_8 = python_code_.Sentence()
    var_9 = "f*>K-os\x0b{lXs^,"
    var_10 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_5, Sentence133=var_4, Sentence=var_4
    )
    assert isinstance(var_10, python_code_.NBVR_Grammar_ImplicationForm)
    var_16 = False
    python_code_.NBVR_Grammar_Condition(otherwise=var_16, condition=[])
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_4,
        NBVR_Grammar_ImplicationForm181=var_8,
        NBVR_Grammar_ImplicationForm178=var_1,
        Sentence133=var_9,
        Sentence179=var_4,
        Sentence176=var_10,
        Sentence184=var_5,
    )
    var_26 = var_6.isStructured()
    var_27 = python_code_.NBVR_Vocabulary_VocabularyItem(concept31=var_26)
    assert isinstance(var_27, python_code_.NBVR_Vocabulary_VocabularyItem)
    var_27.getKind()


def test_29():
    var_0 = python_code_.NBVR_Grammar_Dimension(exponent="i}2x]BdBA&6*Lz( 9")
    var_1 = python_code_.NBVR_Logic_Proposition(text=True, FormulationForm=var_0)
    assert isinstance(var_1, python_code_.NBVR_Logic_Proposition)
    var_1.getType()
    var_3 = python_code_.Word()
    var_5 = python_code_.NBVR_Vocabulary_SyntaxForm(
        text='l/M|6s7+7|T" hYc', isAuxForm=False, form54=set()
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_SyntaxForm)
    python_code_.NBVR_Vocabulary_VocabularyItem()
    var_8 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_3)
    assert isinstance(var_8, python_code_.NBVR_Vocabulary_Word)
    var_8.isNumber()
    var_40 = '`ERj?[DR" d9$8B%t'
    var_41 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_40, NBVR_Grammar_ImplicationForm181=458.92
    )
    assert isinstance(var_41, python_code_.NBVR_Grammar_ImplicationForm)


def test_30():
    var_2 = python_code_.Variable
    var_3 = python_code_.NBVR_Logic_ValueConstant(name=var_2)
    assert isinstance(var_3, python_code_.NBVR_Logic_ValueConstant)
    python_code_.NBVR_Vocabulary_VerbRole(isRange=-580.33)
    var_5 = "K_Which K_But SyntaxForm _NBVR_Logic_Relation__NBVR_Logic_Relation"
    var_6 = python_code_.NBVR_Logic_QuantityValue(
        factor=var_5, unit=[True, "Any", "hvwn(wbpYq&J{"]
    )
    assert isinstance(var_6, python_code_.NBVR_Logic_QuantityValue)
    var_7 = -949
    var_14 = python_code_.NBVR_Logic_Proposition(text="VocabularyItem29")
    assert isinstance(var_14, python_code_.NBVR_Logic_Proposition)
    python_code_.NBVR_Grammar_Instance()
    var_20 = python_code_.NBVR_Vocabulary_RoleElement(slot=var_7)
    assert isinstance(var_20, python_code_.NBVR_Vocabulary_RoleElement)
    var_50 = python_code_.NBVR_Grammar_SimpleNounPhrase()
    var_51 = python_code_.NBVR_Grammar_Nominalization()
    var_52 = python_code_.NBVR_Grammar_SimpleForm(
        NBVR_Grammar_SimpleForm170=var_50,
        NBVR_Grammar_SimpleForm173='uj5[INK|gEo="B',
        Sentence179=var_2,
        Sentence176=var_2,
        Sentence188=var_51,
    )
    assert isinstance(var_52, python_code_.NBVR_Grammar_SimpleForm)
    var_52.getModality()


def test_31():
    var_0 = python_code_.NBVR_Grammar_Dimension(exponent="i}2x]BdBA&6*Lz( 9")
    var_1 = python_code_.NBVR_Logic_Proposition(text=True, FormulationForm=var_0)
    assert isinstance(var_1, python_code_.NBVR_Logic_Proposition)
    var_1.getType()
    var_3 = python_code_.Word()
    var_4 = python_code_.NBVR_Vocabulary_VocProperty
    var_5 = python_code_.NBVR_Vocabulary_SyntaxForm(
        text=var_4, isAuxForm=var_3, form57=var_0
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_SyntaxForm)
    python_code_.NBVR_Vocabulary_VocabularyItem()
    var_8 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_3)
    assert isinstance(var_8, python_code_.NBVR_Vocabulary_Word)
    var_8.isNumber()
    var_11 = "RolePhrase191 NBVR_Grammar_RolePhrase VocProperty Exactly1"
    var_12 = "G\\TV(vE"
    var_13 = python_code_.NBVR_Grammar_DomainForm(
        modality=var_12, NBVR_Grammar_DomainForm=var_4, Sentence=var_4
    )
    assert isinstance(var_13, python_code_.NBVR_Grammar_DomainForm)
    var_14 = python_code_.NBVR_Grammar_ImplicationForm(kind=var_11, Sentence198=var_13)
    assert isinstance(var_14, python_code_.NBVR_Grammar_ImplicationForm)
    var_15 = python_code_.NBVR_Grammar_SimpleForm(Sentence198=var_5, Sentence176=var_14)
    assert isinstance(var_15, python_code_.NBVR_Grammar_SimpleForm)
    var_15.isNegated()
    var_20 = "_NBVR_Logic_Quantification__NBVR_Logic_Quantification K_Why"
    var_21 = python_code_.NBVR_Logic_QuantityValue(factor=var_20, unit=True)
    assert isinstance(var_21, python_code_.NBVR_Logic_QuantityValue)
    var_25 = python_code_.NBVR_Vocabulary_FormulationForm()
    var_25.isStructured()
    var_27 = python_code_.NBVR_Logic_Predicate(name=True)
    assert isinstance(var_27, python_code_.NBVR_Logic_Predicate)
    var_28 = python_code_.NBVR_Grammar_ParseElement()
    var_29 = python_code_.NBVR_Grammar_Qualifier(ParseElement204=var_28)
    assert isinstance(var_29, python_code_.NBVR_Grammar_Qualifier)
    var_29.isSimple()


def test_32():
    var_12 = python_code_.Modifier
    var_13 = python_code_.NBVR_Logic_Predicate(name=var_12, predicate266=var_12)
    assert isinstance(var_13, python_code_.NBVR_Logic_Predicate)
    var_14 = python_code_.WordForm()
    var_15 = python_code_.NBVR_Grammar_LocalName()
    var_16 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb99=var_14, Word9=[True], Word200=var_15, Word18=()
    )
    assert isinstance(var_16, python_code_.NBVR_Vocabulary_Verb)
    var_16.isProgressive(NBVR_wf=complex(-397.88, -421.0))
    var_18 = "K_This:_NBVR_Vocabulary_Word__NBVR_Vocabulary_Word2:_NBVR_Grammar_GroupPhrase__NBVR_Grammar_GroupPhrase:VocabularyItem21"
    var_19 = python_code_.NBVR_Grammar_Question(query=var_18)
    assert isinstance(var_19, python_code_.NBVR_Grammar_Question)
    var_21 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_21.isPrimitive()
    var_23 = python_code_.NBVR_Vocabulary_Word()
    var_23.isIs()
    var_29 = python_code_.NBVR_Vocabulary_VocName(
        VocabularyItem113=var_12, VocabularyItem36=var_14
    )
    assert isinstance(var_29, python_code_.NBVR_Vocabulary_VocName)


def test_33():
    var_11 = python_code_.NBVR_Grammar_Sentence()
    var_11.getType()
    var_14 = python_code_.Modifier
    var_15 = python_code_.NBVR_Logic_Predicate(name=var_14, predicate266=var_14)
    assert isinstance(var_15, python_code_.NBVR_Logic_Predicate)
    var_16 = python_code_.WordForm()
    var_21 = python_code_.NBVR_Vocabulary_VocabularyItem()
    var_21.isPrimitive()
    var_23 = python_code_.NBVR_Vocabulary_Word()
    var_23.isIs()
    var_28 = python_code_.NBVR_Logic_Constant(kind=var_11)
    assert isinstance(var_28, python_code_.NBVR_Logic_Constant)
    var_30 = python_code_.NBVR_Vocabulary_VocName(
        VocabularyItem113=var_14, VocabularyItem36=var_16
    )
    assert isinstance(var_30, python_code_.NBVR_Vocabulary_VocName)


def test_34():
    var_2 = python_code_.Relation
    var_3 = python_code_.NBVR_Logic_ValueConstant(name=var_2)
    assert isinstance(var_3, python_code_.NBVR_Logic_ValueConstant)
    python_code_.NBVR_Vocabulary_VerbRole(isRange=-580.33)
    var_5 = "K_Which K_But SyntaxForm _NBVR_Logic_Relation__NBVR_Logic_Relation"
    var_6 = python_code_.NBVR_Logic_QuantityValue(
        factor=var_5, unit=[True, "Any", "hvwn(wbpYq&J{"]
    )
    assert isinstance(var_6, python_code_.NBVR_Logic_QuantityValue)
    var_7 = -974
    var_9 = python_code_.NBVR_Vocabulary_Name()
    var_14 = python_code_.NBVR_Logic_Proposition(
        text=var_9, FormulationForm=("SubjectRole",)
    )
    assert isinstance(var_14, python_code_.NBVR_Logic_Proposition)
    var_15 = python_code_.NBVR_Grammar_Instance()
    var_20 = python_code_.NBVR_Vocabulary_RoleElement(slot=var_7)
    assert isinstance(var_20, python_code_.NBVR_Vocabulary_RoleElement)
    var_26 = python_code_.NBVR_Grammar_Sentence()
    var_26.getType()
    python_code_.NBVR_Vocabulary_VerbRole(
        isRange=var_15, NBVR_Vocabulary_VerbRole=var_2
    )


def test_35():
    python_code_.NBVR_Vocabulary_VocName()
    var_2 = python_code_.Instance()
    var_3 = "dz}2"
    var_4 = python_code_.NBVR_Vocabulary_Formulation(text=var_3, language=var_2)
    var_4.isStructured()
    var_46 = python_code_.NBVR_Grammar_Intension()
    var_47 = "NBVR_Grammar_CompoundFormAntipreference"
    var_48 = python_code_.NBVR_Logic_Modal(
        kind=var_47, Proposition219=complex(-633.078, -1171.7913), Proposition247=-646
    )
    assert isinstance(var_48, python_code_.NBVR_Logic_Modal)
    var_49 = "s=h~\\Zy\\E"
    var_50 = python_code_.NBVR_Logic_Proposition(text=var_49, FormulationForm=var_46)
    assert isinstance(var_50, python_code_.NBVR_Logic_Proposition)
    var_51 = var_50.getType()
    var_52 = python_code_.NBVR_Logic_Argument
    var_53 = python_code_.NBVR_Logic_Implication()
    var_54 = python_code_.NBVR_Logic_Connection(
        kind={},
        NBVR_Logic_Connection=var_51,
        Proposition219=var_52,
        Proposition=var_52,
        Proposition250=var_53,
    )
    assert isinstance(var_54, python_code_.NBVR_Logic_Connection)
    var_63 = python_code_.WordForm()
    var_64 = python_code_.WordForm()
    var_65 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb=var_63,
        NBVR_Vocabulary_Verb96=var_64,
        NBVR_Vocabulary_Verb99=var_51,
        Word18=complex(-856.0, -607.127),
    )
    assert isinstance(var_65, python_code_.NBVR_Vocabulary_Verb)
    var_65.isPast(NBVR_wf=complex(-2189.9116508, 2085.783))


def test_36():
    var_0 = python_code_.VocUnit()
    var_1 = python_code_.NBVR_Grammar_CompoundForm
    var_2 = python_code_.NBVR_Grammar_Sentence(NBVR_Grammar_Sentence=var_1)
    assert isinstance(var_2, python_code_.NBVR_Grammar_Sentence)
    var_3 = "J>q/B~1}ENe"
    var_4 = True
    var_5 = python_code_.NBVR_Grammar_Condition(otherwise=var_4)
    assert isinstance(var_5, python_code_.NBVR_Grammar_Condition)
    var_6 = ""
    var_7 = python_code_.Relation()
    var_8 = python_code_.NBVR_Logic_Argument(arguments=var_7)
    var_9 = var_8.hasNext()
    var_10 = lambda *args, **kwargs: 2968
    var_11 = python_code_.NBVR_Grammar_CompoundForm(
        kind=var_6,
        NBVR_Grammar_CompoundForm=var_9,
        Sentence179=var_10,
        Sentence125=var_7,
        Sentence188=True,
        Sentence184=b"$UH\x9e\xec\xf9\xdc1\x92\xc9ZO\x88",
    )
    assert isinstance(var_11, python_code_.NBVR_Grammar_CompoundForm)
    var_12 = python_code_.NBVR_Grammar_DomainForm(
        modality=b"\xf2\xba\xbd\xbbg:\xb9\xddl\xa9\x17K\xfe&\x97\xa5>h",
        Sentence133=var_2,
        Sentence179=(1,),
        Sentence184=var_11,
    )
    assert isinstance(var_12, python_code_.NBVR_Grammar_DomainForm)
    var_13 = python_code_.NBVR_Grammar_SimpleQualifier()
    var_14 = python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_3,
        NBVR_Grammar_ImplicationForm=var_12,
        Sentence198=var_12,
        Sentence125=var_13,
    )
    assert isinstance(var_14, python_code_.NBVR_Grammar_ImplicationForm)
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_3, Sentence133=var_2, Sentence179=var_14, Sentence184=var_11
    )
    python_code_.NBVR_Grammar_ImplicationForm(
        kind=var_6,
        NBVR_Grammar_ImplicationForm=var_11,
        NBVR_Grammar_ImplicationForm178=var_8,
        Sentence133=var_2,
        Sentence179=set(),
        Sentence176=var_14,
        Sentence182=var_5,
        Sentence188=var_0,
        Sentence184=var_11,
    )


def test_37():
    var_1 = python_code_.Word()
    var_2 = python_code_.NBVR_Vocabulary_Word(NBVR_Vocabulary_Word4=var_1)
    assert isinstance(var_2, python_code_.NBVR_Vocabulary_Word)
    var_3 = python_code_.NBVR_Grammar_LocalName()
    var_5 = python_code_.NBVR_Vocabulary_Verb(
        NBVR_Vocabulary_Verb102={
            "\x0b\tV?K4": 3034,
            "AdjectiveConcept": "RoleNoun",
            "_tt<-)}F": False,
        },
        Word9="",
        Word200=var_3,
        Word12=None,
        Word186=var_2,
    )
    assert isinstance(var_5, python_code_.NBVR_Vocabulary_Verb)
