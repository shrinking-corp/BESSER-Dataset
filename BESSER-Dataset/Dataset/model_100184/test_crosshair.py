from python_code import sparqlas_AnonymousIndividual

def test_sparqlas_AnonymousIndividual___init__():
    assert sparqlas_AnonymousIndividual.__init__(sparqlas_AnonymousIndividual(''), '') == None


from python_code import sparqlas_DataExactCardinality
from python_code import sparqlas_DataPropertyExpression
from python_code import sparqlas_DataRange

def test_sparqlas_DataExactCardinality___init__():
    assert sparqlas_DataExactCardinality.__init__(sparqlas_DataExactCardinality(0, sparqlas_DataExactCardinality=sparqlas_DataRange(), sparqlas_DataExactCardinality146=sparqlas_DataPropertyExpression()), 0, sparqlas_DataExactCardinality=sparqlas_DataRange(), sparqlas_DataExactCardinality146=sparqlas_DataPropertyExpression()) == None


from python_code import sparqlas_DataMaxCardinality
from python_code import sparqlas_DataPropertyExpression
from python_code import sparqlas_DataRange

def test_sparqlas_DataMaxCardinality___init__():
    assert sparqlas_DataMaxCardinality.__init__(sparqlas_DataMaxCardinality(0, sparqlas_DataMaxCardinality=sparqlas_DataRange(), sparqlas_DataMaxCardinality141=sparqlas_DataPropertyExpression()), 0, sparqlas_DataMaxCardinality=sparqlas_DataRange(), sparqlas_DataMaxCardinality141=sparqlas_DataPropertyExpression()) == None


from python_code import sparqlas_DataMinCardinality
from python_code import sparqlas_DataPropertyExpression
from python_code import sparqlas_DataRange

def test_sparqlas_DataMinCardinality___init__():
    assert sparqlas_DataMinCardinality.__init__(sparqlas_DataMinCardinality(0, sparqlas_DataMinCardinality136=sparqlas_DataPropertyExpression(), sparqlas_DataMinCardinality=sparqlas_DataRange()), 0, sparqlas_DataMinCardinality136=sparqlas_DataPropertyExpression(), sparqlas_DataMinCardinality=sparqlas_DataRange()) == None


from python_code import sparqlas_Constant
from python_code import sparqlas_DescribeQuery
from python_code import sparqlas_FacetRestriction
from python_code import sparqlas_IRI
from python_code import sparqlas_Import
from python_code import sparqlas_OntologyDocument

def test_sparqlas_IRI___init__():
    assert sparqlas_IRI.__init__(sparqlas_IRI('', sparqlas_IRI=sparqlas_OntologyDocument(), sparqlas_IRI23=sparqlas_DescribeQuery(), sparqlas_IRI9=sparqlas_Import(), sparqlas_IRI28=sparqlas_Constant(), sparqlas_IRI162=sparqlas_FacetRestriction()), '', sparqlas_IRI=sparqlas_OntologyDocument(), sparqlas_IRI23=sparqlas_DescribeQuery(), sparqlas_IRI9=sparqlas_Import(), sparqlas_IRI28=sparqlas_Constant(), sparqlas_IRI162=sparqlas_FacetRestriction()) == None


from python_code import sparqlas_Datatype
from python_code import sparqlas_Literal

def test_sparqlas_Literal___init__():
    assert sparqlas_Literal.__init__(sparqlas_Literal('', sparqlas_Literal=sparqlas_Datatype()), '', sparqlas_Literal=sparqlas_Datatype()) == None


from python_code import sparqlas_ClassExpression
from python_code import sparqlas_ObjectExactCardinality
from python_code import sparqlas_ObjectPropertyExpression

def test_sparqlas_ObjectExactCardinality___init__():
    assert sparqlas_ObjectExactCardinality.__init__(sparqlas_ObjectExactCardinality(0, sparqlas_ObjectExactCardinality=sparqlas_ClassExpression(), sparqlas_ObjectExactCardinality117=sparqlas_ObjectPropertyExpression()), 0, sparqlas_ObjectExactCardinality=sparqlas_ClassExpression(), sparqlas_ObjectExactCardinality117=sparqlas_ObjectPropertyExpression()) == None


from python_code import sparqlas_ClassExpression
from python_code import sparqlas_ObjectMaxCardinality
from python_code import sparqlas_ObjectPropertyExpression

def test_sparqlas_ObjectMaxCardinality___init__():
    assert sparqlas_ObjectMaxCardinality.__init__(sparqlas_ObjectMaxCardinality(0, sparqlas_ObjectMaxCardinality=sparqlas_ClassExpression(), sparqlas_ObjectMaxCardinality112=sparqlas_ObjectPropertyExpression()), 0, sparqlas_ObjectMaxCardinality=sparqlas_ClassExpression(), sparqlas_ObjectMaxCardinality112=sparqlas_ObjectPropertyExpression()) == None


from python_code import sparqlas_ClassExpression
from python_code import sparqlas_ObjectMinCardinality
from python_code import sparqlas_ObjectPropertyExpression

def test_sparqlas_ObjectMinCardinality___init__():
    assert sparqlas_ObjectMinCardinality.__init__(sparqlas_ObjectMinCardinality(0, sparqlas_ObjectMinCardinality107=sparqlas_ObjectPropertyExpression(), sparqlas_ObjectMinCardinality=sparqlas_ClassExpression()), 0, sparqlas_ObjectMinCardinality107=sparqlas_ObjectPropertyExpression(), sparqlas_ObjectMinCardinality=sparqlas_ClassExpression()) == None


from python_code import sparqlas_FullIRI
from python_code import sparqlas_OntologyDocument
from python_code import sparqlas_PrefixDefinition

def test_sparqlas_PrefixDefinition___init__():
    assert sparqlas_PrefixDefinition.__init__(sparqlas_PrefixDefinition('', sparqlas_PrefixDefinition=sparqlas_OntologyDocument(), sparqlas_PrefixDefinition11=sparqlas_FullIRI()), '', sparqlas_PrefixDefinition=sparqlas_OntologyDocument(), sparqlas_PrefixDefinition11=sparqlas_FullIRI()) == None


from python_code import sparqlas_SelectQuery
from python_code import sparqlas_Variable

def test_sparqlas_Variable___init__():
    assert sparqlas_Variable.__init__(sparqlas_Variable('', sparqlas_Variable=sparqlas_SelectQuery()), '', sparqlas_Variable=sparqlas_SelectQuery()) == None

