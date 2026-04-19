FROM python:3.12-alpine

ARG http_proxy
ARG https_proxy

ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy

RUN apk add gcc musl-dev
RUN adduser -D myuser
USER myuser

WORKDIR /app
COPY --chown=myuser:myuser . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]