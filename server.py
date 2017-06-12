from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE

@app.route('/')
def start_homepage():
	"""Goes to homepage"""

	return render_template("index.html")


@app.route('/application-form')
def show_application():
	""" application"""	

	return render_template("application-form.html")
						

@app.route('/application-success', methods=["POST"])
def completed_app():
	"""Submitted appication"""
	
	firstname = request.form.get("firstname")
	lastname = request.form.get("lastname")
	salaryreq = "{:,.2f}".format(float(request.form.get("salaryreq")))
	jobtitle = request.form.get("jobtitle")

	return render_template("application-response.html",
							firstname=firstname,
							lastname=lastname,
							salaryreq=salaryreq,
							jobtitle=jobtitle)



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

