from typing import List

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from searchweb import search




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return JSONResponse(
        content={"message": "DataOrchestra API is online and ready to use!"}
    )


@app.post("/search/{query}/{lim}", status_code=status.HTTP_200_OK)
async def result_search(query: str, lim: int):
    try:
        results = await search(query, lim)
        # `search` returns a list of URL strings, so we can return it directly
        return JSONResponse(content=results, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST
        )


@app.post("/search/pdfs/{query}/{limits}", status_code=status.HTTP_200_OK)
async def search_pdfs(query: str, limits: int):
    try:
        raw_results = await search(f"filetype:pdf {query}", limits)
        urls = []
        for result in raw_results:
            urls.append(result)
        return JSONResponse(content=urls, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/search/repositories/{query}/{limit}", status_code=status.HTTP_200_OK)
async def search_repositories(query: str, limit: int):
    try:
        res = []
        s = await search(f"{query} site:github.com", limit)
        res.extend(s)
        s = await search(f"{query} site:gitlab.com", limit)
        res.extend(s)
        return JSONResponse(content=res, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.post("/search/wikipedia/{query}/{max_results}", status_code=status.HTTP_200_OK)
async def search_wikipedia(query: str, max_results: int):
    try:
        merged = []
        res = await search(f"{query} site:wikipedia.org", max_results)
        merged.extend(res)
        res = await search(f"{query} site:wikibooks.org", max_results)
        merged.extend(res)
        res = await search(f"{query} site:wiktionary.org", max_results)
        merged.extend(res)
        res = await search(f"{query} site:grokipedia.com", max_results)
        merged.extend(res)
        res = await search(f"{query} site:wikiquote.org", max_results)
        merged.extend(res)
        res = await search(f"{query} site:wikisource.org", max_results)
        merged.extend(res)
        return JSONResponse(content=merged, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )