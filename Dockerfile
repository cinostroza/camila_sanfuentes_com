###########
# BUILDER #
###########

# pull official base image
FROM python:3.10.8-alpine as builder

# set work directory
WORKDIR /usr/src/camila_sanfuentes_com

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip
# RUN pip install flake8==3.9.2
COPY . .
# RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/camila_sanfuentes_com/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.10.8-alpine

# create directory for the app user
RUN mkdir -p /home/camila_sanfuentes_com

# create the app user
RUN addgroup -S camila_sanfuentes_com && adduser -S camila_sanfuentes_com -G camila_sanfuentes_com

# create the appropriate directories
ENV HOME=/home/camila_sanfuentes_com
ENV APP_HOME=/home/camila_sanfuentes_com/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
COPY --from=builder /usr/src/camila_sanfuentes_com/wheels /wheels
COPY --from=builder /usr/src/camila_sanfuentes_com/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.prod.sh
COPY ./entrypoint.prod.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.prod.sh
RUN chmod +x  $APP_HOME/entrypoint.prod.sh

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R camila_sanfuentes_com:camila_sanfuentes_com $APP_HOME

# change to the app user
USER camila_sanfuentes_com

# run entrypoint.prod.sh
ENTRYPOINT ["/home/camila_sanfuentes_com/web/entrypoint.prod.sh"]