from flask import Flask
import csv
# create flask application, initialize secret key, return app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Winston'

    # import views and auth blueprints
    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app 

def random_generate(file_path='website/random_generator.csv'):
    data = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append({"name": row["name"], "age": row["age"], "days": row["days"]})
    return data
