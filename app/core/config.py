from functools import lru_cache
import os

class Config:

    TG_APP_ID = '28583769'
    TG_APP_HASH = '8c03cfc6e8be855de935ac61ac4047d7'
    SESSION_STRING = '1BJWap1sBuxfjwBGevZY_OIFwYuBsOkXs2smsyLQ4kwOMfWvjsA_8Mz2wySGf1Fsck4GbFqbQ0aK-owQuHbisz5zkcF88zBJnGvr7NIaRkvJ2zFOTFIhhui_pZ3IhhlJRSXj0CiJNhS-YELZjg6L_oJ9Azo5gdV31RhUlR2NNrKKS7jiE-zd-hMkS38saHsDj9hgk27Pj309SKA_a8-LBntYrHiy_bSa4XjIoIFv2POIBZg_xZOu2d5flaUmTL4-vGmaYqLVWT4_q6GvQo667nz8DKqX9iBz3XmjVtuczRtGOV8sgiTC8JS_bmCSZ0BISqnKF_ziNmJ7IFIzLgyDbVS2_FvKgNSc='
    ADMIN_UID = '6675988213'
    
    DATABASE_URL = 'postgres://koyeb-adm:ftqdyolX9Tg0@ep-quiet-resonance-a2yei523.eu-central-1.pg.koyeb.app/koyebdb'


    APP_NAME        = 'Movie Blog'
    APP_DESC        = 'A simple telegram indexer for movie channel'
    APP_URL         = 'https://filexlink-tomenmain.koyeb.app'

    BUFFER_SIZE:int                 = 1024
    MAX_ITEMS_PER_PAGE:int          = 20
    DOWNLOAD_ENABLED:bool           = True
    MAX_SIMULTANIOUS_DOWNLOAD:int   = 20
    
    DEFAULT_COVER_IMG:int   = 1
    DEBUG:bool              = True
    
    def __init__(self):
        for i in dir( self):
            if not i.startswith('__'):
                try:
                    self.__setattr__(i, os.getenv(i,self.__getattribute__(i)))
                except:
                    raise Exception('required env variables missing')


@lru_cache()
def get_config():
	return Config()

CONFIG = get_config()
