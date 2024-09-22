# sentiment_analysis.py

# import openai
# from config import OPENAI_API_KEY

# openai.api_key = OPENAI_API_KEY

# def analyze_sentiment(text):
#     """
#     Analyzes the sentiment of the provided text using OpenAI's API.

#     Args:
#         text (str): The text to analyze.

#     Returns:
#         float: Sentiment score between -1 and 1.
#     """
#     prompt = (
#         "Analyze the sentiment of the following text and provide a score between -1 (very negative) "
#         "and 1 (very positive):\n\n"
#         f"Text: '''{text}'''\n\n"
#         "Sentiment score:"
#     )

#     try:
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=prompt,
#             max_tokens=5,
#             n=1,
#             stop=None,
#             temperature=0
#         )

#         sentiment_score = float(response.choices[0].text.strip())
#         return sentiment_score

#     except Exception as e:
#         print(f"Error during sentiment analysis: {e}")
#         # Handle the error or return a default value
#         return 0.0  # Neutral sentiment as default
