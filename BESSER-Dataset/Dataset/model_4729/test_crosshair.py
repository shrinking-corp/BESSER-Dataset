from python_code import prolog_AtomicNumber

def test_prolog_AtomicNumber___init__():
    assert prolog_AtomicNumber.__init__(prolog_AtomicNumber(0), 0) == None


from python_code import prolog_AtomicQuotedString

def test_prolog_AtomicQuotedString___init__():
    assert prolog_AtomicQuotedString.__init__(prolog_AtomicQuotedString(''), '') == None


from python_code import prolog_Comment

def test_prolog_Comment___init__():
    assert prolog_Comment.__init__(prolog_Comment(''), '') == None


from python_code import prolog_CompoundTerm
from python_code import prolog_Fact
from python_code import prolog_Rule

def test_prolog_CompoundTerm___init__():
    assert prolog_CompoundTerm.__init__(prolog_CompoundTerm('', prolog_CompoundTerm8=prolog_Fact(), prolog_CompoundTerm10=prolog_Rule(), prolog_CompoundTerm=set()), '\x00', prolog_CompoundTerm8=prolog_Fact(), prolog_CompoundTerm10=prolog_Rule(), prolog_CompoundTerm=set()) == None


from python_code import prolog_directives_Directive

def test_prolog_directives_Directive___init__():
    assert prolog_directives_Directive.__init__(prolog_directives_Directive('', prolog_directives_Directive=set()), '', prolog_directives_Directive=set()) == None


from python_code import prolog_directives_PredicateIndicator

def test_prolog_directives_PredicateIndicator___init__():
    assert prolog_directives_PredicateIndicator.__init__(prolog_directives_PredicateIndicator('', 0), '', 0) == None

