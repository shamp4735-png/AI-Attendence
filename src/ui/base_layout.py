
import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: #5865F2 !important;
        }

        .stApp div[data-testid="stColumn"] {
            background-color: #E0E3FF !important;
            padding: 1.5rem !important;
            border-radius: 3rem !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: #E0E3FF !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit default elements */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        .block-container {
            padding-top: 1.5rem !important;
        }

        /* Headings */
        h1, h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            color: #1E293B !important;
        }

        h1 {
            font-size: 3.5rem !important;
        }

        h2 {
            font-size: 2rem !important;
        }

        h3, h4, p, label, li, span {
            font-family: 'Outfit', sans-serif;
        }

        /* Default text */
        .stApp, .stApp p, .stApp label,
        .stApp [data-testid="stMarkdownContainer"] {
            color: #1E293B;
        }

        /* All Streamlit buttons */
        .stButton button,
        .stDownloadButton button,
        div[data-testid="stFormSubmitButton"] button {
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 1.5rem !important;
            padding: 10px 20px !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
        }

        /* Blue buttons */
        .stButton button[kind="primary"],
        .stButton button:not([kind]) {
            background-color: #5865F2 !important;
        }

        /* Pink secondary buttons */
        .stButton button[kind="secondary"] {
            background-color: #EB459E !important;
        }

        /* Black tertiary buttons */
        .stButton button[kind="tertiary"] {
            background-color: #1E1E24 !important;
        }

        /* Keep button text white in all modes */
        .stButton button *,
        .stDownloadButton button *,
        div[data-testid="stFormSubmitButton"] button * {
            color: #FFFFFF !important;
        }

        .stButton button:hover {
            transform: scale(1.03);
            transition: transform 0.2s ease-in-out;
        }

        /* Input fields */
        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] {
            color: #1E293B !important;
            background-color: #FFFFFF !important;
        }

        /* Dropdown text */
        div[data-baseweb="select"] * {
            color: #1E293B !important;
        }

        /* Tables */
        [data-testid="stDataFrame"] {
            color: #1E293B !important;
        }

        /* Dialog */
        [data-testid="stDialog"] {
            color: #FFFFFF;
        }

        </style>
    """, unsafe_allow_html=True)


def footer_home():
    st.markdown("""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            margin-top:2rem;
            color:#1E293B;
            font-family:Outfit,sans-serif;
            font-weight:600;
        ">
            Created by Sham ❤️
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            margin-top:2rem;
            color:#1E293B;
            font-family:Outfit,sans-serif;
            font-weight:600;
        ">
            Created by Sham ❤️
        </div>
    """, unsafe_allow_html=True)
