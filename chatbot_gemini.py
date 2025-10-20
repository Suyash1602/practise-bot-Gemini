from google import genai
from google.genai.errors import APIError


class ChatbotGemini:
    """
    A class to interact with the Google Gemini models using the genai SDK.
    """

    def __init__(self, api_key, model= 'gemini-2.5-flash', temperature= 0.5):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

        # 1. Initialize the client
        self.client = genai.Client(api_key=self.api_key)

    def ask(self, user_input: str) -> str:
        """
        Generates content from the model based on user input.
        """
        try:
            # 2. Call the generate_content method.
            response = self.client.models.generate_content(
                model=self.model,
                contents=user_input,
                config={
                    "temperature": self.temperature
                }
            )
            return response.text

        except APIError as e:
            # Handle specific API-related errors
            return f"An API error occurred: {e}"
        except Exception as e:
            # Handle any other unexpected errors
            return f"An unexpected error occurred: {str(e)}"


api_key = "YOUR_API_KEY"
bot = ChatbotGemini(api_key=api_key, temperature=0.7)

response = bot.ask("What is the capital of India?")
# response = bot.ask("What are some ground breaking AI advancements?")
print(response)



