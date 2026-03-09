import requests

def call_llm_api(prompt, api_key, model="gpt-3.5-turbo"):
    """
    Call an LLM API (OpenAI example)
    
    Args:
        prompt: The input prompt
        api_key: Your API key
        model: The model to use
    
    Returns:
        The API response text
    """
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    return response.json()["choices"][0]["message"]["content"]


if __name__ == "__main__":
    api_key = "your-api-key-here"
    result = call_llm_api("Hello, how are you?", api_key)
    print(result)