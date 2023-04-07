from flask import Flask, render_template, request, jsonify
#from database import add_into_file

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route("/")
def index():
  return render_template('form.html')

@app.route("/form/results", methods=['post'])
def submit_page():
  data = request.args
  return jsonify(data)

""""
@app.route('/1')
def page_1():
  return render_template('test1.html')


@app.route('/2')
def page_2():
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
"""
  #add_into_file(data)
  #return render_template('results.html', data=data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
