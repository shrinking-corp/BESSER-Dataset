# PUML conversion: losslessness check

Generated: 2026-10-18T18:33:26.565705+00:00

- **Models checked:** 9082
- **Lossless (every BUML fact in the PUML, nothing extra):** 9082
- **Unsupported BUML constructs found:** none

## Breakdown by status

| Status | Count |
|---|---|
| lossless | 9082 |

## Source definitions that never reach the model (defect of the source dataset)

1732 string literals in 222 models sit in BUML statements whose value is never read before being overwritten, or never read at all (overloaded methods assigned to the same variable twice). The model loaded from the BUML doesn't contain them, so the PUML can't either; they are not counted as conversion losses.

- **model_100061:** aggregator_InstallableUnitRequest_m_resolveAsSingleton: Method(name='resolveAsSingleton')
- **model_100065:** aggregator_InstallableUnitRequest_m_resolveAsSingleton: Method(name='resolveAsSingleton')
- **model_100075:** build_UnitProvider_m_resolve: Method(name='resolve'); build_UnitProvider_m_resolve: Parameter(name='build_requiredCapability'); build_UnitProvider_m_resolve: Parameter(name='build_ctx')
- **model_100128:** db_Query_m_getParameter: Method(name='getParameter'); db_Query_m_getParameter: Parameter(name='db_name')
- **model_100129:** core_CatalogContainer_m_createConnection: Method(name='createConnection'); core_CatalogContainer_m_createConnection: Parameter(name='core_factory'); core_Connection_m_createStatement: Method(name='createStatement')
- **model_100130:** core_CatalogContainer_m_createConnection: Method(name='createConnection'); core_CatalogContainer_m_createConnection: Parameter(name='core_factory'); core_CatalogMetaData_m_getTable: Method(name='getTable')
- **model_100133:** syntax_BindingParser_m_parseBinding: Method(name='parseBinding'); syntax_BindingParser_m_parseBinding: Parameter(name='syntax_stream'); syntax_DefinitionParser_m_parseDefinition: Method(name='parseDefinition')
- **model_100134:** syntax_BindingParser_m_parseBinding: Method(name='parseBinding'); syntax_BindingParser_m_parseBinding: Parameter(name='syntax_stream'); syntax_DefinitionParser_m_parseDefinition: Method(name='parseDefinition')
- **model_10024:** RandL_LoyaltyProgram_m_getServices: Method(name='getServices'); RandL_LoyaltyProgram_m_getServices: Parameter(name='RandL_pp')
- **model_100242:** spreadsheet_Spreadsheet_m_getSheet: Method(name='getSheet'); spreadsheet_Spreadsheet_m_getSheet: Parameter(name='spreadsheet_sheetindex'); spreadsheet_Row_m_getCell: Method(name='getCell')
- **model_100243:** spreadsheet_Spreadsheet_m_getSheet: Method(name='getSheet'); spreadsheet_Spreadsheet_m_getSheet: Parameter(name='spreadsheet_sheetname'); spreadsheet_Row_m_getCell: Method(name='getCell')
- **model_100253:** table_DTableElementSynchronizer_m_refresh: Method(name='refresh'); table_DTableElementSynchronizer_m_refresh: Parameter(name='table_cell'); table_DTableElementSynchronizer_m_refresh: Method(name='refresh')
- **model_100254:** table_DTableElementSynchronizer_m_refresh: Method(name='refresh'); table_DTableElementSynchronizer_m_refresh: Parameter(name='table_cell'); table_DTableElementSynchronizer_m_refresh: Method(name='refresh')
- **model_10042:** xtend_JvmTypeReference_m_getQualifiedName: Method(name='getQualifiedName'); xtend_JvmIdentifiableElement_m_getQualifiedName: Method(name='getQualifiedName'); xtend_JvmTypeConstraint_m_getQualifiedName: Method(name='getQualifiedName')
- **model_100438:** statemachine_StateMachine_m_accessibleStates: Method(name='accessibleStates'); statemachine_StateMachine_m_accessibleStates: Method(name='accessibleStates'); statemachine_StateMachine_m_accessibleStates: Parameter(name='statemachine_states')

Full per-model detail: see the accompanying `.json` report.
