from python_code import source_PathElementCS
from python_code import source_PathNameCS

def test_source_PathElementCS___init__():
    assert source_PathElementCS.__init__(source_PathElementCS('', source_PathElementCS=source_PathNameCS()), '', source_PathElementCS=source_PathNameCS()) == None

