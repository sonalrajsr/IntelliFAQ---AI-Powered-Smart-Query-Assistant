# Search on Google using SerpAPI
from serpapi.google_search import GoogleSearch
import os

def google_search(query):
    api_key = os.getenv("SERPAPI_API_KEY")
    
    if not api_key:
        print("Error: SERPAPI_API_KEY is not set. Please check your environment variables.")
        return "API key missing."

    params = {
        "api_key": api_key,
        "engine": "google",
        "q": query,
    }

    search = GoogleSearch(params)

    try:
        result = search.get_dict()
        
        if 'error' in result:
            print(f"API Error: {result['error']}")
            return "API Error: Unable to fetch results."

        search_results = [item.get('snippet', '') for item in result.get('organic_results', [])]

        if not search_results:
            return "No relevant search results found."

        return ' '.join(search_results)

    except Exception as e:
        print(f"Exception occurred: {e}")
        return "Error: Unable to fetch search results."
