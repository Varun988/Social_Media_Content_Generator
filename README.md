Structure
social_media_content_generator/
├── agents/
│   ├── agent1.py        # Agent 1: Google Search using SerpApi
│   ├── agent2.py        # Agent 2: Content restructuring using OpenAI
│   ├── agent3.py        # Agent 3: Social Media posting (Twitter, Facebook, Instagram)
├── utils/
│   ├── serp_api.py      # SerpApi helper functions
│   ├── openai_api.py    # OpenAI helper functions for content generation
│   ├── social_media.py  # Social media API helper functions
├── main.py              # Main file to run the whole process using StateGraph
└── requirements.txt     # List of required libraries


Explanation of Changes:
StateGraph:

We use StateGraph to manage the transitions between the states (searching, restructuring, posting).
Each state is associated with an agent that performs a specific task (searching, restructuring, posting).
The state transitions based on the completion of the task, allowing for a more structured, flow-based approach.
States:

searching: Fetches content using Agent1.
restructuring: Uses Agent2 to restructure the content based on the platform.
posting: Posts the content to social media using Agent3.
Graph Execution:

The graph.run() method runs the state transitions and agents in the correct order. The result is stored in the StateGraph state object and can be accessed after the process completes.
How to Run:
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set Environment Variables: Set the necessary API keys for SerpApi, OpenAI, and social media.

Run the System:

bash
Copy code
python main.py
This solution fully integrates the StateGraph from langgraph, allowing the tasks to be executed in a state-driven manner. It’s easy to extend this structure with more states, agents, and transitions if you want to add more functionality in the future.
