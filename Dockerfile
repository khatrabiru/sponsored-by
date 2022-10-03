FROM python:3.10
WORKDIR /code

COPY ./app /code/app
COPY ./requirements.txt /code

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--reload"]