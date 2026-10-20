from python_code import publication_Article

def test_publication_Article___init__():
    assert publication_Article.__init__(publication_Article('', '\x00'), '\x00\x00', '') == None


from python_code import publication_BiblioReference
from python_code import publication_Content

def test_publication_Content___init__():
    assert publication_Content.__init__(publication_Content('', publication_Content=publication_BiblioReference(), publication_Content20=publication_BiblioReference()), '', publication_Content=publication_BiblioReference(), publication_Content20=publication_BiblioReference()) == None


from python_code import publication_BiblioReference
from python_code import publication_Contact
from python_code import publication_Indexing
from python_code import publication_LegalEntity
from python_code import publication_Ontology

def test_publication_Indexing___init__():
    assert publication_Indexing.__init__(publication_Indexing('', Indexing=publication_BiblioReference(), publication_Indexing29=set(), publication_Indexing32=set(), publication_Indexing=publication_Contact(), publication_Indexing24=publication_LegalEntity(), publication_Indexing27=publication_Ontology(), indexings=publication_BiblioReference()), '', Indexing=publication_BiblioReference(), publication_Indexing29=set(), publication_Indexing32=set(), publication_Indexing=publication_Contact(), publication_Indexing24=publication_LegalEntity(), publication_Indexing27=publication_Ontology(), indexings=publication_BiblioReference()) == None


from python_code import publication_Journal
from python_code import publication_SimpleOntologyTerm

def test_publication_Journal___init__():
    assert publication_Journal.__init__(publication_Journal('', publication_Journal=publication_SimpleOntologyTerm()), '', publication_Journal=publication_SimpleOntologyTerm()) == None


from python_code import publication_JournalArticle
from python_code import publication_JournalIssue

def test_publication_JournalIssue___init__():
    assert publication_JournalIssue.__init__(publication_JournalIssue('', '', '', journalIssue=set(), JournalIssue=publication_JournalArticle()), '', '', '', journalIssue=set(), JournalIssue=publication_JournalArticle()) == None


import datetime as _ch_datetime
from python_code import publication_BiblioReferenceSet
from python_code import publication_SimpleCitation

def test_publication_SimpleCitation___init__():
    assert publication_SimpleCitation.__init__(publication_SimpleCitation('', '\x00', _ch_datetime.date(1, 1, 3), publication_SimpleCitation=publication_BiblioReferenceSet()), '', '', _ch_datetime.date(1, 1, 1), publication_SimpleCitation=publication_BiblioReferenceSet()) == None


from python_code import publication_WebResource

def test_publication_WebResource___init__():
    assert publication_WebResource.__init__(publication_WebResource(''), '') == None

