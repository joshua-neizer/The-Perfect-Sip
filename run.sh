#!/bin/bash
./Arduino/check-update.sh &

cd REST-API
# docker-compose down
docker-compose up

# Use sudo killall check-update.sh to stop the background process
