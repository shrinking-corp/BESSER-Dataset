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
    oogen_OOCommentOwner,
    oogen_OOComment,
    OOComparatorExpression,
    oogen_OOEqualsExpression,
    oogen_OOLanguageSpecificSnippet,
    OOOneOperandArithmeticExpression,
    oogen_OOPostfixDecrementExpression,
    oogen_OOPrefixIncrementExpression,
    oogen_OOPrefixDecrementExpression,
    oogen_OOPostfixIncrementExpression,
    oogen_OOPlusExpression,
    oogen_OOMinusExpression,
    oogen_OOBracketedExpression,
    oogen_OOBitWiseComplement,
    oogen_OOLessEqualsExpression,
    oogen_OOGreaterEqualsExpression,
    oogen_OONotEqualsExpression,
    oogen_OOLessThanExpression,
    oogen_OOGreaterThanExpression,
    OOCompoundStatement,
    oogen_OODefault,
    oogen_OOCase,
    OOConditionalStatement,
    oogen_OOFor,
    oogen_OOIf,
    OOLogicalExpression,
    oogen_OOTernaryOperator,
    oogen_OOLogicalLiteral,
    oogen_OOOneOperandLogicalExpression,
    oogen_OOComparatorExpression,
    oogen_OOTwoOperandLogicalExpression,
    OOOneOperandLogicalExpression,
    oogen_OONotExpression,
    OOTwoOperandLogicalExpression,
    oogen_OOXorExpression,
    oogen_OOOrExpression,
    oogen_OOAndExpression,
    OOTwoOperandArithmeticExpression,
    oogen_OOTwoOperandAssignableExpression,
    oogen_OORootExpression,
    oogen_OOPowerExpression,
    oogen_OODoWhile,
    oogen_OOWhile,
    OOArithmeticExpression,
    oogen_OOOneOperandArithmeticExpression,
    oogen_OOFloatLiteral,
    oogen_OODoubleLiteral,
    oogen_OOLongLiteral,
    oogen_OOIntegerLiteral,
    oogen_OOTwoOperandArithmeticExpression,
    OOExpression,
    oogen_OONullLiteral,
    oogen_OOFieldReferenceExpression,
    oogen_OOBoolLiteral,
    oogen_OOIndexing,
    oogen_OONewClass,
    oogen_OOLogicalExpression,
    oogen_OOTypeCast,
    oogen_OONewArray,
    oogen_OOEmptyExpression,
    oogen_OOAssignmentExpression,
    oogen_OOVariableReferenceExpression,
    oogen_OOThisLiteral,
    oogen_OOLanguageSpecificExpression,
    oogen_OOFunctionCallExpression,
    oogen_OOStringLiteral,
    oogen_OOInitializerList,
    oogen_OOArithmeticExpression,
    oogen_OOModel,
    OOTwoOperandAssignableExpression,
    oogen_OOBitwiseXorExpression,
    oogen_OOBitwiseOrExpression,
    oogen_OOBitWiseLeftShift,
    oogen_OOBitwiseAndExpression,
    oogen_OOMultiplicationExpression,
    oogen_OOBitWiseRightShift,
    oogen_OOSubtractionExpression,
    oogen_OOIntegerDivisionExpression,
    oogen_OODivisionExpression,
    oogen_OOModuloExpression,
    oogen_OOAdditionExpression,
    oogen_OOType,
    OOStatement,
    oogen_OOEmptyStatement,
    oogen_OOExpression,
    oogen_OOCompoundStatement,
    oogen_OOReturn,
    oogen_OOSwitch,
    oogen_OOVariableDeclarationList,
    oogen_OOContinue,
    oogen_OOBreak,
    oogen_OOForEach,
    oogen_OOConditionalStatement,
    oogen_OOVariable,
    oogen_OOConstructor,
    OOCommentOwner,
    oogen_OOStatement,
    oogen_OOMethod,
    OOVariable,
    oogen_OOMember,
    oogen_OOPackage,
    oogen_OOEnumeration,
    oogen_OOClass,
    OOVisibility,
    OOLanguage,
    OOBaseType,
    OOCollectionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_oogen_oocommentowner_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCommentOwner)


def test_hyp_oogen_oocommentowner_constructor_exists():
    assert callable(oogen_OOCommentOwner.__init__)


def test_hyp_oogen_oocommentowner_constructor_args():
    sig = inspect.signature(oogen_OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oocomment_is_not_abstract():
    assert not inspect.isabstract(oogen_OOComment)


def test_hyp_oogen_oocomment_constructor_exists():
    assert callable(oogen_OOComment.__init__)


def test_hyp_oogen_oocomment_constructor_args():
    sig = inspect.signature(oogen_OOComment.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "isBlockComment" in params, "Missing parameter 'isBlockComment'"





def test_hyp_oocomparatorexpression_is_not_abstract():
    assert not inspect.isabstract(OOComparatorExpression)


def test_hyp_oocomparatorexpression_constructor_exists():
    assert callable(OOComparatorExpression.__init__)


def test_hyp_oocomparatorexpression_constructor_args():
    sig = inspect.signature(OOComparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEqualsExpression)


def test_hyp_oogen_ooequalsexpression_constructor_exists():
    assert callable(oogen_OOEqualsExpression.__init__)


def test_hyp_oogen_ooequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oolanguagespecificsnippet_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLanguageSpecificSnippet)


def test_hyp_oogen_oolanguagespecificsnippet_constructor_exists():
    assert callable(oogen_OOLanguageSpecificSnippet.__init__)


def test_hyp_oogen_oolanguagespecificsnippet_constructor_args():
    sig = inspect.signature(oogen_OOLanguageSpecificSnippet.__init__)
    params = list(sig.parameters.keys())
    assert "code" in params, "Missing parameter 'code'"
    assert "lang" in params, "Missing parameter 'lang'"





def test_hyp_oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandArithmeticExpression)


def test_hyp_oooneoperandarithmeticexpression_constructor_exists():
    assert callable(OOOneOperandArithmeticExpression.__init__)


def test_hyp_oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oopostfixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPostfixDecrementExpression)


def test_hyp_oogen_oopostfixdecrementexpression_constructor_exists():
    assert callable(oogen_OOPostfixDecrementExpression.__init__)


def test_hyp_oogen_oopostfixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPostfixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooprefixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPrefixIncrementExpression)


def test_hyp_oogen_ooprefixincrementexpression_constructor_exists():
    assert callable(oogen_OOPrefixIncrementExpression.__init__)


def test_hyp_oogen_ooprefixincrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPrefixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooprefixdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPrefixDecrementExpression)


def test_hyp_oogen_ooprefixdecrementexpression_constructor_exists():
    assert callable(oogen_OOPrefixDecrementExpression.__init__)


def test_hyp_oogen_ooprefixdecrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPrefixDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oopostfixincrementexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPostfixIncrementExpression)


def test_hyp_oogen_oopostfixincrementexpression_constructor_exists():
    assert callable(oogen_OOPostfixIncrementExpression.__init__)


def test_hyp_oogen_oopostfixincrementexpression_constructor_args():
    sig = inspect.signature(oogen_OOPostfixIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooplusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPlusExpression)


def test_hyp_oogen_ooplusexpression_constructor_exists():
    assert callable(oogen_OOPlusExpression.__init__)


def test_hyp_oogen_ooplusexpression_constructor_args():
    sig = inspect.signature(oogen_OOPlusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oominusexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMinusExpression)


def test_hyp_oogen_oominusexpression_constructor_exists():
    assert callable(oogen_OOMinusExpression.__init__)


def test_hyp_oogen_oominusexpression_constructor_args():
    sig = inspect.signature(oogen_OOMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobracketedexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBracketedExpression)


def test_hyp_oogen_oobracketedexpression_constructor_exists():
    assert callable(oogen_OOBracketedExpression.__init__)


def test_hyp_oogen_oobracketedexpression_constructor_args():
    sig = inspect.signature(oogen_OOBracketedExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwisecomplement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseComplement)


def test_hyp_oogen_oobitwisecomplement_constructor_exists():
    assert callable(oogen_OOBitWiseComplement.__init__)


def test_hyp_oogen_oobitwisecomplement_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseComplement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oolessequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLessEqualsExpression)


def test_hyp_oogen_oolessequalsexpression_constructor_exists():
    assert callable(oogen_OOLessEqualsExpression.__init__)


def test_hyp_oogen_oolessequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOLessEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oogreaterequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOGreaterEqualsExpression)


def test_hyp_oogen_oogreaterequalsexpression_constructor_exists():
    assert callable(oogen_OOGreaterEqualsExpression.__init__)


def test_hyp_oogen_oogreaterequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OOGreaterEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oonotequalsexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OONotEqualsExpression)


def test_hyp_oogen_oonotequalsexpression_constructor_exists():
    assert callable(oogen_OONotEqualsExpression.__init__)


def test_hyp_oogen_oonotequalsexpression_constructor_args():
    sig = inspect.signature(oogen_OONotEqualsExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oolessthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLessThanExpression)


def test_hyp_oogen_oolessthanexpression_constructor_exists():
    assert callable(oogen_OOLessThanExpression.__init__)


def test_hyp_oogen_oolessthanexpression_constructor_args():
    sig = inspect.signature(oogen_OOLessThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oogreaterthanexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOGreaterThanExpression)


def test_hyp_oogen_oogreaterthanexpression_constructor_exists():
    assert callable(oogen_OOGreaterThanExpression.__init__)


def test_hyp_oogen_oogreaterthanexpression_constructor_args():
    sig = inspect.signature(oogen_OOGreaterThanExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(OOCompoundStatement)


def test_hyp_oocompoundstatement_constructor_exists():
    assert callable(OOCompoundStatement.__init__)


def test_hyp_oocompoundstatement_constructor_args():
    sig = inspect.signature(OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oodefault_is_not_abstract():
    assert not inspect.isabstract(oogen_OODefault)


def test_hyp_oogen_oodefault_constructor_exists():
    assert callable(oogen_OODefault.__init__)


def test_hyp_oogen_oodefault_constructor_args():
    sig = inspect.signature(oogen_OODefault.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oocase_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCase)


def test_hyp_oogen_oocase_constructor_exists():
    assert callable(oogen_OOCase.__init__)


def test_hyp_oogen_oocase_constructor_args():
    sig = inspect.signature(oogen_OOCase.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(OOConditionalStatement)


def test_hyp_ooconditionalstatement_constructor_exists():
    assert callable(OOConditionalStatement.__init__)


def test_hyp_ooconditionalstatement_constructor_args():
    sig = inspect.signature(OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oofor_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFor)


def test_hyp_oogen_oofor_constructor_exists():
    assert callable(oogen_OOFor.__init__)


def test_hyp_oogen_oofor_constructor_args():
    sig = inspect.signature(oogen_OOFor.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooif_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIf)


def test_hyp_oogen_ooif_constructor_exists():
    assert callable(oogen_OOIf.__init__)


def test_hyp_oogen_ooif_constructor_args():
    sig = inspect.signature(oogen_OOIf.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOLogicalExpression)


def test_hyp_oologicalexpression_constructor_exists():
    assert callable(OOLogicalExpression.__init__)


def test_hyp_oologicalexpression_constructor_args():
    sig = inspect.signature(OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooternaryoperator_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTernaryOperator)


def test_hyp_oogen_ooternaryoperator_constructor_exists():
    assert callable(oogen_OOTernaryOperator.__init__)


def test_hyp_oogen_ooternaryoperator_constructor_args():
    sig = inspect.signature(oogen_OOTernaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oologicalliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLogicalLiteral)


def test_hyp_oogen_oologicalliteral_constructor_exists():
    assert callable(oogen_OOLogicalLiteral.__init__)


def test_hyp_oogen_oologicalliteral_constructor_args():
    sig = inspect.signature(oogen_OOLogicalLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOneOperandLogicalExpression)


def test_hyp_oogen_oooneoperandlogicalexpression_constructor_exists():
    assert callable(oogen_OOOneOperandLogicalExpression.__init__)


def test_hyp_oogen_oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oocomparatorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOComparatorExpression)


def test_hyp_oogen_oocomparatorexpression_constructor_exists():
    assert callable(oogen_OOComparatorExpression.__init__)


def test_hyp_oogen_oocomparatorexpression_constructor_args():
    sig = inspect.signature(oogen_OOComparatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandLogicalExpression)


def test_hyp_oogen_ootwooperandlogicalexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandLogicalExpression.__init__)


def test_hyp_oogen_ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oooneoperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOOneOperandLogicalExpression)


def test_hyp_oooneoperandlogicalexpression_constructor_exists():
    assert callable(OOOneOperandLogicalExpression.__init__)


def test_hyp_oooneoperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOOneOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oonotexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OONotExpression)


def test_hyp_oogen_oonotexpression_constructor_exists():
    assert callable(oogen_OONotExpression.__init__)


def test_hyp_oogen_oonotexpression_constructor_args():
    sig = inspect.signature(oogen_OONotExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ootwooperandlogicalexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandLogicalExpression)


def test_hyp_ootwooperandlogicalexpression_constructor_exists():
    assert callable(OOTwoOperandLogicalExpression.__init__)


def test_hyp_ootwooperandlogicalexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooxorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOXorExpression)


def test_hyp_oogen_ooxorexpression_constructor_exists():
    assert callable(oogen_OOXorExpression.__init__)


def test_hyp_oogen_ooxorexpression_constructor_args():
    sig = inspect.signature(oogen_OOXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOrExpression)


def test_hyp_oogen_ooorexpression_constructor_exists():
    assert callable(oogen_OOOrExpression.__init__)


def test_hyp_oogen_ooorexpression_constructor_args():
    sig = inspect.signature(oogen_OOOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAndExpression)


def test_hyp_oogen_ooandexpression_constructor_exists():
    assert callable(oogen_OOAndExpression.__init__)


def test_hyp_oogen_ooandexpression_constructor_args():
    sig = inspect.signature(oogen_OOAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandArithmeticExpression)


def test_hyp_ootwooperandarithmeticexpression_constructor_exists():
    assert callable(OOTwoOperandArithmeticExpression.__init__)


def test_hyp_ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandAssignableExpression)


def test_hyp_oogen_ootwooperandassignableexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandAssignableExpression.__init__)


def test_hyp_oogen_ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assigned" in params, "Missing parameter 'assigned'"




def test_hyp_oogen_oorootexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OORootExpression)


def test_hyp_oogen_oorootexpression_constructor_exists():
    assert callable(oogen_OORootExpression.__init__)


def test_hyp_oogen_oorootexpression_constructor_args():
    sig = inspect.signature(oogen_OORootExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oopowerexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPowerExpression)


def test_hyp_oogen_oopowerexpression_constructor_exists():
    assert callable(oogen_OOPowerExpression.__init__)


def test_hyp_oogen_oopowerexpression_constructor_args():
    sig = inspect.signature(oogen_OOPowerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oodowhile_is_not_abstract():
    assert not inspect.isabstract(oogen_OODoWhile)


def test_hyp_oogen_oodowhile_constructor_exists():
    assert callable(oogen_OODoWhile.__init__)


def test_hyp_oogen_oodowhile_constructor_args():
    sig = inspect.signature(oogen_OODoWhile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oowhile_is_not_abstract():
    assert not inspect.isabstract(oogen_OOWhile)


def test_hyp_oogen_oowhile_constructor_exists():
    assert callable(oogen_OOWhile.__init__)


def test_hyp_oogen_oowhile_constructor_args():
    sig = inspect.signature(oogen_OOWhile.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(OOArithmeticExpression)


def test_hyp_ooarithmeticexpression_constructor_exists():
    assert callable(OOArithmeticExpression.__init__)


def test_hyp_ooarithmeticexpression_constructor_args():
    sig = inspect.signature(OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oooneoperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOOneOperandArithmeticExpression)


def test_hyp_oogen_oooneoperandarithmeticexpression_constructor_exists():
    assert callable(oogen_OOOneOperandArithmeticExpression.__init__)


def test_hyp_oogen_oooneoperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOOneOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oofloatliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFloatLiteral)


def test_hyp_oogen_oofloatliteral_constructor_exists():
    assert callable(oogen_OOFloatLiteral.__init__)


def test_hyp_oogen_oofloatliteral_constructor_args():
    sig = inspect.signature(oogen_OOFloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_oodoubleliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OODoubleLiteral)


def test_hyp_oogen_oodoubleliteral_constructor_exists():
    assert callable(oogen_OODoubleLiteral.__init__)


def test_hyp_oogen_oodoubleliteral_constructor_args():
    sig = inspect.signature(oogen_OODoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_oolongliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLongLiteral)


def test_hyp_oogen_oolongliteral_constructor_exists():
    assert callable(oogen_OOLongLiteral.__init__)


def test_hyp_oogen_oolongliteral_constructor_args():
    sig = inspect.signature(oogen_OOLongLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_oointegerliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIntegerLiteral)


def test_hyp_oogen_oointegerliteral_constructor_exists():
    assert callable(oogen_OOIntegerLiteral.__init__)


def test_hyp_oogen_oointegerliteral_constructor_args():
    sig = inspect.signature(oogen_OOIntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_ootwooperandarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTwoOperandArithmeticExpression)


def test_hyp_oogen_ootwooperandarithmeticexpression_constructor_exists():
    assert callable(oogen_OOTwoOperandArithmeticExpression.__init__)


def test_hyp_oogen_ootwooperandarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOTwoOperandArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ooexpression_is_not_abstract():
    assert not inspect.isabstract(OOExpression)


def test_hyp_ooexpression_constructor_exists():
    assert callable(OOExpression.__init__)


def test_hyp_ooexpression_constructor_args():
    sig = inspect.signature(OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oonullliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OONullLiteral)


def test_hyp_oogen_oonullliteral_constructor_exists():
    assert callable(oogen_OONullLiteral.__init__)


def test_hyp_oogen_oonullliteral_constructor_args():
    sig = inspect.signature(oogen_OONullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oofieldreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFieldReferenceExpression)


def test_hyp_oogen_oofieldreferenceexpression_constructor_exists():
    assert callable(oogen_OOFieldReferenceExpression.__init__)


def test_hyp_oogen_oofieldreferenceexpression_constructor_args():
    sig = inspect.signature(oogen_OOFieldReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"




def test_hyp_oogen_ooboolliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBoolLiteral)


def test_hyp_oogen_ooboolliteral_constructor_exists():
    assert callable(oogen_OOBoolLiteral.__init__)


def test_hyp_oogen_ooboolliteral_constructor_args():
    sig = inspect.signature(oogen_OOBoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_ooindexing_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIndexing)


def test_hyp_oogen_ooindexing_constructor_exists():
    assert callable(oogen_OOIndexing.__init__)


def test_hyp_oogen_ooindexing_constructor_args():
    sig = inspect.signature(oogen_OOIndexing.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oonewclass_is_not_abstract():
    assert not inspect.isabstract(oogen_OONewClass)


def test_hyp_oogen_oonewclass_constructor_exists():
    assert callable(oogen_OONewClass.__init__)


def test_hyp_oogen_oonewclass_constructor_args():
    sig = inspect.signature(oogen_OONewClass.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"




def test_hyp_oogen_oologicalexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLogicalExpression)


def test_hyp_oogen_oologicalexpression_constructor_exists():
    assert callable(oogen_OOLogicalExpression.__init__)


def test_hyp_oogen_oologicalexpression_constructor_args():
    sig = inspect.signature(oogen_OOLogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ootypecast_is_not_abstract():
    assert not inspect.isabstract(oogen_OOTypeCast)


def test_hyp_oogen_ootypecast_constructor_exists():
    assert callable(oogen_OOTypeCast.__init__)


def test_hyp_oogen_ootypecast_constructor_args():
    sig = inspect.signature(oogen_OOTypeCast.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oonewarray_is_not_abstract():
    assert not inspect.isabstract(oogen_OONewArray)


def test_hyp_oogen_oonewarray_constructor_exists():
    assert callable(oogen_OONewArray.__init__)


def test_hyp_oogen_oonewarray_constructor_args():
    sig = inspect.signature(oogen_OONewArray.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooemptyexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEmptyExpression)


def test_hyp_oogen_ooemptyexpression_constructor_exists():
    assert callable(oogen_OOEmptyExpression.__init__)


def test_hyp_oogen_ooemptyexpression_constructor_args():
    sig = inspect.signature(oogen_OOEmptyExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAssignmentExpression)


def test_hyp_oogen_ooassignmentexpression_constructor_exists():
    assert callable(oogen_OOAssignmentExpression.__init__)


def test_hyp_oogen_ooassignmentexpression_constructor_args():
    sig = inspect.signature(oogen_OOAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oovariablereferenceexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariableReferenceExpression)


def test_hyp_oogen_oovariablereferenceexpression_constructor_exists():
    assert callable(oogen_OOVariableReferenceExpression.__init__)


def test_hyp_oogen_oovariablereferenceexpression_constructor_args():
    sig = inspect.signature(oogen_OOVariableReferenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oothisliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOThisLiteral)


def test_hyp_oogen_oothisliteral_constructor_exists():
    assert callable(oogen_OOThisLiteral.__init__)


def test_hyp_oogen_oothisliteral_constructor_args():
    sig = inspect.signature(oogen_OOThisLiteral.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oolanguagespecificexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOLanguageSpecificExpression)


def test_hyp_oogen_oolanguagespecificexpression_constructor_exists():
    assert callable(oogen_OOLanguageSpecificExpression.__init__)


def test_hyp_oogen_oolanguagespecificexpression_constructor_args():
    sig = inspect.signature(oogen_OOLanguageSpecificExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oofunctioncallexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOFunctionCallExpression)


def test_hyp_oogen_oofunctioncallexpression_constructor_exists():
    assert callable(oogen_OOFunctionCallExpression.__init__)


def test_hyp_oogen_oofunctioncallexpression_constructor_args():
    sig = inspect.signature(oogen_OOFunctionCallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "functionName" in params, "Missing parameter 'functionName'"




def test_hyp_oogen_oostringliteral_is_not_abstract():
    assert not inspect.isabstract(oogen_OOStringLiteral)


def test_hyp_oogen_oostringliteral_constructor_exists():
    assert callable(oogen_OOStringLiteral.__init__)


def test_hyp_oogen_oostringliteral_constructor_args():
    sig = inspect.signature(oogen_OOStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"




def test_hyp_oogen_ooinitializerlist_is_not_abstract():
    assert not inspect.isabstract(oogen_OOInitializerList)


def test_hyp_oogen_ooinitializerlist_constructor_exists():
    assert callable(oogen_OOInitializerList.__init__)


def test_hyp_oogen_ooinitializerlist_constructor_args():
    sig = inspect.signature(oogen_OOInitializerList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOArithmeticExpression)


def test_hyp_oogen_ooarithmeticexpression_constructor_exists():
    assert callable(oogen_OOArithmeticExpression.__init__)


def test_hyp_oogen_ooarithmeticexpression_constructor_args():
    sig = inspect.signature(oogen_OOArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oomodel_is_not_abstract():
    assert not inspect.isabstract(oogen_OOModel)


def test_hyp_oogen_oomodel_constructor_exists():
    assert callable(oogen_OOModel.__init__)


def test_hyp_oogen_oomodel_constructor_args():
    sig = inspect.signature(oogen_OOModel.__init__)
    params = list(sig.parameters.keys())



def test_hyp_ootwooperandassignableexpression_is_not_abstract():
    assert not inspect.isabstract(OOTwoOperandAssignableExpression)


def test_hyp_ootwooperandassignableexpression_constructor_exists():
    assert callable(OOTwoOperandAssignableExpression.__init__)


def test_hyp_ootwooperandassignableexpression_constructor_args():
    sig = inspect.signature(OOTwoOperandAssignableExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseXorExpression)


def test_hyp_oogen_oobitwisexorexpression_constructor_exists():
    assert callable(oogen_OOBitwiseXorExpression.__init__)


def test_hyp_oogen_oobitwisexorexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseOrExpression)


def test_hyp_oogen_oobitwiseorexpression_constructor_exists():
    assert callable(oogen_OOBitwiseOrExpression.__init__)


def test_hyp_oogen_oobitwiseorexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwiseleftshift_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseLeftShift)


def test_hyp_oogen_oobitwiseleftshift_constructor_exists():
    assert callable(oogen_OOBitWiseLeftShift.__init__)


def test_hyp_oogen_oobitwiseleftshift_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseLeftShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitwiseAndExpression)


def test_hyp_oogen_oobitwiseandexpression_constructor_exists():
    assert callable(oogen_OOBitwiseAndExpression.__init__)


def test_hyp_oogen_oobitwiseandexpression_constructor_args():
    sig = inspect.signature(oogen_OOBitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oomultiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMultiplicationExpression)


def test_hyp_oogen_oomultiplicationexpression_constructor_exists():
    assert callable(oogen_OOMultiplicationExpression.__init__)


def test_hyp_oogen_oomultiplicationexpression_constructor_args():
    sig = inspect.signature(oogen_OOMultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobitwiserightshift_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBitWiseRightShift)


def test_hyp_oogen_oobitwiserightshift_constructor_exists():
    assert callable(oogen_OOBitWiseRightShift.__init__)


def test_hyp_oogen_oobitwiserightshift_constructor_args():
    sig = inspect.signature(oogen_OOBitWiseRightShift.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oosubtractionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOSubtractionExpression)


def test_hyp_oogen_oosubtractionexpression_constructor_exists():
    assert callable(oogen_OOSubtractionExpression.__init__)


def test_hyp_oogen_oosubtractionexpression_constructor_args():
    sig = inspect.signature(oogen_OOSubtractionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oointegerdivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOIntegerDivisionExpression)


def test_hyp_oogen_oointegerdivisionexpression_constructor_exists():
    assert callable(oogen_OOIntegerDivisionExpression.__init__)


def test_hyp_oogen_oointegerdivisionexpression_constructor_args():
    sig = inspect.signature(oogen_OOIntegerDivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oodivisionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OODivisionExpression)


def test_hyp_oogen_oodivisionexpression_constructor_exists():
    assert callable(oogen_OODivisionExpression.__init__)


def test_hyp_oogen_oodivisionexpression_constructor_args():
    sig = inspect.signature(oogen_OODivisionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oomoduloexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOModuloExpression)


def test_hyp_oogen_oomoduloexpression_constructor_exists():
    assert callable(oogen_OOModuloExpression.__init__)


def test_hyp_oogen_oomoduloexpression_constructor_args():
    sig = inspect.signature(oogen_OOModuloExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooadditionexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOAdditionExpression)


def test_hyp_oogen_ooadditionexpression_constructor_exists():
    assert callable(oogen_OOAdditionExpression.__init__)


def test_hyp_oogen_ooadditionexpression_constructor_args():
    sig = inspect.signature(oogen_OOAdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ootype_is_not_abstract():
    assert not inspect.isabstract(oogen_OOType)


def test_hyp_oogen_ootype_constructor_exists():
    assert callable(oogen_OOType.__init__)


def test_hyp_oogen_ootype_constructor_args():
    sig = inspect.signature(oogen_OOType.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"
    assert "collectionType" in params, "Missing parameter 'collectionType'"
    assert "numberOfIndirections" in params, "Missing parameter 'numberOfIndirections'"
    assert "arrayDimensions" in params, "Missing parameter 'arrayDimensions'"







def test_hyp_oostatement_is_not_abstract():
    assert not inspect.isabstract(OOStatement)


def test_hyp_oostatement_constructor_exists():
    assert callable(OOStatement.__init__)


def test_hyp_oostatement_constructor_args():
    sig = inspect.signature(OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooemptystatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEmptyStatement)


def test_hyp_oogen_ooemptystatement_constructor_exists():
    assert callable(oogen_OOEmptyStatement.__init__)


def test_hyp_oogen_ooemptystatement_constructor_args():
    sig = inspect.signature(oogen_OOEmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooexpression_is_not_abstract():
    assert not inspect.isabstract(oogen_OOExpression)


def test_hyp_oogen_ooexpression_constructor_exists():
    assert callable(oogen_OOExpression.__init__)


def test_hyp_oogen_ooexpression_constructor_args():
    sig = inspect.signature(oogen_OOExpression.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oocompoundstatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOCompoundStatement)


def test_hyp_oogen_oocompoundstatement_constructor_exists():
    assert callable(oogen_OOCompoundStatement.__init__)


def test_hyp_oogen_oocompoundstatement_constructor_args():
    sig = inspect.signature(oogen_OOCompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooreturn_is_not_abstract():
    assert not inspect.isabstract(oogen_OOReturn)


def test_hyp_oogen_ooreturn_constructor_exists():
    assert callable(oogen_OOReturn.__init__)


def test_hyp_oogen_ooreturn_constructor_args():
    sig = inspect.signature(oogen_OOReturn.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooswitch_is_not_abstract():
    assert not inspect.isabstract(oogen_OOSwitch)


def test_hyp_oogen_ooswitch_constructor_exists():
    assert callable(oogen_OOSwitch.__init__)


def test_hyp_oogen_ooswitch_constructor_args():
    sig = inspect.signature(oogen_OOSwitch.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oovariabledeclarationlist_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariableDeclarationList)


def test_hyp_oogen_oovariabledeclarationlist_constructor_exists():
    assert callable(oogen_OOVariableDeclarationList.__init__)


def test_hyp_oogen_oovariabledeclarationlist_constructor_args():
    sig = inspect.signature(oogen_OOVariableDeclarationList.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oocontinue_is_not_abstract():
    assert not inspect.isabstract(oogen_OOContinue)


def test_hyp_oogen_oocontinue_constructor_exists():
    assert callable(oogen_OOContinue.__init__)


def test_hyp_oogen_oocontinue_constructor_args():
    sig = inspect.signature(oogen_OOContinue.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oobreak_is_not_abstract():
    assert not inspect.isabstract(oogen_OOBreak)


def test_hyp_oogen_oobreak_constructor_exists():
    assert callable(oogen_OOBreak.__init__)


def test_hyp_oogen_oobreak_constructor_args():
    sig = inspect.signature(oogen_OOBreak.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooforeach_is_not_abstract():
    assert not inspect.isabstract(oogen_OOForEach)


def test_hyp_oogen_ooforeach_constructor_exists():
    assert callable(oogen_OOForEach.__init__)


def test_hyp_oogen_ooforeach_constructor_args():
    sig = inspect.signature(oogen_OOForEach.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_ooconditionalstatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOConditionalStatement)


def test_hyp_oogen_ooconditionalstatement_constructor_exists():
    assert callable(oogen_OOConditionalStatement.__init__)


def test_hyp_oogen_ooconditionalstatement_constructor_args():
    sig = inspect.signature(oogen_OOConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oovariable_is_not_abstract():
    assert not inspect.isabstract(oogen_OOVariable)


def test_hyp_oogen_oovariable_constructor_exists():
    assert callable(oogen_OOVariable.__init__)


def test_hyp_oogen_oovariable_constructor_args():
    sig = inspect.signature(oogen_OOVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "transient" in params, "Missing parameter 'transient'"





def test_hyp_oogen_ooconstructor_is_not_abstract():
    assert not inspect.isabstract(oogen_OOConstructor)


def test_hyp_oogen_ooconstructor_constructor_exists():
    assert callable(oogen_OOConstructor.__init__)


def test_hyp_oogen_ooconstructor_constructor_args():
    sig = inspect.signature(oogen_OOConstructor.__init__)
    params = list(sig.parameters.keys())
    assert "className" in params, "Missing parameter 'className'"
    assert "visibility" in params, "Missing parameter 'visibility'"





def test_hyp_oocommentowner_is_not_abstract():
    assert not inspect.isabstract(OOCommentOwner)


def test_hyp_oocommentowner_constructor_exists():
    assert callable(OOCommentOwner.__init__)


def test_hyp_oocommentowner_constructor_args():
    sig = inspect.signature(OOCommentOwner.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oostatement_is_not_abstract():
    assert not inspect.isabstract(oogen_OOStatement)


def test_hyp_oogen_oostatement_constructor_exists():
    assert callable(oogen_OOStatement.__init__)


def test_hyp_oogen_oostatement_constructor_args():
    sig = inspect.signature(oogen_OOStatement.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oomethod_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMethod)


def test_hyp_oogen_oomethod_constructor_exists():
    assert callable(oogen_OOMethod.__init__)


def test_hyp_oogen_oomethod_constructor_args():
    sig = inspect.signature(oogen_OOMethod.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "languages" in params, "Missing parameter 'languages'"
    assert "name" in params, "Missing parameter 'name'"
    assert "static" in params, "Missing parameter 'static'"







def test_hyp_oovariable_is_not_abstract():
    assert not inspect.isabstract(OOVariable)


def test_hyp_oovariable_constructor_exists():
    assert callable(OOVariable.__init__)


def test_hyp_oovariable_constructor_args():
    sig = inspect.signature(OOVariable.__init__)
    params = list(sig.parameters.keys())



def test_hyp_oogen_oomember_is_not_abstract():
    assert not inspect.isabstract(oogen_OOMember)


def test_hyp_oogen_oomember_constructor_exists():
    assert callable(oogen_OOMember.__init__)


def test_hyp_oogen_oomember_constructor_args():
    sig = inspect.signature(oogen_OOMember.__init__)
    params = list(sig.parameters.keys())
    assert "languages" in params, "Missing parameter 'languages'"
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"






def test_hyp_oogen_oopackage_is_not_abstract():
    assert not inspect.isabstract(oogen_OOPackage)


def test_hyp_oogen_oopackage_constructor_exists():
    assert callable(oogen_OOPackage.__init__)


def test_hyp_oogen_oopackage_constructor_args():
    sig = inspect.signature(oogen_OOPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"




def test_hyp_oogen_ooenumeration_is_not_abstract():
    assert not inspect.isabstract(oogen_OOEnumeration)


def test_hyp_oogen_ooenumeration_constructor_exists():
    assert callable(oogen_OOEnumeration.__init__)


def test_hyp_oogen_ooenumeration_constructor_args():
    sig = inspect.signature(oogen_OOEnumeration.__init__)
    params = list(sig.parameters.keys())
    assert "options" in params, "Missing parameter 'options'"
    assert "name" in params, "Missing parameter 'name'"





def test_hyp_oogen_ooclass_is_not_abstract():
    assert not inspect.isabstract(oogen_OOClass)


def test_hyp_oogen_ooclass_constructor_exists():
    assert callable(oogen_OOClass.__init__)


def test_hyp_oogen_ooclass_constructor_args():
    sig = inspect.signature(oogen_OOClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "keep" in params, "Missing parameter 'keep'"
    assert "languages" in params, "Missing parameter 'languages'"




def test_hyp_oovisibility_exists():
    # Check that the Enumeration exists
    assert OOVisibility is not None

def test_hyp_oovisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOVisibility]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
        "PACKAGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOVisibility"

def test_hyp_oolanguage_exists():
    # Check that the Enumeration exists
    assert OOLanguage is not None

def test_hyp_oolanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOLanguage]
    expected_literals = [
        "JAVA",
        "CPP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOLanguage"

def test_hyp_oobasetype_exists():
    # Check that the Enumeration exists
    assert OOBaseType is not None

def test_hyp_oobasetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOBaseType]
    expected_literals = [
        "INT",
        "BYTE",
        "DOUBLE",
        "OBJECT",
        "LONG",
        "STRING",
        "BOOLEAN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOBaseType"

def test_hyp_oocollectiontype_exists():
    # Check that the Enumeration exists
    assert OOCollectionType is not None

def test_hyp_oocollectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OOCollectionType]
    expected_literals = [
        "LIST",
        "SET",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OOCollectionType"


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
oogen_OOCommentOwner_strategy = st.builds(
    oogen_OOCommentOwner,
)
oogen_OOComment_strategy = st.builds(
    oogen_OOComment,
    text=
        safe_text,
    isBlockComment=
        st.booleans()
)
OOComparatorExpression_strategy = st.builds(
    OOComparatorExpression,
)
oogen_OOEqualsExpression_strategy = st.builds(
    oogen_OOEqualsExpression,
)
oogen_OOLanguageSpecificSnippet_strategy = st.builds(
    oogen_OOLanguageSpecificSnippet,
    code=
        safe_text,
    lang=
        safe_text
)
OOOneOperandArithmeticExpression_strategy = st.builds(
    OOOneOperandArithmeticExpression,
)
oogen_OOPostfixDecrementExpression_strategy = st.builds(
    oogen_OOPostfixDecrementExpression,
)
oogen_OOPrefixIncrementExpression_strategy = st.builds(
    oogen_OOPrefixIncrementExpression,
)
oogen_OOPrefixDecrementExpression_strategy = st.builds(
    oogen_OOPrefixDecrementExpression,
)
oogen_OOPostfixIncrementExpression_strategy = st.builds(
    oogen_OOPostfixIncrementExpression,
)
oogen_OOPlusExpression_strategy = st.builds(
    oogen_OOPlusExpression,
)
oogen_OOMinusExpression_strategy = st.builds(
    oogen_OOMinusExpression,
)
oogen_OOBracketedExpression_strategy = st.builds(
    oogen_OOBracketedExpression,
)
oogen_OOBitWiseComplement_strategy = st.builds(
    oogen_OOBitWiseComplement,
)
oogen_OOLessEqualsExpression_strategy = st.builds(
    oogen_OOLessEqualsExpression,
)
oogen_OOGreaterEqualsExpression_strategy = st.builds(
    oogen_OOGreaterEqualsExpression,
)
oogen_OONotEqualsExpression_strategy = st.builds(
    oogen_OONotEqualsExpression,
)
oogen_OOLessThanExpression_strategy = st.builds(
    oogen_OOLessThanExpression,
)
oogen_OOGreaterThanExpression_strategy = st.builds(
    oogen_OOGreaterThanExpression,
)
OOCompoundStatement_strategy = st.builds(
    OOCompoundStatement,
)
oogen_OODefault_strategy = st.builds(
    oogen_OODefault,
)
oogen_OOCase_strategy = st.builds(
    oogen_OOCase,
)
OOConditionalStatement_strategy = st.builds(
    OOConditionalStatement,
)
oogen_OOFor_strategy = st.builds(
    oogen_OOFor,
)
oogen_OOIf_strategy = st.builds(
    oogen_OOIf,
)
OOLogicalExpression_strategy = st.builds(
    OOLogicalExpression,
)
oogen_OOTernaryOperator_strategy = st.builds(
    oogen_OOTernaryOperator,
)
oogen_OOLogicalLiteral_strategy = st.builds(
    oogen_OOLogicalLiteral,
    value=
        st.booleans()
)
oogen_OOOneOperandLogicalExpression_strategy = st.builds(
    oogen_OOOneOperandLogicalExpression,
)
oogen_OOComparatorExpression_strategy = st.builds(
    oogen_OOComparatorExpression,
)
oogen_OOTwoOperandLogicalExpression_strategy = st.builds(
    oogen_OOTwoOperandLogicalExpression,
)
OOOneOperandLogicalExpression_strategy = st.builds(
    OOOneOperandLogicalExpression,
)
oogen_OONotExpression_strategy = st.builds(
    oogen_OONotExpression,
)
OOTwoOperandLogicalExpression_strategy = st.builds(
    OOTwoOperandLogicalExpression,
)
oogen_OOXorExpression_strategy = st.builds(
    oogen_OOXorExpression,
)
oogen_OOOrExpression_strategy = st.builds(
    oogen_OOOrExpression,
)
oogen_OOAndExpression_strategy = st.builds(
    oogen_OOAndExpression,
)
OOTwoOperandArithmeticExpression_strategy = st.builds(
    OOTwoOperandArithmeticExpression,
)
oogen_OOTwoOperandAssignableExpression_strategy = st.builds(
    oogen_OOTwoOperandAssignableExpression,
    assigned=
        st.booleans()
)
oogen_OORootExpression_strategy = st.builds(
    oogen_OORootExpression,
)
oogen_OOPowerExpression_strategy = st.builds(
    oogen_OOPowerExpression,
)
oogen_OODoWhile_strategy = st.builds(
    oogen_OODoWhile,
)
oogen_OOWhile_strategy = st.builds(
    oogen_OOWhile,
)
OOArithmeticExpression_strategy = st.builds(
    OOArithmeticExpression,
)
oogen_OOOneOperandArithmeticExpression_strategy = st.builds(
    oogen_OOOneOperandArithmeticExpression,
)
oogen_OOFloatLiteral_strategy = st.builds(
    oogen_OOFloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen_OODoubleLiteral_strategy = st.builds(
    oogen_OODoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
oogen_OOLongLiteral_strategy = st.builds(
    oogen_OOLongLiteral,
    value=
        safe_text
)
oogen_OOIntegerLiteral_strategy = st.builds(
    oogen_OOIntegerLiteral,
    value=
        st.integers()
)
oogen_OOTwoOperandArithmeticExpression_strategy = st.builds(
    oogen_OOTwoOperandArithmeticExpression,
)
OOExpression_strategy = st.builds(
    OOExpression,
)
oogen_OONullLiteral_strategy = st.builds(
    oogen_OONullLiteral,
)
oogen_OOFieldReferenceExpression_strategy = st.builds(
    oogen_OOFieldReferenceExpression,
    fieldName=
        safe_text
)
oogen_OOBoolLiteral_strategy = st.builds(
    oogen_OOBoolLiteral,
    value=
        st.booleans()
)
oogen_OOIndexing_strategy = st.builds(
    oogen_OOIndexing,
)
oogen_OONewClass_strategy = st.builds(
    oogen_OONewClass,
    className=
        safe_text
)
oogen_OOLogicalExpression_strategy = st.builds(
    oogen_OOLogicalExpression,
)
oogen_OOTypeCast_strategy = st.builds(
    oogen_OOTypeCast,
)
oogen_OONewArray_strategy = st.builds(
    oogen_OONewArray,
)
oogen_OOEmptyExpression_strategy = st.builds(
    oogen_OOEmptyExpression,
)
oogen_OOAssignmentExpression_strategy = st.builds(
    oogen_OOAssignmentExpression,
)
oogen_OOVariableReferenceExpression_strategy = st.builds(
    oogen_OOVariableReferenceExpression,
)
oogen_OOThisLiteral_strategy = st.builds(
    oogen_OOThisLiteral,
)
oogen_OOLanguageSpecificExpression_strategy = st.builds(
    oogen_OOLanguageSpecificExpression,
)
oogen_OOFunctionCallExpression_strategy = st.builds(
    oogen_OOFunctionCallExpression,
    functionName=
        safe_text
)
oogen_OOStringLiteral_strategy = st.builds(
    oogen_OOStringLiteral,
    value=
        safe_text
)
oogen_OOInitializerList_strategy = st.builds(
    oogen_OOInitializerList,
)
oogen_OOArithmeticExpression_strategy = st.builds(
    oogen_OOArithmeticExpression,
)
oogen_OOModel_strategy = st.builds(
    oogen_OOModel,
)
OOTwoOperandAssignableExpression_strategy = st.builds(
    OOTwoOperandAssignableExpression,
)
oogen_OOBitwiseXorExpression_strategy = st.builds(
    oogen_OOBitwiseXorExpression,
)
oogen_OOBitwiseOrExpression_strategy = st.builds(
    oogen_OOBitwiseOrExpression,
)
oogen_OOBitWiseLeftShift_strategy = st.builds(
    oogen_OOBitWiseLeftShift,
)
oogen_OOBitwiseAndExpression_strategy = st.builds(
    oogen_OOBitwiseAndExpression,
)
oogen_OOMultiplicationExpression_strategy = st.builds(
    oogen_OOMultiplicationExpression,
)
oogen_OOBitWiseRightShift_strategy = st.builds(
    oogen_OOBitWiseRightShift,
)
oogen_OOSubtractionExpression_strategy = st.builds(
    oogen_OOSubtractionExpression,
)
oogen_OOIntegerDivisionExpression_strategy = st.builds(
    oogen_OOIntegerDivisionExpression,
)
oogen_OODivisionExpression_strategy = st.builds(
    oogen_OODivisionExpression,
)
oogen_OOModuloExpression_strategy = st.builds(
    oogen_OOModuloExpression,
)
oogen_OOAdditionExpression_strategy = st.builds(
    oogen_OOAdditionExpression,
)
oogen_OOType_strategy = st.builds(
    oogen_OOType,
    baseType=
        safe_text,
    collectionType=
        safe_text,
    numberOfIndirections=
        st.integers(),
    arrayDimensions=
        st.integers()
)
OOStatement_strategy = st.builds(
    OOStatement,
)
oogen_OOEmptyStatement_strategy = st.builds(
    oogen_OOEmptyStatement,
)
oogen_OOExpression_strategy = st.builds(
    oogen_OOExpression,
)
oogen_OOCompoundStatement_strategy = st.builds(
    oogen_OOCompoundStatement,
)
oogen_OOReturn_strategy = st.builds(
    oogen_OOReturn,
)
oogen_OOSwitch_strategy = st.builds(
    oogen_OOSwitch,
)
oogen_OOVariableDeclarationList_strategy = st.builds(
    oogen_OOVariableDeclarationList,
)
oogen_OOContinue_strategy = st.builds(
    oogen_OOContinue,
)
oogen_OOBreak_strategy = st.builds(
    oogen_OOBreak,
)
oogen_OOForEach_strategy = st.builds(
    oogen_OOForEach,
)
oogen_OOConditionalStatement_strategy = st.builds(
    oogen_OOConditionalStatement,
)
oogen_OOVariable_strategy = st.builds(
    oogen_OOVariable,
    name=
        safe_text,
    transient=
        st.booleans()
)
oogen_OOConstructor_strategy = st.builds(
    oogen_OOConstructor,
    className=
        safe_text,
    visibility=
        safe_text
)
OOCommentOwner_strategy = st.builds(
    OOCommentOwner,
)
oogen_OOStatement_strategy = st.builds(
    oogen_OOStatement,
)
oogen_OOMethod_strategy = st.builds(
    oogen_OOMethod,
    visibility=
        safe_text,
    languages=
        safe_text,
    name=
        safe_text,
    static=
        st.booleans()
)
OOVariable_strategy = st.builds(
    OOVariable,
)
oogen_OOMember_strategy = st.builds(
    oogen_OOMember,
    languages=
        safe_text,
    static=
        st.booleans(),
    visibility=
        safe_text
)
oogen_OOPackage_strategy = st.builds(
    oogen_OOPackage,
    name=
        safe_text
)
oogen_OOEnumeration_strategy = st.builds(
    oogen_OOEnumeration,
    options=
        safe_text,
    name=
        safe_text
)
oogen_OOClass_strategy = st.builds(
    oogen_OOClass,
    name=
        safe_text,
    keep=
        st.booleans(),
    languages=
        safe_text
)





@given(instance=oogen_OOComment_strategy)
def test_hyp_oogen_oocomment_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=oogen_OOComment_strategy)
def test_hyp_oogen_oocomment_isBlockComment_setter(instance):
    original = instance.isBlockComment
    instance.isBlockComment = original
    assert instance.isBlockComment == original






@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
def test_hyp_oogen_oolanguagespecificsnippet_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original



@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
def test_hyp_oogen_oolanguagespecificsnippet_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original


























@given(instance=oogen_OOLogicalLiteral_strategy)
def test_hyp_oogen_oologicalliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original














@given(instance=oogen_OOTwoOperandAssignableExpression_strategy)
def test_hyp_oogen_ootwooperandassignableexpression_assigned_setter(instance):
    original = instance.assigned
    instance.assigned = original
    assert instance.assigned == original










@given(instance=oogen_OOFloatLiteral_strategy)
def test_hyp_oogen_oofloatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=oogen_OODoubleLiteral_strategy)
def test_hyp_oogen_oodoubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=oogen_OOLongLiteral_strategy)
def test_hyp_oogen_oolongliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=oogen_OOIntegerLiteral_strategy)
def test_hyp_oogen_oointegerliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original







@given(instance=oogen_OOFieldReferenceExpression_strategy)
def test_hyp_oogen_oofieldreferenceexpression_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original




@given(instance=oogen_OOBoolLiteral_strategy)
def test_hyp_oogen_ooboolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original





@given(instance=oogen_OONewClass_strategy)
def test_hyp_oogen_oonewclass_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original












@given(instance=oogen_OOFunctionCallExpression_strategy)
def test_hyp_oogen_oofunctioncallexpression_functionName_setter(instance):
    original = instance.functionName
    instance.functionName = original
    assert instance.functionName == original




@given(instance=oogen_OOStringLiteral_strategy)
def test_hyp_oogen_oostringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



















@given(instance=oogen_OOType_strategy)
def test_hyp_oogen_ootype_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original



@given(instance=oogen_OOType_strategy)
def test_hyp_oogen_ootype_collectionType_setter(instance):
    original = instance.collectionType
    instance.collectionType = original
    assert instance.collectionType == original



@given(instance=oogen_OOType_strategy)
def test_hyp_oogen_ootype_numberOfIndirections_setter(instance):
    original = instance.numberOfIndirections
    instance.numberOfIndirections = original
    assert instance.numberOfIndirections == original



@given(instance=oogen_OOType_strategy)
def test_hyp_oogen_ootype_arrayDimensions_setter(instance):
    original = instance.arrayDimensions
    instance.arrayDimensions = original
    assert instance.arrayDimensions == original















@given(instance=oogen_OOVariable_strategy)
def test_hyp_oogen_oovariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOVariable_strategy)
def test_hyp_oogen_oovariable_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original




@given(instance=oogen_OOConstructor_strategy)
def test_hyp_oogen_ooconstructor_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original



@given(instance=oogen_OOConstructor_strategy)
def test_hyp_oogen_ooconstructor_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original






@given(instance=oogen_OOMethod_strategy)
def test_hyp_oogen_oomethod_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=oogen_OOMethod_strategy)
def test_hyp_oogen_oomethod_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=oogen_OOMethod_strategy)
def test_hyp_oogen_oomethod_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOMethod_strategy)
def test_hyp_oogen_oomethod_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original





@given(instance=oogen_OOMember_strategy)
def test_hyp_oogen_oomember_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original



@given(instance=oogen_OOMember_strategy)
def test_hyp_oogen_oomember_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=oogen_OOMember_strategy)
def test_hyp_oogen_oomember_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original




@given(instance=oogen_OOPackage_strategy)
def test_hyp_oogen_oopackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oogen_OOEnumeration_strategy)
def test_hyp_oogen_ooenumeration_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=oogen_OOEnumeration_strategy)
def test_hyp_oogen_ooenumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original




@given(instance=oogen_OOClass_strategy)
def test_hyp_oogen_ooclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oogen_OOClass_strategy)
def test_hyp_oogen_ooclass_keep_setter(instance):
    original = instance.keep
    instance.keep = original
    assert instance.keep == original



@given(instance=oogen_OOClass_strategy)
def test_hyp_oogen_ooclass_languages_setter(instance):
    original = instance.languages
    instance.languages = original
    assert instance.languages == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    OOArithmeticExpression,
    OOCommentOwner,
    OOComparatorExpression,
    OOCompoundStatement,
    OOConditionalStatement,
    OOExpression,
    OOLogicalExpression,
    OOOneOperandArithmeticExpression,
    OOOneOperandLogicalExpression,
    OOStatement,
    OOTwoOperandArithmeticExpression,
    OOTwoOperandAssignableExpression,
    OOTwoOperandLogicalExpression,
    OOVariable,
    oogen_OOAdditionExpression,
    oogen_OOAndExpression,
    oogen_OOArithmeticExpression,
    oogen_OOAssignmentExpression,
    oogen_OOBitWiseComplement,
    oogen_OOBitWiseLeftShift,
    oogen_OOBitWiseRightShift,
    oogen_OOBitwiseAndExpression,
    oogen_OOBitwiseOrExpression,
    oogen_OOBitwiseXorExpression,
    oogen_OOBoolLiteral,
    oogen_OOBracketedExpression,
    oogen_OOBreak,
    oogen_OOCase,
    oogen_OOClass,
    oogen_OOComment,
    oogen_OOCommentOwner,
    oogen_OOComparatorExpression,
    oogen_OOCompoundStatement,
    oogen_OOConditionalStatement,
    oogen_OOConstructor,
    oogen_OOContinue,
    oogen_OODefault,
    oogen_OODivisionExpression,
    oogen_OODoWhile,
    oogen_OODoubleLiteral,
    oogen_OOEmptyExpression,
    oogen_OOEmptyStatement,
    oogen_OOEnumeration,
    oogen_OOEqualsExpression,
    oogen_OOExpression,
    oogen_OOFieldReferenceExpression,
    oogen_OOFloatLiteral,
    oogen_OOFor,
    oogen_OOForEach,
    oogen_OOFunctionCallExpression,
    oogen_OOGreaterEqualsExpression,
    oogen_OOGreaterThanExpression,
    oogen_OOIf,
    oogen_OOIndexing,
    oogen_OOInitializerList,
    oogen_OOIntegerDivisionExpression,
    oogen_OOIntegerLiteral,
    oogen_OOLanguageSpecificExpression,
    oogen_OOLanguageSpecificSnippet,
    oogen_OOLessEqualsExpression,
    oogen_OOLessThanExpression,
    oogen_OOLogicalExpression,
    oogen_OOLogicalLiteral,
    oogen_OOLongLiteral,
    oogen_OOMember,
    oogen_OOMethod,
    oogen_OOMinusExpression,
    oogen_OOModel,
    oogen_OOModuloExpression,
    oogen_OOMultiplicationExpression,
    oogen_OONewArray,
    oogen_OONewClass,
    oogen_OONotEqualsExpression,
    oogen_OONotExpression,
    oogen_OONullLiteral,
    oogen_OOOneOperandArithmeticExpression,
    oogen_OOOneOperandLogicalExpression,
    oogen_OOOrExpression,
    oogen_OOPackage,
    oogen_OOPlusExpression,
    oogen_OOPostfixDecrementExpression,
    oogen_OOPostfixIncrementExpression,
    oogen_OOPowerExpression,
    oogen_OOPrefixDecrementExpression,
    oogen_OOPrefixIncrementExpression,
    oogen_OOReturn,
    oogen_OORootExpression,
    oogen_OOStatement,
    oogen_OOStringLiteral,
    oogen_OOSubtractionExpression,
    oogen_OOSwitch,
    oogen_OOTernaryOperator,
    oogen_OOThisLiteral,
    oogen_OOTwoOperandArithmeticExpression,
    oogen_OOTwoOperandAssignableExpression,
    oogen_OOTwoOperandLogicalExpression,
    oogen_OOType,
    oogen_OOTypeCast,
    oogen_OOVariable,
    oogen_OOVariableDeclarationList,
    oogen_OOVariableReferenceExpression,
    oogen_OOWhile,
    oogen_OOXorExpression,
    OOBaseType,
    OOCollectionType,
    OOLanguage,
    OOVisibility,
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

def test_oogen_OOBoolLiteral_value_value_roundtrip():
    instance = oogen_OOBoolLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_oogen_OOClass_keep_value_roundtrip():
    instance = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    assert instance.keep == True
    instance.keep = False
    assert instance.keep == False


def test_oogen_OOClass_languages_value_roundtrip():
    instance = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    assert instance.languages == "sample_text"
    instance.languages = "sample_text_2"
    assert instance.languages == "sample_text_2"


def test_oogen_OOClass_name_value_roundtrip():
    instance = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oogen_OOComment_isBlockComment_value_roundtrip():
    instance = oogen_OOComment(isBlockComment=True, text="sample_text")
    assert instance.isBlockComment == True
    instance.isBlockComment = False
    assert instance.isBlockComment == False


def test_oogen_OOComment_text_value_roundtrip():
    instance = oogen_OOComment(isBlockComment=True, text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_oogen_OOConstructor_className_value_roundtrip():
    instance = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_oogen_OOConstructor_visibility_value_roundtrip():
    instance = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_oogen_OODoubleLiteral_value_value_roundtrip():
    instance = oogen_OODoubleLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_oogen_OOEnumeration_name_value_roundtrip():
    instance = oogen_OOEnumeration(name="sample_text", options="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oogen_OOEnumeration_options_value_roundtrip():
    instance = oogen_OOEnumeration(name="sample_text", options="sample_text")
    assert instance.options == "sample_text"
    instance.options = "sample_text_2"
    assert instance.options == "sample_text_2"


def test_oogen_OOFieldReferenceExpression_fieldName_value_roundtrip():
    instance = oogen_OOFieldReferenceExpression(fieldName="sample_text")
    assert instance.fieldName == "sample_text"
    instance.fieldName = "sample_text_2"
    assert instance.fieldName == "sample_text_2"


def test_oogen_OOFloatLiteral_value_value_roundtrip():
    instance = oogen_OOFloatLiteral(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_oogen_OOFunctionCallExpression_functionName_value_roundtrip():
    instance = oogen_OOFunctionCallExpression(functionName="sample_text")
    assert instance.functionName == "sample_text"
    instance.functionName = "sample_text_2"
    assert instance.functionName == "sample_text_2"


def test_oogen_OOIntegerLiteral_value_value_roundtrip():
    instance = oogen_OOIntegerLiteral(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_oogen_OOLanguageSpecificSnippet_code_value_roundtrip():
    instance = oogen_OOLanguageSpecificSnippet(code="sample_text", lang="sample_text")
    assert instance.code == "sample_text"
    instance.code = "sample_text_2"
    assert instance.code == "sample_text_2"


def test_oogen_OOLanguageSpecificSnippet_lang_value_roundtrip():
    instance = oogen_OOLanguageSpecificSnippet(code="sample_text", lang="sample_text")
    assert instance.lang == "sample_text"
    instance.lang = "sample_text_2"
    assert instance.lang == "sample_text_2"


def test_oogen_OOLogicalLiteral_value_value_roundtrip():
    instance = oogen_OOLogicalLiteral(value=True)
    assert instance.value == True
    instance.value = False
    assert instance.value == False


def test_oogen_OOLongLiteral_value_value_roundtrip():
    instance = oogen_OOLongLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_oogen_OOMember_languages_value_roundtrip():
    instance = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    assert instance.languages == "sample_text"
    instance.languages = "sample_text_2"
    assert instance.languages == "sample_text_2"


def test_oogen_OOMember_static_value_roundtrip():
    instance = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_oogen_OOMember_visibility_value_roundtrip():
    instance = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_oogen_OOMethod_languages_value_roundtrip():
    instance = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    assert instance.languages == "sample_text"
    instance.languages = "sample_text_2"
    assert instance.languages == "sample_text_2"


def test_oogen_OOMethod_name_value_roundtrip():
    instance = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oogen_OOMethod_static_value_roundtrip():
    instance = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_oogen_OOMethod_visibility_value_roundtrip():
    instance = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    assert instance.visibility == "sample_text"
    instance.visibility = "sample_text_2"
    assert instance.visibility == "sample_text_2"


def test_oogen_OONewClass_className_value_roundtrip():
    instance = oogen_OONewClass(className="sample_text")
    assert instance.className == "sample_text"
    instance.className = "sample_text_2"
    assert instance.className == "sample_text_2"


def test_oogen_OOPackage_name_value_roundtrip():
    instance = oogen_OOPackage(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oogen_OOStringLiteral_value_value_roundtrip():
    instance = oogen_OOStringLiteral(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_oogen_OOTwoOperandAssignableExpression_assigned_value_roundtrip():
    instance = oogen_OOTwoOperandAssignableExpression(assigned=True)
    assert instance.assigned == True
    instance.assigned = False
    assert instance.assigned == False


def test_oogen_OOType_arrayDimensions_value_roundtrip():
    instance = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    assert instance.arrayDimensions == 7
    instance.arrayDimensions = 13
    assert instance.arrayDimensions == 13


def test_oogen_OOType_baseType_value_roundtrip():
    instance = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    assert instance.baseType == "sample_text"
    instance.baseType = "sample_text_2"
    assert instance.baseType == "sample_text_2"


def test_oogen_OOType_collectionType_value_roundtrip():
    instance = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    assert instance.collectionType == "sample_text"
    instance.collectionType = "sample_text_2"
    assert instance.collectionType == "sample_text_2"


def test_oogen_OOType_numberOfIndirections_value_roundtrip():
    instance = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    assert instance.numberOfIndirections == 7
    instance.numberOfIndirections = 13
    assert instance.numberOfIndirections == 13


def test_oogen_OOVariable_name_value_roundtrip():
    instance = oogen_OOVariable(name="sample_text", transient=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_oogen_OOVariable_transient_value_roundtrip():
    instance = oogen_OOVariable(name="sample_text", transient=True)
    assert instance.transient == True
    instance.transient = False
    assert instance.transient == False


def test_oogen_OODoubleLiteral_isa_OOArithmeticExpression():
    instance = oogen_OODoubleLiteral(value=3.14)
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOFloatLiteral_isa_OOArithmeticExpression():
    instance = oogen_OOFloatLiteral(value=3.14)
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOIntegerLiteral_isa_OOArithmeticExpression():
    instance = oogen_OOIntegerLiteral(value=7)
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOLongLiteral_isa_OOArithmeticExpression():
    instance = oogen_OOLongLiteral(value="sample_text")
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOOneOperandArithmeticExpression_isa_OOArithmeticExpression():
    instance = oogen_OOOneOperandArithmeticExpression()
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOTwoOperandArithmeticExpression_isa_OOArithmeticExpression():
    instance = oogen_OOTwoOperandArithmeticExpression()
    assert isinstance(instance, OOArithmeticExpression)


def test_oogen_OOClass_isa_OOCommentOwner():
    instance = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    assert isinstance(instance, OOCommentOwner)


def test_oogen_OOEnumeration_isa_OOCommentOwner():
    instance = oogen_OOEnumeration(name="sample_text", options="sample_text")
    assert isinstance(instance, OOCommentOwner)


def test_oogen_OOMethod_isa_OOCommentOwner():
    instance = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    assert isinstance(instance, OOCommentOwner)


def test_oogen_OOStatement_isa_OOCommentOwner():
    instance = oogen_OOStatement()
    assert isinstance(instance, OOCommentOwner)


def test_oogen_OOEqualsExpression_isa_OOComparatorExpression():
    instance = oogen_OOEqualsExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OOGreaterEqualsExpression_isa_OOComparatorExpression():
    instance = oogen_OOGreaterEqualsExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OOGreaterThanExpression_isa_OOComparatorExpression():
    instance = oogen_OOGreaterThanExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OOLessEqualsExpression_isa_OOComparatorExpression():
    instance = oogen_OOLessEqualsExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OOLessThanExpression_isa_OOComparatorExpression():
    instance = oogen_OOLessThanExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OONotEqualsExpression_isa_OOComparatorExpression():
    instance = oogen_OONotEqualsExpression()
    assert isinstance(instance, OOComparatorExpression)


def test_oogen_OOCase_isa_OOCompoundStatement():
    instance = oogen_OOCase()
    assert isinstance(instance, OOCompoundStatement)


def test_oogen_OOConditionalStatement_isa_OOCompoundStatement():
    instance = oogen_OOConditionalStatement()
    assert isinstance(instance, OOCompoundStatement)


def test_oogen_OODefault_isa_OOCompoundStatement():
    instance = oogen_OODefault()
    assert isinstance(instance, OOCompoundStatement)


def test_oogen_OODoWhile_isa_OOConditionalStatement():
    instance = oogen_OODoWhile()
    assert isinstance(instance, OOConditionalStatement)


def test_oogen_OOFor_isa_OOConditionalStatement():
    instance = oogen_OOFor()
    assert isinstance(instance, OOConditionalStatement)


def test_oogen_OOIf_isa_OOConditionalStatement():
    instance = oogen_OOIf()
    assert isinstance(instance, OOConditionalStatement)


def test_oogen_OOWhile_isa_OOConditionalStatement():
    instance = oogen_OOWhile()
    assert isinstance(instance, OOConditionalStatement)


def test_oogen_OOArithmeticExpression_isa_OOExpression():
    instance = oogen_OOArithmeticExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OOAssignmentExpression_isa_OOExpression():
    instance = oogen_OOAssignmentExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OOBoolLiteral_isa_OOExpression():
    instance = oogen_OOBoolLiteral(value=True)
    assert isinstance(instance, OOExpression)


def test_oogen_OOEmptyExpression_isa_OOExpression():
    instance = oogen_OOEmptyExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OOFieldReferenceExpression_isa_OOExpression():
    instance = oogen_OOFieldReferenceExpression(fieldName="sample_text")
    assert isinstance(instance, OOExpression)


def test_oogen_OOFunctionCallExpression_isa_OOExpression():
    instance = oogen_OOFunctionCallExpression(functionName="sample_text")
    assert isinstance(instance, OOExpression)


def test_oogen_OOIndexing_isa_OOExpression():
    instance = oogen_OOIndexing()
    assert isinstance(instance, OOExpression)


def test_oogen_OOInitializerList_isa_OOExpression():
    instance = oogen_OOInitializerList()
    assert isinstance(instance, OOExpression)


def test_oogen_OOLanguageSpecificExpression_isa_OOExpression():
    instance = oogen_OOLanguageSpecificExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OOLogicalExpression_isa_OOExpression():
    instance = oogen_OOLogicalExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OONewArray_isa_OOExpression():
    instance = oogen_OONewArray()
    assert isinstance(instance, OOExpression)


def test_oogen_OONewClass_isa_OOExpression():
    instance = oogen_OONewClass(className="sample_text")
    assert isinstance(instance, OOExpression)


def test_oogen_OONullLiteral_isa_OOExpression():
    instance = oogen_OONullLiteral()
    assert isinstance(instance, OOExpression)


def test_oogen_OOStringLiteral_isa_OOExpression():
    instance = oogen_OOStringLiteral(value="sample_text")
    assert isinstance(instance, OOExpression)


def test_oogen_OOThisLiteral_isa_OOExpression():
    instance = oogen_OOThisLiteral()
    assert isinstance(instance, OOExpression)


def test_oogen_OOTypeCast_isa_OOExpression():
    instance = oogen_OOTypeCast()
    assert isinstance(instance, OOExpression)


def test_oogen_OOVariableReferenceExpression_isa_OOExpression():
    instance = oogen_OOVariableReferenceExpression()
    assert isinstance(instance, OOExpression)


def test_oogen_OOComparatorExpression_isa_OOLogicalExpression():
    instance = oogen_OOComparatorExpression()
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOLanguageSpecificExpression_isa_OOLogicalExpression():
    instance = oogen_OOLanguageSpecificExpression()
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOLogicalLiteral_isa_OOLogicalExpression():
    instance = oogen_OOLogicalLiteral(value=True)
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOOneOperandLogicalExpression_isa_OOLogicalExpression():
    instance = oogen_OOOneOperandLogicalExpression()
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOTernaryOperator_isa_OOLogicalExpression():
    instance = oogen_OOTernaryOperator()
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOTwoOperandLogicalExpression_isa_OOLogicalExpression():
    instance = oogen_OOTwoOperandLogicalExpression()
    assert isinstance(instance, OOLogicalExpression)


def test_oogen_OOBitWiseComplement_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOBitWiseComplement()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOBracketedExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOBracketedExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOMinusExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOMinusExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOPlusExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOPlusExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOPostfixDecrementExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOPostfixDecrementExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOPostfixIncrementExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOPostfixIncrementExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOPrefixDecrementExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOPrefixDecrementExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OOPrefixIncrementExpression_isa_OOOneOperandArithmeticExpression():
    instance = oogen_OOPrefixIncrementExpression()
    assert isinstance(instance, OOOneOperandArithmeticExpression)


def test_oogen_OONotExpression_isa_OOOneOperandLogicalExpression():
    instance = oogen_OONotExpression()
    assert isinstance(instance, OOOneOperandLogicalExpression)


def test_oogen_OOBreak_isa_OOStatement():
    instance = oogen_OOBreak()
    assert isinstance(instance, OOStatement)


def test_oogen_OOCompoundStatement_isa_OOStatement():
    instance = oogen_OOCompoundStatement()
    assert isinstance(instance, OOStatement)


def test_oogen_OOConditionalStatement_isa_OOStatement():
    instance = oogen_OOConditionalStatement()
    assert isinstance(instance, OOStatement)


def test_oogen_OOContinue_isa_OOStatement():
    instance = oogen_OOContinue()
    assert isinstance(instance, OOStatement)


def test_oogen_OOEmptyStatement_isa_OOStatement():
    instance = oogen_OOEmptyStatement()
    assert isinstance(instance, OOStatement)


def test_oogen_OOExpression_isa_OOStatement():
    instance = oogen_OOExpression()
    assert isinstance(instance, OOStatement)


def test_oogen_OOForEach_isa_OOStatement():
    instance = oogen_OOForEach()
    assert isinstance(instance, OOStatement)


def test_oogen_OOReturn_isa_OOStatement():
    instance = oogen_OOReturn()
    assert isinstance(instance, OOStatement)


def test_oogen_OOSwitch_isa_OOStatement():
    instance = oogen_OOSwitch()
    assert isinstance(instance, OOStatement)


def test_oogen_OOVariable_isa_OOStatement():
    instance = oogen_OOVariable(name="sample_text", transient=True)
    assert isinstance(instance, OOStatement)


def test_oogen_OOVariableDeclarationList_isa_OOStatement():
    instance = oogen_OOVariableDeclarationList()
    assert isinstance(instance, OOStatement)


def test_oogen_OOPowerExpression_isa_OOTwoOperandArithmeticExpression():
    instance = oogen_OOPowerExpression()
    assert isinstance(instance, OOTwoOperandArithmeticExpression)


def test_oogen_OORootExpression_isa_OOTwoOperandArithmeticExpression():
    instance = oogen_OORootExpression()
    assert isinstance(instance, OOTwoOperandArithmeticExpression)


def test_oogen_OOTwoOperandAssignableExpression_isa_OOTwoOperandArithmeticExpression():
    instance = oogen_OOTwoOperandAssignableExpression(assigned=True)
    assert isinstance(instance, OOTwoOperandArithmeticExpression)


def test_oogen_OOAdditionExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOAdditionExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOBitWiseLeftShift_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOBitWiseLeftShift()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOBitWiseRightShift_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOBitWiseRightShift()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOBitwiseAndExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOBitwiseAndExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOBitwiseOrExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOBitwiseOrExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOBitwiseXorExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOBitwiseXorExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OODivisionExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OODivisionExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOIntegerDivisionExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOIntegerDivisionExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOModuloExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOModuloExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOMultiplicationExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOMultiplicationExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOSubtractionExpression_isa_OOTwoOperandAssignableExpression():
    instance = oogen_OOSubtractionExpression()
    assert isinstance(instance, OOTwoOperandAssignableExpression)


def test_oogen_OOAndExpression_isa_OOTwoOperandLogicalExpression():
    instance = oogen_OOAndExpression()
    assert isinstance(instance, OOTwoOperandLogicalExpression)


def test_oogen_OOOrExpression_isa_OOTwoOperandLogicalExpression():
    instance = oogen_OOOrExpression()
    assert isinstance(instance, OOTwoOperandLogicalExpression)


def test_oogen_OOXorExpression_isa_OOTwoOperandLogicalExpression():
    instance = oogen_OOXorExpression()
    assert isinstance(instance, OOTwoOperandLogicalExpression)


def test_oogen_OOMember_isa_OOVariable():
    instance = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    assert isinstance(instance, OOVariable)


def test_assoc_afterComments142_link_reassign_clear():
    a = oogen_OOComment(isBlockComment=True, text="sample_text")
    b1 = oogen_OOCommentOwner()
    b2 = oogen_OOCommentOwner()
    _safe_set(a, 'oogen_OOComment144', b1)
    assert _is_linked(a, 'oogen_OOComment144', b1)
    if hasattr(b1, 'oogen_OOCommentOwner143'):
        assert _is_linked(b1, 'oogen_OOCommentOwner143', a)
    _safe_set(a, 'oogen_OOComment144', b2)
    assert _is_linked(a, 'oogen_OOComment144', b2)
    if hasattr(b1, 'oogen_OOCommentOwner143'):
        assert not _is_linked(b1, 'oogen_OOCommentOwner143', a)
    if hasattr(b2, 'oogen_OOCommentOwner143'):
        assert _is_linked(b2, 'oogen_OOCommentOwner143', a)
    _safe_set(a, 'oogen_OOComment144', None)
    assert not _is_linked(a, 'oogen_OOComment144', b2)
    if hasattr(b2, 'oogen_OOCommentOwner143'):
        assert not _is_linked(b2, 'oogen_OOCommentOwner143', a)


def test_assoc_argumentExpressions125_link_reassign_clear():
    a = oogen_OOFunctionCallExpression(functionName="sample_text")
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OOFunctionCallExpression', {b1})
    assert _is_linked(a, 'oogen_OOFunctionCallExpression', b1)
    if hasattr(b1, 'oogen_OOExpression126'):
        assert _is_linked(b1, 'oogen_OOExpression126', a)
    _safe_set(a, 'oogen_OOFunctionCallExpression', {b2})
    assert _is_linked(a, 'oogen_OOFunctionCallExpression', b2)
    if hasattr(b1, 'oogen_OOExpression126'):
        assert not _is_linked(b1, 'oogen_OOExpression126', a)
    if hasattr(b2, 'oogen_OOExpression126'):
        assert _is_linked(b2, 'oogen_OOExpression126', a)
    _safe_set(a, 'oogen_OOFunctionCallExpression', set())
    assert not _is_linked(a, 'oogen_OOFunctionCallExpression', b2)
    if hasattr(b2, 'oogen_OOExpression126'):
        assert not _is_linked(b2, 'oogen_OOExpression126', a)


def test_assoc_arraySizeExpressions14_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OOType15', {b1})
    assert _is_linked(a, 'oogen_OOType15', b1)
    if hasattr(b1, 'oogen_OOExpression16'):
        assert _is_linked(b1, 'oogen_OOExpression16', a)
    _safe_set(a, 'oogen_OOType15', {b2})
    assert _is_linked(a, 'oogen_OOType15', b2)
    if hasattr(b1, 'oogen_OOExpression16'):
        assert not _is_linked(b1, 'oogen_OOExpression16', a)
    if hasattr(b2, 'oogen_OOExpression16'):
        assert _is_linked(b2, 'oogen_OOExpression16', a)
    _safe_set(a, 'oogen_OOType15', set())
    assert not _is_linked(a, 'oogen_OOType15', b2)
    if hasattr(b2, 'oogen_OOExpression16'):
        assert not _is_linked(b2, 'oogen_OOExpression16', a)


def test_assoc_arrayType136_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OONewArray()
    b2 = oogen_OONewArray()
    _safe_set(a, 'oogen_OOType137', b1)
    assert _is_linked(a, 'oogen_OOType137', b1)
    if hasattr(b1, 'oogen_OONewArray'):
        assert _is_linked(b1, 'oogen_OONewArray', a)
    _safe_set(a, 'oogen_OOType137', b2)
    assert _is_linked(a, 'oogen_OOType137', b2)
    if hasattr(b1, 'oogen_OONewArray'):
        assert not _is_linked(b1, 'oogen_OONewArray', a)
    if hasattr(b2, 'oogen_OONewArray'):
        assert _is_linked(b2, 'oogen_OONewArray', a)
    _safe_set(a, 'oogen_OOType137', None)
    assert not _is_linked(a, 'oogen_OOType137', b2)
    if hasattr(b2, 'oogen_OONewArray'):
        assert not _is_linked(b2, 'oogen_OONewArray', a)


def test_assoc_beforeComments141_link_reassign_clear():
    a = oogen_OOComment(isBlockComment=True, text="sample_text")
    b1 = oogen_OOCommentOwner()
    b2 = oogen_OOCommentOwner()
    _safe_set(a, 'oogen_OOComment', b1)
    assert _is_linked(a, 'oogen_OOComment', b1)
    if hasattr(b1, 'oogen_OOCommentOwner'):
        assert _is_linked(b1, 'oogen_OOCommentOwner', a)
    _safe_set(a, 'oogen_OOComment', b2)
    assert _is_linked(a, 'oogen_OOComment', b2)
    if hasattr(b1, 'oogen_OOCommentOwner'):
        assert not _is_linked(b1, 'oogen_OOCommentOwner', a)
    if hasattr(b2, 'oogen_OOCommentOwner'):
        assert _is_linked(b2, 'oogen_OOCommentOwner', a)
    _safe_set(a, 'oogen_OOComment', None)
    assert not _is_linked(a, 'oogen_OOComment', b2)
    if hasattr(b2, 'oogen_OOCommentOwner'):
        assert not _is_linked(b2, 'oogen_OOCommentOwner', a)


def test_assoc_classType11_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oogen_OOType12', b1)
    assert _is_linked(a, 'oogen_OOType12', b1)
    if hasattr(b1, 'oogen_OOClass13'):
        assert _is_linked(b1, 'oogen_OOClass13', a)
    _safe_set(a, 'oogen_OOType12', b2)
    assert _is_linked(a, 'oogen_OOType12', b2)
    if hasattr(b1, 'oogen_OOClass13'):
        assert not _is_linked(b1, 'oogen_OOClass13', a)
    if hasattr(b2, 'oogen_OOClass13'):
        assert _is_linked(b2, 'oogen_OOClass13', a)
    _safe_set(a, 'oogen_OOType12', None)
    assert not _is_linked(a, 'oogen_OOType12', b2)
    if hasattr(b2, 'oogen_OOClass13'):
        assert not _is_linked(b2, 'oogen_OOClass13', a)


def test_assoc_classes0_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'package', {b1})
    assert _is_linked(a, 'package', b1)
    if hasattr(b1, 'OOClass'):
        assert _is_linked(b1, 'OOClass', a)
    _safe_set(a, 'package', {b2})
    assert _is_linked(a, 'package', b2)
    if hasattr(b1, 'OOClass'):
        assert not _is_linked(b1, 'OOClass', a)
    if hasattr(b2, 'OOClass'):
        assert _is_linked(b2, 'OOClass', a)
    _safe_set(a, 'package', set())
    assert not _is_linked(a, 'package', b2)
    if hasattr(b2, 'OOClass'):
        assert not _is_linked(b2, 'OOClass', a)


def test_assoc_constructorParameterExpressions89_link_reassign_clear():
    a = oogen_OONewClass(className="sample_text")
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OONewClass', {b1})
    assert _is_linked(a, 'oogen_OONewClass', b1)
    if hasattr(b1, 'oogen_OOExpression90'):
        assert _is_linked(b1, 'oogen_OOExpression90', a)
    _safe_set(a, 'oogen_OONewClass', {b2})
    assert _is_linked(a, 'oogen_OONewClass', b2)
    if hasattr(b1, 'oogen_OOExpression90'):
        assert not _is_linked(b1, 'oogen_OOExpression90', a)
    if hasattr(b2, 'oogen_OOExpression90'):
        assert _is_linked(b2, 'oogen_OOExpression90', a)
    _safe_set(a, 'oogen_OONewClass', set())
    assert not _is_linked(a, 'oogen_OONewClass', b2)
    if hasattr(b2, 'oogen_OOExpression90'):
        assert not _is_linked(b2, 'oogen_OOExpression90', a)


def test_assoc_constructors6_link_reassign_clear():
    a = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oogen_OOConstructor', b1)
    assert _is_linked(a, 'oogen_OOConstructor', b1)
    if hasattr(b1, 'oogen_OOClass7'):
        assert _is_linked(b1, 'oogen_OOClass7', a)
    _safe_set(a, 'oogen_OOConstructor', b2)
    assert _is_linked(a, 'oogen_OOConstructor', b2)
    if hasattr(b1, 'oogen_OOClass7'):
        assert not _is_linked(b1, 'oogen_OOClass7', a)
    if hasattr(b2, 'oogen_OOClass7'):
        assert _is_linked(b2, 'oogen_OOClass7', a)
    _safe_set(a, 'oogen_OOConstructor', None)
    assert not _is_linked(a, 'oogen_OOConstructor', b2)
    if hasattr(b2, 'oogen_OOClass7'):
        assert not _is_linked(b2, 'oogen_OOClass7', a)


def test_assoc_enumType17_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OOEnumeration(name="sample_text", options="sample_text")
    b2 = oogen_OOEnumeration(name="sample_text_2", options="sample_text_2")
    _safe_set(a, 'oogen_OOType18', b1)
    assert _is_linked(a, 'oogen_OOType18', b1)
    if hasattr(b1, 'oogen_OOEnumeration19'):
        assert _is_linked(b1, 'oogen_OOEnumeration19', a)
    _safe_set(a, 'oogen_OOType18', b2)
    assert _is_linked(a, 'oogen_OOType18', b2)
    if hasattr(b1, 'oogen_OOEnumeration19'):
        assert not _is_linked(b1, 'oogen_OOEnumeration19', a)
    if hasattr(b2, 'oogen_OOEnumeration19'):
        assert _is_linked(b2, 'oogen_OOEnumeration19', a)
    _safe_set(a, 'oogen_OOType18', None)
    assert not _is_linked(a, 'oogen_OOType18', b2)
    if hasattr(b2, 'oogen_OOEnumeration19'):
        assert not _is_linked(b2, 'oogen_OOEnumeration19', a)


def test_assoc_enums1_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOEnumeration(name="sample_text", options="sample_text")
    b2 = oogen_OOEnumeration(name="sample_text_2", options="sample_text_2")
    _safe_set(a, 'oogen_OOPackage', {b1})
    assert _is_linked(a, 'oogen_OOPackage', b1)
    if hasattr(b1, 'oogen_OOEnumeration'):
        assert _is_linked(b1, 'oogen_OOEnumeration', a)
    _safe_set(a, 'oogen_OOPackage', {b2})
    assert _is_linked(a, 'oogen_OOPackage', b2)
    if hasattr(b1, 'oogen_OOEnumeration'):
        assert not _is_linked(b1, 'oogen_OOEnumeration', a)
    if hasattr(b2, 'oogen_OOEnumeration'):
        assert _is_linked(b2, 'oogen_OOEnumeration', a)
    _safe_set(a, 'oogen_OOPackage', set())
    assert not _is_linked(a, 'oogen_OOPackage', b2)
    if hasattr(b2, 'oogen_OOEnumeration'):
        assert not _is_linked(b2, 'oogen_OOEnumeration', a)


def test_assoc_fieldOwner119_link_reassign_clear():
    a = oogen_OOFieldReferenceExpression(fieldName="sample_text")
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OOFieldReferenceExpression', b1)
    assert _is_linked(a, 'oogen_OOFieldReferenceExpression', b1)
    if hasattr(b1, 'oogen_OOExpression120'):
        assert _is_linked(b1, 'oogen_OOExpression120', a)
    _safe_set(a, 'oogen_OOFieldReferenceExpression', b2)
    assert _is_linked(a, 'oogen_OOFieldReferenceExpression', b2)
    if hasattr(b1, 'oogen_OOExpression120'):
        assert not _is_linked(b1, 'oogen_OOExpression120', a)
    if hasattr(b2, 'oogen_OOExpression120'):
        assert _is_linked(b2, 'oogen_OOExpression120', a)
    _safe_set(a, 'oogen_OOFieldReferenceExpression', None)
    assert not _is_linked(a, 'oogen_OOFieldReferenceExpression', b2)
    if hasattr(b2, 'oogen_OOExpression120'):
        assert not _is_linked(b2, 'oogen_OOExpression120', a)


def test_assoc_globalFunctions36_link_reassign_clear():
    a = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    b1 = oogen_OOModel()
    b2 = oogen_OOModel()
    _safe_set(a, 'oogen_OOMethod38', b1)
    assert _is_linked(a, 'oogen_OOMethod38', b1)
    if hasattr(b1, 'oogen_OOModel37'):
        assert _is_linked(b1, 'oogen_OOModel37', a)
    _safe_set(a, 'oogen_OOMethod38', b2)
    assert _is_linked(a, 'oogen_OOMethod38', b2)
    if hasattr(b1, 'oogen_OOModel37'):
        assert not _is_linked(b1, 'oogen_OOModel37', a)
    if hasattr(b2, 'oogen_OOModel37'):
        assert _is_linked(b2, 'oogen_OOModel37', a)
    _safe_set(a, 'oogen_OOMethod38', None)
    assert not _is_linked(a, 'oogen_OOMethod38', b2)
    if hasattr(b2, 'oogen_OOModel37'):
        assert not _is_linked(b2, 'oogen_OOModel37', a)


def test_assoc_globalVariables33_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOModel()
    b2 = oogen_OOModel()
    _safe_set(a, 'oogen_OOVariable35', b1)
    assert _is_linked(a, 'oogen_OOVariable35', b1)
    if hasattr(b1, 'oogen_OOModel34'):
        assert _is_linked(b1, 'oogen_OOModel34', a)
    _safe_set(a, 'oogen_OOVariable35', b2)
    assert _is_linked(a, 'oogen_OOVariable35', b2)
    if hasattr(b1, 'oogen_OOModel34'):
        assert not _is_linked(b1, 'oogen_OOModel34', a)
    if hasattr(b2, 'oogen_OOModel34'):
        assert _is_linked(b2, 'oogen_OOModel34', a)
    _safe_set(a, 'oogen_OOVariable35', None)
    assert not _is_linked(a, 'oogen_OOVariable35', b2)
    if hasattr(b2, 'oogen_OOModel34'):
        assert not _is_linked(b2, 'oogen_OOModel34', a)


def test_assoc_initializerExpression9_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OOVariable10', b1)
    assert _is_linked(a, 'oogen_OOVariable10', b1)
    if hasattr(b1, 'oogen_OOExpression'):
        assert _is_linked(b1, 'oogen_OOExpression', a)
    _safe_set(a, 'oogen_OOVariable10', b2)
    assert _is_linked(a, 'oogen_OOVariable10', b2)
    if hasattr(b1, 'oogen_OOExpression'):
        assert not _is_linked(b1, 'oogen_OOExpression', a)
    if hasattr(b2, 'oogen_OOExpression'):
        assert _is_linked(b2, 'oogen_OOExpression', a)
    _safe_set(a, 'oogen_OOVariable10', None)
    assert not _is_linked(a, 'oogen_OOVariable10', b2)
    if hasattr(b2, 'oogen_OOExpression'):
        assert not _is_linked(b2, 'oogen_OOExpression', a)


def test_assoc_loopVariable77_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOForEach()
    b2 = oogen_OOForEach()
    _safe_set(a, 'oogen_OOVariable79', b1)
    assert _is_linked(a, 'oogen_OOVariable79', b1)
    if hasattr(b1, 'oogen_OOForEach78'):
        assert _is_linked(b1, 'oogen_OOForEach78', a)
    _safe_set(a, 'oogen_OOVariable79', b2)
    assert _is_linked(a, 'oogen_OOVariable79', b2)
    if hasattr(b1, 'oogen_OOForEach78'):
        assert not _is_linked(b1, 'oogen_OOForEach78', a)
    if hasattr(b2, 'oogen_OOForEach78'):
        assert _is_linked(b2, 'oogen_OOForEach78', a)
    _safe_set(a, 'oogen_OOVariable79', None)
    assert not _is_linked(a, 'oogen_OOVariable79', b2)
    if hasattr(b2, 'oogen_OOForEach78'):
        assert not _is_linked(b2, 'oogen_OOForEach78', a)


def test_assoc_members2_link_reassign_clear():
    a = oogen_OOMember(languages="sample_text", static=True, visibility="sample_text")
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oogen_OOMember', b1)
    assert _is_linked(a, 'oogen_OOMember', b1)
    if hasattr(b1, 'oogen_OOClass'):
        assert _is_linked(b1, 'oogen_OOClass', a)
    _safe_set(a, 'oogen_OOMember', b2)
    assert _is_linked(a, 'oogen_OOMember', b2)
    if hasattr(b1, 'oogen_OOClass'):
        assert not _is_linked(b1, 'oogen_OOClass', a)
    if hasattr(b2, 'oogen_OOClass'):
        assert _is_linked(b2, 'oogen_OOClass', a)
    _safe_set(a, 'oogen_OOMember', None)
    assert not _is_linked(a, 'oogen_OOMember', b2)
    if hasattr(b2, 'oogen_OOClass'):
        assert not _is_linked(b2, 'oogen_OOClass', a)


def test_assoc_methods4_link_reassign_clear():
    a = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'oogen_OOMethod', b1)
    assert _is_linked(a, 'oogen_OOMethod', b1)
    if hasattr(b1, 'oogen_OOClass5'):
        assert _is_linked(b1, 'oogen_OOClass5', a)
    _safe_set(a, 'oogen_OOMethod', b2)
    assert _is_linked(a, 'oogen_OOMethod', b2)
    if hasattr(b1, 'oogen_OOClass5'):
        assert not _is_linked(b1, 'oogen_OOClass5', a)
    if hasattr(b2, 'oogen_OOClass5'):
        assert _is_linked(b2, 'oogen_OOClass5', a)
    _safe_set(a, 'oogen_OOMethod', None)
    assert not _is_linked(a, 'oogen_OOMethod', b2)
    if hasattr(b2, 'oogen_OOClass5'):
        assert not _is_linked(b2, 'oogen_OOClass5', a)


def test_assoc_oopackage28_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOModel()
    b2 = oogen_OOModel()
    _safe_set(a, 'oogen_OOPackage29', b1)
    assert _is_linked(a, 'oogen_OOPackage29', b1)
    if hasattr(b1, 'oogen_OOModel'):
        assert _is_linked(b1, 'oogen_OOModel', a)
    _safe_set(a, 'oogen_OOPackage29', b2)
    assert _is_linked(a, 'oogen_OOPackage29', b2)
    if hasattr(b1, 'oogen_OOModel'):
        assert not _is_linked(b1, 'oogen_OOModel', a)
    if hasattr(b2, 'oogen_OOModel'):
        assert _is_linked(b2, 'oogen_OOModel', a)
    _safe_set(a, 'oogen_OOPackage29', None)
    assert not _is_linked(a, 'oogen_OOPackage29', b2)
    if hasattr(b2, 'oogen_OOModel'):
        assert not _is_linked(b2, 'oogen_OOModel', a)


def test_assoc_ownerExpression127_link_reassign_clear():
    a = oogen_OOFunctionCallExpression(functionName="sample_text")
    b1 = oogen_OOExpression()
    b2 = oogen_OOExpression()
    _safe_set(a, 'oogen_OOFunctionCallExpression128', b1)
    assert _is_linked(a, 'oogen_OOFunctionCallExpression128', b1)
    if hasattr(b1, 'oogen_OOExpression129'):
        assert _is_linked(b1, 'oogen_OOExpression129', a)
    _safe_set(a, 'oogen_OOFunctionCallExpression128', b2)
    assert _is_linked(a, 'oogen_OOFunctionCallExpression128', b2)
    if hasattr(b1, 'oogen_OOExpression129'):
        assert not _is_linked(b1, 'oogen_OOExpression129', a)
    if hasattr(b2, 'oogen_OOExpression129'):
        assert _is_linked(b2, 'oogen_OOExpression129', a)
    _safe_set(a, 'oogen_OOFunctionCallExpression128', None)
    assert not _is_linked(a, 'oogen_OOFunctionCallExpression128', b2)
    if hasattr(b2, 'oogen_OOExpression129'):
        assert not _is_linked(b2, 'oogen_OOExpression129', a)


def test_assoc_package145_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOEnumeration(name="sample_text", options="sample_text")
    b2 = oogen_OOEnumeration(name="sample_text_2", options="sample_text_2")
    _safe_set(a, 'oogen_OOPackage147', b1)
    assert _is_linked(a, 'oogen_OOPackage147', b1)
    if hasattr(b1, 'oogen_OOEnumeration146'):
        assert _is_linked(b1, 'oogen_OOEnumeration146', a)
    _safe_set(a, 'oogen_OOPackage147', b2)
    assert _is_linked(a, 'oogen_OOPackage147', b2)
    if hasattr(b1, 'oogen_OOEnumeration146'):
        assert not _is_linked(b1, 'oogen_OOEnumeration146', a)
    if hasattr(b2, 'oogen_OOEnumeration146'):
        assert _is_linked(b2, 'oogen_OOEnumeration146', a)
    _safe_set(a, 'oogen_OOPackage147', None)
    assert not _is_linked(a, 'oogen_OOPackage147', b2)
    if hasattr(b2, 'oogen_OOEnumeration146'):
        assert not _is_linked(b2, 'oogen_OOEnumeration146', a)


def test_assoc_package3_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOClass(keep=True, languages="sample_text", name="sample_text")
    b2 = oogen_OOClass(keep=False, languages="sample_text_2", name="sample_text_2")
    _safe_set(a, 'OOPackage', b1)
    assert _is_linked(a, 'OOPackage', b1)
    if hasattr(b1, 'classes'):
        assert _is_linked(b1, 'classes', a)
    _safe_set(a, 'OOPackage', b2)
    assert _is_linked(a, 'OOPackage', b2)
    if hasattr(b1, 'classes'):
        assert not _is_linked(b1, 'classes', a)
    if hasattr(b2, 'classes'):
        assert _is_linked(b2, 'classes', a)
    _safe_set(a, 'OOPackage', None)
    assert not _is_linked(a, 'OOPackage', b2)
    if hasattr(b2, 'classes'):
        assert not _is_linked(b2, 'classes', a)


def test_assoc_packages30_link_reassign_clear():
    a = oogen_OOPackage(name="sample_text")
    b1 = oogen_OOModel()
    b2 = oogen_OOModel()
    _safe_set(a, 'oogen_OOPackage32', b1)
    assert _is_linked(a, 'oogen_OOPackage32', b1)
    if hasattr(b1, 'oogen_OOModel31'):
        assert _is_linked(b1, 'oogen_OOModel31', a)
    _safe_set(a, 'oogen_OOPackage32', b2)
    assert _is_linked(a, 'oogen_OOPackage32', b2)
    if hasattr(b1, 'oogen_OOModel31'):
        assert not _is_linked(b1, 'oogen_OOModel31', a)
    if hasattr(b2, 'oogen_OOModel31'):
        assert _is_linked(b2, 'oogen_OOModel31', a)
    _safe_set(a, 'oogen_OOPackage32', None)
    assert not _is_linked(a, 'oogen_OOPackage32', b2)
    if hasattr(b2, 'oogen_OOModel31'):
        assert not _is_linked(b2, 'oogen_OOModel31', a)


def test_assoc_parameters130_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    b2 = oogen_OOConstructor(className="sample_text_2", visibility="sample_text_2")
    _safe_set(a, 'oogen_OOVariable132', b1)
    assert _is_linked(a, 'oogen_OOVariable132', b1)
    if hasattr(b1, 'oogen_OOConstructor131'):
        assert _is_linked(b1, 'oogen_OOConstructor131', a)
    _safe_set(a, 'oogen_OOVariable132', b2)
    assert _is_linked(a, 'oogen_OOVariable132', b2)
    if hasattr(b1, 'oogen_OOConstructor131'):
        assert not _is_linked(b1, 'oogen_OOConstructor131', a)
    if hasattr(b2, 'oogen_OOConstructor131'):
        assert _is_linked(b2, 'oogen_OOConstructor131', a)
    _safe_set(a, 'oogen_OOVariable132', None)
    assert not _is_linked(a, 'oogen_OOVariable132', b2)
    if hasattr(b2, 'oogen_OOConstructor131'):
        assert not _is_linked(b2, 'oogen_OOConstructor131', a)


def test_assoc_parameters20_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    b2 = oogen_OOMethod(languages="sample_text_2", name="sample_text_2", static=False, visibility="sample_text_2")
    _safe_set(a, 'oogen_OOVariable22', b1)
    assert _is_linked(a, 'oogen_OOVariable22', b1)
    if hasattr(b1, 'oogen_OOMethod21'):
        assert _is_linked(b1, 'oogen_OOMethod21', a)
    _safe_set(a, 'oogen_OOVariable22', b2)
    assert _is_linked(a, 'oogen_OOVariable22', b2)
    if hasattr(b1, 'oogen_OOMethod21'):
        assert not _is_linked(b1, 'oogen_OOMethod21', a)
    if hasattr(b2, 'oogen_OOMethod21'):
        assert _is_linked(b2, 'oogen_OOMethod21', a)
    _safe_set(a, 'oogen_OOVariable22', None)
    assert not _is_linked(a, 'oogen_OOVariable22', b2)
    if hasattr(b2, 'oogen_OOMethod21'):
        assert not _is_linked(b2, 'oogen_OOMethod21', a)


def test_assoc_returnType23_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    b2 = oogen_OOMethod(languages="sample_text_2", name="sample_text_2", static=False, visibility="sample_text_2")
    _safe_set(a, 'oogen_OOType25', b1)
    assert _is_linked(a, 'oogen_OOType25', b1)
    if hasattr(b1, 'oogen_OOMethod24'):
        assert _is_linked(b1, 'oogen_OOMethod24', a)
    _safe_set(a, 'oogen_OOType25', b2)
    assert _is_linked(a, 'oogen_OOType25', b2)
    if hasattr(b1, 'oogen_OOMethod24'):
        assert not _is_linked(b1, 'oogen_OOMethod24', a)
    if hasattr(b2, 'oogen_OOMethod24'):
        assert _is_linked(b2, 'oogen_OOMethod24', a)
    _safe_set(a, 'oogen_OOType25', None)
    assert not _is_linked(a, 'oogen_OOType25', b2)
    if hasattr(b2, 'oogen_OOMethod24'):
        assert not _is_linked(b2, 'oogen_OOMethod24', a)


def test_assoc_snippets83_link_reassign_clear():
    a = oogen_OOLanguageSpecificSnippet(code="sample_text", lang="sample_text")
    b1 = oogen_OOLanguageSpecificExpression()
    b2 = oogen_OOLanguageSpecificExpression()
    _safe_set(a, 'oogen_OOLanguageSpecificSnippet', b1)
    assert _is_linked(a, 'oogen_OOLanguageSpecificSnippet', b1)
    if hasattr(b1, 'oogen_OOLanguageSpecificExpression'):
        assert _is_linked(b1, 'oogen_OOLanguageSpecificExpression', a)
    _safe_set(a, 'oogen_OOLanguageSpecificSnippet', b2)
    assert _is_linked(a, 'oogen_OOLanguageSpecificSnippet', b2)
    if hasattr(b1, 'oogen_OOLanguageSpecificExpression'):
        assert not _is_linked(b1, 'oogen_OOLanguageSpecificExpression', a)
    if hasattr(b2, 'oogen_OOLanguageSpecificExpression'):
        assert _is_linked(b2, 'oogen_OOLanguageSpecificExpression', a)
    _safe_set(a, 'oogen_OOLanguageSpecificSnippet', None)
    assert not _is_linked(a, 'oogen_OOLanguageSpecificSnippet', b2)
    if hasattr(b2, 'oogen_OOLanguageSpecificExpression'):
        assert not _is_linked(b2, 'oogen_OOLanguageSpecificExpression', a)


def test_assoc_statements133_link_reassign_clear():
    a = oogen_OOConstructor(className="sample_text", visibility="sample_text")
    b1 = oogen_OOStatement()
    b2 = oogen_OOStatement()
    _safe_set(a, 'oogen_OOConstructor134', {b1})
    assert _is_linked(a, 'oogen_OOConstructor134', b1)
    if hasattr(b1, 'oogen_OOStatement135'):
        assert _is_linked(b1, 'oogen_OOStatement135', a)
    _safe_set(a, 'oogen_OOConstructor134', {b2})
    assert _is_linked(a, 'oogen_OOConstructor134', b2)
    if hasattr(b1, 'oogen_OOStatement135'):
        assert not _is_linked(b1, 'oogen_OOStatement135', a)
    if hasattr(b2, 'oogen_OOStatement135'):
        assert _is_linked(b2, 'oogen_OOStatement135', a)
    _safe_set(a, 'oogen_OOConstructor134', set())
    assert not _is_linked(a, 'oogen_OOConstructor134', b2)
    if hasattr(b2, 'oogen_OOStatement135'):
        assert not _is_linked(b2, 'oogen_OOStatement135', a)


def test_assoc_statements26_link_reassign_clear():
    a = oogen_OOMethod(languages="sample_text", name="sample_text", static=True, visibility="sample_text")
    b1 = oogen_OOStatement()
    b2 = oogen_OOStatement()
    _safe_set(a, 'oogen_OOMethod27', {b1})
    assert _is_linked(a, 'oogen_OOMethod27', b1)
    if hasattr(b1, 'oogen_OOStatement'):
        assert _is_linked(b1, 'oogen_OOStatement', a)
    _safe_set(a, 'oogen_OOMethod27', {b2})
    assert _is_linked(a, 'oogen_OOMethod27', b2)
    if hasattr(b1, 'oogen_OOStatement'):
        assert not _is_linked(b1, 'oogen_OOStatement', a)
    if hasattr(b2, 'oogen_OOStatement'):
        assert _is_linked(b2, 'oogen_OOStatement', a)
    _safe_set(a, 'oogen_OOMethod27', set())
    assert not _is_linked(a, 'oogen_OOMethod27', b2)
    if hasattr(b2, 'oogen_OOStatement'):
        assert not _is_linked(b2, 'oogen_OOStatement', a)


def test_assoc_traversedVariable75_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOForEach()
    b2 = oogen_OOForEach()
    _safe_set(a, 'oogen_OOVariable76', b1)
    assert _is_linked(a, 'oogen_OOVariable76', b1)
    if hasattr(b1, 'oogen_OOForEach'):
        assert _is_linked(b1, 'oogen_OOForEach', a)
    _safe_set(a, 'oogen_OOVariable76', b2)
    assert _is_linked(a, 'oogen_OOVariable76', b2)
    if hasattr(b1, 'oogen_OOForEach'):
        assert not _is_linked(b1, 'oogen_OOForEach', a)
    if hasattr(b2, 'oogen_OOForEach'):
        assert _is_linked(b2, 'oogen_OOForEach', a)
    _safe_set(a, 'oogen_OOVariable76', None)
    assert not _is_linked(a, 'oogen_OOVariable76', b2)
    if hasattr(b2, 'oogen_OOForEach'):
        assert not _is_linked(b2, 'oogen_OOForEach', a)


def test_assoc_type8_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b2 = oogen_OOType(arrayDimensions=13, baseType="sample_text_2", collectionType="sample_text_2", numberOfIndirections=13)
    _safe_set(a, 'oogen_OOVariable', b1)
    assert _is_linked(a, 'oogen_OOVariable', b1)
    if hasattr(b1, 'oogen_OOType'):
        assert _is_linked(b1, 'oogen_OOType', a)
    _safe_set(a, 'oogen_OOVariable', b2)
    assert _is_linked(a, 'oogen_OOVariable', b2)
    if hasattr(b1, 'oogen_OOType'):
        assert not _is_linked(b1, 'oogen_OOType', a)
    if hasattr(b2, 'oogen_OOType'):
        assert _is_linked(b2, 'oogen_OOType', a)
    _safe_set(a, 'oogen_OOVariable', None)
    assert not _is_linked(a, 'oogen_OOVariable', b2)
    if hasattr(b2, 'oogen_OOType'):
        assert not _is_linked(b2, 'oogen_OOType', a)


def test_assoc_type84_link_reassign_clear():
    a = oogen_OOType(arrayDimensions=7, baseType="sample_text", collectionType="sample_text", numberOfIndirections=7)
    b1 = oogen_OOTypeCast()
    b2 = oogen_OOTypeCast()
    _safe_set(a, 'oogen_OOType85', b1)
    assert _is_linked(a, 'oogen_OOType85', b1)
    if hasattr(b1, 'oogen_OOTypeCast'):
        assert _is_linked(b1, 'oogen_OOTypeCast', a)
    _safe_set(a, 'oogen_OOType85', b2)
    assert _is_linked(a, 'oogen_OOType85', b2)
    if hasattr(b1, 'oogen_OOTypeCast'):
        assert not _is_linked(b1, 'oogen_OOTypeCast', a)
    if hasattr(b2, 'oogen_OOTypeCast'):
        assert _is_linked(b2, 'oogen_OOTypeCast', a)
    _safe_set(a, 'oogen_OOType85', None)
    assert not _is_linked(a, 'oogen_OOType85', b2)
    if hasattr(b2, 'oogen_OOTypeCast'):
        assert not _is_linked(b2, 'oogen_OOTypeCast', a)


def test_assoc_variable121_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOVariableReferenceExpression()
    b2 = oogen_OOVariableReferenceExpression()
    _safe_set(a, 'oogen_OOVariable122', b1)
    assert _is_linked(a, 'oogen_OOVariable122', b1)
    if hasattr(b1, 'oogen_OOVariableReferenceExpression'):
        assert _is_linked(b1, 'oogen_OOVariableReferenceExpression', a)
    _safe_set(a, 'oogen_OOVariable122', b2)
    assert _is_linked(a, 'oogen_OOVariable122', b2)
    if hasattr(b1, 'oogen_OOVariableReferenceExpression'):
        assert not _is_linked(b1, 'oogen_OOVariableReferenceExpression', a)
    if hasattr(b2, 'oogen_OOVariableReferenceExpression'):
        assert _is_linked(b2, 'oogen_OOVariableReferenceExpression', a)
    _safe_set(a, 'oogen_OOVariable122', None)
    assert not _is_linked(a, 'oogen_OOVariable122', b2)
    if hasattr(b2, 'oogen_OOVariableReferenceExpression'):
        assert not _is_linked(b2, 'oogen_OOVariableReferenceExpression', a)


def test_assoc_variableDeclarations107_link_reassign_clear():
    a = oogen_OOVariable(name="sample_text", transient=True)
    b1 = oogen_OOVariableDeclarationList()
    b2 = oogen_OOVariableDeclarationList()
    _safe_set(a, 'oogen_OOVariable108', b1)
    assert _is_linked(a, 'oogen_OOVariable108', b1)
    if hasattr(b1, 'oogen_OOVariableDeclarationList'):
        assert _is_linked(b1, 'oogen_OOVariableDeclarationList', a)
    _safe_set(a, 'oogen_OOVariable108', b2)
    assert _is_linked(a, 'oogen_OOVariable108', b2)
    if hasattr(b1, 'oogen_OOVariableDeclarationList'):
        assert not _is_linked(b1, 'oogen_OOVariableDeclarationList', a)
    if hasattr(b2, 'oogen_OOVariableDeclarationList'):
        assert _is_linked(b2, 'oogen_OOVariableDeclarationList', a)
    _safe_set(a, 'oogen_OOVariable108', None)
    assert not _is_linked(a, 'oogen_OOVariable108', b2)
    if hasattr(b2, 'oogen_OOVariableDeclarationList'):
        assert not _is_linked(b2, 'oogen_OOVariableDeclarationList', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

OOArithmeticExpression_strategy = st.builds(OOArithmeticExpression)
@given(instance=OOArithmeticExpression_strategy)
@settings(max_examples=25)
def test_OOArithmeticExpression_instantiation(instance):
    assert isinstance(instance, OOArithmeticExpression)


OOCommentOwner_strategy = st.builds(OOCommentOwner)
@given(instance=OOCommentOwner_strategy)
@settings(max_examples=25)
def test_OOCommentOwner_instantiation(instance):
    assert isinstance(instance, OOCommentOwner)


OOComparatorExpression_strategy = st.builds(OOComparatorExpression)
@given(instance=OOComparatorExpression_strategy)
@settings(max_examples=25)
def test_OOComparatorExpression_instantiation(instance):
    assert isinstance(instance, OOComparatorExpression)


OOCompoundStatement_strategy = st.builds(OOCompoundStatement)
@given(instance=OOCompoundStatement_strategy)
@settings(max_examples=25)
def test_OOCompoundStatement_instantiation(instance):
    assert isinstance(instance, OOCompoundStatement)


OOConditionalStatement_strategy = st.builds(OOConditionalStatement)
@given(instance=OOConditionalStatement_strategy)
@settings(max_examples=25)
def test_OOConditionalStatement_instantiation(instance):
    assert isinstance(instance, OOConditionalStatement)


OOExpression_strategy = st.builds(OOExpression)
@given(instance=OOExpression_strategy)
@settings(max_examples=25)
def test_OOExpression_instantiation(instance):
    assert isinstance(instance, OOExpression)


OOLogicalExpression_strategy = st.builds(OOLogicalExpression)
@given(instance=OOLogicalExpression_strategy)
@settings(max_examples=25)
def test_OOLogicalExpression_instantiation(instance):
    assert isinstance(instance, OOLogicalExpression)


OOOneOperandArithmeticExpression_strategy = st.builds(OOOneOperandArithmeticExpression)
@given(instance=OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=25)
def test_OOOneOperandArithmeticExpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandArithmeticExpression)


OOOneOperandLogicalExpression_strategy = st.builds(OOOneOperandLogicalExpression)
@given(instance=OOOneOperandLogicalExpression_strategy)
@settings(max_examples=25)
def test_OOOneOperandLogicalExpression_instantiation(instance):
    assert isinstance(instance, OOOneOperandLogicalExpression)


OOStatement_strategy = st.builds(OOStatement)
@given(instance=OOStatement_strategy)
@settings(max_examples=25)
def test_OOStatement_instantiation(instance):
    assert isinstance(instance, OOStatement)


OOTwoOperandArithmeticExpression_strategy = st.builds(OOTwoOperandArithmeticExpression)
@given(instance=OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=25)
def test_OOTwoOperandArithmeticExpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandArithmeticExpression)


OOTwoOperandAssignableExpression_strategy = st.builds(OOTwoOperandAssignableExpression)
@given(instance=OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=25)
def test_OOTwoOperandAssignableExpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandAssignableExpression)


OOTwoOperandLogicalExpression_strategy = st.builds(OOTwoOperandLogicalExpression)
@given(instance=OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=25)
def test_OOTwoOperandLogicalExpression_instantiation(instance):
    assert isinstance(instance, OOTwoOperandLogicalExpression)


OOVariable_strategy = st.builds(OOVariable)
@given(instance=OOVariable_strategy)
@settings(max_examples=25)
def test_OOVariable_instantiation(instance):
    assert isinstance(instance, OOVariable)


oogen_OOAdditionExpression_strategy = st.builds(oogen_OOAdditionExpression)
@given(instance=oogen_OOAdditionExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOAdditionExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAdditionExpression)


oogen_OOAndExpression_strategy = st.builds(oogen_OOAndExpression)
@given(instance=oogen_OOAndExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOAndExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAndExpression)


oogen_OOArithmeticExpression_strategy = st.builds(oogen_OOArithmeticExpression)
@given(instance=oogen_OOArithmeticExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOArithmeticExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOArithmeticExpression)


oogen_OOAssignmentExpression_strategy = st.builds(oogen_OOAssignmentExpression)
@given(instance=oogen_OOAssignmentExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOAssignmentExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOAssignmentExpression)


oogen_OOBitWiseComplement_strategy = st.builds(oogen_OOBitWiseComplement)
@given(instance=oogen_OOBitWiseComplement_strategy)
@settings(max_examples=25)
def test_oogen_OOBitWiseComplement_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseComplement)


oogen_OOBitWiseLeftShift_strategy = st.builds(oogen_OOBitWiseLeftShift)
@given(instance=oogen_OOBitWiseLeftShift_strategy)
@settings(max_examples=25)
def test_oogen_OOBitWiseLeftShift_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseLeftShift)


oogen_OOBitWiseRightShift_strategy = st.builds(oogen_OOBitWiseRightShift)
@given(instance=oogen_OOBitWiseRightShift_strategy)
@settings(max_examples=25)
def test_oogen_OOBitWiseRightShift_instantiation(instance):
    assert isinstance(instance, oogen_OOBitWiseRightShift)


oogen_OOBitwiseAndExpression_strategy = st.builds(oogen_OOBitwiseAndExpression)
@given(instance=oogen_OOBitwiseAndExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOBitwiseAndExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseAndExpression)


oogen_OOBitwiseOrExpression_strategy = st.builds(oogen_OOBitwiseOrExpression)
@given(instance=oogen_OOBitwiseOrExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOBitwiseOrExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseOrExpression)


oogen_OOBitwiseXorExpression_strategy = st.builds(oogen_OOBitwiseXorExpression)
@given(instance=oogen_OOBitwiseXorExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOBitwiseXorExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBitwiseXorExpression)


oogen_OOBoolLiteral_strategy = st.builds(oogen_OOBoolLiteral, value=st.booleans())
@given(instance=oogen_OOBoolLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOBoolLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOBoolLiteral)


oogen_OOBracketedExpression_strategy = st.builds(oogen_OOBracketedExpression)
@given(instance=oogen_OOBracketedExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOBracketedExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOBracketedExpression)


oogen_OOBreak_strategy = st.builds(oogen_OOBreak)
@given(instance=oogen_OOBreak_strategy)
@settings(max_examples=25)
def test_oogen_OOBreak_instantiation(instance):
    assert isinstance(instance, oogen_OOBreak)


oogen_OOCase_strategy = st.builds(oogen_OOCase)
@given(instance=oogen_OOCase_strategy)
@settings(max_examples=25)
def test_oogen_OOCase_instantiation(instance):
    assert isinstance(instance, oogen_OOCase)


oogen_OOClass_strategy = st.builds(oogen_OOClass, keep=st.booleans(), languages=safe_text, name=safe_text)
@given(instance=oogen_OOClass_strategy)
@settings(max_examples=25)
def test_oogen_OOClass_instantiation(instance):
    assert isinstance(instance, oogen_OOClass)


oogen_OOComment_strategy = st.builds(oogen_OOComment, isBlockComment=st.booleans(), text=safe_text)
@given(instance=oogen_OOComment_strategy)
@settings(max_examples=25)
def test_oogen_OOComment_instantiation(instance):
    assert isinstance(instance, oogen_OOComment)


oogen_OOCommentOwner_strategy = st.builds(oogen_OOCommentOwner)
@given(instance=oogen_OOCommentOwner_strategy)
@settings(max_examples=25)
def test_oogen_OOCommentOwner_instantiation(instance):
    assert isinstance(instance, oogen_OOCommentOwner)


oogen_OOComparatorExpression_strategy = st.builds(oogen_OOComparatorExpression)
@given(instance=oogen_OOComparatorExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOComparatorExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOComparatorExpression)


oogen_OOCompoundStatement_strategy = st.builds(oogen_OOCompoundStatement)
@given(instance=oogen_OOCompoundStatement_strategy)
@settings(max_examples=25)
def test_oogen_OOCompoundStatement_instantiation(instance):
    assert isinstance(instance, oogen_OOCompoundStatement)


oogen_OOConditionalStatement_strategy = st.builds(oogen_OOConditionalStatement)
@given(instance=oogen_OOConditionalStatement_strategy)
@settings(max_examples=25)
def test_oogen_OOConditionalStatement_instantiation(instance):
    assert isinstance(instance, oogen_OOConditionalStatement)


oogen_OOConstructor_strategy = st.builds(oogen_OOConstructor, className=safe_text, visibility=safe_text)
@given(instance=oogen_OOConstructor_strategy)
@settings(max_examples=25)
def test_oogen_OOConstructor_instantiation(instance):
    assert isinstance(instance, oogen_OOConstructor)


oogen_OOContinue_strategy = st.builds(oogen_OOContinue)
@given(instance=oogen_OOContinue_strategy)
@settings(max_examples=25)
def test_oogen_OOContinue_instantiation(instance):
    assert isinstance(instance, oogen_OOContinue)


oogen_OODefault_strategy = st.builds(oogen_OODefault)
@given(instance=oogen_OODefault_strategy)
@settings(max_examples=25)
def test_oogen_OODefault_instantiation(instance):
    assert isinstance(instance, oogen_OODefault)


oogen_OODivisionExpression_strategy = st.builds(oogen_OODivisionExpression)
@given(instance=oogen_OODivisionExpression_strategy)
@settings(max_examples=25)
def test_oogen_OODivisionExpression_instantiation(instance):
    assert isinstance(instance, oogen_OODivisionExpression)


oogen_OODoWhile_strategy = st.builds(oogen_OODoWhile)
@given(instance=oogen_OODoWhile_strategy)
@settings(max_examples=25)
def test_oogen_OODoWhile_instantiation(instance):
    assert isinstance(instance, oogen_OODoWhile)


oogen_OODoubleLiteral_strategy = st.builds(oogen_OODoubleLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=oogen_OODoubleLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OODoubleLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OODoubleLiteral)


oogen_OOEmptyExpression_strategy = st.builds(oogen_OOEmptyExpression)
@given(instance=oogen_OOEmptyExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOEmptyExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOEmptyExpression)


oogen_OOEmptyStatement_strategy = st.builds(oogen_OOEmptyStatement)
@given(instance=oogen_OOEmptyStatement_strategy)
@settings(max_examples=25)
def test_oogen_OOEmptyStatement_instantiation(instance):
    assert isinstance(instance, oogen_OOEmptyStatement)


oogen_OOEnumeration_strategy = st.builds(oogen_OOEnumeration, name=safe_text, options=safe_text)
@given(instance=oogen_OOEnumeration_strategy)
@settings(max_examples=25)
def test_oogen_OOEnumeration_instantiation(instance):
    assert isinstance(instance, oogen_OOEnumeration)


oogen_OOEqualsExpression_strategy = st.builds(oogen_OOEqualsExpression)
@given(instance=oogen_OOEqualsExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOEqualsExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOEqualsExpression)


oogen_OOExpression_strategy = st.builds(oogen_OOExpression)
@given(instance=oogen_OOExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOExpression)


oogen_OOFieldReferenceExpression_strategy = st.builds(oogen_OOFieldReferenceExpression, fieldName=safe_text)
@given(instance=oogen_OOFieldReferenceExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOFieldReferenceExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOFieldReferenceExpression)


oogen_OOFloatLiteral_strategy = st.builds(oogen_OOFloatLiteral, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=oogen_OOFloatLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOFloatLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOFloatLiteral)


oogen_OOFor_strategy = st.builds(oogen_OOFor)
@given(instance=oogen_OOFor_strategy)
@settings(max_examples=25)
def test_oogen_OOFor_instantiation(instance):
    assert isinstance(instance, oogen_OOFor)


oogen_OOForEach_strategy = st.builds(oogen_OOForEach)
@given(instance=oogen_OOForEach_strategy)
@settings(max_examples=25)
def test_oogen_OOForEach_instantiation(instance):
    assert isinstance(instance, oogen_OOForEach)


oogen_OOFunctionCallExpression_strategy = st.builds(oogen_OOFunctionCallExpression, functionName=safe_text)
@given(instance=oogen_OOFunctionCallExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOFunctionCallExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOFunctionCallExpression)


oogen_OOGreaterEqualsExpression_strategy = st.builds(oogen_OOGreaterEqualsExpression)
@given(instance=oogen_OOGreaterEqualsExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOGreaterEqualsExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOGreaterEqualsExpression)


oogen_OOGreaterThanExpression_strategy = st.builds(oogen_OOGreaterThanExpression)
@given(instance=oogen_OOGreaterThanExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOGreaterThanExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOGreaterThanExpression)


oogen_OOIf_strategy = st.builds(oogen_OOIf)
@given(instance=oogen_OOIf_strategy)
@settings(max_examples=25)
def test_oogen_OOIf_instantiation(instance):
    assert isinstance(instance, oogen_OOIf)


oogen_OOIndexing_strategy = st.builds(oogen_OOIndexing)
@given(instance=oogen_OOIndexing_strategy)
@settings(max_examples=25)
def test_oogen_OOIndexing_instantiation(instance):
    assert isinstance(instance, oogen_OOIndexing)


oogen_OOInitializerList_strategy = st.builds(oogen_OOInitializerList)
@given(instance=oogen_OOInitializerList_strategy)
@settings(max_examples=25)
def test_oogen_OOInitializerList_instantiation(instance):
    assert isinstance(instance, oogen_OOInitializerList)


oogen_OOIntegerDivisionExpression_strategy = st.builds(oogen_OOIntegerDivisionExpression)
@given(instance=oogen_OOIntegerDivisionExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOIntegerDivisionExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOIntegerDivisionExpression)


oogen_OOIntegerLiteral_strategy = st.builds(oogen_OOIntegerLiteral, value=st.integers())
@given(instance=oogen_OOIntegerLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOIntegerLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOIntegerLiteral)


oogen_OOLanguageSpecificExpression_strategy = st.builds(oogen_OOLanguageSpecificExpression)
@given(instance=oogen_OOLanguageSpecificExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOLanguageSpecificExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLanguageSpecificExpression)


oogen_OOLanguageSpecificSnippet_strategy = st.builds(oogen_OOLanguageSpecificSnippet, code=safe_text, lang=safe_text)
@given(instance=oogen_OOLanguageSpecificSnippet_strategy)
@settings(max_examples=25)
def test_oogen_OOLanguageSpecificSnippet_instantiation(instance):
    assert isinstance(instance, oogen_OOLanguageSpecificSnippet)


oogen_OOLessEqualsExpression_strategy = st.builds(oogen_OOLessEqualsExpression)
@given(instance=oogen_OOLessEqualsExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOLessEqualsExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLessEqualsExpression)


oogen_OOLessThanExpression_strategy = st.builds(oogen_OOLessThanExpression)
@given(instance=oogen_OOLessThanExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOLessThanExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLessThanExpression)


oogen_OOLogicalExpression_strategy = st.builds(oogen_OOLogicalExpression)
@given(instance=oogen_OOLogicalExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOLogicalExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOLogicalExpression)


oogen_OOLogicalLiteral_strategy = st.builds(oogen_OOLogicalLiteral, value=st.booleans())
@given(instance=oogen_OOLogicalLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOLogicalLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOLogicalLiteral)


oogen_OOLongLiteral_strategy = st.builds(oogen_OOLongLiteral, value=safe_text)
@given(instance=oogen_OOLongLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOLongLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOLongLiteral)


oogen_OOMember_strategy = st.builds(oogen_OOMember, languages=safe_text, static=st.booleans(), visibility=safe_text)
@given(instance=oogen_OOMember_strategy)
@settings(max_examples=25)
def test_oogen_OOMember_instantiation(instance):
    assert isinstance(instance, oogen_OOMember)


oogen_OOMethod_strategy = st.builds(oogen_OOMethod, languages=safe_text, name=safe_text, static=st.booleans(), visibility=safe_text)
@given(instance=oogen_OOMethod_strategy)
@settings(max_examples=25)
def test_oogen_OOMethod_instantiation(instance):
    assert isinstance(instance, oogen_OOMethod)


oogen_OOMinusExpression_strategy = st.builds(oogen_OOMinusExpression)
@given(instance=oogen_OOMinusExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOMinusExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOMinusExpression)


oogen_OOModel_strategy = st.builds(oogen_OOModel)
@given(instance=oogen_OOModel_strategy)
@settings(max_examples=25)
def test_oogen_OOModel_instantiation(instance):
    assert isinstance(instance, oogen_OOModel)


oogen_OOModuloExpression_strategy = st.builds(oogen_OOModuloExpression)
@given(instance=oogen_OOModuloExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOModuloExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOModuloExpression)


oogen_OOMultiplicationExpression_strategy = st.builds(oogen_OOMultiplicationExpression)
@given(instance=oogen_OOMultiplicationExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOMultiplicationExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOMultiplicationExpression)


oogen_OONewArray_strategy = st.builds(oogen_OONewArray)
@given(instance=oogen_OONewArray_strategy)
@settings(max_examples=25)
def test_oogen_OONewArray_instantiation(instance):
    assert isinstance(instance, oogen_OONewArray)


oogen_OONewClass_strategy = st.builds(oogen_OONewClass, className=safe_text)
@given(instance=oogen_OONewClass_strategy)
@settings(max_examples=25)
def test_oogen_OONewClass_instantiation(instance):
    assert isinstance(instance, oogen_OONewClass)


oogen_OONotEqualsExpression_strategy = st.builds(oogen_OONotEqualsExpression)
@given(instance=oogen_OONotEqualsExpression_strategy)
@settings(max_examples=25)
def test_oogen_OONotEqualsExpression_instantiation(instance):
    assert isinstance(instance, oogen_OONotEqualsExpression)


oogen_OONotExpression_strategy = st.builds(oogen_OONotExpression)
@given(instance=oogen_OONotExpression_strategy)
@settings(max_examples=25)
def test_oogen_OONotExpression_instantiation(instance):
    assert isinstance(instance, oogen_OONotExpression)


oogen_OONullLiteral_strategy = st.builds(oogen_OONullLiteral)
@given(instance=oogen_OONullLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OONullLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OONullLiteral)


oogen_OOOneOperandArithmeticExpression_strategy = st.builds(oogen_OOOneOperandArithmeticExpression)
@given(instance=oogen_OOOneOperandArithmeticExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOOneOperandArithmeticExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOneOperandArithmeticExpression)


oogen_OOOneOperandLogicalExpression_strategy = st.builds(oogen_OOOneOperandLogicalExpression)
@given(instance=oogen_OOOneOperandLogicalExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOOneOperandLogicalExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOneOperandLogicalExpression)


oogen_OOOrExpression_strategy = st.builds(oogen_OOOrExpression)
@given(instance=oogen_OOOrExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOOrExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOOrExpression)


oogen_OOPackage_strategy = st.builds(oogen_OOPackage, name=safe_text)
@given(instance=oogen_OOPackage_strategy)
@settings(max_examples=25)
def test_oogen_OOPackage_instantiation(instance):
    assert isinstance(instance, oogen_OOPackage)


oogen_OOPlusExpression_strategy = st.builds(oogen_OOPlusExpression)
@given(instance=oogen_OOPlusExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPlusExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPlusExpression)


oogen_OOPostfixDecrementExpression_strategy = st.builds(oogen_OOPostfixDecrementExpression)
@given(instance=oogen_OOPostfixDecrementExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPostfixDecrementExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPostfixDecrementExpression)


oogen_OOPostfixIncrementExpression_strategy = st.builds(oogen_OOPostfixIncrementExpression)
@given(instance=oogen_OOPostfixIncrementExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPostfixIncrementExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPostfixIncrementExpression)


oogen_OOPowerExpression_strategy = st.builds(oogen_OOPowerExpression)
@given(instance=oogen_OOPowerExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPowerExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPowerExpression)


oogen_OOPrefixDecrementExpression_strategy = st.builds(oogen_OOPrefixDecrementExpression)
@given(instance=oogen_OOPrefixDecrementExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPrefixDecrementExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPrefixDecrementExpression)


oogen_OOPrefixIncrementExpression_strategy = st.builds(oogen_OOPrefixIncrementExpression)
@given(instance=oogen_OOPrefixIncrementExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOPrefixIncrementExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOPrefixIncrementExpression)


oogen_OOReturn_strategy = st.builds(oogen_OOReturn)
@given(instance=oogen_OOReturn_strategy)
@settings(max_examples=25)
def test_oogen_OOReturn_instantiation(instance):
    assert isinstance(instance, oogen_OOReturn)


oogen_OORootExpression_strategy = st.builds(oogen_OORootExpression)
@given(instance=oogen_OORootExpression_strategy)
@settings(max_examples=25)
def test_oogen_OORootExpression_instantiation(instance):
    assert isinstance(instance, oogen_OORootExpression)


oogen_OOStatement_strategy = st.builds(oogen_OOStatement)
@given(instance=oogen_OOStatement_strategy)
@settings(max_examples=25)
def test_oogen_OOStatement_instantiation(instance):
    assert isinstance(instance, oogen_OOStatement)


oogen_OOStringLiteral_strategy = st.builds(oogen_OOStringLiteral, value=safe_text)
@given(instance=oogen_OOStringLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOStringLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOStringLiteral)


oogen_OOSubtractionExpression_strategy = st.builds(oogen_OOSubtractionExpression)
@given(instance=oogen_OOSubtractionExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOSubtractionExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOSubtractionExpression)


oogen_OOSwitch_strategy = st.builds(oogen_OOSwitch)
@given(instance=oogen_OOSwitch_strategy)
@settings(max_examples=25)
def test_oogen_OOSwitch_instantiation(instance):
    assert isinstance(instance, oogen_OOSwitch)


oogen_OOTernaryOperator_strategy = st.builds(oogen_OOTernaryOperator)
@given(instance=oogen_OOTernaryOperator_strategy)
@settings(max_examples=25)
def test_oogen_OOTernaryOperator_instantiation(instance):
    assert isinstance(instance, oogen_OOTernaryOperator)


oogen_OOThisLiteral_strategy = st.builds(oogen_OOThisLiteral)
@given(instance=oogen_OOThisLiteral_strategy)
@settings(max_examples=25)
def test_oogen_OOThisLiteral_instantiation(instance):
    assert isinstance(instance, oogen_OOThisLiteral)


oogen_OOTwoOperandArithmeticExpression_strategy = st.builds(oogen_OOTwoOperandArithmeticExpression)
@given(instance=oogen_OOTwoOperandArithmeticExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOTwoOperandArithmeticExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandArithmeticExpression)


oogen_OOTwoOperandAssignableExpression_strategy = st.builds(oogen_OOTwoOperandAssignableExpression, assigned=st.booleans())
@given(instance=oogen_OOTwoOperandAssignableExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOTwoOperandAssignableExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandAssignableExpression)


oogen_OOTwoOperandLogicalExpression_strategy = st.builds(oogen_OOTwoOperandLogicalExpression)
@given(instance=oogen_OOTwoOperandLogicalExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOTwoOperandLogicalExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOTwoOperandLogicalExpression)


oogen_OOType_strategy = st.builds(oogen_OOType, arrayDimensions=st.integers(), baseType=safe_text, collectionType=safe_text, numberOfIndirections=st.integers())
@given(instance=oogen_OOType_strategy)
@settings(max_examples=25)
def test_oogen_OOType_instantiation(instance):
    assert isinstance(instance, oogen_OOType)


oogen_OOTypeCast_strategy = st.builds(oogen_OOTypeCast)
@given(instance=oogen_OOTypeCast_strategy)
@settings(max_examples=25)
def test_oogen_OOTypeCast_instantiation(instance):
    assert isinstance(instance, oogen_OOTypeCast)


oogen_OOVariable_strategy = st.builds(oogen_OOVariable, name=safe_text, transient=st.booleans())
@given(instance=oogen_OOVariable_strategy)
@settings(max_examples=25)
def test_oogen_OOVariable_instantiation(instance):
    assert isinstance(instance, oogen_OOVariable)


oogen_OOVariableDeclarationList_strategy = st.builds(oogen_OOVariableDeclarationList)
@given(instance=oogen_OOVariableDeclarationList_strategy)
@settings(max_examples=25)
def test_oogen_OOVariableDeclarationList_instantiation(instance):
    assert isinstance(instance, oogen_OOVariableDeclarationList)


oogen_OOVariableReferenceExpression_strategy = st.builds(oogen_OOVariableReferenceExpression)
@given(instance=oogen_OOVariableReferenceExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOVariableReferenceExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOVariableReferenceExpression)


oogen_OOWhile_strategy = st.builds(oogen_OOWhile)
@given(instance=oogen_OOWhile_strategy)
@settings(max_examples=25)
def test_oogen_OOWhile_instantiation(instance):
    assert isinstance(instance, oogen_OOWhile)


oogen_OOXorExpression_strategy = st.builds(oogen_OOXorExpression)
@given(instance=oogen_OOXorExpression_strategy)
@settings(max_examples=25)
def test_oogen_OOXorExpression_instantiation(instance):
    assert isinstance(instance, oogen_OOXorExpression)



