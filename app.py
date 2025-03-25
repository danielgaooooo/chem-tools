from flask import Flask, request, render_template
from calculate import main

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    Welcome to Chem Tools.

    Directions:
    - Enter the desired total sum (ex. 16.41)
    - Enter the desired error (ex. for 1 percent error, enter 0.01)
    - Enter the individual parts, separated by a space (ex. 12.33 12.33 9.443 3.9 4)

    When you click "Submit" the program will attempt to find all possible combinations of parts that make the total sum, within the desired error.

    For example, if you input:
    - Total Sum = 16.41
    - Error = 0.01
    - Parts = 12.33 12.33 9.443 3.9 4

    The program will try all combinations of "Parts" that sum to 16.41, within 1 percent error (16.2459 to 16.5741)

    <form action="/submit" method="post">
        <label for="num1">Total Sum:</label>
        <input type="text" id="num1" name="num1"><br><br>

        <label for="num2">Error:</label>
        <input type="text" id="num2" name="num2"><br><br>

        <label for="num3">List of Parts (separate by space):</label>
        <input type="text" id="num3" name="num3"><br><br>

        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Validate the first two inputs as floating point numbers
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        # Validate the third input (list of numbers)
        num3_input = request.form['num3']
        num3_list = [float(x) for x in num3_input.split()]  # Split by spaces and convert to float
    except ValueError:
        return "<h1>Error: Please enter valid numbers!</h1>"

    return f'''
    <h1>Form Submitted!</h1>
    <p>Number 1: {num1}</p>
    <p>Number 2: {num2}</p>
    <p>List of Numbers: {num3_list}</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)