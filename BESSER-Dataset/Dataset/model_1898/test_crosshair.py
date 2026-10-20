from python_code import emig_DotNavigationObjDX
from python_code import emig_DotNavigationObjSX
from python_code import emig_FilterMigrator
from python_code import emig_MigratorDX
from python_code import emig_MigratorSX

def test_emig_FilterMigrator___init__():
    assert emig_FilterMigrator.__init__(emig_FilterMigrator('', emig_FilterMigrator=emig_MigratorSX(), emig_FilterMigrator60=emig_MigratorDX(), emig_FilterMigrator64=emig_DotNavigationObjSX(), emig_FilterMigrator66=emig_DotNavigationObjDX()), '', emig_FilterMigrator=emig_MigratorSX(), emig_FilterMigrator60=emig_MigratorDX(), emig_FilterMigrator64=emig_DotNavigationObjSX(), emig_FilterMigrator66=emig_DotNavigationObjDX()) == None


from python_code import emig_LocatedElement

def test_emig_LocatedElement___init__():
    assert emig_LocatedElement.__init__(emig_LocatedElement(0, 0, 0, 0), 0, 0, 0, 0) == None


from python_code import emig_MigrationLibrary
from python_code import emig_MyModel

def test_emig_MigrationLibrary___init__():
    assert emig_MigrationLibrary.__init__(emig_MigrationLibrary('', emig_MigrationLibrary=emig_MyModel(), emig_MigrationLibrary4=set()), '', emig_MigrationLibrary=emig_MyModel(), emig_MigrationLibrary4=set()) == None


from python_code import emig_Migrator

def test_emig_Migrator___init__():
    assert emig_Migrator.__init__(emig_Migrator(''), '') == None

