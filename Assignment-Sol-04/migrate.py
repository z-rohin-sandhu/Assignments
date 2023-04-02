from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
import os
from dotenv import load_dotenv
import json
from flask_learnings.models.All import Shops, Items, Stocks

ROOT_DIR = os.path.join(os.path.dirname(__file__),"flask_learnings")
DOT_ENV_PATH = os.path.join(ROOT_DIR , ".env")
load_dotenv(DOT_ENV_PATH)

def getDBConnectionString():
    config= {}
    config["username"] = os.getenv('DB_USERNAME')
    config["host"] = os.getenv('DB_HOST')
    config["password"] = os.getenv('DB_PASSWORD')
    config["database"] = os.getenv('DATABASE')
    config["port"] = os.getenv('DB_PORT')
    return f"mysql+pymysql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

engine = create_engine(getDBConnectionString())
db_session = scoped_session(sessionmaker(autocommit = False,autoflush=False, bind= engine))
Base = declarative_base()
Base.query = db_session.query_property()

if __name__=="__main__":
    Base.metadata.create_all(bind = engine)
    item = Items(id =35, name = "Coffe61", description = " Dark Coffe 61")
    db_session.add(item)
    
    shop = Shops(id = 37, name = "Nescaffe61", description = "Coffe Shop 61")
    db_session.add(shop)
    
    stock = Stocks(id = 24,shop_id=shop.id, item_id = item.id, item_count = 20, item_price = 12.5)
    db_session.add(stock)

    db_session.commit()