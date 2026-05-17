from app.llm import generate_response

prompt = "Say hello in one short sentence."

response = generate_response(prompt)

print(response)