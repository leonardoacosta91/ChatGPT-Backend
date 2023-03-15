FROM python:3.9.12

WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
ENV FLASK_APP=application
ENV FLASK_DEBUG=1

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]