#!/usr/bin/env python

from subprocess import call
import tarfile, datetime, os

logPath='/var/log'
uploadCMD='/usr/local/bin/Dropbox-Uploader/dropbox_uploader.sh'
destinationDIR='logs/daily-logs/'

# generate filename
datestamp=datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
filename='/tmp/' + datestamp + '.tar.gz'

print filename

# create tar of log directory
archive = tarfile.open(filename, 'w:gz')
archive.add(logPath)
archive.close()

# upload to dropbox
call([uploadCMD, 'upload', filename, destinationDIR])

# delete temporary file
os.remove(filename)

