
import streamlit as st
from html import escape


def subject_card(name, code, section, stats=None, footer_callback=None):

    html_content = f"""
<div style="
    background: white;
    border-left: 8px solid #EB459E;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid black;
    margin-bottom: 20px;
">

    <h3 style="
        margin: 0;
        color: #1E293B !important;
        font-size: 1.5rem;
    ">
        {escape(str(name))}
    </h3>

    <p style="color: #64748B !important; margin: 10px 0;">
        Code:
        <span style="
            background: #E0E3FF;
            color: #5865F2 !important;
            padding: 2px 8px;
            border-radius: 5px;
        ">
            {escape(str(code))} | Section: {escape(str(section))}
        </span>
    </p>
"""

    if stats:

        html_content += """
    <div style="
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
    ">
"""

        for icon, label, value in stats:

            html_content += f"""
        <div style="
            background: #FCEFF6;
            color: #1E293B !important;
            padding: 8px 12px;
            border-radius: 12px;
            font-size: 0.9rem;
            margin-bottom: 5px;
        ">
            {escape(str(icon))}
            <b style="color: #1E293B !important;">
                {escape(str(value))}
            </b>
            <span style="color: #1E293B !important;">
                {escape(str(label))}
            </span>
        </div>
"""

        html_content += """
    </div>
"""

    html_content += """
</div>
"""

    st.html(html_content)

    if footer_callback:
        footer_callback()
