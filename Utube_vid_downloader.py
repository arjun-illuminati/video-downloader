import sys
import os
import urllib
import urllib2
from bs4 import BeautifulSoup

""" to find the url related to a search query """

textToSearch = '10 sec video'
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
vid_links = []
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    lnk = 'https://www.youtube.com' + vid['href']
    vid_links.append(lnk)

command = "youtube-dl " + "-x --audio-format mp3 --prefer-ffmpeg " +  vid_links[0]  # for just audio file
command1 = "youtube-dl " + "--prefer-ffmpeg " +  vid_links[0]  # for video file
#print command1


#os.system(command1)