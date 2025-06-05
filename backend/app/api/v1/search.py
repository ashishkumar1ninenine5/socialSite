from fastapi import APIRouter, Depends
from ...infrastructure.database import get_db
from ...application.search.service import SearchService

router = APIRouter(prefix="/search", tags=["search"])

def get_database():
    return get_db()

@router.get("/")
def search(query: str, db = Depends(get_database)):
    service = SearchService(db)
    results = service.search(query)
    return {"results": [{**m, "id": str(m["_id"])} for m in results]}
