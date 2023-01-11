from pulumi import ResourceOptions, ComponentResource
from typing import Optional
import base.aws.s3 as s3
import base.aws.iam as iam
import json



class Cloudport(ComponentResource):
    name: str
    s3_bucket: s3.S3Inherited
    iam_policy: iam.IAMPolicyInherited
    opts: Optional[ResourceOptions] = None

    def __init__(self, *, name: str, bucket_args: s3.BucketArgs, opts: Optional[ResourceOptions] = None):
        self.name = name
        self.opts = opts
        super().__init__("amagi_managed:cloudport:s3", self.name, None, self.opts)
        self.s3_bucket = s3.S3Inherited(name=f'{name}-bucket', args=bucket_args)
        self.iam_policy = iam.IAMPolicyInherited(name=f'{name}-role', args=iam.PolicyArgs(policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": [
                        "s3:HeadBucket",
                        "s3:PutObject",
                    ],
                    "Effect": "Allow",
                    "Resource": f"arn:aws:s3:::{self.s3_bucket.bucket}/*",
                }],
            })))

    def create(self) -> None:
        self.s3_bucket.create()
        self.iam_policy.create()
