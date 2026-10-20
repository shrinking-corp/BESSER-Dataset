from python_code import Add_notes
from python_code import Home_page

def test_Add_notes___init__():
    assert Add_notes.__init__(Add_notes(0, '', '\x00\x00', home_page9=Home_page()), 0, '', '', home_page9=Home_page()) == None


from python_code import Course
from python_code import Home_page

def test_Course___init__():
    assert Course.__init__(Course('', '', '', 0, '\x00', 0, '', '', 0, home_page7=Home_page()), '', '', '', 0, '', 0, '', '', 0, home_page7=Home_page()) == None


from python_code import Home_page
from python_code import Show_all_grades

def test_Show_all_grades___init__():
    assert Show_all_grades.__init__(Show_all_grades(0, '', '', '', '', '', home_page5=Home_page()), 0, '', '', '', '\x00', '', home_page5=Home_page()) == None

