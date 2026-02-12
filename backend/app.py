from flask import Flask, request, render_template_string
import threading
import time

app = Flask(__name__)

monitored_urls = []

HTML = """
<!doctype html>
<title>Open Visual Monitor</title>
<h1>Open Visual Monitor</h1>
<form method="post">
  <input name="url" placeholder="https://example.com" required>
  <button>Add</button>
</form>
<ul>
{% for url in urls %}
  <li>{{ url }}</li>
{% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        monitored_urls.append(request.form["url"])
    return render_template_string(HTML, urls=monitored_urls)

def monitor_loop():
    while True:
        for url in monitored_urls:
            print("Monitoring:", url)
        time.sleep(30)

if __name__ == "__main__":
    threading.Thread(target=monitor_loop, daemon=True).start()
    app.run(host="0.0.0.0", port=5000)
