from ..Services.Item import ItemServices,ShopByItemServices
from .BaseRoutes import getNewRoutes

routes = getNewRoutes('Items')
routes.add_url_rule('/', view_func=ItemServices.as_view('Items'), methods = ['GET', 'POST'])
routes.add_url_rule('/Shops/', view_func=ShopByItemServices.as_view('Stocks'), methods = [ 'POST'])