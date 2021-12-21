#!/bin/bash
# IMPORTANT: before running this script ensure to run heroku login

set -e

heroku apps:create $APP_NAME
heroku addons:create heroku-postgresql:hobby-dev --app $APP_NAME
heroku config:set LOG_LEVEL=<CRITICAL|ERROR|WARNING|INFO|DEBUG|NOTSET> --app $APP_NAME
heroku config:set HOST_SUBSCRIPTIONS_API=<host> --app $APP_NAME
heroku config:set HOST_USERS_API=<host> --app $APP_NAME


# DataDog
# Enable Heroku Labs Dyno Metadata to set HEROKU_APP_NAME env variable automatically
# heroku labs:enable runtime-dyno-metadata -a $APP_NAME
heroku config:set DD_API_KEY=<datadog_api_key> --app $APP_NAME
heroku config:set DD_DYNO_HOST=false --app $APP_NAME
heroku config:set DD_APM_ENABLED=true --app $APP_NAME
heroku config:set DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true --app $APP_NAME
