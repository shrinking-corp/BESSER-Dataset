from python_code import research_team_CallForPaper

def test_research_team_CallForPaper___init__():
    assert research_team_CallForPaper.__init__(research_team_CallForPaper('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import research_team_Section

def test_research_team_Section___init__():
    assert research_team_Section.__init__(research_team_Section(''), '') == None


from python_code import research_team_TypeCollaboration

def test_research_team_TypeCollaboration___init__():
    assert research_team_TypeCollaboration.__init__(research_team_TypeCollaboration(''), '') == None

