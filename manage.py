import os
import unittest
from flask_script import Manager
from app import create_app

api = create_app()
manager = Manager(api)

@manager.command
def run():
    api.run('0.0.0.0',debug=True)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()