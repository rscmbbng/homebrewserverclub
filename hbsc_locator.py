#!/usr/bin/python


import twitter, os
from requests import get

#API Keys
consumer_key = 
consumer_secret =
acces_token = 
access_token_secret =



ip_file ='/var/www/ip' #change me to whatever you like

ip = get('http://api.ipify.org').text.encode('UTF-8') #get the current public IP adress

if os.path.exists(ip_file):
	old_ip = open(ip_file).read().strip('\n')
	if ip != old_ip:
		api = twitter.Api(consumer_key = consumer_key, consumer_secret=consumer_secret, access_token_key = acces_token, access_token_secret=access_token_secret)
		api.PostUpdate('The HomeBrewServer.club is currently located at: '+str(ip))
		os.system('echo "'+ip+'" > '+ip_file)

	else:
		#In case the IP adress didn't change since last time, do nothing.
		print('Still the same IP')

else:
	print('This script assumes that you manually make', ip_file, 'to activate it')
