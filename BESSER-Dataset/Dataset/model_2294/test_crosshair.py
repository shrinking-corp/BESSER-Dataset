from python_code import scheduleOfCourse_CourseLoad
from python_code import scheduleOfCourse_scheduleOfCourse

def test_scheduleOfCourse_CourseLoad___init__():
    assert scheduleOfCourse_CourseLoad.__init__(scheduleOfCourse_CourseLoad('', 0, 0, scheduleOfCourse_CourseLoad=scheduleOfCourse_scheduleOfCourse()), '\x00', 0, 0, scheduleOfCourse_CourseLoad=scheduleOfCourse_scheduleOfCourse()) == None


from python_code import scheduleOfCourse_LessonPeriod
from python_code import scheduleOfCourse_scheduleOfCourse

def test_scheduleOfCourse_LessonPeriod___init__():
    assert scheduleOfCourse_LessonPeriod.__init__(scheduleOfCourse_LessonPeriod('', '\x00', scheduleOfCourse_LessonPeriod=scheduleOfCourse_scheduleOfCourse()), '\x00\x00', '', scheduleOfCourse_LessonPeriod=scheduleOfCourse_scheduleOfCourse()) == None

