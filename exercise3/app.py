from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#Dictionary to store users
users = {}

#List of organizations
organizations = ['Charlotte Hack', 'Association of Computing Machinery', '49th Security Division', 'Girls Who Code', 'Game Developers']

#Route for homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #Get user input from the registration from
        name = request.form.get('name')
        org = request.form.get('organization')
        
        #Require both name and organization fields
        if not name or not org:
            #Error message
            err = "Name and Organization are required fields"
            return render_template('index.html', organizations=organizations, err=err)
        
        #Only allow the user to choose hardcoded organizations
        if org not in organizations:
            #Error message
            err = "This organization is invalid"
            return render_template('index.html', organizations=organizations, err=err)
        
        #store users name and organization as a key-value pair
        users[name] = org

        #Redirects the user to registrants page
        return redirect('/registrants')
    #Renders the homepage with the organzations
    return render_template('index.html', organizations=organizations)

#Route for registrants page
@app.route('/registrants')
def registrants():
    #Renders the registrants page with the registered users
    return render_template('registrants.html', users=users)

if __name__ == '__main__':
    #Starts the app
    app.run(debug=True)