import streamlit as st

def main():
    # Title of the app
    st.title("Social Media Content Generator")
    
    # Instructions
    st.markdown("""
    This app generates content for social media platforms (Twitter, Facebook, Instagram) based on a given topic.
    It then posts the content after restructuring it to fit the platform's requirements.
    """)
    
    # # User input: Topic and platform
    # topic = st.text_input("Enter a topic for social media content:")
    # platform_choice = st.selectbox("Select a social media platform:", ["Twitter", "Facebook", "Instagram"])

   
# Run the Streamlit app
if __name__ == "__main__":
    main()
