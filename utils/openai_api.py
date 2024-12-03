from langchain import PromptTemplate # Import PromptTemplate from langchain
from appconfig import AppConfig
from azureai import AzureAI
config = AppConfig()
azure_ai = AzureAI(config)
llm=azure_ai.get_client()


def restructure_content_with_openai(content, platform_choice):
    """Use OpenAI to restructure content for the selected platform."""
    prompt = f"""
    Given the following content: {content},
    please restructure it for {platform_choice} while considering its unique limitations and audience.
    For example, Twitter has a 280 character limit, while Instagram and Facebook allow longer posts.
    Ensure that hashtags are relevant and appropriately formatted.
    """
    
    llm_prompt = PromptTemplate.from_template(
    template=prompt
    )
    formatted_prompt = llm_prompt.format(human_prompt=prompt)

    response = llm.invoke(formatted_prompt)
    return response.content.strip()