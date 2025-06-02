import sys

file_content = sys.stdin.read()
prompt = "Review the following code. Analyze for:\n\nPotential bugs (e.g., logical errors, edge cases, incorrect variable usage).\n\nPerformance issues (e.g., inefficient loops, redundant computations).\n\nReadability improvements (e.g., unclear variable names, lack of structure).\n\nPEP 8/style deviations (e.g., indentation, spacing, naming conventions).\n\nReturn your response in this format:\n\nOriginal code:\n\n{Code snippet with identified issues}\n\nUpdated code:\n\n{Revised code addressing the issues}\n\nPurpose of change:\n\n{Concise explanation of the problem and how the update resolves it}\n\nIf multiple issues exist, address them sequentially in separate sections. Prioritize critical bugs and major style violations.\n\n"
prompt += {file_content} + "\n"
print(prompt)
