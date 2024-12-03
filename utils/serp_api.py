import serpapi
from appconfig import AppConfig
from azureai import AzureAI
config = AppConfig()
azure_ai = AzureAI(config)
def fetch_google_search_results(topic):
    serpapi_params=azure_ai.get_serpapi()
    params = serpapi_params
    search = serpapi.search({
        **params,
        "q": topic,
        "num": 1
    })
    content = [result['snippet'] for result in search.get('organic_results', [])[:3]]

    return content
