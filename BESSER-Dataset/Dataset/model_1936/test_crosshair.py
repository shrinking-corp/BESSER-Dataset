from python_code import emig_MigrationLibrary
from python_code import emig_MyModel

def test_emig_MigrationLibrary___init__():
    assert emig_MigrationLibrary.__init__(emig_MigrationLibrary('', emig_MigrationLibrary=emig_MyModel(), emig_MigrationLibrary4=set()), '', emig_MigrationLibrary=emig_MyModel(), emig_MigrationLibrary4=set()) == None


from python_code import emig_EClass
from python_code import emig_MigratorDX
from python_code import emig_RewritingRule

def test_emig_MigratorDX___init__():
    assert emig_MigratorDX.__init__(emig_MigratorDX('', emig_MigratorDX63=emig_EClass(), emig_MigratorDX66=set(), emig_MigratorDX=emig_RewritingRule()), '', emig_MigratorDX63=emig_EClass(), emig_MigratorDX66=set(), emig_MigratorDX=emig_RewritingRule()) == None

