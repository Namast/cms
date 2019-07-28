[program:cms]
command=/home/namast/venv/bin/gunicorn cms.wsgi:application -c /home/namast/cms/conf/gunicorn.conf.py
directory=/home/namast/cms
user=namast
autorestart=true
redirect_stderr=true
stdout_logfile = /home/namast/cms/logs/debug.log