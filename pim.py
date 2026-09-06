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

if "page" not in st.session_state:
    st.session_state.page = "login"

if "df" not in st.session_state:
    st.session_state.df = None

if "selected_sheet" not in st.session_state:
    st.session_state.selected_sheet = None


# ============================================================
# LOGIN PAGE
# ============================================================

def login_page():

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

    </style>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # LOGIN BOX
    # --------------------------------------------------------

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

            login_button = st.form_submit_button(
                "🔐 Login"
            )


        if login_button:

            if username == "admin" and password == "1234":

                st.session_state.logged_in = True
                st.session_state.page = "upload"

                st.rerun()

            else:

                st.error(
                    "Incorrect username or password."
                )


# ============================================================
# DATA UPLOAD PAGE
# ============================================================

def upload_page():

    st.markdown("""
    <style>

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
        max-width: 900px !important;
        margin: auto;
        padding-top: 5rem !important;
    }

    .upload-title {
        text-align: center;
        color: #0F172A;
        font-size: 36px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .upload-subtitle {
        text-align: center;
        color: #64748B;
        font-size: 16px;
        margin-bottom: 35px;
    }

    .upload-card {
        background: white;
        padding: 35px;
        border-radius: 18px;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 8px 30px rgba(15,23,42,0.08);
    }

    </style>
    """, unsafe_allow_html=True)


    # --------------------------------------------------------
    # TITLE
    # --------------------------------------------------------

    st.markdown(
        '<div class="upload-title">📂 Data Upload</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="upload-subtitle">
            Upload your PIM Excel file and select the worksheet
            you want to analyze.
        </div>
        """,
        unsafe_allow_html=True
    )


    left, center, right = st.columns([1, 2, 1])

    with center:

        st.markdown(
            '<div class="upload-card">',
            unsafe_allow_html=True
        )


        uploaded_file = st.file_uploader(
            "Upload Excel File",
            type=["xlsx", "xls"],
            help="Upload your PIM Excel dataset."
        )


        if uploaded_file is not None:

            try:

                excel_file = pd.ExcelFile(
                    uploaded_file
                )

                sheet_names = excel_file.sheet_names


                # Selectbox label
                st.markdown("""
                <style>

                div[data-testid="stSelectbox"] label {
                    color: #000000 !important;
                }

                </style>
                """, unsafe_allow_html=True)


                selected_sheet = st.selectbox(
                    "Select Worksheet",
                    sheet_names
                )


                if st.button(
                    "Continue to Dashboard →",
                    use_container_width=True
                ):

                    try:

                        df = pd.read_excel(
                            uploaded_file,
                            sheet_name=selected_sheet,
                            skiprows=17,
                            header=None
                        )


                        if len(df) < 2:

                            st.error(
                                "The selected worksheet does not contain "
                                "enough rows to create the required headers."
                            )

                        else:

                            # Save original dataframe
                            st.session_state.df = df

                            # Save sheet name
                            st.session_state.selected_sheet = selected_sheet

                            # Move to dashboard
                            st.session_state.page = "dashboard"

                            st.rerun()


                    except Exception as e:

                        st.error(
                            "Unable to load the selected worksheet."
                        )

                        st.code(str(e))


            except Exception as e:

                st.error(
                    "Unable to read the Excel file."
                )

                st.code(str(e))


        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# DASHBOARD PAGE
# ============================================================

def dashboard_page():

    # ========================================================
    # DASHBOARD CSS
    # ========================================================

    st.markdown("""
    <style>

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


    /* =====================================================
       DASHBOARD TITLE
       ===================================================== */

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


    /* =====================================================
       KPI CARDS
       ===================================================== */

    .kpi-card {
        background: white;

        border: 1px solid #E2E8F0;
        border-radius: 16px;

        padding: 20px;

        min-height: 145px;

        box-shadow:
            0px 4px 15px rgba(15, 23, 42, 0.08);

        transition: all 0.2s ease;
    }


    .kpi-card:hover {

        transform: translateY(-2px);

        box-shadow:
            0px 8px 20px rgba(15, 23, 42, 0.12);
    }


    .kpi-icon {

        font-size: 25px;

        margin-bottom: 10px;
    }


    .kpi-title {

        color: #64748B;

        font-size: 14px;

        font-weight: 500;
    }


    .kpi-value {

        color: #0F172A;

        font-size: 30px;

        font-weight: 700;

        margin-top: 5px;
    }


    .kpi-subtitle {

        color: #94A3B8;

        font-size: 12px;

        margin-top: 5px;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

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


    /* =====================================================
       BUTTONS
       ===================================================== */

    .stButton > button,
    .stDownloadButton > button {

        border-radius: 8px;

        font-weight: 600;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */

    [data-testid="stDataFrame"] {

        border-radius: 10px;
    }


    /* =====================================================
       ALERT
       ===================================================== */

    .stAlert {

        border-radius: 10px;
    }

    </style>
    """, unsafe_allow_html=True)


    # ========================================================
    # CHECK DATA
    # ========================================================

    if st.session_state.df is None:

        st.error(
            "No data has been uploaded."
        )

        st.session_state.page = "upload"

        st.rerun()


    df = st.session_state.df.copy()


    # ========================================================
    # DATA CLEANING
    # ========================================================

    try:

        # ----------------------------------------------------
        # CREATE HEADER
        # ----------------------------------------------------

        main_header = df.iloc[0].ffill()

        month_header = df.iloc[1]


        columns = []


        for main, month in zip(
            main_header,
            month_header
        ):

            if pd.notna(month):

                columns.append(
                    f"{main}_{month}"
                )

            else:

                columns.append(
                    str(main)
                )


        # ----------------------------------------------------
        # ASSIGN COLUMNS
        # ----------------------------------------------------

        df.columns = columns


        # Remove header rows
        df = df.iloc[2:].reset_index(drop=True)


        # ----------------------------------------------------
        # CHANGE DATE FORMAT
        # ----------------------------------------------------

        def change_date_format(col):

            if "_" in col:

                prefix, date = col.rsplit(
                    "_",
                    1
                )

                try:

                    date = pd.to_datetime(
                        date
                    )

                    return (
                        f"{prefix}_"
                        f"{date.strftime('%b')}"
                    )

                except:

                    return col

            return col


        df.columns = [
            change_date_format(col)
            for col in df.columns
        ]


        # ----------------------------------------------------
        # REMOVE EMPTY COLUMNS
        # ----------------------------------------------------

        df = df.dropna(
            axis=1,
            how="all"
        )


        # ----------------------------------------------------
        # REMOVE ROWS WITHOUT SCHOOL
        # ----------------------------------------------------

        if "School Name" in df.columns:

            df = df.dropna(
                subset=["School Name"]
            )


        # ----------------------------------------------------
        # REMOVE S/N
        # ----------------------------------------------------

        if "S/N" in df.columns:

            df = df.drop(
                columns=["S/N"]
            )


    except Exception as e:

        st.error(
            "There was an error while cleaning the data."
        )

        st.code(str(e))

        return


    # ========================================================
    # DATA SCALING / CONVERSION
    # ========================================================

    # --------------------------------------------------------
    # Minimum Standard Columns
    # --------------------------------------------------------

    minimum_standard_cols = [

        col

        for col in df.columns

        if col.startswith(
            "Meeting Minimum Standards By Grade?"
        )

    ]


    # --------------------------------------------------------
    # Priority Columns
    # --------------------------------------------------------

    priority_cols = [

        col

        for col in df.columns

        if col.startswith(
            "Teacher's Priority Area"
        )

    ]


    # --------------------------------------------------------
    # Visit Columns
    # --------------------------------------------------------

    total_visit_cols = [

        col

        for col in df.columns

        if col.startswith(
            "Total Number of Visits Per Month"
        )

    ]


    # ========================================================
    # CONVERT YES / NO
    # ========================================================

    for col in minimum_standard_cols:

        df[col] = df[col].map(
            {
                "No": 0,
                "Yes": 1
            }
        )


    # ========================================================
    # CONVERT PRIORITY AREA
    # ========================================================

    priority_mapping = {

        "0: No Priority Areas Achieved": 0,

        "1: Mastered Instructional Routine": 1,

        "2: Mastered Basic Skills": 2,

        "3: Mastered Advanced Skills": 3

    }


    for col in priority_cols:

        df[col] = df[col].map(
            priority_mapping
        )


    # ========================================================
    # VISIT CALCULATION
    # ========================================================

    if len(total_visit_cols) > 0:

        monthly_visit = (
            df[total_visit_cols]
            .apply(pd.to_numeric, errors="coerce")
            .fillna(0)
            .sum()
        )

        total_Visit = monthly_visit.sum()

    else:

        monthly_visit = pd.Series(
            dtype=float
        )

        total_Visit = 0


    # ========================================================
    # KPI VALUES
    # ========================================================

    if "RtR Staff Name" in df.columns:

        total_LF = df[
            "RtR Staff Name"
        ].nunique()

    else:

        total_LF = 0


    if "School Name" in df.columns:

        total_schools = df[
            "School Name"
        ].nunique()

    else:

        total_schools = 0


    if "Teacher Name" in df.columns:

        total_teachers = df[
            "Teacher Name"
        ].nunique()

    else:

        total_teachers = 0


    total_Visit = int(
        round(total_Visit)
    )


    # ========================================================
    # DASHBOARD TITLE
    # ========================================================

    st.markdown(
        '<div class="dashboard-title">'
        '📊 PIM Dashboard'
        '</div>',
        unsafe_allow_html=True
    )


    st.markdown(
        f"""
        <div class="dashboard-subtitle">
            Worksheet: {st.session_state.selected_sheet}
        </div>
        """,
        unsafe_allow_html=True
    )


    # ========================================================
    # KPI CARD FUNCTION
    # ========================================================

    def kpi_card(
        title,
        value,
        icon,
        subtitle=""
    ):

        st.markdown(
            f"""
            <div class="kpi-card">

                <div class="kpi-icon">
                    {icon}
                </div>

                <div class="kpi-title">
                    {title}
                </div>

                <div class="kpi-value">
                    {value}
                </div>

                <div class="kpi-subtitle">
                    {subtitle}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # DISPLAY KPI CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium"
    )


    # --------------------------------------------------------
    # CARD 1
    # --------------------------------------------------------

    with col1:

        kpi_card(
            title="Total LF",
            value=f"{total_LF:,}",
            icon="👥",
            subtitle="LFs in the program"
        )


    # --------------------------------------------------------
    # CARD 2
    # --------------------------------------------------------

    with col2:

        kpi_card(
            title="Total Schools",
            value=f"{total_schools:,}",
            icon="🏫",
            subtitle="Schools in the program"
        )


    # --------------------------------------------------------
    # CARD 3
    # --------------------------------------------------------

    with col3:

        kpi_card(
            title="Total Teachers",
            value=f"{total_teachers:,}",
            icon="👨‍🏫",
            subtitle="Teachers in the program"
        )


    # --------------------------------------------------------
    # CARD 4
    # --------------------------------------------------------

    with col4:

        kpi_card(
            title="Total Visits",
            value=f"{total_Visit:,}",
            icon="📍",
            subtitle="Total visits recorded"
        )


    # ========================================================
    # SPACE AFTER KPI CARDS
    # ========================================================

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    # ========================================================
    # SIDEBAR
    # ========================================================

    with st.sidebar:

        st.markdown(
            """
            <div style="
                font-size:24px;
                font-weight:700;
                margin-bottom:20px;
            ">
                📊 PIM Dashboard
            </div>
            """,
            unsafe_allow_html=True
        )


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


        st.caption(
            f"Worksheet: "
            f"{st.session_state.selected_sheet}"
        )


        st.markdown("---")


        # ----------------------------------------------------
        # CHANGE DATA
        # ----------------------------------------------------

        if st.button(
            "📂 Change Data",
            use_container_width=True
        ):

            st.session_state.page = "upload"

            st.rerun()


        # ----------------------------------------------------
        # LOGOUT
        # ----------------------------------------------------

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False

            st.session_state.page = "login"

            st.session_state.df = None

            st.session_state.selected_sheet = None

            st.rerun()


    # ========================================================
    # DASHBOARD CONTENT
    # ========================================================

    if page == "Home":

        st.subheader("Home")


        st.info(
            "Your Home dashboard calculations "
            "and charts will go here."
        )


        st.dataframe(
            df.head(),
            use_container_width=True
        )


    # ========================================================
    # SCHOOLS
    # ========================================================

    elif page == "Schools":

        st.subheader("Schools")


        st.info(
            "Your Schools analysis goes here."
        )


    # ========================================================
    # TEACHERS
    # ========================================================

    elif page == "Teachers":

        st.subheader("Teachers")


        st.info(
            "Your Teachers analysis goes here."
        )


    # ========================================================
    # VISITS
    # ========================================================

    elif page == "Visits":

        st.subheader("Visits")


        st.info(
            "Your Visits analysis goes here."
        )


    # ========================================================
    # STANDARDS
    # ========================================================

    elif page == "Standards":

        st.subheader("Standards")


        st.info(
            "Your Standards analysis goes here."
        )


    # ========================================================
    # REPORTS
    # ========================================================

    elif page == "Reports":

        st.subheader("Reports")


        st.info(
            "Your Reports analysis goes here."
        )


# ============================================================
# PAGE ROUTING
# ============================================================

if st.session_state.page == "login":

    login_page()


elif st.session_state.page == "upload":

    upload_page()


elif st.session_state.page == "dashboard":

    dashboard_page()

