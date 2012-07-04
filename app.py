from flask import Flask, Response
import os
import requests
from lxml import etree

FEED_URL = "http://radiofreepython.com/medium_quality.rss"

app = Flask(__name__)

@app.route("/")
def index():
    feed_content = requests.get(FEED_URL)
    #parser = etree.XMLParser(ns_clean=True, recover=True)
    rss = etree.fromstring(feed_content.text.encode("UTF-8"))#, parser)
    for enclosure in rss.xpath("/rss/channel/item/enclosure"):
        enclosure.attrib['url'] = enclosure.attrib['url'].replace(" ", "%20")

    return Response(
        '<?xml version="1.0" encoding="utf-8"?>\n' + etree.tostring(rss, encoding="UTF-8"),
        mimetype="application/rss+xml"
    )

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
