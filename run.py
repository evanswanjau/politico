import os
from app.__init__ import create_app

app = create_app()

from app.version1.views import admin
app.register_blueprint(admin.bp)
