
#GET DATA API URL DATA AND WRITE INTO IN FILE

import requests

r=requests.get('https://api.github.com/events')

# TO GET DATA FROM URL

# print(r.text)
data=r.json()
print(data)
# with open("data.txt","w") as f:
#   f.write(str(data))
