#!/bin/bash

# Define the directory where the logs are stored
LOG_DIR=/home/zhaoxisun/logs/mysql-logs

# Define the MySQL Docker container name
CONTAINER_NAME=honeypot_mysql

# Move the current log file to a new file with the current date
mv "$LOG_DIR/general.log" "$LOG_DIR/$(date --date='yesterday' +%Y%m%d).log"

# Execute FLUSH LOGS command on MySQL server to reopen the log file
docker exec -i $CONTAINER_NAME mysql -uroot -p'123456' -e 'FLUSH LOGS;'
