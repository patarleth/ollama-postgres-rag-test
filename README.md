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

Grouped the WEHA town council meetings by month and year. Data sourced from ical docs https://www.westhartfordct.gov/government-services/meetings-agendas

The 3 generated (morning) meeting strings for the doc titled "November 2024 Meetings in West Hartford"
```
Thursday November 14 2024 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.
Monday November 18 2024 at 7:45 AM, the town of West Hartford in CT is holding a meeting for the Pension Board, held at Town Hall, Room 407.
Tuesday November 19 2024 at 10:00 AM, the town of West Hartford in CT is holding a meeting for the Senior Citizens Advisory Commission, held at Bishop's Corner Senior Center, 15 Starkel Rd.
```

The thought behind a document with this structure is to organize the data for RAG grouped with 'similar' meetings into a individual docs for the vector store.

Using the postgres ai extension and select the query as ollama_embed

```
    cur.execute("""
        SELECT ai.ollama_embed('nomic-embed-text', '%s');
    """ % (query,))
    query_embedding = cur.fetchone()[0]

    # Retrieve relevant documents based on cosine distance
    cur.execute(f"SELECT title, content FROM documents ORDER BY embedding <=> %s LIMIT 30", (query_embedding,))
```

I modeled the actual RAG query after this dudes - 

https://www.raphaelbauer.com/posts/custom-llm-with-rag/

The query fails to find any meetings and returns this string - 

```
Based on the provided DOCUMENT, there is no information about meetings scheduled in November 2024, let alone morning meetings. The DOCUMENT only contains meeting schedules for 2025, starting from February.
```

SOOOOOOOO the query to find the relative meeting docs from the vector store is returning...


February?

Of course the easiest way to get the query to (almost) work is by expanding the number of docs returned from the vector to 12 (aka all the meetings).

This returns -

```
According to the document, there are two West Hartford CT meetings scheduled in November 2024 that were in the morning:

1. Thursday, November 14, 2024 at 8:00 AM - meeting for the Board of Assessors, held at Town Hall - Room 142.
2. Thursday, November 14, 2024 at 5:00 PM is not a morning meeting, but another one is:
Thursday, November 14, 2024 at 8:00 AM is correct and 
Tuesday, November 12, 2024 at 6:00 PM is not in the morning so we look for 
Monday, November 18, 2024 at 7:45 AM - meeting for the Pension Board, held at Town Hall, Room 407.
These are the two meetings scheduled in November 2024 that were in the morning.
```

sigh...