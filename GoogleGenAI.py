from google import genai
from google.genai import types

# Only run this block for Google AI API
client = genai.Client(api_key = 'REMOVED_FOR_GITHUB')

# Only run this block for Vertex AI API
# client = genai.Client(
#     vertexai=True, project='gen-lang-client-0985944511', location='us-central1'
# )

response = client.models.generate_content(
    model='gemini-2.0-flash-exp', contents='What is your name?'
)
print(response.text)