import lxml.html
import re
import urllib2

URL = 'http://download.sugarlabs.org/sources/sucrose/fructose/'
ACTIVITIES=['Terminal']

def update_activity(activity):
    pass
    
def process_activity(activity):
    # Find the latest version
    root = lxml.html.fromstring(urllib2.urlopen(URL + activity).read())
    versions = []
    for link in root.cssselect('a'):
        v = re.search('([0-9]+)\.tar\.bz2$', link.get('href'))
        if  v != None:
            versions.append(int(v.group(1)))
    versions.sort()
    latest_version=versions[len(versions)-1]

    # Find the current version
    for line in open('sugar-activity-%s/PKGBUILD' % activity.lower(),  'r').readlines():
        v = re.search('pkgver=([0-9]+)',  line)
        if v != None:
            current_version = int(v.group(1))
    
    # Compare
    print '%s : %d vs %d' % (activity,  current_version,  latest_version)
    if latest_version > current_version:
        update_activity(activity)

for activity in ACTIVITIES:
    process_activity(activity)
