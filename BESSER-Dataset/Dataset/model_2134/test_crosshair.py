from python_code import architecture_ArchitectureFile

def test_architecture_ArchitectureFile___init__():
    assert architecture_ArchitectureFile.__init__(architecture_ArchitectureFile(''), '') == None


from python_code import architecture_ReferenceDependency

def test_architecture_ReferenceDependency___init__():
    assert architecture_ReferenceDependency.__init__(architecture_ReferenceDependency('', '\x00'), '\x00\x00', '') == None


from python_code import architecture_Type

def test_architecture_Type___init__():
    assert architecture_Type.__init__(architecture_Type('', False, False), '\x00', False, False) == None


from python_code import architecture_extension_ExtensionRelationship

def test_architecture_extension_ExtensionRelationship___init__():
    assert architecture_extension_ExtensionRelationship.__init__(architecture_extension_ExtensionRelationship()) == None

def test_architecture_extension_ExtensionRelationship_checkConstraint():
    assert architecture_extension_ExtensionRelationship.checkConstraint(architecture_extension_ExtensionRelationship()) == None


from python_code import architecture_extension_PatternRelationship

def test_architecture_extension_PatternRelationship___init__():
    assert architecture_extension_PatternRelationship.__init__(architecture_extension_PatternRelationship(''), '') == None

def test_architecture_extension_PatternRelationship_getTarget():
    assert architecture_extension_PatternRelationship.getTarget(architecture_extension_PatternRelationship('')) == None

def test_architecture_extension_PatternRelationship_checkConstraint():
    assert architecture_extension_PatternRelationship.checkConstraint(architecture_extension_PatternRelationship('')) == None

def test_architecture_extension_PatternRelationship_getSource():
    assert architecture_extension_PatternRelationship.getSource(architecture_extension_PatternRelationship('')) == None


from python_code import architecture_extension_RelationshipConstraint

def test_architecture_extension_RelationshipConstraint___init__():
    assert architecture_extension_RelationshipConstraint.__init__(architecture_extension_RelationshipConstraint()) == None

def test_architecture_extension_RelationshipConstraint_check():
    assert architecture_extension_RelationshipConstraint.check(architecture_extension_RelationshipConstraint(), '') == None


from python_code import architecture_extension_Role

def test_architecture_extension_Role___init__():
    assert architecture_extension_Role.__init__(architecture_extension_Role(''), '') == None


from python_code import architecture_extension_RoleRelationship

def test_architecture_extension_RoleRelationship___init__():
    assert architecture_extension_RoleRelationship.__init__(architecture_extension_RoleRelationship()) == None

def test_architecture_extension_RoleRelationship_getTarget():
    assert architecture_extension_RoleRelationship.getTarget(architecture_extension_RoleRelationship()) == None

def test_architecture_extension_RoleRelationship_checkConstraint():
    assert architecture_extension_RoleRelationship.checkConstraint(architecture_extension_RoleRelationship()) == None

