from utils.openai_api import restructure_content_with_openai

class Agent2:
    def __init__(self, name="Agent 2"):
        self.name = name

    def perform_task(self, state):
        content = state.content  # Access content directly using dot notation
        platform_choice = state.platform_choice  # Access platform_choice directly
        if content:
            structured_content = restructure_content_with_openai(content, platform_choice)
            print(f"{self.name} restructured content for {platform_choice}: {structured_content}")
            # Create a new state instance with updated structured_content
            state = state._replace(structured_content=structured_content)
        return state

