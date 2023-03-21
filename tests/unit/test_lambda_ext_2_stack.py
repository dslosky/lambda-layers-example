import aws_cdk as core
import aws_cdk.assertions as assertions
from lambda_ext_2.lambda_ext_2_stack import LambdaExt2Stack


def test_sqs_queue_created():
    app = core.App()
    stack = LambdaExt2Stack(app, "lambda-ext-2")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = LambdaExt2Stack(app, "lambda-ext-2")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
