# weibo_user

1. 模拟登录微博。
    'entry': 'sso',
    'gateway': '1',
    'from': 'null',
    'savestate': '0',
    'useticket': '0',
    'pagerefer': 'https://login.sina.com.cn/sso/login.php?client=ssologin.js',
    'vsnf': '1',
    'su': username,  # 加密用户名
    'service': 'sso',
    'servertime': str(servertime),  #时间戳
    'nonce': nonce,  #解析
    'pwencode': 'rsa2',
    'rsakv': '1330428213',
    'sp': password,# sp加密密码多个参数合并
    'sr': '1920*1080',
    'encoding': 'UTF-8',
    'cdult': '3',
    'domain': 'sina.com.cn',
    'prelt': str(random.randint(37, 600)),  #解析
    'returntype': 'TEXT'
    
2. 登录成功后会重定向到开始制定的爬取页面。
3. 抓取微博用户名，关注数，粉丝数，微博数量
4. 保存到MongDB
