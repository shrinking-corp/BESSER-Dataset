from python_code import rules_RulesLattice

def test_rules_RulesLattice___init__():
    assert rules_RulesLattice.__init__(rules_RulesLattice('\x00\x00', '', rules_RulesLattice=set()), '', '', rules_RulesLattice=set()) == None

