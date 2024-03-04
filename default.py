# 97.1 The Fan Kodi Plugin

from os.path import join
from sys import argv
from time import gmtime, strftime, strptime
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xml.dom.minidom import parseString
from xbmc import translatePath
import xbmcaddon
from xbmcgui import Dialog, ListItem
from xbmcplugin import addDirectoryItem, endOfDirectory

# Stream URL
THEFAN_STREAM = 'https://oom-radiohio.streamguys1.com/cols/wbnsfm.mp3'

# Player 
class StreamPlayer:

    def __init__(self, url):
        self.url = url

    def addLink(self, name, url, image = '', info = {}, totalItems = 0):
        item = ListItem(name.encode('utf-8'), iconImage = image, thumbnailImage = image)
        item.setProperty('mimetype', 'audio/mpeg')
        item.setInfo('music', info)
        return addDirectoryItem(int(argv[1]), url, item, False, totalItems)

    def buildIndex(self):
        self.addLink('[COLOR grey][B]97.1 The Fan[/B][/COLOR] [COLOR red] LIVE[/COLOR]', self.url, '', {
            'title': '97.1 The Fan',
        })

    def run(self, handle):
        endOfDirectory(int(handle))

# Main Loop
if __name__ == '__main__':
    thefan = StreamPlayer(THEFAN_STREAM)
    thefan.buildIndex()
    thefan.run(argv[1])
