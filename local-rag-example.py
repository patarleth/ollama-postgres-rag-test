import psycopg2

# the knowledge base
dummy_data_korea = [
    {"title": "Seoul Tower", "content": "Seoul Tower is a communication and observation tower located on Namsan Mountain in central Seoul, South Korea."},
    {"title": "Gwanghwamun Gate", "content": "Gwanghwamun is the main and largest gate of Gyeongbokgung Palace, in Jongno-gu, Seoul, South Korea."},
    {"title": "Bukchon Hanok Village", "content": "Bukchon Hanok Village is a Korean traditional village in Seoul with a long history."},
    {"title": "Myeong-dong Shopping Street", "content": "Myeong-dong is one of the primary shopping districts in Seoul, South Korea."},
    {"title": "Dongdaemun Design Plaza", "content": "The Dongdaemun Design Plaza is a major urban development landmark in Seoul, South Korea."}
]

dummy_data_mozart = [
    {"title": "Wolfgang Amadeus Mozart", "content": 'When Mozart was feeling a bit sleepy he played a popular card game similar to Pokemon'},
]

dummy_data = [
  {
    "title": "October 2024 Meetings in West Hartford",
    "content": "On Monday October 28 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Sustainable West Hartford Commission, held at Town Hall, Room 407.\nOn Monday October 28 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Sustainable West Hartford Commission, held at Town Hall, Room 407.\nOn Monday October 28 2024 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Historic District Commission, held at Town Hall, Room 312."
  },
  {
    "title": "November 2024 Meetings in West Hartford",
    "content": "On Monday November 4 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Town Plan & Zoning Commission, held at Town Hall - Room 314 - Agenda.\nOn Monday November 4 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Town Plan & Zoning Commission, held at Town Hall - Room 314 - Agenda.\nOn Wednesday November 6 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Human Rights Commission, held at Elmwood Community & Senior Center.\nOn Tuesday November 12 2024 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Mayor's Youth Council, held at Town Hall, Room 217.\nOn Tuesday November 12 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Pedestrian and Bicycle Commission, held at Town Hall - Room 400.\nOn Tuesday November 12 2024 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Thursday November 14 2024 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.\nOn Thursday November 14 2024 at 5:00 PM, the town of West Hartford in CT is holding a meeting for the Prevention Council, held at Town Hall, Room 217.\nOn Monday November 18 2024 at 7:45 AM, the town of West Hartford in CT is holding a meeting for the Pension Board, held at Town Hall, Room 407.\nOn Monday November 18 2024 at 5:30 PM, the town of West Hartford in CT is holding a meeting for the Parks & Recreation Advisory Board, held at Elmwood Community Center.\nOn Monday November 18 2024 at 6:30 PM, the town of West Hartford in CT is holding a meeting for the Commission on the Arts, held at Virtual.\nOn Monday November 18 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Advisory Commission for Persons with Disabilities, held at Elmwood Community Center, Auditorium.\nOn Tuesday November 19 2024 at 10:00 AM, the town of West Hartford in CT is holding a meeting for the Senior Citizens Advisory Commission, held at Bishop's Corner Senior Center, 15 Starkel Rd.\nOn Wednesday November 20 2024 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Civilian Police Review Board, held at Town Hall - Room 400.\nOn Monday November 25 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Sustainable West Hartford Commission, held at Town Hall, Room 407.\nOn Tuesday November 26 2024 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "December 2024 Meetings in West Hartford",
    "content": "On Tuesday December 3 2024 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Mayor's Youth Council, held at Town Hall, Room 217.\nOn Tuesday December 3 2024 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Mayor's Youth Council, held at Town Hall, Room 217.\nOn Wednesday December 4 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Human Rights Commission, held at Elmwood Community & Senior Center.\nOn Monday December 9 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Pedestrian and Bicycle Commission, held at Town Hall - Room 400.\nOn Tuesday December 10 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Veterans' Affairs Commission, held at Town Hall - Room 407.\nOn Tuesday December 10 2024 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Thursday December 12 2024 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.\nOn Thursday December 12 2024 at 5:00 PM, the town of West Hartford in CT is holding a meeting for the Prevention Council, held at Town Hall, Room 217.\nOn Tuesday December 17 2024 at 10:00 AM, the town of West Hartford in CT is holding a meeting for the Senior Citizens Advisory Commission, held at Bishop's Corner Senior Center, 15 Starkel Rd.\nOn Wednesday December 18 2024 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Civilian Police Review Board, held at Town Hall - Room 400.\nOn Monday December 30 2024 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Sustainable West Hartford Commission, held at Town Hall, Room 407."
  },
  {
    "title": "January 2025 Meetings in West Hartford",
    "content": "On Thursday January 9 2025 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.\nOn Thursday January 9 2025 at 8:00 AM, the town of West Hartford in CT is holding a meeting for the Board of Assessors, held at Town Hall - Room 142.\nOn Tuesday January 14 2025 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Mayor's Youth Council, held at Town Hall, Room 217.\nOn Tuesday January 14 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Wednesday January 15 2025 at 6:00 PM, the town of West Hartford in CT is holding a meeting for the Civilian Police Review Board, held at Town Hall - Room 400.\nOn Tuesday January 21 2025 at 10:00 AM, the town of West Hartford in CT is holding a meeting for the Senior Citizens Advisory Commission, held at Bishop's Corner Senior Center, 15 Starkel Rd.\nOn Monday January 27 2025 at 5:30 PM, the town of West Hartford in CT is holding a meeting for the Parks & Recreation Advisory Board, held at Elmwood Community Center.\nOn Monday January 27 2025 at 6:30 PM, the town of West Hartford in CT is holding a meeting for the Commission on the Arts, held at Virtual.\nOn Monday January 27 2025 at 7:00 PM, the town of West Hartford in CT is holding a meeting for the Sustainable West Hartford Commission, held at Town Hall, Room 407.\nOn Monday January 27 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Historic District Commission, held at Town Hall, Room 312.\nOn Tuesday January 28 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "February 2025 Meetings in West Hartford",
    "content": "On Tuesday February 11 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday February 11 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday February 25 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "March 2025 Meetings in West Hartford",
    "content": "On Tuesday March 11 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday March 11 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday March 25 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "April 2025 Meetings in West Hartford",
    "content": "On Tuesday April 8 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday April 8 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Monday April 21 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "May 2025 Meetings in West Hartford",
    "content": "On Tuesday May 13 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday May 13 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday May 27 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "June 2025 Meetings in West Hartford",
    "content": "On Tuesday June 10 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday June 10 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday June 24 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "September 2025 Meetings in West Hartford",
    "content": "On Tuesday September 9 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday September 9 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Monday September 29 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "October 2025 Meetings in West Hartford",
    "content": "On Tuesday October 14 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday October 14 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday October 28 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  },
  {
    "title": "November 2025 Meetings in West Hartford",
    "content": "On Wednesday November 12 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Wednesday November 12 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314.\nOn Tuesday November 18 2025 at 7:30 PM, the town of West Hartford in CT is holding a meeting for the Town Council, held at Town Hall, Room 314."
  }
]

def connect_db(ollama_host):
    conn = psycopg2.connect( # use the credentials of your postgresql database 
        host = 'host.docker.internal',
        database = 'postgres',
        user = 'postgres',
        password = 'password',
        port = '5432'
    )
    with conn:
        with conn.cursor() as cur:
            cur.execute(f"select set_config('ai.ollama_host', '{ollama_host}', false);")
    return conn

def init_db_table_data(conn):
    # make table
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                    CREATE TABLE IF NOT EXISTS documents (
                        id SERIAL PRIMARY KEY,
                        title TEXT,
                        content TEXT,
                        embedding VECTOR(768)
                    );
                """)
        with conn.cursor() as cur:
            cur.execute(f"select count(*) from documents")
            rows = cur.fetchall()
            docCount = rows[0][0]
            if docCount == 0:
                with conn.cursor() as cur:
                    # use the port at which your ollama service is running.
                    for doc in dummy_data:
                        cur.execute("""
                            INSERT INTO documents (title, content, embedding)
                            VALUES (
                                %(title)s,
                                %(content)s,
                                ai.ollama_embed('nomic-embed-text', concat(%(title)s, ' - ', %(content)s))
                            )
                        """, doc)
                # finally run a query
                with conn.cursor() as cur:                
                    cur.execute("""
                        SELECT title, content, vector_dims(embedding) 
                        FROM documents;
                    """)

                    rows = cur.fetchall()
                    print(f"number of docs inserted {len(rows)}")
                    # for row in rows:
                    #     print(f"Title: {row[0]}, Content: {row[1]}, Embedding Dimensions: {row[2]}")

def sample_ollama_embed(conn, query) -> str:
    context=''
    with conn:
        with conn.cursor() as cur:
            # Embed the query using the ollama_embed function
            cur.execute("""
                SELECT ai.ollama_embed('nomic-embed-text', '%s');
            """ % (query))
            query_embedding = cur.fetchone()[0]

            # Retrieve relevant documents based on cosine distance
            cur.execute("""
                SELECT title, content, 1 - (embedding <=> '%s') AS similarity
                FROM documents
                ORDER BY similarity DESC
                LIMIT 12;
            """ % query_embedding)

            rows = cur.fetchall()
                
            # Prepare the context for generating the response
            context = "\n\n".join([f"Title: {row[0]}\nContent: {row[1]}" for row in rows])
            # print(context)
    return context

def sample_ollama_generate(conn, context, query):
    print(f"query: {query}\n")

    with conn.cursor() as cur:
        genStr = f"DOCUMENT:\n{context}\n\nQUESTION:\n{query}\n\nINSTRUCTIONS:\n"
        genStr = genStr + "Answer the users QUESTION using the DOCUMENT text above.\nKeep your answer ground in the facts of the DOCUMENT.\nIf the DOCUMENT doesn’t contain the facts to answer the QUESTION then please say so."

        cur.execute("SELECT ai.ollama_generate('llama3.2', (%s))",
                    (genStr, ))
            
        model_response = cur.fetchone()[0]
        print(model_response['response'])

# query = "Tell me about gates in South Korea."
query = "What West Hartford CT meetings scheduled in November 2024 that were in the morning?"

ollama_host = 'http://host.docker.internal:11434'

conn = connect_db(ollama_host)

try:
    init_db_table_data(conn)
    context = sample_ollama_embed(conn, query)
    sample_ollama_generate(conn, context, query)
finally:
    conn.close()
