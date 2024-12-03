from utils.social_media import post_to_social_media


class Agent3:
    def __init__(self, name="Agent 3"):
        self.name = name

    def perform_task(self, state):
        structured_content = state.structured_content  # Access structured_content directly
        platform_choice = state.platform_choice  # Access platform_choice directly
        if structured_content:
            result = post_to_social_media(structured_content, platform_choice)
            # Create a new state instance with updated posting_result
            state = state._replace(posting_result=result)
        return state