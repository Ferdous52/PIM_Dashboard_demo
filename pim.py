import streamlit as st

# ============================================================
# PIM DASHBOARD — DESIGN ONLY
# No data analysis / Excel processing / calculations
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
# GLOBAL DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GLOBAL
       ====================================================== */

    * {
        font-family: "Segoe UI", Arial, sans-serif;
    }

    .stApp {
        background: linear-gradient(
            135deg,
            #F8FAFC 0%,
            #F1F5F9 50%,
            #EEF2FF 100%
        );
    }

    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
        max-width: 1500px;
    }

    /* Hide Streamlit default elements */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ======================================================
       LOGIN PAGE
       ====================================================== */

    .login-page {
        min-height: 100vh;
        margin-top: -80px;
        display: flex;
        justify-content: center;
        align-items: center;
        background:
            radial-gradient(
                circle at top right,
                rgba(59, 130, 246, 0.20),
                transparent 35%
            ),
            radial-gradient(
                circle at bottom left,
                rgba(30, 64, 175, 0.20),
                transparent 40%
            ),
            linear-gradient(
                135deg,
                #0F172A 0%,
                #172554 50%,
                #1E3A8A 100%
            );
    }

    .login-container {
        width: 430px;
        max-width: 92%;
        padding: 42px 40px;
        border-radius: 24px;
        background: rgba(255,255,255,0.97);
        box-shadow:
            0 25px 60px rgba(0,0,0,0.30),
            0 8px 20px rgba(0,0,0,0.12);
        text-align: center;
    }

    .login-logo {
        width: 72px;
        height: 72px;
        margin: 0 auto 20px auto;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(
            135deg,
            #2563EB,
            #1D4ED8
        );
        color: white;
        font-size: 34px;
        box-shadow: 0 10px 25px rgba(37,99,235,0.30);
    }

    .login-title {
        font-size: 32px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 6px;
    }

    .login-subtitle {
        font-size: 14px;
        color: #64748B;
        margin-bottom: 30px;
        letter-spacing: 0.5px;
    }

    .login-welcome {
        font-size: 21px;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 8px;
    }

    .login-description {
        color: #64748B;
        font-size: 13px;
        margin-bottom: 20px;
    }

    /* ======================================================
       STREAMLIT INPUTS
       ====================================================== */

    .stTextInput > div > div > input {
        border-radius: 12px !important;
        border: 1px solid #CBD5E1 !important;
        background: #F8FAFC !important;
        color: #0F172A !important;
        padding: 12px 14px !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.12) !important;
    }

    .stTextInput label {
        font-weight: 600 !important;
        color: #334155 !important;
    }

    /* Login button */

    .stButton > button {
        width: 100%;
        min-height: 46px;
        border-radius: 12px;
        border: none;
        background: linear-gradient(
            135deg,
            #2563EB,
            #1D4ED8
        );
        color: white;
        font-size: 15px;
        font-weight: 700;
        box-shadow: 0 8px 18px rgba(37,99,235,0.25);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 12px 25px rgba(37,99,235,0.35);
    }

    /* ======================================================
       SIDEBAR
       ====================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0F172A 0%,
                #172554 100%
            );
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    section[data-testid="stSidebar"] > div {
        padding-top: 1.5rem;
    }

    .sidebar-brand {
        padding: 12px 10px 28px 10px;
        text-align: center;
    }

    .sidebar-logo {
        width: 55px;
        height: 55px;
        margin: 0 auto 12px auto;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(
            135deg,
            #3B82F6,
            #2563EB
        );
        color: white;
        font-size: 25px;
    }

    .sidebar-title {
        color: white;
        font-size: 21px;
        font-weight: 800;
    }

    .sidebar-subtitle {
        color: #94A3B8;
        font-size: 11px;
        margin-top: 4px;
    }

    section[data-testid="stSidebar"] .stRadio label {
        color: #CBD5E1 !important;
        font-weight: 500;
        padding: 8px 4px;
    }

    section[data-testid="stSidebar"] .stRadio label:hover {
        color: white !important;
    }

    /* ======================================================
       PAGE HEADER
       ====================================================== */

    .page-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 24px;
        padding-bottom: 18px;
        border-bottom: 1px solid #E2E8F0;
    }

    .page-title {
        font-size: 30px;
        font-weight: 800;
        color: #0F172A;
        margin: 0;
    }

    .page-description {
        color: #64748B;
        font-size: 14px;
        margin-top: 5px;
    }

    .header-badge {
        padding: 8px 15px;
        border-radius: 20px;
        background: #EFF6FF;
        color: #1D4ED8;
        font-size: 12px;
        font-weight: 700;
        border: 1px solid #DBEAFE;
    }

    /* ======================================================
       KPI CARDS
       ====================================================== */

    .metric-card {
        background: rgba(255,255,255,0.96);
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 22px;
        min-height: 145px;
        box-shadow: 0 6px 20px rgba(15,23,42,0.06);
        transition: all 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(15,23,42,0.10);
    }

    .metric-icon {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #EFF6FF;
        color: #2563EB;
        font-size: 20px;
        margin-bottom: 14px;
    }

    .metric-label {
        color: #64748B;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 5px;
    }

    .metric-value {
        color: #0F172A;
        font-size: 29px;
        font-weight: 800;
        line-height: 1.1;
    }

    .metric-change {
        color: #64748B;
        font-size: 11px;
        margin-top: 7px;
    }

    /* ======================================================
       CONTENT CARDS
       ====================================================== */

    .content-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 18px;
        padding: 22px;
        margin-top: 20px;
        box-shadow: 0 6px 20px rgba(15,23,42,0.05);
    }

    .content-card-title {
        font-size: 18px;
        font-weight: 750;
        color: #0F172A;
        margin-bottom: 5px;
    }

    .content-card-subtitle {
        color: #64748B;
        font-size: 12px;
        margin-bottom: 18px;
    }

    /* ======================================================
       SECTION TITLES
       ====================================================== */

    .section-title {
        font-size: 19px;
        font-weight: 750;
        color: #0F172A;
        margin-top: 28px;
        margin-bottom: 14px;
    }

    /* ======================================================
       DATA TABLE
       ====================================================== */

    .stDataFrame {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid #E2E8F0;
    }

    /* ======================================================
       SELECTBOX / MULTISELECT
       ====================================================== */

    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        border-radius: 10px !important;
        border-color: #CBD5E1 !important;
    }

    .stSelectbox label,
    .stMultiSelect label {
        font-weight: 600 !important;
        color: #334155 !important;
    }

    /* ======================================================
       FILE UPLOADER
       ====================================================== */

    [data-testid="stFileUploader"] {
        background: white;
        border: 1px dashed #94A3B8;
        border-radius: 16px;
        padding: 8px;
    }

    /* ======================================================
       DOWNLOAD BUTTON
       ====================================================== */

    .stDownloadButton > button {
        border-radius: 10px;
        background: white;
        color: #1D4ED8;
        border: 1px solid #BFDBFE;
        font-weight: 600;
    }

    .stDownloadButton > button:hover {
        background: #EFF6FF;
        border-color: #93C5FD;
    }

    /* ======================================================
       INFO / SUCCESS / ERROR
       ====================================================== */

    .stAlert {
        border-radius: 12px;
    }

    /* ======================================================
       FOOTER
       ====================================================== */

    .dashboard-footer {
        text-align: center;
        color: #94A3B8;
        font-size: 11px;
        margin-top: 40px;
        padding: 20px;
        border-top: 1px solid #E2E8F0;
    }

    /* ======================================================
       RESPONSIVE
       ====================================================== */

    @media (max-width: 768px) {

        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .page-title {
            font-size: 24px;
        }

        .metric-card {
            margin-bottom: 10px;
        }

        .login-container {
            padding: 30px 25px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGIN DESIGN
# ============================================================

def login_page():

    st.markdown(
        """
        <div class="login-page">
            <div class="login-container">

                <div class="login-logo">
                    📊
                </div>

                <div class="login-title">
                    PIM Dashboard
                </div>

                <div class="login-subtitle">
                    Monitor • Analyze • Improve
                </div>

                <div class="login-welcome">
                    Welcome Back!
                </div>

                <div class="login-description">
                    Sign in to access your dashboard
                </div>

            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Login inputs are positioned over the designed card
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        username = st.text_input(
            "Username",
            placeholder="Enter username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter password",
            type="password",
            key="login_password"
        )

        if st.button("Sign In", use_container_width=True):

            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password.")


# ============================================================
# DASHBOARD HEADER
# ============================================================

def page_header(title, description, badge=None):

    badge_html = ""

    if badge:
        badge_html = f"""
        <div class="header-badge">
            {badge}
        </div>
        """

    st.markdown(
        f"""
        <div class="page-header">

            <div>
                <div class="page-title">
                    {title}
                </div>

                <div class="page-description">
                    {description}
                </div>
            </div>

            {badge_html}

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# KPI CARD
# ============================================================

def metric_card(icon, label, value, description=""):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-icon">
                {icon}
            </div>

            <div class="metric-label">
                {label}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-change">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# CONTENT CARD
# ============================================================

def content_card(title, subtitle=""):

    st.markdown(
        f"""
        <div class="content-card">

            <div class="content-card-title">
                {title}
            </div>

            <div class="content-card-subtitle">
                {subtitle}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-brand">

                <div class="sidebar-logo">
                    📊
                </div>

                <div class="sidebar-title">
                    PIM Dashboard
                </div>

                <div class="sidebar-subtitle">
                    Program Information Management
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        page = st.radio(
            "Navigation",
            [
                "🏠 Home",
                "🏫 Schools",
                "👨‍🏫 Teachers",
                "📍 Visits",
                "✓ Standards",
                "📊 Reports"
            ],
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            st.session_state.logged_in = False
            st.rerun()

    return page


# ============================================================
# HOME DESIGN
# ============================================================

def home_page():

    page_header(
        "Dashboard Overview",
        "Monitor your PIM program at a glance",
        "LIVE DASHBOARD"
    )

    st.markdown(
        '<div class="section-title">Key Performance Indicators</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "🏫",
            "Total Schools",
            "0",
            "Registered schools"
        )

    with c2:
        metric_card(
            "👨‍🏫",
            "Total Teachers",
            "0",
            "Registered teachers"
        )

    with c3:
        metric_card(
            "📍",
            "Total Visits",
            "0",
            "Completed visits"
        )

    with c4:
        metric_card(
            "✓",
            "Standards Met",
            "0%",
            "Overall performance"
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                Monthly Visit Overview
            </div>

            <div class="content-card-subtitle">
                Monthly performance visualization
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Chart area — connect your analysis/data code here.")


# ============================================================
# SCHOOLS DESIGN
# ============================================================

def schools_page():

    page_header(
        "Schools",
        "School-level program overview",
        "SCHOOLS"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card(
            "🏫",
            "Total Schools",
            "0",
            "Unique schools"
        )

    with c2:
        metric_card(
            "👥",
            "Active Staff",
            "0",
            "Assigned staff"
        )

    with c3:
        metric_card(
            "📊",
            "Coverage",
            "0%",
            "School coverage"
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                School Summary
            </div>

            <div class="content-card-subtitle">
                School-wise overview and performance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("School analysis table will appear here.")


# ============================================================
# TEACHERS DESIGN
# ============================================================

def teachers_page():

    page_header(
        "Teachers",
        "Teacher-level program overview",
        "TEACHERS"
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        metric_card(
            "👨‍🏫",
            "Total Teachers",
            "0",
            "Unique teachers"
        )

    with c2:
        metric_card(
            "🏫",
            "Schools",
            "0",
            "Teacher coverage"
        )

    with c3:
        metric_card(
            "📈",
            "Performance",
            "0%",
            "Overall performance"
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                Teacher Summary
            </div>

            <div class="content-card-subtitle">
                Teacher-wise performance overview
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Teacher analysis table will appear here.")


# ============================================================
# VISITS DESIGN
# ============================================================

def visits_page():

    page_header(
        "Visits",
        "Monitor visit targets and completion",
        "VISITS"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "🎯",
            "Target Visits",
            "0",
            "Planned visits"
        )

    with c2:
        metric_card(
            "📍",
            "Actual Visits",
            "0",
            "Completed visits"
        )

    with c3:
        metric_card(
            "📉",
            "Visit Gap",
            "0",
            "Target minus actual"
        )

    with c4:
        metric_card(
            "📊",
            "Achievement",
            "0%",
            "Target achievement"
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                Visit Performance
            </div>

            <div class="content-card-subtitle">
                Staff-wise visit performance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Visit analysis table will appear here.")


# ============================================================
# STANDARDS DESIGN
# ============================================================

def standards_page():

    page_header(
        "Standards",
        "Monitor minimum standards performance",
        "STANDARDS"
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "1️⃣",
            "Grade 1",
            "0",
            "Standards met"
        )

    with c2:
        metric_card(
            "2️⃣",
            "Grade 2",
            "0",
            "Standards met"
        )

    with c3:
        metric_card(
            "✓",
            "Total Standards",
            "0",
            "Standards met"
        )

    with c4:
        metric_card(
            "📈",
            "Achievement",
            "0%",
            "Overall standards"
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                Standards Performance
            </div>

            <div class="content-card-subtitle">
                Grade-wise and staff-wise standards performance
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Standards analysis table will appear here.")


# ============================================================
# REPORTS DESIGN
# ============================================================

def reports_page():

    page_header(
        "Reports",
        "Filter and export program information",
        "REPORTS"
    )

    st.markdown(
        '<div class="section-title">Report Filters</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.selectbox(
            "RtR Staff",
            ["All Staff"]
        )

    with c2:
        st.selectbox(
            "Grade",
            ["All Grades"]
        )

    with c3:
        st.selectbox(
            "Report Type",
            [
                "Overview",
                "Schools",
                "Teachers",
                "Visits",
                "Standards"
            ]
        )

    st.markdown(
        """
        <div class="content-card">

            <div class="content-card-title">
                Report Preview
            </div>

            <div class="content-card-subtitle">
                Filtered report data will appear here
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info("Report table will appear here.")

    st.download_button(
        "⬇️ Download Report",
        data="",
        file_name="PIM_Report.csv",
        mime="text/csv"
    )


# ============================================================
# MAIN APPLICATION
# ============================================================

if not st.session_state.logged_in:

    login_page()

else:

    selected_page = sidebar()

    if selected_page == "🏠 Home":
        home_page()

    elif selected_page == "🏫 Schools":
        schools_page()

    elif selected_page == "👨‍🏫 Teachers":
        teachers_page()

    elif selected_page == "📍 Visits":
        visits_page()

    elif selected_page == "✓ Standards":
        standards_page()

    elif selected_page == "📊 Reports":
        reports_page()

    st.markdown(
        """
        <div class="dashboard-footer">
            PIM Dashboard • Program Information Management
        </div>
        """,
        unsafe_allow_html=True
    )
