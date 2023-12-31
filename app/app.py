from flask import Flask, render_template, abort
import pandas as pd
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Load environment variables from .env file
load_dotenv()

# Configure Sentry
sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),  # Use environment variable for Sentry DSN
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

# Update the dataset_path to the raw GitHub URL
dataset_path = 'https://raw.githubusercontent.com/Jannath19/flask_e2e_project/main/data/Pregnancy-Associated-Mortality-Cleaned.csv'

# Load the dataset
df = pd.read_csv(dataset_path)

# Index route
@app.route('/')
def index():
    return render_template('index.html', message='Welcome to Pregnancy-Associated Mortality Web App!', dataset=df.to_html(index=False))

# About route (you can modify this if needed)
@app.route('/about')
def about():
    return render_template('about.html')

# Dataset route
@app.route('/dataset')
def dataset():
    return render_template('dataset.html', dataset=df.to_html(index=False))

# Trigger error route
@app.route('/trigger-error')
def trigger_error():
    # Intentionally raise an exception
    raise Exception("This is a test exception")

if __name__ == '__main__':
    app.run(debug=True)
