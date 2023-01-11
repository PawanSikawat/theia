from pulumi import ResourceOptions, export
from typing import Optional
from pulumi_aws.iam import Role, RoleArgs, Policy, PolicyArgs


class IAMRoleInherited(Role):
    resource_name: str
    args: Optional[RoleArgs] = None
    opts: Optional[ResourceOptions] = None

    def check_args(self, args: RoleArgs) -> bool:
        return True
        if args.tags is None or not len(args.tags):
            return False
    def __init__(self, *, name: str, args: Optional[RoleArgs] = None, opts: Optional[ResourceOptions] = None) -> None:
        if args is not None and not self.check_args(args):
            raise TypeError("Please check input values")
        self.resource_name = name
        self.args = args
        self.opts = opts
    def create(self) -> None:
        super().__init__(self.resource_name, self.args, self.opts)
        export(self.name, vars(self.args))
    @classmethod
    def get(cls, name) -> Role:
        return super().get(name)


class IAMPolicyInherited(Policy):
    resource_name: str
    args: Optional[PolicyArgs] = None
    opts: Optional[ResourceOptions] = None

    def check_args(self, args: PolicyArgs) -> bool:
        return True
        if args.tags is None or not len(args.tags):
            return False
    def __init__(self, *, name: str, args: Optional[PolicyArgs] = None, opts: Optional[ResourceOptions] = None) -> None:
        if args is not None and not self.check_args(args):
            raise TypeError("Please check input values")
        self.resource_name = name
        self.args = args or PolicyArgs()
        self.opts = opts
    def create(self) -> None:
        super().__init__(self.resource_name, self.args, self.opts)
        export(self.resource_name, vars(self.args))
