from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(g, "_database", None)

    if db is None:
        db = g._database = SQLAlchemy(current_app)
        migrate = Migrate(current_app, db)
    return db


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)


