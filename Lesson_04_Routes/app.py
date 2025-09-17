from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
            <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="/user/alice">User Profile: alice</a></li>
    <li><a href=""></a><li>
    <li><a href=""></a><li>
    <li><a href=""></a><li>
    <li><a href=""></a><li>
    <li><a href=""></a><li>
</ul>
'''

@app.route('/user/<username>', methods=[''])
def user_profile(username):
    return '''
     <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile TypeL {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
    <a href="/">Back to Homepage</a>
    <a href="/user/alice">Alice</a>
    <a href="/user/bob">Bob</a>
 </nav>
'''
@app.route("/calc/<int:num1>/<operation>/<int:num2>")
def calculator(num1, operation, num2):
    operations = {
        '+' : num1 + num2,
        '-' : num1 - num2,
        '*' : num1 * num2,
        '/' : num1 / num2 if num2 !=0 else 'Error: Division by zero!',
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result}"
    else:
        return f"Unknown operation!{operation}"
        
    # return f"{num1} {operation} {num2} = "

@app.route("/temp/<str:unit>/<int:num>")
def conversion(unit, num):
    if unit == "F" or unit == "f":
        result = ((num - 32) * 5/9)
        return f"{num} degrees Fahrenheit = {result} degrees Celsius"
    elif unit == "C" or unit =='c':
        result = (num * 5/9) + 32
        return f"{num} degrees Celsius = {result} degrees Fahrenheit"
    else:
        return "error, enter F or C"

if __name__ == '__main__':
    app.run(debug=True, port=5050)