from core import db


def test_db_connection():
    _engine = db.engine
    _engine.connect()
