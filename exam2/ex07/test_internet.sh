#!/bin/bash

set -e

if curl -s -I www.google.com>/dev/null ;then
	echo $(date '+%Y-%m-%d:%H:%M:%S') internet ok>>internet.log
else
	echo $(date '+%Y-%m-%d:%H:%M:%S') internet FAIL>>internet.log
	exit 2
fi
exit 0

