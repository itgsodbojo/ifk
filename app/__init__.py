from flask import Flask
from pony.orm import Database,sql_debug

app = Flask(__name__)


db = Database("sqlite", "ifk.db", create_db=True)


import models
sql_debug(True)
db.generate_mapping(create_tables=True)


import views


