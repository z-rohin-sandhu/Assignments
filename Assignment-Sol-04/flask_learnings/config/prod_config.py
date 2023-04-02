from .base_config import Base_Config

class ProductionConfig(Base_Config):
    DEVELOPMENT = False
    DEBUG = True