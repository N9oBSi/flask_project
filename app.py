from flask import Flask, render_template
from controllers.home_controller import home_page, privacy

# app = Flask(__name__)

app = Flask(__name__, static_folder='static')

app.add_url_rule('/', 'home', home_page)
app.add_url_rule('/privacy', 'privacy', privacy)

if __name__ == "__main__":
    app.run(debug=True)