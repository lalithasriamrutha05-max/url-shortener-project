from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_database = {}

# GenAI function
def suggest_short_name(url):
    if "youtube" in url:
        return ["video-link", "youtube-video"]
    elif "amazon" in url:
        return ["shopping-link", "amazon-deal"]
    else:
        return ["my-link", "quick-link"]

def generate_code():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )

@app.route('/', methods=['GET', 'POST'])
def home():

    short_url = ""

    if request.method == 'POST':
        original_url = request.form['url']

        code = generate_code()

        url_database[code] = original_url

        short_url = request.host_url + code

    return render_template(
        'index.html',
        short_url=short_url
    )

@app.route('/<code>')
def redirect_url(code):

    if code in url_database:
        return redirect(url_database[code])

    return "URL Not Found"

if __name__ == "__main__":
    app.run(debug=True)