from python_code import wiki_Graph

def test_wiki_Graph___init__():
    assert wiki_Graph.__init__(wiki_Graph('', wiki_Graph=set(), wiki_Graph16=set()), '', wiki_Graph=set(), wiki_Graph16=set()) == None


from python_code import wiki_ArticleGraph
from python_code import wiki_CategoryGraph
from python_code import wiki_ClassificationGraph
from python_code import wiki_IndexGraph
from python_code import wiki_Wiki

def test_wiki_Wiki___init__():
    assert wiki_Wiki.__init__(wiki_Wiki('', wiki_Wiki=wiki_IndexGraph(), wiki_Wiki2=wiki_CategoryGraph(), wiki_Wiki4=wiki_ArticleGraph(), wiki_Wiki6=wiki_ClassificationGraph(), wiki_Wiki8=set(), wiki_Wiki10=set(), wiki_Wiki12=set()), '', wiki_Wiki=wiki_IndexGraph(), wiki_Wiki2=wiki_CategoryGraph(), wiki_Wiki4=wiki_ArticleGraph(), wiki_Wiki6=wiki_ClassificationGraph(), wiki_Wiki8=set(), wiki_Wiki10=set(), wiki_Wiki12=set()) == None

