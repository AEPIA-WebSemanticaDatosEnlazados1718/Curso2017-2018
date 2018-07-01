import random
from bottle import Bottle, run
from repository import Repository

repository = Repository()
repository.load_graph()
app = Bottle()
tables_class = "mdl-data-table mdl-js-data-table mdl-shadow--2dp"


@app.route('/')
def render_tables():
    data = repository.get_info()
    data.columns = ['Place', 'Total Attendance', 'Winner', 'Year']

    return add_html(data.to_html(classes=tables_class, index=False))


@app.route('/years/<year>')
def render_tables(year):
    data = repository.get_info_by_year(year)
    data.columns = ['Attendance', 'City', 'MatchID', 'DateTime']

    return add_html(data.to_html(classes=tables_class, index=False))


@app.route('/teams')
def render_tables():
    data = repository.get_team_ids()
    data.columns = ['Team Code', 'Team']

    return add_html(data.to_html(classes=tables_class, index=False))


@app.route('/goals')
def render_tables():
    data = repository.get_goals_by_team()
    data.columns = ['Team Code', 'Goals Scored']

    return add_html(data.to_html(classes=tables_class, index=False))


@app.route('/players')
def render_tables():
    data = repository.get_matches_by_player()
    data.columns = ['Games played', 'Player']

    return add_html(data.to_html(classes=tables_class, index=False))


def add_html(table):
    years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994,
             1998, 2002, 2006, 2010, 2014]
    year = random.SystemRandom().choice(years)

    return """
        <html>
        <head>
            <title>FIFA World Cup</title>
            <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
            <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
            <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
        </head>
        <body style="padding-top:14px;background-color:"#eee">
            <div style="padding-left:30px;padding-right:24px;padding-bottom:20px;">
                <div>
                     <a href="/" class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                        Years
                    </a>
                    <a href="/teams" class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                        Teams
                    </a>
                    <a href="/goals" class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                        Goals
                    </a>
                    <a href="/players" class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                        Players
                    </a>
                    <a href="/years/""" + str(year) + """"
                     class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect">
                        Random Edition
                    </a>
                </div>
                <br/>
    """ + table + """
        </div>
        </body>
        </html>
    """


run(app, host='localhost', port=8080)
