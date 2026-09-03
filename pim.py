import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PIM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ============================================================
# LOGIN PAGE
# ============================================================

if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .stApp {
        background:
            linear-gradient(
                135deg,
                #0F172A 0%,
                #172554 50%,
                #0F172A 100%
            ) !important;
    }

    .main .block-container {
        min-height: 100vh;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 30px !important;
        padding-bottom: 30px !important;
    }

    .pim-title {
        text-align: center;
        color: white;
        font-size: 42px;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 5px;
    }

    .pim-subtitle {
        text-align: center;
        color: #CBD5E1;
        font-size: 17px;
        margin-bottom: 30px;
    }

    [data-testid="stForm"] {
        background: rgba(15, 23, 42, 0.95);
        padding: 30px !important;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0px 10px 40px rgba(0,0,0,0.45);
    }

    [data-testid="stForm"] label {
        color: #E5E7EB !important;
        font-weight: 500;
    }

    [data-testid="stForm"] input {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.20) !important;
        border-radius: 8px !important;
    }

    [data-testid="stForm"] input::placeholder {
        color: #94A3B8 !important;
    }

    [data-testid="stFormSubmitButton"] button {
        width: 100%;
        background-color: #2563EB;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        font-weight: 600;
    }

    [data-testid="stFormSubmitButton"] button:hover {
        background-color: #1D4ED8;
        color: white;
    }

    @media (max-width: 600px) {

        .main .block-container {
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        .pim-title {
            font-size: 32px;
        }

        .pim-subtitle {
            font-size: 14px;
            margin-bottom: 20px;
        }

        [data-testid="stForm"] {
            padding: 22px !important;
            border-radius: 14px;
        }
    }

    @media (max-height: 700px) {

        .main .block-container {
            padding-top: 15px !important;
            padding-bottom: 20px !important;
        }

        .pim-title {
            font-size: 34px;
        }

        .pim-subtitle {
            font-size: 15px;
        }

        [data-testid="stForm"] {
            padding: 22px !important;
        }
    }

    @media (max-height: 550px) {

        .pim-title {
            font-size: 28px;
        }

        .pim-subtitle {
            margin-bottom: 12px;
        }

        [data-testid="stForm"] {
            padding: 18px !important;
        }
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="pim-title">📊 PIM Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="pim-subtitle">
            Monitor &nbsp;•&nbsp; Analyze &nbsp;•&nbsp; Improve
        </div>
        """,
        unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 1.1, 1])

    with center:

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#FFFFFF;
                font-size:24px;
                font-weight:600;
                margin-bottom:8px;
            ">
                Welcome Back!
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#CBD5E1;
                font-size:14px;
                margin-bottom:15px;
            ">
                Sign in to access the PIM Dashboard
            </div>
            """,
            unsafe_allow_html=True
        )

        with st.form("login_form"):

            username = st.text_input(
                "Username",
                placeholder="Enter your username"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login_button = st.form_submit_button("🔐 Login")

        if login_button:

            if username == "admin" and password == "1234":

                st.session_state.logged_in = True
                st.rerun()

            else:

                st.error("Incorrect username or password.")

    st.stop()


# ============================================================
# DASHBOARD CSS
# ============================================================

st.markdown("""
<style>

/* ============================================================
   GLOBAL
============================================================ */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F8FAFC 0%,
            #EEF2FF 50%,
            #F8FAFC 100%
        ) !important;
}

.main .block-container {
    max-width: none !important;
    width: 100% !important;
    padding-top: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 2rem !important;
}


/* ============================================================
   TITLES
============================================================ */

.dashboard-title {
    color: #0F172A;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 5px;
}

.dashboard-subtitle {
    color: #64748B;
    font-size: 16px;
    margin-bottom: 25px;
}


/* ============================================================
   METRIC CARDS
============================================================ */

[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #E2E8F0;
    box-shadow: 0px 4px 15px rgba(15,23,42,0.08);
}

[data-testid="stMetricLabel"] {
    color: #64748B !important;
}

[data-testid="stMetricValue"] {
    color: #0F172A !important;
}


/* ============================================================
   SIDEBAR
============================================================ */

[data-testid="stSidebar"] {
    background-color: #0F172A;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stSidebar"] label {
    color: white !important;
}

[data-testid="stSidebar"] button {
    border-radius: 8px;
}


/* ============================================================
   DATAFRAME
============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 10px;
}


/* ============================================================
   FILE UPLOADER
============================================================ */

[data-testid="stFileUploader"] {
    background: white;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #E2E8F0;
}


/* ============================================================
   SELECTBOX
============================================================ */

[data-baseweb="select"] {
    border-radius: 8px;
}


/* ============================================================
   ALERTS
============================================================ */

.stAlert {
    border-radius: 10px;
}


/* ============================================================
   BUTTONS
============================================================ */

.stButton > button,
.stDownloadButton > button {
    border-radius: 8px;
    font-weight: 600;
}


/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 600px) {

    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }

    .dashboard-title {
        font-size: 26px;
    }

    .dashboard-subtitle {
        font-size: 14px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        [
            "Home",
            "Schools",
            "Teachers",
            "Visits",
            "Standards",
            "Reports"
        ]
    )
    
    st.markdown("---")
    
    st.markdown("---")

    st.markdown(
        """
        <div class="dashboard-title">
            Data Upload
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div class="dashboard-subtitle">
            Upload your Excel file and select the worksheet to analyze.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    uploaded_file = st.file_uploader(
        "Upload Excel File",
        type=["xlsx", "xls"],
        help="Upload your PIM Excel dataset."
    )
    
    st.markdown("---")
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

# ============================================================
# STOP IF NO FILE
# ============================================================

if uploaded_file is None:
    st.info("Please upload an Excel file to start the dashboard.")
    st.stop()


# ============================================================
# READ EXCEL
# ============================================================

try:

    excel_file = pd.ExcelFile(uploaded_file)
    sheet_names = excel_file.sheet_names

except Exception as e:

    st.error("Unable to read the Excel file.")
    st.code(str(e))
    st.stop()


# ============================================================
# SHEET SELECTION
# ============================================================

selected_sheet = st.selectbox(
    "Select Worksheet",
    sheet_names
)


# ============================================================
# LOAD SHEET
# ============================================================

try:

    df = pd.read_excel(
        uploaded_file,
        sheet_name=selected_sheet,
        skiprows=17,
        header=None
    )

except Exception as e:

    st.error("Unable to load the selected worksheet.")
    st.code(str(e))
    st.stop()


# ============================================================
# CHECK DATA
# ============================================================

if len(df) < 2:

    st.error(
        "The selected worksheet does not contain enough rows "
        "to create the required headers."
    )

    st.stop()










