import sys
import json
import requests
from st2common.runners.base_action import Action
class MyAction(Action):
	def run(self,id,title,desc,pgc,exc,pbp):
		try:
			data={"ID": id,"Title":title,"Description": desc,"PageCount": pgc,"Excerpt": exc,  "PublishDate": pbp}
			data1=json.dumps(data)
			headers={'content-type': 'application/json'}
			url='https://fakerestapi.azurewebsites.net/api/Books'
			response=requests.post(url,headers=headers,data=data1,timeout=6.0)
			print(response)
			data2=response.json()
			print(data2)
			
		except requests.exceptions.Timeout:
                        print("timeout")
                        sys.exit(0)
    
