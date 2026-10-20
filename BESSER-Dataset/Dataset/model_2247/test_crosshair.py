from python_code import courses_CourseHour
from python_code import courses_Timetable

def test_courses_CourseHour___init__():
    assert courses_CourseHour.__init__(courses_CourseHour('', '', '', '', '', courses_CourseHour46=set(), courses_CourseHour=courses_Timetable()), '', '', '', '\x00', '', courses_CourseHour46=set(), courses_CourseHour=courses_Timetable()) == None


from python_code import courses_CourseInstance
from python_code import courses_Coursework

def test_courses_Coursework___init__():
    assert courses_Coursework.__init__(courses_Coursework(0, '', 0, 0, 0, '', '', courses_Coursework=courses_CourseInstance()), 0, '\x00', 0, 0, 0, '', '', courses_Coursework=courses_CourseInstance()) == None


from python_code import courses_Content
from python_code import courses_ExaminationArrangement

def test_courses_ExaminationArrangement___init__():
    assert courses_ExaminationArrangement.__init__(courses_ExaminationArrangement('\x00\x00', '', courses_ExaminationArrangement35=set(), courses_ExaminationArrangement=courses_Content()), '', '', courses_ExaminationArrangement35=set(), courses_ExaminationArrangement=courses_Content()) == None


from python_code import courses_Content
from python_code import courses_Paragraph

def test_courses_Paragraph___init__():
    assert courses_Paragraph.__init__(courses_Paragraph('', '\x00', courses_Paragraph=courses_Content()), '\x00\x00', '', courses_Paragraph=courses_Content()) == None

