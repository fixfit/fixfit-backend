from fixfit import create_application, db
from fixfit.models.user import User

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

import os

def make_shell_context():
    return dict(app=app, db=db, User=User)

app = create_application(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
