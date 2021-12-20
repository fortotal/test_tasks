FROM python:3.7

COPY . /app
WORKDIR app/
RUN pip install -r /app/requirements.txt

ENV FLASK_APP /app/app.py

EXPOSE 5000

CMD python app.py
