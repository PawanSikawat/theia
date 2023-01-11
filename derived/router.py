from fastapi import APIRouter
from pulumi import automation as auto
from derived import cloudport as cp
from models import stack
import anyio



router = APIRouter()

@router.post("/create/cloudport/{name}")
async def create_cloudport(name: str, stack: stack.Stack):
    try:
        stack_api = auto.create_or_select_stack(
            stack_name=stack.name,
            project_name=stack.project,
            program=cp.Cloudport(name=f"cloudport-{name}", bucket_args=None, opts=None).create
        )
        anyio.run(stack_api.up(on_output=print))
    except Exception as e:
        print(e)
        return {"status": False, "error": e}
    return {"status": True, "error": None}


@router.delete("/destroy/cloudport/{name}")
async def destroy_cloudport(name: str, stack: stack.Stack):
    try:
        stack_api = auto.create_or_select_stack(
            stack_name=stack.name,
            project_name=stack.project,
            program=cp.Cloudport(name=f"cloudport-{name}", bucket_args=None, opts=None).create
        )
        await stack_api.destroy(on_output=print)
    except Exception as e:
        print(e)
        return {"status": False, "error": e}
    return {"status": True, "error": None}