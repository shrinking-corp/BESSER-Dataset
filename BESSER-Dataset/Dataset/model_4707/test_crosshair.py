from python_code import Type
from python_code import smif_constraints_GeneralizationConstraint

def test_smif_constraints_GeneralizationConstraint___init__():
    assert smif_constraints_GeneralizationConstraint.__init__(smif_constraints_GeneralizationConstraint('', hasSpecialization=Type(), hasGeneralization=Type()), '', hasSpecialization=Type(), hasGeneralization=Type()) == None


from python_code import Type
from python_code import smif_constraints_MultiplicityConstraint

def test_smif_constraints_MultiplicityConstraint___init__():
    assert smif_constraints_MultiplicityConstraint.__init__(smif_constraints_MultiplicityConstraint('\x00\x00', '', '', '', respectOf=set(), hasMultiplicity=Type()), '', '', '', '', respectOf=set(), hasMultiplicity=Type()) == None


from python_code import Type
from python_code import smif_constraints_PropertyTypeConstraint

def test_smif_constraints_PropertyTypeConstraint___init__():
    assert smif_constraints_PropertyTypeConstraint.__init__(smif_constraints_PropertyTypeConstraint('', propertiesOfType=Type()), '', propertiesOfType=Type()) == None


from python_code import smif_constraints_UniquenessConstraint

def test_smif_constraints_UniquenessConstraint___init__():
    assert smif_constraints_UniquenessConstraint.__init__(smif_constraints_UniquenessConstraint('', hasUniquenessConstraint=set()), '', hasUniquenessConstraint=set()) == None


from python_code import FunctionType
from python_code import smif_expressions_ExpressionNode
from python_code import smif_toplevel_Context
from python_code import smif_types_Type

def test_smif_expressions_ExpressionNode___init__():
    assert smif_expressions_ExpressionNode.__init__(smif_expressions_ExpressionNode('', '', evaluates=set(), implementedBy=FunctionType(), ExpressionContext=smif_types_Type(), ExpressionContext99=smif_toplevel_Context()), '', '', evaluates=set(), implementedBy=FunctionType(), ExpressionContext=smif_types_Type(), ExpressionContext99=smif_toplevel_Context()) == None


from python_code import smif_expressions_Traversal

def test_smif_expressions_Traversal___init__():
    assert smif_expressions_Traversal.__init__(smif_expressions_Traversal('\x00\x00', '', traversedBy=set()), '', '', traversedBy=set()) == None


from python_code import smif_identifiers_TextIdentifier
from python_code import smif_toplevel_IdentifiableEntity

def test_smif_identifiers_TextIdentifier___init__():
    assert smif_identifiers_TextIdentifier.__init__(smif_identifiers_TextIdentifier('', Identifier73=smif_toplevel_IdentifiableEntity(), Identifier=smif_toplevel_IdentifiableEntity()), '', Identifier73=smif_toplevel_IdentifiableEntity(), Identifier=smif_toplevel_IdentifiableEntity()) == None


from python_code import smif_mapping_ComputedFacade

def test_smif_mapping_ComputedFacade___init__():
    assert smif_mapping_ComputedFacade.__init__(smif_mapping_ComputedFacade()) == None

def test_smif_mapping_ComputedFacade_push():
    assert smif_mapping_ComputedFacade.push(smif_mapping_ComputedFacade()) == None

def test_smif_mapping_ComputedFacade_pull():
    assert smif_mapping_ComputedFacade.pull(smif_mapping_ComputedFacade()) == None


from python_code import PatternVariable
from python_code import smif_mapping_Mapping

def test_smif_mapping_Mapping___init__():
    assert smif_mapping_Mapping.__init__(smif_mapping_Mapping('', referenceMapping=PatternVariable(), concreteMapping=PatternVariable(), mapRuleOf=set()), '', referenceMapping=PatternVariable(), concreteMapping=PatternVariable(), mapRuleOf=set()) == None


from python_code import Mapping
from python_code import MatchEnd
from python_code import smif_constraints_Rule
from python_code import smif_mapping_MatchRule
from python_code import smif_toplevel_IdentifiableEntity

def test_smif_mapping_MatchRule___init__():
    assert smif_mapping_MatchRule.__init__(smif_mapping_MatchRule('', matchFrom=MatchEnd(), matchTo=MatchEnd(), hasMapRule=Mapping(), Rule=smif_constraints_Rule(), Rule78=smif_toplevel_IdentifiableEntity(), Rule51=smif_constraints_Rule()), '', matchFrom=MatchEnd(), matchTo=MatchEnd(), hasMapRule=Mapping(), Rule=smif_constraints_Rule(), Rule78=smif_toplevel_IdentifiableEntity(), Rule51=smif_constraints_Rule()) == None


from python_code import Type
from python_code import smif_mapping_RepresentationRule

def test_smif_mapping_RepresentationRule___init__():
    assert smif_mapping_RepresentationRule.__init__(smif_mapping_RepresentationRule('', representsRule=Type(), conceptRule=set()), '', representsRule=Type(), conceptRule=set()) == None


from python_code import IRIIdentifier
from python_code import IdentifiableEntity
from python_code import Term
from python_code import smif_metadata_Definition
from python_code import smif_toplevel_Context
from python_code import smif_toplevel_IdentifiableEntity

def test_smif_metadata_Definition___init__():
    assert smif_metadata_Definition.__init__(smif_metadata_Definition('', '', smif_metadata_Definition=IRIIdentifier(), smif_metadata_Definition185=Term(), definedBy=IdentifiableEntity(), Metadata=smif_toplevel_IdentifiableEntity()), '', '', smif_metadata_Definition=IRIIdentifier(), smif_metadata_Definition185=Term(), definedBy=smif_toplevel_Context(), Metadata=smif_toplevel_IdentifiableEntity()) == None


from python_code import smif_patterns_PartVariable

def test_smif_patterns_PartVariable___init__():
    assert smif_patterns_PartVariable.__init__(smif_patterns_PartVariable(''), '') == None


from python_code import Mapping
from python_code import Pattern
from python_code import smif_patterns_PatternVariable

def test_smif_patterns_PatternVariable___init__():
    assert smif_patterns_PatternVariable.__init__(smif_patterns_PatternVariable('', '', mapsVariable=set(), hasSubset=set(), excludes=set(), excludedBy=set(), referenceFocus=Mapping(), concreteFocus=Mapping(), ownsVariable=Pattern(), subsets=set()), '', '', mapsVariable=set(), hasSubset=set(), excludes=set(), excludedBy=set(), referenceFocus=Mapping(), concreteFocus=Mapping(), ownsVariable=Pattern(), subsets=set()) == None


from python_code import smif_values_ScalarQuantity

def test_smif_values_ScalarQuantity___init__():
    assert smif_values_ScalarQuantity.__init__(smif_values_ScalarQuantity(''), '') == None


from python_code import Definition
from python_code import SystemOfUnits
from python_code import smif_metadata_Statement
from python_code import smif_values_UnitType

def test_smif_values_UnitType___init__():
    assert smif_values_UnitType.__init__(smif_values_UnitType('', '', '\x00\x00', unitOfSystem=SystemOfUnits(), smif_values_UnitType=Definition(), ValueType173=smif_metadata_Statement(), ValueType=smif_metadata_Statement(), ValueType176=smif_metadata_Statement()), '', '', '', unitOfSystem=SystemOfUnits(), smif_values_UnitType=Definition(), ValueType173=smif_metadata_Statement(), ValueType=smif_metadata_Statement(), ValueType176=smif_metadata_Statement()) == None


from python_code import smif_values_UnitValue

def test_smif_values_UnitValue___init__():
    assert smif_values_UnitValue.__init__(smif_values_UnitValue(''), '') == None

