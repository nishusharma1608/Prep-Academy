from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3 as sql


app = Flask(__name__)
# app._static_folder = "/static"

conn = sql.connect("project.db")
cur = conn.cursor()

@app.route("/")
def home():
	return render_template("homepage.html", errors = "")

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)
@app.route("/landing_page/<name>")
def landing_page(name):
	conn = sql.connect("project.db")
	# conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT company FROM appearances where RegdNo=(?)",(session['username'],))
	comp_list = cur.fetchall()
	return render_template("landing_page.html", name = name , rows=comp_list)

@app.route("/login", methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		user = request.form['Regd.No.']
		pwd = request.form['Password']
	errors = ""

	conn = sql.connect("project.db")
	# conn.row_factory = sql.Row
	cur = conn.cursor()
	cur.execute("SELECT name, password FROM students where RegdNo=(?)",(user,))
	res = cur.fetchall()
	if (len(res) == 0):
		errors = "Username does not exist"
		return render_template('homepage.html', errors = errors)
	else:
		if (res[0][1] != pwd):
			errors = "Invalid Password"
			return render_template("homepage.html", errors = errors)

	session['username']=user
	return redirect(url_for("landing_page", name = res[0][0]))

@app.route("/company/<name>/")
def render_company(name):
	session['company'] = name
	conn = sql.connect("project.db")
	cur = conn.cursor()
	cur.execute("SELECT name FROM students where RegdNo=?",(session['username'],))
	user_name = cur.fetchone()
	cur.execute("SELECT requirement FROM company where name=(?)",(name,))
	sub_list = cur.fetchall()

	session['company'] = name
	return render_template("company.html", company = name, name = user_name[0], subs = sub_list)


@app.route("/company/<company>/<subject>/")
def subjects(company,subject):
	session.pop('sub', None)

	conn = sql.connect("project.db")
	cur = conn.cursor()
	cur.execute("SELECT name FROM students where RegdNo=(?)",(session['username'],))
	user_name = cur.fetchone()
	cur.execute("SELECT requirement FROM company where name=(?)",(company,))
	sub_list = cur.fetchall()
	details=subject

	session['sub'] = subject
	return render_template("company.html", company = company , name = user_name[0], subs=sub_list , details = details)


@app.route("/signout")
def signout():
	session.pop('username', None)
	session.pop('company', None)
	session.pop('sub', None)
	return redirect(url_for("home"))

@app.route("/submit/")
def submit():
	# cur.execute("SELECT name FROM students where RegdNo in (?,?)",(session['username'], session['username']))
	# user_name = cur.fetchone()
	conn = sql.connect("project.db")
	cur = conn.cursor()
	# cur.execute("SELECT name FROM students where RegdNo in (?,?)",(session['username'], session['username']))
	# return render_template("submit.html")
	return render_template("submit.html", company = session['company'] , name = session['username'])

if __name__ == "__main__":
	app.secret_key = "ac234-hjkjll6-5656gfgt-656dte"
	app.run(debug = True)
