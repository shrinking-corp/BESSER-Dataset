from python_code import story_Catalog
from python_code import story_CatalogElement

def test_story_CatalogElement___init__():
    assert story_CatalogElement.__init__(story_CatalogElement('', '', '\x00\x00', story_CatalogElement=story_Catalog()), '', '', '', story_CatalogElement=story_Catalog()) == None

