from python_code import imdb_db

def test_imdb_db___init__():
    assert imdb_db.__init__(imdb_db('', imdb_db=set(), imdb_db10=set(), imdb_db21=set(), imdb_db13=set(), imdb_db16=set(), imdb_db19=set()), '', imdb_db=set(), imdb_db10=set(), imdb_db21=set(), imdb_db13=set(), imdb_db16=set(), imdb_db19=set()) == None

def test_imdb_db_sam():
    assert imdb_db.sam(imdb_db('', imdb_db=set(), imdb_db10=set(), imdb_db21=set(), imdb_db13=set(), imdb_db16=set(), imdb_db19=set())) == None

