from flask import Flask, request, render_template, redirect, url_for
from calculate import compare

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Welcome to Chem Tools.</h1><br>
    <h2>Directions</h2>
    <p>
    - Enter the desired total sum (ex. 16.41)<br>
    - Enter the desired error (ex. for 1 percent error, enter 0.01)<br>
    - Enter the individual parts, separated by a space (ex. 12.33 12.33 9.443 3.9 4)<br>
    <br>
    When you click "Submit" the program will attempt to find all possible combinations of parts that make the total sum, within the desired error.<br>
    <br>
    For example, if you input:<br>
    - Total Sum = 16.41<br>
    - Error = 0.01<br>
    - Parts = 12.33 12.33 9.443 3.9 4<br>
    The program will try all combinations of "Parts" that sum to 16.41, within 1 percent error (16.2459 to 16.5741)<br>
    <br>
    </p>
    
    <h2>Your Inputs</h2><br>
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
        return '''
    <h1>Error: Please double-check that your inputs are valid.</h1>
    
    <h2>Directions</h2><br>
    - Enter the desired total sum (ex. 16.41)<br>
    - Enter the desired error (ex. for 1 percent error, enter 0.01)<br>
    - Enter the individual parts, separated by a space (ex. 12.33 12.33 9.443 3.9 4)<br>
    <br>
    
    <form action="/" method="get">
        <input type="submit" value="Go back">
    </form>
    '''

    # Pass the submitted values to the confirmation page
    return render_template('confirm.html', num1=num1, num2=num2, num3_list=num3_list)

@app.route('/confirm', methods=['POST'])
def confirm():
    # Handle the confirmation form submission
    user_response = request.form['confirmation']
    
    if user_response == 'edit':
        # Redirect back to the form if user wants to edit
        return redirect(url_for('index'))
    elif user_response == 'confirm':
        # Redirect to the final page if user confirms
        return redirect(url_for('final', num1=request.form['num1'], num2=request.form['num2'], num3_list=request.form['num3_list']))

@app.route('/final')
def final():
    # Get values from query string (passed from confirmation page)
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    num3_list = [float(x) for x in list(request.args.get('num3_list'))]

    # Call the function with the values
    final_vals = compare(num1, num2, num3_list)

    # Display the final values
    return f'''
    <h1>Final Values:</h1>
    {final_vals}</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)