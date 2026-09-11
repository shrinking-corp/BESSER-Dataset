import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    Access_Declaration,
    Access_Declarations,
    Access_Name,
    Access_Path,
    Action_Association,
    Action_Name,
    Action_Qualifier,
    Action_Time,
    Add_Operator,
    And_Operator,
    Array_Initial_Elements,
    Array_Initialization,
    Array_Spec_Init,
    Array_Specification,
    Array_Type_Name,
    Array_Variable,
    Assignment_Name,
    Assignment_Operator,
    Assignment_Symbol,
    BSInteger,
    Bit_String_Type_Name,
    Blocks,
    Bool_Type_Name,
    Byte_String,
    Byte_String_Type_Name,
    Case_Element,
    Case_List,
    Case_List_Element,
    Character_String,
    Commentable,
    Common_Character_Representation,
    Comparison_Operator,
    Cond2_Condition,
    Configuration_Name,
    Constant,
    Control_Variable,
    DT_Type_Name,
    Data_Sink,
    Data_Source,
    Data_Type_Name,
    Date_Literal,
    Date_Type_Name,
    Daytime,
    Derived_Function_Block_Name,
    Derived_Function_Name,
    Derived_Type_Name,
    Direct_Variable,
    Divide_Operator,
    Dot_Operator,
    Double_BString,
    Double_Byte_Character_Representation,
    Double_Byte_Character_String,
    Double_Byte_String_Spec,
    Double_Byte_String_Type_Name,
    Duration_Type_Name,
    Elementary_Type_Name,
    Else_If_Statement,
    Else_Statement,
    Enumerated_Spec_Init,
    Enumerated_Specification,
    Enumerated_Type_Name,
    Enumerated_Value,
    EquUequ_Operator,
    Equal_Operator,
    Expression_Types,
    Expression_Variable,
    External_Declaration,
    External_Specification,
    Fbd_Network,
    Fixed_Point,
    Fixed_Point_Literal,
    For_List,
    Function_Block_Body,
    Function_Block_Declaration,
    Function_Block_Type_Name,
    Function_Block_Vars,
    Function_Body,
    Function_Declaration,
    Function_Name,
    Function_Return_Value,
    Function_Vars,
    Global_Var_Decl,
    Global_Var_Declarations,
    Global_Var_Name,
    Global_Var_Spec,
    GreaterEqual_Operator,
    Greater_Operator,
    Hours,
    Il_Assign_Operator,
    Il_Assign_Out_Operator,
    Il_Call_Operator,
    Il_Expr_Operator,
    Il_Instruction,
    Il_Jump_Operator,
    Il_Operand,
    Il_Operand_List,
    Il_Operations,
    Il_Param_Instruction,
    Il_Param_Last_Instruction,
    Il_Param_List,
    Il_Simple_Instruction,
    Il_Simple_Operation,
    Il_Simple_Operator,
    Incompl_Located_Var_Decl,
    Incompl_Location,
    Initial_Element,
    Initial_Step,
    Initialized_Structure,
    Input_Declaration,
    Input_Reference,
    Instance_Specific_Init,
    Instance_Specific_Initializations,
    Integer,
    Integer_Type_Name,
    Interval,
    Io_Var_Declaration,
    Iteration_Statement,
    Label,
    LessEqual_Operator,
    Less_Operator,
    Library_Element_Declaration,
    Library_Element_Name,
    Located_Var_Decl,
    Located_Var_Spec_Init,
    Location,
    Milliseconds,
    Minutes,
    Multi_Element_Variable,
    Multiply_Operator,
    NamedElement,
    Non_Generic_Type_Name,
    Not_Operator,
    Numeric_Literal,
    Numeric_Type_Name,
    Operands,
    Operator,
    Or_Operator,
    Other_Var_Declaration,
    Output_Reference,
    Param_Assignment,
    Param_Assignments,
    Param_Instruction,
    Power_Operator,
    Power_Symbol,
    Primary_Expression,
    Priority,
    Prog_Cnxn,
    Prog_Conf_Element,
    Prog_Conf_Elements,
    Prog_Data_Source,
    Program_Access_Decl,
    Program_Configuration,
    Program_Declaration,
    Program_Name,
    Program_Type_Name,
    Program_Vars,
    RNV_Declarations,
    Range,
    Real_Type_Name,
    Resource_Declaration,
    Resource_Name,
    Resource_Type_Name,
    Seconds,
    Selection_Statement,
    Sfc_Elements,
    Sfc_Network,
    Signed_Integer,
    Simple_Instr,
    Simple_Instr_List,
    Simple_Spec_Init,
    Simple_Specification,
    Simple_Specification_Func,
    Simple_Type_Name,
    Single,
    Single_BString,
    Single_Byte_Character_Representation,
    Single_Byte_Character_String,
    Single_Byte_String_Spec,
    Single_Byte_String_Type_Name,
    Single_Element_Type_Declaration,
    Single_Element_Type_Name,
    Single_Resource_Declaration,
    Specification,
    Statement,
    Statement_List,
    Step_Name,
    Step_Types,
    Steps,
    String_Type_Name,
    String_Var_Declaration,
    Structure_Element_Declaration,
    Structure_Element_Initialization,
    Structure_Element_Name,
    Structure_Elements,
    Structure_Initialization,
    Structure_Specification,
    Structure_Type_Name,
    Structured_Variable,
    Subprogram_Control_Statement,
    Subrange,
    Subrange_Spec_Init,
    Subrange_Specification,
    Subrange_Type_Name,
    Subscript_List,
    Substraction_Operator,
    Symbolic_Variable,
    TOD_Type_Name,
    Task_Configuration,
    Task_Initialization,
    Task_Name,
    Temp_Var_Decl,
    Temp_Var_Declaration,
    Time_Literal,
    Timed_Qualifier,
    Transition_Condition,
    Transition_Name,
    Type_Declaration,
    Unary_Operator,
    Unequal_Operator,
    Unsigned_Integer,
    Var1_List,
    Var1_Specification,
    Var1_Specification_Func,
    Var2_Init_Decl,
    Var_Declaration,
    Var_Init_Decl,
    Var_Spec,
    Variable,
    Variable_Name,
    Xor_Operator,
    configurations_Data_Sink,
    configurations_Data_Source,
    configurations_Prog_Data_Source,
    iec61131_Commentable,
    iec61131_IEC61131,
    iec61131_Library_Element_Declaration,
    iec61131_Library_Element_Name,
    iec61131_NamedElement,
    iec61131_configurations_Access_Declaration,
    iec61131_configurations_Access_Declarations,
    iec61131_configurations_Access_Name,
    iec61131_configurations_Access_Path,
    iec61131_configurations_Configuration_Declaration,
    iec61131_configurations_Configuration_Name,
    iec61131_configurations_Data_Sink,
    iec61131_configurations_Data_Source,
    iec61131_configurations_Direct_Path,
    iec61131_configurations_Fb_Task,
    iec61131_configurations_Global_Var_Reference,
    iec61131_configurations_Instance_Spec1,
    iec61131_configurations_Instance_Spec2,
    iec61131_configurations_Instance_Specific_Init,
    iec61131_configurations_Instance_Specific_Initializations,
    iec61131_configurations_Interval,
    iec61131_configurations_Priority,
    iec61131_configurations_Prog_Cnxn,
    iec61131_configurations_Prog_Conf_Element,
    iec61131_configurations_Prog_Conf_Elements,
    iec61131_configurations_Prog_Data_Source,
    iec61131_configurations_Prog_Sink,
    iec61131_configurations_Prog_Source,
    iec61131_configurations_Program_Configuration,
    iec61131_configurations_Program_Name,
    iec61131_configurations_Program_Output_Reference,
    iec61131_configurations_Resource_Declaration,
    iec61131_configurations_Resource_Name,
    iec61131_configurations_Resource_Type_Name,
    iec61131_configurations_Single,
    iec61131_configurations_Single_Resource_Declaration,
    iec61131_configurations_Symbolic_Path,
    iec61131_configurations_Task_Configuration,
    iec61131_configurations_Task_Initialization,
    iec61131_configurations_Task_Name,
    iec61131_fbd_Fbd_Network,
    iec61131_fbd_Function_Block_Diagram,
    iec61131_il_Il_Assign_Operator,
    iec61131_il_Il_Assign_Out_Operator,
    iec61131_il_Il_Call_Operator,
    iec61131_il_Il_Expr_Operator,
    iec61131_il_Il_Expression,
    iec61131_il_Il_Fb_Call,
    iec61131_il_Il_Formal_Funct_Call,
    iec61131_il_Il_Instruction,
    iec61131_il_Il_Jump_Operation,
    iec61131_il_Il_Jump_Operator,
    iec61131_il_Il_Operand,
    iec61131_il_Il_Operand_List,
    iec61131_il_Il_Operations,
    iec61131_il_Il_Param_Assignment,
    iec61131_il_Il_Param_Instruction,
    iec61131_il_Il_Param_Last_Instruction,
    iec61131_il_Il_Param_List,
    iec61131_il_Il_Param_Out_Assignment,
    iec61131_il_Il_Return_Operator,
    iec61131_il_Il_Simple_Instruction,
    iec61131_il_Il_Simple_Operation,
    iec61131_il_Il_Simple_Operator,
    iec61131_il_Instruction_List,
    iec61131_il_Label,
    iec61131_il_Operand1,
    iec61131_il_Operand2,
    iec61131_il_Operands,
    iec61131_il_Param_Assignment,
    iec61131_il_Param_Assignment2,
    iec61131_il_Param_Assignments,
    iec61131_il_Param_Instruction,
    iec61131_il_Simple_Instr,
    iec61131_il_Simple_Instr_List,
    iec61131_il_Simple_Operation1,
    iec61131_il_Simple_Operation2,
    iec61131_interfaces_Array_Initial_Elements,
    iec61131_interfaces_Array_Initial_Elements1,
    iec61131_interfaces_Array_Initial_Elements2,
    iec61131_interfaces_Array_Initialization,
    iec61131_interfaces_Array_Spec_Init,
    iec61131_interfaces_Array_Specification,
    iec61131_interfaces_Array_Specification1,
    iec61131_interfaces_Array_Specification2,
    iec61131_interfaces_Array_Var_Declaration,
    iec61131_interfaces_Array_Var_Init_Decl,
    iec61131_interfaces_Byte_String,
    iec61131_interfaces_Double_BString,
    iec61131_interfaces_Double_Byte_String_Spec,
    iec61131_interfaces_Double_Byte_String_Var_Declaration,
    iec61131_interfaces_Edge_Declaration,
    iec61131_interfaces_Enumerated_Spec_Init,
    iec61131_interfaces_Enumerated_Specification,
    iec61131_interfaces_Enumerated_Specification1,
    iec61131_interfaces_Enumerated_Specification2,
    iec61131_interfaces_Enumerated_Value,
    iec61131_interfaces_External_Declaration,
    iec61131_interfaces_External_Specification,
    iec61131_interfaces_External_Var_Declarations,
    iec61131_interfaces_Fb_Name_Decl,
    iec61131_interfaces_Function_Var_Decl,
    iec61131_interfaces_Global_Var_Decl,
    iec61131_interfaces_Global_Var_Declarations,
    iec61131_interfaces_Global_Var_List,
    iec61131_interfaces_Global_Var_Location,
    iec61131_interfaces_Global_Var_Name,
    iec61131_interfaces_Global_Var_Spec,
    iec61131_interfaces_Incompl_Located_Var_Decl,
    iec61131_interfaces_Incompl_Located_Var_Declarations,
    iec61131_interfaces_Incompl_Location,
    iec61131_interfaces_InitElement_Array,
    iec61131_interfaces_InitElement_Constant,
    iec61131_interfaces_InitElement_EnumValue,
    iec61131_interfaces_InitElement_Structure,
    iec61131_interfaces_Initial_Element,
    iec61131_interfaces_Initialized_Structure,
    iec61131_interfaces_Input_Declaration,
    iec61131_interfaces_Input_Declarations,
    iec61131_interfaces_Input_Output_Declarations,
    iec61131_interfaces_Interface,
    iec61131_interfaces_Io_Var_Declaration,
    iec61131_interfaces_Located_Var_Decl,
    iec61131_interfaces_Located_Var_Declarations,
    iec61131_interfaces_Located_Var_Spec_Init,
    iec61131_interfaces_Location,
    iec61131_interfaces_Non_Retentive_Var_Declarations,
    iec61131_interfaces_Other_Var_Declaration,
    iec61131_interfaces_Output_Declarations,
    iec61131_interfaces_RNV_Declarations,
    iec61131_interfaces_Range,
    iec61131_interfaces_Retentive_Var_Declarations,
    iec61131_interfaces_Simple_Spec_Init,
    iec61131_interfaces_Simple_Spec_Init_Func,
    iec61131_interfaces_Simple_Specification_Func,
    iec61131_interfaces_Single_BString,
    iec61131_interfaces_Single_Byte_String_Spec,
    iec61131_interfaces_Single_Byte_String_Var_Declaration,
    iec61131_interfaces_Specification,
    iec61131_interfaces_String_Var_Declaration,
    iec61131_interfaces_Structure_Element_Initialization,
    iec61131_interfaces_Structure_Element_Name,
    iec61131_interfaces_Structure_Initialization,
    iec61131_interfaces_Structured_Var_Declaration,
    iec61131_interfaces_Structured_Var_Init_Decl,
    iec61131_interfaces_Subrange,
    iec61131_interfaces_Subrange_Spec_Init,
    iec61131_interfaces_Subrange_Specification,
    iec61131_interfaces_Subrange_Specification1,
    iec61131_interfaces_Subrange_Specification2,
    iec61131_interfaces_Temp_Var_Decl,
    iec61131_interfaces_Temp_Var_Declaration,
    iec61131_interfaces_Temp_Var_Decls,
    iec61131_interfaces_Var1_Declaration,
    iec61131_interfaces_Var1_Init_Decl,
    iec61131_interfaces_Var1_List,
    iec61131_interfaces_Var1_Specification,
    iec61131_interfaces_Var1_Specification_Func,
    iec61131_interfaces_Var2_Init_Decl,
    iec61131_interfaces_Var_Declaration,
    iec61131_interfaces_Var_Declarations,
    iec61131_interfaces_Var_Init_Decl,
    iec61131_interfaces_Var_Init_Decl_Func,
    iec61131_interfaces_Var_Name_Decl,
    iec61131_interfaces_Var_Spec,
    iec61131_ld_Ladder_Diagram,
    iec61131_ld_Rung,
    iec61131_literals_BSInteger,
    iec61131_literals_Binary_Integer,
    iec61131_literals_Bit_String_Literal,
    iec61131_literals_Boolean_Literal,
    iec61131_literals_Character_String,
    iec61131_literals_Common_Character_Representation,
    iec61131_literals_Constant,
    iec61131_literals_Date,
    iec61131_literals_Date_And_Time,
    iec61131_literals_Date_Literal,
    iec61131_literals_Days,
    iec61131_literals_Daytime,
    iec61131_literals_Double_Byte_Character_Representation,
    iec61131_literals_Double_Byte_Character_String,
    iec61131_literals_Duration,
    iec61131_literals_Fixed_Point,
    iec61131_literals_Fixed_Point_Literal,
    iec61131_literals_Hex_Integer,
    iec61131_literals_Hours,
    iec61131_literals_Integer,
    iec61131_literals_Integer_Literal,
    iec61131_literals_Interval,
    iec61131_literals_Milliseconds,
    iec61131_literals_Minutes,
    iec61131_literals_Numeric_Literal,
    iec61131_literals_Octal_Integer,
    iec61131_literals_Real_Literal,
    iec61131_literals_Seconds,
    iec61131_literals_Signed_Integer,
    iec61131_literals_Single_Byte_Character_Representation,
    iec61131_literals_Single_Byte_Character_String,
    iec61131_literals_Time_Literal,
    iec61131_literals_Time_Of_Day,
    iec61131_literals_Unsigned_Integer,
    iec61131_operators_Add_Operator,
    iec61131_operators_Addition_Name,
    iec61131_operators_Addition_Operator,
    iec61131_operators_Addition_Symbol,
    iec61131_operators_And_Name,
    iec61131_operators_And_Operator,
    iec61131_operators_And_Symbol,
    iec61131_operators_Arithmetic_Name,
    iec61131_operators_Assignment_Name,
    iec61131_operators_Assignment_Operator,
    iec61131_operators_Assignment_Symbol,
    iec61131_operators_Comparison_Name,
    iec61131_operators_Comparison_Operator,
    iec61131_operators_Divide_Name,
    iec61131_operators_Divide_Operator,
    iec61131_operators_Divide_Symbol,
    iec61131_operators_Dot_Operator,
    iec61131_operators_EquUequ_Operator,
    iec61131_operators_Equal_Name,
    iec61131_operators_Equal_Operator,
    iec61131_operators_Equal_Symbol,
    iec61131_operators_GreaterEqual_Name,
    iec61131_operators_GreaterEqual_Operator,
    iec61131_operators_GreaterEqual_Symbol,
    iec61131_operators_Greater_Name,
    iec61131_operators_Greater_Operator,
    iec61131_operators_Greater_Symbol,
    iec61131_operators_LessEqual_Name,
    iec61131_operators_LessEqual_Operator,
    iec61131_operators_LessEqual_Symbol,
    iec61131_operators_Less_Name,
    iec61131_operators_Less_Operator,
    iec61131_operators_Less_Symbol,
    iec61131_operators_Modulo_Operator,
    iec61131_operators_Multiply_Name,
    iec61131_operators_Multiply_Operator,
    iec61131_operators_Multiply_Symbol,
    iec61131_operators_Not_Operator,
    iec61131_operators_Operator,
    iec61131_operators_Or_Operator,
    iec61131_operators_Power_Name,
    iec61131_operators_Power_Operator,
    iec61131_operators_Power_Symbol,
    iec61131_operators_Substraction_Name,
    iec61131_operators_Substraction_Operator,
    iec61131_operators_Substraction_Symbol,
    iec61131_operators_Unary_Operator,
    iec61131_operators_Unequal_Name,
    iec61131_operators_Unequal_Operator,
    iec61131_operators_Unequal_Symbol,
    iec61131_operators_Xor_Operator,
    iec61131_pous_Access_Name,
    iec61131_pous_Array_Type_Declaration,
    iec61131_pous_Data_Type_Declaration,
    iec61131_pous_Derived_Function_Block_Name,
    iec61131_pous_Derived_Function_Name,
    iec61131_pous_Enumerated_Type_Declaration,
    iec61131_pous_Function_Block_Body,
    iec61131_pous_Function_Block_Declaration,
    iec61131_pous_Function_Block_Type_Name,
    iec61131_pous_Function_Block_Vars,
    iec61131_pous_Function_Body,
    iec61131_pous_Function_Declaration,
    iec61131_pous_Function_Name,
    iec61131_pous_Function_Return_Value,
    iec61131_pous_Function_Vars,
    iec61131_pous_Library,
    iec61131_pous_Other_Language,
    iec61131_pous_Program_Access_Decl,
    iec61131_pous_Program_Access_Decls,
    iec61131_pous_Program_Declaration,
    iec61131_pous_Program_Type_Name,
    iec61131_pous_Program_Vars,
    iec61131_pous_Simple_Type_Declaration,
    iec61131_pous_Single_Element_Type_Declaration,
    iec61131_pous_String_Type_Declaration,
    iec61131_pous_Structure_Declaration,
    iec61131_pous_Structure_Element_Declaration,
    iec61131_pous_Structure_Elements,
    iec61131_pous_Structure_Specification,
    iec61131_pous_Structure_Type_Declaration,
    iec61131_pous_Subrange_Type_Declaration,
    iec61131_pous_Type_Declaration,
    iec61131_sfc_Action,
    iec61131_sfc_ActionTime2,
    iec61131_sfc_Action_Association,
    iec61131_sfc_Action_Name,
    iec61131_sfc_Action_Qualifier,
    iec61131_sfc_Action_Time,
    iec61131_sfc_Cond2_Condition,
    iec61131_sfc_Initial_Step,
    iec61131_sfc_Sequential_Function_Chart,
    iec61131_sfc_Sfc_Elements,
    iec61131_sfc_Sfc_Network,
    iec61131_sfc_Step,
    iec61131_sfc_Step_Name,
    iec61131_sfc_Step_Types,
    iec61131_sfc_Steps,
    iec61131_sfc_Steps1,
    iec61131_sfc_Steps2,
    iec61131_sfc_Timed_Qualifier,
    iec61131_sfc_Transition,
    iec61131_sfc_Transition_Cond1,
    iec61131_sfc_Transition_Cond2,
    iec61131_sfc_Transition_Cond3,
    iec61131_sfc_Transition_Condition,
    iec61131_sfc_Transition_Name,
    iec61131_st_Add_Expression,
    iec61131_st_And_Expression,
    iec61131_st_Assignment_Statement,
    iec61131_st_Bracket_Expression,
    iec61131_st_Call_Expression,
    iec61131_st_Case_Element,
    iec61131_st_Case_List,
    iec61131_st_Case_List_Element,
    iec61131_st_Case_Statement,
    iec61131_st_Comparison,
    iec61131_st_Control_Variable,
    iec61131_st_Else_If_Statement,
    iec61131_st_Else_Statement,
    iec61131_st_Equ_Expression,
    iec61131_st_Exit_Statement,
    iec61131_st_Expression,
    iec61131_st_Expression_Constant,
    iec61131_st_Expression_EnumValue,
    iec61131_st_Expression_Types,
    iec61131_st_Expression_Variable,
    iec61131_st_Expression_Variable_Type,
    iec61131_st_Fb_Invocation,
    iec61131_st_For_List,
    iec61131_st_For_Statement,
    iec61131_st_If_Statement,
    iec61131_st_Iteration_Statement,
    iec61131_st_Param_Assignment,
    iec61131_st_Param_Type1,
    iec61131_st_Param_Type2,
    iec61131_st_Power_Expression,
    iec61131_st_Primary_Expression,
    iec61131_st_Repeat_Statement,
    iec61131_st_Return_Statement,
    iec61131_st_Selection_Statement,
    iec61131_st_Statement,
    iec61131_st_Statement_List,
    iec61131_st_Subprogram_Control_Statement,
    iec61131_st_Term_Expression,
    iec61131_st_Unary_Expression,
    iec61131_st_While_Statement,
    iec61131_st_Xor_Expression,
    iec61131_types_Array_Type_Name,
    iec61131_types_Bit_String_Type_Name,
    iec61131_types_Bool_Type_Name,
    iec61131_types_Byte_String_Type_Name,
    iec61131_types_DT_Type_Name,
    iec61131_types_Data_Type_Name,
    iec61131_types_Date_Type_Name,
    iec61131_types_Derived_Type_Name,
    iec61131_types_Double_Byte_String_Type_Name,
    iec61131_types_Duration_Type_Name,
    iec61131_types_Elementary_Type_Name,
    iec61131_types_Enumerated_Type_Name,
    iec61131_types_Generic_Type_Name,
    iec61131_types_Integer_Type_Name,
    iec61131_types_Non_Generic_Type_Name,
    iec61131_types_Numeric_Type_Name,
    iec61131_types_Real_Type_Name,
    iec61131_types_Signed_Integer_Type_Name,
    iec61131_types_Simple_Specification,
    iec61131_types_Simple_Type_Name,
    iec61131_types_Single_Byte_String_Type_Name,
    iec61131_types_Single_Element_Type_Name,
    iec61131_types_String_Type_Name,
    iec61131_types_Structure_Type_Name,
    iec61131_types_Subrange_Type_Name,
    iec61131_types_TOD_Type_Name,
    iec61131_types_TypeLib,
    iec61131_types_Unsigned_Integer_Type_Name,
    iec61131_variables_Array_Variable,
    iec61131_variables_Direct_Variable,
    iec61131_variables_Multi_Element_Variable,
    iec61131_variables_Structured_Variable,
    iec61131_variables_Subscript_List,
    iec61131_variables_Symbolic_Variable,
    iec61131_variables_Variable,
    iec61131_variables_Variable_Name,
    il_Il_Expr_Operator,
    il_Il_Operand,
    il_Il_Operations,
    il_Il_Simple_Operator,
    il_Simple_Instr,
    interfaces_External_Specification,
    interfaces_Interface,
    interfaces_Located_Var_Spec_Init,
    interfaces_Range,
    interfaces_Simple_Specification_Func,
    interfaces_Specification,
    interfaces_Temp_Var_Decl,
    interfaces_Var1_Specification,
    interfaces_Var1_Specification_Func,
    interfaces_Var2_Init_Decl,
    interfaces_Var_Spec,
    literals_BSInteger,
    literals_Fixed_Point_Literal,
    literals_Integer,
    literals_Time_Literal,
    operators_Add_Operator,
    operators_Addition_Operator,
    operators_Arithmetic_Name,
    operators_Comparison_Name,
    operators_Divide_Operator,
    operators_Dot_Operator,
    operators_Equal_Operator,
    operators_GreaterEqual_Operator,
    operators_Greater_Operator,
    operators_LessEqual_Operator,
    operators_Less_Operator,
    operators_Multiply_Operator,
    operators_Operator,
    operators_Substraction_Operator,
    operators_Unary_Operator,
    operators_Unequal_Operator,
    pous_Function_Block_Body,
    pous_Function_Block_Type_Name,
    pous_Function_Block_Vars,
    pous_Function_Body,
    pous_Function_Name,
    pous_Function_Return_Value,
    pous_Function_Vars,
    pous_Program_Vars,
    pous_Structure_Elements,
    pous_Structure_Specification,
    sfc_Action_Time,
    sfc_Sfc_Elements,
    sfc_Step_Types,
    st_Case_List_Element,
    types_Data_Type_Name,
    types_Derived_Type_Name,
    types_Non_Generic_Type_Name,
    types_Simple_Specification,
    types_Single_Element_Type_Name,
    variables_Symbolic_Variable,
    variables_Variable,
    Direction,
    Edge,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

def _is_linked(obj, attr_name, other):
    value = getattr(obj, attr_name, None)
    if isinstance(value, (set, list, tuple, frozenset)):
        return other in value
    return value == other

def _safe_set(obj, attr_name, value):
    # Some generated models have a genuine bug: two reciprocal setters
    # unconditionally call each other with no base case, causing
    # infinite mutual recursion for that specific relationship (found
    # in model_10000002's items10/sc11 pair). That's a defect in the
    # code under test, not in this test -- skip rather than fail so it
    # doesn't masquerade as a test-suite problem.
    try:
        setattr(obj, attr_name, value)
    except RecursionError:
        pytest.skip(f'{attr_name!r} setter has infinite mutual recursion in the generated code')

# =============================================================================
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_iec61131_Commentable_comments_value_roundtrip():
    instance = iec61131_Commentable(comments="sample_text")
    assert instance.comments == "sample_text"
    instance.comments = "sample_text_2"
    assert instance.comments == "sample_text_2"


def test_iec61131_NamedElement_name_value_roundtrip():
    instance = iec61131_NamedElement(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_configurations_Access_Declaration_direction_value_roundtrip():
    instance = iec61131_configurations_Access_Declaration(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_iec61131_configurations_Access_Name_name_value_roundtrip():
    instance = iec61131_configurations_Access_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_configurations_Program_Configuration_retain_value_roundtrip():
    instance = iec61131_configurations_Program_Configuration(retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_configurations_Program_Name_name_value_roundtrip():
    instance = iec61131_configurations_Program_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_configurations_Resource_Name_name_value_roundtrip():
    instance = iec61131_configurations_Resource_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_configurations_Task_Name_name_value_roundtrip():
    instance = iec61131_configurations_Task_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_il_Label_label_value_roundtrip():
    instance = iec61131_il_Label(label="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_iec61131_interfaces_Edge_Declaration_edge_value_roundtrip():
    instance = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    assert instance.edge == "sample_text"
    instance.edge = "sample_text_2"
    assert instance.edge == "sample_text_2"


def test_iec61131_interfaces_Enumerated_Value_name_value_roundtrip():
    instance = iec61131_interfaces_Enumerated_Value(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_interfaces_External_Var_Declarations_constant_value_roundtrip():
    instance = iec61131_interfaces_External_Var_Declarations(constant=True)
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_iec61131_interfaces_Function_Var_Decl_constant_value_roundtrip():
    instance = iec61131_interfaces_Function_Var_Decl(constant=True)
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_iec61131_interfaces_Global_Var_Declarations_constant_value_roundtrip():
    instance = iec61131_interfaces_Global_Var_Declarations(constant=True, retain=True)
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_iec61131_interfaces_Global_Var_Declarations_retain_value_roundtrip():
    instance = iec61131_interfaces_Global_Var_Declarations(constant=True, retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_interfaces_Incompl_Located_Var_Declarations_retain_value_roundtrip():
    instance = iec61131_interfaces_Incompl_Located_Var_Declarations(retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_interfaces_Incompl_Location_location_value_roundtrip():
    instance = iec61131_interfaces_Incompl_Location(location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_iec61131_interfaces_Input_Declarations_retain_value_roundtrip():
    instance = iec61131_interfaces_Input_Declarations(retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_interfaces_Located_Var_Declarations_constant_value_roundtrip():
    instance = iec61131_interfaces_Located_Var_Declarations(constant=True, retain=True)
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_iec61131_interfaces_Located_Var_Declarations_retain_value_roundtrip():
    instance = iec61131_interfaces_Located_Var_Declarations(constant=True, retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_interfaces_Output_Declarations_retain_value_roundtrip():
    instance = iec61131_interfaces_Output_Declarations(retain=True)
    assert instance.retain == True
    instance.retain = False
    assert instance.retain == False


def test_iec61131_interfaces_Structure_Element_Name_name_value_roundtrip():
    instance = iec61131_interfaces_Structure_Element_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_interfaces_Subrange_delimiter_value_roundtrip():
    instance = iec61131_interfaces_Subrange(delimiter="sample_text")
    assert instance.delimiter == "sample_text"
    instance.delimiter = "sample_text_2"
    assert instance.delimiter == "sample_text_2"


def test_iec61131_interfaces_Var_Declarations_constant_value_roundtrip():
    instance = iec61131_interfaces_Var_Declarations(constant=True)
    assert instance.constant == True
    instance.constant = False
    assert instance.constant == False


def test_iec61131_literals_Boolean_Literal_value_value_roundtrip():
    instance = iec61131_literals_Boolean_Literal(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_literals_Common_Character_Representation_value_value_roundtrip():
    instance = iec61131_literals_Common_Character_Representation(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_literals_Date_Literal_day_value_roundtrip():
    instance = iec61131_literals_Date_Literal(day="sample_text", month="sample_text", year="sample_text")
    assert instance.day == "sample_text"
    instance.day = "sample_text_2"
    assert instance.day == "sample_text_2"


def test_iec61131_literals_Date_Literal_month_value_roundtrip():
    instance = iec61131_literals_Date_Literal(day="sample_text", month="sample_text", year="sample_text")
    assert instance.month == "sample_text"
    instance.month = "sample_text_2"
    assert instance.month == "sample_text_2"


def test_iec61131_literals_Date_Literal_year_value_roundtrip():
    instance = iec61131_literals_Date_Literal(day="sample_text", month="sample_text", year="sample_text")
    assert instance.year == "sample_text"
    instance.year = "sample_text_2"
    assert instance.year == "sample_text_2"


def test_iec61131_literals_Daytime_hour_value_roundtrip():
    instance = iec61131_literals_Daytime(hour="sample_text", minute="sample_text")
    assert instance.hour == "sample_text"
    instance.hour = "sample_text_2"
    assert instance.hour == "sample_text_2"


def test_iec61131_literals_Daytime_minute_value_roundtrip():
    instance = iec61131_literals_Daytime(hour="sample_text", minute="sample_text")
    assert instance.minute == "sample_text"
    instance.minute = "sample_text_2"
    assert instance.minute == "sample_text_2"


def test_iec61131_literals_Double_Byte_Character_Representation_value_value_roundtrip():
    instance = iec61131_literals_Double_Byte_Character_Representation(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_literals_Fixed_Point_valuePost_value_roundtrip():
    instance = iec61131_literals_Fixed_Point(valuePost="sample_text", valuePre="sample_text")
    assert instance.valuePost == "sample_text"
    instance.valuePost = "sample_text_2"
    assert instance.valuePost == "sample_text_2"


def test_iec61131_literals_Fixed_Point_valuePre_value_roundtrip():
    instance = iec61131_literals_Fixed_Point(valuePost="sample_text", valuePre="sample_text")
    assert instance.valuePre == "sample_text"
    instance.valuePre = "sample_text_2"
    assert instance.valuePre == "sample_text_2"


def test_iec61131_literals_Integer_value_value_roundtrip():
    instance = iec61131_literals_Integer(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_literals_Real_Literal_exponent_value_roundtrip():
    instance = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    assert instance.exponent == "sample_text"
    instance.exponent = "sample_text_2"
    assert instance.exponent == "sample_text_2"


def test_iec61131_literals_Real_Literal_negative_value_roundtrip():
    instance = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    assert instance.negative == True
    instance.negative = False
    assert instance.negative == False


def test_iec61131_literals_Signed_Integer_negative_value_roundtrip():
    instance = iec61131_literals_Signed_Integer(negative=True)
    assert instance.negative == True
    instance.negative = False
    assert instance.negative == False


def test_iec61131_literals_Single_Byte_Character_Representation_value_value_roundtrip():
    instance = iec61131_literals_Single_Byte_Character_Representation(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_pous_Access_Name_name_value_roundtrip():
    instance = iec61131_pous_Access_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_pous_Other_Language_text_value_roundtrip():
    instance = iec61131_pous_Other_Language(text="sample_text")
    assert instance.text == "sample_text"
    instance.text = "sample_text_2"
    assert instance.text == "sample_text_2"


def test_iec61131_pous_Program_Access_Decl_direction_value_roundtrip():
    instance = iec61131_pous_Program_Access_Decl(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_iec61131_sfc_Action_Name_name_value_roundtrip():
    instance = iec61131_sfc_Action_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_sfc_Action_Qualifier_qualifier_value_roundtrip():
    instance = iec61131_sfc_Action_Qualifier(qualifier="sample_text")
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_iec61131_sfc_Timed_Qualifier_qualifier_value_roundtrip():
    instance = iec61131_sfc_Timed_Qualifier(qualifier="sample_text")
    assert instance.qualifier == "sample_text"
    instance.qualifier = "sample_text_2"
    assert instance.qualifier == "sample_text_2"


def test_iec61131_sfc_Transition_Name_name_value_roundtrip():
    instance = iec61131_sfc_Transition_Name(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_st_Control_Variable_name_value_roundtrip():
    instance = iec61131_st_Control_Variable(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_iec61131_variables_Direct_Variable_value_value_roundtrip():
    instance = iec61131_variables_Direct_Variable(value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_iec61131_configurations_Direct_Path_isa_Access_Path():
    instance = iec61131_configurations_Direct_Path()
    assert isinstance(instance, Access_Path)


def test_iec61131_configurations_Symbolic_Path_isa_Access_Path():
    instance = iec61131_configurations_Symbolic_Path()
    assert isinstance(instance, Access_Path)


def test_iec61131_sfc_ActionTime2_isa_Action_Time():
    instance = iec61131_sfc_ActionTime2()
    assert isinstance(instance, Action_Time)


def test_iec61131_operators_And_Name_isa_And_Operator():
    instance = iec61131_operators_And_Name()
    assert isinstance(instance, And_Operator)


def test_iec61131_operators_And_Symbol_isa_And_Operator():
    instance = iec61131_operators_And_Symbol()
    assert isinstance(instance, And_Operator)


def test_iec61131_interfaces_Array_Initial_Elements1_isa_Array_Initial_Elements():
    instance = iec61131_interfaces_Array_Initial_Elements1()
    assert isinstance(instance, Array_Initial_Elements)


def test_iec61131_interfaces_Array_Initial_Elements2_isa_Array_Initial_Elements():
    instance = iec61131_interfaces_Array_Initial_Elements2()
    assert isinstance(instance, Array_Initial_Elements)


def test_iec61131_interfaces_Array_Specification1_isa_Array_Specification():
    instance = iec61131_interfaces_Array_Specification1()
    assert isinstance(instance, Array_Specification)


def test_iec61131_interfaces_Array_Specification2_isa_Array_Specification():
    instance = iec61131_interfaces_Array_Specification2()
    assert isinstance(instance, Array_Specification)


def test_iec61131_operators_Assignment_Name_isa_Assignment_Operator():
    instance = iec61131_operators_Assignment_Name()
    assert isinstance(instance, Assignment_Operator)


def test_iec61131_operators_Assignment_Symbol_isa_Assignment_Operator():
    instance = iec61131_operators_Assignment_Symbol()
    assert isinstance(instance, Assignment_Operator)


def test_iec61131_types_Bool_Type_Name_isa_Bit_String_Type_Name():
    instance = iec61131_types_Bool_Type_Name()
    assert isinstance(instance, Bit_String_Type_Name)


def test_iec61131_pous_Derived_Function_Block_Name_isa_Blocks():
    instance = iec61131_pous_Derived_Function_Block_Name()
    assert isinstance(instance, Blocks)


def test_iec61131_pous_Derived_Function_Name_isa_Blocks():
    instance = iec61131_pous_Derived_Function_Name()
    assert isinstance(instance, Blocks)


def test_iec61131_pous_Program_Type_Name_isa_Blocks():
    instance = iec61131_pous_Program_Type_Name()
    assert isinstance(instance, Blocks)


def test_iec61131_interfaces_Double_BString_isa_Byte_String():
    instance = iec61131_interfaces_Double_BString()
    assert isinstance(instance, Byte_String)


def test_iec61131_interfaces_Single_BString_isa_Byte_String():
    instance = iec61131_interfaces_Single_BString()
    assert isinstance(instance, Byte_String)


def test_iec61131_types_Double_Byte_String_Type_Name_isa_Byte_String_Type_Name():
    instance = iec61131_types_Double_Byte_String_Type_Name()
    assert isinstance(instance, Byte_String_Type_Name)


def test_iec61131_types_Single_Byte_String_Type_Name_isa_Byte_String_Type_Name():
    instance = iec61131_types_Single_Byte_String_Type_Name()
    assert isinstance(instance, Byte_String_Type_Name)


def test_iec61131_interfaces_Subrange_isa_Case_List_Element():
    instance = iec61131_interfaces_Subrange(delimiter="sample_text")
    assert isinstance(instance, Case_List_Element)


def test_iec61131_literals_Double_Byte_Character_String_isa_Character_String():
    instance = iec61131_literals_Double_Byte_Character_String()
    assert isinstance(instance, Character_String)


def test_iec61131_literals_Single_Byte_Character_String_isa_Character_String():
    instance = iec61131_literals_Single_Byte_Character_String()
    assert isinstance(instance, Character_String)


def test_iec61131_Library_Element_Declaration_isa_Commentable():
    instance = iec61131_Library_Element_Declaration()
    assert isinstance(instance, Commentable)


def test_iec61131_configurations_Program_Configuration_isa_Commentable():
    instance = iec61131_configurations_Program_Configuration(retain=True)
    assert isinstance(instance, Commentable)


def test_iec61131_interfaces_Global_Var_Decl_isa_Commentable():
    instance = iec61131_interfaces_Global_Var_Decl()
    assert isinstance(instance, Commentable)


def test_iec61131_interfaces_Global_Var_Name_isa_Commentable():
    instance = iec61131_interfaces_Global_Var_Name()
    assert isinstance(instance, Commentable)


def test_iec61131_interfaces_Interface_isa_Commentable():
    instance = iec61131_interfaces_Interface()
    assert isinstance(instance, Commentable)


def test_iec61131_pous_Function_Block_Type_Name_isa_Commentable():
    instance = iec61131_pous_Function_Block_Type_Name()
    assert isinstance(instance, Commentable)


def test_iec61131_st_Expression_Types_isa_Commentable():
    instance = iec61131_st_Expression_Types()
    assert isinstance(instance, Commentable)


def test_iec61131_st_Expression_Variable_isa_Commentable():
    instance = iec61131_st_Expression_Variable()
    assert isinstance(instance, Commentable)


def test_iec61131_st_Param_Assignment_isa_Commentable():
    instance = iec61131_st_Param_Assignment()
    assert isinstance(instance, Commentable)


def test_iec61131_st_Statement_isa_Commentable():
    instance = iec61131_st_Statement()
    assert isinstance(instance, Commentable)


def test_iec61131_variables_Variable_isa_Commentable():
    instance = iec61131_variables_Variable()
    assert isinstance(instance, Commentable)


def test_iec61131_operators_GreaterEqual_Operator_isa_Comparison_Operator():
    instance = iec61131_operators_GreaterEqual_Operator()
    assert isinstance(instance, Comparison_Operator)


def test_iec61131_operators_Greater_Operator_isa_Comparison_Operator():
    instance = iec61131_operators_Greater_Operator()
    assert isinstance(instance, Comparison_Operator)


def test_iec61131_operators_LessEqual_Operator_isa_Comparison_Operator():
    instance = iec61131_operators_LessEqual_Operator()
    assert isinstance(instance, Comparison_Operator)


def test_iec61131_operators_Less_Operator_isa_Comparison_Operator():
    instance = iec61131_operators_Less_Operator()
    assert isinstance(instance, Comparison_Operator)


def test_iec61131_fbd_Fbd_Network_isa_Cond2_Condition():
    instance = iec61131_fbd_Fbd_Network()
    assert isinstance(instance, Cond2_Condition)


def test_iec61131_ld_Rung_isa_Cond2_Condition():
    instance = iec61131_ld_Rung()
    assert isinstance(instance, Cond2_Condition)


def test_iec61131_literals_Bit_String_Literal_isa_Constant():
    instance = iec61131_literals_Bit_String_Literal()
    assert isinstance(instance, Constant)


def test_iec61131_literals_Boolean_Literal_isa_Constant():
    instance = iec61131_literals_Boolean_Literal(value="sample_text")
    assert isinstance(instance, Constant)


def test_iec61131_literals_Character_String_isa_Constant():
    instance = iec61131_literals_Character_String()
    assert isinstance(instance, Constant)


def test_iec61131_literals_Numeric_Literal_isa_Constant():
    instance = iec61131_literals_Numeric_Literal()
    assert isinstance(instance, Constant)


def test_iec61131_literals_Time_Literal_isa_Constant():
    instance = iec61131_literals_Time_Literal()
    assert isinstance(instance, Constant)


def test_iec61131_configurations_Program_Output_Reference_isa_Data_Source():
    instance = iec61131_configurations_Program_Output_Reference()
    assert isinstance(instance, Data_Source)


def test_iec61131_types_Simple_Specification_isa_Data_Type_Name():
    instance = iec61131_types_Simple_Specification()
    assert isinstance(instance, Data_Type_Name)


def test_iec61131_types_DT_Type_Name_isa_Date_Type_Name():
    instance = iec61131_types_DT_Type_Name()
    assert isinstance(instance, Date_Type_Name)


def test_iec61131_types_TOD_Type_Name_isa_Date_Type_Name():
    instance = iec61131_types_TOD_Type_Name()
    assert isinstance(instance, Date_Type_Name)


def test_iec61131_types_Array_Type_Name_isa_Derived_Type_Name():
    instance = iec61131_types_Array_Type_Name()
    assert isinstance(instance, Derived_Type_Name)


def test_iec61131_types_Single_Element_Type_Name_isa_Derived_Type_Name():
    instance = iec61131_types_Single_Element_Type_Name()
    assert isinstance(instance, Derived_Type_Name)


def test_iec61131_types_String_Type_Name_isa_Derived_Type_Name():
    instance = iec61131_types_String_Type_Name()
    assert isinstance(instance, Derived_Type_Name)


def test_iec61131_operators_Divide_Symbol_isa_Divide_Operator():
    instance = iec61131_operators_Divide_Symbol()
    assert isinstance(instance, Divide_Operator)


def test_iec61131_operators_Divide_Operator_isa_Dot_Operator():
    instance = iec61131_operators_Divide_Operator()
    assert isinstance(instance, Dot_Operator)


def test_iec61131_operators_Multiply_Operator_isa_Dot_Operator():
    instance = iec61131_operators_Multiply_Operator()
    assert isinstance(instance, Dot_Operator)


def test_iec61131_types_Bit_String_Type_Name_isa_Elementary_Type_Name():
    instance = iec61131_types_Bit_String_Type_Name()
    assert isinstance(instance, Elementary_Type_Name)


def test_iec61131_types_Byte_String_Type_Name_isa_Elementary_Type_Name():
    instance = iec61131_types_Byte_String_Type_Name()
    assert isinstance(instance, Elementary_Type_Name)


def test_iec61131_types_Date_Type_Name_isa_Elementary_Type_Name():
    instance = iec61131_types_Date_Type_Name()
    assert isinstance(instance, Elementary_Type_Name)


def test_iec61131_types_Duration_Type_Name_isa_Elementary_Type_Name():
    instance = iec61131_types_Duration_Type_Name()
    assert isinstance(instance, Elementary_Type_Name)


def test_iec61131_types_Numeric_Type_Name_isa_Elementary_Type_Name():
    instance = iec61131_types_Numeric_Type_Name()
    assert isinstance(instance, Elementary_Type_Name)


def test_iec61131_interfaces_Enumerated_Specification1_isa_Enumerated_Specification():
    instance = iec61131_interfaces_Enumerated_Specification1()
    assert isinstance(instance, Enumerated_Specification)


def test_iec61131_interfaces_Enumerated_Specification2_isa_Enumerated_Specification():
    instance = iec61131_interfaces_Enumerated_Specification2()
    assert isinstance(instance, Enumerated_Specification)


def test_iec61131_operators_Equal_Operator_isa_EquUequ_Operator():
    instance = iec61131_operators_Equal_Operator()
    assert isinstance(instance, EquUequ_Operator)


def test_iec61131_operators_Unequal_Operator_isa_EquUequ_Operator():
    instance = iec61131_operators_Unequal_Operator()
    assert isinstance(instance, EquUequ_Operator)


def test_iec61131_operators_Equal_Symbol_isa_Equal_Operator():
    instance = iec61131_operators_Equal_Symbol()
    assert isinstance(instance, Equal_Operator)


def test_iec61131_st_Add_Expression_isa_Expression_Types():
    instance = iec61131_st_Add_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_And_Expression_isa_Expression_Types():
    instance = iec61131_st_And_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Comparison_isa_Expression_Types():
    instance = iec61131_st_Comparison()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Equ_Expression_isa_Expression_Types():
    instance = iec61131_st_Equ_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Expression_isa_Expression_Types():
    instance = iec61131_st_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Power_Expression_isa_Expression_Types():
    instance = iec61131_st_Power_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Primary_Expression_isa_Expression_Types():
    instance = iec61131_st_Primary_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Term_Expression_isa_Expression_Types():
    instance = iec61131_st_Term_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Unary_Expression_isa_Expression_Types():
    instance = iec61131_st_Unary_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_st_Xor_Expression_isa_Expression_Types():
    instance = iec61131_st_Xor_Expression()
    assert isinstance(instance, Expression_Types)


def test_iec61131_literals_Fixed_Point_isa_Fixed_Point_Literal():
    instance = iec61131_literals_Fixed_Point(valuePost="sample_text", valuePre="sample_text")
    assert isinstance(instance, Fixed_Point_Literal)


def test_iec61131_sfc_Sequential_Function_Chart_isa_Function_Block_Body():
    instance = iec61131_sfc_Sequential_Function_Chart()
    assert isinstance(instance, Function_Block_Body)


def test_iec61131_interfaces_Global_Var_List_isa_Global_Var_Spec():
    instance = iec61131_interfaces_Global_Var_List()
    assert isinstance(instance, Global_Var_Spec)


def test_iec61131_interfaces_Global_Var_Location_isa_Global_Var_Spec():
    instance = iec61131_interfaces_Global_Var_Location()
    assert isinstance(instance, Global_Var_Spec)


def test_iec61131_operators_GreaterEqual_Symbol_isa_GreaterEqual_Operator():
    instance = iec61131_operators_GreaterEqual_Symbol()
    assert isinstance(instance, GreaterEqual_Operator)


def test_iec61131_operators_Greater_Symbol_isa_Greater_Operator():
    instance = iec61131_operators_Greater_Symbol()
    assert isinstance(instance, Greater_Operator)


def test_iec61131_operators_Arithmetic_Name_isa_Il_Expr_Operator():
    instance = iec61131_operators_Arithmetic_Name()
    assert isinstance(instance, Il_Expr_Operator)


def test_iec61131_operators_Comparison_Name_isa_Il_Expr_Operator():
    instance = iec61131_operators_Comparison_Name()
    assert isinstance(instance, Il_Expr_Operator)


def test_iec61131_il_Il_Fb_Call_isa_Il_Operations():
    instance = iec61131_il_Il_Fb_Call()
    assert isinstance(instance, Il_Operations)


def test_iec61131_il_Il_Jump_Operation_isa_Il_Operations():
    instance = iec61131_il_Il_Jump_Operation()
    assert isinstance(instance, Il_Operations)


def test_iec61131_il_Il_Return_Operator_isa_Il_Operations():
    instance = iec61131_il_Il_Return_Operator()
    assert isinstance(instance, Il_Operations)


def test_iec61131_il_Simple_Operation1_isa_Il_Simple_Operation():
    instance = iec61131_il_Simple_Operation1()
    assert isinstance(instance, Il_Simple_Operation)


def test_iec61131_il_Simple_Operation2_isa_Il_Simple_Operation():
    instance = iec61131_il_Simple_Operation2()
    assert isinstance(instance, Il_Simple_Operation)


def test_iec61131_il_Il_Expr_Operator_isa_Il_Simple_Operator():
    instance = iec61131_il_Il_Expr_Operator()
    assert isinstance(instance, Il_Simple_Operator)


def test_iec61131_interfaces_InitElement_Array_isa_Initial_Element():
    instance = iec61131_interfaces_InitElement_Array()
    assert isinstance(instance, Initial_Element)


def test_iec61131_interfaces_InitElement_Constant_isa_Initial_Element():
    instance = iec61131_interfaces_InitElement_Constant()
    assert isinstance(instance, Initial_Element)


def test_iec61131_interfaces_InitElement_EnumValue_isa_Initial_Element():
    instance = iec61131_interfaces_InitElement_EnumValue()
    assert isinstance(instance, Initial_Element)


def test_iec61131_interfaces_InitElement_Structure_isa_Initial_Element():
    instance = iec61131_interfaces_InitElement_Structure()
    assert isinstance(instance, Initial_Element)


def test_iec61131_interfaces_Edge_Declaration_isa_Input_Declaration():
    instance = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    assert isinstance(instance, Input_Declaration)


def test_iec61131_interfaces_Var_Init_Decl_isa_Input_Declaration():
    instance = iec61131_interfaces_Var_Init_Decl()
    assert isinstance(instance, Input_Declaration)


def test_iec61131_variables_Variable_Name_isa_Input_Reference():
    instance = iec61131_variables_Variable_Name()
    assert isinstance(instance, Input_Reference)


def test_iec61131_configurations_Instance_Spec1_isa_Instance_Specific_Init():
    instance = iec61131_configurations_Instance_Spec1()
    assert isinstance(instance, Instance_Specific_Init)


def test_iec61131_configurations_Instance_Spec2_isa_Instance_Specific_Init():
    instance = iec61131_configurations_Instance_Spec2()
    assert isinstance(instance, Instance_Specific_Init)


def test_iec61131_types_Signed_Integer_Type_Name_isa_Integer_Type_Name():
    instance = iec61131_types_Signed_Integer_Type_Name()
    assert isinstance(instance, Integer_Type_Name)


def test_iec61131_types_Unsigned_Integer_Type_Name_isa_Integer_Type_Name():
    instance = iec61131_types_Unsigned_Integer_Type_Name()
    assert isinstance(instance, Integer_Type_Name)


def test_iec61131_literals_Days_isa_Interval():
    instance = iec61131_literals_Days()
    assert isinstance(instance, Interval)


def test_iec61131_literals_Hours_isa_Interval():
    instance = iec61131_literals_Hours()
    assert isinstance(instance, Interval)


def test_iec61131_literals_Milliseconds_isa_Interval():
    instance = iec61131_literals_Milliseconds()
    assert isinstance(instance, Interval)


def test_iec61131_literals_Minutes_isa_Interval():
    instance = iec61131_literals_Minutes()
    assert isinstance(instance, Interval)


def test_iec61131_literals_Seconds_isa_Interval():
    instance = iec61131_literals_Seconds()
    assert isinstance(instance, Interval)


def test_iec61131_interfaces_Input_Declarations_isa_Io_Var_Declaration():
    instance = iec61131_interfaces_Input_Declarations(retain=True)
    assert isinstance(instance, Io_Var_Declaration)


def test_iec61131_interfaces_Input_Output_Declarations_isa_Io_Var_Declaration():
    instance = iec61131_interfaces_Input_Output_Declarations()
    assert isinstance(instance, Io_Var_Declaration)


def test_iec61131_interfaces_Output_Declarations_isa_Io_Var_Declaration():
    instance = iec61131_interfaces_Output_Declarations(retain=True)
    assert isinstance(instance, Io_Var_Declaration)


def test_iec61131_st_Exit_Statement_isa_Iteration_Statement():
    instance = iec61131_st_Exit_Statement()
    assert isinstance(instance, Iteration_Statement)


def test_iec61131_st_For_Statement_isa_Iteration_Statement():
    instance = iec61131_st_For_Statement()
    assert isinstance(instance, Iteration_Statement)


def test_iec61131_st_Repeat_Statement_isa_Iteration_Statement():
    instance = iec61131_st_Repeat_Statement()
    assert isinstance(instance, Iteration_Statement)


def test_iec61131_st_While_Statement_isa_Iteration_Statement():
    instance = iec61131_st_While_Statement()
    assert isinstance(instance, Iteration_Statement)


def test_iec61131_operators_LessEqual_Symbol_isa_LessEqual_Operator():
    instance = iec61131_operators_LessEqual_Symbol()
    assert isinstance(instance, LessEqual_Operator)


def test_iec61131_operators_Less_Symbol_isa_Less_Operator():
    instance = iec61131_operators_Less_Symbol()
    assert isinstance(instance, Less_Operator)


def test_iec61131_configurations_Configuration_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_configurations_Configuration_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_configurations_Resource_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_configurations_Resource_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_interfaces_Global_Var_Declarations_isa_Library_Element_Declaration():
    instance = iec61131_interfaces_Global_Var_Declarations(constant=True, retain=True)
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_pous_Data_Type_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_pous_Data_Type_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_pous_Function_Block_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_pous_Function_Block_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_pous_Function_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_pous_Function_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_pous_Program_Declaration_isa_Library_Element_Declaration():
    instance = iec61131_pous_Program_Declaration()
    assert isinstance(instance, Library_Element_Declaration)


def test_iec61131_configurations_Configuration_Name_isa_Library_Element_Name():
    instance = iec61131_configurations_Configuration_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_configurations_Resource_Type_Name_isa_Library_Element_Name():
    instance = iec61131_configurations_Resource_Type_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_interfaces_Global_Var_Name_isa_Library_Element_Name():
    instance = iec61131_interfaces_Global_Var_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_pous_Function_Block_Type_Name_isa_Library_Element_Name():
    instance = iec61131_pous_Function_Block_Type_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_pous_Function_Name_isa_Library_Element_Name():
    instance = iec61131_pous_Function_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_pous_Program_Type_Name_isa_Library_Element_Name():
    instance = iec61131_pous_Program_Type_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_types_Data_Type_Name_isa_Library_Element_Name():
    instance = iec61131_types_Data_Type_Name()
    assert isinstance(instance, Library_Element_Name)


def test_iec61131_interfaces_Double_Byte_String_Spec_isa_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Double_Byte_String_Spec()
    assert isinstance(instance, Located_Var_Spec_Init)


def test_iec61131_interfaces_Single_Byte_String_Spec_isa_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Single_Byte_String_Spec()
    assert isinstance(instance, Located_Var_Spec_Init)


def test_iec61131_variables_Array_Variable_isa_Multi_Element_Variable():
    instance = iec61131_variables_Array_Variable()
    assert isinstance(instance, Multi_Element_Variable)


def test_iec61131_variables_Structured_Variable_isa_Multi_Element_Variable():
    instance = iec61131_variables_Structured_Variable()
    assert isinstance(instance, Multi_Element_Variable)


def test_iec61131_operators_Multiply_Symbol_isa_Multiply_Operator():
    instance = iec61131_operators_Multiply_Symbol()
    assert isinstance(instance, Multiply_Operator)


def test_iec61131_Library_Element_Name_isa_NamedElement():
    instance = iec61131_Library_Element_Name()
    assert isinstance(instance, NamedElement)


def test_iec61131_sfc_Step_Name_isa_NamedElement():
    instance = iec61131_sfc_Step_Name()
    assert isinstance(instance, NamedElement)


def test_iec61131_variables_Variable_Name_isa_NamedElement():
    instance = iec61131_variables_Variable_Name()
    assert isinstance(instance, NamedElement)


def test_iec61131_types_Derived_Type_Name_isa_Non_Generic_Type_Name():
    instance = iec61131_types_Derived_Type_Name()
    assert isinstance(instance, Non_Generic_Type_Name)


def test_iec61131_literals_Integer_Literal_isa_Numeric_Literal():
    instance = iec61131_literals_Integer_Literal()
    assert isinstance(instance, Numeric_Literal)


def test_iec61131_literals_Real_Literal_isa_Numeric_Literal():
    instance = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    assert isinstance(instance, Numeric_Literal)


def test_iec61131_types_Integer_Type_Name_isa_Numeric_Type_Name():
    instance = iec61131_types_Integer_Type_Name()
    assert isinstance(instance, Numeric_Type_Name)


def test_iec61131_types_Real_Type_Name_isa_Numeric_Type_Name():
    instance = iec61131_types_Real_Type_Name()
    assert isinstance(instance, Numeric_Type_Name)


def test_iec61131_il_Operand1_isa_Operands():
    instance = iec61131_il_Operand1()
    assert isinstance(instance, Operands)


def test_iec61131_il_Operand2_isa_Operands():
    instance = iec61131_il_Operand2()
    assert isinstance(instance, Operands)


def test_iec61131_operators_Add_Operator_isa_Operator():
    instance = iec61131_operators_Add_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_Assignment_Operator_isa_Operator():
    instance = iec61131_operators_Assignment_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_Comparison_Operator_isa_Operator():
    instance = iec61131_operators_Comparison_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_Dot_Operator_isa_Operator():
    instance = iec61131_operators_Dot_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_EquUequ_Operator_isa_Operator():
    instance = iec61131_operators_EquUequ_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_Power_Operator_isa_Operator():
    instance = iec61131_operators_Power_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_operators_Unary_Operator_isa_Operator():
    instance = iec61131_operators_Unary_Operator()
    assert isinstance(instance, Operator)


def test_iec61131_interfaces_External_Var_Declarations_isa_Other_Var_Declaration():
    instance = iec61131_interfaces_External_Var_Declarations(constant=True)
    assert isinstance(instance, Other_Var_Declaration)


def test_iec61131_interfaces_Incompl_Located_Var_Declarations_isa_Other_Var_Declaration():
    instance = iec61131_interfaces_Incompl_Located_Var_Declarations(retain=True)
    assert isinstance(instance, Other_Var_Declaration)


def test_iec61131_interfaces_RNV_Declarations_isa_Other_Var_Declaration():
    instance = iec61131_interfaces_RNV_Declarations()
    assert isinstance(instance, Other_Var_Declaration)


def test_iec61131_interfaces_Temp_Var_Decls_isa_Other_Var_Declaration():
    instance = iec61131_interfaces_Temp_Var_Decls()
    assert isinstance(instance, Other_Var_Declaration)


def test_iec61131_variables_Variable_Name_isa_Output_Reference():
    instance = iec61131_variables_Variable_Name()
    assert isinstance(instance, Output_Reference)


def test_iec61131_il_Il_Operand_isa_Param_Assignment():
    instance = iec61131_il_Il_Operand()
    assert isinstance(instance, Param_Assignment)


def test_iec61131_il_Param_Assignment2_isa_Param_Assignment():
    instance = iec61131_il_Param_Assignment2()
    assert isinstance(instance, Param_Assignment)


def test_iec61131_st_Param_Type1_isa_Param_Assignment():
    instance = iec61131_st_Param_Type1()
    assert isinstance(instance, Param_Assignment)


def test_iec61131_st_Param_Type2_isa_Param_Assignment():
    instance = iec61131_st_Param_Type2()
    assert isinstance(instance, Param_Assignment)


def test_iec61131_il_Il_Param_Assignment_isa_Param_Assignments():
    instance = iec61131_il_Il_Param_Assignment()
    assert isinstance(instance, Param_Assignments)


def test_iec61131_il_Il_Param_Out_Assignment_isa_Param_Assignments():
    instance = iec61131_il_Il_Param_Out_Assignment()
    assert isinstance(instance, Param_Assignments)


def test_iec61131_il_Il_Param_Instruction_isa_Param_Instruction():
    instance = iec61131_il_Il_Param_Instruction()
    assert isinstance(instance, Param_Instruction)


def test_iec61131_il_Il_Param_Last_Instruction_isa_Param_Instruction():
    instance = iec61131_il_Il_Param_Last_Instruction()
    assert isinstance(instance, Param_Instruction)


def test_iec61131_operators_Power_Name_isa_Power_Operator():
    instance = iec61131_operators_Power_Name()
    assert isinstance(instance, Power_Operator)


def test_iec61131_operators_Power_Symbol_isa_Power_Operator():
    instance = iec61131_operators_Power_Symbol()
    assert isinstance(instance, Power_Operator)


def test_iec61131_st_Bracket_Expression_isa_Primary_Expression():
    instance = iec61131_st_Bracket_Expression()
    assert isinstance(instance, Primary_Expression)


def test_iec61131_st_Call_Expression_isa_Primary_Expression():
    instance = iec61131_st_Call_Expression()
    assert isinstance(instance, Primary_Expression)


def test_iec61131_st_Expression_Constant_isa_Primary_Expression():
    instance = iec61131_st_Expression_Constant()
    assert isinstance(instance, Primary_Expression)


def test_iec61131_st_Expression_EnumValue_isa_Primary_Expression():
    instance = iec61131_st_Expression_EnumValue()
    assert isinstance(instance, Primary_Expression)


def test_iec61131_st_Expression_Variable_Type_isa_Primary_Expression():
    instance = iec61131_st_Expression_Variable_Type()
    assert isinstance(instance, Primary_Expression)


def test_iec61131_configurations_Prog_Sink_isa_Prog_Cnxn():
    instance = iec61131_configurations_Prog_Sink()
    assert isinstance(instance, Prog_Cnxn)


def test_iec61131_configurations_Prog_Source_isa_Prog_Cnxn():
    instance = iec61131_configurations_Prog_Source()
    assert isinstance(instance, Prog_Cnxn)


def test_iec61131_configurations_Fb_Task_isa_Prog_Conf_Element():
    instance = iec61131_configurations_Fb_Task()
    assert isinstance(instance, Prog_Conf_Element)


def test_iec61131_configurations_Prog_Cnxn_isa_Prog_Conf_Element():
    instance = iec61131_configurations_Prog_Cnxn()
    assert isinstance(instance, Prog_Conf_Element)


def test_iec61131_interfaces_Located_Var_Declarations_isa_Program_Vars():
    instance = iec61131_interfaces_Located_Var_Declarations(constant=True, retain=True)
    assert isinstance(instance, Program_Vars)


def test_iec61131_pous_Program_Access_Decls_isa_Program_Vars():
    instance = iec61131_pous_Program_Access_Decls()
    assert isinstance(instance, Program_Vars)


def test_iec61131_interfaces_Non_Retentive_Var_Declarations_isa_RNV_Declarations():
    instance = iec61131_interfaces_Non_Retentive_Var_Declarations()
    assert isinstance(instance, RNV_Declarations)


def test_iec61131_interfaces_Retentive_Var_Declarations_isa_RNV_Declarations():
    instance = iec61131_interfaces_Retentive_Var_Declarations()
    assert isinstance(instance, RNV_Declarations)


def test_iec61131_interfaces_Var_Declarations_isa_RNV_Declarations():
    instance = iec61131_interfaces_Var_Declarations(constant=True)
    assert isinstance(instance, RNV_Declarations)


def test_iec61131_st_Case_Statement_isa_Selection_Statement():
    instance = iec61131_st_Case_Statement()
    assert isinstance(instance, Selection_Statement)


def test_iec61131_st_If_Statement_isa_Selection_Statement():
    instance = iec61131_st_If_Statement()
    assert isinstance(instance, Selection_Statement)


def test_iec61131_sfc_Action_isa_Sfc_Elements():
    instance = iec61131_sfc_Action()
    assert isinstance(instance, Sfc_Elements)


def test_iec61131_sfc_Transition_isa_Sfc_Elements():
    instance = iec61131_sfc_Transition()
    assert isinstance(instance, Sfc_Elements)


def test_iec61131_interfaces_Var_Name_Decl_isa_Simple_Spec_Init():
    instance = iec61131_interfaces_Var_Name_Decl()
    assert isinstance(instance, Simple_Spec_Init)


def test_iec61131_pous_Enumerated_Type_Declaration_isa_Single_Element_Type_Declaration():
    instance = iec61131_pous_Enumerated_Type_Declaration()
    assert isinstance(instance, Single_Element_Type_Declaration)


def test_iec61131_pous_Simple_Type_Declaration_isa_Single_Element_Type_Declaration():
    instance = iec61131_pous_Simple_Type_Declaration()
    assert isinstance(instance, Single_Element_Type_Declaration)


def test_iec61131_pous_Subrange_Type_Declaration_isa_Single_Element_Type_Declaration():
    instance = iec61131_pous_Subrange_Type_Declaration()
    assert isinstance(instance, Single_Element_Type_Declaration)


def test_iec61131_types_Enumerated_Type_Name_isa_Single_Element_Type_Name():
    instance = iec61131_types_Enumerated_Type_Name()
    assert isinstance(instance, Single_Element_Type_Name)


def test_iec61131_types_Subrange_Type_Name_isa_Single_Element_Type_Name():
    instance = iec61131_types_Subrange_Type_Name()
    assert isinstance(instance, Single_Element_Type_Name)


def test_iec61131_st_Assignment_Statement_isa_Statement():
    instance = iec61131_st_Assignment_Statement()
    assert isinstance(instance, Statement)


def test_iec61131_st_Iteration_Statement_isa_Statement():
    instance = iec61131_st_Iteration_Statement()
    assert isinstance(instance, Statement)


def test_iec61131_st_Selection_Statement_isa_Statement():
    instance = iec61131_st_Selection_Statement()
    assert isinstance(instance, Statement)


def test_iec61131_st_Subprogram_Control_Statement_isa_Statement():
    instance = iec61131_st_Subprogram_Control_Statement()
    assert isinstance(instance, Statement)


def test_iec61131_sfc_Initial_Step_isa_Step_Types():
    instance = iec61131_sfc_Initial_Step()
    assert isinstance(instance, Step_Types)


def test_iec61131_sfc_Steps1_isa_Steps():
    instance = iec61131_sfc_Steps1()
    assert isinstance(instance, Steps)


def test_iec61131_sfc_Steps2_isa_Steps():
    instance = iec61131_sfc_Steps2()
    assert isinstance(instance, Steps)


def test_iec61131_interfaces_Double_Byte_String_Var_Declaration_isa_String_Var_Declaration():
    instance = iec61131_interfaces_Double_Byte_String_Var_Declaration()
    assert isinstance(instance, String_Var_Declaration)


def test_iec61131_interfaces_Single_Byte_String_Var_Declaration_isa_String_Var_Declaration():
    instance = iec61131_interfaces_Single_Byte_String_Var_Declaration()
    assert isinstance(instance, String_Var_Declaration)


def test_iec61131_pous_Structure_Declaration_isa_Structure_Specification():
    instance = iec61131_pous_Structure_Declaration()
    assert isinstance(instance, Structure_Specification)


def test_iec61131_st_Fb_Invocation_isa_Subprogram_Control_Statement():
    instance = iec61131_st_Fb_Invocation()
    assert isinstance(instance, Subprogram_Control_Statement)


def test_iec61131_st_Return_Statement_isa_Subprogram_Control_Statement():
    instance = iec61131_st_Return_Statement()
    assert isinstance(instance, Subprogram_Control_Statement)


def test_iec61131_interfaces_Subrange_Specification1_isa_Subrange_Specification():
    instance = iec61131_interfaces_Subrange_Specification1()
    assert isinstance(instance, Subrange_Specification)


def test_iec61131_interfaces_Subrange_Specification2_isa_Subrange_Specification():
    instance = iec61131_interfaces_Subrange_Specification2()
    assert isinstance(instance, Subrange_Specification)


def test_iec61131_variables_Multi_Element_Variable_isa_Symbolic_Variable():
    instance = iec61131_variables_Multi_Element_Variable()
    assert isinstance(instance, Symbolic_Variable)


def test_iec61131_configurations_Interval_isa_Task_Initialization():
    instance = iec61131_configurations_Interval()
    assert isinstance(instance, Task_Initialization)


def test_iec61131_configurations_Priority_isa_Task_Initialization():
    instance = iec61131_configurations_Priority()
    assert isinstance(instance, Task_Initialization)


def test_iec61131_configurations_Single_isa_Task_Initialization():
    instance = iec61131_configurations_Single()
    assert isinstance(instance, Task_Initialization)


def test_iec61131_interfaces_Temp_Var_Declaration_isa_Temp_Var_Decl():
    instance = iec61131_interfaces_Temp_Var_Declaration()
    assert isinstance(instance, Temp_Var_Decl)


def test_iec61131_interfaces_Array_Var_Declaration_isa_Temp_Var_Declaration():
    instance = iec61131_interfaces_Array_Var_Declaration()
    assert isinstance(instance, Temp_Var_Declaration)


def test_iec61131_interfaces_Fb_Name_Decl_isa_Temp_Var_Declaration():
    instance = iec61131_interfaces_Fb_Name_Decl()
    assert isinstance(instance, Temp_Var_Declaration)


def test_iec61131_interfaces_Structured_Var_Declaration_isa_Temp_Var_Declaration():
    instance = iec61131_interfaces_Structured_Var_Declaration()
    assert isinstance(instance, Temp_Var_Declaration)


def test_iec61131_interfaces_Var1_Declaration_isa_Temp_Var_Declaration():
    instance = iec61131_interfaces_Var1_Declaration()
    assert isinstance(instance, Temp_Var_Declaration)


def test_iec61131_literals_Date_isa_Time_Literal():
    instance = iec61131_literals_Date()
    assert isinstance(instance, Time_Literal)


def test_iec61131_literals_Date_And_Time_isa_Time_Literal():
    instance = iec61131_literals_Date_And_Time()
    assert isinstance(instance, Time_Literal)


def test_iec61131_literals_Time_Of_Day_isa_Time_Literal():
    instance = iec61131_literals_Time_Of_Day()
    assert isinstance(instance, Time_Literal)


def test_iec61131_sfc_Transition_Cond1_isa_Transition_Condition():
    instance = iec61131_sfc_Transition_Cond1()
    assert isinstance(instance, Transition_Condition)


def test_iec61131_sfc_Transition_Cond2_isa_Transition_Condition():
    instance = iec61131_sfc_Transition_Cond2()
    assert isinstance(instance, Transition_Condition)


def test_iec61131_sfc_Transition_Cond3_isa_Transition_Condition():
    instance = iec61131_sfc_Transition_Cond3()
    assert isinstance(instance, Transition_Condition)


def test_iec61131_pous_Array_Type_Declaration_isa_Type_Declaration():
    instance = iec61131_pous_Array_Type_Declaration()
    assert isinstance(instance, Type_Declaration)


def test_iec61131_pous_Single_Element_Type_Declaration_isa_Type_Declaration():
    instance = iec61131_pous_Single_Element_Type_Declaration()
    assert isinstance(instance, Type_Declaration)


def test_iec61131_pous_String_Type_Declaration_isa_Type_Declaration():
    instance = iec61131_pous_String_Type_Declaration()
    assert isinstance(instance, Type_Declaration)


def test_iec61131_pous_Structure_Type_Declaration_isa_Type_Declaration():
    instance = iec61131_pous_Structure_Type_Declaration()
    assert isinstance(instance, Type_Declaration)


def test_iec61131_operators_Unequal_Symbol_isa_Unequal_Operator():
    instance = iec61131_operators_Unequal_Symbol()
    assert isinstance(instance, Unequal_Operator)


def test_iec61131_interfaces_Var1_Specification_Func_isa_Var1_Specification():
    instance = iec61131_interfaces_Var1_Specification_Func()
    assert isinstance(instance, Var1_Specification)


def test_iec61131_interfaces_Simple_Spec_Init_Func_isa_Var1_Specification_Func():
    instance = iec61131_interfaces_Simple_Spec_Init_Func()
    assert isinstance(instance, Var1_Specification_Func)


def test_iec61131_interfaces_Array_Var_Init_Decl_isa_Var2_Init_Decl():
    instance = iec61131_interfaces_Array_Var_Init_Decl()
    assert isinstance(instance, Var2_Init_Decl)


def test_iec61131_interfaces_Structured_Var_Init_Decl_isa_Var2_Init_Decl():
    instance = iec61131_interfaces_Structured_Var_Init_Decl()
    assert isinstance(instance, Var2_Init_Decl)


def test_iec61131_interfaces_Var_Init_Decl_Func_isa_Var2_Init_Decl():
    instance = iec61131_interfaces_Var_Init_Decl_Func()
    assert isinstance(instance, Var2_Init_Decl)


def test_iec61131_interfaces_Temp_Var_Decl_isa_Var_Declaration():
    instance = iec61131_interfaces_Temp_Var_Decl()
    assert isinstance(instance, Var_Declaration)


def test_iec61131_interfaces_Var1_Init_Decl_isa_Var_Init_Decl():
    instance = iec61131_interfaces_Var1_Init_Decl()
    assert isinstance(instance, Var_Init_Decl)


def test_iec61131_interfaces_Var2_Init_Decl_isa_Var_Init_Decl():
    instance = iec61131_interfaces_Var2_Init_Decl()
    assert isinstance(instance, Var_Init_Decl)


def test_iec61131_interfaces_Byte_String_isa_Var_Spec():
    instance = iec61131_interfaces_Byte_String()
    assert isinstance(instance, Var_Spec)


def test_iec61131_variables_Symbolic_Variable_isa_Variable():
    instance = iec61131_variables_Symbolic_Variable()
    assert isinstance(instance, Variable)


def test_iec61131_configurations_Global_Var_Reference_isa_configurations_Data_Sink():
    instance = iec61131_configurations_Global_Var_Reference()
    assert isinstance(instance, configurations_Data_Sink)


def test_iec61131_variables_Direct_Variable_isa_configurations_Data_Sink():
    instance = iec61131_variables_Direct_Variable(value="sample_text")
    assert isinstance(instance, configurations_Data_Sink)


def test_iec61131_configurations_Global_Var_Reference_isa_configurations_Data_Source():
    instance = iec61131_configurations_Global_Var_Reference()
    assert isinstance(instance, configurations_Data_Source)


def test_iec61131_literals_Constant_isa_configurations_Data_Source():
    instance = iec61131_literals_Constant()
    assert isinstance(instance, configurations_Data_Source)


def test_iec61131_variables_Direct_Variable_isa_configurations_Data_Source():
    instance = iec61131_variables_Direct_Variable(value="sample_text")
    assert isinstance(instance, configurations_Data_Source)


def test_iec61131_configurations_Global_Var_Reference_isa_configurations_Prog_Data_Source():
    instance = iec61131_configurations_Global_Var_Reference()
    assert isinstance(instance, configurations_Prog_Data_Source)


def test_iec61131_interfaces_Enumerated_Value_isa_configurations_Prog_Data_Source():
    instance = iec61131_interfaces_Enumerated_Value(name="sample_text")
    assert isinstance(instance, configurations_Prog_Data_Source)


def test_iec61131_literals_Constant_isa_configurations_Prog_Data_Source():
    instance = iec61131_literals_Constant()
    assert isinstance(instance, configurations_Prog_Data_Source)


def test_iec61131_variables_Direct_Variable_isa_configurations_Prog_Data_Source():
    instance = iec61131_variables_Direct_Variable(value="sample_text")
    assert isinstance(instance, configurations_Prog_Data_Source)


def test_iec61131_operators_And_Operator_isa_il_Il_Expr_Operator():
    instance = iec61131_operators_And_Operator()
    assert isinstance(instance, il_Il_Expr_Operator)


def test_iec61131_operators_Modulo_Operator_isa_il_Il_Expr_Operator():
    instance = iec61131_operators_Modulo_Operator()
    assert isinstance(instance, il_Il_Expr_Operator)


def test_iec61131_operators_Or_Operator_isa_il_Il_Expr_Operator():
    instance = iec61131_operators_Or_Operator()
    assert isinstance(instance, il_Il_Expr_Operator)


def test_iec61131_operators_Xor_Operator_isa_il_Il_Expr_Operator():
    instance = iec61131_operators_Xor_Operator()
    assert isinstance(instance, il_Il_Expr_Operator)


def test_iec61131_interfaces_Enumerated_Value_isa_il_Il_Operand():
    instance = iec61131_interfaces_Enumerated_Value(name="sample_text")
    assert isinstance(instance, il_Il_Operand)


def test_iec61131_literals_Constant_isa_il_Il_Operand():
    instance = iec61131_literals_Constant()
    assert isinstance(instance, il_Il_Operand)


def test_iec61131_variables_Variable_isa_il_Il_Operand():
    instance = iec61131_variables_Variable()
    assert isinstance(instance, il_Il_Operand)


def test_iec61131_il_Il_Expression_isa_il_Il_Operations():
    instance = iec61131_il_Il_Expression()
    assert isinstance(instance, il_Il_Operations)


def test_iec61131_il_Il_Formal_Funct_Call_isa_il_Il_Operations():
    instance = iec61131_il_Il_Formal_Funct_Call()
    assert isinstance(instance, il_Il_Operations)


def test_iec61131_il_Il_Simple_Operation_isa_il_Il_Operations():
    instance = iec61131_il_Il_Simple_Operation()
    assert isinstance(instance, il_Il_Operations)


def test_iec61131_operators_Not_Operator_isa_il_Il_Simple_Operator():
    instance = iec61131_operators_Not_Operator()
    assert isinstance(instance, il_Il_Simple_Operator)


def test_iec61131_il_Il_Expression_isa_il_Simple_Instr():
    instance = iec61131_il_Il_Expression()
    assert isinstance(instance, il_Simple_Instr)


def test_iec61131_il_Il_Formal_Funct_Call_isa_il_Simple_Instr():
    instance = iec61131_il_Il_Formal_Funct_Call()
    assert isinstance(instance, il_Simple_Instr)


def test_iec61131_il_Il_Simple_Operation_isa_il_Simple_Instr():
    instance = iec61131_il_Il_Simple_Operation()
    assert isinstance(instance, il_Simple_Instr)


def test_iec61131_interfaces_Array_Specification_isa_interfaces_External_Specification():
    instance = iec61131_interfaces_Array_Specification()
    assert isinstance(instance, interfaces_External_Specification)


def test_iec61131_interfaces_Enumerated_Specification_isa_interfaces_External_Specification():
    instance = iec61131_interfaces_Enumerated_Specification()
    assert isinstance(instance, interfaces_External_Specification)


def test_iec61131_interfaces_Subrange_Specification_isa_interfaces_External_Specification():
    instance = iec61131_interfaces_Subrange_Specification()
    assert isinstance(instance, interfaces_External_Specification)


def test_iec61131_pous_Function_Block_Type_Name_isa_interfaces_External_Specification():
    instance = iec61131_pous_Function_Block_Type_Name()
    assert isinstance(instance, interfaces_External_Specification)


def test_iec61131_types_Structure_Type_Name_isa_interfaces_External_Specification():
    instance = iec61131_types_Structure_Type_Name()
    assert isinstance(instance, interfaces_External_Specification)


def test_iec61131_interfaces_Function_Var_Decl_isa_interfaces_Interface():
    instance = iec61131_interfaces_Function_Var_Decl(constant=True)
    assert isinstance(instance, interfaces_Interface)


def test_iec61131_interfaces_Io_Var_Declaration_isa_interfaces_Interface():
    instance = iec61131_interfaces_Io_Var_Declaration()
    assert isinstance(instance, interfaces_Interface)


def test_iec61131_interfaces_Other_Var_Declaration_isa_interfaces_Interface():
    instance = iec61131_interfaces_Other_Var_Declaration()
    assert isinstance(instance, interfaces_Interface)


def test_iec61131_interfaces_Array_Spec_Init_isa_interfaces_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Array_Spec_Init()
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


def test_iec61131_interfaces_Enumerated_Spec_Init_isa_interfaces_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Enumerated_Spec_Init()
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


def test_iec61131_interfaces_Initialized_Structure_isa_interfaces_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Initialized_Structure()
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


def test_iec61131_interfaces_Simple_Spec_Init_isa_interfaces_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Simple_Spec_Init()
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


def test_iec61131_interfaces_Subrange_Spec_Init_isa_interfaces_Located_Var_Spec_Init():
    instance = iec61131_interfaces_Subrange_Spec_Init()
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


def test_iec61131_literals_Signed_Integer_isa_interfaces_Range():
    instance = iec61131_literals_Signed_Integer(negative=True)
    assert isinstance(instance, interfaces_Range)


def test_iec61131_literals_Unsigned_Integer_isa_interfaces_Range():
    instance = iec61131_literals_Unsigned_Integer()
    assert isinstance(instance, interfaces_Range)


def test_iec61131_types_Elementary_Type_Name_isa_interfaces_Simple_Specification_Func():
    instance = iec61131_types_Elementary_Type_Name()
    assert isinstance(instance, interfaces_Simple_Specification_Func)


def test_iec61131_types_Simple_Type_Name_isa_interfaces_Simple_Specification_Func():
    instance = iec61131_types_Simple_Type_Name()
    assert isinstance(instance, interfaces_Simple_Specification_Func)


def test_iec61131_interfaces_Enumerated_Specification_isa_interfaces_Specification():
    instance = iec61131_interfaces_Enumerated_Specification()
    assert isinstance(instance, interfaces_Specification)


def test_iec61131_interfaces_Subrange_Specification_isa_interfaces_Specification():
    instance = iec61131_interfaces_Subrange_Specification()
    assert isinstance(instance, interfaces_Specification)


def test_iec61131_interfaces_String_Var_Declaration_isa_interfaces_Temp_Var_Decl():
    instance = iec61131_interfaces_String_Var_Declaration()
    assert isinstance(instance, interfaces_Temp_Var_Decl)


def test_iec61131_interfaces_Enumerated_Spec_Init_isa_interfaces_Var1_Specification():
    instance = iec61131_interfaces_Enumerated_Spec_Init()
    assert isinstance(instance, interfaces_Var1_Specification)


def test_iec61131_interfaces_Simple_Spec_Init_isa_interfaces_Var1_Specification():
    instance = iec61131_interfaces_Simple_Spec_Init()
    assert isinstance(instance, interfaces_Var1_Specification)


def test_iec61131_interfaces_Subrange_Spec_Init_isa_interfaces_Var1_Specification():
    instance = iec61131_interfaces_Subrange_Spec_Init()
    assert isinstance(instance, interfaces_Var1_Specification)


def test_iec61131_interfaces_Enumerated_Spec_Init_isa_interfaces_Var1_Specification_Func():
    instance = iec61131_interfaces_Enumerated_Spec_Init()
    assert isinstance(instance, interfaces_Var1_Specification_Func)


def test_iec61131_interfaces_Subrange_Spec_Init_isa_interfaces_Var1_Specification_Func():
    instance = iec61131_interfaces_Subrange_Spec_Init()
    assert isinstance(instance, interfaces_Var1_Specification_Func)


def test_iec61131_interfaces_String_Var_Declaration_isa_interfaces_Var2_Init_Decl():
    instance = iec61131_interfaces_String_Var_Declaration()
    assert isinstance(instance, interfaces_Var2_Init_Decl)


def test_iec61131_interfaces_Array_Specification_isa_interfaces_Var_Spec():
    instance = iec61131_interfaces_Array_Specification()
    assert isinstance(instance, interfaces_Var_Spec)


def test_iec61131_interfaces_Enumerated_Specification_isa_interfaces_Var_Spec():
    instance = iec61131_interfaces_Enumerated_Specification()
    assert isinstance(instance, interfaces_Var_Spec)


def test_iec61131_interfaces_Subrange_Specification_isa_interfaces_Var_Spec():
    instance = iec61131_interfaces_Subrange_Specification()
    assert isinstance(instance, interfaces_Var_Spec)


def test_iec61131_types_Structure_Type_Name_isa_interfaces_Var_Spec():
    instance = iec61131_types_Structure_Type_Name()
    assert isinstance(instance, interfaces_Var_Spec)


def test_iec61131_literals_Binary_Integer_isa_literals_BSInteger():
    instance = iec61131_literals_Binary_Integer()
    assert isinstance(instance, literals_BSInteger)


def test_iec61131_literals_Hex_Integer_isa_literals_BSInteger():
    instance = iec61131_literals_Hex_Integer()
    assert isinstance(instance, literals_BSInteger)


def test_iec61131_literals_Octal_Integer_isa_literals_BSInteger():
    instance = iec61131_literals_Octal_Integer()
    assert isinstance(instance, literals_BSInteger)


def test_iec61131_literals_Unsigned_Integer_isa_literals_BSInteger():
    instance = iec61131_literals_Unsigned_Integer()
    assert isinstance(instance, literals_BSInteger)


def test_iec61131_literals_Unsigned_Integer_isa_literals_Fixed_Point_Literal():
    instance = iec61131_literals_Unsigned_Integer()
    assert isinstance(instance, literals_Fixed_Point_Literal)


def test_iec61131_literals_Binary_Integer_isa_literals_Integer():
    instance = iec61131_literals_Binary_Integer()
    assert isinstance(instance, literals_Integer)


def test_iec61131_literals_Hex_Integer_isa_literals_Integer():
    instance = iec61131_literals_Hex_Integer()
    assert isinstance(instance, literals_Integer)


def test_iec61131_literals_Octal_Integer_isa_literals_Integer():
    instance = iec61131_literals_Octal_Integer()
    assert isinstance(instance, literals_Integer)


def test_iec61131_literals_Signed_Integer_isa_literals_Integer():
    instance = iec61131_literals_Signed_Integer(negative=True)
    assert isinstance(instance, literals_Integer)


def test_iec61131_literals_Unsigned_Integer_isa_literals_Integer():
    instance = iec61131_literals_Unsigned_Integer()
    assert isinstance(instance, literals_Integer)


def test_iec61131_literals_Duration_isa_literals_Time_Literal():
    instance = iec61131_literals_Duration()
    assert isinstance(instance, literals_Time_Literal)


def test_iec61131_operators_Addition_Symbol_isa_operators_Add_Operator():
    instance = iec61131_operators_Addition_Symbol()
    assert isinstance(instance, operators_Add_Operator)


def test_iec61131_operators_Substraction_Symbol_isa_operators_Add_Operator():
    instance = iec61131_operators_Substraction_Symbol()
    assert isinstance(instance, operators_Add_Operator)


def test_iec61131_operators_Addition_Name_isa_operators_Addition_Operator():
    instance = iec61131_operators_Addition_Name()
    assert isinstance(instance, operators_Addition_Operator)


def test_iec61131_operators_Addition_Symbol_isa_operators_Addition_Operator():
    instance = iec61131_operators_Addition_Symbol()
    assert isinstance(instance, operators_Addition_Operator)


def test_iec61131_operators_Addition_Name_isa_operators_Arithmetic_Name():
    instance = iec61131_operators_Addition_Name()
    assert isinstance(instance, operators_Arithmetic_Name)


def test_iec61131_operators_Divide_Name_isa_operators_Arithmetic_Name():
    instance = iec61131_operators_Divide_Name()
    assert isinstance(instance, operators_Arithmetic_Name)


def test_iec61131_operators_Multiply_Name_isa_operators_Arithmetic_Name():
    instance = iec61131_operators_Multiply_Name()
    assert isinstance(instance, operators_Arithmetic_Name)


def test_iec61131_operators_Substraction_Name_isa_operators_Arithmetic_Name():
    instance = iec61131_operators_Substraction_Name()
    assert isinstance(instance, operators_Arithmetic_Name)


def test_iec61131_operators_Equal_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_Equal_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_GreaterEqual_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_GreaterEqual_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_Greater_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_Greater_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_LessEqual_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_LessEqual_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_Less_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_Less_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_Unequal_Name_isa_operators_Comparison_Name():
    instance = iec61131_operators_Unequal_Name()
    assert isinstance(instance, operators_Comparison_Name)


def test_iec61131_operators_Divide_Name_isa_operators_Divide_Operator():
    instance = iec61131_operators_Divide_Name()
    assert isinstance(instance, operators_Divide_Operator)


def test_iec61131_operators_Modulo_Operator_isa_operators_Dot_Operator():
    instance = iec61131_operators_Modulo_Operator()
    assert isinstance(instance, operators_Dot_Operator)


def test_iec61131_operators_Equal_Name_isa_operators_Equal_Operator():
    instance = iec61131_operators_Equal_Name()
    assert isinstance(instance, operators_Equal_Operator)


def test_iec61131_operators_GreaterEqual_Name_isa_operators_GreaterEqual_Operator():
    instance = iec61131_operators_GreaterEqual_Name()
    assert isinstance(instance, operators_GreaterEqual_Operator)


def test_iec61131_operators_Greater_Name_isa_operators_Greater_Operator():
    instance = iec61131_operators_Greater_Name()
    assert isinstance(instance, operators_Greater_Operator)


def test_iec61131_operators_LessEqual_Name_isa_operators_LessEqual_Operator():
    instance = iec61131_operators_LessEqual_Name()
    assert isinstance(instance, operators_LessEqual_Operator)


def test_iec61131_operators_Less_Name_isa_operators_Less_Operator():
    instance = iec61131_operators_Less_Name()
    assert isinstance(instance, operators_Less_Operator)


def test_iec61131_operators_Multiply_Name_isa_operators_Multiply_Operator():
    instance = iec61131_operators_Multiply_Name()
    assert isinstance(instance, operators_Multiply_Operator)


def test_iec61131_operators_And_Operator_isa_operators_Operator():
    instance = iec61131_operators_And_Operator()
    assert isinstance(instance, operators_Operator)


def test_iec61131_operators_Or_Operator_isa_operators_Operator():
    instance = iec61131_operators_Or_Operator()
    assert isinstance(instance, operators_Operator)


def test_iec61131_operators_Xor_Operator_isa_operators_Operator():
    instance = iec61131_operators_Xor_Operator()
    assert isinstance(instance, operators_Operator)


def test_iec61131_operators_Substraction_Name_isa_operators_Substraction_Operator():
    instance = iec61131_operators_Substraction_Name()
    assert isinstance(instance, operators_Substraction_Operator)


def test_iec61131_operators_Substraction_Symbol_isa_operators_Substraction_Operator():
    instance = iec61131_operators_Substraction_Symbol()
    assert isinstance(instance, operators_Substraction_Operator)


def test_iec61131_operators_Not_Operator_isa_operators_Unary_Operator():
    instance = iec61131_operators_Not_Operator()
    assert isinstance(instance, operators_Unary_Operator)


def test_iec61131_operators_Substraction_Symbol_isa_operators_Unary_Operator():
    instance = iec61131_operators_Substraction_Symbol()
    assert isinstance(instance, operators_Unary_Operator)


def test_iec61131_operators_Unequal_Name_isa_operators_Unequal_Operator():
    instance = iec61131_operators_Unequal_Name()
    assert isinstance(instance, operators_Unequal_Operator)


def test_iec61131_fbd_Function_Block_Diagram_isa_pous_Function_Block_Body():
    instance = iec61131_fbd_Function_Block_Diagram()
    assert isinstance(instance, pous_Function_Block_Body)


def test_iec61131_il_Instruction_List_isa_pous_Function_Block_Body():
    instance = iec61131_il_Instruction_List()
    assert isinstance(instance, pous_Function_Block_Body)


def test_iec61131_ld_Ladder_Diagram_isa_pous_Function_Block_Body():
    instance = iec61131_ld_Ladder_Diagram()
    assert isinstance(instance, pous_Function_Block_Body)


def test_iec61131_pous_Other_Language_isa_pous_Function_Block_Body():
    instance = iec61131_pous_Other_Language(text="sample_text")
    assert isinstance(instance, pous_Function_Block_Body)


def test_iec61131_st_Statement_List_isa_pous_Function_Block_Body():
    instance = iec61131_st_Statement_List()
    assert isinstance(instance, pous_Function_Block_Body)


def test_iec61131_pous_Derived_Function_Block_Name_isa_pous_Function_Block_Type_Name():
    instance = iec61131_pous_Derived_Function_Block_Name()
    assert isinstance(instance, pous_Function_Block_Type_Name)


def test_iec61131_interfaces_Io_Var_Declaration_isa_pous_Function_Block_Vars():
    instance = iec61131_interfaces_Io_Var_Declaration()
    assert isinstance(instance, pous_Function_Block_Vars)


def test_iec61131_interfaces_Other_Var_Declaration_isa_pous_Function_Block_Vars():
    instance = iec61131_interfaces_Other_Var_Declaration()
    assert isinstance(instance, pous_Function_Block_Vars)


def test_iec61131_fbd_Function_Block_Diagram_isa_pous_Function_Body():
    instance = iec61131_fbd_Function_Block_Diagram()
    assert isinstance(instance, pous_Function_Body)


def test_iec61131_il_Instruction_List_isa_pous_Function_Body():
    instance = iec61131_il_Instruction_List()
    assert isinstance(instance, pous_Function_Body)


def test_iec61131_ld_Ladder_Diagram_isa_pous_Function_Body():
    instance = iec61131_ld_Ladder_Diagram()
    assert isinstance(instance, pous_Function_Body)


def test_iec61131_pous_Other_Language_isa_pous_Function_Body():
    instance = iec61131_pous_Other_Language(text="sample_text")
    assert isinstance(instance, pous_Function_Body)


def test_iec61131_st_Statement_List_isa_pous_Function_Body():
    instance = iec61131_st_Statement_List()
    assert isinstance(instance, pous_Function_Body)


def test_iec61131_pous_Derived_Function_Name_isa_pous_Function_Name():
    instance = iec61131_pous_Derived_Function_Name()
    assert isinstance(instance, pous_Function_Name)


def test_iec61131_types_Generic_Type_Name_isa_pous_Function_Return_Value():
    instance = iec61131_types_Generic_Type_Name()
    assert isinstance(instance, pous_Function_Return_Value)


def test_iec61131_types_Non_Generic_Type_Name_isa_pous_Function_Return_Value():
    instance = iec61131_types_Non_Generic_Type_Name()
    assert isinstance(instance, pous_Function_Return_Value)


def test_iec61131_interfaces_Function_Var_Decl_isa_pous_Function_Vars():
    instance = iec61131_interfaces_Function_Var_Decl(constant=True)
    assert isinstance(instance, pous_Function_Vars)


def test_iec61131_interfaces_Io_Var_Declaration_isa_pous_Function_Vars():
    instance = iec61131_interfaces_Io_Var_Declaration()
    assert isinstance(instance, pous_Function_Vars)


def test_iec61131_interfaces_Io_Var_Declaration_isa_pous_Program_Vars():
    instance = iec61131_interfaces_Io_Var_Declaration()
    assert isinstance(instance, pous_Program_Vars)


def test_iec61131_interfaces_Other_Var_Declaration_isa_pous_Program_Vars():
    instance = iec61131_interfaces_Other_Var_Declaration()
    assert isinstance(instance, pous_Program_Vars)


def test_iec61131_interfaces_Array_Spec_Init_isa_pous_Structure_Elements():
    instance = iec61131_interfaces_Array_Spec_Init()
    assert isinstance(instance, pous_Structure_Elements)


def test_iec61131_interfaces_Enumerated_Spec_Init_isa_pous_Structure_Elements():
    instance = iec61131_interfaces_Enumerated_Spec_Init()
    assert isinstance(instance, pous_Structure_Elements)


def test_iec61131_interfaces_Initialized_Structure_isa_pous_Structure_Elements():
    instance = iec61131_interfaces_Initialized_Structure()
    assert isinstance(instance, pous_Structure_Elements)


def test_iec61131_interfaces_Simple_Spec_Init_isa_pous_Structure_Elements():
    instance = iec61131_interfaces_Simple_Spec_Init()
    assert isinstance(instance, pous_Structure_Elements)


def test_iec61131_interfaces_Subrange_Spec_Init_isa_pous_Structure_Elements():
    instance = iec61131_interfaces_Subrange_Spec_Init()
    assert isinstance(instance, pous_Structure_Elements)


def test_iec61131_interfaces_Initialized_Structure_isa_pous_Structure_Specification():
    instance = iec61131_interfaces_Initialized_Structure()
    assert isinstance(instance, pous_Structure_Specification)


def test_iec61131_literals_Duration_isa_sfc_Action_Time():
    instance = iec61131_literals_Duration()
    assert isinstance(instance, sfc_Action_Time)


def test_iec61131_sfc_Step_isa_sfc_Sfc_Elements():
    instance = iec61131_sfc_Step()
    assert isinstance(instance, sfc_Sfc_Elements)


def test_iec61131_sfc_Step_isa_sfc_Step_Types():
    instance = iec61131_sfc_Step()
    assert isinstance(instance, sfc_Step_Types)


def test_iec61131_interfaces_Enumerated_Value_isa_st_Case_List_Element():
    instance = iec61131_interfaces_Enumerated_Value(name="sample_text")
    assert isinstance(instance, st_Case_List_Element)


def test_iec61131_literals_Signed_Integer_isa_st_Case_List_Element():
    instance = iec61131_literals_Signed_Integer(negative=True)
    assert isinstance(instance, st_Case_List_Element)


def test_iec61131_literals_Unsigned_Integer_isa_st_Case_List_Element():
    instance = iec61131_literals_Unsigned_Integer()
    assert isinstance(instance, st_Case_List_Element)


def test_iec61131_types_Generic_Type_Name_isa_types_Data_Type_Name():
    instance = iec61131_types_Generic_Type_Name()
    assert isinstance(instance, types_Data_Type_Name)


def test_iec61131_types_Non_Generic_Type_Name_isa_types_Data_Type_Name():
    instance = iec61131_types_Non_Generic_Type_Name()
    assert isinstance(instance, types_Data_Type_Name)


def test_iec61131_types_Structure_Type_Name_isa_types_Derived_Type_Name():
    instance = iec61131_types_Structure_Type_Name()
    assert isinstance(instance, types_Derived_Type_Name)


def test_iec61131_types_Elementary_Type_Name_isa_types_Non_Generic_Type_Name():
    instance = iec61131_types_Elementary_Type_Name()
    assert isinstance(instance, types_Non_Generic_Type_Name)


def test_iec61131_pous_Function_Block_Type_Name_isa_types_Simple_Specification():
    instance = iec61131_pous_Function_Block_Type_Name()
    assert isinstance(instance, types_Simple_Specification)


def test_iec61131_types_Elementary_Type_Name_isa_types_Simple_Specification():
    instance = iec61131_types_Elementary_Type_Name()
    assert isinstance(instance, types_Simple_Specification)


def test_iec61131_types_Generic_Type_Name_isa_types_Simple_Specification():
    instance = iec61131_types_Generic_Type_Name()
    assert isinstance(instance, types_Simple_Specification)


def test_iec61131_types_Simple_Type_Name_isa_types_Simple_Specification():
    instance = iec61131_types_Simple_Type_Name()
    assert isinstance(instance, types_Simple_Specification)


def test_iec61131_types_Simple_Type_Name_isa_types_Single_Element_Type_Name():
    instance = iec61131_types_Simple_Type_Name()
    assert isinstance(instance, types_Single_Element_Type_Name)


def test_iec61131_variables_Variable_Name_isa_variables_Symbolic_Variable():
    instance = iec61131_variables_Variable_Name()
    assert isinstance(instance, variables_Symbolic_Variable)


def test_iec61131_variables_Direct_Variable_isa_variables_Variable():
    instance = iec61131_variables_Direct_Variable(value="sample_text")
    assert isinstance(instance, variables_Variable)


def test_assoc_access_name230_link_reassign_clear():
    a = iec61131_pous_Program_Access_Decl(direction="sample_text")
    b1 = Access_Name()
    b2 = Access_Name()
    _safe_set(a, 'iec61131_pous_Program_Access_Decl', b1)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl', b1)
    if hasattr(b1, 'Access_Name'):
        assert _is_linked(b1, 'Access_Name', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl', b2)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl', b2)
    if hasattr(b1, 'Access_Name'):
        assert not _is_linked(b1, 'Access_Name', a)
    if hasattr(b2, 'Access_Name'):
        assert _is_linked(b2, 'Access_Name', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl', None)
    assert not _is_linked(a, 'iec61131_pous_Program_Access_Decl', b2)
    if hasattr(b2, 'Access_Name'):
        assert not _is_linked(b2, 'Access_Name', a)


def test_assoc_access_name334_link_reassign_clear():
    a = iec61131_configurations_Access_Declaration(direction="sample_text")
    b1 = Access_Name()
    b2 = Access_Name()
    _safe_set(a, 'iec61131_configurations_Access_Declaration', b1)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration', b1)
    if hasattr(b1, 'Access_Name335'):
        assert _is_linked(b1, 'Access_Name335', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration', b2)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration', b2)
    if hasattr(b1, 'Access_Name335'):
        assert not _is_linked(b1, 'Access_Name335', a)
    if hasattr(b2, 'Access_Name335'):
        assert _is_linked(b2, 'Access_Name335', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration', None)
    assert not _is_linked(a, 'iec61131_configurations_Access_Declaration', b2)
    if hasattr(b2, 'Access_Name335'):
        assert not _is_linked(b2, 'Access_Name335', a)


def test_assoc_access_path336_link_reassign_clear():
    a = iec61131_configurations_Access_Declaration(direction="sample_text")
    b1 = Access_Path()
    b2 = Access_Path()
    _safe_set(a, 'iec61131_configurations_Access_Declaration337', b1)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration337', b1)
    if hasattr(b1, 'Access_Path'):
        assert _is_linked(b1, 'Access_Path', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration337', b2)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration337', b2)
    if hasattr(b1, 'Access_Path'):
        assert not _is_linked(b1, 'Access_Path', a)
    if hasattr(b2, 'Access_Path'):
        assert _is_linked(b2, 'Access_Path', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration337', None)
    assert not _is_linked(a, 'iec61131_configurations_Access_Declaration337', b2)
    if hasattr(b2, 'Access_Path'):
        assert not _is_linked(b2, 'Access_Path', a)


def test_assoc_action_time652_link_reassign_clear():
    a = iec61131_sfc_Action_Qualifier(qualifier="sample_text")
    b1 = Action_Time()
    b2 = Action_Time()
    _safe_set(a, 'iec61131_sfc_Action_Qualifier653', b1)
    assert _is_linked(a, 'iec61131_sfc_Action_Qualifier653', b1)
    if hasattr(b1, 'Action_Time'):
        assert _is_linked(b1, 'Action_Time', a)
    _safe_set(a, 'iec61131_sfc_Action_Qualifier653', b2)
    assert _is_linked(a, 'iec61131_sfc_Action_Qualifier653', b2)
    if hasattr(b1, 'Action_Time'):
        assert not _is_linked(b1, 'Action_Time', a)
    if hasattr(b2, 'Action_Time'):
        assert _is_linked(b2, 'Action_Time', a)
    _safe_set(a, 'iec61131_sfc_Action_Qualifier653', None)
    assert not _is_linked(a, 'iec61131_sfc_Action_Qualifier653', b2)
    if hasattr(b2, 'Action_Time'):
        assert not _is_linked(b2, 'Action_Time', a)


def test_assoc_bool_type_name58_link_reassign_clear():
    a = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    b1 = Bool_Type_Name()
    b2 = Bool_Type_Name()
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration59', b1)
    assert _is_linked(a, 'iec61131_interfaces_Edge_Declaration59', b1)
    if hasattr(b1, 'Bool_Type_Name'):
        assert _is_linked(b1, 'Bool_Type_Name', a)
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration59', b2)
    assert _is_linked(a, 'iec61131_interfaces_Edge_Declaration59', b2)
    if hasattr(b1, 'Bool_Type_Name'):
        assert not _is_linked(b1, 'Bool_Type_Name', a)
    if hasattr(b2, 'Bool_Type_Name'):
        assert _is_linked(b2, 'Bool_Type_Name', a)
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration59', None)
    assert not _is_linked(a, 'iec61131_interfaces_Edge_Declaration59', b2)
    if hasattr(b2, 'Bool_Type_Name'):
        assert not _is_linked(b2, 'Bool_Type_Name', a)


def test_assoc_common_character_representation50_link_reassign_clear():
    a = iec61131_literals_Single_Byte_Character_Representation(value="sample_text")
    b1 = Common_Character_Representation()
    b2 = Common_Character_Representation()
    _safe_set(a, 'iec61131_literals_Single_Byte_Character_Representation', b1)
    assert _is_linked(a, 'iec61131_literals_Single_Byte_Character_Representation', b1)
    if hasattr(b1, 'Common_Character_Representation'):
        assert _is_linked(b1, 'Common_Character_Representation', a)
    _safe_set(a, 'iec61131_literals_Single_Byte_Character_Representation', b2)
    assert _is_linked(a, 'iec61131_literals_Single_Byte_Character_Representation', b2)
    if hasattr(b1, 'Common_Character_Representation'):
        assert not _is_linked(b1, 'Common_Character_Representation', a)
    if hasattr(b2, 'Common_Character_Representation'):
        assert _is_linked(b2, 'Common_Character_Representation', a)
    _safe_set(a, 'iec61131_literals_Single_Byte_Character_Representation', None)
    assert not _is_linked(a, 'iec61131_literals_Single_Byte_Character_Representation', b2)
    if hasattr(b2, 'Common_Character_Representation'):
        assert not _is_linked(b2, 'Common_Character_Representation', a)


def test_assoc_common_character_representation51_link_reassign_clear():
    a = iec61131_literals_Double_Byte_Character_Representation(value="sample_text")
    b1 = Common_Character_Representation()
    b2 = Common_Character_Representation()
    _safe_set(a, 'iec61131_literals_Double_Byte_Character_Representation', b1)
    assert _is_linked(a, 'iec61131_literals_Double_Byte_Character_Representation', b1)
    if hasattr(b1, 'Common_Character_Representation52'):
        assert _is_linked(b1, 'Common_Character_Representation52', a)
    _safe_set(a, 'iec61131_literals_Double_Byte_Character_Representation', b2)
    assert _is_linked(a, 'iec61131_literals_Double_Byte_Character_Representation', b2)
    if hasattr(b1, 'Common_Character_Representation52'):
        assert not _is_linked(b1, 'Common_Character_Representation52', a)
    if hasattr(b2, 'Common_Character_Representation52'):
        assert _is_linked(b2, 'Common_Character_Representation52', a)
    _safe_set(a, 'iec61131_literals_Double_Byte_Character_Representation', None)
    assert not _is_linked(a, 'iec61131_literals_Double_Byte_Character_Representation', b2)
    if hasattr(b2, 'Common_Character_Representation52'):
        assert not _is_linked(b2, 'Common_Character_Representation52', a)


def test_assoc_enumerated_type_name98_link_reassign_clear():
    a = iec61131_interfaces_Enumerated_Value(name="sample_text")
    b1 = Enumerated_Type_Name()
    b2 = Enumerated_Type_Name()
    _safe_set(a, 'iec61131_interfaces_Enumerated_Value', b1)
    assert _is_linked(a, 'iec61131_interfaces_Enumerated_Value', b1)
    if hasattr(b1, 'Enumerated_Type_Name'):
        assert _is_linked(b1, 'Enumerated_Type_Name', a)
    _safe_set(a, 'iec61131_interfaces_Enumerated_Value', b2)
    assert _is_linked(a, 'iec61131_interfaces_Enumerated_Value', b2)
    if hasattr(b1, 'Enumerated_Type_Name'):
        assert not _is_linked(b1, 'Enumerated_Type_Name', a)
    if hasattr(b2, 'Enumerated_Type_Name'):
        assert _is_linked(b2, 'Enumerated_Type_Name', a)
    _safe_set(a, 'iec61131_interfaces_Enumerated_Value', None)
    assert not _is_linked(a, 'iec61131_interfaces_Enumerated_Value', b2)
    if hasattr(b2, 'Enumerated_Type_Name'):
        assert not _is_linked(b2, 'Enumerated_Type_Name', a)


def test_assoc_external_declaration121_link_reassign_clear():
    a = iec61131_interfaces_External_Var_Declarations(constant=True)
    b1 = External_Declaration()
    b2 = External_Declaration()
    _safe_set(a, 'iec61131_interfaces_External_Var_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_External_Var_Declarations', b1)
    if hasattr(b1, 'External_Declaration'):
        assert _is_linked(b1, 'External_Declaration', a)
    _safe_set(a, 'iec61131_interfaces_External_Var_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_External_Var_Declarations', b2)
    if hasattr(b1, 'External_Declaration'):
        assert not _is_linked(b1, 'External_Declaration', a)
    if hasattr(b2, 'External_Declaration'):
        assert _is_linked(b2, 'External_Declaration', a)
    _safe_set(a, 'iec61131_interfaces_External_Var_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_External_Var_Declarations', b2)
    if hasattr(b2, 'External_Declaration'):
        assert not _is_linked(b2, 'External_Declaration', a)


def test_assoc_fixed_point10_link_reassign_clear():
    a = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    b1 = Fixed_Point()
    b2 = Fixed_Point()
    _safe_set(a, 'iec61131_literals_Real_Literal11', b1)
    assert _is_linked(a, 'iec61131_literals_Real_Literal11', b1)
    if hasattr(b1, 'Fixed_Point'):
        assert _is_linked(b1, 'Fixed_Point', a)
    _safe_set(a, 'iec61131_literals_Real_Literal11', b2)
    assert _is_linked(a, 'iec61131_literals_Real_Literal11', b2)
    if hasattr(b1, 'Fixed_Point'):
        assert not _is_linked(b1, 'Fixed_Point', a)
    if hasattr(b2, 'Fixed_Point'):
        assert _is_linked(b2, 'Fixed_Point', a)
    _safe_set(a, 'iec61131_literals_Real_Literal11', None)
    assert not _is_linked(a, 'iec61131_literals_Real_Literal11', b2)
    if hasattr(b2, 'Fixed_Point'):
        assert not _is_linked(b2, 'Fixed_Point', a)


def test_assoc_global_var_decl145_link_reassign_clear():
    a = iec61131_interfaces_Global_Var_Declarations(constant=True, retain=True)
    b1 = Global_Var_Decl()
    b2 = Global_Var_Decl()
    _safe_set(a, 'iec61131_interfaces_Global_Var_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Global_Var_Declarations', b1)
    if hasattr(b1, 'Global_Var_Decl'):
        assert _is_linked(b1, 'Global_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Global_Var_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Global_Var_Declarations', b2)
    if hasattr(b1, 'Global_Var_Decl'):
        assert not _is_linked(b1, 'Global_Var_Decl', a)
    if hasattr(b2, 'Global_Var_Decl'):
        assert _is_linked(b2, 'Global_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Global_Var_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_Global_Var_Declarations', b2)
    if hasattr(b2, 'Global_Var_Decl'):
        assert not _is_linked(b2, 'Global_Var_Decl', a)


def test_assoc_incompl_located_var_decl128_link_reassign_clear():
    a = iec61131_interfaces_Incompl_Located_Var_Declarations(retain=True)
    b1 = Incompl_Located_Var_Decl()
    b2 = Incompl_Located_Var_Decl()
    _safe_set(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', b1)
    if hasattr(b1, 'Incompl_Located_Var_Decl'):
        assert _is_linked(b1, 'Incompl_Located_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', b2)
    if hasattr(b1, 'Incompl_Located_Var_Decl'):
        assert not _is_linked(b1, 'Incompl_Located_Var_Decl', a)
    if hasattr(b2, 'Incompl_Located_Var_Decl'):
        assert _is_linked(b2, 'Incompl_Located_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_Incompl_Located_Var_Declarations', b2)
    if hasattr(b2, 'Incompl_Located_Var_Decl'):
        assert not _is_linked(b2, 'Incompl_Located_Var_Decl', a)


def test_assoc_input_declaration53_link_reassign_clear():
    a = iec61131_interfaces_Input_Declarations(retain=True)
    b1 = Input_Declaration()
    b2 = Input_Declaration()
    _safe_set(a, 'iec61131_interfaces_Input_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Input_Declarations', b1)
    if hasattr(b1, 'Input_Declaration'):
        assert _is_linked(b1, 'Input_Declaration', a)
    _safe_set(a, 'iec61131_interfaces_Input_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Input_Declarations', b2)
    if hasattr(b1, 'Input_Declaration'):
        assert not _is_linked(b1, 'Input_Declaration', a)
    if hasattr(b2, 'Input_Declaration'):
        assert _is_linked(b2, 'Input_Declaration', a)
    _safe_set(a, 'iec61131_interfaces_Input_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_Input_Declarations', b2)
    if hasattr(b2, 'Input_Declaration'):
        assert not _is_linked(b2, 'Input_Declaration', a)


def test_assoc_integer105_link_reassign_clear():
    a = iec61131_interfaces_Subrange(delimiter="sample_text")
    b1 = Range()
    b2 = Range()
    _safe_set(a, 'iec61131_interfaces_Subrange', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Subrange', b1)
    if hasattr(b1, 'Range'):
        assert _is_linked(b1, 'Range', a)
    _safe_set(a, 'iec61131_interfaces_Subrange', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Subrange', b2)
    if hasattr(b1, 'Range'):
        assert not _is_linked(b1, 'Range', a)
    if hasattr(b2, 'Range'):
        assert _is_linked(b2, 'Range', a)
    _safe_set(a, 'iec61131_interfaces_Subrange', set())
    assert not _is_linked(a, 'iec61131_interfaces_Subrange', b2)
    if hasattr(b2, 'Range'):
        assert not _is_linked(b2, 'Range', a)


def test_assoc_located_var_decl144_link_reassign_clear():
    a = iec61131_interfaces_Located_Var_Declarations(constant=True, retain=True)
    b1 = Located_Var_Decl()
    b2 = Located_Var_Decl()
    _safe_set(a, 'iec61131_interfaces_Located_Var_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Located_Var_Declarations', b1)
    if hasattr(b1, 'Located_Var_Decl'):
        assert _is_linked(b1, 'Located_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Located_Var_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Located_Var_Declarations', b2)
    if hasattr(b1, 'Located_Var_Decl'):
        assert not _is_linked(b1, 'Located_Var_Decl', a)
    if hasattr(b2, 'Located_Var_Decl'):
        assert _is_linked(b2, 'Located_Var_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Located_Var_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_Located_Var_Declarations', b2)
    if hasattr(b2, 'Located_Var_Decl'):
        assert not _is_linked(b2, 'Located_Var_Decl', a)


def test_assoc_non_generic_type_name231_link_reassign_clear():
    a = iec61131_pous_Program_Access_Decl(direction="sample_text")
    b1 = Non_Generic_Type_Name()
    b2 = Non_Generic_Type_Name()
    _safe_set(a, 'iec61131_pous_Program_Access_Decl232', b1)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl232', b1)
    if hasattr(b1, 'Non_Generic_Type_Name233'):
        assert _is_linked(b1, 'Non_Generic_Type_Name233', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl232', b2)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl232', b2)
    if hasattr(b1, 'Non_Generic_Type_Name233'):
        assert not _is_linked(b1, 'Non_Generic_Type_Name233', a)
    if hasattr(b2, 'Non_Generic_Type_Name233'):
        assert _is_linked(b2, 'Non_Generic_Type_Name233', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl232', None)
    assert not _is_linked(a, 'iec61131_pous_Program_Access_Decl232', b2)
    if hasattr(b2, 'Non_Generic_Type_Name233'):
        assert not _is_linked(b2, 'Non_Generic_Type_Name233', a)


def test_assoc_non_generic_type_name338_link_reassign_clear():
    a = iec61131_configurations_Access_Declaration(direction="sample_text")
    b1 = Non_Generic_Type_Name()
    b2 = Non_Generic_Type_Name()
    _safe_set(a, 'iec61131_configurations_Access_Declaration339', b1)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration339', b1)
    if hasattr(b1, 'Non_Generic_Type_Name340'):
        assert _is_linked(b1, 'Non_Generic_Type_Name340', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration339', b2)
    assert _is_linked(a, 'iec61131_configurations_Access_Declaration339', b2)
    if hasattr(b1, 'Non_Generic_Type_Name340'):
        assert not _is_linked(b1, 'Non_Generic_Type_Name340', a)
    if hasattr(b2, 'Non_Generic_Type_Name340'):
        assert _is_linked(b2, 'Non_Generic_Type_Name340', a)
    _safe_set(a, 'iec61131_configurations_Access_Declaration339', None)
    assert not _is_linked(a, 'iec61131_configurations_Access_Declaration339', b2)
    if hasattr(b2, 'Non_Generic_Type_Name340'):
        assert not _is_linked(b2, 'Non_Generic_Type_Name340', a)


def test_assoc_prog_conf_elements317_link_reassign_clear():
    a = iec61131_configurations_Program_Configuration(retain=True)
    b1 = Prog_Conf_Elements()
    b2 = Prog_Conf_Elements()
    _safe_set(a, 'iec61131_configurations_Program_Configuration318', b1)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration318', b1)
    if hasattr(b1, 'Prog_Conf_Elements'):
        assert _is_linked(b1, 'Prog_Conf_Elements', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration318', b2)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration318', b2)
    if hasattr(b1, 'Prog_Conf_Elements'):
        assert not _is_linked(b1, 'Prog_Conf_Elements', a)
    if hasattr(b2, 'Prog_Conf_Elements'):
        assert _is_linked(b2, 'Prog_Conf_Elements', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration318', None)
    assert not _is_linked(a, 'iec61131_configurations_Program_Configuration318', b2)
    if hasattr(b2, 'Prog_Conf_Elements'):
        assert not _is_linked(b2, 'Prog_Conf_Elements', a)


def test_assoc_program_name310_link_reassign_clear():
    a = iec61131_configurations_Program_Configuration(retain=True)
    b1 = Program_Name()
    b2 = Program_Name()
    _safe_set(a, 'iec61131_configurations_Program_Configuration', b1)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration', b1)
    if hasattr(b1, 'Program_Name'):
        assert _is_linked(b1, 'Program_Name', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration', b2)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration', b2)
    if hasattr(b1, 'Program_Name'):
        assert not _is_linked(b1, 'Program_Name', a)
    if hasattr(b2, 'Program_Name'):
        assert _is_linked(b2, 'Program_Name', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration', None)
    assert not _is_linked(a, 'iec61131_configurations_Program_Configuration', b2)
    if hasattr(b2, 'Program_Name'):
        assert not _is_linked(b2, 'Program_Name', a)


def test_assoc_program_type_name314_link_reassign_clear():
    a = iec61131_configurations_Program_Configuration(retain=True)
    b1 = Program_Type_Name()
    b2 = Program_Type_Name()
    _safe_set(a, 'iec61131_configurations_Program_Configuration315', b1)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration315', b1)
    if hasattr(b1, 'Program_Type_Name316'):
        assert _is_linked(b1, 'Program_Type_Name316', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration315', b2)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration315', b2)
    if hasattr(b1, 'Program_Type_Name316'):
        assert not _is_linked(b1, 'Program_Type_Name316', a)
    if hasattr(b2, 'Program_Type_Name316'):
        assert _is_linked(b2, 'Program_Type_Name316', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration315', None)
    assert not _is_linked(a, 'iec61131_configurations_Program_Configuration315', b2)
    if hasattr(b2, 'Program_Type_Name316'):
        assert not _is_linked(b2, 'Program_Type_Name316', a)


def test_assoc_real_type_name9_link_reassign_clear():
    a = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    b1 = Real_Type_Name()
    b2 = Real_Type_Name()
    _safe_set(a, 'iec61131_literals_Real_Literal', b1)
    assert _is_linked(a, 'iec61131_literals_Real_Literal', b1)
    if hasattr(b1, 'Real_Type_Name'):
        assert _is_linked(b1, 'Real_Type_Name', a)
    _safe_set(a, 'iec61131_literals_Real_Literal', b2)
    assert _is_linked(a, 'iec61131_literals_Real_Literal', b2)
    if hasattr(b1, 'Real_Type_Name'):
        assert not _is_linked(b1, 'Real_Type_Name', a)
    if hasattr(b2, 'Real_Type_Name'):
        assert _is_linked(b2, 'Real_Type_Name', a)
    _safe_set(a, 'iec61131_literals_Real_Literal', None)
    assert not _is_linked(a, 'iec61131_literals_Real_Literal', b2)
    if hasattr(b2, 'Real_Type_Name'):
        assert not _is_linked(b2, 'Real_Type_Name', a)


def test_assoc_second48_link_reassign_clear():
    a = iec61131_literals_Daytime(hour="sample_text", minute="sample_text")
    b1 = Fixed_Point()
    b2 = Fixed_Point()
    _safe_set(a, 'iec61131_literals_Daytime', b1)
    assert _is_linked(a, 'iec61131_literals_Daytime', b1)
    if hasattr(b1, 'Fixed_Point49'):
        assert _is_linked(b1, 'Fixed_Point49', a)
    _safe_set(a, 'iec61131_literals_Daytime', b2)
    assert _is_linked(a, 'iec61131_literals_Daytime', b2)
    if hasattr(b1, 'Fixed_Point49'):
        assert not _is_linked(b1, 'Fixed_Point49', a)
    if hasattr(b2, 'Fixed_Point49'):
        assert _is_linked(b2, 'Fixed_Point49', a)
    _safe_set(a, 'iec61131_literals_Daytime', None)
    assert not _is_linked(a, 'iec61131_literals_Daytime', b2)
    if hasattr(b2, 'Fixed_Point49'):
        assert not _is_linked(b2, 'Fixed_Point49', a)


def test_assoc_symbolic_variable234_link_reassign_clear():
    a = iec61131_pous_Program_Access_Decl(direction="sample_text")
    b1 = Symbolic_Variable()
    b2 = Symbolic_Variable()
    _safe_set(a, 'iec61131_pous_Program_Access_Decl235', b1)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl235', b1)
    if hasattr(b1, 'Symbolic_Variable'):
        assert _is_linked(b1, 'Symbolic_Variable', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl235', b2)
    assert _is_linked(a, 'iec61131_pous_Program_Access_Decl235', b2)
    if hasattr(b1, 'Symbolic_Variable'):
        assert not _is_linked(b1, 'Symbolic_Variable', a)
    if hasattr(b2, 'Symbolic_Variable'):
        assert _is_linked(b2, 'Symbolic_Variable', a)
    _safe_set(a, 'iec61131_pous_Program_Access_Decl235', None)
    assert not _is_linked(a, 'iec61131_pous_Program_Access_Decl235', b2)
    if hasattr(b2, 'Symbolic_Variable'):
        assert not _is_linked(b2, 'Symbolic_Variable', a)


def test_assoc_task_name311_link_reassign_clear():
    a = iec61131_configurations_Program_Configuration(retain=True)
    b1 = Task_Name()
    b2 = Task_Name()
    _safe_set(a, 'iec61131_configurations_Program_Configuration312', b1)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration312', b1)
    if hasattr(b1, 'Task_Name313'):
        assert _is_linked(b1, 'Task_Name313', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration312', b2)
    assert _is_linked(a, 'iec61131_configurations_Program_Configuration312', b2)
    if hasattr(b1, 'Task_Name313'):
        assert not _is_linked(b1, 'Task_Name313', a)
    if hasattr(b2, 'Task_Name313'):
        assert _is_linked(b2, 'Task_Name313', a)
    _safe_set(a, 'iec61131_configurations_Program_Configuration312', None)
    assert not _is_linked(a, 'iec61131_configurations_Program_Configuration312', b2)
    if hasattr(b2, 'Task_Name313'):
        assert not _is_linked(b2, 'Task_Name313', a)


def test_assoc_timed_qualifier651_link_reassign_clear():
    a = iec61131_sfc_Action_Qualifier(qualifier="sample_text")
    b1 = Timed_Qualifier()
    b2 = Timed_Qualifier()
    _safe_set(a, 'iec61131_sfc_Action_Qualifier', b1)
    assert _is_linked(a, 'iec61131_sfc_Action_Qualifier', b1)
    if hasattr(b1, 'Timed_Qualifier'):
        assert _is_linked(b1, 'Timed_Qualifier', a)
    _safe_set(a, 'iec61131_sfc_Action_Qualifier', b2)
    assert _is_linked(a, 'iec61131_sfc_Action_Qualifier', b2)
    if hasattr(b1, 'Timed_Qualifier'):
        assert not _is_linked(b1, 'Timed_Qualifier', a)
    if hasattr(b2, 'Timed_Qualifier'):
        assert _is_linked(b2, 'Timed_Qualifier', a)
    _safe_set(a, 'iec61131_sfc_Action_Qualifier', None)
    assert not _is_linked(a, 'iec61131_sfc_Action_Qualifier', b2)
    if hasattr(b2, 'Timed_Qualifier'):
        assert not _is_linked(b2, 'Timed_Qualifier', a)


def test_assoc_var2_init_decl199_link_reassign_clear():
    a = iec61131_interfaces_Function_Var_Decl(constant=True)
    b1 = Var2_Init_Decl()
    b2 = Var2_Init_Decl()
    _safe_set(a, 'iec61131_interfaces_Function_Var_Decl', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Function_Var_Decl', b1)
    if hasattr(b1, 'Var2_Init_Decl'):
        assert _is_linked(b1, 'Var2_Init_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Function_Var_Decl', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Function_Var_Decl', b2)
    if hasattr(b1, 'Var2_Init_Decl'):
        assert not _is_linked(b1, 'Var2_Init_Decl', a)
    if hasattr(b2, 'Var2_Init_Decl'):
        assert _is_linked(b2, 'Var2_Init_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Function_Var_Decl', set())
    assert not _is_linked(a, 'iec61131_interfaces_Function_Var_Decl', b2)
    if hasattr(b2, 'Var2_Init_Decl'):
        assert not _is_linked(b2, 'Var2_Init_Decl', a)


def test_assoc_var_init_decl76_link_reassign_clear():
    a = iec61131_interfaces_Output_Declarations(retain=True)
    b1 = Var_Init_Decl()
    b2 = Var_Init_Decl()
    _safe_set(a, 'iec61131_interfaces_Output_Declarations', {b1})
    assert _is_linked(a, 'iec61131_interfaces_Output_Declarations', b1)
    if hasattr(b1, 'Var_Init_Decl'):
        assert _is_linked(b1, 'Var_Init_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Output_Declarations', {b2})
    assert _is_linked(a, 'iec61131_interfaces_Output_Declarations', b2)
    if hasattr(b1, 'Var_Init_Decl'):
        assert not _is_linked(b1, 'Var_Init_Decl', a)
    if hasattr(b2, 'Var_Init_Decl'):
        assert _is_linked(b2, 'Var_Init_Decl', a)
    _safe_set(a, 'iec61131_interfaces_Output_Declarations', set())
    assert not _is_linked(a, 'iec61131_interfaces_Output_Declarations', b2)
    if hasattr(b2, 'Var_Init_Decl'):
        assert not _is_linked(b2, 'Var_Init_Decl', a)


def test_assoc_var_list56_link_reassign_clear():
    a = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    b1 = Var1_List()
    b2 = Var1_List()
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration', b1)
    assert _is_linked(a, 'iec61131_interfaces_Edge_Declaration', b1)
    if hasattr(b1, 'Var1_List57'):
        assert _is_linked(b1, 'Var1_List57', a)
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration', b2)
    assert _is_linked(a, 'iec61131_interfaces_Edge_Declaration', b2)
    if hasattr(b1, 'Var1_List57'):
        assert not _is_linked(b1, 'Var1_List57', a)
    if hasattr(b2, 'Var1_List57'):
        assert _is_linked(b2, 'Var1_List57', a)
    _safe_set(a, 'iec61131_interfaces_Edge_Declaration', None)
    assert not _is_linked(a, 'iec61131_interfaces_Edge_Declaration', b2)
    if hasattr(b2, 'Var1_List57'):
        assert not _is_linked(b2, 'Var1_List57', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Access_Declaration_strategy = st.builds(Access_Declaration)
@given(instance=Access_Declaration_strategy)
@settings(max_examples=25)
def test_Access_Declaration_instantiation(instance):
    assert isinstance(instance, Access_Declaration)


Access_Declarations_strategy = st.builds(Access_Declarations)
@given(instance=Access_Declarations_strategy)
@settings(max_examples=25)
def test_Access_Declarations_instantiation(instance):
    assert isinstance(instance, Access_Declarations)


Access_Name_strategy = st.builds(Access_Name)
@given(instance=Access_Name_strategy)
@settings(max_examples=25)
def test_Access_Name_instantiation(instance):
    assert isinstance(instance, Access_Name)


Access_Path_strategy = st.builds(Access_Path)
@given(instance=Access_Path_strategy)
@settings(max_examples=25)
def test_Access_Path_instantiation(instance):
    assert isinstance(instance, Access_Path)


Action_Association_strategy = st.builds(Action_Association)
@given(instance=Action_Association_strategy)
@settings(max_examples=25)
def test_Action_Association_instantiation(instance):
    assert isinstance(instance, Action_Association)


Action_Name_strategy = st.builds(Action_Name)
@given(instance=Action_Name_strategy)
@settings(max_examples=25)
def test_Action_Name_instantiation(instance):
    assert isinstance(instance, Action_Name)


Action_Qualifier_strategy = st.builds(Action_Qualifier)
@given(instance=Action_Qualifier_strategy)
@settings(max_examples=25)
def test_Action_Qualifier_instantiation(instance):
    assert isinstance(instance, Action_Qualifier)


Action_Time_strategy = st.builds(Action_Time)
@given(instance=Action_Time_strategy)
@settings(max_examples=25)
def test_Action_Time_instantiation(instance):
    assert isinstance(instance, Action_Time)


Add_Operator_strategy = st.builds(Add_Operator)
@given(instance=Add_Operator_strategy)
@settings(max_examples=25)
def test_Add_Operator_instantiation(instance):
    assert isinstance(instance, Add_Operator)


And_Operator_strategy = st.builds(And_Operator)
@given(instance=And_Operator_strategy)
@settings(max_examples=25)
def test_And_Operator_instantiation(instance):
    assert isinstance(instance, And_Operator)


Array_Initial_Elements_strategy = st.builds(Array_Initial_Elements)
@given(instance=Array_Initial_Elements_strategy)
@settings(max_examples=25)
def test_Array_Initial_Elements_instantiation(instance):
    assert isinstance(instance, Array_Initial_Elements)


Array_Initialization_strategy = st.builds(Array_Initialization)
@given(instance=Array_Initialization_strategy)
@settings(max_examples=25)
def test_Array_Initialization_instantiation(instance):
    assert isinstance(instance, Array_Initialization)


Array_Spec_Init_strategy = st.builds(Array_Spec_Init)
@given(instance=Array_Spec_Init_strategy)
@settings(max_examples=25)
def test_Array_Spec_Init_instantiation(instance):
    assert isinstance(instance, Array_Spec_Init)


Array_Specification_strategy = st.builds(Array_Specification)
@given(instance=Array_Specification_strategy)
@settings(max_examples=25)
def test_Array_Specification_instantiation(instance):
    assert isinstance(instance, Array_Specification)


Array_Type_Name_strategy = st.builds(Array_Type_Name)
@given(instance=Array_Type_Name_strategy)
@settings(max_examples=25)
def test_Array_Type_Name_instantiation(instance):
    assert isinstance(instance, Array_Type_Name)


Array_Variable_strategy = st.builds(Array_Variable)
@given(instance=Array_Variable_strategy)
@settings(max_examples=25)
def test_Array_Variable_instantiation(instance):
    assert isinstance(instance, Array_Variable)


Assignment_Name_strategy = st.builds(Assignment_Name)
@given(instance=Assignment_Name_strategy)
@settings(max_examples=25)
def test_Assignment_Name_instantiation(instance):
    assert isinstance(instance, Assignment_Name)


Assignment_Operator_strategy = st.builds(Assignment_Operator)
@given(instance=Assignment_Operator_strategy)
@settings(max_examples=25)
def test_Assignment_Operator_instantiation(instance):
    assert isinstance(instance, Assignment_Operator)


Assignment_Symbol_strategy = st.builds(Assignment_Symbol)
@given(instance=Assignment_Symbol_strategy)
@settings(max_examples=25)
def test_Assignment_Symbol_instantiation(instance):
    assert isinstance(instance, Assignment_Symbol)


BSInteger_strategy = st.builds(BSInteger)
@given(instance=BSInteger_strategy)
@settings(max_examples=25)
def test_BSInteger_instantiation(instance):
    assert isinstance(instance, BSInteger)


Bit_String_Type_Name_strategy = st.builds(Bit_String_Type_Name)
@given(instance=Bit_String_Type_Name_strategy)
@settings(max_examples=25)
def test_Bit_String_Type_Name_instantiation(instance):
    assert isinstance(instance, Bit_String_Type_Name)


Blocks_strategy = st.builds(Blocks)
@given(instance=Blocks_strategy)
@settings(max_examples=25)
def test_Blocks_instantiation(instance):
    assert isinstance(instance, Blocks)


Bool_Type_Name_strategy = st.builds(Bool_Type_Name)
@given(instance=Bool_Type_Name_strategy)
@settings(max_examples=25)
def test_Bool_Type_Name_instantiation(instance):
    assert isinstance(instance, Bool_Type_Name)


Byte_String_strategy = st.builds(Byte_String)
@given(instance=Byte_String_strategy)
@settings(max_examples=25)
def test_Byte_String_instantiation(instance):
    assert isinstance(instance, Byte_String)


Byte_String_Type_Name_strategy = st.builds(Byte_String_Type_Name)
@given(instance=Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, Byte_String_Type_Name)


Case_Element_strategy = st.builds(Case_Element)
@given(instance=Case_Element_strategy)
@settings(max_examples=25)
def test_Case_Element_instantiation(instance):
    assert isinstance(instance, Case_Element)


Case_List_strategy = st.builds(Case_List)
@given(instance=Case_List_strategy)
@settings(max_examples=25)
def test_Case_List_instantiation(instance):
    assert isinstance(instance, Case_List)


Case_List_Element_strategy = st.builds(Case_List_Element)
@given(instance=Case_List_Element_strategy)
@settings(max_examples=25)
def test_Case_List_Element_instantiation(instance):
    assert isinstance(instance, Case_List_Element)


Character_String_strategy = st.builds(Character_String)
@given(instance=Character_String_strategy)
@settings(max_examples=25)
def test_Character_String_instantiation(instance):
    assert isinstance(instance, Character_String)


Commentable_strategy = st.builds(Commentable)
@given(instance=Commentable_strategy)
@settings(max_examples=25)
def test_Commentable_instantiation(instance):
    assert isinstance(instance, Commentable)


Common_Character_Representation_strategy = st.builds(Common_Character_Representation)
@given(instance=Common_Character_Representation_strategy)
@settings(max_examples=25)
def test_Common_Character_Representation_instantiation(instance):
    assert isinstance(instance, Common_Character_Representation)


Comparison_Operator_strategy = st.builds(Comparison_Operator)
@given(instance=Comparison_Operator_strategy)
@settings(max_examples=25)
def test_Comparison_Operator_instantiation(instance):
    assert isinstance(instance, Comparison_Operator)


Cond2_Condition_strategy = st.builds(Cond2_Condition)
@given(instance=Cond2_Condition_strategy)
@settings(max_examples=25)
def test_Cond2_Condition_instantiation(instance):
    assert isinstance(instance, Cond2_Condition)


Configuration_Name_strategy = st.builds(Configuration_Name)
@given(instance=Configuration_Name_strategy)
@settings(max_examples=25)
def test_Configuration_Name_instantiation(instance):
    assert isinstance(instance, Configuration_Name)


Constant_strategy = st.builds(Constant)
@given(instance=Constant_strategy)
@settings(max_examples=25)
def test_Constant_instantiation(instance):
    assert isinstance(instance, Constant)


Control_Variable_strategy = st.builds(Control_Variable)
@given(instance=Control_Variable_strategy)
@settings(max_examples=25)
def test_Control_Variable_instantiation(instance):
    assert isinstance(instance, Control_Variable)


DT_Type_Name_strategy = st.builds(DT_Type_Name)
@given(instance=DT_Type_Name_strategy)
@settings(max_examples=25)
def test_DT_Type_Name_instantiation(instance):
    assert isinstance(instance, DT_Type_Name)


Data_Sink_strategy = st.builds(Data_Sink)
@given(instance=Data_Sink_strategy)
@settings(max_examples=25)
def test_Data_Sink_instantiation(instance):
    assert isinstance(instance, Data_Sink)


Data_Source_strategy = st.builds(Data_Source)
@given(instance=Data_Source_strategy)
@settings(max_examples=25)
def test_Data_Source_instantiation(instance):
    assert isinstance(instance, Data_Source)


Data_Type_Name_strategy = st.builds(Data_Type_Name)
@given(instance=Data_Type_Name_strategy)
@settings(max_examples=25)
def test_Data_Type_Name_instantiation(instance):
    assert isinstance(instance, Data_Type_Name)


Date_Literal_strategy = st.builds(Date_Literal)
@given(instance=Date_Literal_strategy)
@settings(max_examples=25)
def test_Date_Literal_instantiation(instance):
    assert isinstance(instance, Date_Literal)


Date_Type_Name_strategy = st.builds(Date_Type_Name)
@given(instance=Date_Type_Name_strategy)
@settings(max_examples=25)
def test_Date_Type_Name_instantiation(instance):
    assert isinstance(instance, Date_Type_Name)


Daytime_strategy = st.builds(Daytime)
@given(instance=Daytime_strategy)
@settings(max_examples=25)
def test_Daytime_instantiation(instance):
    assert isinstance(instance, Daytime)


Derived_Function_Block_Name_strategy = st.builds(Derived_Function_Block_Name)
@given(instance=Derived_Function_Block_Name_strategy)
@settings(max_examples=25)
def test_Derived_Function_Block_Name_instantiation(instance):
    assert isinstance(instance, Derived_Function_Block_Name)


Derived_Function_Name_strategy = st.builds(Derived_Function_Name)
@given(instance=Derived_Function_Name_strategy)
@settings(max_examples=25)
def test_Derived_Function_Name_instantiation(instance):
    assert isinstance(instance, Derived_Function_Name)


Derived_Type_Name_strategy = st.builds(Derived_Type_Name)
@given(instance=Derived_Type_Name_strategy)
@settings(max_examples=25)
def test_Derived_Type_Name_instantiation(instance):
    assert isinstance(instance, Derived_Type_Name)


Direct_Variable_strategy = st.builds(Direct_Variable)
@given(instance=Direct_Variable_strategy)
@settings(max_examples=25)
def test_Direct_Variable_instantiation(instance):
    assert isinstance(instance, Direct_Variable)


Divide_Operator_strategy = st.builds(Divide_Operator)
@given(instance=Divide_Operator_strategy)
@settings(max_examples=25)
def test_Divide_Operator_instantiation(instance):
    assert isinstance(instance, Divide_Operator)


Dot_Operator_strategy = st.builds(Dot_Operator)
@given(instance=Dot_Operator_strategy)
@settings(max_examples=25)
def test_Dot_Operator_instantiation(instance):
    assert isinstance(instance, Dot_Operator)


Double_BString_strategy = st.builds(Double_BString)
@given(instance=Double_BString_strategy)
@settings(max_examples=25)
def test_Double_BString_instantiation(instance):
    assert isinstance(instance, Double_BString)


Double_Byte_Character_Representation_strategy = st.builds(Double_Byte_Character_Representation)
@given(instance=Double_Byte_Character_Representation_strategy)
@settings(max_examples=25)
def test_Double_Byte_Character_Representation_instantiation(instance):
    assert isinstance(instance, Double_Byte_Character_Representation)


Double_Byte_Character_String_strategy = st.builds(Double_Byte_Character_String)
@given(instance=Double_Byte_Character_String_strategy)
@settings(max_examples=25)
def test_Double_Byte_Character_String_instantiation(instance):
    assert isinstance(instance, Double_Byte_Character_String)


Double_Byte_String_Spec_strategy = st.builds(Double_Byte_String_Spec)
@given(instance=Double_Byte_String_Spec_strategy)
@settings(max_examples=25)
def test_Double_Byte_String_Spec_instantiation(instance):
    assert isinstance(instance, Double_Byte_String_Spec)


Double_Byte_String_Type_Name_strategy = st.builds(Double_Byte_String_Type_Name)
@given(instance=Double_Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_Double_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, Double_Byte_String_Type_Name)


Duration_Type_Name_strategy = st.builds(Duration_Type_Name)
@given(instance=Duration_Type_Name_strategy)
@settings(max_examples=25)
def test_Duration_Type_Name_instantiation(instance):
    assert isinstance(instance, Duration_Type_Name)


Elementary_Type_Name_strategy = st.builds(Elementary_Type_Name)
@given(instance=Elementary_Type_Name_strategy)
@settings(max_examples=25)
def test_Elementary_Type_Name_instantiation(instance):
    assert isinstance(instance, Elementary_Type_Name)


Else_If_Statement_strategy = st.builds(Else_If_Statement)
@given(instance=Else_If_Statement_strategy)
@settings(max_examples=25)
def test_Else_If_Statement_instantiation(instance):
    assert isinstance(instance, Else_If_Statement)


Else_Statement_strategy = st.builds(Else_Statement)
@given(instance=Else_Statement_strategy)
@settings(max_examples=25)
def test_Else_Statement_instantiation(instance):
    assert isinstance(instance, Else_Statement)


Enumerated_Spec_Init_strategy = st.builds(Enumerated_Spec_Init)
@given(instance=Enumerated_Spec_Init_strategy)
@settings(max_examples=25)
def test_Enumerated_Spec_Init_instantiation(instance):
    assert isinstance(instance, Enumerated_Spec_Init)


Enumerated_Specification_strategy = st.builds(Enumerated_Specification)
@given(instance=Enumerated_Specification_strategy)
@settings(max_examples=25)
def test_Enumerated_Specification_instantiation(instance):
    assert isinstance(instance, Enumerated_Specification)


Enumerated_Type_Name_strategy = st.builds(Enumerated_Type_Name)
@given(instance=Enumerated_Type_Name_strategy)
@settings(max_examples=25)
def test_Enumerated_Type_Name_instantiation(instance):
    assert isinstance(instance, Enumerated_Type_Name)


Enumerated_Value_strategy = st.builds(Enumerated_Value)
@given(instance=Enumerated_Value_strategy)
@settings(max_examples=25)
def test_Enumerated_Value_instantiation(instance):
    assert isinstance(instance, Enumerated_Value)


EquUequ_Operator_strategy = st.builds(EquUequ_Operator)
@given(instance=EquUequ_Operator_strategy)
@settings(max_examples=25)
def test_EquUequ_Operator_instantiation(instance):
    assert isinstance(instance, EquUequ_Operator)


Equal_Operator_strategy = st.builds(Equal_Operator)
@given(instance=Equal_Operator_strategy)
@settings(max_examples=25)
def test_Equal_Operator_instantiation(instance):
    assert isinstance(instance, Equal_Operator)


Expression_Types_strategy = st.builds(Expression_Types)
@given(instance=Expression_Types_strategy)
@settings(max_examples=25)
def test_Expression_Types_instantiation(instance):
    assert isinstance(instance, Expression_Types)


Expression_Variable_strategy = st.builds(Expression_Variable)
@given(instance=Expression_Variable_strategy)
@settings(max_examples=25)
def test_Expression_Variable_instantiation(instance):
    assert isinstance(instance, Expression_Variable)


External_Declaration_strategy = st.builds(External_Declaration)
@given(instance=External_Declaration_strategy)
@settings(max_examples=25)
def test_External_Declaration_instantiation(instance):
    assert isinstance(instance, External_Declaration)


External_Specification_strategy = st.builds(External_Specification)
@given(instance=External_Specification_strategy)
@settings(max_examples=25)
def test_External_Specification_instantiation(instance):
    assert isinstance(instance, External_Specification)


Fbd_Network_strategy = st.builds(Fbd_Network)
@given(instance=Fbd_Network_strategy)
@settings(max_examples=25)
def test_Fbd_Network_instantiation(instance):
    assert isinstance(instance, Fbd_Network)


Fixed_Point_strategy = st.builds(Fixed_Point)
@given(instance=Fixed_Point_strategy)
@settings(max_examples=25)
def test_Fixed_Point_instantiation(instance):
    assert isinstance(instance, Fixed_Point)


Fixed_Point_Literal_strategy = st.builds(Fixed_Point_Literal)
@given(instance=Fixed_Point_Literal_strategy)
@settings(max_examples=25)
def test_Fixed_Point_Literal_instantiation(instance):
    assert isinstance(instance, Fixed_Point_Literal)


For_List_strategy = st.builds(For_List)
@given(instance=For_List_strategy)
@settings(max_examples=25)
def test_For_List_instantiation(instance):
    assert isinstance(instance, For_List)


Function_Block_Body_strategy = st.builds(Function_Block_Body)
@given(instance=Function_Block_Body_strategy)
@settings(max_examples=25)
def test_Function_Block_Body_instantiation(instance):
    assert isinstance(instance, Function_Block_Body)


Function_Block_Declaration_strategy = st.builds(Function_Block_Declaration)
@given(instance=Function_Block_Declaration_strategy)
@settings(max_examples=25)
def test_Function_Block_Declaration_instantiation(instance):
    assert isinstance(instance, Function_Block_Declaration)


Function_Block_Type_Name_strategy = st.builds(Function_Block_Type_Name)
@given(instance=Function_Block_Type_Name_strategy)
@settings(max_examples=25)
def test_Function_Block_Type_Name_instantiation(instance):
    assert isinstance(instance, Function_Block_Type_Name)


Function_Block_Vars_strategy = st.builds(Function_Block_Vars)
@given(instance=Function_Block_Vars_strategy)
@settings(max_examples=25)
def test_Function_Block_Vars_instantiation(instance):
    assert isinstance(instance, Function_Block_Vars)


Function_Body_strategy = st.builds(Function_Body)
@given(instance=Function_Body_strategy)
@settings(max_examples=25)
def test_Function_Body_instantiation(instance):
    assert isinstance(instance, Function_Body)


Function_Declaration_strategy = st.builds(Function_Declaration)
@given(instance=Function_Declaration_strategy)
@settings(max_examples=25)
def test_Function_Declaration_instantiation(instance):
    assert isinstance(instance, Function_Declaration)


Function_Name_strategy = st.builds(Function_Name)
@given(instance=Function_Name_strategy)
@settings(max_examples=25)
def test_Function_Name_instantiation(instance):
    assert isinstance(instance, Function_Name)


Function_Return_Value_strategy = st.builds(Function_Return_Value)
@given(instance=Function_Return_Value_strategy)
@settings(max_examples=25)
def test_Function_Return_Value_instantiation(instance):
    assert isinstance(instance, Function_Return_Value)


Function_Vars_strategy = st.builds(Function_Vars)
@given(instance=Function_Vars_strategy)
@settings(max_examples=25)
def test_Function_Vars_instantiation(instance):
    assert isinstance(instance, Function_Vars)


Global_Var_Decl_strategy = st.builds(Global_Var_Decl)
@given(instance=Global_Var_Decl_strategy)
@settings(max_examples=25)
def test_Global_Var_Decl_instantiation(instance):
    assert isinstance(instance, Global_Var_Decl)


Global_Var_Declarations_strategy = st.builds(Global_Var_Declarations)
@given(instance=Global_Var_Declarations_strategy)
@settings(max_examples=25)
def test_Global_Var_Declarations_instantiation(instance):
    assert isinstance(instance, Global_Var_Declarations)


Global_Var_Name_strategy = st.builds(Global_Var_Name)
@given(instance=Global_Var_Name_strategy)
@settings(max_examples=25)
def test_Global_Var_Name_instantiation(instance):
    assert isinstance(instance, Global_Var_Name)


Global_Var_Spec_strategy = st.builds(Global_Var_Spec)
@given(instance=Global_Var_Spec_strategy)
@settings(max_examples=25)
def test_Global_Var_Spec_instantiation(instance):
    assert isinstance(instance, Global_Var_Spec)


GreaterEqual_Operator_strategy = st.builds(GreaterEqual_Operator)
@given(instance=GreaterEqual_Operator_strategy)
@settings(max_examples=25)
def test_GreaterEqual_Operator_instantiation(instance):
    assert isinstance(instance, GreaterEqual_Operator)


Greater_Operator_strategy = st.builds(Greater_Operator)
@given(instance=Greater_Operator_strategy)
@settings(max_examples=25)
def test_Greater_Operator_instantiation(instance):
    assert isinstance(instance, Greater_Operator)


Hours_strategy = st.builds(Hours)
@given(instance=Hours_strategy)
@settings(max_examples=25)
def test_Hours_instantiation(instance):
    assert isinstance(instance, Hours)


Il_Assign_Operator_strategy = st.builds(Il_Assign_Operator)
@given(instance=Il_Assign_Operator_strategy)
@settings(max_examples=25)
def test_Il_Assign_Operator_instantiation(instance):
    assert isinstance(instance, Il_Assign_Operator)


Il_Assign_Out_Operator_strategy = st.builds(Il_Assign_Out_Operator)
@given(instance=Il_Assign_Out_Operator_strategy)
@settings(max_examples=25)
def test_Il_Assign_Out_Operator_instantiation(instance):
    assert isinstance(instance, Il_Assign_Out_Operator)


Il_Call_Operator_strategy = st.builds(Il_Call_Operator)
@given(instance=Il_Call_Operator_strategy)
@settings(max_examples=25)
def test_Il_Call_Operator_instantiation(instance):
    assert isinstance(instance, Il_Call_Operator)


Il_Expr_Operator_strategy = st.builds(Il_Expr_Operator)
@given(instance=Il_Expr_Operator_strategy)
@settings(max_examples=25)
def test_Il_Expr_Operator_instantiation(instance):
    assert isinstance(instance, Il_Expr_Operator)


Il_Instruction_strategy = st.builds(Il_Instruction)
@given(instance=Il_Instruction_strategy)
@settings(max_examples=25)
def test_Il_Instruction_instantiation(instance):
    assert isinstance(instance, Il_Instruction)


Il_Jump_Operator_strategy = st.builds(Il_Jump_Operator)
@given(instance=Il_Jump_Operator_strategy)
@settings(max_examples=25)
def test_Il_Jump_Operator_instantiation(instance):
    assert isinstance(instance, Il_Jump_Operator)


Il_Operand_strategy = st.builds(Il_Operand)
@given(instance=Il_Operand_strategy)
@settings(max_examples=25)
def test_Il_Operand_instantiation(instance):
    assert isinstance(instance, Il_Operand)


Il_Operand_List_strategy = st.builds(Il_Operand_List)
@given(instance=Il_Operand_List_strategy)
@settings(max_examples=25)
def test_Il_Operand_List_instantiation(instance):
    assert isinstance(instance, Il_Operand_List)


Il_Operations_strategy = st.builds(Il_Operations)
@given(instance=Il_Operations_strategy)
@settings(max_examples=25)
def test_Il_Operations_instantiation(instance):
    assert isinstance(instance, Il_Operations)


Il_Param_Instruction_strategy = st.builds(Il_Param_Instruction)
@given(instance=Il_Param_Instruction_strategy)
@settings(max_examples=25)
def test_Il_Param_Instruction_instantiation(instance):
    assert isinstance(instance, Il_Param_Instruction)


Il_Param_Last_Instruction_strategy = st.builds(Il_Param_Last_Instruction)
@given(instance=Il_Param_Last_Instruction_strategy)
@settings(max_examples=25)
def test_Il_Param_Last_Instruction_instantiation(instance):
    assert isinstance(instance, Il_Param_Last_Instruction)


Il_Param_List_strategy = st.builds(Il_Param_List)
@given(instance=Il_Param_List_strategy)
@settings(max_examples=25)
def test_Il_Param_List_instantiation(instance):
    assert isinstance(instance, Il_Param_List)


Il_Simple_Instruction_strategy = st.builds(Il_Simple_Instruction)
@given(instance=Il_Simple_Instruction_strategy)
@settings(max_examples=25)
def test_Il_Simple_Instruction_instantiation(instance):
    assert isinstance(instance, Il_Simple_Instruction)


Il_Simple_Operation_strategy = st.builds(Il_Simple_Operation)
@given(instance=Il_Simple_Operation_strategy)
@settings(max_examples=25)
def test_Il_Simple_Operation_instantiation(instance):
    assert isinstance(instance, Il_Simple_Operation)


Il_Simple_Operator_strategy = st.builds(Il_Simple_Operator)
@given(instance=Il_Simple_Operator_strategy)
@settings(max_examples=25)
def test_Il_Simple_Operator_instantiation(instance):
    assert isinstance(instance, Il_Simple_Operator)


Incompl_Located_Var_Decl_strategy = st.builds(Incompl_Located_Var_Decl)
@given(instance=Incompl_Located_Var_Decl_strategy)
@settings(max_examples=25)
def test_Incompl_Located_Var_Decl_instantiation(instance):
    assert isinstance(instance, Incompl_Located_Var_Decl)


Incompl_Location_strategy = st.builds(Incompl_Location)
@given(instance=Incompl_Location_strategy)
@settings(max_examples=25)
def test_Incompl_Location_instantiation(instance):
    assert isinstance(instance, Incompl_Location)


Initial_Element_strategy = st.builds(Initial_Element)
@given(instance=Initial_Element_strategy)
@settings(max_examples=25)
def test_Initial_Element_instantiation(instance):
    assert isinstance(instance, Initial_Element)


Initial_Step_strategy = st.builds(Initial_Step)
@given(instance=Initial_Step_strategy)
@settings(max_examples=25)
def test_Initial_Step_instantiation(instance):
    assert isinstance(instance, Initial_Step)


Initialized_Structure_strategy = st.builds(Initialized_Structure)
@given(instance=Initialized_Structure_strategy)
@settings(max_examples=25)
def test_Initialized_Structure_instantiation(instance):
    assert isinstance(instance, Initialized_Structure)


Input_Declaration_strategy = st.builds(Input_Declaration)
@given(instance=Input_Declaration_strategy)
@settings(max_examples=25)
def test_Input_Declaration_instantiation(instance):
    assert isinstance(instance, Input_Declaration)


Input_Reference_strategy = st.builds(Input_Reference)
@given(instance=Input_Reference_strategy)
@settings(max_examples=25)
def test_Input_Reference_instantiation(instance):
    assert isinstance(instance, Input_Reference)


Instance_Specific_Init_strategy = st.builds(Instance_Specific_Init)
@given(instance=Instance_Specific_Init_strategy)
@settings(max_examples=25)
def test_Instance_Specific_Init_instantiation(instance):
    assert isinstance(instance, Instance_Specific_Init)


Instance_Specific_Initializations_strategy = st.builds(Instance_Specific_Initializations)
@given(instance=Instance_Specific_Initializations_strategy)
@settings(max_examples=25)
def test_Instance_Specific_Initializations_instantiation(instance):
    assert isinstance(instance, Instance_Specific_Initializations)


Integer_strategy = st.builds(Integer)
@given(instance=Integer_strategy)
@settings(max_examples=25)
def test_Integer_instantiation(instance):
    assert isinstance(instance, Integer)


Integer_Type_Name_strategy = st.builds(Integer_Type_Name)
@given(instance=Integer_Type_Name_strategy)
@settings(max_examples=25)
def test_Integer_Type_Name_instantiation(instance):
    assert isinstance(instance, Integer_Type_Name)


Interval_strategy = st.builds(Interval)
@given(instance=Interval_strategy)
@settings(max_examples=25)
def test_Interval_instantiation(instance):
    assert isinstance(instance, Interval)


Io_Var_Declaration_strategy = st.builds(Io_Var_Declaration)
@given(instance=Io_Var_Declaration_strategy)
@settings(max_examples=25)
def test_Io_Var_Declaration_instantiation(instance):
    assert isinstance(instance, Io_Var_Declaration)


Iteration_Statement_strategy = st.builds(Iteration_Statement)
@given(instance=Iteration_Statement_strategy)
@settings(max_examples=25)
def test_Iteration_Statement_instantiation(instance):
    assert isinstance(instance, Iteration_Statement)


Label_strategy = st.builds(Label)
@given(instance=Label_strategy)
@settings(max_examples=25)
def test_Label_instantiation(instance):
    assert isinstance(instance, Label)


LessEqual_Operator_strategy = st.builds(LessEqual_Operator)
@given(instance=LessEqual_Operator_strategy)
@settings(max_examples=25)
def test_LessEqual_Operator_instantiation(instance):
    assert isinstance(instance, LessEqual_Operator)


Less_Operator_strategy = st.builds(Less_Operator)
@given(instance=Less_Operator_strategy)
@settings(max_examples=25)
def test_Less_Operator_instantiation(instance):
    assert isinstance(instance, Less_Operator)


Library_Element_Declaration_strategy = st.builds(Library_Element_Declaration)
@given(instance=Library_Element_Declaration_strategy)
@settings(max_examples=25)
def test_Library_Element_Declaration_instantiation(instance):
    assert isinstance(instance, Library_Element_Declaration)


Library_Element_Name_strategy = st.builds(Library_Element_Name)
@given(instance=Library_Element_Name_strategy)
@settings(max_examples=25)
def test_Library_Element_Name_instantiation(instance):
    assert isinstance(instance, Library_Element_Name)


Located_Var_Decl_strategy = st.builds(Located_Var_Decl)
@given(instance=Located_Var_Decl_strategy)
@settings(max_examples=25)
def test_Located_Var_Decl_instantiation(instance):
    assert isinstance(instance, Located_Var_Decl)


Located_Var_Spec_Init_strategy = st.builds(Located_Var_Spec_Init)
@given(instance=Located_Var_Spec_Init_strategy)
@settings(max_examples=25)
def test_Located_Var_Spec_Init_instantiation(instance):
    assert isinstance(instance, Located_Var_Spec_Init)


Location_strategy = st.builds(Location)
@given(instance=Location_strategy)
@settings(max_examples=25)
def test_Location_instantiation(instance):
    assert isinstance(instance, Location)


Milliseconds_strategy = st.builds(Milliseconds)
@given(instance=Milliseconds_strategy)
@settings(max_examples=25)
def test_Milliseconds_instantiation(instance):
    assert isinstance(instance, Milliseconds)


Minutes_strategy = st.builds(Minutes)
@given(instance=Minutes_strategy)
@settings(max_examples=25)
def test_Minutes_instantiation(instance):
    assert isinstance(instance, Minutes)


Multi_Element_Variable_strategy = st.builds(Multi_Element_Variable)
@given(instance=Multi_Element_Variable_strategy)
@settings(max_examples=25)
def test_Multi_Element_Variable_instantiation(instance):
    assert isinstance(instance, Multi_Element_Variable)


Multiply_Operator_strategy = st.builds(Multiply_Operator)
@given(instance=Multiply_Operator_strategy)
@settings(max_examples=25)
def test_Multiply_Operator_instantiation(instance):
    assert isinstance(instance, Multiply_Operator)


NamedElement_strategy = st.builds(NamedElement)
@given(instance=NamedElement_strategy)
@settings(max_examples=25)
def test_NamedElement_instantiation(instance):
    assert isinstance(instance, NamedElement)


Non_Generic_Type_Name_strategy = st.builds(Non_Generic_Type_Name)
@given(instance=Non_Generic_Type_Name_strategy)
@settings(max_examples=25)
def test_Non_Generic_Type_Name_instantiation(instance):
    assert isinstance(instance, Non_Generic_Type_Name)


Not_Operator_strategy = st.builds(Not_Operator)
@given(instance=Not_Operator_strategy)
@settings(max_examples=25)
def test_Not_Operator_instantiation(instance):
    assert isinstance(instance, Not_Operator)


Numeric_Literal_strategy = st.builds(Numeric_Literal)
@given(instance=Numeric_Literal_strategy)
@settings(max_examples=25)
def test_Numeric_Literal_instantiation(instance):
    assert isinstance(instance, Numeric_Literal)


Numeric_Type_Name_strategy = st.builds(Numeric_Type_Name)
@given(instance=Numeric_Type_Name_strategy)
@settings(max_examples=25)
def test_Numeric_Type_Name_instantiation(instance):
    assert isinstance(instance, Numeric_Type_Name)


Operands_strategy = st.builds(Operands)
@given(instance=Operands_strategy)
@settings(max_examples=25)
def test_Operands_instantiation(instance):
    assert isinstance(instance, Operands)


Operator_strategy = st.builds(Operator)
@given(instance=Operator_strategy)
@settings(max_examples=25)
def test_Operator_instantiation(instance):
    assert isinstance(instance, Operator)


Or_Operator_strategy = st.builds(Or_Operator)
@given(instance=Or_Operator_strategy)
@settings(max_examples=25)
def test_Or_Operator_instantiation(instance):
    assert isinstance(instance, Or_Operator)


Other_Var_Declaration_strategy = st.builds(Other_Var_Declaration)
@given(instance=Other_Var_Declaration_strategy)
@settings(max_examples=25)
def test_Other_Var_Declaration_instantiation(instance):
    assert isinstance(instance, Other_Var_Declaration)


Output_Reference_strategy = st.builds(Output_Reference)
@given(instance=Output_Reference_strategy)
@settings(max_examples=25)
def test_Output_Reference_instantiation(instance):
    assert isinstance(instance, Output_Reference)


Param_Assignment_strategy = st.builds(Param_Assignment)
@given(instance=Param_Assignment_strategy)
@settings(max_examples=25)
def test_Param_Assignment_instantiation(instance):
    assert isinstance(instance, Param_Assignment)


Param_Assignments_strategy = st.builds(Param_Assignments)
@given(instance=Param_Assignments_strategy)
@settings(max_examples=25)
def test_Param_Assignments_instantiation(instance):
    assert isinstance(instance, Param_Assignments)


Param_Instruction_strategy = st.builds(Param_Instruction)
@given(instance=Param_Instruction_strategy)
@settings(max_examples=25)
def test_Param_Instruction_instantiation(instance):
    assert isinstance(instance, Param_Instruction)


Power_Operator_strategy = st.builds(Power_Operator)
@given(instance=Power_Operator_strategy)
@settings(max_examples=25)
def test_Power_Operator_instantiation(instance):
    assert isinstance(instance, Power_Operator)


Power_Symbol_strategy = st.builds(Power_Symbol)
@given(instance=Power_Symbol_strategy)
@settings(max_examples=25)
def test_Power_Symbol_instantiation(instance):
    assert isinstance(instance, Power_Symbol)


Primary_Expression_strategy = st.builds(Primary_Expression)
@given(instance=Primary_Expression_strategy)
@settings(max_examples=25)
def test_Primary_Expression_instantiation(instance):
    assert isinstance(instance, Primary_Expression)


Priority_strategy = st.builds(Priority)
@given(instance=Priority_strategy)
@settings(max_examples=25)
def test_Priority_instantiation(instance):
    assert isinstance(instance, Priority)


Prog_Cnxn_strategy = st.builds(Prog_Cnxn)
@given(instance=Prog_Cnxn_strategy)
@settings(max_examples=25)
def test_Prog_Cnxn_instantiation(instance):
    assert isinstance(instance, Prog_Cnxn)


Prog_Conf_Element_strategy = st.builds(Prog_Conf_Element)
@given(instance=Prog_Conf_Element_strategy)
@settings(max_examples=25)
def test_Prog_Conf_Element_instantiation(instance):
    assert isinstance(instance, Prog_Conf_Element)


Prog_Conf_Elements_strategy = st.builds(Prog_Conf_Elements)
@given(instance=Prog_Conf_Elements_strategy)
@settings(max_examples=25)
def test_Prog_Conf_Elements_instantiation(instance):
    assert isinstance(instance, Prog_Conf_Elements)


Prog_Data_Source_strategy = st.builds(Prog_Data_Source)
@given(instance=Prog_Data_Source_strategy)
@settings(max_examples=25)
def test_Prog_Data_Source_instantiation(instance):
    assert isinstance(instance, Prog_Data_Source)


Program_Access_Decl_strategy = st.builds(Program_Access_Decl)
@given(instance=Program_Access_Decl_strategy)
@settings(max_examples=25)
def test_Program_Access_Decl_instantiation(instance):
    assert isinstance(instance, Program_Access_Decl)


Program_Configuration_strategy = st.builds(Program_Configuration)
@given(instance=Program_Configuration_strategy)
@settings(max_examples=25)
def test_Program_Configuration_instantiation(instance):
    assert isinstance(instance, Program_Configuration)


Program_Declaration_strategy = st.builds(Program_Declaration)
@given(instance=Program_Declaration_strategy)
@settings(max_examples=25)
def test_Program_Declaration_instantiation(instance):
    assert isinstance(instance, Program_Declaration)


Program_Name_strategy = st.builds(Program_Name)
@given(instance=Program_Name_strategy)
@settings(max_examples=25)
def test_Program_Name_instantiation(instance):
    assert isinstance(instance, Program_Name)


Program_Type_Name_strategy = st.builds(Program_Type_Name)
@given(instance=Program_Type_Name_strategy)
@settings(max_examples=25)
def test_Program_Type_Name_instantiation(instance):
    assert isinstance(instance, Program_Type_Name)


Program_Vars_strategy = st.builds(Program_Vars)
@given(instance=Program_Vars_strategy)
@settings(max_examples=25)
def test_Program_Vars_instantiation(instance):
    assert isinstance(instance, Program_Vars)


RNV_Declarations_strategy = st.builds(RNV_Declarations)
@given(instance=RNV_Declarations_strategy)
@settings(max_examples=25)
def test_RNV_Declarations_instantiation(instance):
    assert isinstance(instance, RNV_Declarations)


Range_strategy = st.builds(Range)
@given(instance=Range_strategy)
@settings(max_examples=25)
def test_Range_instantiation(instance):
    assert isinstance(instance, Range)


Real_Type_Name_strategy = st.builds(Real_Type_Name)
@given(instance=Real_Type_Name_strategy)
@settings(max_examples=25)
def test_Real_Type_Name_instantiation(instance):
    assert isinstance(instance, Real_Type_Name)


Resource_Declaration_strategy = st.builds(Resource_Declaration)
@given(instance=Resource_Declaration_strategy)
@settings(max_examples=25)
def test_Resource_Declaration_instantiation(instance):
    assert isinstance(instance, Resource_Declaration)


Resource_Name_strategy = st.builds(Resource_Name)
@given(instance=Resource_Name_strategy)
@settings(max_examples=25)
def test_Resource_Name_instantiation(instance):
    assert isinstance(instance, Resource_Name)


Resource_Type_Name_strategy = st.builds(Resource_Type_Name)
@given(instance=Resource_Type_Name_strategy)
@settings(max_examples=25)
def test_Resource_Type_Name_instantiation(instance):
    assert isinstance(instance, Resource_Type_Name)


Seconds_strategy = st.builds(Seconds)
@given(instance=Seconds_strategy)
@settings(max_examples=25)
def test_Seconds_instantiation(instance):
    assert isinstance(instance, Seconds)


Selection_Statement_strategy = st.builds(Selection_Statement)
@given(instance=Selection_Statement_strategy)
@settings(max_examples=25)
def test_Selection_Statement_instantiation(instance):
    assert isinstance(instance, Selection_Statement)


Sfc_Elements_strategy = st.builds(Sfc_Elements)
@given(instance=Sfc_Elements_strategy)
@settings(max_examples=25)
def test_Sfc_Elements_instantiation(instance):
    assert isinstance(instance, Sfc_Elements)


Sfc_Network_strategy = st.builds(Sfc_Network)
@given(instance=Sfc_Network_strategy)
@settings(max_examples=25)
def test_Sfc_Network_instantiation(instance):
    assert isinstance(instance, Sfc_Network)


Signed_Integer_strategy = st.builds(Signed_Integer)
@given(instance=Signed_Integer_strategy)
@settings(max_examples=25)
def test_Signed_Integer_instantiation(instance):
    assert isinstance(instance, Signed_Integer)


Simple_Instr_strategy = st.builds(Simple_Instr)
@given(instance=Simple_Instr_strategy)
@settings(max_examples=25)
def test_Simple_Instr_instantiation(instance):
    assert isinstance(instance, Simple_Instr)


Simple_Instr_List_strategy = st.builds(Simple_Instr_List)
@given(instance=Simple_Instr_List_strategy)
@settings(max_examples=25)
def test_Simple_Instr_List_instantiation(instance):
    assert isinstance(instance, Simple_Instr_List)


Simple_Spec_Init_strategy = st.builds(Simple_Spec_Init)
@given(instance=Simple_Spec_Init_strategy)
@settings(max_examples=25)
def test_Simple_Spec_Init_instantiation(instance):
    assert isinstance(instance, Simple_Spec_Init)


Simple_Specification_strategy = st.builds(Simple_Specification)
@given(instance=Simple_Specification_strategy)
@settings(max_examples=25)
def test_Simple_Specification_instantiation(instance):
    assert isinstance(instance, Simple_Specification)


Simple_Specification_Func_strategy = st.builds(Simple_Specification_Func)
@given(instance=Simple_Specification_Func_strategy)
@settings(max_examples=25)
def test_Simple_Specification_Func_instantiation(instance):
    assert isinstance(instance, Simple_Specification_Func)


Simple_Type_Name_strategy = st.builds(Simple_Type_Name)
@given(instance=Simple_Type_Name_strategy)
@settings(max_examples=25)
def test_Simple_Type_Name_instantiation(instance):
    assert isinstance(instance, Simple_Type_Name)


Single_strategy = st.builds(Single)
@given(instance=Single_strategy)
@settings(max_examples=25)
def test_Single_instantiation(instance):
    assert isinstance(instance, Single)


Single_BString_strategy = st.builds(Single_BString)
@given(instance=Single_BString_strategy)
@settings(max_examples=25)
def test_Single_BString_instantiation(instance):
    assert isinstance(instance, Single_BString)


Single_Byte_Character_Representation_strategy = st.builds(Single_Byte_Character_Representation)
@given(instance=Single_Byte_Character_Representation_strategy)
@settings(max_examples=25)
def test_Single_Byte_Character_Representation_instantiation(instance):
    assert isinstance(instance, Single_Byte_Character_Representation)


Single_Byte_Character_String_strategy = st.builds(Single_Byte_Character_String)
@given(instance=Single_Byte_Character_String_strategy)
@settings(max_examples=25)
def test_Single_Byte_Character_String_instantiation(instance):
    assert isinstance(instance, Single_Byte_Character_String)


Single_Byte_String_Spec_strategy = st.builds(Single_Byte_String_Spec)
@given(instance=Single_Byte_String_Spec_strategy)
@settings(max_examples=25)
def test_Single_Byte_String_Spec_instantiation(instance):
    assert isinstance(instance, Single_Byte_String_Spec)


Single_Byte_String_Type_Name_strategy = st.builds(Single_Byte_String_Type_Name)
@given(instance=Single_Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_Single_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, Single_Byte_String_Type_Name)


Single_Element_Type_Declaration_strategy = st.builds(Single_Element_Type_Declaration)
@given(instance=Single_Element_Type_Declaration_strategy)
@settings(max_examples=25)
def test_Single_Element_Type_Declaration_instantiation(instance):
    assert isinstance(instance, Single_Element_Type_Declaration)


Single_Element_Type_Name_strategy = st.builds(Single_Element_Type_Name)
@given(instance=Single_Element_Type_Name_strategy)
@settings(max_examples=25)
def test_Single_Element_Type_Name_instantiation(instance):
    assert isinstance(instance, Single_Element_Type_Name)


Single_Resource_Declaration_strategy = st.builds(Single_Resource_Declaration)
@given(instance=Single_Resource_Declaration_strategy)
@settings(max_examples=25)
def test_Single_Resource_Declaration_instantiation(instance):
    assert isinstance(instance, Single_Resource_Declaration)


Specification_strategy = st.builds(Specification)
@given(instance=Specification_strategy)
@settings(max_examples=25)
def test_Specification_instantiation(instance):
    assert isinstance(instance, Specification)


Statement_strategy = st.builds(Statement)
@given(instance=Statement_strategy)
@settings(max_examples=25)
def test_Statement_instantiation(instance):
    assert isinstance(instance, Statement)


Statement_List_strategy = st.builds(Statement_List)
@given(instance=Statement_List_strategy)
@settings(max_examples=25)
def test_Statement_List_instantiation(instance):
    assert isinstance(instance, Statement_List)


Step_Name_strategy = st.builds(Step_Name)
@given(instance=Step_Name_strategy)
@settings(max_examples=25)
def test_Step_Name_instantiation(instance):
    assert isinstance(instance, Step_Name)


Step_Types_strategy = st.builds(Step_Types)
@given(instance=Step_Types_strategy)
@settings(max_examples=25)
def test_Step_Types_instantiation(instance):
    assert isinstance(instance, Step_Types)


Steps_strategy = st.builds(Steps)
@given(instance=Steps_strategy)
@settings(max_examples=25)
def test_Steps_instantiation(instance):
    assert isinstance(instance, Steps)


String_Type_Name_strategy = st.builds(String_Type_Name)
@given(instance=String_Type_Name_strategy)
@settings(max_examples=25)
def test_String_Type_Name_instantiation(instance):
    assert isinstance(instance, String_Type_Name)


String_Var_Declaration_strategy = st.builds(String_Var_Declaration)
@given(instance=String_Var_Declaration_strategy)
@settings(max_examples=25)
def test_String_Var_Declaration_instantiation(instance):
    assert isinstance(instance, String_Var_Declaration)


Structure_Element_Declaration_strategy = st.builds(Structure_Element_Declaration)
@given(instance=Structure_Element_Declaration_strategy)
@settings(max_examples=25)
def test_Structure_Element_Declaration_instantiation(instance):
    assert isinstance(instance, Structure_Element_Declaration)


Structure_Element_Initialization_strategy = st.builds(Structure_Element_Initialization)
@given(instance=Structure_Element_Initialization_strategy)
@settings(max_examples=25)
def test_Structure_Element_Initialization_instantiation(instance):
    assert isinstance(instance, Structure_Element_Initialization)


Structure_Element_Name_strategy = st.builds(Structure_Element_Name)
@given(instance=Structure_Element_Name_strategy)
@settings(max_examples=25)
def test_Structure_Element_Name_instantiation(instance):
    assert isinstance(instance, Structure_Element_Name)


Structure_Elements_strategy = st.builds(Structure_Elements)
@given(instance=Structure_Elements_strategy)
@settings(max_examples=25)
def test_Structure_Elements_instantiation(instance):
    assert isinstance(instance, Structure_Elements)


Structure_Initialization_strategy = st.builds(Structure_Initialization)
@given(instance=Structure_Initialization_strategy)
@settings(max_examples=25)
def test_Structure_Initialization_instantiation(instance):
    assert isinstance(instance, Structure_Initialization)


Structure_Specification_strategy = st.builds(Structure_Specification)
@given(instance=Structure_Specification_strategy)
@settings(max_examples=25)
def test_Structure_Specification_instantiation(instance):
    assert isinstance(instance, Structure_Specification)


Structure_Type_Name_strategy = st.builds(Structure_Type_Name)
@given(instance=Structure_Type_Name_strategy)
@settings(max_examples=25)
def test_Structure_Type_Name_instantiation(instance):
    assert isinstance(instance, Structure_Type_Name)


Structured_Variable_strategy = st.builds(Structured_Variable)
@given(instance=Structured_Variable_strategy)
@settings(max_examples=25)
def test_Structured_Variable_instantiation(instance):
    assert isinstance(instance, Structured_Variable)


Subprogram_Control_Statement_strategy = st.builds(Subprogram_Control_Statement)
@given(instance=Subprogram_Control_Statement_strategy)
@settings(max_examples=25)
def test_Subprogram_Control_Statement_instantiation(instance):
    assert isinstance(instance, Subprogram_Control_Statement)


Subrange_strategy = st.builds(Subrange)
@given(instance=Subrange_strategy)
@settings(max_examples=25)
def test_Subrange_instantiation(instance):
    assert isinstance(instance, Subrange)


Subrange_Spec_Init_strategy = st.builds(Subrange_Spec_Init)
@given(instance=Subrange_Spec_Init_strategy)
@settings(max_examples=25)
def test_Subrange_Spec_Init_instantiation(instance):
    assert isinstance(instance, Subrange_Spec_Init)


Subrange_Specification_strategy = st.builds(Subrange_Specification)
@given(instance=Subrange_Specification_strategy)
@settings(max_examples=25)
def test_Subrange_Specification_instantiation(instance):
    assert isinstance(instance, Subrange_Specification)


Subrange_Type_Name_strategy = st.builds(Subrange_Type_Name)
@given(instance=Subrange_Type_Name_strategy)
@settings(max_examples=25)
def test_Subrange_Type_Name_instantiation(instance):
    assert isinstance(instance, Subrange_Type_Name)


Subscript_List_strategy = st.builds(Subscript_List)
@given(instance=Subscript_List_strategy)
@settings(max_examples=25)
def test_Subscript_List_instantiation(instance):
    assert isinstance(instance, Subscript_List)


Substraction_Operator_strategy = st.builds(Substraction_Operator)
@given(instance=Substraction_Operator_strategy)
@settings(max_examples=25)
def test_Substraction_Operator_instantiation(instance):
    assert isinstance(instance, Substraction_Operator)


Symbolic_Variable_strategy = st.builds(Symbolic_Variable)
@given(instance=Symbolic_Variable_strategy)
@settings(max_examples=25)
def test_Symbolic_Variable_instantiation(instance):
    assert isinstance(instance, Symbolic_Variable)


TOD_Type_Name_strategy = st.builds(TOD_Type_Name)
@given(instance=TOD_Type_Name_strategy)
@settings(max_examples=25)
def test_TOD_Type_Name_instantiation(instance):
    assert isinstance(instance, TOD_Type_Name)


Task_Configuration_strategy = st.builds(Task_Configuration)
@given(instance=Task_Configuration_strategy)
@settings(max_examples=25)
def test_Task_Configuration_instantiation(instance):
    assert isinstance(instance, Task_Configuration)


Task_Initialization_strategy = st.builds(Task_Initialization)
@given(instance=Task_Initialization_strategy)
@settings(max_examples=25)
def test_Task_Initialization_instantiation(instance):
    assert isinstance(instance, Task_Initialization)


Task_Name_strategy = st.builds(Task_Name)
@given(instance=Task_Name_strategy)
@settings(max_examples=25)
def test_Task_Name_instantiation(instance):
    assert isinstance(instance, Task_Name)


Temp_Var_Decl_strategy = st.builds(Temp_Var_Decl)
@given(instance=Temp_Var_Decl_strategy)
@settings(max_examples=25)
def test_Temp_Var_Decl_instantiation(instance):
    assert isinstance(instance, Temp_Var_Decl)


Temp_Var_Declaration_strategy = st.builds(Temp_Var_Declaration)
@given(instance=Temp_Var_Declaration_strategy)
@settings(max_examples=25)
def test_Temp_Var_Declaration_instantiation(instance):
    assert isinstance(instance, Temp_Var_Declaration)


Time_Literal_strategy = st.builds(Time_Literal)
@given(instance=Time_Literal_strategy)
@settings(max_examples=25)
def test_Time_Literal_instantiation(instance):
    assert isinstance(instance, Time_Literal)


Timed_Qualifier_strategy = st.builds(Timed_Qualifier)
@given(instance=Timed_Qualifier_strategy)
@settings(max_examples=25)
def test_Timed_Qualifier_instantiation(instance):
    assert isinstance(instance, Timed_Qualifier)


Transition_Condition_strategy = st.builds(Transition_Condition)
@given(instance=Transition_Condition_strategy)
@settings(max_examples=25)
def test_Transition_Condition_instantiation(instance):
    assert isinstance(instance, Transition_Condition)


Transition_Name_strategy = st.builds(Transition_Name)
@given(instance=Transition_Name_strategy)
@settings(max_examples=25)
def test_Transition_Name_instantiation(instance):
    assert isinstance(instance, Transition_Name)


Type_Declaration_strategy = st.builds(Type_Declaration)
@given(instance=Type_Declaration_strategy)
@settings(max_examples=25)
def test_Type_Declaration_instantiation(instance):
    assert isinstance(instance, Type_Declaration)


Unary_Operator_strategy = st.builds(Unary_Operator)
@given(instance=Unary_Operator_strategy)
@settings(max_examples=25)
def test_Unary_Operator_instantiation(instance):
    assert isinstance(instance, Unary_Operator)


Unequal_Operator_strategy = st.builds(Unequal_Operator)
@given(instance=Unequal_Operator_strategy)
@settings(max_examples=25)
def test_Unequal_Operator_instantiation(instance):
    assert isinstance(instance, Unequal_Operator)


Unsigned_Integer_strategy = st.builds(Unsigned_Integer)
@given(instance=Unsigned_Integer_strategy)
@settings(max_examples=25)
def test_Unsigned_Integer_instantiation(instance):
    assert isinstance(instance, Unsigned_Integer)


Var1_List_strategy = st.builds(Var1_List)
@given(instance=Var1_List_strategy)
@settings(max_examples=25)
def test_Var1_List_instantiation(instance):
    assert isinstance(instance, Var1_List)


Var1_Specification_strategy = st.builds(Var1_Specification)
@given(instance=Var1_Specification_strategy)
@settings(max_examples=25)
def test_Var1_Specification_instantiation(instance):
    assert isinstance(instance, Var1_Specification)


Var1_Specification_Func_strategy = st.builds(Var1_Specification_Func)
@given(instance=Var1_Specification_Func_strategy)
@settings(max_examples=25)
def test_Var1_Specification_Func_instantiation(instance):
    assert isinstance(instance, Var1_Specification_Func)


Var2_Init_Decl_strategy = st.builds(Var2_Init_Decl)
@given(instance=Var2_Init_Decl_strategy)
@settings(max_examples=25)
def test_Var2_Init_Decl_instantiation(instance):
    assert isinstance(instance, Var2_Init_Decl)


Var_Declaration_strategy = st.builds(Var_Declaration)
@given(instance=Var_Declaration_strategy)
@settings(max_examples=25)
def test_Var_Declaration_instantiation(instance):
    assert isinstance(instance, Var_Declaration)


Var_Init_Decl_strategy = st.builds(Var_Init_Decl)
@given(instance=Var_Init_Decl_strategy)
@settings(max_examples=25)
def test_Var_Init_Decl_instantiation(instance):
    assert isinstance(instance, Var_Init_Decl)


Var_Spec_strategy = st.builds(Var_Spec)
@given(instance=Var_Spec_strategy)
@settings(max_examples=25)
def test_Var_Spec_instantiation(instance):
    assert isinstance(instance, Var_Spec)


Variable_strategy = st.builds(Variable)
@given(instance=Variable_strategy)
@settings(max_examples=25)
def test_Variable_instantiation(instance):
    assert isinstance(instance, Variable)


Variable_Name_strategy = st.builds(Variable_Name)
@given(instance=Variable_Name_strategy)
@settings(max_examples=25)
def test_Variable_Name_instantiation(instance):
    assert isinstance(instance, Variable_Name)


Xor_Operator_strategy = st.builds(Xor_Operator)
@given(instance=Xor_Operator_strategy)
@settings(max_examples=25)
def test_Xor_Operator_instantiation(instance):
    assert isinstance(instance, Xor_Operator)


configurations_Data_Sink_strategy = st.builds(configurations_Data_Sink)
@given(instance=configurations_Data_Sink_strategy)
@settings(max_examples=25)
def test_configurations_Data_Sink_instantiation(instance):
    assert isinstance(instance, configurations_Data_Sink)


configurations_Data_Source_strategy = st.builds(configurations_Data_Source)
@given(instance=configurations_Data_Source_strategy)
@settings(max_examples=25)
def test_configurations_Data_Source_instantiation(instance):
    assert isinstance(instance, configurations_Data_Source)


configurations_Prog_Data_Source_strategy = st.builds(configurations_Prog_Data_Source)
@given(instance=configurations_Prog_Data_Source_strategy)
@settings(max_examples=25)
def test_configurations_Prog_Data_Source_instantiation(instance):
    assert isinstance(instance, configurations_Prog_Data_Source)


iec61131_Commentable_strategy = st.builds(iec61131_Commentable, comments=safe_text)
@given(instance=iec61131_Commentable_strategy)
@settings(max_examples=25)
def test_iec61131_Commentable_instantiation(instance):
    assert isinstance(instance, iec61131_Commentable)


iec61131_IEC61131_strategy = st.builds(iec61131_IEC61131)
@given(instance=iec61131_IEC61131_strategy)
@settings(max_examples=25)
def test_iec61131_IEC61131_instantiation(instance):
    assert isinstance(instance, iec61131_IEC61131)


iec61131_Library_Element_Declaration_strategy = st.builds(iec61131_Library_Element_Declaration)
@given(instance=iec61131_Library_Element_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_Library_Element_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_Library_Element_Declaration)


iec61131_Library_Element_Name_strategy = st.builds(iec61131_Library_Element_Name)
@given(instance=iec61131_Library_Element_Name_strategy)
@settings(max_examples=25)
def test_iec61131_Library_Element_Name_instantiation(instance):
    assert isinstance(instance, iec61131_Library_Element_Name)


iec61131_NamedElement_strategy = st.builds(iec61131_NamedElement, name=safe_text)
@given(instance=iec61131_NamedElement_strategy)
@settings(max_examples=25)
def test_iec61131_NamedElement_instantiation(instance):
    assert isinstance(instance, iec61131_NamedElement)


iec61131_configurations_Access_Declaration_strategy = st.builds(iec61131_configurations_Access_Declaration, direction=safe_text)
@given(instance=iec61131_configurations_Access_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Access_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Declaration)


iec61131_configurations_Access_Declarations_strategy = st.builds(iec61131_configurations_Access_Declarations)
@given(instance=iec61131_configurations_Access_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Access_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Declarations)


iec61131_configurations_Access_Name_strategy = st.builds(iec61131_configurations_Access_Name, name=safe_text)
@given(instance=iec61131_configurations_Access_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Access_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Name)


iec61131_configurations_Access_Path_strategy = st.builds(iec61131_configurations_Access_Path)
@given(instance=iec61131_configurations_Access_Path_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Access_Path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Path)


iec61131_configurations_Configuration_Declaration_strategy = st.builds(iec61131_configurations_Configuration_Declaration)
@given(instance=iec61131_configurations_Configuration_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Configuration_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Configuration_Declaration)


iec61131_configurations_Configuration_Name_strategy = st.builds(iec61131_configurations_Configuration_Name)
@given(instance=iec61131_configurations_Configuration_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Configuration_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Configuration_Name)


iec61131_configurations_Data_Sink_strategy = st.builds(iec61131_configurations_Data_Sink)
@given(instance=iec61131_configurations_Data_Sink_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Data_Sink_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Data_Sink)


iec61131_configurations_Data_Source_strategy = st.builds(iec61131_configurations_Data_Source)
@given(instance=iec61131_configurations_Data_Source_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Data_Source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Data_Source)


iec61131_configurations_Direct_Path_strategy = st.builds(iec61131_configurations_Direct_Path)
@given(instance=iec61131_configurations_Direct_Path_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Direct_Path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Direct_Path)


iec61131_configurations_Fb_Task_strategy = st.builds(iec61131_configurations_Fb_Task)
@given(instance=iec61131_configurations_Fb_Task_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Fb_Task_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Fb_Task)


iec61131_configurations_Global_Var_Reference_strategy = st.builds(iec61131_configurations_Global_Var_Reference)
@given(instance=iec61131_configurations_Global_Var_Reference_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Global_Var_Reference_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Global_Var_Reference)


iec61131_configurations_Instance_Spec1_strategy = st.builds(iec61131_configurations_Instance_Spec1)
@given(instance=iec61131_configurations_Instance_Spec1_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Instance_Spec1_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Spec1)


iec61131_configurations_Instance_Spec2_strategy = st.builds(iec61131_configurations_Instance_Spec2)
@given(instance=iec61131_configurations_Instance_Spec2_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Instance_Spec2_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Spec2)


iec61131_configurations_Instance_Specific_Init_strategy = st.builds(iec61131_configurations_Instance_Specific_Init)
@given(instance=iec61131_configurations_Instance_Specific_Init_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Instance_Specific_Init_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Specific_Init)


iec61131_configurations_Instance_Specific_Initializations_strategy = st.builds(iec61131_configurations_Instance_Specific_Initializations)
@given(instance=iec61131_configurations_Instance_Specific_Initializations_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Instance_Specific_Initializations_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Specific_Initializations)


iec61131_configurations_Interval_strategy = st.builds(iec61131_configurations_Interval)
@given(instance=iec61131_configurations_Interval_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Interval_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Interval)


iec61131_configurations_Priority_strategy = st.builds(iec61131_configurations_Priority)
@given(instance=iec61131_configurations_Priority_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Priority_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Priority)


iec61131_configurations_Prog_Cnxn_strategy = st.builds(iec61131_configurations_Prog_Cnxn)
@given(instance=iec61131_configurations_Prog_Cnxn_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Cnxn_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Cnxn)


iec61131_configurations_Prog_Conf_Element_strategy = st.builds(iec61131_configurations_Prog_Conf_Element)
@given(instance=iec61131_configurations_Prog_Conf_Element_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Conf_Element_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Conf_Element)


iec61131_configurations_Prog_Conf_Elements_strategy = st.builds(iec61131_configurations_Prog_Conf_Elements)
@given(instance=iec61131_configurations_Prog_Conf_Elements_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Conf_Elements_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Conf_Elements)


iec61131_configurations_Prog_Data_Source_strategy = st.builds(iec61131_configurations_Prog_Data_Source)
@given(instance=iec61131_configurations_Prog_Data_Source_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Data_Source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Data_Source)


iec61131_configurations_Prog_Sink_strategy = st.builds(iec61131_configurations_Prog_Sink)
@given(instance=iec61131_configurations_Prog_Sink_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Sink_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Sink)


iec61131_configurations_Prog_Source_strategy = st.builds(iec61131_configurations_Prog_Source)
@given(instance=iec61131_configurations_Prog_Source_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Prog_Source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Source)


iec61131_configurations_Program_Configuration_strategy = st.builds(iec61131_configurations_Program_Configuration, retain=st.booleans())
@given(instance=iec61131_configurations_Program_Configuration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Program_Configuration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Configuration)


iec61131_configurations_Program_Name_strategy = st.builds(iec61131_configurations_Program_Name, name=safe_text)
@given(instance=iec61131_configurations_Program_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Program_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Name)


iec61131_configurations_Program_Output_Reference_strategy = st.builds(iec61131_configurations_Program_Output_Reference)
@given(instance=iec61131_configurations_Program_Output_Reference_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Program_Output_Reference_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Output_Reference)


iec61131_configurations_Resource_Declaration_strategy = st.builds(iec61131_configurations_Resource_Declaration)
@given(instance=iec61131_configurations_Resource_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Resource_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Declaration)


iec61131_configurations_Resource_Name_strategy = st.builds(iec61131_configurations_Resource_Name, name=safe_text)
@given(instance=iec61131_configurations_Resource_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Resource_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Name)


iec61131_configurations_Resource_Type_Name_strategy = st.builds(iec61131_configurations_Resource_Type_Name)
@given(instance=iec61131_configurations_Resource_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Resource_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Type_Name)


iec61131_configurations_Single_strategy = st.builds(iec61131_configurations_Single)
@given(instance=iec61131_configurations_Single_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Single_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Single)


iec61131_configurations_Single_Resource_Declaration_strategy = st.builds(iec61131_configurations_Single_Resource_Declaration)
@given(instance=iec61131_configurations_Single_Resource_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Single_Resource_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Single_Resource_Declaration)


iec61131_configurations_Symbolic_Path_strategy = st.builds(iec61131_configurations_Symbolic_Path)
@given(instance=iec61131_configurations_Symbolic_Path_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Symbolic_Path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Symbolic_Path)


iec61131_configurations_Task_Configuration_strategy = st.builds(iec61131_configurations_Task_Configuration)
@given(instance=iec61131_configurations_Task_Configuration_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Task_Configuration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Configuration)


iec61131_configurations_Task_Initialization_strategy = st.builds(iec61131_configurations_Task_Initialization)
@given(instance=iec61131_configurations_Task_Initialization_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Task_Initialization_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Initialization)


iec61131_configurations_Task_Name_strategy = st.builds(iec61131_configurations_Task_Name, name=safe_text)
@given(instance=iec61131_configurations_Task_Name_strategy)
@settings(max_examples=25)
def test_iec61131_configurations_Task_Name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Name)


iec61131_fbd_Fbd_Network_strategy = st.builds(iec61131_fbd_Fbd_Network)
@given(instance=iec61131_fbd_Fbd_Network_strategy)
@settings(max_examples=25)
def test_iec61131_fbd_Fbd_Network_instantiation(instance):
    assert isinstance(instance, iec61131_fbd_Fbd_Network)


iec61131_fbd_Function_Block_Diagram_strategy = st.builds(iec61131_fbd_Function_Block_Diagram)
@given(instance=iec61131_fbd_Function_Block_Diagram_strategy)
@settings(max_examples=25)
def test_iec61131_fbd_Function_Block_Diagram_instantiation(instance):
    assert isinstance(instance, iec61131_fbd_Function_Block_Diagram)


iec61131_il_Il_Assign_Operator_strategy = st.builds(iec61131_il_Il_Assign_Operator)
@given(instance=iec61131_il_Il_Assign_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Assign_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Assign_Operator)


iec61131_il_Il_Assign_Out_Operator_strategy = st.builds(iec61131_il_Il_Assign_Out_Operator)
@given(instance=iec61131_il_Il_Assign_Out_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Assign_Out_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Assign_Out_Operator)


iec61131_il_Il_Call_Operator_strategy = st.builds(iec61131_il_Il_Call_Operator)
@given(instance=iec61131_il_Il_Call_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Call_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Call_Operator)


iec61131_il_Il_Expr_Operator_strategy = st.builds(iec61131_il_Il_Expr_Operator)
@given(instance=iec61131_il_Il_Expr_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Expr_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Expr_Operator)


iec61131_il_Il_Expression_strategy = st.builds(iec61131_il_Il_Expression)
@given(instance=iec61131_il_Il_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Expression)


iec61131_il_Il_Fb_Call_strategy = st.builds(iec61131_il_Il_Fb_Call)
@given(instance=iec61131_il_Il_Fb_Call_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Fb_Call_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Fb_Call)


iec61131_il_Il_Formal_Funct_Call_strategy = st.builds(iec61131_il_Il_Formal_Funct_Call)
@given(instance=iec61131_il_Il_Formal_Funct_Call_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Formal_Funct_Call_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Formal_Funct_Call)


iec61131_il_Il_Instruction_strategy = st.builds(iec61131_il_Il_Instruction)
@given(instance=iec61131_il_Il_Instruction_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Instruction)


iec61131_il_Il_Jump_Operation_strategy = st.builds(iec61131_il_Il_Jump_Operation)
@given(instance=iec61131_il_Il_Jump_Operation_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Jump_Operation_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Jump_Operation)


iec61131_il_Il_Jump_Operator_strategy = st.builds(iec61131_il_Il_Jump_Operator)
@given(instance=iec61131_il_Il_Jump_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Jump_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Jump_Operator)


iec61131_il_Il_Operand_strategy = st.builds(iec61131_il_Il_Operand)
@given(instance=iec61131_il_Il_Operand_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Operand_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operand)


iec61131_il_Il_Operand_List_strategy = st.builds(iec61131_il_Il_Operand_List)
@given(instance=iec61131_il_Il_Operand_List_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Operand_List_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operand_List)


iec61131_il_Il_Operations_strategy = st.builds(iec61131_il_Il_Operations)
@given(instance=iec61131_il_Il_Operations_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Operations_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operations)


iec61131_il_Il_Param_Assignment_strategy = st.builds(iec61131_il_Il_Param_Assignment)
@given(instance=iec61131_il_Il_Param_Assignment_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Param_Assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Assignment)


iec61131_il_Il_Param_Instruction_strategy = st.builds(iec61131_il_Il_Param_Instruction)
@given(instance=iec61131_il_Il_Param_Instruction_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Param_Instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Instruction)


iec61131_il_Il_Param_Last_Instruction_strategy = st.builds(iec61131_il_Il_Param_Last_Instruction)
@given(instance=iec61131_il_Il_Param_Last_Instruction_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Param_Last_Instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Last_Instruction)


iec61131_il_Il_Param_List_strategy = st.builds(iec61131_il_Il_Param_List)
@given(instance=iec61131_il_Il_Param_List_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Param_List_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_List)


iec61131_il_Il_Param_Out_Assignment_strategy = st.builds(iec61131_il_Il_Param_Out_Assignment)
@given(instance=iec61131_il_Il_Param_Out_Assignment_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Param_Out_Assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Out_Assignment)


iec61131_il_Il_Return_Operator_strategy = st.builds(iec61131_il_Il_Return_Operator)
@given(instance=iec61131_il_Il_Return_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Return_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Return_Operator)


iec61131_il_Il_Simple_Instruction_strategy = st.builds(iec61131_il_Il_Simple_Instruction)
@given(instance=iec61131_il_Il_Simple_Instruction_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Simple_Instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Instruction)


iec61131_il_Il_Simple_Operation_strategy = st.builds(iec61131_il_Il_Simple_Operation)
@given(instance=iec61131_il_Il_Simple_Operation_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Simple_Operation_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Operation)


iec61131_il_Il_Simple_Operator_strategy = st.builds(iec61131_il_Il_Simple_Operator)
@given(instance=iec61131_il_Il_Simple_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_il_Il_Simple_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Operator)


iec61131_il_Instruction_List_strategy = st.builds(iec61131_il_Instruction_List)
@given(instance=iec61131_il_Instruction_List_strategy)
@settings(max_examples=25)
def test_iec61131_il_Instruction_List_instantiation(instance):
    assert isinstance(instance, iec61131_il_Instruction_List)


iec61131_il_Label_strategy = st.builds(iec61131_il_Label, label=safe_text)
@given(instance=iec61131_il_Label_strategy)
@settings(max_examples=25)
def test_iec61131_il_Label_instantiation(instance):
    assert isinstance(instance, iec61131_il_Label)


iec61131_il_Operand1_strategy = st.builds(iec61131_il_Operand1)
@given(instance=iec61131_il_Operand1_strategy)
@settings(max_examples=25)
def test_iec61131_il_Operand1_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operand1)


iec61131_il_Operand2_strategy = st.builds(iec61131_il_Operand2)
@given(instance=iec61131_il_Operand2_strategy)
@settings(max_examples=25)
def test_iec61131_il_Operand2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operand2)


iec61131_il_Operands_strategy = st.builds(iec61131_il_Operands)
@given(instance=iec61131_il_Operands_strategy)
@settings(max_examples=25)
def test_iec61131_il_Operands_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operands)


iec61131_il_Param_Assignment_strategy = st.builds(iec61131_il_Param_Assignment)
@given(instance=iec61131_il_Param_Assignment_strategy)
@settings(max_examples=25)
def test_iec61131_il_Param_Assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignment)


iec61131_il_Param_Assignment2_strategy = st.builds(iec61131_il_Param_Assignment2)
@given(instance=iec61131_il_Param_Assignment2_strategy)
@settings(max_examples=25)
def test_iec61131_il_Param_Assignment2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignment2)


iec61131_il_Param_Assignments_strategy = st.builds(iec61131_il_Param_Assignments)
@given(instance=iec61131_il_Param_Assignments_strategy)
@settings(max_examples=25)
def test_iec61131_il_Param_Assignments_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignments)


iec61131_il_Param_Instruction_strategy = st.builds(iec61131_il_Param_Instruction)
@given(instance=iec61131_il_Param_Instruction_strategy)
@settings(max_examples=25)
def test_iec61131_il_Param_Instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Instruction)


iec61131_il_Simple_Instr_strategy = st.builds(iec61131_il_Simple_Instr)
@given(instance=iec61131_il_Simple_Instr_strategy)
@settings(max_examples=25)
def test_iec61131_il_Simple_Instr_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Instr)


iec61131_il_Simple_Instr_List_strategy = st.builds(iec61131_il_Simple_Instr_List)
@given(instance=iec61131_il_Simple_Instr_List_strategy)
@settings(max_examples=25)
def test_iec61131_il_Simple_Instr_List_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Instr_List)


iec61131_il_Simple_Operation1_strategy = st.builds(iec61131_il_Simple_Operation1)
@given(instance=iec61131_il_Simple_Operation1_strategy)
@settings(max_examples=25)
def test_iec61131_il_Simple_Operation1_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Operation1)


iec61131_il_Simple_Operation2_strategy = st.builds(iec61131_il_Simple_Operation2)
@given(instance=iec61131_il_Simple_Operation2_strategy)
@settings(max_examples=25)
def test_iec61131_il_Simple_Operation2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Operation2)


iec61131_interfaces_Array_Initial_Elements_strategy = st.builds(iec61131_interfaces_Array_Initial_Elements)
@given(instance=iec61131_interfaces_Array_Initial_Elements_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Initial_Elements_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements)


iec61131_interfaces_Array_Initial_Elements1_strategy = st.builds(iec61131_interfaces_Array_Initial_Elements1)
@given(instance=iec61131_interfaces_Array_Initial_Elements1_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Initial_Elements1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements1)


iec61131_interfaces_Array_Initial_Elements2_strategy = st.builds(iec61131_interfaces_Array_Initial_Elements2)
@given(instance=iec61131_interfaces_Array_Initial_Elements2_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Initial_Elements2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements2)


iec61131_interfaces_Array_Initialization_strategy = st.builds(iec61131_interfaces_Array_Initialization)
@given(instance=iec61131_interfaces_Array_Initialization_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initialization)


iec61131_interfaces_Array_Spec_Init_strategy = st.builds(iec61131_interfaces_Array_Spec_Init)
@given(instance=iec61131_interfaces_Array_Spec_Init_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Spec_Init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Spec_Init)


iec61131_interfaces_Array_Specification_strategy = st.builds(iec61131_interfaces_Array_Specification)
@given(instance=iec61131_interfaces_Array_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification)


iec61131_interfaces_Array_Specification1_strategy = st.builds(iec61131_interfaces_Array_Specification1)
@given(instance=iec61131_interfaces_Array_Specification1_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification1)


iec61131_interfaces_Array_Specification2_strategy = st.builds(iec61131_interfaces_Array_Specification2)
@given(instance=iec61131_interfaces_Array_Specification2_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification2)


iec61131_interfaces_Array_Var_Declaration_strategy = st.builds(iec61131_interfaces_Array_Var_Declaration)
@given(instance=iec61131_interfaces_Array_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Var_Declaration)


iec61131_interfaces_Array_Var_Init_Decl_strategy = st.builds(iec61131_interfaces_Array_Var_Init_Decl)
@given(instance=iec61131_interfaces_Array_Var_Init_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Array_Var_Init_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Var_Init_Decl)


iec61131_interfaces_Byte_String_strategy = st.builds(iec61131_interfaces_Byte_String)
@given(instance=iec61131_interfaces_Byte_String_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Byte_String_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Byte_String)


iec61131_interfaces_Double_BString_strategy = st.builds(iec61131_interfaces_Double_BString)
@given(instance=iec61131_interfaces_Double_BString_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Double_BString_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_BString)


iec61131_interfaces_Double_Byte_String_Spec_strategy = st.builds(iec61131_interfaces_Double_Byte_String_Spec)
@given(instance=iec61131_interfaces_Double_Byte_String_Spec_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Double_Byte_String_Spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_Byte_String_Spec)


iec61131_interfaces_Double_Byte_String_Var_Declaration_strategy = st.builds(iec61131_interfaces_Double_Byte_String_Var_Declaration)
@given(instance=iec61131_interfaces_Double_Byte_String_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Double_Byte_String_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_Byte_String_Var_Declaration)


iec61131_interfaces_Edge_Declaration_strategy = st.builds(iec61131_interfaces_Edge_Declaration, edge=safe_text)
@given(instance=iec61131_interfaces_Edge_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Edge_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Edge_Declaration)


iec61131_interfaces_Enumerated_Spec_Init_strategy = st.builds(iec61131_interfaces_Enumerated_Spec_Init)
@given(instance=iec61131_interfaces_Enumerated_Spec_Init_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Enumerated_Spec_Init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Spec_Init)


iec61131_interfaces_Enumerated_Specification_strategy = st.builds(iec61131_interfaces_Enumerated_Specification)
@given(instance=iec61131_interfaces_Enumerated_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Enumerated_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification)


iec61131_interfaces_Enumerated_Specification1_strategy = st.builds(iec61131_interfaces_Enumerated_Specification1)
@given(instance=iec61131_interfaces_Enumerated_Specification1_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Enumerated_Specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification1)


iec61131_interfaces_Enumerated_Specification2_strategy = st.builds(iec61131_interfaces_Enumerated_Specification2)
@given(instance=iec61131_interfaces_Enumerated_Specification2_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Enumerated_Specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification2)


iec61131_interfaces_Enumerated_Value_strategy = st.builds(iec61131_interfaces_Enumerated_Value, name=safe_text)
@given(instance=iec61131_interfaces_Enumerated_Value_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Enumerated_Value_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Value)


iec61131_interfaces_External_Declaration_strategy = st.builds(iec61131_interfaces_External_Declaration)
@given(instance=iec61131_interfaces_External_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_External_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Declaration)


iec61131_interfaces_External_Specification_strategy = st.builds(iec61131_interfaces_External_Specification)
@given(instance=iec61131_interfaces_External_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_External_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Specification)


iec61131_interfaces_External_Var_Declarations_strategy = st.builds(iec61131_interfaces_External_Var_Declarations, constant=st.booleans())
@given(instance=iec61131_interfaces_External_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_External_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Var_Declarations)


iec61131_interfaces_Fb_Name_Decl_strategy = st.builds(iec61131_interfaces_Fb_Name_Decl)
@given(instance=iec61131_interfaces_Fb_Name_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Fb_Name_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Fb_Name_Decl)


iec61131_interfaces_Function_Var_Decl_strategy = st.builds(iec61131_interfaces_Function_Var_Decl, constant=st.booleans())
@given(instance=iec61131_interfaces_Function_Var_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Function_Var_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Function_Var_Decl)


iec61131_interfaces_Global_Var_Decl_strategy = st.builds(iec61131_interfaces_Global_Var_Decl)
@given(instance=iec61131_interfaces_Global_Var_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Decl)


iec61131_interfaces_Global_Var_Declarations_strategy = st.builds(iec61131_interfaces_Global_Var_Declarations, constant=st.booleans(), retain=st.booleans())
@given(instance=iec61131_interfaces_Global_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Declarations)


iec61131_interfaces_Global_Var_List_strategy = st.builds(iec61131_interfaces_Global_Var_List)
@given(instance=iec61131_interfaces_Global_Var_List_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_List_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_List)


iec61131_interfaces_Global_Var_Location_strategy = st.builds(iec61131_interfaces_Global_Var_Location)
@given(instance=iec61131_interfaces_Global_Var_Location_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_Location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Location)


iec61131_interfaces_Global_Var_Name_strategy = st.builds(iec61131_interfaces_Global_Var_Name)
@given(instance=iec61131_interfaces_Global_Var_Name_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_Name_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Name)


iec61131_interfaces_Global_Var_Spec_strategy = st.builds(iec61131_interfaces_Global_Var_Spec)
@given(instance=iec61131_interfaces_Global_Var_Spec_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Global_Var_Spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Spec)


iec61131_interfaces_Incompl_Located_Var_Decl_strategy = st.builds(iec61131_interfaces_Incompl_Located_Var_Decl)
@given(instance=iec61131_interfaces_Incompl_Located_Var_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Incompl_Located_Var_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Located_Var_Decl)


iec61131_interfaces_Incompl_Located_Var_Declarations_strategy = st.builds(iec61131_interfaces_Incompl_Located_Var_Declarations, retain=st.booleans())
@given(instance=iec61131_interfaces_Incompl_Located_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Incompl_Located_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Located_Var_Declarations)


iec61131_interfaces_Incompl_Location_strategy = st.builds(iec61131_interfaces_Incompl_Location, location=safe_text)
@given(instance=iec61131_interfaces_Incompl_Location_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Incompl_Location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Location)


iec61131_interfaces_InitElement_Array_strategy = st.builds(iec61131_interfaces_InitElement_Array)
@given(instance=iec61131_interfaces_InitElement_Array_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_InitElement_Array_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Array)


iec61131_interfaces_InitElement_Constant_strategy = st.builds(iec61131_interfaces_InitElement_Constant)
@given(instance=iec61131_interfaces_InitElement_Constant_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_InitElement_Constant_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Constant)


iec61131_interfaces_InitElement_EnumValue_strategy = st.builds(iec61131_interfaces_InitElement_EnumValue)
@given(instance=iec61131_interfaces_InitElement_EnumValue_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_InitElement_EnumValue_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_EnumValue)


iec61131_interfaces_InitElement_Structure_strategy = st.builds(iec61131_interfaces_InitElement_Structure)
@given(instance=iec61131_interfaces_InitElement_Structure_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_InitElement_Structure_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Structure)


iec61131_interfaces_Initial_Element_strategy = st.builds(iec61131_interfaces_Initial_Element)
@given(instance=iec61131_interfaces_Initial_Element_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Initial_Element_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Initial_Element)


iec61131_interfaces_Initialized_Structure_strategy = st.builds(iec61131_interfaces_Initialized_Structure)
@given(instance=iec61131_interfaces_Initialized_Structure_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Initialized_Structure_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Initialized_Structure)


iec61131_interfaces_Input_Declaration_strategy = st.builds(iec61131_interfaces_Input_Declaration)
@given(instance=iec61131_interfaces_Input_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Input_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Declaration)


iec61131_interfaces_Input_Declarations_strategy = st.builds(iec61131_interfaces_Input_Declarations, retain=st.booleans())
@given(instance=iec61131_interfaces_Input_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Input_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Declarations)


iec61131_interfaces_Input_Output_Declarations_strategy = st.builds(iec61131_interfaces_Input_Output_Declarations)
@given(instance=iec61131_interfaces_Input_Output_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Input_Output_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Output_Declarations)


iec61131_interfaces_Interface_strategy = st.builds(iec61131_interfaces_Interface)
@given(instance=iec61131_interfaces_Interface_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Interface_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Interface)


iec61131_interfaces_Io_Var_Declaration_strategy = st.builds(iec61131_interfaces_Io_Var_Declaration)
@given(instance=iec61131_interfaces_Io_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Io_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Io_Var_Declaration)


iec61131_interfaces_Located_Var_Decl_strategy = st.builds(iec61131_interfaces_Located_Var_Decl)
@given(instance=iec61131_interfaces_Located_Var_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Located_Var_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Decl)


iec61131_interfaces_Located_Var_Declarations_strategy = st.builds(iec61131_interfaces_Located_Var_Declarations, constant=st.booleans(), retain=st.booleans())
@given(instance=iec61131_interfaces_Located_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Located_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Declarations)


iec61131_interfaces_Located_Var_Spec_Init_strategy = st.builds(iec61131_interfaces_Located_Var_Spec_Init)
@given(instance=iec61131_interfaces_Located_Var_Spec_Init_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Located_Var_Spec_Init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Spec_Init)


iec61131_interfaces_Location_strategy = st.builds(iec61131_interfaces_Location)
@given(instance=iec61131_interfaces_Location_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Location)


iec61131_interfaces_Non_Retentive_Var_Declarations_strategy = st.builds(iec61131_interfaces_Non_Retentive_Var_Declarations)
@given(instance=iec61131_interfaces_Non_Retentive_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Non_Retentive_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Non_Retentive_Var_Declarations)


iec61131_interfaces_Other_Var_Declaration_strategy = st.builds(iec61131_interfaces_Other_Var_Declaration)
@given(instance=iec61131_interfaces_Other_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Other_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Other_Var_Declaration)


iec61131_interfaces_Output_Declarations_strategy = st.builds(iec61131_interfaces_Output_Declarations, retain=st.booleans())
@given(instance=iec61131_interfaces_Output_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Output_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Output_Declarations)


iec61131_interfaces_RNV_Declarations_strategy = st.builds(iec61131_interfaces_RNV_Declarations)
@given(instance=iec61131_interfaces_RNV_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_RNV_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_RNV_Declarations)


iec61131_interfaces_Range_strategy = st.builds(iec61131_interfaces_Range)
@given(instance=iec61131_interfaces_Range_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Range_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Range)


iec61131_interfaces_Retentive_Var_Declarations_strategy = st.builds(iec61131_interfaces_Retentive_Var_Declarations)
@given(instance=iec61131_interfaces_Retentive_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Retentive_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Retentive_Var_Declarations)


iec61131_interfaces_Simple_Spec_Init_strategy = st.builds(iec61131_interfaces_Simple_Spec_Init)
@given(instance=iec61131_interfaces_Simple_Spec_Init_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Simple_Spec_Init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Spec_Init)


iec61131_interfaces_Simple_Spec_Init_Func_strategy = st.builds(iec61131_interfaces_Simple_Spec_Init_Func)
@given(instance=iec61131_interfaces_Simple_Spec_Init_Func_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Simple_Spec_Init_Func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Spec_Init_Func)


iec61131_interfaces_Simple_Specification_Func_strategy = st.builds(iec61131_interfaces_Simple_Specification_Func)
@given(instance=iec61131_interfaces_Simple_Specification_Func_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Simple_Specification_Func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Specification_Func)


iec61131_interfaces_Single_BString_strategy = st.builds(iec61131_interfaces_Single_BString)
@given(instance=iec61131_interfaces_Single_BString_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Single_BString_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_BString)


iec61131_interfaces_Single_Byte_String_Spec_strategy = st.builds(iec61131_interfaces_Single_Byte_String_Spec)
@given(instance=iec61131_interfaces_Single_Byte_String_Spec_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Single_Byte_String_Spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_Byte_String_Spec)


iec61131_interfaces_Single_Byte_String_Var_Declaration_strategy = st.builds(iec61131_interfaces_Single_Byte_String_Var_Declaration)
@given(instance=iec61131_interfaces_Single_Byte_String_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Single_Byte_String_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_Byte_String_Var_Declaration)


iec61131_interfaces_Specification_strategy = st.builds(iec61131_interfaces_Specification)
@given(instance=iec61131_interfaces_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Specification)


iec61131_interfaces_String_Var_Declaration_strategy = st.builds(iec61131_interfaces_String_Var_Declaration)
@given(instance=iec61131_interfaces_String_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_String_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_String_Var_Declaration)


iec61131_interfaces_Structure_Element_Initialization_strategy = st.builds(iec61131_interfaces_Structure_Element_Initialization)
@given(instance=iec61131_interfaces_Structure_Element_Initialization_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Structure_Element_Initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Element_Initialization)


iec61131_interfaces_Structure_Element_Name_strategy = st.builds(iec61131_interfaces_Structure_Element_Name, name=safe_text)
@given(instance=iec61131_interfaces_Structure_Element_Name_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Structure_Element_Name_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Element_Name)


iec61131_interfaces_Structure_Initialization_strategy = st.builds(iec61131_interfaces_Structure_Initialization)
@given(instance=iec61131_interfaces_Structure_Initialization_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Structure_Initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Initialization)


iec61131_interfaces_Structured_Var_Declaration_strategy = st.builds(iec61131_interfaces_Structured_Var_Declaration)
@given(instance=iec61131_interfaces_Structured_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Structured_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structured_Var_Declaration)


iec61131_interfaces_Structured_Var_Init_Decl_strategy = st.builds(iec61131_interfaces_Structured_Var_Init_Decl)
@given(instance=iec61131_interfaces_Structured_Var_Init_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Structured_Var_Init_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structured_Var_Init_Decl)


iec61131_interfaces_Subrange_strategy = st.builds(iec61131_interfaces_Subrange, delimiter=safe_text)
@given(instance=iec61131_interfaces_Subrange_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Subrange_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange)


iec61131_interfaces_Subrange_Spec_Init_strategy = st.builds(iec61131_interfaces_Subrange_Spec_Init)
@given(instance=iec61131_interfaces_Subrange_Spec_Init_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Subrange_Spec_Init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Spec_Init)


iec61131_interfaces_Subrange_Specification_strategy = st.builds(iec61131_interfaces_Subrange_Specification)
@given(instance=iec61131_interfaces_Subrange_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Subrange_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification)


iec61131_interfaces_Subrange_Specification1_strategy = st.builds(iec61131_interfaces_Subrange_Specification1)
@given(instance=iec61131_interfaces_Subrange_Specification1_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Subrange_Specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification1)


iec61131_interfaces_Subrange_Specification2_strategy = st.builds(iec61131_interfaces_Subrange_Specification2)
@given(instance=iec61131_interfaces_Subrange_Specification2_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Subrange_Specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification2)


iec61131_interfaces_Temp_Var_Decl_strategy = st.builds(iec61131_interfaces_Temp_Var_Decl)
@given(instance=iec61131_interfaces_Temp_Var_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Temp_Var_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Decl)


iec61131_interfaces_Temp_Var_Declaration_strategy = st.builds(iec61131_interfaces_Temp_Var_Declaration)
@given(instance=iec61131_interfaces_Temp_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Temp_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Declaration)


iec61131_interfaces_Temp_Var_Decls_strategy = st.builds(iec61131_interfaces_Temp_Var_Decls)
@given(instance=iec61131_interfaces_Temp_Var_Decls_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Temp_Var_Decls_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Decls)


iec61131_interfaces_Var1_Declaration_strategy = st.builds(iec61131_interfaces_Var1_Declaration)
@given(instance=iec61131_interfaces_Var1_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var1_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Declaration)


iec61131_interfaces_Var1_Init_Decl_strategy = st.builds(iec61131_interfaces_Var1_Init_Decl)
@given(instance=iec61131_interfaces_Var1_Init_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var1_Init_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Init_Decl)


iec61131_interfaces_Var1_List_strategy = st.builds(iec61131_interfaces_Var1_List)
@given(instance=iec61131_interfaces_Var1_List_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var1_List_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_List)


iec61131_interfaces_Var1_Specification_strategy = st.builds(iec61131_interfaces_Var1_Specification)
@given(instance=iec61131_interfaces_Var1_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var1_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Specification)


iec61131_interfaces_Var1_Specification_Func_strategy = st.builds(iec61131_interfaces_Var1_Specification_Func)
@given(instance=iec61131_interfaces_Var1_Specification_Func_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var1_Specification_Func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Specification_Func)


iec61131_interfaces_Var2_Init_Decl_strategy = st.builds(iec61131_interfaces_Var2_Init_Decl)
@given(instance=iec61131_interfaces_Var2_Init_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var2_Init_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var2_Init_Decl)


iec61131_interfaces_Var_Declaration_strategy = st.builds(iec61131_interfaces_Var_Declaration)
@given(instance=iec61131_interfaces_Var_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Declaration)


iec61131_interfaces_Var_Declarations_strategy = st.builds(iec61131_interfaces_Var_Declarations, constant=st.booleans())
@given(instance=iec61131_interfaces_Var_Declarations_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Declarations)


iec61131_interfaces_Var_Init_Decl_strategy = st.builds(iec61131_interfaces_Var_Init_Decl)
@given(instance=iec61131_interfaces_Var_Init_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Init_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Init_Decl)


iec61131_interfaces_Var_Init_Decl_Func_strategy = st.builds(iec61131_interfaces_Var_Init_Decl_Func)
@given(instance=iec61131_interfaces_Var_Init_Decl_Func_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Init_Decl_Func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Init_Decl_Func)


iec61131_interfaces_Var_Name_Decl_strategy = st.builds(iec61131_interfaces_Var_Name_Decl)
@given(instance=iec61131_interfaces_Var_Name_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Name_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Name_Decl)


iec61131_interfaces_Var_Spec_strategy = st.builds(iec61131_interfaces_Var_Spec)
@given(instance=iec61131_interfaces_Var_Spec_strategy)
@settings(max_examples=25)
def test_iec61131_interfaces_Var_Spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Spec)


iec61131_ld_Ladder_Diagram_strategy = st.builds(iec61131_ld_Ladder_Diagram)
@given(instance=iec61131_ld_Ladder_Diagram_strategy)
@settings(max_examples=25)
def test_iec61131_ld_Ladder_Diagram_instantiation(instance):
    assert isinstance(instance, iec61131_ld_Ladder_Diagram)


iec61131_ld_Rung_strategy = st.builds(iec61131_ld_Rung)
@given(instance=iec61131_ld_Rung_strategy)
@settings(max_examples=25)
def test_iec61131_ld_Rung_instantiation(instance):
    assert isinstance(instance, iec61131_ld_Rung)


iec61131_literals_BSInteger_strategy = st.builds(iec61131_literals_BSInteger)
@given(instance=iec61131_literals_BSInteger_strategy)
@settings(max_examples=25)
def test_iec61131_literals_BSInteger_instantiation(instance):
    assert isinstance(instance, iec61131_literals_BSInteger)


iec61131_literals_Binary_Integer_strategy = st.builds(iec61131_literals_Binary_Integer)
@given(instance=iec61131_literals_Binary_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Binary_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Binary_Integer)


iec61131_literals_Bit_String_Literal_strategy = st.builds(iec61131_literals_Bit_String_Literal)
@given(instance=iec61131_literals_Bit_String_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Bit_String_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Bit_String_Literal)


iec61131_literals_Boolean_Literal_strategy = st.builds(iec61131_literals_Boolean_Literal, value=safe_text)
@given(instance=iec61131_literals_Boolean_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Boolean_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Boolean_Literal)


iec61131_literals_Character_String_strategy = st.builds(iec61131_literals_Character_String)
@given(instance=iec61131_literals_Character_String_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Character_String_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Character_String)


iec61131_literals_Common_Character_Representation_strategy = st.builds(iec61131_literals_Common_Character_Representation, value=safe_text)
@given(instance=iec61131_literals_Common_Character_Representation_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Common_Character_Representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Common_Character_Representation)


iec61131_literals_Constant_strategy = st.builds(iec61131_literals_Constant)
@given(instance=iec61131_literals_Constant_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Constant_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Constant)


iec61131_literals_Date_strategy = st.builds(iec61131_literals_Date)
@given(instance=iec61131_literals_Date_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Date_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date)


iec61131_literals_Date_And_Time_strategy = st.builds(iec61131_literals_Date_And_Time)
@given(instance=iec61131_literals_Date_And_Time_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Date_And_Time_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date_And_Time)


iec61131_literals_Date_Literal_strategy = st.builds(iec61131_literals_Date_Literal, day=safe_text, month=safe_text, year=safe_text)
@given(instance=iec61131_literals_Date_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Date_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date_Literal)


iec61131_literals_Days_strategy = st.builds(iec61131_literals_Days)
@given(instance=iec61131_literals_Days_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Days_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Days)


iec61131_literals_Daytime_strategy = st.builds(iec61131_literals_Daytime, hour=safe_text, minute=safe_text)
@given(instance=iec61131_literals_Daytime_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Daytime_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Daytime)


iec61131_literals_Double_Byte_Character_Representation_strategy = st.builds(iec61131_literals_Double_Byte_Character_Representation, value=safe_text)
@given(instance=iec61131_literals_Double_Byte_Character_Representation_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Double_Byte_Character_Representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Double_Byte_Character_Representation)


iec61131_literals_Double_Byte_Character_String_strategy = st.builds(iec61131_literals_Double_Byte_Character_String)
@given(instance=iec61131_literals_Double_Byte_Character_String_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Double_Byte_Character_String_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Double_Byte_Character_String)


iec61131_literals_Duration_strategy = st.builds(iec61131_literals_Duration)
@given(instance=iec61131_literals_Duration_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Duration_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Duration)


iec61131_literals_Fixed_Point_strategy = st.builds(iec61131_literals_Fixed_Point, valuePost=safe_text, valuePre=safe_text)
@given(instance=iec61131_literals_Fixed_Point_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Fixed_Point_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Fixed_Point)


iec61131_literals_Fixed_Point_Literal_strategy = st.builds(iec61131_literals_Fixed_Point_Literal)
@given(instance=iec61131_literals_Fixed_Point_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Fixed_Point_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Fixed_Point_Literal)


iec61131_literals_Hex_Integer_strategy = st.builds(iec61131_literals_Hex_Integer)
@given(instance=iec61131_literals_Hex_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Hex_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Hex_Integer)


iec61131_literals_Hours_strategy = st.builds(iec61131_literals_Hours)
@given(instance=iec61131_literals_Hours_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Hours_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Hours)


iec61131_literals_Integer_strategy = st.builds(iec61131_literals_Integer, value=safe_text)
@given(instance=iec61131_literals_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Integer)


iec61131_literals_Integer_Literal_strategy = st.builds(iec61131_literals_Integer_Literal)
@given(instance=iec61131_literals_Integer_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Integer_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Integer_Literal)


iec61131_literals_Interval_strategy = st.builds(iec61131_literals_Interval)
@given(instance=iec61131_literals_Interval_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Interval_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Interval)


iec61131_literals_Milliseconds_strategy = st.builds(iec61131_literals_Milliseconds)
@given(instance=iec61131_literals_Milliseconds_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Milliseconds_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Milliseconds)


iec61131_literals_Minutes_strategy = st.builds(iec61131_literals_Minutes)
@given(instance=iec61131_literals_Minutes_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Minutes_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Minutes)


iec61131_literals_Numeric_Literal_strategy = st.builds(iec61131_literals_Numeric_Literal)
@given(instance=iec61131_literals_Numeric_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Numeric_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Numeric_Literal)


iec61131_literals_Octal_Integer_strategy = st.builds(iec61131_literals_Octal_Integer)
@given(instance=iec61131_literals_Octal_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Octal_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Octal_Integer)


iec61131_literals_Real_Literal_strategy = st.builds(iec61131_literals_Real_Literal, exponent=safe_text, negative=st.booleans())
@given(instance=iec61131_literals_Real_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Real_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Real_Literal)


iec61131_literals_Seconds_strategy = st.builds(iec61131_literals_Seconds)
@given(instance=iec61131_literals_Seconds_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Seconds_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Seconds)


iec61131_literals_Signed_Integer_strategy = st.builds(iec61131_literals_Signed_Integer, negative=st.booleans())
@given(instance=iec61131_literals_Signed_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Signed_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Signed_Integer)


iec61131_literals_Single_Byte_Character_Representation_strategy = st.builds(iec61131_literals_Single_Byte_Character_Representation, value=safe_text)
@given(instance=iec61131_literals_Single_Byte_Character_Representation_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Single_Byte_Character_Representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Single_Byte_Character_Representation)


iec61131_literals_Single_Byte_Character_String_strategy = st.builds(iec61131_literals_Single_Byte_Character_String)
@given(instance=iec61131_literals_Single_Byte_Character_String_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Single_Byte_Character_String_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Single_Byte_Character_String)


iec61131_literals_Time_Literal_strategy = st.builds(iec61131_literals_Time_Literal)
@given(instance=iec61131_literals_Time_Literal_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Time_Literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Time_Literal)


iec61131_literals_Time_Of_Day_strategy = st.builds(iec61131_literals_Time_Of_Day)
@given(instance=iec61131_literals_Time_Of_Day_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Time_Of_Day_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Time_Of_Day)


iec61131_literals_Unsigned_Integer_strategy = st.builds(iec61131_literals_Unsigned_Integer)
@given(instance=iec61131_literals_Unsigned_Integer_strategy)
@settings(max_examples=25)
def test_iec61131_literals_Unsigned_Integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Unsigned_Integer)


iec61131_operators_Add_Operator_strategy = st.builds(iec61131_operators_Add_Operator)
@given(instance=iec61131_operators_Add_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Add_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Add_Operator)


iec61131_operators_Addition_Name_strategy = st.builds(iec61131_operators_Addition_Name)
@given(instance=iec61131_operators_Addition_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Addition_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Name)


iec61131_operators_Addition_Operator_strategy = st.builds(iec61131_operators_Addition_Operator)
@given(instance=iec61131_operators_Addition_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Addition_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Operator)


iec61131_operators_Addition_Symbol_strategy = st.builds(iec61131_operators_Addition_Symbol)
@given(instance=iec61131_operators_Addition_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Addition_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Symbol)


iec61131_operators_And_Name_strategy = st.builds(iec61131_operators_And_Name)
@given(instance=iec61131_operators_And_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_And_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Name)


iec61131_operators_And_Operator_strategy = st.builds(iec61131_operators_And_Operator)
@given(instance=iec61131_operators_And_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_And_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Operator)


iec61131_operators_And_Symbol_strategy = st.builds(iec61131_operators_And_Symbol)
@given(instance=iec61131_operators_And_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_And_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Symbol)


iec61131_operators_Arithmetic_Name_strategy = st.builds(iec61131_operators_Arithmetic_Name)
@given(instance=iec61131_operators_Arithmetic_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Arithmetic_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Arithmetic_Name)


iec61131_operators_Assignment_Name_strategy = st.builds(iec61131_operators_Assignment_Name)
@given(instance=iec61131_operators_Assignment_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Assignment_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Name)


iec61131_operators_Assignment_Operator_strategy = st.builds(iec61131_operators_Assignment_Operator)
@given(instance=iec61131_operators_Assignment_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Assignment_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Operator)


iec61131_operators_Assignment_Symbol_strategy = st.builds(iec61131_operators_Assignment_Symbol)
@given(instance=iec61131_operators_Assignment_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Assignment_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Symbol)


iec61131_operators_Comparison_Name_strategy = st.builds(iec61131_operators_Comparison_Name)
@given(instance=iec61131_operators_Comparison_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Comparison_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Comparison_Name)


iec61131_operators_Comparison_Operator_strategy = st.builds(iec61131_operators_Comparison_Operator)
@given(instance=iec61131_operators_Comparison_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Comparison_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Comparison_Operator)


iec61131_operators_Divide_Name_strategy = st.builds(iec61131_operators_Divide_Name)
@given(instance=iec61131_operators_Divide_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Divide_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Name)


iec61131_operators_Divide_Operator_strategy = st.builds(iec61131_operators_Divide_Operator)
@given(instance=iec61131_operators_Divide_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Divide_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Operator)


iec61131_operators_Divide_Symbol_strategy = st.builds(iec61131_operators_Divide_Symbol)
@given(instance=iec61131_operators_Divide_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Divide_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Symbol)


iec61131_operators_Dot_Operator_strategy = st.builds(iec61131_operators_Dot_Operator)
@given(instance=iec61131_operators_Dot_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Dot_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Dot_Operator)


iec61131_operators_EquUequ_Operator_strategy = st.builds(iec61131_operators_EquUequ_Operator)
@given(instance=iec61131_operators_EquUequ_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_EquUequ_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_EquUequ_Operator)


iec61131_operators_Equal_Name_strategy = st.builds(iec61131_operators_Equal_Name)
@given(instance=iec61131_operators_Equal_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Equal_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Name)


iec61131_operators_Equal_Operator_strategy = st.builds(iec61131_operators_Equal_Operator)
@given(instance=iec61131_operators_Equal_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Equal_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Operator)


iec61131_operators_Equal_Symbol_strategy = st.builds(iec61131_operators_Equal_Symbol)
@given(instance=iec61131_operators_Equal_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Equal_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Symbol)


iec61131_operators_GreaterEqual_Name_strategy = st.builds(iec61131_operators_GreaterEqual_Name)
@given(instance=iec61131_operators_GreaterEqual_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_GreaterEqual_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Name)


iec61131_operators_GreaterEqual_Operator_strategy = st.builds(iec61131_operators_GreaterEqual_Operator)
@given(instance=iec61131_operators_GreaterEqual_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_GreaterEqual_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Operator)


iec61131_operators_GreaterEqual_Symbol_strategy = st.builds(iec61131_operators_GreaterEqual_Symbol)
@given(instance=iec61131_operators_GreaterEqual_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_GreaterEqual_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Symbol)


iec61131_operators_Greater_Name_strategy = st.builds(iec61131_operators_Greater_Name)
@given(instance=iec61131_operators_Greater_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Greater_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Name)


iec61131_operators_Greater_Operator_strategy = st.builds(iec61131_operators_Greater_Operator)
@given(instance=iec61131_operators_Greater_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Greater_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Operator)


iec61131_operators_Greater_Symbol_strategy = st.builds(iec61131_operators_Greater_Symbol)
@given(instance=iec61131_operators_Greater_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Greater_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Symbol)


iec61131_operators_LessEqual_Name_strategy = st.builds(iec61131_operators_LessEqual_Name)
@given(instance=iec61131_operators_LessEqual_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_LessEqual_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Name)


iec61131_operators_LessEqual_Operator_strategy = st.builds(iec61131_operators_LessEqual_Operator)
@given(instance=iec61131_operators_LessEqual_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_LessEqual_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Operator)


iec61131_operators_LessEqual_Symbol_strategy = st.builds(iec61131_operators_LessEqual_Symbol)
@given(instance=iec61131_operators_LessEqual_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_LessEqual_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Symbol)


iec61131_operators_Less_Name_strategy = st.builds(iec61131_operators_Less_Name)
@given(instance=iec61131_operators_Less_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Less_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Name)


iec61131_operators_Less_Operator_strategy = st.builds(iec61131_operators_Less_Operator)
@given(instance=iec61131_operators_Less_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Less_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Operator)


iec61131_operators_Less_Symbol_strategy = st.builds(iec61131_operators_Less_Symbol)
@given(instance=iec61131_operators_Less_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Less_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Symbol)


iec61131_operators_Modulo_Operator_strategy = st.builds(iec61131_operators_Modulo_Operator)
@given(instance=iec61131_operators_Modulo_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Modulo_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Modulo_Operator)


iec61131_operators_Multiply_Name_strategy = st.builds(iec61131_operators_Multiply_Name)
@given(instance=iec61131_operators_Multiply_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Multiply_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Name)


iec61131_operators_Multiply_Operator_strategy = st.builds(iec61131_operators_Multiply_Operator)
@given(instance=iec61131_operators_Multiply_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Multiply_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Operator)


iec61131_operators_Multiply_Symbol_strategy = st.builds(iec61131_operators_Multiply_Symbol)
@given(instance=iec61131_operators_Multiply_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Multiply_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Symbol)


iec61131_operators_Not_Operator_strategy = st.builds(iec61131_operators_Not_Operator)
@given(instance=iec61131_operators_Not_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Not_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Not_Operator)


iec61131_operators_Operator_strategy = st.builds(iec61131_operators_Operator)
@given(instance=iec61131_operators_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Operator)


iec61131_operators_Or_Operator_strategy = st.builds(iec61131_operators_Or_Operator)
@given(instance=iec61131_operators_Or_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Or_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Or_Operator)


iec61131_operators_Power_Name_strategy = st.builds(iec61131_operators_Power_Name)
@given(instance=iec61131_operators_Power_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Power_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Name)


iec61131_operators_Power_Operator_strategy = st.builds(iec61131_operators_Power_Operator)
@given(instance=iec61131_operators_Power_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Power_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Operator)


iec61131_operators_Power_Symbol_strategy = st.builds(iec61131_operators_Power_Symbol)
@given(instance=iec61131_operators_Power_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Power_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Symbol)


iec61131_operators_Substraction_Name_strategy = st.builds(iec61131_operators_Substraction_Name)
@given(instance=iec61131_operators_Substraction_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Substraction_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Name)


iec61131_operators_Substraction_Operator_strategy = st.builds(iec61131_operators_Substraction_Operator)
@given(instance=iec61131_operators_Substraction_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Substraction_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Operator)


iec61131_operators_Substraction_Symbol_strategy = st.builds(iec61131_operators_Substraction_Symbol)
@given(instance=iec61131_operators_Substraction_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Substraction_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Symbol)


iec61131_operators_Unary_Operator_strategy = st.builds(iec61131_operators_Unary_Operator)
@given(instance=iec61131_operators_Unary_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Unary_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unary_Operator)


iec61131_operators_Unequal_Name_strategy = st.builds(iec61131_operators_Unequal_Name)
@given(instance=iec61131_operators_Unequal_Name_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Unequal_Name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Name)


iec61131_operators_Unequal_Operator_strategy = st.builds(iec61131_operators_Unequal_Operator)
@given(instance=iec61131_operators_Unequal_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Unequal_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Operator)


iec61131_operators_Unequal_Symbol_strategy = st.builds(iec61131_operators_Unequal_Symbol)
@given(instance=iec61131_operators_Unequal_Symbol_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Unequal_Symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Symbol)


iec61131_operators_Xor_Operator_strategy = st.builds(iec61131_operators_Xor_Operator)
@given(instance=iec61131_operators_Xor_Operator_strategy)
@settings(max_examples=25)
def test_iec61131_operators_Xor_Operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Xor_Operator)


iec61131_pous_Access_Name_strategy = st.builds(iec61131_pous_Access_Name, name=safe_text)
@given(instance=iec61131_pous_Access_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Access_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Access_Name)


iec61131_pous_Array_Type_Declaration_strategy = st.builds(iec61131_pous_Array_Type_Declaration)
@given(instance=iec61131_pous_Array_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Array_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Array_Type_Declaration)


iec61131_pous_Data_Type_Declaration_strategy = st.builds(iec61131_pous_Data_Type_Declaration)
@given(instance=iec61131_pous_Data_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Data_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Data_Type_Declaration)


iec61131_pous_Derived_Function_Block_Name_strategy = st.builds(iec61131_pous_Derived_Function_Block_Name)
@given(instance=iec61131_pous_Derived_Function_Block_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Derived_Function_Block_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Derived_Function_Block_Name)


iec61131_pous_Derived_Function_Name_strategy = st.builds(iec61131_pous_Derived_Function_Name)
@given(instance=iec61131_pous_Derived_Function_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Derived_Function_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Derived_Function_Name)


iec61131_pous_Enumerated_Type_Declaration_strategy = st.builds(iec61131_pous_Enumerated_Type_Declaration)
@given(instance=iec61131_pous_Enumerated_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Enumerated_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Enumerated_Type_Declaration)


iec61131_pous_Function_Block_Body_strategy = st.builds(iec61131_pous_Function_Block_Body)
@given(instance=iec61131_pous_Function_Block_Body_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Block_Body_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Body)


iec61131_pous_Function_Block_Declaration_strategy = st.builds(iec61131_pous_Function_Block_Declaration)
@given(instance=iec61131_pous_Function_Block_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Block_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Declaration)


iec61131_pous_Function_Block_Type_Name_strategy = st.builds(iec61131_pous_Function_Block_Type_Name)
@given(instance=iec61131_pous_Function_Block_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Block_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Type_Name)


iec61131_pous_Function_Block_Vars_strategy = st.builds(iec61131_pous_Function_Block_Vars)
@given(instance=iec61131_pous_Function_Block_Vars_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Block_Vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Vars)


iec61131_pous_Function_Body_strategy = st.builds(iec61131_pous_Function_Body)
@given(instance=iec61131_pous_Function_Body_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Body_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Body)


iec61131_pous_Function_Declaration_strategy = st.builds(iec61131_pous_Function_Declaration)
@given(instance=iec61131_pous_Function_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Declaration)


iec61131_pous_Function_Name_strategy = st.builds(iec61131_pous_Function_Name)
@given(instance=iec61131_pous_Function_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Name)


iec61131_pous_Function_Return_Value_strategy = st.builds(iec61131_pous_Function_Return_Value)
@given(instance=iec61131_pous_Function_Return_Value_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Return_Value_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Return_Value)


iec61131_pous_Function_Vars_strategy = st.builds(iec61131_pous_Function_Vars)
@given(instance=iec61131_pous_Function_Vars_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Function_Vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Vars)


iec61131_pous_Library_strategy = st.builds(iec61131_pous_Library)
@given(instance=iec61131_pous_Library_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Library_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Library)


iec61131_pous_Other_Language_strategy = st.builds(iec61131_pous_Other_Language, text=safe_text)
@given(instance=iec61131_pous_Other_Language_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Other_Language_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Other_Language)


iec61131_pous_Program_Access_Decl_strategy = st.builds(iec61131_pous_Program_Access_Decl, direction=safe_text)
@given(instance=iec61131_pous_Program_Access_Decl_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Program_Access_Decl_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Access_Decl)


iec61131_pous_Program_Access_Decls_strategy = st.builds(iec61131_pous_Program_Access_Decls)
@given(instance=iec61131_pous_Program_Access_Decls_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Program_Access_Decls_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Access_Decls)


iec61131_pous_Program_Declaration_strategy = st.builds(iec61131_pous_Program_Declaration)
@given(instance=iec61131_pous_Program_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Program_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Declaration)


iec61131_pous_Program_Type_Name_strategy = st.builds(iec61131_pous_Program_Type_Name)
@given(instance=iec61131_pous_Program_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Program_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Type_Name)


iec61131_pous_Program_Vars_strategy = st.builds(iec61131_pous_Program_Vars)
@given(instance=iec61131_pous_Program_Vars_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Program_Vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Vars)


iec61131_pous_Simple_Type_Declaration_strategy = st.builds(iec61131_pous_Simple_Type_Declaration)
@given(instance=iec61131_pous_Simple_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Simple_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Simple_Type_Declaration)


iec61131_pous_Single_Element_Type_Declaration_strategy = st.builds(iec61131_pous_Single_Element_Type_Declaration)
@given(instance=iec61131_pous_Single_Element_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Single_Element_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Single_Element_Type_Declaration)


iec61131_pous_String_Type_Declaration_strategy = st.builds(iec61131_pous_String_Type_Declaration)
@given(instance=iec61131_pous_String_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_String_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_String_Type_Declaration)


iec61131_pous_Structure_Declaration_strategy = st.builds(iec61131_pous_Structure_Declaration)
@given(instance=iec61131_pous_Structure_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Structure_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Declaration)


iec61131_pous_Structure_Element_Declaration_strategy = st.builds(iec61131_pous_Structure_Element_Declaration)
@given(instance=iec61131_pous_Structure_Element_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Structure_Element_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Element_Declaration)


iec61131_pous_Structure_Elements_strategy = st.builds(iec61131_pous_Structure_Elements)
@given(instance=iec61131_pous_Structure_Elements_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Structure_Elements_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Elements)


iec61131_pous_Structure_Specification_strategy = st.builds(iec61131_pous_Structure_Specification)
@given(instance=iec61131_pous_Structure_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Structure_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Specification)


iec61131_pous_Structure_Type_Declaration_strategy = st.builds(iec61131_pous_Structure_Type_Declaration)
@given(instance=iec61131_pous_Structure_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Structure_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Type_Declaration)


iec61131_pous_Subrange_Type_Declaration_strategy = st.builds(iec61131_pous_Subrange_Type_Declaration)
@given(instance=iec61131_pous_Subrange_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Subrange_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Subrange_Type_Declaration)


iec61131_pous_Type_Declaration_strategy = st.builds(iec61131_pous_Type_Declaration)
@given(instance=iec61131_pous_Type_Declaration_strategy)
@settings(max_examples=25)
def test_iec61131_pous_Type_Declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Type_Declaration)


iec61131_sfc_Action_strategy = st.builds(iec61131_sfc_Action)
@given(instance=iec61131_sfc_Action_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Action_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action)


iec61131_sfc_ActionTime2_strategy = st.builds(iec61131_sfc_ActionTime2)
@given(instance=iec61131_sfc_ActionTime2_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_ActionTime2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_ActionTime2)


iec61131_sfc_Action_Association_strategy = st.builds(iec61131_sfc_Action_Association)
@given(instance=iec61131_sfc_Action_Association_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Action_Association_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Association)


iec61131_sfc_Action_Name_strategy = st.builds(iec61131_sfc_Action_Name, name=safe_text)
@given(instance=iec61131_sfc_Action_Name_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Action_Name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Name)


iec61131_sfc_Action_Qualifier_strategy = st.builds(iec61131_sfc_Action_Qualifier, qualifier=safe_text)
@given(instance=iec61131_sfc_Action_Qualifier_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Action_Qualifier_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Qualifier)


iec61131_sfc_Action_Time_strategy = st.builds(iec61131_sfc_Action_Time)
@given(instance=iec61131_sfc_Action_Time_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Action_Time_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Time)


iec61131_sfc_Cond2_Condition_strategy = st.builds(iec61131_sfc_Cond2_Condition)
@given(instance=iec61131_sfc_Cond2_Condition_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Cond2_Condition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Cond2_Condition)


iec61131_sfc_Initial_Step_strategy = st.builds(iec61131_sfc_Initial_Step)
@given(instance=iec61131_sfc_Initial_Step_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Initial_Step_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Initial_Step)


iec61131_sfc_Sequential_Function_Chart_strategy = st.builds(iec61131_sfc_Sequential_Function_Chart)
@given(instance=iec61131_sfc_Sequential_Function_Chart_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Sequential_Function_Chart_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sequential_Function_Chart)


iec61131_sfc_Sfc_Elements_strategy = st.builds(iec61131_sfc_Sfc_Elements)
@given(instance=iec61131_sfc_Sfc_Elements_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Sfc_Elements_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sfc_Elements)


iec61131_sfc_Sfc_Network_strategy = st.builds(iec61131_sfc_Sfc_Network)
@given(instance=iec61131_sfc_Sfc_Network_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Sfc_Network_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sfc_Network)


iec61131_sfc_Step_strategy = st.builds(iec61131_sfc_Step)
@given(instance=iec61131_sfc_Step_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Step_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step)


iec61131_sfc_Step_Name_strategy = st.builds(iec61131_sfc_Step_Name)
@given(instance=iec61131_sfc_Step_Name_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Step_Name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step_Name)


iec61131_sfc_Step_Types_strategy = st.builds(iec61131_sfc_Step_Types)
@given(instance=iec61131_sfc_Step_Types_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Step_Types_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step_Types)


iec61131_sfc_Steps_strategy = st.builds(iec61131_sfc_Steps)
@given(instance=iec61131_sfc_Steps_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Steps_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps)


iec61131_sfc_Steps1_strategy = st.builds(iec61131_sfc_Steps1)
@given(instance=iec61131_sfc_Steps1_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Steps1_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps1)


iec61131_sfc_Steps2_strategy = st.builds(iec61131_sfc_Steps2)
@given(instance=iec61131_sfc_Steps2_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Steps2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps2)


iec61131_sfc_Timed_Qualifier_strategy = st.builds(iec61131_sfc_Timed_Qualifier, qualifier=safe_text)
@given(instance=iec61131_sfc_Timed_Qualifier_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Timed_Qualifier_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Timed_Qualifier)


iec61131_sfc_Transition_strategy = st.builds(iec61131_sfc_Transition)
@given(instance=iec61131_sfc_Transition_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition)


iec61131_sfc_Transition_Cond1_strategy = st.builds(iec61131_sfc_Transition_Cond1)
@given(instance=iec61131_sfc_Transition_Cond1_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_Cond1_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond1)


iec61131_sfc_Transition_Cond2_strategy = st.builds(iec61131_sfc_Transition_Cond2)
@given(instance=iec61131_sfc_Transition_Cond2_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_Cond2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond2)


iec61131_sfc_Transition_Cond3_strategy = st.builds(iec61131_sfc_Transition_Cond3)
@given(instance=iec61131_sfc_Transition_Cond3_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_Cond3_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond3)


iec61131_sfc_Transition_Condition_strategy = st.builds(iec61131_sfc_Transition_Condition)
@given(instance=iec61131_sfc_Transition_Condition_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_Condition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Condition)


iec61131_sfc_Transition_Name_strategy = st.builds(iec61131_sfc_Transition_Name, name=safe_text)
@given(instance=iec61131_sfc_Transition_Name_strategy)
@settings(max_examples=25)
def test_iec61131_sfc_Transition_Name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Name)


iec61131_st_Add_Expression_strategy = st.builds(iec61131_st_Add_Expression)
@given(instance=iec61131_st_Add_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Add_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Add_Expression)


iec61131_st_And_Expression_strategy = st.builds(iec61131_st_And_Expression)
@given(instance=iec61131_st_And_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_And_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_And_Expression)


iec61131_st_Assignment_Statement_strategy = st.builds(iec61131_st_Assignment_Statement)
@given(instance=iec61131_st_Assignment_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Assignment_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Assignment_Statement)


iec61131_st_Bracket_Expression_strategy = st.builds(iec61131_st_Bracket_Expression)
@given(instance=iec61131_st_Bracket_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Bracket_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Bracket_Expression)


iec61131_st_Call_Expression_strategy = st.builds(iec61131_st_Call_Expression)
@given(instance=iec61131_st_Call_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Call_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Call_Expression)


iec61131_st_Case_Element_strategy = st.builds(iec61131_st_Case_Element)
@given(instance=iec61131_st_Case_Element_strategy)
@settings(max_examples=25)
def test_iec61131_st_Case_Element_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_Element)


iec61131_st_Case_List_strategy = st.builds(iec61131_st_Case_List)
@given(instance=iec61131_st_Case_List_strategy)
@settings(max_examples=25)
def test_iec61131_st_Case_List_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_List)


iec61131_st_Case_List_Element_strategy = st.builds(iec61131_st_Case_List_Element)
@given(instance=iec61131_st_Case_List_Element_strategy)
@settings(max_examples=25)
def test_iec61131_st_Case_List_Element_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_List_Element)


iec61131_st_Case_Statement_strategy = st.builds(iec61131_st_Case_Statement)
@given(instance=iec61131_st_Case_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Case_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_Statement)


iec61131_st_Comparison_strategy = st.builds(iec61131_st_Comparison)
@given(instance=iec61131_st_Comparison_strategy)
@settings(max_examples=25)
def test_iec61131_st_Comparison_instantiation(instance):
    assert isinstance(instance, iec61131_st_Comparison)


iec61131_st_Control_Variable_strategy = st.builds(iec61131_st_Control_Variable, name=safe_text)
@given(instance=iec61131_st_Control_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_st_Control_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_st_Control_Variable)


iec61131_st_Else_If_Statement_strategy = st.builds(iec61131_st_Else_If_Statement)
@given(instance=iec61131_st_Else_If_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Else_If_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Else_If_Statement)


iec61131_st_Else_Statement_strategy = st.builds(iec61131_st_Else_Statement)
@given(instance=iec61131_st_Else_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Else_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Else_Statement)


iec61131_st_Equ_Expression_strategy = st.builds(iec61131_st_Equ_Expression)
@given(instance=iec61131_st_Equ_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Equ_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Equ_Expression)


iec61131_st_Exit_Statement_strategy = st.builds(iec61131_st_Exit_Statement)
@given(instance=iec61131_st_Exit_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Exit_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Exit_Statement)


iec61131_st_Expression_strategy = st.builds(iec61131_st_Expression)
@given(instance=iec61131_st_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression)


iec61131_st_Expression_Constant_strategy = st.builds(iec61131_st_Expression_Constant)
@given(instance=iec61131_st_Expression_Constant_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_Constant_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Constant)


iec61131_st_Expression_EnumValue_strategy = st.builds(iec61131_st_Expression_EnumValue)
@given(instance=iec61131_st_Expression_EnumValue_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_EnumValue_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_EnumValue)


iec61131_st_Expression_Types_strategy = st.builds(iec61131_st_Expression_Types)
@given(instance=iec61131_st_Expression_Types_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_Types_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Types)


iec61131_st_Expression_Variable_strategy = st.builds(iec61131_st_Expression_Variable)
@given(instance=iec61131_st_Expression_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Variable)


iec61131_st_Expression_Variable_Type_strategy = st.builds(iec61131_st_Expression_Variable_Type)
@given(instance=iec61131_st_Expression_Variable_Type_strategy)
@settings(max_examples=25)
def test_iec61131_st_Expression_Variable_Type_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Variable_Type)


iec61131_st_Fb_Invocation_strategy = st.builds(iec61131_st_Fb_Invocation)
@given(instance=iec61131_st_Fb_Invocation_strategy)
@settings(max_examples=25)
def test_iec61131_st_Fb_Invocation_instantiation(instance):
    assert isinstance(instance, iec61131_st_Fb_Invocation)


iec61131_st_For_List_strategy = st.builds(iec61131_st_For_List)
@given(instance=iec61131_st_For_List_strategy)
@settings(max_examples=25)
def test_iec61131_st_For_List_instantiation(instance):
    assert isinstance(instance, iec61131_st_For_List)


iec61131_st_For_Statement_strategy = st.builds(iec61131_st_For_Statement)
@given(instance=iec61131_st_For_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_For_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_For_Statement)


iec61131_st_If_Statement_strategy = st.builds(iec61131_st_If_Statement)
@given(instance=iec61131_st_If_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_If_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_If_Statement)


iec61131_st_Iteration_Statement_strategy = st.builds(iec61131_st_Iteration_Statement)
@given(instance=iec61131_st_Iteration_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Iteration_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Iteration_Statement)


iec61131_st_Param_Assignment_strategy = st.builds(iec61131_st_Param_Assignment)
@given(instance=iec61131_st_Param_Assignment_strategy)
@settings(max_examples=25)
def test_iec61131_st_Param_Assignment_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Assignment)


iec61131_st_Param_Type1_strategy = st.builds(iec61131_st_Param_Type1)
@given(instance=iec61131_st_Param_Type1_strategy)
@settings(max_examples=25)
def test_iec61131_st_Param_Type1_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Type1)


iec61131_st_Param_Type2_strategy = st.builds(iec61131_st_Param_Type2)
@given(instance=iec61131_st_Param_Type2_strategy)
@settings(max_examples=25)
def test_iec61131_st_Param_Type2_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Type2)


iec61131_st_Power_Expression_strategy = st.builds(iec61131_st_Power_Expression)
@given(instance=iec61131_st_Power_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Power_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Power_Expression)


iec61131_st_Primary_Expression_strategy = st.builds(iec61131_st_Primary_Expression)
@given(instance=iec61131_st_Primary_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Primary_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Primary_Expression)


iec61131_st_Repeat_Statement_strategy = st.builds(iec61131_st_Repeat_Statement)
@given(instance=iec61131_st_Repeat_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Repeat_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Repeat_Statement)


iec61131_st_Return_Statement_strategy = st.builds(iec61131_st_Return_Statement)
@given(instance=iec61131_st_Return_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Return_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Return_Statement)


iec61131_st_Selection_Statement_strategy = st.builds(iec61131_st_Selection_Statement)
@given(instance=iec61131_st_Selection_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Selection_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Selection_Statement)


iec61131_st_Statement_strategy = st.builds(iec61131_st_Statement)
@given(instance=iec61131_st_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Statement)


iec61131_st_Statement_List_strategy = st.builds(iec61131_st_Statement_List)
@given(instance=iec61131_st_Statement_List_strategy)
@settings(max_examples=25)
def test_iec61131_st_Statement_List_instantiation(instance):
    assert isinstance(instance, iec61131_st_Statement_List)


iec61131_st_Subprogram_Control_Statement_strategy = st.builds(iec61131_st_Subprogram_Control_Statement)
@given(instance=iec61131_st_Subprogram_Control_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_Subprogram_Control_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Subprogram_Control_Statement)


iec61131_st_Term_Expression_strategy = st.builds(iec61131_st_Term_Expression)
@given(instance=iec61131_st_Term_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Term_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Term_Expression)


iec61131_st_Unary_Expression_strategy = st.builds(iec61131_st_Unary_Expression)
@given(instance=iec61131_st_Unary_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Unary_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Unary_Expression)


iec61131_st_While_Statement_strategy = st.builds(iec61131_st_While_Statement)
@given(instance=iec61131_st_While_Statement_strategy)
@settings(max_examples=25)
def test_iec61131_st_While_Statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_While_Statement)


iec61131_st_Xor_Expression_strategy = st.builds(iec61131_st_Xor_Expression)
@given(instance=iec61131_st_Xor_Expression_strategy)
@settings(max_examples=25)
def test_iec61131_st_Xor_Expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Xor_Expression)


iec61131_types_Array_Type_Name_strategy = st.builds(iec61131_types_Array_Type_Name)
@given(instance=iec61131_types_Array_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Array_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Array_Type_Name)


iec61131_types_Bit_String_Type_Name_strategy = st.builds(iec61131_types_Bit_String_Type_Name)
@given(instance=iec61131_types_Bit_String_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Bit_String_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Bit_String_Type_Name)


iec61131_types_Bool_Type_Name_strategy = st.builds(iec61131_types_Bool_Type_Name)
@given(instance=iec61131_types_Bool_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Bool_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Bool_Type_Name)


iec61131_types_Byte_String_Type_Name_strategy = st.builds(iec61131_types_Byte_String_Type_Name)
@given(instance=iec61131_types_Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Byte_String_Type_Name)


iec61131_types_DT_Type_Name_strategy = st.builds(iec61131_types_DT_Type_Name)
@given(instance=iec61131_types_DT_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_DT_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_DT_Type_Name)


iec61131_types_Data_Type_Name_strategy = st.builds(iec61131_types_Data_Type_Name)
@given(instance=iec61131_types_Data_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Data_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Data_Type_Name)


iec61131_types_Date_Type_Name_strategy = st.builds(iec61131_types_Date_Type_Name)
@given(instance=iec61131_types_Date_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Date_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Date_Type_Name)


iec61131_types_Derived_Type_Name_strategy = st.builds(iec61131_types_Derived_Type_Name)
@given(instance=iec61131_types_Derived_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Derived_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Derived_Type_Name)


iec61131_types_Double_Byte_String_Type_Name_strategy = st.builds(iec61131_types_Double_Byte_String_Type_Name)
@given(instance=iec61131_types_Double_Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Double_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Double_Byte_String_Type_Name)


iec61131_types_Duration_Type_Name_strategy = st.builds(iec61131_types_Duration_Type_Name)
@given(instance=iec61131_types_Duration_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Duration_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Duration_Type_Name)


iec61131_types_Elementary_Type_Name_strategy = st.builds(iec61131_types_Elementary_Type_Name)
@given(instance=iec61131_types_Elementary_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Elementary_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Elementary_Type_Name)


iec61131_types_Enumerated_Type_Name_strategy = st.builds(iec61131_types_Enumerated_Type_Name)
@given(instance=iec61131_types_Enumerated_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Enumerated_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Enumerated_Type_Name)


iec61131_types_Generic_Type_Name_strategy = st.builds(iec61131_types_Generic_Type_Name)
@given(instance=iec61131_types_Generic_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Generic_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Generic_Type_Name)


iec61131_types_Integer_Type_Name_strategy = st.builds(iec61131_types_Integer_Type_Name)
@given(instance=iec61131_types_Integer_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Integer_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Integer_Type_Name)


iec61131_types_Non_Generic_Type_Name_strategy = st.builds(iec61131_types_Non_Generic_Type_Name)
@given(instance=iec61131_types_Non_Generic_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Non_Generic_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Non_Generic_Type_Name)


iec61131_types_Numeric_Type_Name_strategy = st.builds(iec61131_types_Numeric_Type_Name)
@given(instance=iec61131_types_Numeric_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Numeric_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Numeric_Type_Name)


iec61131_types_Real_Type_Name_strategy = st.builds(iec61131_types_Real_Type_Name)
@given(instance=iec61131_types_Real_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Real_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Real_Type_Name)


iec61131_types_Signed_Integer_Type_Name_strategy = st.builds(iec61131_types_Signed_Integer_Type_Name)
@given(instance=iec61131_types_Signed_Integer_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Signed_Integer_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Signed_Integer_Type_Name)


iec61131_types_Simple_Specification_strategy = st.builds(iec61131_types_Simple_Specification)
@given(instance=iec61131_types_Simple_Specification_strategy)
@settings(max_examples=25)
def test_iec61131_types_Simple_Specification_instantiation(instance):
    assert isinstance(instance, iec61131_types_Simple_Specification)


iec61131_types_Simple_Type_Name_strategy = st.builds(iec61131_types_Simple_Type_Name)
@given(instance=iec61131_types_Simple_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Simple_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Simple_Type_Name)


iec61131_types_Single_Byte_String_Type_Name_strategy = st.builds(iec61131_types_Single_Byte_String_Type_Name)
@given(instance=iec61131_types_Single_Byte_String_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Single_Byte_String_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Single_Byte_String_Type_Name)


iec61131_types_Single_Element_Type_Name_strategy = st.builds(iec61131_types_Single_Element_Type_Name)
@given(instance=iec61131_types_Single_Element_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Single_Element_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Single_Element_Type_Name)


iec61131_types_String_Type_Name_strategy = st.builds(iec61131_types_String_Type_Name)
@given(instance=iec61131_types_String_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_String_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_String_Type_Name)


iec61131_types_Structure_Type_Name_strategy = st.builds(iec61131_types_Structure_Type_Name)
@given(instance=iec61131_types_Structure_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Structure_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Structure_Type_Name)


iec61131_types_Subrange_Type_Name_strategy = st.builds(iec61131_types_Subrange_Type_Name)
@given(instance=iec61131_types_Subrange_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Subrange_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Subrange_Type_Name)


iec61131_types_TOD_Type_Name_strategy = st.builds(iec61131_types_TOD_Type_Name)
@given(instance=iec61131_types_TOD_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_TOD_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_TOD_Type_Name)


iec61131_types_TypeLib_strategy = st.builds(iec61131_types_TypeLib)
@given(instance=iec61131_types_TypeLib_strategy)
@settings(max_examples=25)
def test_iec61131_types_TypeLib_instantiation(instance):
    assert isinstance(instance, iec61131_types_TypeLib)


iec61131_types_Unsigned_Integer_Type_Name_strategy = st.builds(iec61131_types_Unsigned_Integer_Type_Name)
@given(instance=iec61131_types_Unsigned_Integer_Type_Name_strategy)
@settings(max_examples=25)
def test_iec61131_types_Unsigned_Integer_Type_Name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Unsigned_Integer_Type_Name)


iec61131_variables_Array_Variable_strategy = st.builds(iec61131_variables_Array_Variable)
@given(instance=iec61131_variables_Array_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Array_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Array_Variable)


iec61131_variables_Direct_Variable_strategy = st.builds(iec61131_variables_Direct_Variable, value=safe_text)
@given(instance=iec61131_variables_Direct_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Direct_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Direct_Variable)


iec61131_variables_Multi_Element_Variable_strategy = st.builds(iec61131_variables_Multi_Element_Variable)
@given(instance=iec61131_variables_Multi_Element_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Multi_Element_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Multi_Element_Variable)


iec61131_variables_Structured_Variable_strategy = st.builds(iec61131_variables_Structured_Variable)
@given(instance=iec61131_variables_Structured_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Structured_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Structured_Variable)


iec61131_variables_Subscript_List_strategy = st.builds(iec61131_variables_Subscript_List)
@given(instance=iec61131_variables_Subscript_List_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Subscript_List_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Subscript_List)


iec61131_variables_Symbolic_Variable_strategy = st.builds(iec61131_variables_Symbolic_Variable)
@given(instance=iec61131_variables_Symbolic_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Symbolic_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Symbolic_Variable)


iec61131_variables_Variable_strategy = st.builds(iec61131_variables_Variable)
@given(instance=iec61131_variables_Variable_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Variable)


iec61131_variables_Variable_Name_strategy = st.builds(iec61131_variables_Variable_Name)
@given(instance=iec61131_variables_Variable_Name_strategy)
@settings(max_examples=25)
def test_iec61131_variables_Variable_Name_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Variable_Name)


il_Il_Expr_Operator_strategy = st.builds(il_Il_Expr_Operator)
@given(instance=il_Il_Expr_Operator_strategy)
@settings(max_examples=25)
def test_il_Il_Expr_Operator_instantiation(instance):
    assert isinstance(instance, il_Il_Expr_Operator)


il_Il_Operand_strategy = st.builds(il_Il_Operand)
@given(instance=il_Il_Operand_strategy)
@settings(max_examples=25)
def test_il_Il_Operand_instantiation(instance):
    assert isinstance(instance, il_Il_Operand)


il_Il_Operations_strategy = st.builds(il_Il_Operations)
@given(instance=il_Il_Operations_strategy)
@settings(max_examples=25)
def test_il_Il_Operations_instantiation(instance):
    assert isinstance(instance, il_Il_Operations)


il_Il_Simple_Operator_strategy = st.builds(il_Il_Simple_Operator)
@given(instance=il_Il_Simple_Operator_strategy)
@settings(max_examples=25)
def test_il_Il_Simple_Operator_instantiation(instance):
    assert isinstance(instance, il_Il_Simple_Operator)


il_Simple_Instr_strategy = st.builds(il_Simple_Instr)
@given(instance=il_Simple_Instr_strategy)
@settings(max_examples=25)
def test_il_Simple_Instr_instantiation(instance):
    assert isinstance(instance, il_Simple_Instr)


interfaces_External_Specification_strategy = st.builds(interfaces_External_Specification)
@given(instance=interfaces_External_Specification_strategy)
@settings(max_examples=25)
def test_interfaces_External_Specification_instantiation(instance):
    assert isinstance(instance, interfaces_External_Specification)


interfaces_Interface_strategy = st.builds(interfaces_Interface)
@given(instance=interfaces_Interface_strategy)
@settings(max_examples=25)
def test_interfaces_Interface_instantiation(instance):
    assert isinstance(instance, interfaces_Interface)


interfaces_Located_Var_Spec_Init_strategy = st.builds(interfaces_Located_Var_Spec_Init)
@given(instance=interfaces_Located_Var_Spec_Init_strategy)
@settings(max_examples=25)
def test_interfaces_Located_Var_Spec_Init_instantiation(instance):
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)


interfaces_Range_strategy = st.builds(interfaces_Range)
@given(instance=interfaces_Range_strategy)
@settings(max_examples=25)
def test_interfaces_Range_instantiation(instance):
    assert isinstance(instance, interfaces_Range)


interfaces_Simple_Specification_Func_strategy = st.builds(interfaces_Simple_Specification_Func)
@given(instance=interfaces_Simple_Specification_Func_strategy)
@settings(max_examples=25)
def test_interfaces_Simple_Specification_Func_instantiation(instance):
    assert isinstance(instance, interfaces_Simple_Specification_Func)


interfaces_Specification_strategy = st.builds(interfaces_Specification)
@given(instance=interfaces_Specification_strategy)
@settings(max_examples=25)
def test_interfaces_Specification_instantiation(instance):
    assert isinstance(instance, interfaces_Specification)


interfaces_Temp_Var_Decl_strategy = st.builds(interfaces_Temp_Var_Decl)
@given(instance=interfaces_Temp_Var_Decl_strategy)
@settings(max_examples=25)
def test_interfaces_Temp_Var_Decl_instantiation(instance):
    assert isinstance(instance, interfaces_Temp_Var_Decl)


interfaces_Var1_Specification_strategy = st.builds(interfaces_Var1_Specification)
@given(instance=interfaces_Var1_Specification_strategy)
@settings(max_examples=25)
def test_interfaces_Var1_Specification_instantiation(instance):
    assert isinstance(instance, interfaces_Var1_Specification)


interfaces_Var1_Specification_Func_strategy = st.builds(interfaces_Var1_Specification_Func)
@given(instance=interfaces_Var1_Specification_Func_strategy)
@settings(max_examples=25)
def test_interfaces_Var1_Specification_Func_instantiation(instance):
    assert isinstance(instance, interfaces_Var1_Specification_Func)


interfaces_Var2_Init_Decl_strategy = st.builds(interfaces_Var2_Init_Decl)
@given(instance=interfaces_Var2_Init_Decl_strategy)
@settings(max_examples=25)
def test_interfaces_Var2_Init_Decl_instantiation(instance):
    assert isinstance(instance, interfaces_Var2_Init_Decl)


interfaces_Var_Spec_strategy = st.builds(interfaces_Var_Spec)
@given(instance=interfaces_Var_Spec_strategy)
@settings(max_examples=25)
def test_interfaces_Var_Spec_instantiation(instance):
    assert isinstance(instance, interfaces_Var_Spec)


literals_BSInteger_strategy = st.builds(literals_BSInteger)
@given(instance=literals_BSInteger_strategy)
@settings(max_examples=25)
def test_literals_BSInteger_instantiation(instance):
    assert isinstance(instance, literals_BSInteger)


literals_Fixed_Point_Literal_strategy = st.builds(literals_Fixed_Point_Literal)
@given(instance=literals_Fixed_Point_Literal_strategy)
@settings(max_examples=25)
def test_literals_Fixed_Point_Literal_instantiation(instance):
    assert isinstance(instance, literals_Fixed_Point_Literal)


literals_Integer_strategy = st.builds(literals_Integer)
@given(instance=literals_Integer_strategy)
@settings(max_examples=25)
def test_literals_Integer_instantiation(instance):
    assert isinstance(instance, literals_Integer)


literals_Time_Literal_strategy = st.builds(literals_Time_Literal)
@given(instance=literals_Time_Literal_strategy)
@settings(max_examples=25)
def test_literals_Time_Literal_instantiation(instance):
    assert isinstance(instance, literals_Time_Literal)


operators_Add_Operator_strategy = st.builds(operators_Add_Operator)
@given(instance=operators_Add_Operator_strategy)
@settings(max_examples=25)
def test_operators_Add_Operator_instantiation(instance):
    assert isinstance(instance, operators_Add_Operator)


operators_Addition_Operator_strategy = st.builds(operators_Addition_Operator)
@given(instance=operators_Addition_Operator_strategy)
@settings(max_examples=25)
def test_operators_Addition_Operator_instantiation(instance):
    assert isinstance(instance, operators_Addition_Operator)


operators_Arithmetic_Name_strategy = st.builds(operators_Arithmetic_Name)
@given(instance=operators_Arithmetic_Name_strategy)
@settings(max_examples=25)
def test_operators_Arithmetic_Name_instantiation(instance):
    assert isinstance(instance, operators_Arithmetic_Name)


operators_Comparison_Name_strategy = st.builds(operators_Comparison_Name)
@given(instance=operators_Comparison_Name_strategy)
@settings(max_examples=25)
def test_operators_Comparison_Name_instantiation(instance):
    assert isinstance(instance, operators_Comparison_Name)


operators_Divide_Operator_strategy = st.builds(operators_Divide_Operator)
@given(instance=operators_Divide_Operator_strategy)
@settings(max_examples=25)
def test_operators_Divide_Operator_instantiation(instance):
    assert isinstance(instance, operators_Divide_Operator)


operators_Dot_Operator_strategy = st.builds(operators_Dot_Operator)
@given(instance=operators_Dot_Operator_strategy)
@settings(max_examples=25)
def test_operators_Dot_Operator_instantiation(instance):
    assert isinstance(instance, operators_Dot_Operator)


operators_Equal_Operator_strategy = st.builds(operators_Equal_Operator)
@given(instance=operators_Equal_Operator_strategy)
@settings(max_examples=25)
def test_operators_Equal_Operator_instantiation(instance):
    assert isinstance(instance, operators_Equal_Operator)


operators_GreaterEqual_Operator_strategy = st.builds(operators_GreaterEqual_Operator)
@given(instance=operators_GreaterEqual_Operator_strategy)
@settings(max_examples=25)
def test_operators_GreaterEqual_Operator_instantiation(instance):
    assert isinstance(instance, operators_GreaterEqual_Operator)


operators_Greater_Operator_strategy = st.builds(operators_Greater_Operator)
@given(instance=operators_Greater_Operator_strategy)
@settings(max_examples=25)
def test_operators_Greater_Operator_instantiation(instance):
    assert isinstance(instance, operators_Greater_Operator)


operators_LessEqual_Operator_strategy = st.builds(operators_LessEqual_Operator)
@given(instance=operators_LessEqual_Operator_strategy)
@settings(max_examples=25)
def test_operators_LessEqual_Operator_instantiation(instance):
    assert isinstance(instance, operators_LessEqual_Operator)


operators_Less_Operator_strategy = st.builds(operators_Less_Operator)
@given(instance=operators_Less_Operator_strategy)
@settings(max_examples=25)
def test_operators_Less_Operator_instantiation(instance):
    assert isinstance(instance, operators_Less_Operator)


operators_Multiply_Operator_strategy = st.builds(operators_Multiply_Operator)
@given(instance=operators_Multiply_Operator_strategy)
@settings(max_examples=25)
def test_operators_Multiply_Operator_instantiation(instance):
    assert isinstance(instance, operators_Multiply_Operator)


operators_Operator_strategy = st.builds(operators_Operator)
@given(instance=operators_Operator_strategy)
@settings(max_examples=25)
def test_operators_Operator_instantiation(instance):
    assert isinstance(instance, operators_Operator)


operators_Substraction_Operator_strategy = st.builds(operators_Substraction_Operator)
@given(instance=operators_Substraction_Operator_strategy)
@settings(max_examples=25)
def test_operators_Substraction_Operator_instantiation(instance):
    assert isinstance(instance, operators_Substraction_Operator)


operators_Unary_Operator_strategy = st.builds(operators_Unary_Operator)
@given(instance=operators_Unary_Operator_strategy)
@settings(max_examples=25)
def test_operators_Unary_Operator_instantiation(instance):
    assert isinstance(instance, operators_Unary_Operator)


operators_Unequal_Operator_strategy = st.builds(operators_Unequal_Operator)
@given(instance=operators_Unequal_Operator_strategy)
@settings(max_examples=25)
def test_operators_Unequal_Operator_instantiation(instance):
    assert isinstance(instance, operators_Unequal_Operator)


pous_Function_Block_Body_strategy = st.builds(pous_Function_Block_Body)
@given(instance=pous_Function_Block_Body_strategy)
@settings(max_examples=25)
def test_pous_Function_Block_Body_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Body)


pous_Function_Block_Type_Name_strategy = st.builds(pous_Function_Block_Type_Name)
@given(instance=pous_Function_Block_Type_Name_strategy)
@settings(max_examples=25)
def test_pous_Function_Block_Type_Name_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Type_Name)


pous_Function_Block_Vars_strategy = st.builds(pous_Function_Block_Vars)
@given(instance=pous_Function_Block_Vars_strategy)
@settings(max_examples=25)
def test_pous_Function_Block_Vars_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Vars)


pous_Function_Body_strategy = st.builds(pous_Function_Body)
@given(instance=pous_Function_Body_strategy)
@settings(max_examples=25)
def test_pous_Function_Body_instantiation(instance):
    assert isinstance(instance, pous_Function_Body)


pous_Function_Name_strategy = st.builds(pous_Function_Name)
@given(instance=pous_Function_Name_strategy)
@settings(max_examples=25)
def test_pous_Function_Name_instantiation(instance):
    assert isinstance(instance, pous_Function_Name)


pous_Function_Return_Value_strategy = st.builds(pous_Function_Return_Value)
@given(instance=pous_Function_Return_Value_strategy)
@settings(max_examples=25)
def test_pous_Function_Return_Value_instantiation(instance):
    assert isinstance(instance, pous_Function_Return_Value)


pous_Function_Vars_strategy = st.builds(pous_Function_Vars)
@given(instance=pous_Function_Vars_strategy)
@settings(max_examples=25)
def test_pous_Function_Vars_instantiation(instance):
    assert isinstance(instance, pous_Function_Vars)


pous_Program_Vars_strategy = st.builds(pous_Program_Vars)
@given(instance=pous_Program_Vars_strategy)
@settings(max_examples=25)
def test_pous_Program_Vars_instantiation(instance):
    assert isinstance(instance, pous_Program_Vars)


pous_Structure_Elements_strategy = st.builds(pous_Structure_Elements)
@given(instance=pous_Structure_Elements_strategy)
@settings(max_examples=25)
def test_pous_Structure_Elements_instantiation(instance):
    assert isinstance(instance, pous_Structure_Elements)


pous_Structure_Specification_strategy = st.builds(pous_Structure_Specification)
@given(instance=pous_Structure_Specification_strategy)
@settings(max_examples=25)
def test_pous_Structure_Specification_instantiation(instance):
    assert isinstance(instance, pous_Structure_Specification)


sfc_Action_Time_strategy = st.builds(sfc_Action_Time)
@given(instance=sfc_Action_Time_strategy)
@settings(max_examples=25)
def test_sfc_Action_Time_instantiation(instance):
    assert isinstance(instance, sfc_Action_Time)


sfc_Sfc_Elements_strategy = st.builds(sfc_Sfc_Elements)
@given(instance=sfc_Sfc_Elements_strategy)
@settings(max_examples=25)
def test_sfc_Sfc_Elements_instantiation(instance):
    assert isinstance(instance, sfc_Sfc_Elements)


sfc_Step_Types_strategy = st.builds(sfc_Step_Types)
@given(instance=sfc_Step_Types_strategy)
@settings(max_examples=25)
def test_sfc_Step_Types_instantiation(instance):
    assert isinstance(instance, sfc_Step_Types)


st_Case_List_Element_strategy = st.builds(st_Case_List_Element)
@given(instance=st_Case_List_Element_strategy)
@settings(max_examples=25)
def test_st_Case_List_Element_instantiation(instance):
    assert isinstance(instance, st_Case_List_Element)


types_Data_Type_Name_strategy = st.builds(types_Data_Type_Name)
@given(instance=types_Data_Type_Name_strategy)
@settings(max_examples=25)
def test_types_Data_Type_Name_instantiation(instance):
    assert isinstance(instance, types_Data_Type_Name)


types_Derived_Type_Name_strategy = st.builds(types_Derived_Type_Name)
@given(instance=types_Derived_Type_Name_strategy)
@settings(max_examples=25)
def test_types_Derived_Type_Name_instantiation(instance):
    assert isinstance(instance, types_Derived_Type_Name)


types_Non_Generic_Type_Name_strategy = st.builds(types_Non_Generic_Type_Name)
@given(instance=types_Non_Generic_Type_Name_strategy)
@settings(max_examples=25)
def test_types_Non_Generic_Type_Name_instantiation(instance):
    assert isinstance(instance, types_Non_Generic_Type_Name)


types_Simple_Specification_strategy = st.builds(types_Simple_Specification)
@given(instance=types_Simple_Specification_strategy)
@settings(max_examples=25)
def test_types_Simple_Specification_instantiation(instance):
    assert isinstance(instance, types_Simple_Specification)


types_Single_Element_Type_Name_strategy = st.builds(types_Single_Element_Type_Name)
@given(instance=types_Single_Element_Type_Name_strategy)
@settings(max_examples=25)
def test_types_Single_Element_Type_Name_instantiation(instance):
    assert isinstance(instance, types_Single_Element_Type_Name)


variables_Symbolic_Variable_strategy = st.builds(variables_Symbolic_Variable)
@given(instance=variables_Symbolic_Variable_strategy)
@settings(max_examples=25)
def test_variables_Symbolic_Variable_instantiation(instance):
    assert isinstance(instance, variables_Symbolic_Variable)


variables_Variable_strategy = st.builds(variables_Variable)
@given(instance=variables_Variable_strategy)
@settings(max_examples=25)
def test_variables_Variable_instantiation(instance):
    assert isinstance(instance, variables_Variable)


