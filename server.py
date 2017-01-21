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
    # job = "software_engineer"
    # print open_jobs[job]

    return render_template("/application-form.html", open_jobs=open_jobs)


@app.route("/application-success", methods=["POST"])
def app_form_confirmation():
    """Return a confirmation of a submitted job application"""
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    #todo: add handling for non-numerical inputs for salary
    salary = float(request.form.get("salary"))
    job = request.form.get("job")
    # print job
    # print type(job)
    return render_template("/application-response.html",
                           first_name=first_name,
                           last_name=last_name,
                           salary=salary,
                           job=job
                           )

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
