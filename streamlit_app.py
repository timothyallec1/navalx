##streamlit run /workspaces/navalx/streamlit_app.py
from collections import defaultdict
from pathlib import Path
import sqlite3

import streamlit as st
import altair as alt
import pandas as pd


# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Inventory tracker',
    page_icon=':shopping_bags:', # This is an emoji shortcode. Could be a URL too.
)



 