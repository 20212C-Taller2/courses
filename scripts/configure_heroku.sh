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
# Use the latest major Agent version
heroku config:add DD_AGENT_MAJOR_VERSION=7

# Enable Heroku Labs Dyno Metadata to set HEROKU_APP_NAME env variable automatically
heroku labs:enable runtime-dyno-metadata --app $APP_NAME

# Set hostname in Datadog as appname.dynotype.dynonumber for metrics continuity
heroku config:add DD_DYNO_HOST=true --app $APP_NAME

# Add this buildpack and set your Datadog API key
heroku buildpacks:add --index 1 https://github.com/DataDog/heroku-buildpack-datadog.git --app $APP_NAME

heroku config:set DD_API_KEY=<datadog_api_key> --app $APP_NAME
heroku config:set DD_DYNO_HOST=false --app $APP_NAME
heroku config:set DD_APM_ENABLED=true --app $APP_NAME
heroku config:set DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true --app $APP_NAME
