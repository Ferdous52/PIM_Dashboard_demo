import streamlit as st

# ============================================================
# PIM DASHBOARD — DESIGN ONLY
# No Excel / pandas / analysis code
# ============================================================

st.set_page_config(
    page_title="PIM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ============================================================
# GLOBAL DESIGN
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* =========================
   GLOBAL
   ========================= */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #F7F8FC;
}

.main {
    padding-top: 0rem;
}

/* Remove default header */
header[data-testid="stHeader"] {
    background: transparent;
}

/* =========================
   LOGIN PAGE
   ========================= */

.login-background {
    min-height: 100vh;
    width: 100%;
    margin: -5rem 0 0 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(59,130,246,0.18),
            transparent 35%
        ),
        radial-gradient(
            circle at 80% 80%,
            rgba(99,102,241,0.15),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #0B1220 0%,
            #111827 50%,
            #172554 100%
        );
}

.login-card {
    width: 420px;
    padding: 42px 40px;
    border-radius: 24px;
    background: rgba(255,255,255,0.97);
    box-shadow:
        0 25px 70px rgba(0,0,0,0.35),
        0 10px 30px rgba(0,0,0,0.15);
    text-align: center;
}

.login-logo {
    width: 72px;
    height: 72px;
    margin: 0 auto 22px auto;
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(
        135deg,
        #2563EB,
        #4F46E5
    );
    color: white;
    font-size: 32px;
    box-shadow: 0 10px 25px rgba(37,99,235,0.30);
}

.login-title {
    font-size: 30px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 5px;
}

.login-subtitle {
    color: #64748B;
    font-size: 14px;
    margin-bottom: 30px;
}

.login-welcome {
    text-align: left;
    font-size: 20px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 5px;
}

.login-description {
    text-align: left;
    color: #64748B;
    font-size: 13px;
    margin-bottom: 20px;
}

/* Login inputs */

div[data-testid="stForm"] {
    border: none;
    padding: 0;
}

div[data-testid="stTextInput"] label {
    color: #334155;
    font-size: 13px;
    font-weight: 600;
}

div[data-testid="stTextInput"] input {
    height: 48px;
    border-radius: 12px;
    border: 1px solid #E2E8F0;
    background: #F8FAFC;
    color: #111827;
    padding-left: 14px;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #2563EB;
    box-shadow: 0 0 0 2px rgba(37,99,235,0.10);
}

/* Login button */

.login-card button[kind="primary"] {
    width: 100%;
    height: 48px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(
        135deg,
        #2563EB,
        #4F46E5
    );
    color: white;
    font-weight: 700;
    font-size: 14px;
    transition: 0.2s ease;
}

.login-card button[kind="primary"]:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 20px rgba(37,99,235,0.25);
}

/* =========================
   SIDEBAR
   ========================= */

section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0F172A 0%,
            #111827 100%
        );
    border-right: 1px solid rgba(255,255,255,0.06);
}

section[data-testid="stSidebar"] > div {
    padding-top: 1.5rem;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 10px 12px 25px 12px;
}

.sidebar-logo-icon {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(
        135deg,
        #2563EB,
        #4F46E5
    );
    color: white;
    font-size: 20px;
}

.sidebar-logo-text {
    color: white;
    font-size: 19px;
    font-weight: 800;
}

.sidebar-logo-sub {
    color: #94A3B8;
    font-size: 10px;
    margin-top: 2px;
}

/* Sidebar radio */

section[data-testid="stSidebar"]
div[role="radiogroup"] {
    gap: 7px;
}

section[data-testid="stSidebar"]
div[role="radiogroup"] label {
    border-radius: 12px;
    padding: 11px 12px;
    color: #CBD5E1;
    transition: 0.2s ease;
}

section[data-testid="stSidebar"]
div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.07);
    color: white;
}

section[data-testid="stSidebar"]
div[role="radiogroup"]
label[data-checked="true"] {
    background: linear-gradient(
        135deg,
        rgba(37,99,235,0.95),
        rgba(79,70,229,0.95)
    );
    color: white;
}

/* =========================
   MAIN HEADER
   ========================= */

.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 5px 0 25px 0;
}

.dashboard-title {
    font-size: 30px;
    font-weight: 800;
    color: #0F172A;
    margin: 0;
}

.dashboard-subtitle {
    color: #64748B;
    font-size: 14px;
    margin-top: 5px;
}

.user-badge {
    display: flex;
    align-items: center;
    gap: 10px;
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 14px;
    padding: 8px 14px;
    box-shadow: 0 3px 12px rgba(15,23,42,0.05);
}

.user-avatar {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: #DBEAFE;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #2563EB;
    font-weight: 700;
}

/* =========================
   KPI CARDS
   ========================= */

.kpi-card {
    background: white;
    border: 1px solid #E8ECF3;
    border-radius: 18px;
    padding: 22px;
    min-height: 145px;
    box-shadow:
        0 4px 16px rgba(15,23,42,0.04);
    transition: 0.2s ease;
}

.kpi-card:hover {
    transform: translateY(-2px);
    box-shadow:
        0 10px 25px rgba(15,23,42,0.08);
}

.kpi-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.kpi-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #EFF6FF;
    color: #2563EB;
    font-size: 21px;
}

.kpi-label {
    color: #64748B;
    font-size: 13px;
    font-weight: 600;
    margin-top: 16px;
}

.kpi-value {
    color: #0F172A;
    font-size: 30px;
    font-weight: 800;
    margin-top: 4px;
}

.kpi-change {
    color: #16A34A;
    font-size: 11px;
    font-weight: 600;
    margin-top: 5px;
}

/* =========================
   SECTION CARDS
   ========================= */

.section-card {
    background: white;
    border: 1px solid #E8ECF3;
    border-radius: 18px;
    padding: 22px;
    box-shadow:
        0 4px 16px rgba(15,23,42,0.04);
}

.section-title {
    font-size: 17px;
    font-weight: 750;
    color: #0F172A;
    margin-bottom: 3px;
}

.section-subtitle {
    font-size: 12px;
    color: #64748B;
    margin-bottom: 18px;
}

/* =========================
   FILTER AREA
   ========================= */

.filter-card {
    background: white;
    border: 1px solid #E8ECF3;
    border-radius: 16px;
    padding: 18px 20px;
    margin-bottom: 20px;
}

div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label {
    font-size: 12px;
    font-weight: 600;
    color: #475569;
}

div[data-testid="stSelectbox"] > div > div {
    border-radius: 10px;
}

/* =========================
   TABLE
   ========================= */

div[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #E2E8F0;
}

/* =========================
   FILE UPLOADER
   ========================= */

section[data-testid="stFileUploaderDropzone"] {
    border: 2px dashed #CBD5E1;
    border-radius: 16px;
    background: #F8FAFC;
}

section[data-testid="stFileUploaderDropzone"]:hover {
    border-color: #2563EB;
    background: #EFF6FF;
}

/* =========================
   BUTTONS
   ========================= */

.stButton > button {
    border-radius: 10px;
    border: 1px solid #E2E8F0;
    background: white;
    color: #334155;
    font-weight: 600;
}

.stButton > button:hover {
    border-color: #2563EB;
    color: #2563EB;
}

/* =========================
   DOWNLOAD BUTTON
   ========================= */

.stDownloadButton > button {
    border-radius: 10px;
    background: #2563EB;
    color: white;
    border: none;
    font-weight: 600;
}

/* =========================
   PROGRESS
   ========================= */

div[data-testid="stProgress"] > div > div {
    border-radius: 10px;
}

/* =========================
   ALERTS
   ========================= */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* =========================
   DIVIDER
   ========================= */

hr {
    border: none;
    border-top: 1px solid #E2E8F0;
    margin: 20px 0;
}

/* =========================
   FOOTER
   ========================= */

.dashboard-footer {
    text-align: center;
    padding: 35px 0 15px 0;
    color: #94A3B8;
    font-size: 11px;
}

/* =========================
   RESPONSIVE
   ========================= */

@media (max-width: 900px) {

    .dashboard-title {
        font-size: 24px;
    }

    .kpi-card {
        min-height: 125px;
    }

    .login-card {
        width: 90%;
        padding: 30px;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOGIN DESIGN
# ============================================================

def login_page():

    st.markdown("""
    <div class="login-background">

        <div class="login-card">

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
    """, unsafe_allow_html=True)

    # Login form is kept only for the visual structure.
    # Replace authentication logic later if needed.

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

        login = st.form_submit_button(
            "Sign In",
            type="primary",
            use_container_width=True
        )

        if login:
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid username or password.")


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():

    st.markdown("""
    <div class="sidebar-logo">

        <div class="sidebar-logo-icon">
            📊
        </div>

        <div>
            <div class="sidebar-logo-text">
                PIM Dashboard
            </div>

            <div class="sidebar-logo-sub">
                PROGRAM MONITORING
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "",
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

    st.markdown("---")

    if st.button(
        "🚪  Logout",
        use_container_width=True
    ):
        st.session_state.logged_in = False
        st.rerun()

    return page


# ============================================================
# DASHBOARD HEADER
# ============================================================

def dashboard_header(title, subtitle):

    st.markdown(f"""
    <div class="dashboard-header">

        <div>
            <div class="dashboard-title">
                {title}
            </div>

            <div class="dashboard-subtitle">
                {subtitle}
            </div>
        </div>

        <div class="user-badge">

            <div class="user-avatar">
                A
            </div>

            <div>
                <div style="
                    font-size:13px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    Administrator
                </div>

                <div style="
                    font-size:10px;
                    color:#64748B;
                ">
                    PIM User
                </div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# KPI CARD
# ============================================================

def kpi_card(icon, label, value, change=""):

    st.markdown(f"""
    <div class="kpi-card">

        <div class="kpi-top">

            <div class="kpi-icon">
                {icon}
            </div>

        </div>

        <div class="kpi-label">
            {label}
        </div>

        <div class="kpi-value">
            {value}
        </div>

        <div class="kpi-change">
            {change}
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SECTION CARD
# ============================================================

def section_header(title, subtitle=""):

    st.markdown(f"""
    <div class="section-title">
        {title}
    </div>

    <div class="section-subtitle">
        {subtitle}
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HOME DESIGN
# ============================================================

def home_page():

    dashboard_header(
        "Dashboard Overview",
        "Monitor program performance at a glance"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI ROW
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card(
            "🏫",
            "Total Schools",
            "120",
            "↑ 8% this month"
        )

    with c2:
        kpi_card(
            "👨‍🏫",
            "Total Teachers",
            "2,450",
            "↑ 5% this month"
        )

    with c3:
        kpi_card(
            "📍",
            "Total Visits",
            "1,680",
            "↑ 12% this month"
        )

    with c4:
        kpi_card(
            "✓",
            "Standards Met",
            "78.5%",
            "↑ 4.2% this month"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # CHART / SUMMARY AREA
    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown("""
        <div class="section-card">

            <div class="section-title">
                Monthly Visit Performance
            </div>

            <div class="section-subtitle">
                Overview of visits completed each month
            </div>

        </div>
        """, unsafe_allow_html=True)

        # Design placeholder
        chart_placeholder = st.empty()

        chart_placeholder.markdown("""
        <div style="
            height:300px;
            background:#F8FAFC;
            border:1px dashed #CBD5E1;
            border-radius:14px;
            display:flex;
            align-items:center;
            justify-content:center;
            color:#94A3B8;
            font-size:14px;
        ">
            Monthly Chart Area
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="section-card">

            <div class="section-title">
                Performance Summary
            </div>

            <div class="section-subtitle">
                Current program status
            </div>

            <div style="
                margin-top:20px;
                padding:18px;
                border-radius:14px;
                background:#F8FAFC;
            ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:14px;
                ">
                    <span style="color:#64748B;font-size:13px;">
                        Visit Target
                    </span>
                    <b style="color:#0F172A;">
                        2,000
                    </b>
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:14px;
                ">
                    <span style="color:#64748B;font-size:13px;">
                        Completed
                    </span>
                    <b style="color:#0F172A;">
                        1,680
                    </b>
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                ">
                    <span style="color:#64748B;font-size:13px;">
                        Completion
                    </span>
                    <b style="color:#2563EB;">
                        84%
                    </b>
                </div>

            </div>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # RECENT ACTIVITY
    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            Recent Activity
        </div>

        <div class="section-subtitle">
            Latest dashboard updates
        </div>

        <div style="
            display:grid;
            grid-template-columns:repeat(3,1fr);
            gap:15px;
        ">

            <div style="
                padding:15px;
                border-radius:12px;
                background:#F8FAFC;
            ">
                <b style="font-size:13px;">
                    📍 Visit Update
                </b>
                <br>
                <span style="
                    font-size:11px;
                    color:#64748B;
                ">
                    Monthly visits updated
                </span>
            </div>

            <div style="
                padding:15px;
                border-radius:12px;
                background:#F8FAFC;
            ">
                <b style="font-size:13px;">
                    ✓ Standards
                </b>
                <br>
                <span style="
                    font-size:11px;
                    color:#64748B;
                ">
                    Standards data reviewed
                </span>
            </div>

            <div style="
                padding:15px;
                border-radius:12px;
                background:#F8FAFC;
            ">
                <b style="font-size:13px;">
                    📊 Report
                </b>
                <br>
                <span style="
                    font-size:11px;
                    color:#64748B;
                ">
                    Latest report generated
                </span>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SCHOOLS DESIGN
# ============================================================

def schools_page():

    dashboard_header(
        "Schools",
        "School-level program monitoring"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi_card("🏫", "Total Schools", "120")

    with c2:
        kpi_card("📍", "Active Schools", "112")

    with c3:
        kpi_card("✓", "Coverage", "93.3%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">
        <div class="section-title">
            School Summary
        </div>

        <div class="section-subtitle">
            School-wise monitoring overview
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        {
            "School": [
                "School A",
                "School B",
                "School C",
                "School D",
                "School E"
            ],
            "Staff": [
                "Staff 01",
                "Staff 02",
                "Staff 03",
                "Staff 01",
                "Staff 04"
            ],
            "Teachers": [
                25, 31, 28, 22, 35
            ],
            "Visits": [
                40, 52, 45, 38, 60
            ],
            "Status": [
                "Active",
                "Active",
                "Active",
                "Active",
                "Active"
            ]
        },
        hide_index=True,
        use_container_width=True
    )


# ============================================================
# TEACHERS DESIGN
# ============================================================

def teachers_page():

    dashboard_header(
        "Teachers",
        "Teacher-level monitoring and coverage"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi_card("👨‍🏫", "Total Teachers", "2,450")

    with c2:
        kpi_card("🏫", "Schools Covered", "120")

    with c3:
        kpi_card("📍", "Average Visits", "4.8")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            Teacher Summary
        </div>

        <div class="section-subtitle">
            Teacher-wise monitoring overview
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        {
            "Teacher": [
                "Teacher 01",
                "Teacher 02",
                "Teacher 03",
                "Teacher 04",
                "Teacher 05"
            ],
            "School": [
                "School A",
                "School B",
                "School C",
                "School A",
                "School D"
            ],
            "Grade": [
                1, 2, 1, 2, 1
            ],
            "Visits": [
                8, 10, 7, 9, 11
            ],
            "Standard": [
                "Met",
                "Met",
                "Not Met",
                "Met",
                "Met"
            ]
        },
        hide_index=True,
        use_container_width=True
    )


# ============================================================
# VISITS DESIGN
# ============================================================

def visits_page():

    dashboard_header(
        "Visits",
        "Monitor target versus completed visits"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        kpi_card("🎯", "Target Visits", "2,000")

    with c2:
        kpi_card("📍", "Actual Visits", "1,680")

    with c3:
        kpi_card("📉", "Visit Gap", "320")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            Visit Performance
        </div>

        <div class="section-subtitle">
            Staff-wise target and actual visits
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        {
            "Staff": [
                "Staff 01",
                "Staff 02",
                "Staff 03",
                "Staff 04",
                "Staff 05"
            ],
            "Target Visits": [
                180, 200, 160, 220, 190
            ],
            "Actual Visits": [
                165, 190, 148, 205, 175
            ],
            "Gap": [
                15, 10, 12, 15, 15
            ],
            "Performance": [
                "92%",
                "95%",
                "93%",
                "93%",
                "92%"
            ]
        },
        hide_index=True,
        use_container_width=True
    )


# ============================================================
# STANDARDS DESIGN
# ============================================================

def standards_page():

    dashboard_header(
        "Standards",
        "Monitor teacher performance against minimum standards"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        kpi_card("1️⃣", "Grade 1", "82%")

    with c2:
        kpi_card("2️⃣", "Grade 2", "75%")

    with c3:
        kpi_card("✓", "Total Standards", "78.5%")

    with c4:
        kpi_card("📈", "Improvement", "+4.2%")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            Standards Performance
        </div>

        <div class="section-subtitle">
            Staff-wise minimum standard achievement
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        {
            "Staff": [
                "Staff 01",
                "Staff 02",
                "Staff 03",
                "Staff 04",
                "Staff 05"
            ],
            "Grade 1": [
                "84%",
                "80%",
                "76%",
                "88%",
                "81%"
            ],
            "Grade 2": [
                "77%",
                "74%",
                "70%",
                "82%",
                "73%"
            ],
            "Overall": [
                "81%",
                "77%",
                "73%",
                "85%",
                "77%"
            ]
        },
        hide_index=True,
        use_container_width=True
    )


# ============================================================
# REPORTS DESIGN
# ============================================================

def reports_page():

    dashboard_header(
        "Reports",
        "Filter, view and export monitoring reports"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="filter-card">

        <div class="section-title">
            Report Filters
        </div>

        <div class="section-subtitle">
            Select the required filters
        </div>

    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.selectbox(
            "RtR Staff",
            [
                "All Staff",
                "Staff 01",
                "Staff 02",
                "Staff 03",
                "Staff 04"
            ]
        )

    with c2:
        st.selectbox(
            "Grade",
            [
                "All Grades",
                "Grade 1",
                "Grade 2",
                "Grade 3"
            ]
        )

    with c3:
        st.selectbox(
            "Report Type",
            [
                "School Report",
                "Teacher Report",
                "Visit Report",
                "Standards Report"
            ]
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-card">

        <div class="section-title">
            Report Preview
        </div>

        <div class="section-subtitle">
            Filtered report data will appear here
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        {
            "Staff": [
                "Staff 01",
                "Staff 02",
                "Staff 03",
                "Staff 04"
            ],
            "School": [
                "School A",
                "School B",
                "School C",
                "School D"
            ],
            "Teachers": [
                25,
                31,
                28,
                35
            ],
            "Visits": [
                40,
                52,
                45,
                60
            ],
            "Standards": [
                "82%",
                "78%",
                "75%",
                "86%"
            ]
        },
        hide_index=True,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.download_button(
        "⬇️ Download Report",
        data="Report",
        file_name="pim_report.csv",
        mime="text/csv"
    )


# ============================================================
# MAIN APP
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

    st.markdown("""
    <div class="dashboard-footer">
        PIM Dashboard • Program Monitoring System
    </div>
    """, unsafe_allow_html=True)
