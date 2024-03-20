import requests

url = 'http://localhost:8080/article'
payload = {
          "title": "湖南旅游攻略",
          "content": "天安门,华清池,法门寺,华山...爱去哪去哪...",
          "coverImg": "https://big-event-gwd.oss-cn-beijing.aliyuncs.com/9bf1cf5b-1420-4c1b-91ad-e0f4631cbed4.png",
          "state": "",
          "categoryId": "2",
       # "id": "3",
       # "categoryName": "人文",
       # "categoryAlias": "renwen"
}
headers = {
    'Content-Type': 'application/json',
    'Authorization':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGFpbXMiOnsiaWQiOjIsInVzZXJuYW1lIjoid2FuYUFRQSJ9LCJleHAiOjE3MDA2ODE0NTN9.QPcNw9O7aTs52tZlV9zVuTNNPk4UpYeJAcZJ69n0B6k'
}
response = requests.post(url, json=payload,headers=headers)

if response.status_code == 200:
    print("请求成功！")
    print("响应内容:", response.text)
else:
    print("请求失败，状态码:", response.status_code)