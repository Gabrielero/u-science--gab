from urllib import request
from time import sleep

while True:
	sleep(3)
	x=5
	form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdqFYyIh_8hmv2xf2foTMmis056QtIw9WtmG_c7ykTbsGG1UA/formResponse?usp=pp_url&entry.1738433285={}&submit=Submit".format(x)
	request.urlopen(form_url)


