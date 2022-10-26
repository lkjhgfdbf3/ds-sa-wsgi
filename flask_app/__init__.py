from flask import Flask, render_template
from flask_app.routes import user_routes

app = Flask(__name__)
app.register_blueprint(user_routes.bp)

@app.route('/index/',defaults={'num':0})
@app.route('/index/<num>')
def index_num(num):
    return 'Welcome to Index %i' % int(num)

@app.route('/')
def index():
   return render_template('child.html')

def create_app():
    app = Flask(__name__)

    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app

if __name__ == "__main__":
  app = create_app()
  app.run()