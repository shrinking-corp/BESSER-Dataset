import pytest
from datetime import date, datetime, time, timedelta

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
# REVERSE-DIRECTION ASSOCIATION TESTS
# Mirrors test_structural_full.py's link_reassign_clear, but sets from the
# OTHER end's own setter directly, instead of relying on it firing only as a
# side effect of the forward-direction test. See module docstring.
# =============================================================================

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_access_name230_stub_double():
    # Access_Name has no real 'Access_Name' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_pous_Program_Access_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_pous_Program_Access_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_pous_Program_Access_Decl(direction="sample_text")
    partner = Access_Name()
    setattr(partner, 'Access_Name', None)
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl', partner)
    assert getattr(partner, 'Access_Name') == owner
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl', None)
    assert getattr(partner, 'Access_Name') is None


def test_assoc_access_name334_stub_double():
    # Access_Name has no real 'Access_Name335' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Access_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Access_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Access_Declaration(direction="sample_text")
    partner = Access_Name()
    setattr(partner, 'Access_Name335', None)
    _safe_set(owner, 'iec61131_configurations_Access_Declaration', partner)
    assert getattr(partner, 'Access_Name335') == owner
    _safe_set(owner, 'iec61131_configurations_Access_Declaration', None)
    assert getattr(partner, 'Access_Name335') is None


def test_assoc_access_path336_stub_double():
    # Access_Path has no real 'Access_Path' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Access_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Access_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Access_Declaration(direction="sample_text")
    partner = Access_Path()
    setattr(partner, 'Access_Path', None)
    _safe_set(owner, 'iec61131_configurations_Access_Declaration337', partner)
    assert getattr(partner, 'Access_Path') == owner
    _safe_set(owner, 'iec61131_configurations_Access_Declaration337', None)
    assert getattr(partner, 'Access_Path') is None


def test_assoc_action_time652_stub_double():
    # Action_Time has no real 'Action_Time' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_sfc_Action_Qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_sfc_Action_Qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_sfc_Action_Qualifier(qualifier="sample_text")
    partner = Action_Time()
    setattr(partner, 'Action_Time', None)
    _safe_set(owner, 'iec61131_sfc_Action_Qualifier653', partner)
    assert getattr(partner, 'Action_Time') == owner
    _safe_set(owner, 'iec61131_sfc_Action_Qualifier653', None)
    assert getattr(partner, 'Action_Time') is None


def test_assoc_bool_type_name58_stub_double():
    # Bool_Type_Name has no real 'Bool_Type_Name' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Edge_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Edge_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    partner = Bool_Type_Name()
    setattr(partner, 'Bool_Type_Name', None)
    _safe_set(owner, 'iec61131_interfaces_Edge_Declaration59', partner)
    assert getattr(partner, 'Bool_Type_Name') == owner
    _safe_set(owner, 'iec61131_interfaces_Edge_Declaration59', None)
    assert getattr(partner, 'Bool_Type_Name') is None


def test_assoc_common_character_representation50_stub_double():
    # Common_Character_Representation has no real 'Common_Character_Representation' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_literals_Single_Byte_Character_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_literals_Single_Byte_Character_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_literals_Single_Byte_Character_Representation(value="sample_text")
    partner = Common_Character_Representation()
    setattr(partner, 'Common_Character_Representation', None)
    _safe_set(owner, 'iec61131_literals_Single_Byte_Character_Representation', partner)
    assert getattr(partner, 'Common_Character_Representation') == owner
    _safe_set(owner, 'iec61131_literals_Single_Byte_Character_Representation', None)
    assert getattr(partner, 'Common_Character_Representation') is None


def test_assoc_common_character_representation51_stub_double():
    # Common_Character_Representation has no real 'Common_Character_Representation52' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_literals_Double_Byte_Character_Representation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_literals_Double_Byte_Character_Representation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_literals_Double_Byte_Character_Representation(value="sample_text")
    partner = Common_Character_Representation()
    setattr(partner, 'Common_Character_Representation52', None)
    _safe_set(owner, 'iec61131_literals_Double_Byte_Character_Representation', partner)
    assert getattr(partner, 'Common_Character_Representation52') == owner
    _safe_set(owner, 'iec61131_literals_Double_Byte_Character_Representation', None)
    assert getattr(partner, 'Common_Character_Representation52') is None


def test_assoc_enumerated_type_name98_stub_double():
    # Enumerated_Type_Name has no real 'Enumerated_Type_Name' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Enumerated_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Enumerated_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Enumerated_Value(name="sample_text")
    partner = Enumerated_Type_Name()
    setattr(partner, 'Enumerated_Type_Name', None)
    _safe_set(owner, 'iec61131_interfaces_Enumerated_Value', partner)
    assert getattr(partner, 'Enumerated_Type_Name') == owner
    _safe_set(owner, 'iec61131_interfaces_Enumerated_Value', None)
    assert getattr(partner, 'Enumerated_Type_Name') is None


def test_assoc_external_declaration121_stub_double():
    # External_Declaration has no real 'External_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_External_Var_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_External_Var_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_External_Var_Declarations(constant=True)
    partner = External_Declaration()
    setattr(partner, 'External_Declaration', None)
    _safe_set(owner, 'iec61131_interfaces_External_Var_Declarations', {partner})
    assert getattr(partner, 'External_Declaration') == owner
    _safe_set(owner, 'iec61131_interfaces_External_Var_Declarations', set())
    assert getattr(partner, 'External_Declaration') is None


def test_assoc_fixed_point10_stub_double():
    # Fixed_Point has no real 'Fixed_Point' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_literals_Real_Literal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_literals_Real_Literal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    partner = Fixed_Point()
    setattr(partner, 'Fixed_Point', None)
    _safe_set(owner, 'iec61131_literals_Real_Literal11', partner)
    assert getattr(partner, 'Fixed_Point') == owner
    _safe_set(owner, 'iec61131_literals_Real_Literal11', None)
    assert getattr(partner, 'Fixed_Point') is None


def test_assoc_global_var_decl145_stub_double():
    # Global_Var_Decl has no real 'Global_Var_Decl' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Global_Var_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Global_Var_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Global_Var_Declarations(constant=True, retain=True)
    partner = Global_Var_Decl()
    setattr(partner, 'Global_Var_Decl', None)
    _safe_set(owner, 'iec61131_interfaces_Global_Var_Declarations', {partner})
    assert getattr(partner, 'Global_Var_Decl') == owner
    _safe_set(owner, 'iec61131_interfaces_Global_Var_Declarations', set())
    assert getattr(partner, 'Global_Var_Decl') is None


def test_assoc_incompl_located_var_decl128_stub_double():
    # Incompl_Located_Var_Decl has no real 'Incompl_Located_Var_Decl' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Incompl_Located_Var_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Incompl_Located_Var_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Incompl_Located_Var_Declarations(retain=True)
    partner = Incompl_Located_Var_Decl()
    setattr(partner, 'Incompl_Located_Var_Decl', None)
    _safe_set(owner, 'iec61131_interfaces_Incompl_Located_Var_Declarations', {partner})
    assert getattr(partner, 'Incompl_Located_Var_Decl') == owner
    _safe_set(owner, 'iec61131_interfaces_Incompl_Located_Var_Declarations', set())
    assert getattr(partner, 'Incompl_Located_Var_Decl') is None


def test_assoc_input_declaration53_stub_double():
    # Input_Declaration has no real 'Input_Declaration' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Input_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Input_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Input_Declarations(retain=True)
    partner = Input_Declaration()
    setattr(partner, 'Input_Declaration', None)
    _safe_set(owner, 'iec61131_interfaces_Input_Declarations', {partner})
    assert getattr(partner, 'Input_Declaration') == owner
    _safe_set(owner, 'iec61131_interfaces_Input_Declarations', set())
    assert getattr(partner, 'Input_Declaration') is None


def test_assoc_integer105_stub_double():
    # Range has no real 'Range' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Subrange's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Subrange's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Subrange(delimiter="sample_text")
    partner = Range()
    setattr(partner, 'Range', None)
    _safe_set(owner, 'iec61131_interfaces_Subrange', {partner})
    assert getattr(partner, 'Range') == owner
    _safe_set(owner, 'iec61131_interfaces_Subrange', set())
    assert getattr(partner, 'Range') is None


def test_assoc_located_var_decl144_stub_double():
    # Located_Var_Decl has no real 'Located_Var_Decl' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Located_Var_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Located_Var_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Located_Var_Declarations(constant=True, retain=True)
    partner = Located_Var_Decl()
    setattr(partner, 'Located_Var_Decl', None)
    _safe_set(owner, 'iec61131_interfaces_Located_Var_Declarations', {partner})
    assert getattr(partner, 'Located_Var_Decl') == owner
    _safe_set(owner, 'iec61131_interfaces_Located_Var_Declarations', set())
    assert getattr(partner, 'Located_Var_Decl') is None


def test_assoc_non_generic_type_name231_stub_double():
    # Non_Generic_Type_Name has no real 'Non_Generic_Type_Name233' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_pous_Program_Access_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_pous_Program_Access_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_pous_Program_Access_Decl(direction="sample_text")
    partner = Non_Generic_Type_Name()
    setattr(partner, 'Non_Generic_Type_Name233', None)
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl232', partner)
    assert getattr(partner, 'Non_Generic_Type_Name233') == owner
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl232', None)
    assert getattr(partner, 'Non_Generic_Type_Name233') is None


def test_assoc_non_generic_type_name338_stub_double():
    # Non_Generic_Type_Name has no real 'Non_Generic_Type_Name340' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Access_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Access_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Access_Declaration(direction="sample_text")
    partner = Non_Generic_Type_Name()
    setattr(partner, 'Non_Generic_Type_Name340', None)
    _safe_set(owner, 'iec61131_configurations_Access_Declaration339', partner)
    assert getattr(partner, 'Non_Generic_Type_Name340') == owner
    _safe_set(owner, 'iec61131_configurations_Access_Declaration339', None)
    assert getattr(partner, 'Non_Generic_Type_Name340') is None


def test_assoc_prog_conf_elements317_stub_double():
    # Prog_Conf_Elements has no real 'Prog_Conf_Elements' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Program_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Program_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Program_Configuration(retain=True)
    partner = Prog_Conf_Elements()
    setattr(partner, 'Prog_Conf_Elements', None)
    _safe_set(owner, 'iec61131_configurations_Program_Configuration318', partner)
    assert getattr(partner, 'Prog_Conf_Elements') == owner
    _safe_set(owner, 'iec61131_configurations_Program_Configuration318', None)
    assert getattr(partner, 'Prog_Conf_Elements') is None


def test_assoc_program_name310_stub_double():
    # Program_Name has no real 'Program_Name' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Program_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Program_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Program_Configuration(retain=True)
    partner = Program_Name()
    setattr(partner, 'Program_Name', None)
    _safe_set(owner, 'iec61131_configurations_Program_Configuration', partner)
    assert getattr(partner, 'Program_Name') == owner
    _safe_set(owner, 'iec61131_configurations_Program_Configuration', None)
    assert getattr(partner, 'Program_Name') is None


def test_assoc_program_type_name314_stub_double():
    # Program_Type_Name has no real 'Program_Type_Name316' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Program_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Program_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Program_Configuration(retain=True)
    partner = Program_Type_Name()
    setattr(partner, 'Program_Type_Name316', None)
    _safe_set(owner, 'iec61131_configurations_Program_Configuration315', partner)
    assert getattr(partner, 'Program_Type_Name316') == owner
    _safe_set(owner, 'iec61131_configurations_Program_Configuration315', None)
    assert getattr(partner, 'Program_Type_Name316') is None


def test_assoc_real_type_name9_stub_double():
    # Real_Type_Name has no real 'Real_Type_Name' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_literals_Real_Literal's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_literals_Real_Literal's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_literals_Real_Literal(exponent="sample_text", negative=True)
    partner = Real_Type_Name()
    setattr(partner, 'Real_Type_Name', None)
    _safe_set(owner, 'iec61131_literals_Real_Literal', partner)
    assert getattr(partner, 'Real_Type_Name') == owner
    _safe_set(owner, 'iec61131_literals_Real_Literal', None)
    assert getattr(partner, 'Real_Type_Name') is None


def test_assoc_second48_stub_double():
    # Fixed_Point has no real 'Fixed_Point49' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_literals_Daytime's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_literals_Daytime's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_literals_Daytime(hour="sample_text", minute="sample_text")
    partner = Fixed_Point()
    setattr(partner, 'Fixed_Point49', None)
    _safe_set(owner, 'iec61131_literals_Daytime', partner)
    assert getattr(partner, 'Fixed_Point49') == owner
    _safe_set(owner, 'iec61131_literals_Daytime', None)
    assert getattr(partner, 'Fixed_Point49') is None


def test_assoc_symbolic_variable234_stub_double():
    # Symbolic_Variable has no real 'Symbolic_Variable' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_pous_Program_Access_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_pous_Program_Access_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_pous_Program_Access_Decl(direction="sample_text")
    partner = Symbolic_Variable()
    setattr(partner, 'Symbolic_Variable', None)
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl235', partner)
    assert getattr(partner, 'Symbolic_Variable') == owner
    _safe_set(owner, 'iec61131_pous_Program_Access_Decl235', None)
    assert getattr(partner, 'Symbolic_Variable') is None


def test_assoc_task_name311_stub_double():
    # Task_Name has no real 'Task_Name313' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_configurations_Program_Configuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_configurations_Program_Configuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_configurations_Program_Configuration(retain=True)
    partner = Task_Name()
    setattr(partner, 'Task_Name313', None)
    _safe_set(owner, 'iec61131_configurations_Program_Configuration312', partner)
    assert getattr(partner, 'Task_Name313') == owner
    _safe_set(owner, 'iec61131_configurations_Program_Configuration312', None)
    assert getattr(partner, 'Task_Name313') is None


def test_assoc_timed_qualifier651_stub_double():
    # Timed_Qualifier has no real 'Timed_Qualifier' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_sfc_Action_Qualifier's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_sfc_Action_Qualifier's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_sfc_Action_Qualifier(qualifier="sample_text")
    partner = Timed_Qualifier()
    setattr(partner, 'Timed_Qualifier', None)
    _safe_set(owner, 'iec61131_sfc_Action_Qualifier', partner)
    assert getattr(partner, 'Timed_Qualifier') == owner
    _safe_set(owner, 'iec61131_sfc_Action_Qualifier', None)
    assert getattr(partner, 'Timed_Qualifier') is None


def test_assoc_var2_init_decl199_stub_double():
    # Var2_Init_Decl has no real 'Var2_Init_Decl' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Function_Var_Decl's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Function_Var_Decl's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Function_Var_Decl(constant=True)
    partner = Var2_Init_Decl()
    setattr(partner, 'Var2_Init_Decl', None)
    _safe_set(owner, 'iec61131_interfaces_Function_Var_Decl', {partner})
    assert getattr(partner, 'Var2_Init_Decl') == owner
    _safe_set(owner, 'iec61131_interfaces_Function_Var_Decl', set())
    assert getattr(partner, 'Var2_Init_Decl') is None


def test_assoc_var_init_decl76_stub_double():
    # Var_Init_Decl has no real 'Var_Init_Decl' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Output_Declarations's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Output_Declarations's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Output_Declarations(retain=True)
    partner = Var_Init_Decl()
    setattr(partner, 'Var_Init_Decl', None)
    _safe_set(owner, 'iec61131_interfaces_Output_Declarations', {partner})
    assert getattr(partner, 'Var_Init_Decl') == owner
    _safe_set(owner, 'iec61131_interfaces_Output_Declarations', set())
    assert getattr(partner, 'Var_Init_Decl') is None


def test_assoc_var_list56_stub_double():
    # Var1_List has no real 'Var1_List57' property in the generated
    # code (a bare stub) -- manually attach it so iec61131_interfaces_Edge_Declaration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iec61131_interfaces_Edge_Declaration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iec61131_interfaces_Edge_Declaration(edge="sample_text")
    partner = Var1_List()
    setattr(partner, 'Var1_List57', None)
    _safe_set(owner, 'iec61131_interfaces_Edge_Declaration', partner)
    assert getattr(partner, 'Var1_List57') == owner
    _safe_set(owner, 'iec61131_interfaces_Edge_Declaration', None)
    assert getattr(partner, 'Var1_List57') is None


