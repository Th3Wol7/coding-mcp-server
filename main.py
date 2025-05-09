import json
import os

import httpx
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL = "https://google.serper.dev/search"

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
    "python": "docs.python.org/3",
    "nextjs": "nextjs.org/docs",
    "reactjs": "reactjs.org/docs",
    "spring": "docs.spring.io/spring-framework/reference",
    "spring-boot": "docs.spring.io/spring-boot/docs/3.2.5/reference/htmlsingle",
}


async def search_web(query: str) -> dict | None:
    payload = json.dumps({"q": query, "num": 2})

    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                SERPER_URL, headers=headers, data=payload, timeout=30.0
            )
            response.raise_for_status()
            return response.json()
        except httpx.TimeoutException:
            return {"organic": []}


async def fetch_url(url: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text()
            return text
        except httpx.TimeoutException:
            return "Timeout error: request timeout"


@mcp.tool()
async def get_docs(query: str, library: str):
    """
    Search the docs for a given query and library.
    Supports langchain, openai, llama-index, python, nextjs, reactjs, spring and spring-boot.

    Args:
        str:param query: The query to search for (e.g. "PYTorch")
        str:param library: The library to search in (e.g. "python")

    Returns:
        Text from the documentation.
    """
    if library not in docs_urls:
        raise ValueError(f"Library {library} is not supported by this tool")

    query = f"site:{docs_urls[library]} {query}"
    results = await search_web(query)

    if len(results["organic"]) == 0:
        return "No organic results found"

    text = ""
    for result in results["organic"]:
        text += await fetch_url(result["link"])
        return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mcp.run(transport="stdio")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
