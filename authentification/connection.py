import redis
from core.config import get_settings

redisconn = redis.Redis(host=get_settings().REDIS_HOST,
port=get_settings().REDIS_PORT,
password=get_settings().REDIS_PASSWORD
,db=0)
