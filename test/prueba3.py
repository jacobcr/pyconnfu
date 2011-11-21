import pycurl, json

STREAM_URL = "https://stream.connfu.com/connfu-stream-testing-emc2"

USER = "segphault"
PASS = "XXXXXXXXX"

def on_receive(data):
  print data

conn = pycurl.Curl()
conn.setopt(pycurl.USERPWD, "%s:%s" % (USER, PASS))
conn.setopt(pycurl.HTTPHEADER, ['authorization : Backchat f2fc94294e373d67e9bd404fcc247f73'])
conn.setopt(pycurl.URL, STREAM_URL)
conn.setopt(conn.SSL_VERIFYHOST,0)
conn.setopt(pycurl.WRITEFUNCTION, on_receive)
conn.perform()
