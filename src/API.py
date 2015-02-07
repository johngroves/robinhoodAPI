import requests as req
import json

class rh_client(object):
	rh_api_endpoint = 'https://api.robinhood.com'
	UserAgent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
	ContentType = 'application/json'

	#def __init__(self):


	"""Login and set the oath_token """
	def login(self, username, password):
		url = self.rh_api_endpoint + '/api-token-auth/'
		params = {'username': username,
				  'password': password}
		hdrs = {'User-Agent': self.UserAgent,
				'Content-Type': self.ContentType}
		resp = req.post(url, data=json.dumps(params), headers=hdrs)
		json_resp = resp.json()
		try:
			self.oath_token = resp['token']
		except KeyError:
			pass
	