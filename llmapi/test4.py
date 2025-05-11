import json

# Sample response object
response = {
    "id": "resp_6820bc6fb0dc819194c86d9a4053f612031de1ee71582e23",
    "created_at": 1746975855.0,
    "error": None,
    "incomplete_details": None,
    "instructions": None,
    "metadata": {},
    "model": "gpt-4.1-nano-2025-04-14",
    "object": "response",
    "output": [
        {
            "id": "msg_6820bc6fdc508191ab37d432bfe80536031de1ee71582e23",
            "content": [
                {
                    "annotations": [],
                    "text": "The capital of India is New Delhi.",
                    "type": "output_text"
                }
            ],
            "role": "assistant",
            "status": "completed",
            "type": "message"
        }
    ],
    "parallel_tool_calls": True,
    "temperature": 1.0,
    "tool_choice": "auto",
    "tools": [],
    "top_p": 1.0,
    "max_output_tokens": None,
    "previous_response_id": None,
    "reasoning": {
        "effort": None,
        "generate_summary": None,
        "summary": None
    },
    "service_tier": "default",
    "status": "completed",
    "text": {
        "format": {
            "type": "text"
        }
    },
    "truncation": "disabled",
    "usage": {
        "input_tokens": 14,
        "input_tokens_details": {
            "cached_tokens": 0
        },
        "output_tokens": 9,
        "output_tokens_details": {
            "reasoning_tokens": 0
        },
        "total_tokens": 23
    },
    "user": None,
    "store": True
}

# Extracting the text
output_text = response["output"][0]["content"][0]["text"]
print(output_text)