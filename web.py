import bottle
from bottle import route
from bottle_sqlalchemy import SQLAlchemyPlugin

import config
import database



if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)