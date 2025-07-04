from fastapi import FastAPI, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from .database import async_session, init_db
from .schemas import NoteCreate, NoteOut
from .crud import create_note, get_all_notes

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@app.post("/notes", response_model=NoteOut)
async def add_note(note: NoteCreate, session: AsyncSession = Depends(get_session)):
    return await create_note(note, session)

@app.get("/notes", response_model=list[NoteOut])
async def read_notes(session: AsyncSession = Depends(get_session)):
    return await get_all_notes(session)
