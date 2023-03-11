FROM python:3.10

WORKDIR /code
COPY . /code
RUN pip install pipenv
RUN pipenv install --system --deploy

CMD [ "uvicorn" , "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080", "--reload"]