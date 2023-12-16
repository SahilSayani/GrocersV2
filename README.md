#

to run: 
create venv> cd backend > pip install -r requirements.txt
#
run app.py
#
redis-server
#
for celery workers 
backend> celery -A app.celery  worker
#
for celery beat 
backend>celery -A app.celery beat
#
frontend> npm run dev
