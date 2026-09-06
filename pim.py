import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
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
    st.session_state.page = "Login"

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

    /* Remove Streamlit default padding */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    /* Full page background */
    .login-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;

        background:
            linear-gradient(
                rgba(10, 25, 47, 0.90),
                rgba(10, 25, 47, 0.90)
            );

        z-index: -1;
    }

    /* Login container */
    .login-container {
        width: 430px;
        margin: 100px auto 0 auto;
        padding: 45px 40px;

        background: rgba(255, 255, 255, 0.97);

        border-radius: 20px;

        box-shadow:
            0px 15px 40px rgba(0,0,0,0.25);

        text-align: center;
    }

    .login-logo {
        font-size: 50px;
        margin-bottom: 10px;
    }

    .login-title {
        font-size: 30px;
        font-weight: 700;
        color: #0A2540;
        margin-bottom: 5px;
    }

    .login-subtitle {
        font-size: 14px;
        color: #777;
        margin-bottom: 30px;
    }

    </style>

    <div class="login-background"></div>

    <div class="login-container">

        <div class="login-logo">
            📊
        </div>

        <div class="login-title">
            PIM Dashboard
        </div>

        <div class="login-subtitle">
            Program Information Management System
        </div>

    </div>

    """, unsafe_allow_html=True)


    # Login form
    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        login_button = st.form_submit_button(
            "Login",
            use_container_width=True
        )

        if login_button:

            if username == "admin" and password == "1234":

                st.session_state.logged_in = True
                st.session_state.page = "Upload"

                st.rerun()

            else:

                st.error("Invalid username or password.")


# ============================================================
# UPLOAD PAGE
# ============================================================

def upload_page():

    st.markdown("""
    <style>

    .upload-title {
        font-size: 36px;
        font-weight: 700;
        color: #0A2540;
        margin-bottom: 5px;
    }

    .upload-subtitle {
        color: #777;
        font-size: 16px;
        margin-bottom: 30px;
    }

    </style>
    """, unsafe_allow_html=True)


    st.markdown(
        '<div class="upload-title">📂 Upload Dataset</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="upload-subtitle">Upload your PIM Excel dataset to continue.</div>',
        unsafe_allow_html=True
    )


    uploaded_file = st.file_uploader(
        "Choose an Excel file",
        type=["xlsx", "xls"]
    )


    if uploaded_file is not None:

        try:

            # Read Excel workbook
            excel_file = pd.ExcelFile(uploaded_file)

            sheets = excel_file.sheet_names

            selected_sheet = st.selectbox(
                "Select Sheet",
                sheets
            )


            if st.button(
                "Load Dataset",
                use_container_width=True
            ):

                uploaded_file.seek(0)

                df = pd.read_excel(
                    uploaded_file,
                    sheet_name=selected_sheet,
                    skiprows=17,
                    header=None
                )

                st.session_state.df = df
                st.session_state.selected_sheet = selected_sheet
                st.session_state.page = "Dashboard"

                st.success("Dataset loaded successfully!")

                st.rerun()


        except Exception as e:

            st.error(
                f"Unable to read the Excel file: {e}"
            )


# ============================================================
# KPI CARD
# ============================================================

def kpi_card(title, value, icon, subtitle):

    return f"""
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
    """


# ============================================================
# DASHBOARD PAGE
# ============================================================

def dashboard_page():

    # --------------------------------------------------------
    # Check dataset
    # --------------------------------------------------------

    if st.session_state.df is None:

        st.warning("No dataset has been uploaded.")

        if st.button("Go to Upload Page"):

            st.session_state.page = "Upload"

            st.rerun()

        return


    # --------------------------------------------------------
    # Copy original dataframe
    # --------------------------------------------------------

    df = st.session_state.df.copy()


    # --------------------------------------------------------
    # CREATE COLUMN NAMES
    # --------------------------------------------------------

    try:

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


        df.columns = columns

        # Remove first two header rows
        df = df.iloc[2:].reset_index(drop=True)


    except Exception as e:

        st.error(
            f"Error creating column names: {e}"
        )

        return


    # --------------------------------------------------------
    # CHANGE DATE FORMAT
    # Example:
    # Total Number of Visits Per Month_2026-01-01
    # becomes:
    # Total Number of Visits Per Month_Jan
    # --------------------------------------------------------

    def change_date_format(col):

        if "_" in str(col):

            prefix, date = str(col).rsplit("_", 1)

            try:

                date = pd.to_datetime(date)

                return f"{prefix}_{date.strftime('%b')}"

            except:

                return col

        return col


    df.columns = [
        change_date_format(col)
        for col in df.columns
    ]


    # --------------------------------------------------------
    # REMOVE COMPLETELY EMPTY COLUMNS
    # --------------------------------------------------------

    df = df.dropna(
        axis=1,
        how="all"
    )


    # --------------------------------------------------------
    # REMOVE ROWS WITHOUT SCHOOL NAME
    # --------------------------------------------------------

    if "School Name" in df.columns:

        df = df[
            df["School Name"].notna()
        ].copy()


    # --------------------------------------------------------
    # REMOVE S/N IF EXISTS
    # --------------------------------------------------------

    if "S/N" in df.columns:

        df = df.drop(
            columns=["S/N"]
        )


    # --------------------------------------------------------
    # IDENTIFY MONTHLY COLUMNS
    # --------------------------------------------------------

    minimum_standard_cols = [
        col
        for col in df.columns
        if str(col).startswith(
            "Meeting Minimum Standards By Grade?"
        )
    ]


    priority_cols = [
        col
        for col in df.columns
        if str(col).startswith(
            "Teacher's Priority Area"
        )
    ]


    total_visit_cols = [
        col
        for col in df.columns
        if str(col).startswith(
            "Total Number of Visits Per Month"
        )
    ]


    # --------------------------------------------------------
    # CONVERT MINIMUM STANDARD TO 0 / 1
    # --------------------------------------------------------

    for col in minimum_standard_cols:

        df[col] = df[col].map({
            "No": 0,
            "Yes": 1
        })


    # --------------------------------------------------------
    # CONVERT PRIORITY AREA
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # CALCULATE TOTAL VISITS
    # --------------------------------------------------------

    if total_visit_cols:

        visit_data = (
            df[total_visit_cols]
            .apply(
                pd.to_numeric,
                errors="coerce"
            )
            .fillna(0)
        )

        monthly_visit = visit_data.sum()

        total_Visit = monthly_visit.sum()

    else:

        total_Visit = 0


    # --------------------------------------------------------
    # KPI VALUES
    # --------------------------------------------------------

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
    # DASHBOARD CSS
    # ========================================================

    st.markdown("""
    <style>

    /* ------------------------------------------------------
       GENERAL
    ------------------------------------------------------ */

    .stApp {

        background:
            linear-gradient(
                135deg,
                #f8fafc 0%,
                #eef3f8 100%
            );

    }


    /* ------------------------------------------------------
       MAIN CONTAINER
    ------------------------------------------------------ */

    .block-container {

        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        padding-bottom: 2rem;

    }


    /* ------------------------------------------------------
       DASHBOARD TITLE
    ------------------------------------------------------ */

    .dashboard-title {

        font-size: 34px;
        font-weight: 700;

        color: #0A2540;

        margin-bottom: 3px;

    }


    .dashboard-subtitle {

        font-size: 15px;

        color: #777;

        margin-bottom: 25px;

    }


    /* ------------------------------------------------------
       KPI CARD
    ------------------------------------------------------ */

    .kpi-card {

        background: #ffffff;

        padding: 24px 20px;

        border-radius: 18px;

        min-height: 175px;

        text-align: center;

        box-shadow:
            0 5px 20px rgba(0, 0, 0, 0.08);

        border: 1px solid #edf0f4;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;

    }


    .kpi-card:hover {

        transform: translateY(-4px);

        box-shadow:
            0 10px 28px rgba(0, 0, 0, 0.12);

    }


    /* ------------------------------------------------------
       KPI ICON
    ------------------------------------------------------ */

    .kpi-icon {

        font-size: 34px;

        margin-bottom: 8px;

    }


    /* ------------------------------------------------------
       KPI TITLE
    ------------------------------------------------------ */

    .kpi-title {

        font-size: 15px;

        font-weight: 600;

        color: #666;

        margin-bottom: 5px;

    }


    /* ------------------------------------------------------
       KPI VALUE
    ------------------------------------------------------ */

    .kpi-value {

        font-size: 34px;

        font-weight: 750;

        color: #0A2540;

        line-height: 1.2;

        margin: 5px 0;

    }


    /* ------------------------------------------------------
       KPI SUBTITLE
    ------------------------------------------------------ */

    .kpi-subtitle {

        font-size: 13px;

        color: #999;

        margin-top: 5px;

    }


    /* ------------------------------------------------------
       DIVIDER
    ------------------------------------------------------ */

    .dashboard-divider {

        height: 1px;

        background: #e5e7eb;

        margin-top: 25px;

        margin-bottom: 25px;

    }


    /* ------------------------------------------------------
       SIDEBAR
    ------------------------------------------------------ */

    [data-testid="stSidebar"] {

        background: #ffffff;

    }


    </style>
    """, unsafe_allow_html=True)


    # ========================================================
    # DASHBOARD HEADER
    # ========================================================

    st.markdown(
        '<div class="dashboard-title">📊 PIM Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="dashboard-subtitle">'
        'Program Information Management Overview'
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # KPI CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(
        4,
        gap="medium"
    )


    with col1:

        st.markdown(
            kpi_card(
                "Total LF",
                total_LF,
                "👥",
                "LFs in the program"
            ),
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            kpi_card(
                "Total Schools",
                total_schools,
                "🏫",
                "Schools in the program"
            ),
            unsafe_allow_html=True
        )


    with col3:

        st.markdown(
            kpi_card(
                "Total Teachers",
                total_teachers,
                "👨‍🏫",
                "Teachers supported"
            ),
            unsafe_allow_html=True
        )


    with col4:

        st.markdown(
            kpi_card(
                "Total Visits",
                total_Visit,
                "📍",
                "Classroom visits"
            ),
            unsafe_allow_html=True
        )


    # ========================================================
    # DIVIDER
    # ========================================================

    st.markdown(
        '<div class="dashboard-divider"></div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # SIDEBAR NAVIGATION
    # ========================================================

    st.sidebar.title("📊 PIM Dashboard")

    st.sidebar.markdown(
        "---"
    )


    page = st.sidebar.radio(
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


    st.sidebar.markdown(
        "---"
    )


    if st.sidebar.button(
        "📂 Upload New Dataset",
        use_container_width=True
    ):

        st.session_state.page = "Upload"

        st.rerun()


    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False
        st.session_state.page = "Login"
        st.session_state.df = None

        st.rerun()


    # ========================================================
    # PAGE CONTENT
    # ========================================================

    if page == "Home":

        st.subheader("🏠 Home")

        st.info(
            "Welcome to the PIM Dashboard."
        )


    elif page == "Schools":

        st.subheader("🏫 Schools")

        if "School Name" in df.columns:

            school_count = df[
                "School Name"
            ].nunique()

            st.metric(
                "Unique Schools",
                school_count
            )

            school_table = (
                df[
                    ["School Name"]
                ]
                .drop_duplicates()
                .reset_index(drop=True)
            )

            st.dataframe(
                school_table,
                use_container_width=True
            )


    elif page == "Teachers":

        st.subheader("👨‍🏫 Teachers")

        if "Teacher Name" in df.columns:

            teacher_count = df[
                "Teacher Name"
            ].nunique()

            st.metric(
                "Unique Teachers",
                teacher_count
            )

            teacher_table = (
                df[
                    ["Teacher Name"]
                ]
                .drop_duplicates()
                .reset_index(drop=True)
            )

            st.dataframe(
                teacher_table,
                use_container_width=True
            )


    elif page == "Visits":

        st.subheader("📍 Visits")

        if total_visit_cols:

            monthly_visit_display = (
                df[total_visit_cols]
                .apply(
                    pd.to_numeric,
                    errors="coerce"
                )
                .fillna(0)
                .sum()
                .reset_index()
            )

            monthly_visit_display.columns = [
                "Month",
                "Total Visits"
            ]

            st.dataframe(
                monthly_visit_display,
                use_container_width=True
            )


    elif page == "Standards":

        st.subheader(
            "📈 Meeting Minimum Standards"
        )

        if minimum_standard_cols:

            standard_data = (
                df[minimum_standard_cols]
                .apply(
                    pd.to_numeric,
                    errors="coerce"
                )
            )

            total_standard_meet = (
                standard_data.sum().sum()
            )

            total_standard_records = (
                standard_data.count().sum()
            )


            if total_standard_records > 0:

                standard_percentage = (
                    total_standard_meet /
                    total_standard_records
                ) * 100

            else:

                standard_percentage = 0


            st.metric(
                "Standards Met",
                f"{standard_percentage:.1f}%"
            )


    elif page == "Reports":

        st.subheader("📑 Reports")

        st.write(
            "Report section is ready for additional analysis."
        )


# ============================================================
# MAIN APPLICATION ROUTING
# ============================================================

if not st.session_state.logged_in:

    login_page()

else:

    if st.session_state.page == "Upload":

        upload_page()

    elif st.session_state.page == "Dashboard":

        dashboard_page()

    else:

        upload_page()
