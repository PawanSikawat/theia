from fastapi import FastAPI
import uvicorn
from derived import router as derived_router



app = FastAPI()
for router in derived_router:
    app.include_router(router.router)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=2)

