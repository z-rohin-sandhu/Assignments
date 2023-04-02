from flask import Blueprint
from . import ShopRoutes, ItemRoutes, BaseRoutes

def init_app(app):
    app.register_blueprint(BaseRoutes.routes)
    app.register_blueprint(ShopRoutes.routes)
    app.register_blueprint(ItemRoutes.routes)
    return app