FROM python:3.10.0

RUN pip install pipenv

ADD Pipfile .
ADD Pipfile.lock .

RUN pipenv install --system --deploy

ADD auth.py .
ADD private.py .

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "80" ]

