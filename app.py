import streamlit as st
from langgraph.graph import StateGraph, END
from agents.agent1 import Agent1
from agents.agent2 import Agent2
from agents.agent3 import Agent3
from typing import NamedTuple
from typing import Optional
from typing import Optional

# Function to run the social media process
def run_social_media_process(topic, platform_choice):
    agent1 = Agent1()
    agent2 = Agent2()
    agent3 = Agent3()

    # Define the state schema for the state graph

    class StateSchema(NamedTuple):
        content: Optional[list] = None  # Default to None, but it could also be a list
        structured_content: Optional[str] = None  # Default to None, but it could also be a string
        posting_result: Optional[str] = None  # Default to None, but it could also be a string
        topic: Optional[str] = None  # Default to None, but it could also be a string
        platform_choice: Optional[str] = None  # Default to None, but it could also be a string


    # Create a StateGraph object with the defined state schema
    graph = StateGraph(state_schema=StateSchema)

    # Define states with the nodes for each agent's task
    graph.add_node("searching", agent1.perform_task)
    graph.add_node("restructuring", agent2.perform_task)
    graph.add_node("posting", agent3.perform_task)

    # Define edges using state names
    graph.add_edge("searching", "restructuring")
    graph.add_edge("restructuring", "posting")
    graph.add_edge("posting", END)

    # Set entry point
    graph.set_entry_point("searching")

    # Compile the graph to prepare it for execution
    runnable = graph.compile()

    # Invoke the graph with the correct initial state values
    out = runnable.invoke({
        "content": [],  # Initial empty list for content
        "topic": topic,  # Pass the topic to the first agent
        "platform_choice": platform_choice  # Pass platform choice to the agents
    })

    # Access the results from the execution
    posting_result = out['posting_result']
    content = out['content']
    structured_content = out['structured_content']

    return posting_result, content, structured_content
# Streamlit UI
def main():
    # Title of the app
    st.title("Social Media Content Generator")
    
    # Instructions
    st.markdown("""
    This app generates content for social media platforms (Twitter, Facebook, Instagram) based on a given topic.
    It then posts the content after restructuring it to fit the platform's requirements.
    """)
    
    # User input: Topic and platform
    topic = st.text_input("Enter a topic for social media content:")
    platform_choice = st.selectbox("Select a social media platform:", ["Twitter", "Facebook", "Instagram"])

    if st.button("Generate & Post Content"):
        if topic:
            # Show a loading spinner while processing
            with st.spinner('Processing...'):
                posting_result, content, structured_content = run_social_media_process(topic, platform_choice)
            
            # Show the results
            st.subheader("Fetched Content:")
            st.write(content)
            
            st.subheader("Restructured Content for " + platform_choice + ":")
            st.write(structured_content)
            
            st.subheader("Posting Result:")
            st.write(posting_result)
        else:
            st.error("Please enter a topic to proceed.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
