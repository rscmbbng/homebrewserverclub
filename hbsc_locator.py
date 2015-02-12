#!/usr/bin/python


import twitter, os, socket, re, commands

from requests import get
from hbsc_auth_keys import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter auth tokens are in a separate file which is not pushed to git!

ip_file = '/var/www/ip' #change me to whatever you like
local_ip_file = '/var/www/local_ip'

ip = get('http://api.ipify.org').text.encode('UTF-8') #get the current public IP adress

#extract the ip address (or addresses) from ifconfig
found_ips = []
ips = re.findall( r'[0-9]+(?:\.[0-9]+){3}', commands.getoutput("/sbin/ifconfig"))
for local_ip in ips:
  if local_ip.startswith("255") or local_ip.startswith("127") or local_ip.endswith("255"):
    continue
  found_ips.append(local_ip)

local_ip = found_ips[0]

if os.path.exists(ip_file) and os.path.exists(local_ip_file):
	old_ip = open(ip_file).read().strip('\n')
	old_local_ip = open(local_ip_file).read().strip('\n')
	if ip != old_ip or local_ip != old_local_ip:
		api = twitter.Api(consumer_key = consumer_key, consumer_secret=consumer_secret, access_token_key = access_token, access_token_secret=access_token_secret)
		api.PostUpdate('The HomeBrewServer.club is currently located at: '+str(ip)+', '+str(local_ip))
		os.system('echo "'+ip+'" > '+ip_file)
		os.system('echo "'+local_ip+'" > '+local_ip_file)
	else:
		#In case the IP adress didn't change since last time, do nothing.
		print('Still the same external IP')

else:
	print 'This script assumes that you manually make %s and %s to activate it' % (ip_file, local_ip_file)
