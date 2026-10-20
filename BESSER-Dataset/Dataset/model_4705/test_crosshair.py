from python_code import terms_Declarations
from python_code import terms_TermsDeclaration

def test_terms_TermsDeclaration___init__():
    assert terms_TermsDeclaration.__init__(terms_TermsDeclaration('', '\x00', declaration=terms_Declarations(), TermsDeclaration=terms_Declarations()), '\x00\x00', '', declaration=terms_Declarations(), TermsDeclaration=terms_Declarations()) == None

