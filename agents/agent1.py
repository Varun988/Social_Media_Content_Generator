from utils.serp_api import fetch_google_search_results

# Define the agents and workflow with StateGraph
class Agent1:
    def __init__(self, name="Agent 1"):
        self.name = name

    def perform_task(self, state):
        topic = state.topic  # Access topic directly using dot notation
        content = fetch_google_search_results(topic)
        print(f"{self.name} fetched content for '{topic}': {content}")
        # Create a new state instance with updated content
        state = state._replace(content=content)
        return state
