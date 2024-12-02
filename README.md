# ollama demo

## simple py lib to interact w/ ollama

https://github.com/ollama/ollama-python

    python -m venv .venv (vscode ask if you want to use)
    .venv/bin/pip install ollama
    then run with
    .venv/bin/python ollama_test.py

---

## chainlit full python lib to build chat bots

https://docs.chainlit.io/get-started/overview


## RAG data

Group WEHA town council meetings by month year. Data sourced from ical docs https://www.westhartfordct.gov/government-services/meetings-agendas

The 4 generated (morning) meeting strings for the doc titled "November 2024 Meetings in West Hartford"

```
    On Monday November 4 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Town Plan & Zoning Commission, held at Town Hall - Room 314 - Agenda.
```
...
```
    On Thursday November 14 2024 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.
```
...
```
    On Monday November 18 2024 at 7:45 AM, the town of West Hartford in CT is holding a meeting for the Pension Board, held at Town Hall, Room 407.
```
...
```
    On Tuesday November 19 2024 at 10:00 AM, the town of West Hartford in CT is holding a meeting for the Senior Citizens Advisory Commission, held at Bishop's Corner Senior Center, 15 Starkel Rd.
```

The thought behind a document with this structure is to organize the data for RAG grouped with 'similar' meetings into a individual docs for the vector store.

Using the postgres ai extension and select the query as ollama_embed

```
    cur.execute("""
        SELECT ai.ollama_embed('llama3.2', '%s');
    """ % (query))
    query_embedding = cur.fetchone()[0]

    # Retrieve relevant documents based on cosine distance
    cur.execute("""
        SELECT title, content, 1 - (embedding <=> '%s') AS similarity
        FROM documents
        ORDER BY similarity DESC
        LIMIT 3;
    """ % query_embedding)
```

I modeled the actual RAG query after this dudes - 

https://www.raphaelbauer.com/posts/custom-llm-with-rag/

The query fails to find any meetings and returns this string - 

```
Based on the provided DOCUMENT, there is no information about meetings scheduled in November 2024, let alone morning meetings. The DOCUMENT only contains meeting schedules for 2025, starting from February.
```

SOOOOOOOO the query to find the relative meeting docs from the vector store is returning...


February?


More to come..