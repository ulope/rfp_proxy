#!/usr/bin/env python

from flaskext.script import Manager

from app import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()
