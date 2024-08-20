from flask import Flask, render_template, request, json
import model
# in order to access anything from model

app = Flask(__name__)

# Main Page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/createAccount')
def createAccount():
    return render_template('create_account.html')

@app.route('/getCreateAccount', methods=['GET', 'POST'])
def getCreateAccount():
    # Collect the variables that will be used to create a student/account
    name = request.form['name']
    password = request.form['password']
    net_worth = request.form['net_worth']
    debt_amount = request.form['debt_amount']
    time_to_payment = request.form['time_to_payment']
    user = model.Student(name, password,float(net_worth), float(debt_amount), float(time_to_payment))
    # The following will be used to store information
    user.store_info()
    props = {
        "name" : name,
        "id" : user.id,
        "password" : password,
        "net_worth" : net_worth,
        "debt_amount" : debt_amount,
        "time_to_payment" : time_to_payment,
        "passowrd" : password,
    }
    return render_template('temp.html', props=props)

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/login')
def goToLogin():
    return render_template('login.html')

@app.route('/checkLogin', methods=['GET', 'POST'])
def checkLogin():
    id = request.form['id']
    password = request.form['password']
    # ... (Logic to check login credentials)
    student_data = {}
    with open("student_data.json", "r") as file:
      student_data = json.load(file)
    if id in student_data['student_accounts'] and password == student_data['student_accounts'][id]['password']:
        return render_template('results.html') # Return a response, e.g., a template
    else:
        return render_template('error.html')

@app.route('/results')
def result():
    return render_template('results.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


@app.route('/results/') 
def results(): 
    payment_plans = [
        {
            "Fixed Plans": {
                "Standard": "Payments are a fixed amount that ensures your loans are paid off within 10 years (within 10 to 30 years for Consolidation Loans).",
                "Graduated": "Payments are lower at first and then increase, usually every two years. Payment amounts are designed to ensure your loans are paid off within 10 years (within 10 to 30 years for Consolidation Loans).",
                "Extended": "Payments can be fixed or graduated and will ensure that your loans are paid off within 25 years."
            }
        },
        {
            "Income Driven Repayment": {
                "SAVE Plan": "10% of discretionary income.",
                "IBR Plan": "Either 10% or 15% of your discretionary income (depending on when you received your first loans) but never more than what you would pay under the 10-year Standard Repayment Plan.",
                "ICR Plan": "20% of your discretionary income, or the amount you would pay on a repayment plan with a fixed payment over 12 years, adjusted according to your income."
            }
        }
    ]
    return render_template('results.html', payment_plans=payment_plans)