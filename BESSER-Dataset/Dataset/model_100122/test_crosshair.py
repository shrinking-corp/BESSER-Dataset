from python_code import datasetload_DataSourceJdbc

def test_datasetload_DataSourceJdbc___init__():
    assert datasetload_DataSourceJdbc.__init__(datasetload_DataSourceJdbc('', '', '\x00\x00'), '', '', '') == None

