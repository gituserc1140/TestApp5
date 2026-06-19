import streamlit as st
from constants import TITLE, MESSAGE

def main():
    """
    Main function to run the Streamlit application.
    """
    try:
        st.title(TITLE)
        st.write(MESSAGE)
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
