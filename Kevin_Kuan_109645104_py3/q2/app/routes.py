from flask import Flask, render_template, redirect, url_for
from forms import SubmissionForm
result=0
# from text_form import SubmissionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'


@app.route('/')
def default():
	return redirect(url_for('index'))
@app.route('/index',methods=['GET', 'POST'])
def index():
	global result
	form = SubmissionForm()
	if form.validate_on_submit():
		try:
			test_op1=float(form.operand1.data)
		except ValueError:
			return redirect(url_for('input_error'))
		try:
			test_op2=float(form.operand2.data)
		except ValueError:
			return redirect(url_for('input_error'))
			
		op1=float(form.operand1.data)
		op2=float(form.operand2.data)
		operator=(form.operator.data)


		if operator=="add":
			result= op1+op2
			return redirect(url_for('add'))

		elif operator=="subtract":
			result= op1-op2
			return redirect(url_for('subtract'))

		elif operator=="multiply":
			result= op1*op2
			return redirect(url_for('multiply'))

		else:
			if op2 == float(0):
				return redirect(url_for('divide_by_zero'))
			result= op1/op2		
			return redirect(url_for('divide'))

	return render_template("index.html",title="Form", form=form)

@app.route("/result/add")
def add():
	global result
	return render_template('result.html',result=result)

@app.route("/result/subtract")
def subtract():
	global result
	return render_template('result.html',result=result)

@app.route("/result/multiply")
def multiply():
	global result	
	return render_template('result.html',result=result)

@app.route("/result/divide")
def divide():
	global result	
	return render_template('result.html',result=result)

@app.route("/result/error")
def input_error():
    return render_template('error.html')

@app.route("/result/divide_by_zero")
def divide_by_zero():
	return render_template("divide_by_zero.html")
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

@app.errorhandler(500)
def not_found_error(error):
	return render_template('500.html'), 500

@app.errorhandler(403)
def not_found_error(error):
	return render_template('403.html'), 403

if __name__ == '__main__':
	app.run()
