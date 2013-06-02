from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )

import requests


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {}


@view_config(route_name='zip', renderer='zip.mak')
def zip(request):
    zipcode = request.matchdict.get('zipcode')
    url = 'http://iaspub.epa.gov/enviro/efservice/getEnvirofactsUVHOURLY/ZIP/'\
           + zipcode + '/json'
    r = requests.get(url)
    data = r.json()
    return dict(zipcode=zipcode,
                data=data)


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_EPAUV_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
