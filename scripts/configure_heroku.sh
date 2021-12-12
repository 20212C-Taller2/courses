#!/bin/bash
# IMPORTANT: before running this script ensure to run heroku login!!!!

set -e

heroku apps:create $APP_NAME
heroku addons:create heroku-postgresql:hobby-dev --app $APP_NAME
heroku config:set HOST_SUBSCRIPTIONS_API=<host> --app $APP_NAME
heroku config:set LOG_LEVEL=<CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET> --app $APP_NAME
