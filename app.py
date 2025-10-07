from flask import Flask, jsonify, redirect, render_template, request, url_for
from weather_report import get_weather_report

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route("/weather/<city>")
def find_weather(city):
    report = get_weather_report(city)
    return render_template('result.html', results=report)

@app.route('/result', methods=['GET', 'POST'])
def show_result():
    if request.method=='POST':
        current_city = request.form['city']
    else:
        return render_template('home.html')
    return redirect(url_for('find_weather', city=str(current_city)))


if __name__ == '__main__':
    app.run(debug=True, port=5001)

