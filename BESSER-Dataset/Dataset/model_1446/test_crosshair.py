from python_code import GraphWiki_Graph

def test_GraphWiki_Graph___init__():
    assert GraphWiki_Graph.__init__(GraphWiki_Graph('', GraphWiki_Graph=set(), GraphWiki_Graph16=set()), '', GraphWiki_Graph=set(), GraphWiki_Graph16=set()) == None


from python_code import GraphWiki_ArticleGraph
from python_code import GraphWiki_CategoryGraph
from python_code import GraphWiki_ClassificationGraph
from python_code import GraphWiki_IndexGraph
from python_code import GraphWiki_Wiki

def test_GraphWiki_Wiki___init__():
    assert GraphWiki_Wiki.__init__(GraphWiki_Wiki('', GraphWiki_Wiki=GraphWiki_IndexGraph(), GraphWiki_Wiki2=GraphWiki_CategoryGraph(), GraphWiki_Wiki4=GraphWiki_ArticleGraph(), GraphWiki_Wiki6=GraphWiki_ClassificationGraph(), GraphWiki_Wiki8=set(), GraphWiki_Wiki10=set(), GraphWiki_Wiki12=set()), '', GraphWiki_Wiki=GraphWiki_IndexGraph(), GraphWiki_Wiki2=GraphWiki_CategoryGraph(), GraphWiki_Wiki4=GraphWiki_ArticleGraph(), GraphWiki_Wiki6=GraphWiki_ClassificationGraph(), GraphWiki_Wiki8=set(), GraphWiki_Wiki10=set(), GraphWiki_Wiki12=set()) == None

