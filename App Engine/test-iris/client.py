# -*- coding: utf-8 -*-
import requests
# Change the value of experience that you want to test
# 在部屬前先用 url=http://127.0.0.1:8080/api
url = 'https://iris-predict-dot-light-team-436602-j3.de.r.appspot.com/api'   
feature = [[5.8, 4.0, 1.2, 0.2]]
labels ={
  0: "setosa",
  1: "versicolor",
  2: "virginica"
}

r = requests.post(url,json={'feature': feature})
print(labels[r.json()])
