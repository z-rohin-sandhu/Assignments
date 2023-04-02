from ..models.All import Shops, Items, Stocks

def get_values(table,id):
    if id == None:
        result=[s.as_dict() for s in table.query.all()]
        return result
    return [s.as_dict() for s in table.query.filter(id==table.id)]

def get_shop(id=None):
    return get_values(Shops,id)

def get_item(id = None):
    return get_values(Items,id)

def getItemByShopServices(item_id = None):
    if item_id == None:
        result=[s.as_dict() for s in Stocks.query.all()]
        return result
    return [s.as_dict() for s in Stocks.query.filter(item_id==Stocks.item_id)]

def getShopByItemServices(shop_id = None):
    if shop_id == None:
        result=[s.as_dict() for s in Stocks.query.all()]
        return result
    return [s.as_dict() for s in Stocks.query.filter(shop_id==Stocks.shop_id)]