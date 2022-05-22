FROM python:3.7-slim-buster

RUN pip install --upgrade pip \
&& pip install --upgrade setuptools

RUN adduser --force-badname 1000

WORKDIR /app

USER 1000

ENV PATH=/home/1000/.local/bin:$PATH

COPY --chown=1000:1000 requirements.txt /app/requirements.txt

RUN pip install --user -r requirements.txt

COPY --chown=1000:1000 . /app

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=1", "--threads=15", "run:app"]