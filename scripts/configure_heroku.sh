#!/bin/bash
# IMPORTANT: before running this script ensure to run heroku login!!!!

set -e

heroku apps:create $APP_NAME
heroku addons:create heroku-postgresql:hobby-dev --app $APP_NAME
# heroku config:set FASTAPI_POSTGRESQL=postgres+psycopg2://<DATABASE_URL> --app $APP_NAME
