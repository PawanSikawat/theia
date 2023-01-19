from pulumi import ResourceOptions, export
from typing import Optional
from pulumi_aws.s3 import Bucket, BucketArgs, CannedAcl



class S3Inherited(Bucket):
    name: str
    args: Optional[BucketArgs] = None
    opts: Optional[ResourceOptions] = None

    def check_args(self, args: BucketArgs) -> bool:
        return True
        if args.lifecycle_rules is None:
            return False
        if args.tags is None or not len(args.tags):
            return False
        if args.acl in {CannedAcl.PUBLIC_READ, CannedAcl.PUBLIC_READ_WRITE}:
            return False
    def __init__(self, *, name: str, args: Optional[BucketArgs] = None, opts: Optional[ResourceOptions] = None) -> None:
        if args is not None and not self.check_args(args):
            raise TypeError("Please check input values")
        self.name = name
        self.args = args or BucketArgs()
        self.opts = opts
    def create(self) -> None:
        super().__init__(resource_name=self.name, opts=self.opts, **vars(self.args))
        export(self.name, self)
    @classmethod
    def get(cls, name, id) -> Bucket:
        return super().get(name, id)
    
