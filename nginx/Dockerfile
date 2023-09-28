FROM nginx:1.25.2

# Install inotify-tools
RUN apt-get update && apt-get install -y inotify-tools

COPY nginx.conf.d /etc/nginx/nginx.conf.d
COPY entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]

CMD ["nginx-debug", "-g", "daemon off;"]