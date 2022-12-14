FROM esirk/python3.10-base-with-pycopg2
WORKDIR /app
COPY . /app/
RUN pip3 install poetry \
&& pip3 install psycopg[binary,pool] \
&& poetry config virtualenvs.create false \
&& poetry add psycopg[binary,pool] \
&& poetry add psycopg2 \
&& poetry install
CMD python manage.py migrate && \
   python manage.py runserver 0.0.0.0:8080
EXPOSE 8080