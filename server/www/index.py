import sys
sys.path.append("/home/glacsweb/picogps/server")

import gpsdb
import datetime 
from csvconvert import csv_convert

CONFIG = "/home/glacsweb/picogps/server/db.ini"

def index(req):
    output = "<html><head><title>Glacier Tracker Status</title></head><body>"
    output += "<h1>Glacier Tracker Status</h1>\r\n"
    output += "<h2>Latest Data Summary</h2>\r\n"
    output += ("<p>As at %s UTC</p>" % datetime.datetime.utcnow())
    output += ("<table  border><tr><th>Glacier</th><th>IMEI</th><th>Timestamp</th>" + 
        "<th>Longitude</th><th>Latitude</th><th>Altitude</th><th>Quality</th>" +
        "<th>HDOP</th><th>Satelites</th><th>Position Count</th></tr>")
    DB = gpsdb.GpsDb(CONFIG)
    LATEST = DB.get_latest_data()
    for SITE in LATEST:
        COUNT = DB.get_data_count(SITE[1])
        output += "<tr>"
        output += ("<td>%s</td>" % SITE[0])
        output += ("<td>%s</td>" % SITE[1])
        output += ("<td>%s</td>" % SITE[2])
        output += ("<td>%s</td>" % SITE[3])
        output += ("<td>%s</td>" % SITE[4])
        output += ("<td>%s</td>" % SITE[5])
        output += ("<td>%s</td>" % SITE[6])
        output += ("<td>%s</td>" % SITE[7])
        output += ("<td>%s</td>" % SITE[8])
        output += ("<td>%s</td>" % COUNT)
        output += "</tr>"
    output += "</table>"
    output += "<p>Number of unprocessed messages: %d</p>\r\n" % DB.get_unprocessed_message_count()
    output += "</body></html>"
    return output