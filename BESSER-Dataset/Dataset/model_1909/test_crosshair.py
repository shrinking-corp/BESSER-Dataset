from python_code import preprocess_commons_LibraryElement

def test_preprocess_commons_LibraryElement___init__():
    assert preprocess_commons_LibraryElement.__init__(preprocess_commons_LibraryElement(''), '') == None


from python_code import preprocess_commons_NamedElement

def test_preprocess_commons_NamedElement___init__():
    assert preprocess_commons_NamedElement.__init__(preprocess_commons_NamedElement(''), '') == None


from python_code import CobolWord
from python_code import DataSegment
from python_code import ProcedureSegment
from python_code import preprocess_containers_PreprocessingUnit

def test_preprocess_containers_PreprocessingUnit___init__():
    assert preprocess_containers_PreprocessingUnit.__init__(preprocess_containers_PreprocessingUnit('', preprocess_containers_PreprocessingUnit=set(), preprocess_containers_PreprocessingUnit2=CobolWord(), preprocess_containers_PreprocessingUnit4=DataSegment(), preprocess_containers_PreprocessingUnit6=ProcedureSegment()), '', preprocess_containers_PreprocessingUnit=set(), preprocess_containers_PreprocessingUnit2=CobolWord(), preprocess_containers_PreprocessingUnit4=DataSegment(), preprocess_containers_PreprocessingUnit6=ProcedureSegment()) == None


from python_code import CobolSourceFormat
from python_code import preprocess_layouts_CobolLine

def test_preprocess_layouts_CobolLine___init__():
    assert preprocess_layouts_CobolLine.__init__(preprocess_layouts_CobolLine('', '', '', '', '', preprocess_layouts_CobolLine=CobolSourceFormat()), '', '', '', '', '', preprocess_layouts_CobolLine=CobolSourceFormat()) == None


from python_code import preprocess_layouts_CobolSourceFormat

def test_preprocess_layouts_CobolSourceFormat___init__():
    assert preprocess_layouts_CobolSourceFormat.__init__(preprocess_layouts_CobolSourceFormat('\x00\x00', '', '', True), '', '', '', False) == None


from python_code import preprocess_literals_AllLiteral
from python_code import preprocess_literals_AlphanumericLiteral

def test_preprocess_literals_AlphanumericLiteral___init__():
    assert preprocess_literals_AlphanumericLiteral.__init__(preprocess_literals_AlphanumericLiteral('', Literal=preprocess_literals_AllLiteral()), '', Literal=preprocess_literals_AllLiteral()) == None


from python_code import preprocess_literals_AllLiteral
from python_code import preprocess_literals_NumericLiteral

def test_preprocess_literals_NumericLiteral___init__():
    assert preprocess_literals_NumericLiteral.__init__(preprocess_literals_NumericLiteral('', Literal=preprocess_literals_AllLiteral()), '', Literal=preprocess_literals_AllLiteral()) == None


from python_code import preprocess_literals_AllLiteral
from python_code import preprocess_literals_PseudoLiteral

def test_preprocess_literals_PseudoLiteral___init__():
    assert preprocess_literals_PseudoLiteral.__init__(preprocess_literals_PseudoLiteral('', Literal=preprocess_literals_AllLiteral()), '', Literal=preprocess_literals_AllLiteral()) == None


from python_code import preprocess_operands_CobolWord

def test_preprocess_operands_CobolWord___init__():
    assert preprocess_operands_CobolWord.__init__(preprocess_operands_CobolWord(''), '') == None


from python_code import preprocess_sentences_CopySentence

def test_preprocess_sentences_CopySentence___init__():
    assert preprocess_sentences_CopySentence.__init__(preprocess_sentences_CopySentence(True), False) == None


from python_code import preprocess_containers_CopyUnit
from python_code import preprocess_sentences_ReplaceSentence

def test_preprocess_sentences_ReplaceSentence___init__():
    assert preprocess_sentences_ReplaceSentence.__init__(preprocess_sentences_ReplaceSentence(True, PreprocessingSentence=preprocess_containers_CopyUnit()), False, PreprocessingSentence=preprocess_containers_CopyUnit()) == None


from python_code import preprocess_statements_Execute

def test_preprocess_statements_Execute___init__():
    assert preprocess_statements_Execute.__init__(preprocess_statements_Execute(''), '') == None

