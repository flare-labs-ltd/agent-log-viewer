# Log Viewer Service

A minimal dockerized python code for exposing files within a specified directory via http. To setup, run

```bash
cp .env.example .env
```

and fill in the .env file with required fields, then run

```bash
docker build . -t log-viewer && docker compose up -d
```

To expose via nginx, append the below configuration:

```text
location /view-logs {
    proxy_pass http://127.0.0.1:{API_PORT};
    rewrite ^/view-logs/(.*)$ /$1 break;
}
```

To allow access only from selected IP, prepend

```text
allow IP;
deny all;
```

to the above nginx /view-logs location rule.

To authenticate access for user <username> via basic auth, run

```bash
sudo sh -c "echo -n '<username>:' >> /etc/nginx/.htpasswd"
sudo sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"
```

then prepend the below configuration to the above nginx /view-logs location rule

```text
auth_basic "Restricted Content";
auth_basic_user_file /etc/nginx/.htpasswd;
```
