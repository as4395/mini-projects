from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

# Vulnerable XSS endpoint: reflects user input without sanitization
@app.route('/xss')
def xss():
    user_input = request.args.get('input', '')
    # Unsafe rendering of user input directly into the page
    html = f"""
    <h1>XSS Demo</h1>
    <p>User input: {user_input}</p>
    <form action="/xss" method="get">
      <input type="text" name="input" placeholder="Enter text">
      <input type="submit" value="Submit">
    </form>
    """
    return render_template_string(html)

# Vulnerable CSRF form: updates user email without CSRF protection
user_email = "user@example.com"

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    global user_email
    if request.method == 'POST':
        # No CSRF token verification here - vulnerable to CSRF attack
        user_email = request.form.get('email', user_email)
        return redirect('/profile')
    html = f"""
    <h1>User Profile</h1>
    <p>Current email: {user_email}</p>
    <form action="/profile" method="post">
      <input type="email" name="email" placeholder="New email">
      <input type="submit" value="Update Email">
    </form>
    """
    return render_template_string(html)

# Vulnerable LFI endpoint: includes file based on user input
@app.route('/lfi')
def lfi():
    filename = request.args.get('file', 'default.txt')
    try:
        with open(f'files/{filename}', 'r') as f:
            content = f.read()
    except Exception:
        content = "File not found or inaccessible."
    html = f"""
    <h1>LFI Demo</h1>
    <pre>{content}</pre>
    <form action="/lfi" method="get">
      <input type="text" name="file" placeholder="Enter filename">
      <input type="submit" value="View File">
    </form>
    """
    return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True)
