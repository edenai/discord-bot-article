from phoenix.otel import register
import os
from dotenv import load_dotenv

load_dotenv()

tracer_provider = register(
    project_name="discord-bot",
    endpoint=os.getenv("PHOENIX_COLLECTOR_ENDPOINT") + "/v1/traces",
    protocol="http/protobuf",
)

instrumenting_module_name = "rag.ask_llm"
