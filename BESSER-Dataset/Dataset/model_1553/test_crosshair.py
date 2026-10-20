from python_code import model_R4ECommentType

def test_model_R4ECommentType___init__():
    assert model_R4ECommentType.__init__(model_R4ECommentType(''), '') == None


from python_code import model_R4EContent
from python_code import model_R4EDelta
from python_code import model_R4EPosition

def test_model_R4EContent___init__():
    assert model_R4EContent.__init__(model_R4EContent('', model_R4EContent=model_R4EDelta(), model_R4EContent64=model_R4EDelta(), model_R4EContent69=model_R4EPosition()), '', model_R4EContent=model_R4EDelta(), model_R4EContent64=model_R4EDelta(), model_R4EContent69=model_R4EPosition()) == None


from python_code import model_R4EFormalReview
from python_code import model_R4EParticipant

def test_model_R4EParticipant___init__():
    assert model_R4EParticipant.__init__(model_R4EParticipant('', '', False, model_R4EParticipant=model_R4EFormalReview(), model_R4EParticipant36=set(), model_R4EParticipant38=set()), '', '', False, model_R4EParticipant=model_R4EFormalReview(), model_R4EParticipant36=set(), model_R4EParticipant38=set()) == None


from python_code import model_R4EReviewComponent

def test_model_R4EReviewComponent___init__():
    assert model_R4EReviewComponent.__init__(model_R4EReviewComponent(''), '') == None


import datetime as _ch_datetime
from python_code import model_R4EFormalReview
from python_code import model_R4EReviewPhaseInfo

def test_model_R4EReviewPhaseInfo___init__():
    assert model_R4EReviewPhaseInfo.__init__(model_R4EReviewPhaseInfo(_ch_datetime.date(1, 1, 1), '\x00', '\x00\x00', _ch_datetime.date(1, 1, 1), model_R4EReviewPhaseInfo=model_R4EFormalReview(), model_R4EReviewPhaseInfo27=model_R4EFormalReview()), _ch_datetime.date(1, 1, 1), '', '', _ch_datetime.date(1, 1, 1), model_R4EReviewPhaseInfo=model_R4EFormalReview(), model_R4EReviewPhaseInfo27=model_R4EFormalReview()) == None


from python_code import model_R4EReviewState

def test_model_R4EReviewState___init__():
    assert model_R4EReviewState.__init__(model_R4EReviewState(''), '') == None


from python_code import model_R4ETextContent

def test_model_R4ETextContent___init__():
    assert model_R4ETextContent.__init__(model_R4ETextContent(''), '') == None


from python_code import model_R4ETextPosition

def test_model_R4ETextPosition___init__():
    assert model_R4ETextPosition.__init__(model_R4ETextPosition(0, 0, 0, 0), 0, 0, 0, 0) == None

