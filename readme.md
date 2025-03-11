# Log Viewer Service

A minimal dockerized python code for exposing files within a specified directory via http. To setup, run

```bash
cp .env.example .env
```

and fill in the .env file with required fields, then run

```bash
docker build . -t log-viewer && docker compose up -d
```

To expose via nginx, append the below configuration (assuming .env port was left unchanged at 57005)

```text
location /view-logs {
    proxy_pass http://127.0.0.1:57005;
    rewrite ^/view-logs/(.*)$ /$1 break;
}
```

To allow access only from selected IP, prepend

```text
allow 188.230.128.78;
deny all;
```

to the above nginx /view-logs location rule.
