from python_code import dsl_AnimtationActor

def test_dsl_AnimtationActor___init__():
    assert dsl_AnimtationActor.__init__(dsl_AnimtationActor('', '', '\x00\x00'), '', '', '') == None


from python_code import dsl_DamageEffect

def test_dsl_DamageEffect___init__():
    assert dsl_DamageEffect.__init__(dsl_DamageEffect(0), 0) == None


from python_code import dsl_PersistentEffect

def test_dsl_PersistentEffect___init__():
    assert dsl_PersistentEffect.__init__(dsl_PersistentEffect(0, '', '', dsl_PersistentEffect=set()), 0, '', '', dsl_PersistentEffect=set()) == None


from python_code import dsl_Model
from python_code import dsl_Turrent
from python_code import dsl_UnitWeaponLink

def test_dsl_Turrent___init__():
    assert dsl_Turrent.__init__(dsl_Turrent('', 0, 0, '', '', dsl_Turrent=dsl_Model(), dsl_Turrent39=dsl_UnitWeaponLink()), '', 0, 0, '', '', dsl_Turrent=dsl_Model(), dsl_Turrent39=dsl_UnitWeaponLink()) == None

