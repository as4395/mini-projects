import subprocess
from flask import Flask, render_template_string, request, redirect

app = Flask(__name__)

HTML_TEMPLATE = '''
<!doctype html>
<title>Firewall Manager</title>
<h1>Simulated pfSense Firewall</h1>
<form method="post" action="/apply">
    <label>Port to Allow:</label>
    <input type="text" name="allow_port">
    <input type="submit" value="Allow Port">
</form>
<form method="post" action="/flush">
    <input type="submit" value="Flush All Rules">
</form>
<pre>{{ rules }}</pre>
'''

def get_current_rules():
    result = subprocess.run(["iptables", "-L"], capture_output=True, text=True)
    return result.stdout

@app.route("/", methods=["GET"])
def index():
    rules = get_current_rules()
    return render_template_string(HTML_TEMPLATE, rules=rules)

@app.route("/apply", methods=["POST"])
def allow_port():
    port = request.form.get("allow_port")
    if port.isdigit():
        subprocess.run(["iptables", "-A", "INPUT", "-p", "tcp", "--dport", port, "-j", "ACCEPT"])
    return redirect("/")

@app.route("/flush", methods=["POST"])
def flush_rules():
    subprocess.run(["iptables", "-F"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
