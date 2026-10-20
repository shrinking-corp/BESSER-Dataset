from python_code import iec61131_Commentable

def test_iec61131_Commentable___init__():
    assert iec61131_Commentable.__init__(iec61131_Commentable(''), '') == None


from python_code import iec61131_NamedElement

def test_iec61131_NamedElement___init__():
    assert iec61131_NamedElement.__init__(iec61131_NamedElement(''), '') == None


from python_code import Access_Name
from python_code import Access_Path
from python_code import Non_Generic_Type_Name
from python_code import iec61131_configurations_Access_Declaration

def test_iec61131_configurations_Access_Declaration___init__():
    assert iec61131_configurations_Access_Declaration.__init__(iec61131_configurations_Access_Declaration('', iec61131_configurations_Access_Declaration=Access_Name(), iec61131_configurations_Access_Declaration337=Access_Path(), iec61131_configurations_Access_Declaration339=Non_Generic_Type_Name()), '', iec61131_configurations_Access_Declaration=Access_Name(), iec61131_configurations_Access_Declaration337=Access_Path(), iec61131_configurations_Access_Declaration339=Non_Generic_Type_Name()) == None


from python_code import iec61131_configurations_Access_Name

def test_iec61131_configurations_Access_Name___init__():
    assert iec61131_configurations_Access_Name.__init__(iec61131_configurations_Access_Name(''), '') == None


from python_code import Prog_Conf_Elements
from python_code import Program_Name
from python_code import Program_Type_Name
from python_code import Task_Name
from python_code import iec61131_configurations_Program_Configuration

def test_iec61131_configurations_Program_Configuration___init__():
    assert iec61131_configurations_Program_Configuration.__init__(iec61131_configurations_Program_Configuration(True, iec61131_configurations_Program_Configuration=Program_Name(), iec61131_configurations_Program_Configuration312=Task_Name(), iec61131_configurations_Program_Configuration315=Program_Type_Name(), iec61131_configurations_Program_Configuration318=Prog_Conf_Elements()), False, iec61131_configurations_Program_Configuration=Program_Name(), iec61131_configurations_Program_Configuration312=Task_Name(), iec61131_configurations_Program_Configuration315=Program_Type_Name(), iec61131_configurations_Program_Configuration318=Prog_Conf_Elements()) == None


from python_code import iec61131_configurations_Program_Name

def test_iec61131_configurations_Program_Name___init__():
    assert iec61131_configurations_Program_Name.__init__(iec61131_configurations_Program_Name(''), '') == None


from python_code import iec61131_configurations_Resource_Name

def test_iec61131_configurations_Resource_Name___init__():
    assert iec61131_configurations_Resource_Name.__init__(iec61131_configurations_Resource_Name(''), '') == None


from python_code import iec61131_configurations_Task_Name

def test_iec61131_configurations_Task_Name___init__():
    assert iec61131_configurations_Task_Name.__init__(iec61131_configurations_Task_Name(''), '') == None


from python_code import iec61131_il_Label

def test_iec61131_il_Label___init__():
    assert iec61131_il_Label.__init__(iec61131_il_Label(''), '') == None


from python_code import Bool_Type_Name
from python_code import Var1_List
from python_code import iec61131_interfaces_Edge_Declaration
from python_code import iec61131_interfaces_Input_Declarations

def test_iec61131_interfaces_Edge_Declaration___init__():
    assert iec61131_interfaces_Edge_Declaration.__init__(iec61131_interfaces_Edge_Declaration('\x00\x00', iec61131_interfaces_Edge_Declaration=Var1_List(), iec61131_interfaces_Edge_Declaration59=Bool_Type_Name(), Input_Declaration=iec61131_interfaces_Input_Declarations(True, iec61131_interfaces_Input_Declarations=set())), '', iec61131_interfaces_Edge_Declaration=Var1_List(), iec61131_interfaces_Edge_Declaration59=Bool_Type_Name(), Input_Declaration=iec61131_interfaces_Input_Declarations(False, iec61131_interfaces_Input_Declarations=set())) == None


from python_code import Enumerated_Type_Name
from python_code import iec61131_interfaces_Enumerated_Value

def test_iec61131_interfaces_Enumerated_Value___init__():
    assert iec61131_interfaces_Enumerated_Value.__init__(iec61131_interfaces_Enumerated_Value('', iec61131_interfaces_Enumerated_Value=Enumerated_Type_Name()), '', iec61131_interfaces_Enumerated_Value=Enumerated_Type_Name()) == None


from python_code import iec61131_interfaces_External_Var_Declarations

def test_iec61131_interfaces_External_Var_Declarations___init__():
    assert iec61131_interfaces_External_Var_Declarations.__init__(iec61131_interfaces_External_Var_Declarations(False, iec61131_interfaces_External_Var_Declarations=set()), False, iec61131_interfaces_External_Var_Declarations=set()) == None


from python_code import iec61131_interfaces_Function_Var_Decl

def test_iec61131_interfaces_Function_Var_Decl___init__():
    assert iec61131_interfaces_Function_Var_Decl.__init__(iec61131_interfaces_Function_Var_Decl(False, iec61131_interfaces_Function_Var_Decl=set()), False, iec61131_interfaces_Function_Var_Decl=set()) == None


from python_code import iec61131_interfaces_Global_Var_Declarations

def test_iec61131_interfaces_Global_Var_Declarations___init__():
    assert iec61131_interfaces_Global_Var_Declarations.__init__(iec61131_interfaces_Global_Var_Declarations(False, False, iec61131_interfaces_Global_Var_Declarations=set()), False, False, iec61131_interfaces_Global_Var_Declarations=set()) == None


from python_code import iec61131_interfaces_Incompl_Located_Var_Declarations

def test_iec61131_interfaces_Incompl_Located_Var_Declarations___init__():
    assert iec61131_interfaces_Incompl_Located_Var_Declarations.__init__(iec61131_interfaces_Incompl_Located_Var_Declarations(False, iec61131_interfaces_Incompl_Located_Var_Declarations=set()), False, iec61131_interfaces_Incompl_Located_Var_Declarations=set()) == None


from python_code import iec61131_interfaces_Incompl_Location

def test_iec61131_interfaces_Incompl_Location___init__():
    assert iec61131_interfaces_Incompl_Location.__init__(iec61131_interfaces_Incompl_Location(''), '') == None


from python_code import iec61131_interfaces_Input_Declarations

def test_iec61131_interfaces_Input_Declarations___init__():
    assert iec61131_interfaces_Input_Declarations.__init__(iec61131_interfaces_Input_Declarations(False, iec61131_interfaces_Input_Declarations=set()), False, iec61131_interfaces_Input_Declarations=set()) == None


from python_code import iec61131_interfaces_Located_Var_Declarations
from python_code import iec61131_pous_Program_Declaration

def test_iec61131_interfaces_Located_Var_Declarations___init__():
    assert iec61131_interfaces_Located_Var_Declarations.__init__(iec61131_interfaces_Located_Var_Declarations(False, False, iec61131_interfaces_Located_Var_Declarations=set(), Program_Vars=iec61131_pous_Program_Declaration()), False, False, iec61131_interfaces_Located_Var_Declarations=set(), Program_Vars=iec61131_pous_Program_Declaration()) == None


from python_code import iec61131_interfaces_Output_Declarations

def test_iec61131_interfaces_Output_Declarations___init__():
    assert iec61131_interfaces_Output_Declarations.__init__(iec61131_interfaces_Output_Declarations(False, iec61131_interfaces_Output_Declarations=set()), False, iec61131_interfaces_Output_Declarations=set()) == None


from python_code import iec61131_interfaces_Structure_Element_Name

def test_iec61131_interfaces_Structure_Element_Name___init__():
    assert iec61131_interfaces_Structure_Element_Name.__init__(iec61131_interfaces_Structure_Element_Name(''), '') == None


from python_code import iec61131_interfaces_Subrange
from python_code import iec61131_st_Case_List

def test_iec61131_interfaces_Subrange___init__():
    assert iec61131_interfaces_Subrange.__init__(iec61131_interfaces_Subrange('', iec61131_interfaces_Subrange=set(), Case_List_Element=iec61131_st_Case_List()), '', iec61131_interfaces_Subrange=set(), Case_List_Element=iec61131_st_Case_List()) == None


from python_code import iec61131_interfaces_Var_Declarations

def test_iec61131_interfaces_Var_Declarations___init__():
    assert iec61131_interfaces_Var_Declarations.__init__(iec61131_interfaces_Var_Declarations(True), False) == None


from python_code import iec61131_interfaces_InitElement_Constant
from python_code import iec61131_interfaces_Simple_Spec_Init_Func
from python_code import iec61131_interfaces_Var_Name_Decl
from python_code import iec61131_literals_Boolean_Literal
from python_code import iec61131_st_Expression_Constant

def test_iec61131_literals_Boolean_Literal___init__():
    assert iec61131_literals_Boolean_Literal.__init__(iec61131_literals_Boolean_Literal('', Constant=iec61131_interfaces_InitElement_Constant(), Constant201=iec61131_interfaces_Var_Name_Decl(), Constant209=iec61131_interfaces_Simple_Spec_Init_Func(), Constant555=iec61131_st_Expression_Constant()), '', Constant=iec61131_interfaces_InitElement_Constant(), Constant201=iec61131_interfaces_Var_Name_Decl(), Constant209=iec61131_interfaces_Simple_Spec_Init_Func(), Constant555=iec61131_st_Expression_Constant()) == None


from python_code import iec61131_literals_Common_Character_Representation

def test_iec61131_literals_Common_Character_Representation___init__():
    assert iec61131_literals_Common_Character_Representation.__init__(iec61131_literals_Common_Character_Representation(''), '') == None


from python_code import iec61131_literals_Date_Literal

def test_iec61131_literals_Date_Literal___init__():
    assert iec61131_literals_Date_Literal.__init__(iec61131_literals_Date_Literal('', '', '\x00\x00'), '', '', '') == None


from python_code import Fixed_Point
from python_code import iec61131_literals_Daytime

def test_iec61131_literals_Daytime___init__():
    assert iec61131_literals_Daytime.__init__(iec61131_literals_Daytime('', '\x00', iec61131_literals_Daytime=Fixed_Point()), '\x00\x00', '', iec61131_literals_Daytime=Fixed_Point()) == None


from python_code import Common_Character_Representation
from python_code import iec61131_literals_Double_Byte_Character_Representation

def test_iec61131_literals_Double_Byte_Character_Representation___init__():
    assert iec61131_literals_Double_Byte_Character_Representation.__init__(iec61131_literals_Double_Byte_Character_Representation('', iec61131_literals_Double_Byte_Character_Representation=Common_Character_Representation()), '', iec61131_literals_Double_Byte_Character_Representation=Common_Character_Representation()) == None


from python_code import iec61131_literals_Fixed_Point
from python_code import iec61131_literals_Interval

def test_iec61131_literals_Fixed_Point___init__():
    assert iec61131_literals_Fixed_Point.__init__(iec61131_literals_Fixed_Point('', '\x00', Fixed_Point_Literal=iec61131_literals_Interval()), '\x00\x00', '', Fixed_Point_Literal=iec61131_literals_Interval()) == None


from python_code import iec61131_literals_Integer

def test_iec61131_literals_Integer___init__():
    assert iec61131_literals_Integer.__init__(iec61131_literals_Integer(''), '') == None


from python_code import Fixed_Point
from python_code import Real_Type_Name
from python_code import iec61131_literals_Real_Literal

def test_iec61131_literals_Real_Literal___init__():
    assert iec61131_literals_Real_Literal.__init__(iec61131_literals_Real_Literal('', False, iec61131_literals_Real_Literal=Real_Type_Name(), iec61131_literals_Real_Literal11=Fixed_Point()), '', False, iec61131_literals_Real_Literal=Real_Type_Name(), iec61131_literals_Real_Literal11=Fixed_Point()) == None


from python_code import iec61131_literals_Signed_Integer

def test_iec61131_literals_Signed_Integer___init__():
    assert iec61131_literals_Signed_Integer.__init__(iec61131_literals_Signed_Integer(True), False) == None


from python_code import Common_Character_Representation
from python_code import iec61131_literals_Single_Byte_Character_Representation

def test_iec61131_literals_Single_Byte_Character_Representation___init__():
    assert iec61131_literals_Single_Byte_Character_Representation.__init__(iec61131_literals_Single_Byte_Character_Representation('', iec61131_literals_Single_Byte_Character_Representation=Common_Character_Representation()), '', iec61131_literals_Single_Byte_Character_Representation=Common_Character_Representation()) == None


from python_code import iec61131_pous_Access_Name

def test_iec61131_pous_Access_Name___init__():
    assert iec61131_pous_Access_Name.__init__(iec61131_pous_Access_Name(''), '') == None


from python_code import iec61131_pous_Other_Language

def test_iec61131_pous_Other_Language___init__():
    assert iec61131_pous_Other_Language.__init__(iec61131_pous_Other_Language(''), '') == None


from python_code import Access_Name
from python_code import Non_Generic_Type_Name
from python_code import Symbolic_Variable
from python_code import iec61131_pous_Program_Access_Decl

def test_iec61131_pous_Program_Access_Decl___init__():
    assert iec61131_pous_Program_Access_Decl.__init__(iec61131_pous_Program_Access_Decl('', iec61131_pous_Program_Access_Decl=Access_Name(), iec61131_pous_Program_Access_Decl232=Non_Generic_Type_Name(), iec61131_pous_Program_Access_Decl235=Symbolic_Variable()), '', iec61131_pous_Program_Access_Decl=Access_Name(), iec61131_pous_Program_Access_Decl232=Non_Generic_Type_Name(), iec61131_pous_Program_Access_Decl235=Symbolic_Variable()) == None

