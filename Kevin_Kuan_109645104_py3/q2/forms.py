from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, StringField, TextField, DecimalField, RadioField
from wtforms.validators import DataRequired



class SubmissionForm(FlaskForm):
  
    operand1 = StringField('First number', validators=[DataRequired()])
    operand2 = StringField('Second number', validators=[DataRequired()])
    operator = RadioField('Operator', choices=[('add','Add'),('subtract','Subtract'),('multiply','Multiply'),('divide','Divide')])
    submit = SubmitField('Calculate')
