import boto3


class AWSExtractor(object):

    def __init__(self, resource_name):
        self.resource = boto3.resource(resource_name)
