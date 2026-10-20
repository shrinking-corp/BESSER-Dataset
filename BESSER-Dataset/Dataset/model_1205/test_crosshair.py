from python_code import ocl_expressions_BooleanLiteralExp

def test_ocl_expressions_BooleanLiteralExp___init__():
    assert ocl_expressions_BooleanLiteralExp.__init__(ocl_expressions_BooleanLiteralExp(''), '') == None

def test_ocl_expressions_BooleanLiteralExp_boolean_type():
    assert ocl_expressions_BooleanLiteralExp.boolean_type(ocl_expressions_BooleanLiteralExp(''), 0, '\x00\x00') == None


from python_code import ocl_expressions_CollectionItem

def test_ocl_expressions_CollectionItem___init__():
    assert ocl_expressions_CollectionItem.__init__(ocl_expressions_CollectionItem()) == None

def test_ocl_expressions_CollectionItem_item_type():
    assert ocl_expressions_CollectionItem.item_type(ocl_expressions_CollectionItem(), '', '') == None


from python_code import ocl_expressions_CollectionLiteralExp

def test_ocl_expressions_CollectionLiteralExp___init__():
    assert ocl_expressions_CollectionLiteralExp.__init__(ocl_expressions_CollectionLiteralExp('', False), '', False) == None

def test_ocl_expressions_CollectionLiteralExp_element_type():
    assert ocl_expressions_CollectionLiteralExp.element_type(ocl_expressions_CollectionLiteralExp('', False), '', '') == None

def test_ocl_expressions_CollectionLiteralExp_sequence_kind():
    assert ocl_expressions_CollectionLiteralExp.sequence_kind(ocl_expressions_CollectionLiteralExp('', False), '', '') == None

def test_ocl_expressions_CollectionLiteralExp_bag_kind():
    assert ocl_expressions_CollectionLiteralExp.bag_kind(ocl_expressions_CollectionLiteralExp('', False), '', '') == None

def test_ocl_expressions_CollectionLiteralExp_set_kind():
    assert ocl_expressions_CollectionLiteralExp.set_kind(ocl_expressions_CollectionLiteralExp('', False), '', '') == None

def test_ocl_expressions_CollectionLiteralExp_no_collection_instances():
    assert ocl_expressions_CollectionLiteralExp.no_collection_instances(ocl_expressions_CollectionLiteralExp('', False), '', '') == None


from python_code import ocl_expressions_CollectionRange

def test_ocl_expressions_CollectionRange___init__():
    assert ocl_expressions_CollectionRange.__init__(ocl_expressions_CollectionRange()) == None

def test_ocl_expressions_CollectionRange_range_type():
    assert ocl_expressions_CollectionRange.range_type(ocl_expressions_CollectionRange(), '', '') == None


from python_code import ocl_expressions_EnumLiteralExp

def test_ocl_expressions_EnumLiteralExp___init__():
    assert ocl_expressions_EnumLiteralExp.__init__(ocl_expressions_EnumLiteralExp()) == None

def test_ocl_expressions_EnumLiteralExp_enum_type():
    assert ocl_expressions_EnumLiteralExp.enum_type(ocl_expressions_EnumLiteralExp(), '', '') == None


from python_code import ocl_expressions_FeatureCallExp

def test_ocl_expressions_FeatureCallExp___init__():
    assert ocl_expressions_FeatureCallExp.__init__(ocl_expressions_FeatureCallExp(True), False) == None


from python_code import ocl_expressions_IfExp

def test_ocl_expressions_IfExp___init__():
    assert ocl_expressions_IfExp.__init__(ocl_expressions_IfExp()) == None

def test_ocl_expressions_IfExp_boolean_condition():
    assert ocl_expressions_IfExp.boolean_condition(ocl_expressions_IfExp(), '', '') == None

def test_ocl_expressions_IfExp_if_type():
    assert ocl_expressions_IfExp.if_type(ocl_expressions_IfExp(), '', '') == None


from python_code import ocl_expressions_IntegerLiteralExp

def test_ocl_expressions_IntegerLiteralExp___init__():
    assert ocl_expressions_IntegerLiteralExp.__init__(ocl_expressions_IntegerLiteralExp(''), '') == None

def test_ocl_expressions_IntegerLiteralExp_integer_type():
    assert ocl_expressions_IntegerLiteralExp.integer_type(ocl_expressions_IntegerLiteralExp(''), 0, '\x00\x00') == None


from python_code import ocl_expressions_IterateExp

def test_ocl_expressions_IterateExp___init__():
    assert ocl_expressions_IterateExp.__init__(ocl_expressions_IterateExp()) == None

def test_ocl_expressions_IterateExp_result_init():
    assert ocl_expressions_IterateExp.result_init(ocl_expressions_IterateExp(), '', '') == None

def test_ocl_expressions_IterateExp_iterate_type():
    assert ocl_expressions_IterateExp.iterate_type(ocl_expressions_IterateExp(), '', '') == None

def test_ocl_expressions_IterateExp_body_type():
    assert ocl_expressions_IterateExp.body_type(ocl_expressions_IterateExp(), '', '') == None


from python_code import ocl_expressions_IteratorExp

def test_ocl_expressions_IteratorExp___init__():
    assert ocl_expressions_IteratorExp.__init__(ocl_expressions_IteratorExp()) == None

def test_ocl_expressions_IteratorExp_select_reject_type():
    assert ocl_expressions_IteratorExp.select_reject_type(ocl_expressions_IteratorExp(), '', '') == None

def test_ocl_expressions_IteratorExp_boolean_type():
    assert ocl_expressions_IteratorExp.boolean_type(ocl_expressions_IteratorExp(), '', '') == None

def test_ocl_expressions_IteratorExp_boolean_body_type():
    assert ocl_expressions_IteratorExp.boolean_body_type(ocl_expressions_IteratorExp(), '', '') == None

def test_ocl_expressions_IteratorExp_collect_type():
    assert ocl_expressions_IteratorExp.collect_type(ocl_expressions_IteratorExp(), '', '') == None


from python_code import ocl_expressions_LetExp

def test_ocl_expressions_LetExp___init__():
    assert ocl_expressions_LetExp.__init__(ocl_expressions_LetExp()) == None

def test_ocl_expressions_LetExp_let_type():
    assert ocl_expressions_LetExp.let_type(ocl_expressions_LetExp(), '', '') == None


from python_code import ocl_expressions_LoopExp

def test_ocl_expressions_LoopExp___init__():
    assert ocl_expressions_LoopExp.__init__(ocl_expressions_LoopExp()) == None

def test_ocl_expressions_LoopExp_loop_variable_type():
    assert ocl_expressions_LoopExp.loop_variable_type(ocl_expressions_LoopExp(), '', '') == None

def test_ocl_expressions_LoopExp_loop_variable_init():
    assert ocl_expressions_LoopExp.loop_variable_init(ocl_expressions_LoopExp(), '', '') == None

def test_ocl_expressions_LoopExp_source_collection():
    assert ocl_expressions_LoopExp.source_collection(ocl_expressions_LoopExp(), '', '') == None


from python_code import ocl_expressions_MessageExp

def test_ocl_expressions_MessageExp___init__():
    assert ocl_expressions_MessageExp.__init__(ocl_expressions_MessageExp()) == None

def test_ocl_expressions_MessageExp_target_not_collection():
    assert ocl_expressions_MessageExp.target_not_collection(ocl_expressions_MessageExp(), '', '') == None

def test_ocl_expressions_MessageExp_has_operation_or_signal():
    assert ocl_expressions_MessageExp.has_operation_or_signal(ocl_expressions_MessageExp(), '', '') == None

def test_ocl_expressions_MessageExp_target_defines_operation():
    assert ocl_expressions_MessageExp.target_defines_operation(ocl_expressions_MessageExp(), '', '') == None

def test_ocl_expressions_MessageExp_operation_arguments():
    assert ocl_expressions_MessageExp.operation_arguments(ocl_expressions_MessageExp(), '', '') == None

def test_ocl_expressions_MessageExp_signal_arguments():
    assert ocl_expressions_MessageExp.signal_arguments(ocl_expressions_MessageExp(), '', '') == None


from python_code import ocl_expressions_OperationCallExp

def test_ocl_expressions_OperationCallExp___init__():
    assert ocl_expressions_OperationCallExp.__init__(ocl_expressions_OperationCallExp(0), 0) == None

def test_ocl_expressions_OperationCallExp_arguments_conform():
    assert ocl_expressions_OperationCallExp.arguments_conform(ocl_expressions_OperationCallExp(0), 0, '\x00\x00') == None

def test_ocl_expressions_OperationCallExp_argument_count():
    assert ocl_expressions_OperationCallExp.argument_count(ocl_expressions_OperationCallExp(0), 0, '\x00\x00') == None


from python_code import ocl_expressions_PropertyCallExp

def test_ocl_expressions_PropertyCallExp___init__():
    assert ocl_expressions_PropertyCallExp.__init__(ocl_expressions_PropertyCallExp()) == None

def test_ocl_expressions_PropertyCallExp_property_type():
    assert ocl_expressions_PropertyCallExp.property_type(ocl_expressions_PropertyCallExp(), '', '') == None


from python_code import ocl_expressions_RealLiteralExp

def test_ocl_expressions_RealLiteralExp___init__():
    assert ocl_expressions_RealLiteralExp.__init__(ocl_expressions_RealLiteralExp(''), '') == None

def test_ocl_expressions_RealLiteralExp_real_type():
    assert ocl_expressions_RealLiteralExp.real_type(ocl_expressions_RealLiteralExp(''), 0, '\x00\x00') == None


from python_code import ocl_expressions_StringLiteralExp

def test_ocl_expressions_StringLiteralExp___init__():
    assert ocl_expressions_StringLiteralExp.__init__(ocl_expressions_StringLiteralExp(''), '') == None

def test_ocl_expressions_StringLiteralExp_string_type():
    assert ocl_expressions_StringLiteralExp.string_type(ocl_expressions_StringLiteralExp(''), 0, '\x00\x00') == None


from python_code import ocl_expressions_TupleLiteralExp

def test_ocl_expressions_TupleLiteralExp___init__():
    assert ocl_expressions_TupleLiteralExp.__init__(ocl_expressions_TupleLiteralExp()) == None

def test_ocl_expressions_TupleLiteralExp_parts_unique():
    assert ocl_expressions_TupleLiteralExp.parts_unique(ocl_expressions_TupleLiteralExp(), '', '') == None

def test_ocl_expressions_TupleLiteralExp_tuple_type():
    assert ocl_expressions_TupleLiteralExp.tuple_type(ocl_expressions_TupleLiteralExp(), '', '') == None


from python_code import ocl_expressions_TupleLiteralPart

def test_ocl_expressions_TupleLiteralPart___init__():
    assert ocl_expressions_TupleLiteralPart.__init__(ocl_expressions_TupleLiteralPart()) == None

def test_ocl_expressions_TupleLiteralPart_value_type():
    assert ocl_expressions_TupleLiteralPart.value_type(ocl_expressions_TupleLiteralPart(), '', '') == None


from python_code import ocl_expressions_UnlimitedNaturalLiteralExp

def test_ocl_expressions_UnlimitedNaturalLiteralExp___init__():
    assert ocl_expressions_UnlimitedNaturalLiteralExp.__init__(ocl_expressions_UnlimitedNaturalLiteralExp('', False), '', False) == None

def test_ocl_expressions_UnlimitedNaturalLiteralExp_natural_type():
    assert ocl_expressions_UnlimitedNaturalLiteralExp.natural_type(ocl_expressions_UnlimitedNaturalLiteralExp('', False), '', '') == None


from python_code import ocl_expressions_Variable

def test_ocl_expressions_Variable___init__():
    assert ocl_expressions_Variable.__init__(ocl_expressions_Variable()) == None

def test_ocl_expressions_Variable_init_type():
    assert ocl_expressions_Variable.init_type(ocl_expressions_Variable(), '', '') == None


from python_code import ocl_expressions_VariableExp

def test_ocl_expressions_VariableExp___init__():
    assert ocl_expressions_VariableExp.__init__(ocl_expressions_VariableExp()) == None

def test_ocl_expressions_VariableExp_var_type():
    assert ocl_expressions_VariableExp.var_type(ocl_expressions_VariableExp(), '', '') == None


from python_code import ocl_types_CollectionType

def test_ocl_types_CollectionType___init__():
    assert ocl_types_CollectionType.__init__(ocl_types_CollectionType(''), '') == None

def test_ocl_types_CollectionType_collection_type_name():
    assert ocl_types_CollectionType.collection_type_name(ocl_types_CollectionType(''), 0, '\x00\x00') == None

def test_ocl_types_CollectionType_oclIterators():
    assert ocl_types_CollectionType.oclIterators(ocl_types_CollectionType('')) == None

def test_ocl_types_CollectionType_no_invalid_values():
    assert ocl_types_CollectionType.no_invalid_values(ocl_types_CollectionType(''), 0, '\x00\x00') == None


from python_code import ocl_types_MessageType

def test_ocl_types_MessageType___init__():
    assert ocl_types_MessageType.__init__(ocl_types_MessageType()) == None

def test_ocl_types_MessageType_exclusive_signature():
    assert ocl_types_MessageType.exclusive_signature(ocl_types_MessageType(), '', '') == None

def test_ocl_types_MessageType_operation_parameters():
    assert ocl_types_MessageType.operation_parameters(ocl_types_MessageType(), '', '') == None

def test_ocl_types_MessageType_signal_attributes():
    assert ocl_types_MessageType.signal_attributes(ocl_types_MessageType(), '', '') == None

def test_ocl_types_MessageType_oclProperties():
    assert ocl_types_MessageType.oclProperties(ocl_types_MessageType()) == None


from python_code import ocl_types_TemplateParameterType

def test_ocl_types_TemplateParameterType___init__():
    assert ocl_types_TemplateParameterType.__init__(ocl_types_TemplateParameterType(''), '') == None


from python_code import ocl_types_TupleType

def test_ocl_types_TupleType___init__():
    assert ocl_types_TupleType.__init__(ocl_types_TupleType()) == None

def test_ocl_types_TupleType_part_names_unique():
    assert ocl_types_TupleType.part_names_unique(ocl_types_TupleType(), '', '') == None

def test_ocl_types_TupleType_tuple_type_name():
    assert ocl_types_TupleType.tuple_type_name(ocl_types_TupleType(), '', '') == None

def test_ocl_types_TupleType_oclProperties():
    assert ocl_types_TupleType.oclProperties(ocl_types_TupleType()) == None

def test_ocl_types_TupleType_features_only_properties():
    assert ocl_types_TupleType.features_only_properties(ocl_types_TupleType(), '', '') == None


from python_code import ocl_utilities_ASTNode

def test_ocl_utilities_ASTNode___init__():
    assert ocl_utilities_ASTNode.__init__(ocl_utilities_ASTNode(0, 0), 0, 0) == None


from python_code import ocl_utilities_CallingASTNode

def test_ocl_utilities_CallingASTNode___init__():
    assert ocl_utilities_CallingASTNode.__init__(ocl_utilities_CallingASTNode(0, 0), 0, 0) == None


from python_code import ocl_utilities_PredefinedType

def test_ocl_utilities_PredefinedType___init__():
    assert ocl_utilities_PredefinedType.__init__(ocl_utilities_PredefinedType()) == None

def test_ocl_utilities_PredefinedType_getName():
    assert ocl_utilities_PredefinedType.getName(ocl_utilities_PredefinedType()) == None

def test_ocl_utilities_PredefinedType_oclOperations():
    assert ocl_utilities_PredefinedType.oclOperations(ocl_utilities_PredefinedType()) == None


from python_code import ocl_utilities_TypedASTNode

def test_ocl_utilities_TypedASTNode___init__():
    assert ocl_utilities_TypedASTNode.__init__(ocl_utilities_TypedASTNode(0, 0), 0, 0) == None


from python_code import ocl_utilities_TypedElement

def test_ocl_utilities_TypedElement___init__():
    assert ocl_utilities_TypedElement.__init__(ocl_utilities_TypedElement()) == None

def test_ocl_utilities_TypedElement_getType():
    assert ocl_utilities_TypedElement.getType(ocl_utilities_TypedElement()) == None

def test_ocl_utilities_TypedElement_setType():
    assert ocl_utilities_TypedElement.setType(ocl_utilities_TypedElement(), '') == None

def test_ocl_utilities_TypedElement_setName():
    assert ocl_utilities_TypedElement.setName(ocl_utilities_TypedElement(), '') == None

def test_ocl_utilities_TypedElement_getName():
    assert ocl_utilities_TypedElement.getName(ocl_utilities_TypedElement()) == None


from python_code import ocl_utilities_Visitable

def test_ocl_utilities_Visitable___init__():
    assert ocl_utilities_Visitable.__init__(ocl_utilities_Visitable()) == None

def test_ocl_utilities_Visitable_accept():
    assert ocl_utilities_Visitable.accept(ocl_utilities_Visitable(), '') == None


from python_code import ocl_utilities_Visitor

def test_ocl_utilities_Visitor___init__():
    assert ocl_utilities_Visitor.__init__(ocl_utilities_Visitor()) == None

def test_ocl_utilities_Visitor_visitEnumLiteralExp():
    assert ocl_utilities_Visitor.visitEnumLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitIteratorExp():
    assert ocl_utilities_Visitor.visitIteratorExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitConstraint():
    assert ocl_utilities_Visitor.visitConstraint(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitVariableExp():
    assert ocl_utilities_Visitor.visitVariableExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitOperationCallExp():
    assert ocl_utilities_Visitor.visitOperationCallExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitMessageExp():
    assert ocl_utilities_Visitor.visitMessageExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitIterateExp():
    assert ocl_utilities_Visitor.visitIterateExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitCollectionLiteralExp():
    assert ocl_utilities_Visitor.visitCollectionLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitLetExp():
    assert ocl_utilities_Visitor.visitLetExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitUnlimitedNaturalLiteralExp():
    assert ocl_utilities_Visitor.visitUnlimitedNaturalLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitTypeExp():
    assert ocl_utilities_Visitor.visitTypeExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitTupleLiteralExp():
    assert ocl_utilities_Visitor.visitTupleLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitIfExp():
    assert ocl_utilities_Visitor.visitIfExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitVariable():
    assert ocl_utilities_Visitor.visitVariable(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitStateExp():
    assert ocl_utilities_Visitor.visitStateExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitRealLiteralExp():
    assert ocl_utilities_Visitor.visitRealLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitAssociationClassCallExp():
    assert ocl_utilities_Visitor.visitAssociationClassCallExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitCollectionRange():
    assert ocl_utilities_Visitor.visitCollectionRange(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitNullLiteralExp():
    assert ocl_utilities_Visitor.visitNullLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitStringLiteralExp():
    assert ocl_utilities_Visitor.visitStringLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitUnspecifiedValueExp():
    assert ocl_utilities_Visitor.visitUnspecifiedValueExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitCollectionItem():
    assert ocl_utilities_Visitor.visitCollectionItem(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitInvalidLiteralExp():
    assert ocl_utilities_Visitor.visitInvalidLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitPropertyCallExp():
    assert ocl_utilities_Visitor.visitPropertyCallExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitIntegerLiteralExp():
    assert ocl_utilities_Visitor.visitIntegerLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitTupleLiteralPart():
    assert ocl_utilities_Visitor.visitTupleLiteralPart(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitBooleanLiteralExp():
    assert ocl_utilities_Visitor.visitBooleanLiteralExp(ocl_utilities_Visitor(), '') == None

def test_ocl_utilities_Visitor_visitExpressionInOCL():
    assert ocl_utilities_Visitor.visitExpressionInOCL(ocl_utilities_Visitor(), '') == None

