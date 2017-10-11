#!/usr/env/python3

import json
import sys
import subprocess

data = json.load(open(sys.argv[1]))

def getinfo():
	for k,v in data.items():
		if "videoId" in v["contentDetails"] and "title" in v["snippet"]:
			if "watch" in sys.argv[2:]:
				p = subprocess.Popen("streamlink http://www.youtube.com/watch?v=%s" %(v["contentDetails"]["videoId"])
			elif "save" in sys.argv[2:].lower() or "download" in sys.argv[2].lower():
				p = subprocess.Popen('streamlink http://www.youtube.com/watch?v=%s -o "%s" ' %(v["contentDetails"]["videoId"], v["snippet"]["title"])
			"""newData = [{
				k : {
					title=str(v["snippet"]["title"]),
					vId=str(v["contentDetails"]["videoId"])
				}
			}]
			return newData
		print newData"""