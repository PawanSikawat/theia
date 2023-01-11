from fastapi import FastAPI
import uvicorn
from derived import router as derived_router



app = FastAPI()
for router in derived_router:
    app.include_router(router.router)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=2)



















# cp_obj = cp.Cloudport(name='cloudport-test', bucket_args=None, opts=None)
# # cp_obj.create()

# stack = auto.create_or_select_stack(
#     stack_name='theia-api',
#     project_name='demo',
#     program=cp_obj.create
# )

# # result = stack.destroy(on_output=print)
# result = stack.up(on_output=print)


