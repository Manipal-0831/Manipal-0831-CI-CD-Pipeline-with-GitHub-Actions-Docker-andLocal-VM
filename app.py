import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # FIX: APP_VERSION is retrieved inside the function, allowing environment
    # variables to be correctly injected during testing and deployment.
    APP_VERSION = os.environ.get("APP_VERSION", "v0.0.0-local")

    return f"""
    <div style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
        <h1 style="color: #10B981;">CI/CD Pipeline Success!</h1>
        <p style="font-size: 1.2em;">This application was deployed from a Docker image built by GitHub Actions.</p>
        <p style="font-size: 1.5em; font-weight: bold; color: #3B82F6;">
            Application Version: {APP_VERSION}
        </p>
        <p>Go check the CI/CD workflow run in your GitHub repository!</p>
    </div>
    """

@app.route('/health')
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
