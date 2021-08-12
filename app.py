from app.flask import app

from app.views.main import *
from app.views.posts import *
from app.views.users import *
from app.views.chat import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)