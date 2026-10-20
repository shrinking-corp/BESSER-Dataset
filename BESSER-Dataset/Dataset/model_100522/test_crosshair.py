from python_code import Association
from python_code import Classifier
from python_code import Core_AssociationEnd
from python_code import Core_Namespace
from python_code import Multiplicity_

def test_Core_AssociationEnd___init__():
    assert Core_AssociationEnd.__init__(Core_AssociationEnd('', '', '\x00', '', '', Core_AssociationEnd74=Multiplicity_(), connection64=Association(), Core_AssociationEnd=set(), Core_AssociationEnd69=Classifier(), associationEnd=set(), ModelElement=Core_Namespace()), '', '', '', '', '', Core_AssociationEnd74=Multiplicity_(), connection64=Association(), Core_AssociationEnd=set(), Core_AssociationEnd69=Classifier(), associationEnd=set(), ModelElement=Core_Namespace()) == None


from python_code import Classifier
from python_code import Core_Feature
from python_code import Core_Namespace

def test_Core_Feature___init__():
    assert Core_Feature.__init__(Core_Feature('', feature=Classifier(), ModelElement=Core_Namespace()), '\x00', feature=Classifier(), ModelElement=Core_Namespace()) == None


from python_code import Core_GeneralizableElement
from python_code import Core_Namespace

def test_Core_GeneralizableElement___init__():
    assert Core_GeneralizableElement.__init__(Core_GeneralizableElement('', '', '', child=set(), ModelElement=Core_Namespace()), '', '', '', child=set(), ModelElement=Core_Namespace()) == None


from python_code import Classifier
from python_code import Core_Classifier
from python_code import Core_Generalization_

def test_Core_Generalization____init__():
    assert Core_Generalization_.__init__(Core_Generalization_('', Core_Generalization=Core_Classifier(), powertypeRange=Classifier(), generalization=Core_Classifier()), '', Core_Generalization=Core_Classifier(), powertypeRange=Classifier(), generalization=Core_Classifier()) == None


from python_code import Core_Classifier
from python_code import Core_ModelElement
from python_code import Namespace

def test_Core_ModelElement___init__():
    assert Core_ModelElement.__init__(Core_ModelElement('', '', '', ownedElement=Core_Classifier()), '', '', '', ownedElement=Namespace()) == None


from python_code import Classifier
from python_code import Core_Classifier
from python_code import Core_StructuralFeature
from python_code import Multiplicity_
from python_code import Use_Cases_Actor

def test_Core_StructuralFeature___init__():
    assert Core_StructuralFeature.__init__(Core_StructuralFeature('', '', '', Core_StructuralFeature=Use_Cases_Actor(), Core_StructuralFeature62=Multiplicity_(), Feature=Core_Classifier()), '', '', '', Core_StructuralFeature=Classifier(), Core_StructuralFeature62=Multiplicity_(), Feature=Core_Classifier()) == None


from python_code import Data_Types_Expression

def test_Data_Types_Expression___init__():
    assert Data_Types_Expression.__init__(Data_Types_Expression('', '\x00'), '\x00\x00', '') == None


from python_code import Data_Types_MultiplicityRange
from python_code import Multiplicity_

def test_Data_Types_MultiplicityRange___init__():
    assert Data_Types_MultiplicityRange.__init__(Data_Types_MultiplicityRange('', '\x00', range=Multiplicity_()), '\x00\x00', '', range=Multiplicity_()) == None


from python_code import Core_Namespace
from python_code import UseCase
from python_code import Use_Cases_ExtensionPoint

def test_Use_Cases_ExtensionPoint___init__():
    assert Use_Cases_ExtensionPoint.__init__(Use_Cases_ExtensionPoint('', extensionPoint=UseCase(), ModelElement=Core_Namespace()), '', extensionPoint=UseCase(), ModelElement=Core_Namespace()) == None

