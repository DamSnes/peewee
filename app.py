from app.flask import app

from app.views.main import *
from app.views.posts import *
from app.views.users import *
from app.views.chat import *
from app.views.tables import *
from app.views.monday import *
from app.views.tuesday import *
from app.views.wednesday import *
from app.views.thursday import *
from app.views.friday import *
from app.views.saturday import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)