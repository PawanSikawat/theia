
from pulumi import automation as auto
from derived import cloudport as cp
from base.aws.s3 import S3Inherited, BucketArgs
from models import stack


# Stack
curr_stack = stack.Stack(name="theia-api", project="demo")
name = "test1"

# Bucket Obj
s3_bucket = S3Inherited.get("cloudport-test1-bucket", "cloudport-test1-bucket-4ef648f")

# New Bucket Args
new_args = BucketArgs(acl=cp.s3.CannedAcl.PUBLIC_READ, tags={'foo': 'bar'})

# Update args
filtered_args = {k: v for k, v in vars(s3_bucket).items() if k in BucketArgs.__init__.__code__.co_varnames}
filtered_args.update(vars(new_args))
filtered_args = BucketArgs(**filtered_args)


# Cloudport obj
cloudport = cp.Cloudport(name=f"cloudport-{name}", bucket_args=filtered_args)


# Stack commands
stack_api = auto.create_or_select_stack(
    stack_name=curr_stack.name,
    project_name=curr_stack.project,
    program=cloudport.create
)

stack_api.up(on_output=print)


'''
-- Current
Cloudport
    S3 (acl=foo, tags=bar)
    IAM

-- Update
Cloudport
    S3 (tags=bar1)
    IAM ()

-- New
Cloudport
    S3 (acl=foo, tags=bar1)
    IAM
'''
