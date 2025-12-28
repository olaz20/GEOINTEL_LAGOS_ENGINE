from fastapi import FastAPI, Depends


from .database import  engine, get_db, AsyncSessionLocal
from .security import initialize_default_admin
app = FastAPI()
from routes.auth import router as auth_router
from routes.notification import router as notification_router
from fastapi.responses import RedirectResponse

@app.on_event("startup")
async def startup():
    async with AsyncSessionLocal() as db:
        await initialize_default_admin(db)


app.include_router(auth_router)
app.include_router(notification_router)

@app.get("/", include_in_schema=False)  
async def redirect_to_docs():
    return RedirectResponse("/docs")