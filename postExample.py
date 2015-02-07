#import urllib
#import urllib2
import requests as req
import json

def addToWatchlist(instHash):
	# Now you can call printme function
	user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
	url = 'https://api.robinhood.com/watchlists/Default/'
	#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	instToAdd = 'https://api.robinhood.com/instruments/' + instHash + '/'
	print (instToAdd)
	payload = {'instrument' : instToAdd}
	hdrs = { 'User-Agent' : user_agent,
	 'Content-Type':'application/json',
	 'Authorization' : 'Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' }

	r = req.post(url, data=json.dumps(payload), headers=hdrs)

	#data = urllib.urlencode(values)
	#req = urllib2.Request(url, data=, headers=hdrs)
	#req = urllib2.Request(url, None, headers=hdrs)
	#response = urllib2.urlopen(req)
	#the_page = response.read()
	print(r.text[2])
	return r;

def main():
	response = addToWatchlist('03452d32-66f3-40ef-abc9-d7d0518fa572')
	print(response.text)
	
main()
