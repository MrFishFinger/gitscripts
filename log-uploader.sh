#!/bin/bash

LOGFILE=/var/log/syslog
DPU=/usr/local/bin/Dropbox-Uploader/dropbox_uploader.sh

#/usr/local/bin/Dropbox-Upyloader/dropbox_uploader.sh upload $LOGFILE logs/syslog

$DPU upload $LOGFILE logs/syslog



