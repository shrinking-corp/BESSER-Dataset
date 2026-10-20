from python_code import ingest_Catalogue
from python_code import ingest_Database

def test_ingest_Database___init__():
    assert ingest_Database.__init__(ingest_Database('', '', '', '', '', ingest_Database=set(), ingest_Database10=ingest_Catalogue()), '', '', '', '\x00', '', ingest_Database=set(), ingest_Database10=ingest_Catalogue()) == None


from python_code import ingest_SqoopHiveImport

def test_ingest_SqoopHiveImport___init__():
    assert ingest_SqoopHiveImport.__init__(ingest_SqoopHiveImport('', '\x00'), '\x00\x00', '') == None

