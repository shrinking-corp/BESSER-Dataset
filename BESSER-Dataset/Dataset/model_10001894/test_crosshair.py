from python_code import Action

def test_Action___init__():
    assert Action.__init__(Action(''), '') == None


from python_code import CastSpell
from python_code import Spell

def test_CastSpell___init__():
    assert CastSpell.__init__(CastSpell('', Spell()), '', Spell()) == None


from python_code import Dash

def test_Dash___init__():
    assert Dash.__init__(Dash(''), '') == None


from python_code import Dash2

def test_Dash2___init__():
    assert Dash2.__init__(Dash2(''), '') == None


from python_code import Weapon
from python_code import WeaponAttack

def test_WeaponAttack___init__():
    assert WeaponAttack.__init__(WeaponAttack('', Weapon()), '', Weapon()) == None

