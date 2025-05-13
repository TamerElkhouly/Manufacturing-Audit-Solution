from flask import Flask
from routes.auth import auth_bp
from routes.functions import functions_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(functions_bp)

if __name__ == "__main__":
    app.run(debug=True)
