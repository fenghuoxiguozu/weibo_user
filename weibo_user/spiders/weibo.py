# -*- coding: utf-8 -*-
import scrapy
import requests
import base64
import json
import re
import rsa
import random
import binascii
from weibo_user.settings import *
from weibo_user.items import WeiboUserItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://login.sina.com.cn/sso/login.php?client=ssologin.js']
    session=requests.session()



    def get_username(self,inputname):
        username = base64.b64encode(inputname.encode('utf-8'))
        return str(username, 'utf-8')

    def get_password_data(self):
        html = self.session.get(PASSWORD_URL).text
        data = re.findall(r'sinaSSOController.preloginCallBack\((.+)\)', html, re.S)
        print("正则数据：",data)
        data = data[0]
        content = json.loads(data)
        pubkey = content['pubkey']
        nonce = content['nonce']
        rsakv = content["rsakv"]
        servertime = content["servertime"]
        return pubkey, nonce, rsakv, servertime

    def get_password(self,inputpassword, servertime, nonce, pubkey):
        rsaPubkey = int(pubkey, 16)
        RSAKey = rsa.PublicKey(rsaPubkey, 65537)  # 创建公钥
        codeStr = str(servertime) + '\t' + str(nonce) + '\n' + inputpassword  # 根据js拼接方式构造明文
        pwd = rsa.encrypt(codeStr.encode(), RSAKey)  # 使用rsa进行加密
        # print(str(binascii.b2a_hex(pwd),'utf-8'))
        return binascii.b2a_hex(pwd).decode()  # 将加密信息转换为16进制。

    def start_requests(self):
        username = self.get_username(USER_NAME)
        pubkey, nonce, rsakv, servertime = self.get_password_data()
        password = self.get_password(USER_PASSWORD,servertime, nonce, pubkey)
        print("加密的后用户名：",username)
        print("加密的后密码：", password)
        formdata = {
            'entry': 'sso',
            'gateway': '1',
            'from': 'null',
            'savestate': '0',
            'useticket': '0',
            'pagerefer': 'https://login.sina.com.cn/sso/login.php?client=ssologin.js',
            'vsnf': '1',
            'su': username,  #
            'service': 'sso',
            'servertime': str(servertime),  #
            'nonce': nonce,  #
            'pwencode': 'rsa2',
            'rsakv': '1330428213',
            'sp': password,# sp
            'sr': '1920*1080',
            'encoding': 'UTF-8',
            'cdult': '3',
            'domain': 'sina.com.cn',
            'prelt': str(random.randint(37, 600)),  #
            'returntype': 'TEXT'
        }
        print("正在登陆，请稍后。。。：")
        yield scrapy.FormRequest(url=LOGIN_URL, formdata=formdata,callback=self.login)

    def login(self,response):
        json_data = json.loads(response.text)
        print("json数据：",json_data)
        uid = json_data['uid']
        redirect_url = json_data['crossDomainUrlList'][0]
        user_url = 'https://weibo.com/u/{}'.format(uid)
        print("登录回调URL: ",user_url, redirect_url)
        yield scrapy.Request(user_url, callback=self.redirect_login,meta={'redirect_url':redirect_url})


    def redirect_login(self,response):
        redirect_url=response.meta['redirect_url']
        yield scrapy.Request(redirect_url, callback=self.successful_login)

    def successful_login(self,response):
        print("模拟登陆成功，开始抓取页面。。。")
        yield scrapy.Request(START_CRAWL_URL, callback=self.parse_index)

    def parse_index(self,response):
        s = re.findall(r"page_id'\]='(\d+)';", response.text, re.S)
        # print("正则follow:", s)
        follow_url = BASE_URL.format(s[0])
        yield scrapy.Request(follow_url,callback=self.parse_info)

    def parse_info(self, response):
        # print("网页源码：",response.text)
        item=WeiboUserItem()
        contents = re.findall(r'<script>(.*?)\)</script>', response.text, re.S)
        contents = contents[-1].replace('FM.view(', '')
        json_data = json.loads(contents)
        content = json_data['html']
        lists = re.findall(r'<li class="follow_item S_line2(.*?)</li>', content, re.S)
        for list in lists:

            # if 'follow_item S_line2' in list:
            #     print("ok")
            user = re.findall(r'target="_blank" title="(.*?)" href', list, re.S)
            care_num = re.findall(r'关注 <em class="count"><a target=.*? >(\d+)</a></em>', list, re.S)
            fans_num = re.findall(r'粉丝<em class="count"><a target=.*? >(\d+)</a></em>', list, re.S)
            weibo_num = re.findall(r'微博<em class="count"><a target.*? >(\d+)</a></em>', list, re.S)
            weibo_url = re.findall(r'微博<em class="count"><a target="_blank" href="(.*?)" >', list, re.S)

            if user:
                item['user'] = user[0]
            if care_num:
                item['care_num'] = care_num[0]
            else:
                item['care_num'] = 'null'
            if fans_num:
                item['fans_num'] = fans_num[0]
            else:
                item['fans_num'] = 'null'
            if weibo_num:
                item['weibo_num'] = weibo_num[0]
            else:
                item['weibo_num'] = 'null'
            yield item
            if weibo_url:
                weibo_url = 'https://weibo.com/' + weibo_url[0]
                yield scrapy.Request(weibo_url,callback=self.parse_index)


