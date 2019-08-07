# Redis数据库地址
REDIS_HOST = '129.28.200.147'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = 'Re_Lei'

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 购买的讯代理url
XDAILI_URL = 'http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=f5f6c78087e440d5ac874264e9c0bc57&orderno=YZ2019862398AlA8PJ&returnType=2&count=20'

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://m.weibo.cn/'

# API配置
# 4个0代表任意ip均可访问，此处勿动，写死
API_HOST = '0.0.0.0'
API_PORT = 5557
# http://127.0.0.1:5557/random

# 开关
GETTER_ENABLED = True
TESTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 10
