from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """Return index page"""
    return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Return page with application form"""
    open_jobs = {"software_engineer": "Software Engineer",
                 "qa_engineer": "QA Engineer",
                 "data_scientist": "Data Scientist",
                 "software_architect": "Software Architect",
                 "product_manager": "Product Manager"
                 }

    return render_template("/application-form.html", open_jobs=open_jobs)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
