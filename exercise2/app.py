from flask import Flask, render_template, request

app = Flask(__name__)

#Route for homepage
@app.route('/')
def index():
    #Renders the home page
    return render_template('index.html')

#Route for calculate page
@app.route('/calculate', methods=['GET'])
def calc():
    #Message that will be displayed on the calculate page
    msg = ""
    if request.method == 'GET':
        #Getting the number input from the html form
        number = request.args['number']
        try:
            #Checks if the number is even or odd
            if int(number) % 2 == 0:
                msg = number + " is even"
            else: 
                msg = number + " is odd"
        except:
            #Checks if a number is provided
            if not number:
                msg = "No number provided"
            else:
                msg = number + " is not an integer"
        #Renders the calculate page
        return render_template('calculate.html', msg = msg)
    
if __name__ == '__main__':
    #Starts the app
    app.run(debug=True)