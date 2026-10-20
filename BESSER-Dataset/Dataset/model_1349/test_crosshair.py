from python_code import source_PathElementCS
from python_code import source_PathNameCS

def test_source_PathElementCS___init__():
    assert source_PathElementCS.__init__(source_PathElementCS('', PathElementCS=source_PathNameCS(), path=source_PathNameCS()), '', PathElementCS=source_PathNameCS(), path=source_PathNameCS()) == None

