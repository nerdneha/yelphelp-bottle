import os
import bottle
import bson
from urlparse import urlparse

MONGO_URL = os.environ.get('MONGOHQ_URL')

@bottle.route('/', method="GET")
def get_main_page():
    """
    Directs to main page for navigation
    """
    bottle.redirect('/main')

@bottle.route('/main', method="GET")
def present_options():
    """
    Allows user to search for restaurants or compare
    """
    return bottle.template('main')

@bottle.route('/search', method="GET")
def add_restaurant_review():
    return bottle.template('/search', add_var=None)

@bottle.route('/search', method="POST")
def add_review_to_db():
    for key, value in bottle.request.forms.items():
        print "%s: %s" % (key, value)
    #do something w/ yelp app
    return bottle.template('/search_results')


'''
#we don't need this yet but just in case
@bottle.route('/static/:filename#.*#')
def server_static(filename):
    #import pdb; pdb.set_trace()
    return bottle.static_file(filename, root='static')
'''
if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
        port = int(os.environ.get('PORT', 5000))
        print "port = %d" % port
        bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        bottle.debug(True) #dev only, not for production
        bottle.run(host='localhost', port=8081, reloader=True) #dev only