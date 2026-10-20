from python_code import HAL_AbstractDepot

def test_HAL_AbstractDepot___init__():
    assert HAL_AbstractDepot.__init__(HAL_AbstractDepot(''), '') == None


from python_code import HAL_AffiliationType

def test_HAL_AffiliationType___init__():
    assert HAL_AffiliationType.__init__(HAL_AffiliationType('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import HAL_ArtOuvrageType
from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import ReferenceBiblioType

def test_HAL_ArtOuvrageType___init__():
    assert HAL_ArtOuvrageType.__init__(HAL_ArtOuvrageType('', '', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import HAL_ArtRevueType
from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import ReferenceBiblioType

def test_HAL_ArtRevueType___init__():
    assert HAL_ArtRevueType.__init__(HAL_ArtRevueType('\x00', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('\x00', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import AbstractDepot
from python_code import HAL_ArticleRetro

def test_HAL_ArticleRetro___init__():
    assert HAL_ArticleRetro.__init__(HAL_ArticleRetro('', HAL_ArticleRetro=AbstractDepot()), '\x00', HAL_ArticleRetro=AbstractDepot()) == None


from python_code import HAL_Auteur
from python_code import Laboratoire

def test_HAL_Auteur___init__():
    assert HAL_Auteur.__init__(HAL_Auteur('', '', '', '', '', HAL_Auteur=Laboratoire()), '', '', '', '', '', HAL_Auteur=Laboratoire()) == None


from python_code import HAL_AutreType
from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import ReferenceBiblioType

def test_HAL_AutreType___init__():
    assert HAL_AutreType.__init__(HAL_AutreType('', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '\x00', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import HAL_BrevetType
from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import ReferenceBiblioType

def test_HAL_BrevetType___init__():
    assert HAL_BrevetType.__init__(HAL_BrevetType('', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('\x00', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import HAL_Connexion

def test_HAL_Connexion___init__():
    assert HAL_Connexion.__init__(HAL_Connexion('', '\x00'), '\x00\x00', '') == None


from python_code import AbstractDepot
from python_code import HAL_ArticleRetro
from python_code import HAL_Depot
from python_code import HAL_DepotsType

def test_HAL_Depot___init__():
    assert HAL_Depot.__init__(HAL_Depot('', AbstractDepot=HAL_ArticleRetro('', HAL_ArticleRetro=AbstractDepot()), AbstractDepot20=HAL_DepotsType()), '', AbstractDepot=HAL_ArticleRetro('', HAL_ArticleRetro=AbstractDepot()), AbstractDepot20=HAL_DepotsType()) == None


from python_code import AbstractDepot
from python_code import HAL_ArticleRetro
from python_code import HAL_DepotWeb
from python_code import HAL_DepotsType

def test_HAL_DepotWeb___init__():
    assert HAL_DepotWeb.__init__(HAL_DepotWeb('', AbstractDepot=HAL_ArticleRetro('', HAL_ArticleRetro=AbstractDepot()), AbstractDepot20=HAL_DepotsType()), '', AbstractDepot=HAL_ArticleRetro('', HAL_ArticleRetro=AbstractDepot()), AbstractDepot20=HAL_DepotsType()) == None


from python_code import AbstractMetaLab
from python_code import HAL_Laboratoire

def test_HAL_Laboratoire___init__():
    assert HAL_Laboratoire.__init__(HAL_Laboratoire('', HAL_Laboratoire=AbstractMetaLab()), '\x00', HAL_Laboratoire=AbstractMetaLab()) == None


from python_code import HAL_MetaArtNoticeType
from python_code import ReferenceBiblioType

def test_HAL_MetaArtNoticeType___init__():
    assert HAL_MetaArtNoticeType.__init__(HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType()), '', '', HAL_MetaArtNoticeType=ReferenceBiblioType()) == None


from python_code import HAL_MetaArtType
from python_code import ReferenceBiblioType

def test_HAL_MetaArtType___init__():
    assert HAL_MetaArtType.__init__(HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), '\x00\x00', '', HAL_MetaArtType=ReferenceBiblioType()) == None


from python_code import AbstractMetaLab
from python_code import HAL_Laboratoire
from python_code import HAL_MetaLab

def test_HAL_MetaLab___init__():
    assert HAL_MetaLab.__init__(HAL_MetaLab('', AbstractMetaLab=HAL_Laboratoire('', HAL_Laboratoire=AbstractMetaLab())), '', AbstractMetaLab=HAL_Laboratoire('', HAL_Laboratoire=AbstractMetaLab())) == None


from python_code import HAL_MetaType

def test_HAL_MetaType___init__():
    assert HAL_MetaType.__init__(HAL_MetaType('', '', '', '', '', '', '', '', '\x00', '', '', '', ''), '', '', '', '', '', '', '', '', '', '', '', '\x00', '') == None


from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import HAL_OuvrageType
from python_code import ReferenceBiblioType

def test_HAL_OuvrageType___init__():
    assert HAL_OuvrageType.__init__(HAL_OuvrageType('', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import HAL_TamponType

def test_HAL_TamponType___init__():
    assert HAL_TamponType.__init__(HAL_TamponType(''), '') == None


from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import HAL_TheseType
from python_code import ReferenceBiblioType

def test_HAL_TheseType___init__():
    assert HAL_TheseType.__init__(HAL_TheseType('\x00', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('\x00', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None


from python_code import HAL_WebLink
from python_code import Server

def test_HAL_WebLink___init__():
    assert HAL_WebLink.__init__(HAL_WebLink('', HAL_WebLink=Server()), '', HAL_WebLink=Server()) == None


from python_code import HAL_MetaArtNoticeType
from python_code import HAL_MetaArtType
from python_code import HAL_WorkshopType
from python_code import ReferenceBiblioType

def test_HAL_WorkshopType___init__():
    assert HAL_WorkshopType.__init__(HAL_WorkshopType('', '', '', '', '\x00', '', '', '', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '', HAL_MetaArtNoticeType=ReferenceBiblioType())), '', '', '', '\x00', '\x00', '', '', '\x00', '', ReferenceBiblioType=HAL_MetaArtType('', '', HAL_MetaArtType=ReferenceBiblioType()), ReferenceBiblioType12=HAL_MetaArtNoticeType('', '\x00', HAL_MetaArtNoticeType=ReferenceBiblioType())) == None

