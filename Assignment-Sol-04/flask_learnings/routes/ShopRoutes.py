from ..Services.Shop import ShopsServices, ItemsByShopServices
from .BaseRoutes import getNewRoutes

routes = getNewRoutes('Shops')
routes.add_url_rule('/', view_func=ShopsServices.as_view('Shops'), methods = ['GET', 'POST'])
routes.add_url_rule('/Items/', view_func=ItemsByShopServices.as_view('Stocks'), methods = ['POST'])
