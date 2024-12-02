select ai.ollama_generate
( 'llama3.2'
, 'what is the typical weather like in Alabama in June'
, host=>'http://host.docker.internal:11434' -- tells pgai that Ollama is running on the host when pgai is in a docker container
);

select set_config('ai.ollama_host', 'http://host.docker.internal:11434', false);

select ai.ollama_embed
( 'llama3.2'
, 'the purple elephant sits on a red mushroom'
);

