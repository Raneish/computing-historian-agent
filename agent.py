import logging
logging.getLogger("azure").setLevel(logging.ERROR)

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "your-endpoint-here"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "computing-historian"
my_version = "1"

openai_client = project_client.get_openai_client()

print("Computing Historian Agent ready. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("Exiting. Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = openai_client.responses.create(
            input=[{"role": "user", "content": user_input}],
            extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
        )

        if response.output_text:
            print(f"\nAgent: {response.output_text}\n")
        else:
            print(f"\n[Debug] Empty response. Full response object: {response}\n")

    except Exception as e:
        print(f"\n[Error] {e}\n")