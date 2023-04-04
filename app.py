from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "ASDN23483N5JN34693M2450J46345345M3J45N354M"

friends_dict = [
    {}
]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template(
        "about.html", pageTitle="About Page", friends=friends_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        fname = form["fname"]
        classroom = form["classroom"]
        icecream = form["icecream"]
        sports = form.getlist("sports")  # this is a PYthon list

        print(fname)
        print(classroom)
        print(icecream)
        print(sports)

        activities_string = ", ".join(sports)  # make the Python list into a string

        friend_dict = {
            "name": fname,
            "classroom": classroom,
            "icecream": icecream,
            "sports": activities_string,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)
        flash('Record successfully added.', 'success')
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
