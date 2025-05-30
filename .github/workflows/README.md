# code-review.yml
This project consists of two files, `llm_review.py` and `llm_code_review.yaml`, which uses Nvidia's deepseek LLM to perform automated code reviews on Python files in Pull Requests.

## Setup and Maintainance
1.  Place the `llm_review.py` in the root directory of your repository.
2.  Place the `llm_code_review.yaml` in the `.github/workflows` directory
3.  **Add API Key Secret:**
    *   Go to your GitHub repository's settings.
    *   Navigate to "Secrets and variables" -> "Actions".
    *   Click "New repository secret".
    *   Name the secret `LLM_API_KEY`.
    *   Paste your NVIDIA API key as the value.
    *   Update key every 6 months
5.   **Add PAT Key Secret:**
     *   Go to your GitHub account settings.
     *   Navigate to "Developer settings" -> "Personal access tokens".
     *   Click "Tokens (classic)" or "Fine-grained tokens" with the relevant permissions.
     *   Copy the key (You will not be able to see it again once you leave the page).
     *   Navigate to "Repository secrets" (See step 3).
     *   Name the secret `Personal_Token`.
     *   Paste your PAT key as the value.
     *   Update key as needed
## Customization
  *   **Prompt:** Adjust the prompt in `llm_review.py`
      https://github.com/agentize/prompthon-tools/blob/82c28931c7291cfc8f4bfd4ae341bea76099bd00/llm_review.py#L12
