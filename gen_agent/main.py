from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
# from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
# from llama_index.core.embeddings import resolve_embed_model

llm = Ollama(model="llama3.2", request_timeout=30.0)
result = llm.complete("Hello Machaaa")
print(result)


prompt_template = LlamaParse().__str__