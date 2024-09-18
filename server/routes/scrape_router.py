from fastapi import APIRouter, Request, HTTPException, BackgroundTasks

from ..services.crawl import run_scraper

router = APIRouter()


@router.post("/scrape")
async def scrape(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    if "query" not in body:
        raise HTTPException(status_code=400, detail="query parameter is missing")

    background_tasks.add_task(run_scraper, query=body["query"])

    return {"detail": f"started scraping products with search query: {body['query']}"}
