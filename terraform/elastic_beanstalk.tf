resource "aws_elastic_beanstalk_application" "application" {
    name = "flaskbb"  
}
# CoRise TODO: change cname_prefix to reflect your unique application name
# test PR
resource "aws_elastic_beanstalk_environment" "environment" {
  name                = "flaskbb-environment"
  cname_prefix        = "hzarkoobflaskbb"
  application         = aws_elastic_beanstalk_application.application.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.0.1 running Python 3.11"
  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = "aws-elasticbeanstalk-ec2-role"
  }
}