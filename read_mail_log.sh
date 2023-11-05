#!/bin/bash
CONTAINER_NAME="honeypot_mailoney"
current_time=$(date +"%m_%d_%H_%M")
LOG_PATH="/app/logs/mail.log"
DEST="/home/zhaoxisun/logs/${CONTAINER_NAME}_${current_time}.txt"

docker cp "${CONTAINER_NAME}:${LOG_PATH}" "$DEST"

if [ $? -eq 0 ]; then
        docker exec "$CONTAINER_NAME" truncate -s 0 "$LOG_PATH"
else
        echo "Error happen during copying the log from the container. Skipping truncate."
fi
