from flask import Flask, render_template, url_for

#from database import add_into_file

app = Flask(__name__)  # template_folder='templates', static_folder='static')


@app.route("/")
def index():

  return render_template('form.html')


@app.route('/1')
def page_1():

  return render_template('test1.html')


@app.route('/2', methods=["GET", "POST"])
def page_2():
  from flask import request
  if request.method == "POST":
    # jeśli formularz został wysłany, zacznij liczyć czas
    from datetime import time
    start_time = time.time()
    return render_template("test2.html", start_time=start_time)
  else:
      return render_template('test2.html')


@app.route('/3')
def page_3():
  return render_template('test3.html')


@app.route('/4')
def survey():
  return render_template('survey.html')


@app.route('/5')
def results():
  return render_template('results.html')


@app.route("/form/test1", methods=['get'])
def submit_page():
  from flask import request
  data = request.args

  #add_into_file(data)
  return render_template('test1.html', data=data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
