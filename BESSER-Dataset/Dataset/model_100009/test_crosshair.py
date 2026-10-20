from python_code import bibtex_Article
from python_code import bibtex_Author
from python_code import bibtex_Book
from python_code import bibtex_Booklet
from python_code import bibtex_Conference
from python_code import bibtex_Incollection
from python_code import bibtex_Inproceedings
from python_code import bibtex_Manual
from python_code import bibtex_Mastersthesis
from python_code import bibtex_Misc
from python_code import bibtex_Phdthesis
from python_code import bibtex_Techreport
from python_code import bibtex_Unpublished

def test_bibtex_Author___init__():
    assert bibtex_Author.__init__(bibtex_Author('', bibtex_Author=bibtex_Article(), bibtex_Author25=bibtex_Book(), bibtex_Author38=bibtex_Booklet(), bibtex_Author45=bibtex_Conference(), bibtex_Author125=bibtex_Manual(), bibtex_Author143=bibtex_Misc(), bibtex_Author136=bibtex_Mastersthesis(), bibtex_Author148=bibtex_Phdthesis(), bibtex_Author167=bibtex_Techreport(), bibtex_Author179=bibtex_Unpublished(), bibtex_Author82=bibtex_Incollection(), bibtex_Author102=bibtex_Inproceedings()), '', bibtex_Author=bibtex_Article(), bibtex_Author25=bibtex_Book(), bibtex_Author38=bibtex_Booklet(), bibtex_Author45=bibtex_Conference(), bibtex_Author125=bibtex_Manual(), bibtex_Author143=bibtex_Misc(), bibtex_Author136=bibtex_Mastersthesis(), bibtex_Author148=bibtex_Phdthesis(), bibtex_Author167=bibtex_Techreport(), bibtex_Author179=bibtex_Unpublished(), bibtex_Author82=bibtex_Incollection(), bibtex_Author102=bibtex_Inproceedings()) == None


from python_code import bibtex_Booktitle
from python_code import bibtex_Conference
from python_code import bibtex_Incollection
from python_code import bibtex_Inproceedings

def test_bibtex_Booktitle___init__():
    assert bibtex_Booktitle.__init__(bibtex_Booktitle('', bibtex_Booktitle=bibtex_Conference(), bibtex_Booktitle85=bibtex_Incollection(), bibtex_Booktitle105=bibtex_Inproceedings()), '', bibtex_Booktitle=bibtex_Conference(), bibtex_Booktitle85=bibtex_Incollection(), bibtex_Booktitle105=bibtex_Inproceedings()) == None


from python_code import bibtex_BibType
from python_code import bibtex_CiteKey

def test_bibtex_CiteKey___init__():
    assert bibtex_CiteKey.__init__(bibtex_CiteKey('', bibtex_CiteKey=bibtex_BibType()), '', bibtex_CiteKey=bibtex_BibType()) == None


from python_code import bibtex_Crossref

def test_bibtex_Crossref___init__():
    assert bibtex_Crossref.__init__(bibtex_Crossref(''), '') == None


from python_code import bibtex_Book
from python_code import bibtex_Conference
from python_code import bibtex_Editor
from python_code import bibtex_Incollection
from python_code import bibtex_Inproceedings
from python_code import bibtex_Proceedings

def test_bibtex_Editor___init__():
    assert bibtex_Editor.__init__(bibtex_Editor('', bibtex_Editor=bibtex_Book(), bibtex_Editor50=bibtex_Conference(), bibtex_Editor156=bibtex_Proceedings(), bibtex_Editor88=bibtex_Incollection(), bibtex_Editor108=bibtex_Inproceedings()), '', bibtex_Editor=bibtex_Book(), bibtex_Editor50=bibtex_Conference(), bibtex_Editor156=bibtex_Proceedings(), bibtex_Editor88=bibtex_Incollection(), bibtex_Editor108=bibtex_Inproceedings()) == None


from python_code import bibtex_Booklet
from python_code import bibtex_Howpublished
from python_code import bibtex_Misc

def test_bibtex_Howpublished___init__():
    assert bibtex_Howpublished.__init__(bibtex_Howpublished('', bibtex_Howpublished=bibtex_Booklet(), bibtex_Howpublished146=bibtex_Misc()), '', bibtex_Howpublished=bibtex_Booklet(), bibtex_Howpublished146=bibtex_Misc()) == None


from python_code import bibtex_Institution
from python_code import bibtex_Techreport

def test_bibtex_Institution___init__():
    assert bibtex_Institution.__init__(bibtex_Institution('', bibtex_Institution=bibtex_Techreport()), '', bibtex_Institution=bibtex_Techreport()) == None


from python_code import bibtex_Article
from python_code import bibtex_Journal

def test_bibtex_Journal___init__():
    assert bibtex_Journal.__init__(bibtex_Journal('', bibtex_Journal=bibtex_Article()), '', bibtex_Journal=bibtex_Article()) == None


from python_code import bibtex_BibType
from python_code import bibtex_Key

def test_bibtex_Key___init__():
    assert bibtex_Key.__init__(bibtex_Key('', bibtex_Key=bibtex_BibType()), '', bibtex_Key=bibtex_BibType()) == None


from python_code import bibtex_BibType
from python_code import bibtex_Month

def test_bibtex_Month___init__():
    assert bibtex_Month.__init__(bibtex_Month('', bibtex_Month=bibtex_BibType()), '', bibtex_Month=bibtex_BibType()) == None


from python_code import bibtex_BibType
from python_code import bibtex_Note

def test_bibtex_Note___init__():
    assert bibtex_Note.__init__(bibtex_Note('', bibtex_Note=bibtex_BibType()), '', bibtex_Note=bibtex_BibType()) == None


from python_code import bibtex_Article
from python_code import bibtex_Number
from python_code import bibtex_Techreport

def test_bibtex_Number___init__():
    assert bibtex_Number.__init__(bibtex_Number('', bibtex_Number=bibtex_Article(), bibtex_Number174=bibtex_Techreport()), '', bibtex_Number=bibtex_Article(), bibtex_Number174=bibtex_Techreport()) == None


from python_code import bibtex_Conference
from python_code import bibtex_Incollection
from python_code import bibtex_Inproceedings
from python_code import bibtex_Manual
from python_code import bibtex_Organization
from python_code import bibtex_Proceedings

def test_bibtex_Organization___init__():
    assert bibtex_Organization.__init__(bibtex_Organization('', bibtex_Organization=bibtex_Conference(), bibtex_Organization117=bibtex_Inproceedings(), bibtex_Organization128=bibtex_Manual(), bibtex_Organization162=bibtex_Proceedings(), bibtex_Organization94=bibtex_Incollection()), '', bibtex_Organization=bibtex_Conference(), bibtex_Organization117=bibtex_Inproceedings(), bibtex_Organization128=bibtex_Manual(), bibtex_Organization162=bibtex_Proceedings(), bibtex_Organization94=bibtex_Incollection()) == None


from python_code import bibtex_Mastersthesis
from python_code import bibtex_Phdthesis
from python_code import bibtex_School

def test_bibtex_School___init__():
    assert bibtex_School.__init__(bibtex_School('', bibtex_School=bibtex_Mastersthesis(), bibtex_School151=bibtex_Phdthesis()), '', bibtex_School=bibtex_Mastersthesis(), bibtex_School151=bibtex_Phdthesis()) == None


from python_code import bibtex_BibType
from python_code import bibtex_Title

def test_bibtex_Title___init__():
    assert bibtex_Title.__init__(bibtex_Title('', bibtex_Title=bibtex_BibType()), '', bibtex_Title=bibtex_BibType()) == None


from python_code import bibtex_Techreport
from python_code import bibtex_Type

def test_bibtex_Type___init__():
    assert bibtex_Type.__init__(bibtex_Type('', bibtex_Type=bibtex_Techreport()), '', bibtex_Type=bibtex_Techreport()) == None


from python_code import bibtex_BibType
from python_code import bibtex_Year

def test_bibtex_Year___init__():
    assert bibtex_Year.__init__(bibtex_Year('', bibtex_Year=bibtex_BibType()), '', bibtex_Year=bibtex_BibType()) == None

