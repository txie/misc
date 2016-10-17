import requests

url = "https://integration.trustlook.com/hwmarket/api/job"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"\r\n\r\n{   \"api_name\": \"submit\",   \"app_info\": [     {       \"name\": \"weixin\",       \"package\": \"com.qq.weixin\",       \"apk_url\": \"http://dfdafdasfaf\",       \"md5\": \"aaaadfdfefafdafdadfaf\"     },     {       \"name\": \"QQ\",       \"package\": \"com.qq.qq\",       \"apk_url\": \"http://dfaeffeafdfadsf\",       \"md5\": \"eeeeeadfdfefafdafdadfaf\"     }   ],   \"ts\": \"1333333333\" }\r\n-----011000010111000001101001--"
headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'cache-control': "no-cache",
    'postman-token': "d4421df1-6453-9ec7-f56d-3bfdd315a99a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
