from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, TextField
from wtforms.validators import DataRequired


class SubmissionForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = StringField('Text', validators=[DataRequired()])

    operand1 = IntegerField('First number', validators=[DataRequired()])
    operand2 = IntegerField('Second number', validators=[DataRequired()])
    submit = SubmitField('Submit Entry')
