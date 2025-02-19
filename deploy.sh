zip -r "flaskbb_deploy-$1.zip" ./flaskbb ./.ebextensions wsgi.py setup.py setup.cfg requirements.txt flaskbb.cfg celery_worker.py

aws s3 cp "flaskbb_deploy-$1.zip" s3://hzarkoob-flaskbb

aws elasticbeanstalk create-application-version --application-name hzarkoob_flaskbb --source-bundle S3Bucket="hzarkoob-flaskbb",S3Key="flaskbb_deploy-$1.zip" --version-label "ver-$1" --description "file permissions" --region "us-west-1"

aws elasticbeanstalk update-environment --environment-name flaskbb-environment --version-label "ver-$1" --region "us-west-1"