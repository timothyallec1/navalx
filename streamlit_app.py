import streamlit as st

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Inventory tracker',
    page_icon=':shopping_bags:', # This is an emoji shortcode. Could be a URL too.
)

# Add some content to your Streamlit app
st.title('CAMiLL - NavalX AI Bot')

# You can add other components like text, sliders, buttons, etc. here
# For example:
st.write('This bot answers questions about NavalX and its tech bridges.')

# Finally, run your Streamlit app
if __name__ == "__main__":
    streamlit_app()
