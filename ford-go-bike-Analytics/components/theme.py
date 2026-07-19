from pathlib import Path

import streamlit as st


def apply_theme():

    css_path = Path(__file__).resolve().parent.parent / "css" / "styles.css"

    with open(css_path, encoding="utf-8") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True,
        )
        """
<style>

/* -------------------------------------------------- */
/* Main App */
/* -------------------------------------------------- */

.stApp{

background:#09111F;

color:white;

font-family:'Segoe UI',sans-serif;

}


/* -------------------------------------------------- */
/* Sidebar */
/* -------------------------------------------------- */

section[data-testid="stSidebar"]{

background:#111827;

border-right:1px solid #293548;

}


/* -------------------------------------------------- */
/* KPI Cards */
/* -------------------------------------------------- */

.kpi-card{

background:linear-gradient(135deg,#162447,#1F4068);

padding:22px;

border-radius:18px;

box-shadow:0 8px 25px rgba(0,0,0,.35);

transition:.35s;

border:1px solid rgba(255,255,255,.05);

}

.kpi-card:hover{

transform:translateY(-6px);

box-shadow:0 12px 30px rgba(0,0,0,.45);

}


/* -------------------------------------------------- */
/* Hero */
/* -------------------------------------------------- */

.hero{

background:linear-gradient(120deg,#1E3A8A,#2563EB);

padding:45px;

border-radius:22px;

color:white;

}


/* -------------------------------------------------- */
/* Section Title */
/* -------------------------------------------------- */

.section-title{

font-size:32px;

font-weight:700;

margin-top:25px;

margin-bottom:15px;

color:#4FC3F7;

}


/* -------------------------------------------------- */
/* Metric Value */
/* -------------------------------------------------- */

.metric-value{

font-size:38px;

font-weight:bold;

color:#38BDF8;

}


/* -------------------------------------------------- */
/* Metric Label */
/* -------------------------------------------------- */

.metric-label{

font-size:18px;

color:#D1D5DB;

}


/* -------------------------------------------------- */
/* Buttons */
/* -------------------------------------------------- */

.stButton>button{

background:#2563EB;

color:white;

border:none;

padding:12px 22px;

border-radius:10px;

font-weight:bold;

}

.stButton>button:hover{

background:#1D4ED8;

}


/* -------------------------------------------------- */
/* Footer */
/* -------------------------------------------------- */

.footer{

text-align:center;

margin-top:45px;

color:#9CA3AF;

font-size:15px;

}

</style>
""",
        unsafe_allow_html=True