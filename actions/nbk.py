import sys
import requests
from st2common.runners.base_action import Action

  class Myclass:
    def run(self, id, title)
          try:
            x = { "Id": id,"title": title}
            x1=json.dumps(x)
            r = requests.post('https://fakerestapi.azurewebsites.net/api/Books',x = x1)
            print(response)
          except requests.exceptions.Timeout:
            print("timeout")
            sys.exit(0)
    
