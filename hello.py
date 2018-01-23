from db_manager import db_manager
from flask import Flask, g, render_template
from json_loader import get_settings

db_path, db_name = get_settings()
db_m = db_manager(db_path)
db_m.table = db_name

# Static is where the html,css shit is
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=db_path)
#pp.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    db = get_db()

    a = db_m.get_random_row(db)
    # just nedd to grab the /static/images/username/0 TODO
    img_src = str(a[1]) + '0'
    #img = "/static/images/0"
    return render_template('index.html', img=img_src)



# @app.route('/<db_name>')
# def hello():
#    # return app.send_static_file('index.html')



def get_db():
    """Opens a new database connection if there is
    none yet for the current application context.
    And counts total number of rows in database"""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = db_m.create_connect()
        db_m.count_row(g.sqlite_db)  # Counts the total number of rows
    return g.sqlite_db


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db = get_db()
    print("Connected to database.\n")

if __name__ == '__main__':
    hello.run