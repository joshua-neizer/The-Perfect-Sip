#!/bin/bash

### Set initial time of file
LTIME=`stat -c %Z preferences.json`
echo "Start..."
while true    
do
   ATIME=`stat -c %Z preferences.json`

   if [[ "$ATIME" != "$LTIME" ]]
   then    
       ./start.sh
       LTIME=$ATIME
   fi
   sleep 5
done