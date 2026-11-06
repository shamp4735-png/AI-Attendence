
import streamlit as st


def footer_home():

    st.markdown("""
        <div style="
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 2rem;
        ">
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown("""
        <div style="
            margin-top: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 5px;
        ">
            <p style="
                font-family: Outfit, sans-serif;
                font-weight: 700;
                color: #1E293B;
                margin: 0;
            ">
                Created by Sham
            </p>
        </div>
    """, unsafe_allow_html=True)
