import requests
import time


def push(name):
    url = "https://maker.ifttt.com/trigger/ppp/with/key/bm4a3i-fD-1FDWMKC4pqc1"
    payload = "{\n    \"value1\": \"" + name + "\"\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

    print(response.text)


def p(name, u, d, j, headers):
    if d == 0:

        a = requests.post(u, json=j, headers=headers)
        time.sleep(10)

        b = requests.post(u, json=j, headers=headers)
        if a.text == b.text:
            push(name)
    else:
        a = requests.post(u, data=d, headers=headers)
        time.sleep(10)

        b = requests.post(u, data=d, headers=headers)
        print(a.content.decode('unicode_escape'))
        if a.text == b.text:
            push(name)


def g(name, u, c):
    headers = {
        "Cookie": c,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1"
    }

    a = requests.get(u, headers=headers)
    time.sleep(10)

    b = requests.get(u, headers=headers)
    print(a.content.decode('unicode_escape'))

    if a.text == b.text:
        push(name)


'''g(
    "远景论坛",
    "http://i.pcbeta.com/home.php?mod=task&do=apply&id=149",
    "Hm_lpvt_76c941eab16e9b48cd0fb4a6d9482a4f=1585631235; Hm_lvt_76c941eab16e9b48cd0fb4a6d9482a4f=1585630994; jqCP_887f_lastact=1585631234%09home.php%09task; jqCP_887f_sid=SJqoZn; jqCP_887f_uuid=4861988; jqCP_887f_home_diymode=1; jqCP_887f_viewuids=2091602; _ga=GA1.2.529656265.1585630919; _gid=GA1.2.1968332020.1585630919; jqCP_887f_mobile=no; jqCP_887f_checkpm=1; jqCP_887f_mrd=%09; jqCP_887f_sendmail=1; jqCP_887f_auth=722bGngd70GSYKBu0PI%2BDXsocMru2sSUz1WcVQ2kXojZsvOD2kUOhQMZDmMzfA%2BlV%2BG5nMEeaWKwFQvjxZEKttFGB3fg; jqCP_887f_ulastactivity=9209X%2BIwxqfd9aTT0HCPN8SX0ZuD541kXHmkn0amUvrUUKtWNoCr; jqCP_887f_lastvisit=1585627318; jqCP_887f_saltkey=T9759a2V"
)'''

'''p(
    "Mac毒",
    "https://www.macdo.cn/api/v1/actions/daily_sign",
    {
        '_wpnonce': '5f942c3830'
    },
    "0",
    {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
     "Cookie": "Hm_lpvt_2b40469dbef9b5ed6874ddfa5becd200=1585901770; Hm_lvt_2b40469dbef9b5ed6874ddfa5becd200=1585901681; "
               "_ga=GA1.2.2040850481.1585901681; _gid=GA1.2.1130495362.1585901681; tt_ref=; _gat_gtag_UA_101217690_2=1; "
               "Cute_cache=1; wordpress_logged_in_b797b15401facbe5978d03d18378e9da=740162752%40qq.com%7C1587111320"
               "%7C7EAcDGnslgOZK0Yb6T3qPsKU6n5rCzX7ulZPjUopWLf"
               "%7C566df09a48dba5878a2642484c0c380ddcb40e50487d4e125f47e6cc38bf15c1; "
               "cx_oauth_redirect=https%253A%252F%252Fwww.macdo.cn%252F "
        ,
     "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 source/jegotrip"
     }
)'''

'''g(
        "吾爱破解论坛",
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2",
        "Hm_lpvt_46d556462595ed05e05f009cdafff31a=1585824773; Hm_lvt_46d556462595ed05e05f009cdafff31a=1585824632,1585824729; htVD_2132_auth=c4d6Q7LNab2YubOlE5xkTt9Ie%2FcleP1BTK15VPQXROs1jxa4JL03csuTPZKn6WiE5Xdy3ydYu5X3qESrhjvaMi%2FkaHk; htVD_2132_checkfollow=1; htVD_2132_checkpm=1; htVD_2132_client_created=1585824767; htVD_2132_client_token=0CCAC93F86CF62B2AADDEFFA6E1BE5B3; htVD_2132_connect_is_bind=1; htVD_2132_connect_login=1; htVD_2132_connect_uin=0CCAC93F86CF62B2AADDEFFA6E1BE5B3; htVD_2132_lastact=1585824768%09home.php%09spacecp; htVD_2132_lastcheckfeed=689288%7C1585824768; htVD_2132_stats_qc_login=3; htVD_2132_ttask=689288%7C20200402; htVD_2132_ulastactivity=1585824767%7C0; htVD_2132_con_request_uri=https%3A%2F%2Fwww.52pojie.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhttps%253A%252F%252Fwww.52pojie.cn%252F; htVD_2132_seccode=1516986.7c17cd1df34d2d3aac; __gads=ID=b387dfa2869a213e:T=1585824634:S=ALNI_MbbPJ1pCgZBXmO-KbRBsSnSBuKtPQ; htVD_2132_lastvisit=1585821029; htVD_2132_saltkey=J2iiPTBi"
        )

'''
time.sleep(1)
g(
    '卡饭论坛',
    'https://a.kafan.cn/static/1/ajax.js?hEW',
    "r6pb_69df_saltkey=QUJTXgr8;r6pb_69df_lastvisit=1585921620;	r6pb_69df_con_request_uri=https%3A%2F%2Fbbs.kafan.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php;	r6pb_69df_sid=Nn03MH;	r6pb_69df_client_created=1585925243;r6pb_69df_client_token=F7B71380AE6F0BE2D2556D823643C1B9;r6pb_69df_ulastactivity=cf8auW0c9iqufm%2FiQahd7qc8a7VPa1wY3TxllNxCNsaB2%2BhScern;r6pb_69df_auth=915cFn%2BryFiqGNYrhBNue32OGUmHYJDUaV6VnxDbBuFMKnXaaP1KPo4xKq4%2BRRi9DqIrE83Pb3co9apBUAxIdOjAnE9h;r6pb_69df_connect_login=1;r6pb_69df_connect_is_bind=1;r6pb_69df_connect_uin=F7B71380AE6F0BE2D2556D823643C1B9;r6pb_69df_stats_qc_login=3;r6pb_69df_nofavfid=1;Hm_lvt_92b3c18c8d9607c79a41c0e018b4e032=1585925511;Hm_lpvt_92b3c18c8d9607c79a41c0e018b4e032=1585925539;	r6pb_69df_dsu_amupper=CjxkaXYgY2xhc3M9InBwZXJ3Ym0iIGlkPSJwcGVyd2JfbWVudSIgc3R5bGU9ImRpc3BsYXk6IG5vbmUiID4KPEEgSFJFRj0icGx1Z2luLnBocD9pZD1kc3VfYW11cHBlcjpwcGVybGlzdCIgdGFyZ2V0PSJfYmxhbmsiPiFzaG93bGlzdCE8L0E%2BCjxzdHJvbmc%2BIWFkZHVwITxzcGFuIGNsYXNzPSJ0aW1lcyI%2BMzk8L3NwYW4%2BIXRpbWVzITwvc3Ryb25nPjxicj4KCjxBIEhSRUY9ImZvcnVtLnBocD9tb2Q9dmlld3RocmVhZCZhbXA7dGlkPTIxNzc2NzMmYW1wO2F1dGhvcmlkPTEyMTQzMjUiIHRhcmdldD0iX2JsYW5rIj4hc2hvd3Bvc3QhPC9BPgoKPHN0cm9uZz4hY29ucyE8c3BhbiBjbGFzcz0idGltZXMiPjA8L3NwYW4%2BIXRpbWVzITwvc3Ryb25nPjxicj4KCjxzdHJvbmc%2BIWxhc3QhOiA8c3BhbiBjbGFzcz0idGltZXMiPjIwMjAtMDQtMDMgMjI6NDc6NTk8L3NwYW4%2BPC9zdHJvbmc%2BCjwvZGl2Pgo%3D;r6pb_69df_lastact=1585927230%09home.php%09spacecp"
)
