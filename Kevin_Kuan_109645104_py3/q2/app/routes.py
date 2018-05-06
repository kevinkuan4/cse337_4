from flask import Flask, render_template, redirect
from forms import SubmissionForm

# from text_form import SubmissionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'




@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def index():
	form = SubmissionForm()
	if form.validate_on_submit():
		return redirect(url_for('index'))


	return render_template("index.html",title="Form", form=form)

@app.route("/result/add")
def add():
	return "Add!"

@app.route("/result/subtract")
def subtract():
	return "Subtract!"

@app.route("/result/multiply")
def multiply():
	return "Multiply!"

@app.route("/result/divide")
def divide():
	return "Divide!"

@app.route("/result/error")
def input_error():
	return "Invalid numbers!"

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
