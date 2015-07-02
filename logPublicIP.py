#!/usr/bin/env python

def datestamp():
  import datetime
  return datetime.datetime.now().strftime('%Y-%m-%d_%H%M')


def logMe(logname,msg):
  logFileName='/var/log/' + logname
  print msg
  with open(logFileName, "a") as logFile:
    logFile.write(datestamp() + ' - ' + msg + '\n')


def getPublicIP():
  "This returns the Public IP address using a helper site"
  import urllib2

  helperSite1 = 'http://ip.42.pl/raw'
  helperSite2 = 'http://canihazip.com/s'

  publicIP = urllib2.urlopen(helperSite2).read()

  return publicIP


def main():
  logfile = 'publicIP.log'
  logMe(logfile,getPublicIP())


main()

