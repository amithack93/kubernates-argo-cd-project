from flask import Flask, render_template
import os

# Determine the absolute path to the 'templates' folder
template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# Create a Flask app instance
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', template_folder=template_folder)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)