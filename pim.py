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

    st.markdown("# 📊 PIM Dashboard")

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

    if st.button("🚪 Logout", use_container_width=True):

        st.session_state.logged_in = False
        st.rerun()


# ============================================================
# DATA UPLOAD
# ============================================================

st.markdown(
    """
    <div class="dashboard-title">
        📂 Data Upload
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


# ============================================================
# CREATE COLUMN NAMES
# ============================================================

main_header = df.iloc[0].ffill()
month_header = df.iloc[1]

columns = []

for main, month in zip(main_header, month_header):

    if pd.notna(month):

        columns.append(f"{main}_{month}")

    else:

        columns.append(str(main))


df.columns = columns

df = df.iloc[2:].reset_index(drop=True)


# ============================================================
# CHANGE DATE FORMAT
# ============================================================

def change_date_format(col):

    if "_" in str(col):

        prefix, date = str(col).rsplit("_", 1)

        try:

            date = pd.to_datetime(date)

            return f"{prefix}_{date.strftime('%b')}"

        except:

            return str(col)

    return str(col)


df.columns = [
    change_date_format(col)
    for col in df.columns
]


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = [
    str(col).strip()
    for col in df.columns
]


# ============================================================
# CLEAN DATA
# ============================================================

df = df.dropna(
    axis=1,
    how="all"
)

if "School Name" in df.columns:

    df = df.dropna(
        subset=["School Name"]
    )

if "S/N" in df.columns:

    df = df.drop(
        columns=["S/N"]
    )


# ============================================================
# REQUIRED COLUMNS
# ============================================================

required_columns = [
    "RtR Staff Name",
    "School Name",
    "Teacher Name",
    "Grade"
]

missing_columns = [
    col
    for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        "The following required columns are missing:"
    )

    for col in missing_columns:
        st.write(f"- {col}")

    st.stop()


# ============================================================
# IDENTIFY IMPORTANT COLUMNS
# ============================================================

minimum_standard_cols = [
    col
    for col in df.columns
    if col.startswith(
        "Meeting Minimum Standards By Grade?"
    )
]

priority_cols = [
    col
    for col in df.columns
    if col.startswith(
        "Teacher's Priority Area"
    )
]

# Also support curly apostrophe
priority_cols += [
    col
    for col in df.columns
    if col.startswith(
        "Teacher’s Priority Area"
    )
]

priority_cols = list(dict.fromkeys(priority_cols))

total_visit_cols = [
    col
    for col in df.columns
    if col.startswith(
        "Total Number of Visits Per Month"
    )
]


# ============================================================
# CONVERT MINIMUM STANDARD
# ============================================================

minimum_standard_mapping = {
    "No": 0,
    "Yes": 1
}

for col in minimum_standard_cols:

    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .map(minimum_standard_mapping)
    )


# ============================================================
# CONVERT PRIORITY AREA
# ============================================================

priority_mapping = {
    "0: No Priority Areas Achieved": 0,
    "1: Mastered Instructional Routine": 1,
    "2: Mastered Basic Skills": 2,
    "3: Mastered Advanced Skills": 3
}

for col in priority_cols:

    df[col] = (
        df[col]
        .astype("string")
        .str.strip()
        .map(priority_mapping)
    )


# ============================================================
# CONVERT VISITS TO NUMERIC
# ============================================================

for col in total_visit_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    ).fillna(0)


# ============================================================
# CONVERT GRADE
# ============================================================

df["Grade"] = pd.to_numeric(
    df["Grade"],
    errors="coerce"
)


# ============================================================
# DATA INFORMATION
# ============================================================

st.success(
    f"Loaded sheet: **{selected_sheet}**"
)

with st.expander("📋 Data Preview"):

    st.write(f"Rows: {len(df):,}")
    st.write(f"Columns: {len(df.columns):,}")

    st.dataframe(
        df.head(10),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# CALCULATIONS
# ============================================================



# ============================================================
# REPORTS
# ============================================================

elif page == "Reports":

    st.markdown(
        """
        <div class="dashboard-title">
            Reports
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="dashboard-subtitle">
            Filter and explore the classroom observation dataset.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        staff_options = [
            "All"
        ] + sorted(
            df["RtR Staff Name"]
            .dropna()
            .unique()
            .tolist()
        )

        selected_staff = st.selectbox(
            "RtR Staff",
            staff_options
        )

    with col2:

        grade_values = (
            df["Grade"]
            .dropna()
            .unique()
            .tolist()
        )

        grade_values = sorted(
            grade_values
        )

        grade_options = [
            "All"
        ] + grade_values

        selected_grade = st.selectbox(
            "Grade",
            grade_options
        )

    filtered_df = df.copy()

    if selected_staff != "All":

        filtered_df = filtered_df[
            filtered_df[
                "RtR Staff Name"
            ]
            ==
            selected_staff
        ]

    if selected_grade != "All":

        filtered_df = filtered_df[
            filtered_df[
                "Grade"
            ]
            ==
            selected_grade
        ]

    st.markdown("---")

    st.write(
        f"Showing **{len(filtered_df):,}** records"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    csv_data = filtered_df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Filtered Report",
        data=csv_data,
        file_name="PIM_Filtered_Report.csv",
        mime="text/csv",
        use_container_width=False
    )
