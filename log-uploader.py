#!/usr/bin/env python

from subprocess import call

logList=['/var/log/syslog','/var/log/cron.log', '/var/log/dmesg', '/var/log/messages', '/var/log/kern.log']
uploadCMD='/usr/local/bin/Dropbox-Uploader/dropbox_uploader.sh'
destinationDIR='logs'

for log in logList:
  print log
  call([uploadCMD, 'upload', log, destinationDIR])

