from python_code import core_CatalogMetaData

def test_core_CatalogMetaData___init__():
    assert core_CatalogMetaData.__init__(core_CatalogMetaData()) == None

def test_core_CatalogMetaData_getIndex():
    assert core_CatalogMetaData.getIndex(core_CatalogMetaData(), '', '', '') == None

def test_core_CatalogMetaData_getView():
    assert core_CatalogMetaData.getView(core_CatalogMetaData(), '', '') == None

def test_core_CatalogMetaData_getSchema():
    assert core_CatalogMetaData.getSchema(core_CatalogMetaData(), '') == None

def test_core_CatalogMetaData_getSchemas():
    assert core_CatalogMetaData.getSchemas(core_CatalogMetaData()) == None

def test_core_CatalogMetaData_getTable():
    assert core_CatalogMetaData.getTable(core_CatalogMetaData(), '', '') == None


from python_code import core_Connection

def test_core_Connection___init__():
    assert core_Connection.__init__(core_Connection()) == None

def test_core_Connection_getCatalog():
    assert core_Connection.getCatalog(core_Connection()) == None

def test_core_Connection_translate():
    assert core_Connection.translate(core_Connection(), '') == None

def test_core_Connection_createStatement():
    assert core_Connection.createStatement(core_Connection(), '', '') == None

def test_core_Connection_close():
    assert core_Connection.close(core_Connection()) == None

def test_core_Connection_getCatalogMetaData():
    assert core_Connection.getCatalogMetaData(core_Connection()) == None

def test_core_Connection_setCatalog():
    assert core_Connection.setCatalog(core_Connection(), '') == None

def test_core_Connection_prepareStatement():
    assert core_Connection.prepareStatement(core_Connection(), '', '', '') == None

def test_core_Connection_getConnectionDescription():
    assert core_Connection.getConnectionDescription(core_Connection()) == None

def test_core_Connection_getCatalogGenerationStrategy():
    assert core_Connection.getCatalogGenerationStrategy(core_Connection()) == None


from python_code import core_ConnectionDescription

def test_core_ConnectionDescription___init__():
    assert core_ConnectionDescription.__init__(core_ConnectionDescription(''), '') == None


from python_code import core_ConnectionManager

def test_core_ConnectionManager___init__():
    assert core_ConnectionManager.__init__(core_ConnectionManager()) == None

def test_core_ConnectionManager_createConnection():
    assert core_ConnectionManager.createConnection(core_ConnectionManager(), '', '', '') == None


from python_code import core_DatabaseManager

def test_core_DatabaseManager___init__():
    assert core_DatabaseManager.__init__(core_DatabaseManager()) == None

def test_core_DatabaseManager_dropTable():
    assert core_DatabaseManager.dropTable(core_DatabaseManager(), '', '') == None

def test_core_DatabaseManager_createTable():
    assert core_DatabaseManager.createTable(core_DatabaseManager(), '', '', '', '') == None

def test_core_DatabaseManager_isStarted():
    assert core_DatabaseManager.isStarted(core_DatabaseManager()) == None

def test_core_DatabaseManager_createView():
    assert core_DatabaseManager.createView(core_DatabaseManager(), '', '', '', '') == None

def test_core_DatabaseManager_start():
    assert core_DatabaseManager.start(core_DatabaseManager(), '') == None

def test_core_DatabaseManager_createSchema():
    assert core_DatabaseManager.createSchema(core_DatabaseManager(), '', '', '') == None

def test_core_DatabaseManager_dropSchema():
    assert core_DatabaseManager.dropSchema(core_DatabaseManager(), '', '', '') == None

def test_core_DatabaseManager_dropView():
    assert core_DatabaseManager.dropView(core_DatabaseManager(), '', '') == None

def test_core_DatabaseManager_createIndex():
    assert core_DatabaseManager.createIndex(core_DatabaseManager(), '', '', '', '') == None

def test_core_DatabaseManager_dropIndex():
    assert core_DatabaseManager.dropIndex(core_DatabaseManager(), '', '') == None


from python_code import core_IndexDef

def test_core_IndexDef___init__():
    assert core_IndexDef.__init__(core_IndexDef(False, False, core_IndexDef=set()), False, False, core_IndexDef=set()) == None


from python_code import core_PreparedStatement

def test_core_PreparedStatement___init__():
    assert core_PreparedStatement.__init__(core_PreparedStatement()) == None

def test_core_PreparedStatement_addBatch():
    assert core_PreparedStatement.addBatch(core_PreparedStatement()) == None

def test_core_PreparedStatement_executeQuery():
    assert core_PreparedStatement.executeQuery(core_PreparedStatement()) == None

def test_core_PreparedStatement_clearParameters():
    assert core_PreparedStatement.clearParameters(core_PreparedStatement()) == None

def test_core_PreparedStatement_execute():
    assert core_PreparedStatement.execute(core_PreparedStatement()) == None

def test_core_PreparedStatement_setString():
    assert core_PreparedStatement.setString(core_PreparedStatement(), '', '') == None

def test_core_PreparedStatement_setInt():
    assert core_PreparedStatement.setInt(core_PreparedStatement(), '', '') == None

def test_core_PreparedStatement_executeUpdate():
    assert core_PreparedStatement.executeUpdate(core_PreparedStatement()) == None


from python_code import core_QualifiedName

def test_core_QualifiedName___init__():
    assert core_QualifiedName.__init__(core_QualifiedName(''), '') == None

def test_core_QualifiedName_getLastQualifier():
    assert core_QualifiedName.getLastQualifier(core_QualifiedName('')) == None

def test_core_QualifiedName_getFirstQualifier():
    assert core_QualifiedName.getFirstQualifier(core_QualifiedName('')) == None


from python_code import core_Statement

def test_core_Statement___init__():
    assert core_Statement.__init__(core_Statement()) == None

def test_core_Statement_addBatch():
    assert core_Statement.addBatch(core_Statement(), '') == None

def test_core_Statement_clearBatch():
    assert core_Statement.clearBatch(core_Statement()) == None

def test_core_Statement_executeUpdate():
    assert core_Statement.executeUpdate(core_Statement(), '') == None

def test_core_Statement_executeBatch():
    assert core_Statement.executeBatch(core_Statement()) == None

def test_core_Statement_close():
    assert core_Statement.close(core_Statement()) == None

def test_core_Statement_executeQuery():
    assert core_Statement.executeQuery(core_Statement(), '') == None

def test_core_Statement_execute():
    assert core_Statement.execute(core_Statement(), '') == None


from python_code import core_TableColumnDef
from python_code import core_TableDef

def test_core_TableColumnDef___init__():
    assert core_TableColumnDef.__init__(core_TableColumnDef('', False, 0, '', False, 0, core_TableColumnDef=core_TableDef()), '', False, 0, '', False, 0, core_TableColumnDef=core_TableDef()) == None


from python_code import core_ViewDef

def test_core_ViewDef___init__():
    assert core_ViewDef.__init__(core_ViewDef(''), '') == None

