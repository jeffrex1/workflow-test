import sys
from openai import OpenAI

# Read the file content from standard input
file_content = sys.stdin.read()

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "${{ secrets.LLM_API_KEY }}"
)

completion = client.chat.completions.create(
  model="deepseek-ai/deepseek-r1",
  messages=[{"role":"user","content":f"Review the following Python code. Provide concise feedback focusing on potential bugs, areas for improvement (readability, performance), and any significant deviations from common Python best practices or style guides (like PEP 8, if applicable). Keep the review brief and to the point.\n\n```python\n{file_content}\n```"}],
  temperature=0.6,
  top_p=0.7,
  max_tokens=4096,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
