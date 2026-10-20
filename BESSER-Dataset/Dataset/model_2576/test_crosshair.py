from python_code import esper2Maude_ComparisonOperator
from python_code import esper2Maude_FilterOperator

def test_esper2Maude_ComparisonOperator___init__():
    assert esper2Maude_ComparisonOperator.__init__(esper2Maude_ComparisonOperator('', '', '', '', '', '', esper2Maude_ComparisonOperator=esper2Maude_FilterOperator()), '', '', '', '', '\x00', '', esper2Maude_ComparisonOperator=esper2Maude_FilterOperator()) == None


from python_code import esper2Maude_FilterEvent
from python_code import esper2Maude_FilterPart

def test_esper2Maude_FilterPart___init__():
    assert esper2Maude_FilterPart.__init__(esper2Maude_FilterPart('', '', '', 0, 0, '', '\x00', '', esper2Maude_FilterPart=esper2Maude_FilterEvent(), esper2Maude_FilterPart66=esper2Maude_FilterEvent()), '', '', '', 0, 0, '', '', '', esper2Maude_FilterPart=esper2Maude_FilterEvent(), esper2Maude_FilterPart66=esper2Maude_FilterEvent()) == None


from python_code import esper2Maude_FilterEvent
from python_code import esper2Maude_FilterOperator
from python_code import esper2Maude_FollowedBy
from python_code import esper2Maude_WhereFilter

def test_esper2Maude_WhereFilter___init__():
    assert esper2Maude_WhereFilter.__init__(esper2Maude_WhereFilter('', 0, esper2Maude_WhereFilter47=esper2Maude_FollowedBy(), esper2Maude_WhereFilter22=esper2Maude_FilterOperator(), esper2Maude_WhereFilter=esper2Maude_FilterEvent(), esper2Maude_WhereFilter20=esper2Maude_FilterOperator(), esper2Maude_WhereFilter25=esper2Maude_FilterEvent()), '', 0, esper2Maude_WhereFilter47=esper2Maude_FollowedBy(), esper2Maude_WhereFilter22=esper2Maude_FilterOperator(), esper2Maude_WhereFilter=esper2Maude_FilterEvent(), esper2Maude_WhereFilter20=esper2Maude_FilterOperator(), esper2Maude_WhereFilter25=esper2Maude_FilterEvent()) == None

