FROM debian:buster-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y nginx mailman postfix supervisor fcgiwrap multiwatch busybox-syslogd locales && \
    rm -rf /var/lib/apt/lists/* && \
    # Configure Nginx
    sed -i -e 's@worker_processes 4@worker_processes 1@g' /etc/nginx/nginx.conf && \
    rm -f /etc/nginx/sites-enabled/default && \
    # Cache default dirs as template (must come after configuration)
    cp -a /etc/mailman /etc/mailman.cache && \
    cp -a /var/lib/mailman /var/lib/mailman.cache && \
    cp -a /var/spool/postfix /var/spool/postfix.cache

ADD nginx.conf /etc/nginx/conf.d/
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD mm_cfg.py /etc/mailman/mm_cfg.py
ADD *.sh /

EXPOSE 25 80

#VOLUME ["/etc/mailman/", "/var/lib/mailman", "/var/log/mailman", "/var/spool/postfix"]

ENTRYPOINT ["/entry.sh"]

CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
