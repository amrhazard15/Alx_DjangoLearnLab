# Social Media API Deployment

## Deployment Overview
This Django REST API was prepared for production deployment using Heroku.

## Production Settings
- DEBUG set to False
- ALLOWED_HOSTS configured
- Security settings enabled
- Gunicorn used as WSGI server

## Static Files
Static files are collected using Django collectstatic.

## Hosting Service
- Platform: Heroku
- WSGI Server: Gunicorn
- Database: PostgreSQL

## Environment Variables
- SECRET_KEY
- DEBUG
- DATABASE_URL

## Live URL
https://example-social-media-api.herokuapp.com/
