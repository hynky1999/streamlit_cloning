#!/bin/bash
###########
envsubst '$FLASK_HOST $FLASK_PORT' < /etc/nginx/nginx.conf.d > /etc/nginx/nginx.conf
cat /etc/nginx/nginx.conf
exec /docker-entrypoint.sh "$@"