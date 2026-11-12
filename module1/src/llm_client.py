import os

from aisuite import Client
from dotenv import load_dotenv

load_dotenv()


def make_client() -> Client:
    """Build the aisuite client.

    If ANTHROPIC_WORKSPACE_ID is set, send it as the `anthropic-workspace-id`
    header (needed when the API key is not scoped to a single workspace).
    """
    workspace_id = os.getenv("ANTHROPIC_WORKSPACE_ID")
    if workspace_id:
        return Client(
            provider_configs={
                "anthropic": {
                    "default_headers": {"anthropic-workspace-id": workspace_id}
                }
            }
        )
    return Client()
