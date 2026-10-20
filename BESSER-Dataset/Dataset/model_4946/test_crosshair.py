from python_code import form_AbstractTable
from python_code import form_Expression
from python_code import form_TableExpression

def test_form_AbstractTable___init__():
    assert form_AbstractTable.__init__(form_AbstractTable(False, True, False, False, False, False, False, form_AbstractTable=form_Expression(), form_AbstractTable105=form_Expression(), form_AbstractTable108=form_TableExpression()), False, False, False, False, False, False, False, form_AbstractTable=form_Expression(), form_AbstractTable105=form_Expression(), form_AbstractTable108=form_TableExpression()) == None


from python_code import form_DateFormField

def test_form_DateFormField___init__():
    assert form_DateFormField.__init__(form_DateFormField('', '\x00'), '\x00\x00', '') == None


from python_code import form_Duplicable
from python_code import form_Expression

def test_form_Duplicable___init__():
    assert form_Duplicable.__init__(form_Duplicable(False, False, False, form_Duplicable=form_Expression(), form_Duplicable23=form_Expression(), form_Duplicable26=form_Expression(), form_Duplicable29=form_Expression(), form_Duplicable32=form_Expression(), form_Duplicable35=form_Expression()), False, False, False, form_Duplicable=form_Expression(), form_Duplicable23=form_Expression(), form_Duplicable26=form_Expression(), form_Duplicable29=form_Expression(), form_Duplicable32=form_Expression(), form_Duplicable35=form_Expression()) == None


from python_code import form_DurationFormField

def test_form_DurationFormField___init__():
    assert form_DurationFormField.__init__(form_DurationFormField('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import form_DynamicTable
from python_code import form_Expression

def test_form_DynamicTable___init__():
    assert form_DynamicTable.__init__(form_DynamicTable(False, False, False, True, False, False, form_DynamicTable=form_Expression(), form_DynamicTable120=form_Expression(), form_DynamicTable123=form_Expression(), form_DynamicTable126=form_Expression()), False, False, False, False, False, False, form_DynamicTable=form_Expression(), form_DynamicTable120=form_Expression(), form_DynamicTable123=form_Expression(), form_DynamicTable126=form_Expression()) == None


from python_code import form_Document
from python_code import form_Expression
from python_code import form_FileWidget

def test_form_FileWidget___init__():
    assert form_FileWidget.__init__(form_FileWidget('', '', False, False, '', '', False, '', form_FileWidget=form_Document(), form_FileWidget95=form_Expression()), '', '', False, False, '', '', False, '', form_FileWidget=form_Document(), form_FileWidget95=form_Expression()) == None


from python_code import form_FormButton

def test_form_FormButton___init__():
    assert form_FormButton.__init__(form_FormButton(''), '') == None


from python_code import form_Expression
from python_code import form_FormField

def test_form_FormField___init__():
    assert form_FormField.__init__(form_FormField('', '\x00', form_FormField=form_Expression()), '\x00\x00', '', form_FormField=form_Expression()) == None


from python_code import form_Document
from python_code import form_Expression
from python_code import form_ImageWidget

def test_form_ImageWidget___init__():
    assert form_ImageWidget.__init__(form_ImageWidget(True, form_ImageWidget=form_Document(), form_ImageWidget100=form_Expression()), False, form_ImageWidget=form_Document(), form_ImageWidget100=form_Expression()) == None


from python_code import form_ItemContainer

def test_form_ItemContainer___init__():
    assert form_ItemContainer.__init__(form_ItemContainer(''), '') == None


from python_code import form_ListFormField

def test_form_ListFormField___init__():
    assert form_ListFormField.__init__(form_ListFormField(0), 0) == None


from python_code import form_PasswordFormField

def test_form_PasswordFormField___init__():
    assert form_PasswordFormField.__init__(form_PasswordFormField(0), 0) == None


from python_code import form_SuggestBox

def test_form_SuggestBox___init__():
    assert form_SuggestBox.__init__(form_SuggestBox(0, False, False, 0), 0, False, False, 0) == None


from python_code import form_Expression
from python_code import form_Table

def test_form_Table___init__():
    assert form_Table.__init__(form_Table(False, False, False, form_Table115=form_Expression(), form_Table=form_Expression(), form_Table112=form_Expression()), False, False, False, form_Table115=form_Expression(), form_Table=form_Expression(), form_Table112=form_Expression()) == None


from python_code import form_TextAreaFormField

def test_form_TextAreaFormField___init__():
    assert form_TextAreaFormField.__init__(form_TextAreaFormField(0, 0), 0, 0) == None


from python_code import form_TextFormField

def test_form_TextFormField___init__():
    assert form_TextFormField.__init__(form_TextFormField(0), 0) == None


from python_code import form_Validable

def test_form_Validable___init__():
    assert form_Validable.__init__(form_Validable('\x00\x00', False, form_Validable=set()), '', True, form_Validable=set()) == None

