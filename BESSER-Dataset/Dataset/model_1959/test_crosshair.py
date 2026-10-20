from python_code import shadowrun_AbstaktWaffe
from python_code import shadowrun_Fertigkeit
from python_code import shadowrun_Konzentration
from python_code import shadowrun_Spezialisierung

def test_shadowrun_AbstaktWaffe___init__():
    assert shadowrun_AbstaktWaffe.__init__(shadowrun_AbstaktWaffe('', shadowrun_AbstaktWaffe22=shadowrun_Konzentration(), shadowrun_AbstaktWaffe24=shadowrun_Spezialisierung(), shadowrun_AbstaktWaffe=shadowrun_Fertigkeit()), '', shadowrun_AbstaktWaffe22=shadowrun_Konzentration(), shadowrun_AbstaktWaffe24=shadowrun_Spezialisierung(), shadowrun_AbstaktWaffe=shadowrun_Fertigkeit()) == None


from python_code import shadowrun_AbstractMagier

def test_shadowrun_AbstractMagier___init__():
    assert shadowrun_AbstractMagier.__init__(shadowrun_AbstractMagier(0, 0, 0), 0, 0, 0) == None


from python_code import shadowrun_AbstractMagischePaersona

def test_shadowrun_AbstractMagischePaersona___init__():
    assert shadowrun_AbstractMagischePaersona.__init__(shadowrun_AbstractMagischePaersona(0), 0) == None


from python_code import shadowrun_AbstrakRaumKoerper
from python_code import shadowrun_RaumKoordinate

def test_shadowrun_AbstrakRaumKoerper___init__():
    assert shadowrun_AbstrakRaumKoerper.__init__(shadowrun_AbstrakRaumKoerper(shadowrun_AbstrakRaumKoerper=shadowrun_RaumKoordinate()), shadowrun_AbstrakRaumKoerper=shadowrun_RaumKoordinate()) == None

def test_shadowrun_AbstrakRaumKoerper_ProcessWorldTick():
    assert shadowrun_AbstrakRaumKoerper.ProcessWorldTick(shadowrun_AbstrakRaumKoerper(shadowrun_AbstrakRaumKoerper=shadowrun_RaumKoordinate())) == None


from python_code import shadowrun_AbstrakteRuestung

def test_shadowrun_AbstrakteRuestung___init__():
    assert shadowrun_AbstrakteRuestung.__init__(shadowrun_AbstrakteRuestung(0, 0), 0, 0) == None


from python_code import shadowrun_AttributModifikatorWert
from python_code import shadowrun_EAttribute
from python_code import shadowrun_Modifizierbar

def test_shadowrun_AttributModifikatorWert___init__():
    assert shadowrun_AttributModifikatorWert.__init__(shadowrun_AttributModifikatorWert(0, shadowrun_AttributModifikatorWert=shadowrun_EAttribute(), mods=shadowrun_Modifizierbar(), AttributModifikatorWert=shadowrun_Modifizierbar()), 0, shadowrun_AttributModifikatorWert=shadowrun_EAttribute(), mods=shadowrun_Modifizierbar(), AttributModifikatorWert=shadowrun_Modifizierbar()) == None


from python_code import shadowrun_BaseMagischePersona

def test_shadowrun_BaseMagischePersona___init__():
    assert shadowrun_BaseMagischePersona.__init__(shadowrun_BaseMagischePersona(0), 0) == None


from python_code import shadowrun_Bemerkbar

def test_shadowrun_Bemerkbar___init__():
    assert shadowrun_Bemerkbar.__init__(shadowrun_Bemerkbar(0), 0) == None


from python_code import shadowrun_BerechneteAttribute

def test_shadowrun_BerechneteAttribute___init__():
    assert shadowrun_BerechneteAttribute.__init__(shadowrun_BerechneteAttribute(0, 0, 0), 0, 0, 0) == None


from python_code import shadowrun_Beschreibbar

def test_shadowrun_Beschreibbar___init__():
    assert shadowrun_Beschreibbar.__init__(shadowrun_Beschreibbar('', '', '\x00\x00'), '', '', '') == None


from python_code import shadowrun_BodyIndex

def test_shadowrun_BodyIndex___init__():
    assert shadowrun_BodyIndex.__init__(shadowrun_BodyIndex(0), 0) == None


from python_code import shadowrun_Essenz

def test_shadowrun_Essenz___init__():
    assert shadowrun_Essenz.__init__(shadowrun_Essenz(0), 0) == None


from python_code import shadowrun_FernkampfwaffenModifikatoren

def test_shadowrun_FernkampfwaffenModifikatoren___init__():
    assert shadowrun_FernkampfwaffenModifikatoren.__init__(shadowrun_FernkampfwaffenModifikatoren('', 0, False, False, 0), '', 0, False, False, 0) == None


from python_code import shadowrun_Feuerwaffe
from python_code import shadowrun_MunitionsBehealter

def test_shadowrun_Feuerwaffe___init__():
    assert shadowrun_Feuerwaffe.__init__(shadowrun_Feuerwaffe(0, '', '\x00\x00', shadowrun_Feuerwaffe=shadowrun_MunitionsBehealter()), 0, '', '', shadowrun_Feuerwaffe=shadowrun_MunitionsBehealter()) == None


from python_code import shadowrun_GegenstandStufen

def test_shadowrun_GegenstandStufen___init__():
    assert shadowrun_GegenstandStufen.__init__(shadowrun_GegenstandStufen(0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0) == None


from python_code import shadowrun_GeistigeAttribute

def test_shadowrun_GeistigeAttribute___init__():
    assert shadowrun_GeistigeAttribute.__init__(shadowrun_GeistigeAttribute(0, 0, 0), 0, 0, 0) == None


from python_code import shadowrun_GeldWert

def test_shadowrun_GeldWert___init__():
    assert shadowrun_GeldWert.__init__(shadowrun_GeldWert(0.0, '', ''), 0.0, '', '') == None


from python_code import shadowrun_Granate

def test_shadowrun_Granate___init__():
    assert shadowrun_Granate.__init__(shadowrun_Granate('', '\x00'), '\x00\x00', '') == None


from python_code import shadowrun_KoerperlicheAtribute

def test_shadowrun_KoerperlicheAtribute___init__():
    assert shadowrun_KoerperlicheAtribute.__init__(shadowrun_KoerperlicheAtribute(0, 0, 0), 0, 0, 0) == None


from python_code import shadowrun_Legalitaet

def test_shadowrun_Legalitaet___init__():
    assert shadowrun_Legalitaet.__init__(shadowrun_Legalitaet(''), '') == None


from python_code import shadowrun_ModifikatorList

def test_shadowrun_ModifikatorList___init__():
    assert shadowrun_ModifikatorList.__init__(shadowrun_ModifikatorList('', shadowrun_ModifikatorList=set()), '', shadowrun_ModifikatorList=set()) == None


from python_code import shadowrun_NahkampfReichweite

def test_shadowrun_NahkampfReichweite___init__():
    assert shadowrun_NahkampfReichweite.__init__(shadowrun_NahkampfReichweite(0), 0) == None


from python_code import shadowrun_PersonaKoerper

def test_shadowrun_PersonaKoerper___init__():
    assert shadowrun_PersonaKoerper.__init__(shadowrun_PersonaKoerper(0), 0) == None


from python_code import shadowrun_Schadenswiederstand

def test_shadowrun_Schadenswiederstand___init__():
    assert shadowrun_Schadenswiederstand.__init__(shadowrun_Schadenswiederstand(0, 0), 0, 0) == None


from python_code import shadowrun_Sichtverhaeltnisse

def test_shadowrun_Sichtverhaeltnisse___init__():
    assert shadowrun_Sichtverhaeltnisse.__init__(shadowrun_Sichtverhaeltnisse('', '', '\x00\x00'), '', '', '') == None

