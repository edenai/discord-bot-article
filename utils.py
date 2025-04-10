import requests
import os
import json

from phoenix_setup import tracer_provider, instrumenting_module_name
from openinference.semconv.trace import SpanAttributes, OpenInferenceMimeTypeValues
from opentelemetry.trace import StatusCode, Status


MAX_TOKENS = 200
TIMEOUT = 60.0
LLM_SETTINGS = {
    "llm_provider": "google",
    "llm_model": "gemini-2.0-flash",
    "max_tokens": MAX_TOKENS,
    "k": 6,
    "min_score": 0.6,
}

SYSTEM_PROMPT = """You are a helpful Discord bot that answers questions and provides information to users."""


def ask_llm(query: str) -> str:
    url = f"https://api.edenai.run/v2/aiproducts/askyoda/v2/{os.getenv('RAG_PROJECT_ID')}/ask_llm"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv("API_KEY"),
    }
    payload = {
        **LLM_SETTINGS,
        "query": query,
        "chatbot_global_action": SYSTEM_PROMPT,  # You can set it directly in the ui
    }
    with tracer_provider.get_tracer(
        instrumenting_module_name=instrumenting_module_name
    ).start_as_current_span("ask_llm") as span:
        try:

            response = requests.post(
                url, headers=headers, json=payload, timeout=TIMEOUT
            )
            data = response.json()
            response.raise_for_status()

            span.set_status(Status(StatusCode.OK))

            span.set_attribute(
                SpanAttributes.INPUT_VALUE,
                query,
            )

            span.set_attribute(
                SpanAttributes.LLM_INPUT_MESSAGES,
                format_input_messages(SYSTEM_PROMPT, query),
            )

            span.set_attribute(SpanAttributes.OPENINFERENCE_SPAN_KIND, "llm")

            span.set_attribute(
                SpanAttributes.OUTPUT_VALUE,
                data["result"],
            )

            span.set_attribute(
                SpanAttributes.LLM_OUTPUT_MESSAGES,
                format_output_messages(data["result"]),
            )
            span.set_attributes(
                {
                    SpanAttributes.LLM_PROVIDER: LLM_SETTINGS["llm_provider"],
                    SpanAttributes.LLM_MODEL_NAME: LLM_SETTINGS["llm_model"],
                    SpanAttributes.LLM_INVOCATION_PARAMETERS: json.dumps(LLM_SETTINGS),
                    SpanAttributes.LLM_SYSTEM: "RAG",
                }
            )

            return data["result"]
        except Exception as e:
            span.set_status(Status(StatusCode.ERROR, str(e)))
            span.record_exception(e)
            raise


def format_input_messages(system_prompt: str, query: str) -> str:
    """Format the input messages for the LLM API."""
    return json.dumps(
        {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "text",
                            "content": {"text": system_prompt},
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "content": {"text": query},
                        }
                    ],
                },
            ]
        }
    )


def format_output_messages(llm_response: str) -> str:
    """Format the output messages from the LLM API."""
    return json.dumps(
        [
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "content": {"text": llm_response},
                    }
                ],
            }
        ]
    )
