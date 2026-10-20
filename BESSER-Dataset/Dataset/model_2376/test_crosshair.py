from python_code import relational_Column
from python_code import relational_ForeignKey
from python_code import relational_ReferenceConstraint
from python_code import relational_Table

def test_relational_Column___init__():
    assert relational_Column.__init__(relational_Column(False, '', 0, '', Column=relational_Table(), columns=relational_Table(), members=set(), referencedMembers=set(), Column30=relational_ReferenceConstraint(), Column36=relational_ForeignKey()), False, '', 0, '', Column=relational_Table(), columns=relational_Table(), members=set(), referencedMembers=set(), Column30=relational_ReferenceConstraint(), Column36=relational_ForeignKey()) == None


from python_code import relational_ENamedElement

def test_relational_ENamedElement___init__():
    assert relational_ENamedElement.__init__(relational_ENamedElement(''), '') == None


from python_code import relational_Schema
from python_code import relational_Table
from python_code import relational_Trigger

def test_relational_Trigger___init__():
    assert relational_Trigger.__init__(relational_Trigger(False, False, False, '', Trigger=relational_Schema(), triggers9=relational_Table(), triggersConstrainted=set(), Trigger16=relational_Table(), Trigger18=relational_Table(), triggers=relational_Schema()), False, False, False, '', Trigger=relational_Schema(), triggers9=relational_Table(), triggersConstrainted=set(), Trigger16=relational_Table(), Trigger18=relational_Table(), triggers=relational_Schema()) == None

