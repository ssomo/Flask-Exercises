from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)

#Route for the homepage
@app.route('/')
def index():
    #Gets the user's current datetime
    time = datetime.now()
    #Renders the homepage
    return render_template('index.html', time=time)

if __name__ == "__main__":
    #Starts the app
    app.run(debug=True)