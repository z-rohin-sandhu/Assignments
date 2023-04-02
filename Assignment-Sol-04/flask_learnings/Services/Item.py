from flask.views import MethodView
from ..models.All import db
from flask import request
from ..common import get_item, getShopByItemServices
import json

class ItemServices(MethodView):
    def __init__(self):
        self.id = None 
    
    def get(self, *args, **kwargs):
        result = get_item()
        if result == None:
            result = {"success": False, "result": result, "code": 404}
            return result
        result = {"success": True, "result": result, "code": 200}
        return result

    def post(self, *args, **kwargs):
        params = json.loads(request.data)
        result = get_item(params['id'])
        if result == None:
            result = {"success": False, "result": result, "code": 404}
            return result
        result = {"success": True, "result": result, "code": 200}
        return result

class ShopByItemServices(MethodView):
    def __init__(self):
        self.id=None

    def post(self,*args, **kwargs):
        params=json.loads(request.data)
        result=getShopByItemServices(params['id'])
        if result is not None:
            result={"success":True,"result":result,"code":200}
            return result
        else:
            result={"success":False,"result":"Bad Request","code":404}
            return result