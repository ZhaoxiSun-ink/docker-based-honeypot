#!/bin/bash
CONTAINER_NAME="honeypot_apache"
current_time=$(date --date='yesterday' +"%m_%d_%H_%M")
filename=${CONTAINER_NAME}_${current_time}.txt
echo "name: $filename"
docker logs $CONTAINER_NAME >"/home/zhaoxisun/logs/$filename"

LOG_FILE=$(docker inspect $CONTAINER_NAME --format='{{.LogPath}}')
sudo truncate -s 0 $LOG_FILE
