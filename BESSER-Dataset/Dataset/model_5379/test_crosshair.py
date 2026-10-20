from python_code import html5_button

def test_html5_button___init__():
    assert html5_button.__init__(html5_button(''), '') == None


from python_code import html5_img

def test_html5_img___init__():
    assert html5_img.__init__(html5_img(''), '') == None


from python_code import html5_input

def test_html5_input___init__():
    assert html5_input.__init__(html5_input('', '', '\x00\x00'), '', '', '') == None


from python_code import html5_label

def test_html5_label___init__():
    assert html5_label.__init__(html5_label(''), '') == None


from python_code import html5_fieldset
from python_code import html5_legend

def test_html5_legend___init__():
    assert html5_legend.__init__(html5_legend('', '\x00', html5_legend=html5_fieldset()), '\x00\x00', '', html5_legend=html5_fieldset()) == None


from python_code import html5_option
from python_code import html5_select_multiple

def test_html5_select_multiple___init__():
    assert html5_select_multiple.__init__(html5_select_multiple('', html5_select_multiple=html5_option()), '', html5_select_multiple=html5_option()) == None

