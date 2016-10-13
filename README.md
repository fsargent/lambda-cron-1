[![Build Status](https://travis-ci.com/MediaMath/knox-lambda-cron.svg?token=tMt81cZ8XUGin1RurU5s&branch=master)](https://travis-ci.com/MediaMath/knox-lambda-cron)

# Knox Lambda Cron

Project to run scheduled tasks using lambda functions on AWS.

![diagram](/diagram.png)

Lamdba function will run once an hour, it will read all tasks available and it
will run all jobs that should run in that hour.

Tasks are saved in a S3 bucket:

```
s3://lambda-cron.prod.mmknox/tasks/
```

Task are defined in [knox-lambda-cron-tasks](https://github.com/MediaMath/knox-lambda-cron-tasks)

## Sample Task Definition

``` yaml
name: sample name
expression: "0 2 * * *"
task:
  key1: value 1
  key2: value 2
```

## Local Setup

### Requirements
- Python 2.7
- Virtual Environment
- pip
- Boto3
  - Boto3 is installed as part of the lambda functions Environment.  To aviod the overhead of including it in your deployment artifact install boto3 on your system instead of in the virtual environment
- awscli (configured)

### Setup
From the repo root dir
``` bash
$ virtualenv venv
$ pip install -r requirements.txt
```

## Diagram
The diagram was created with draw.io, using the lambda-cron.xml file in this repo

## Deployment
Deployment is automated with Travis CI:

* Branch **develop**: deploy sandbox
* Branch **staging**: deploy staging
* New **tag** version: deploy prod

## TODO & Ideas & Features

* Monitoring
    * Logs & metrics
    * Cloudwatch alerts
* Lambda code:
    * Add tag name (version) to .zip file
    * Upload .zip file directly to lambda function (not to S3) ?
    * Add tag name (version) to lambda function description ?
* Feature
    * Disable crons (Expresion = DISABLED)
    * Read only reports that must run