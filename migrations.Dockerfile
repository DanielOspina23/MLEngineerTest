FROM python:3.7

COPY . project/
WORKDIR project/

RUN pip install --upgrade pip
RUN pip install alembic==1.4.2 && pip install python-dotenv==0.14.0 && pip install psycopg2==2.8.5

RUN chmod +x migrations/entry-point.sh

CMD ["migrations/entry-point.sh"]
