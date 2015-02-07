#import urllib
#import urllib2
import requests as req
import json

def userLogin(username,password):
	user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
	url = 'https://api.robinhood.com/api-token-auth/'
	payload = {'username' : username,
		   'password' : password}
	hdrs = { 'User-Agent' : user_agent,
	 'Content-Type':'application/json'}

	r = req.post(url, data=json.dumps(payload), headers=hdrs)
	return r;

