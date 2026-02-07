import os
from openai import OpenAI

key ="sk-proj-VQsydctp1UMWeWFbMZAP1bJUI66vRDG-3nYTGzG-m9iHHrK6CCe3KGrXCtiZBpeD2Q vLZF3nrrT3BlbkFJkD-sG_W_nKmQxXilPN2fcvfgvFeVb1PLz5C7j2HQRPyks6das0xhGx2BxNH OzPLIQMQTdmszUA"

client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

response = client.responses.create(
    model="gpt-5.2",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)