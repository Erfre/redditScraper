from database_manager import db_manager
from flask import Flask, g, render_template, request
from json_loader import get_settings

subreddits, db_path = get_settings()
db_m = db_manager(db_path)
#db_m.table = db_name
#
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=db_path)


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_tables(subreddits):
    for each in subreddits:
        pass
    # show the different subbreddits and tables in the database
    return render_template('index.html', tables=subreddits)

@app.route('/<subreddit>', methods=['GET', 'POST'])
def show_entries(subreddit):
    db = get_db(subreddit)   # creates a connection on flask.g

    rand_row = db_m.get_random_row(db)
    print(rand_row)
    id = str(rand_row[0])
    img_src = str(rand_row[1]) + '0'
    title = rand_row[2]
    user = rand_row[3]
    descritpion = title + '\n\nCredit:/u/' + user

    if request.method == 'POST':
        if request.form['action'] == 'Save':
            desc = format(request.form['text'])
            db_m.update_desc(db, id, desc)
        if request.form['action'] == 'Delete':
            db_m.delete_row(db, id)

    return render_template('subtemp.html', img=img_src, desc=descritpion)


# @app.route('/<db_name>')
# def hello():
#    # return app.send_static_file('index.html')



def get_db(sub):
    """Opens a new database connection if there is
    none yet for the current application context.
    And counts total number of rows in database"""

    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = db_m.create_connect()
        db_m.table = sub
        db_m.count_row(g.sqlite_db)  # Counts the total number of rows
    return g.sqlite_db


# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     db = get_db()
#     print("Connected to database.\n")
