from fastapi import APIRouter, Request, HTTPException, BackgroundTasks

from ..services.crawl import run_scraper

router = APIRouter()
