import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PIM Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DESIGN TOKENS
# ============================================================
# Single source of truth for the palette so login + dashboard
# stay visually consistent. Change these and the whole app updates.

INK        = "#0B1220"   # near-black text / dark surface
INK_SOFT   = "#475569"   # secondary text
SURFACE    = "#F6F7FB"   # app background
CARD       = "#FFFFFF"   # card background
BORDER     = "#E6E8F0"   # hairline borders
ACCENT     = "#4F46E5"   # indigo — primary actions
ACCENT_2   = "#059669"   # emerald — positive / success
ACCENT_3   = "#DC2626"   # red — gap / warning
MUTED_BG   = "#EEF0FB"   # pale accent chip background

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Helvetica", "Arial"],
    "axes.edgecolor": BORDER,
    "axes.labelcolor": INK_SOFT,
    "xtick.color": INK_SOFT,
    "ytick.color": INK_SOFT,
    "text.color": INK,
})

# ============================================================
# SESSION STATE
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# ============================================================
# LOGIN PAGE
# ============================================================

if not st.session_state.logged_in:

    st.markdown(f"""
    <style>

    #MainMenu, header, footer {{ visibility: hidden; }}

    .stApp {{
        background:
            radial-gradient(circle at 15% 15%, #1E293B 0%, {INK} 45%, #05070C 100%) !important;
    }}

    .main .block-container {{
        min-height: 100vh;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 30px !important;
        padding-bottom: 30px !important;
        max-width: 480px;
    }}

    .pim-badge {{
        display: flex;
        justify-content: center;
        margin-bottom: 18px;
    }}

    .pim-badge span {{
        width: 56px;
        height: 56px;
        border-radius: 16px;
        background: linear-gradient(135deg, {ACCENT}, #7C3AED);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        box-shadow: 0 8px 24px rgba(79,70,229,0.45);
    }}

    .pim-title {{
        text-align: center;
        color: white;
        font-size: 30px;
        font-weight: 700;
        letter-spacing: -0.02em;
        margin-top: 0;
        margin-bottom: 4px;
    }}

    .pim-subtitle {{
        text-align: center;
        color: #94A3B8;
        font-size: 14px;
        margin-bottom: 28px;
        letter-spacing: 0.02em;
        text-transform: uppercase;
    }}

    [data-testid="stForm"] {{
        background: rgba(255,255,255,0.04);
        backdrop-filter: blur(20px);
        padding: 32px !important;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    [data-testid="stForm"] label {{
        color: #CBD5E1 !important;
        font-weight: 500;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }}

    [data-testid="stForm"] input {{
        background-color: rgba(255,255,255,0.06) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.14) !important;
        border-radius: 10px !important;
        padding: 10px 14px !important;
    }}

    [data-testid="stForm"] input:focus {{
        border-color: {ACCENT} !important;
        box-shadow: 0 0 0 3px rgba(79,70,229,0.25) !important;
    }}

    [data-testid="stForm"] input::placeholder {{
        color: #64748B !important;
    }}

    [data-testid="stFormSubmitButton"] button {{
        width: 100%;
        background: linear-gradient(135deg, {ACCENT}, #7C3AED);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 15px;
        font-weight: 600;
        margin-top: 6px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}

    [data-testid="stFormSubmitButton"] button:hover {{
        transform: translateY(-1px);
        box-shadow: 0 10px 28px rgba(79,70,229,0.45);
    }}

    @media (max-width: 600px) {{
        .main .block-container {{ padding-left: 20px !important; padding-right: 20px !important; }}
        .pim-title {{ font-size: 26px; }}
        [data-testid="stForm"] {{ padding: 22px !important; border-radius: 16px; }}
    }}

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="pim-badge"><span>📊</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="pim-title">PIM Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="pim-subtitle">Monitor · Analyze · Improve</div>', unsafe_allow_html=True)

    with st.form("login_form"):

        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        login_button = st.form_submit_button("Sign In")

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

st.markdown(f"""
<style>

#MainMenu, footer {{ visibility: hidden; }}

/* GLOBAL */
.stApp {{
    background: {SURFACE} !important;
}}

.main .block-container {{
    max-width: 1400px !important;
    padding-top: 1.5rem !important;
    padding-left: 2.5rem !important;
    padding-right: 2.5rem !important;
    padding-bottom: 2.5rem !important;
}}

html, body, [class*="css"] {{
    font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}}

/* HEADER BLOCK */
.dash-header {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
}}

.dashboard-title {{
    color: {INK};
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.01em;
    margin-bottom: 2px;
}}

.dashboard-subtitle {{
    color: {INK_SOFT};
    font-size: 14px;
    margin-bottom: 22px;
}}

.section-divider {{
    height: 1px;
    background: {BORDER};
    border: none;
    margin: 22px 0;
}}

/* METRIC CARDS */
[data-testid="stMetric"] {{
    background: {CARD};
    padding: 18px 20px;
    border-radius: 14px;
    border: 1px solid {BORDER};
    box-shadow: 0 1px 2px rgba(15,23,42,0.04);
    transition: box-shadow 0.15s ease, transform 0.15s ease;
}}

[data-testid="stMetric"]:hover {{
    box-shadow: 0 8px 24px rgba(15,23,42,0.08);
    transform: translateY(-2px);
}}

[data-testid="stMetricLabel"] {{
    color: {INK_SOFT} !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    text-transform: uppercase;
    letter-spacing: 0.03em;
}}

[data-testid="stMetricValue"] {{
    color: {INK} !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}}

/* SIDEBAR */
[data-testid="stSidebar"] {{
    background-color: {INK};
    border-right: 1px solid rgba(255,255,255,0.06);
}}

[data-testid="stSidebar"] * {{
    color: #E2E8F0 !important;
}}

.sidebar-brand {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 6px 0 18px 0;
}}

.sidebar-brand .icon {{
    width: 38px;
    height: 38px;
    border-radius: 10px;
    background: linear-gradient(135deg, {ACCENT}, #7C3AED);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
}}

.sidebar-brand .txt {{
    font-size: 16px;
    font-weight: 700;
    color: white !important;
}}

[data-testid="stSidebar"] [data-testid="stRadio"] label {{
    padding: 4px 0;
}}

[data-testid="stSidebar"] hr {{
    border-color: rgba(255,255,255,0.10);
}}

[data-testid="stSidebar"] button {{
    border-radius: 8px;
    background-color: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12) !important;
}}

[data-testid="stSidebar"] button:hover {{
    background-color: rgba(239,68,68,0.18);
    border-color: rgba(239,68,68,0.4) !important;
}}

/* DATAFRAME */
[data-testid="stDataFrame"] {{
    border-radius: 12px;
    border: 1px solid {BORDER};
    overflow: hidden;
}}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {{
    background: {CARD};
    border-radius: 14px;
    padding: 14px;
    border: 1.5px dashed {BORDER};
}}

/* SELECTBOX */
[data-baseweb="select"] > div {{
    border-radius: 10px !important;
    border-color: {BORDER} !important;
}}

/* ALERTS */
.stAlert {{
    border-radius: 12px;
}}

/* BUTTONS */
.stButton > button,
.stDownloadButton > button {{
    border-radius: 10px;
    font-weight: 600;
    border: 1px solid {BORDER};
}}

.stDownloadButton > button {{
    background: {ACCENT};
    color: white;
    border: none;
}}

.stDownloadButton > button:hover {{
    background: #4338CA;
    color: white;
}}

/* EXPANDER */
[data-testid="stExpander"] {{
    border-radius: 12px;
    border: 1px solid {BORDER};
    background: {CARD};
}}

/* MOBILE */
@media (max-width: 600px) {{
    .main .block-container {{
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
    }}
    .dashboard-title {{ font-size: 21px; }}
    .dashboard-subtitle {{ font-size: 13px; }}
    [data-testid="stMetricValue"] {{ font-size: 22px !important; }}
}}

</style>
""", unsafe_allow_html=True)


def section_header(title, subtitle):
    st.markdown(f'<div class="dashboard-title">{title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="dashboard-subtitle">{subtitle}</div>', unsafe_allow_html=True)


def styled_line_chart(x, y, xlabel, ylabel, title):
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor(CARD)
    ax.set_facecolor(CARD)

    ax.plot(x, y, marker="o", markersize=7, linewidth=2.5, color=ACCENT,
            markerfacecolor="white", markeredgewidth=2, markeredgecolor=ACCENT, zorder=3)
    ax.fill_between(range(len(x)), y, color=ACCENT, alpha=0.06)

    for i, value in enumerate(y):
        ax.annotate(str(int(value)), (i, value), textcoords="offset points",
                    xytext=(0, 10), ha="center", fontsize=9, color=INK_SOFT, fontweight="600")

    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_title(title, fontsize=13, fontweight="700", color=INK, loc="left", pad=14)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="y", alpha=0.25, linewidth=0.8)
    ax.tick_params(length=0)

    return fig


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-brand"><div class="icon">📊</div>'
        '<div class="txt">PIM Dashboard</div></div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🏫 Schools", "🧑‍🏫 Teachers", "✅ Visits", "📐 Standards", "📄 Reports"],
        label_visibility="collapsed"
    )
    page = page.split(" ", 1)[1]  # strip emoji for logic below

    st.markdown("---")

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()


# ============================================================
# DATA UPLOAD
# ============================================================

section_header("📂 Data Upload", "Upload your Excel file and select the worksheet to analyze.")

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

selected_sheet = st.selectbox("Select Worksheet", sheet_names)


# ============================================================
# LOAD SHEET
# ============================================================

try:
    df = pd.read_excel(uploaded_file, sheet_name=selected_sheet, skiprows=17, header=None)
except Exception as e:
    st.error("Unable to load the selected worksheet.")
    st.code(str(e))
    st.stop()


# ============================================================
# CHECK DATA
# ============================================================

if len(df) < 2:
    st.error("The selected worksheet does not contain enough rows to create the required headers.")
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
        except Exception:
            return str(col)
    return str(col)

df.columns = [change_date_format(col) for col in df.columns]
df.columns = [str(col).strip() for col in df.columns]


# ============================================================
# CLEAN DATA
# ============================================================

df = df.dropna(axis=1, how="all")

if "School Name" in df.columns:
    df = df.dropna(subset=["School Name"])

if "S/N" in df.columns:
    df = df.drop(columns=["S/N"])


# ============================================================
# REQUIRED COLUMNS
# ============================================================

required_columns = ["RtR Staff Name", "School Name", "Teacher Name", "Grade"]
missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error("The following required columns are missing:")
    for col in missing_columns:
        st.write(f"- {col}")
    st.stop()


# ============================================================
# IDENTIFY IMPORTANT COLUMNS
# ============================================================

minimum_standard_cols = [c for c in df.columns if c.startswith("Meeting Minimum Standards By Grade?")]

priority_cols = [c for c in df.columns if c.startswith("Teacher's Priority Area")]
priority_cols += [c for c in df.columns if c.startswith("Teacher’s Priority Area")]
priority_cols = list(dict.fromkeys(priority_cols))

total_visit_cols = [c for c in df.columns if c.startswith("Total Number of Visits Per Month")]


# ============================================================
# CONVERT MINIMUM STANDARD
# ============================================================

minimum_standard_mapping = {"No": 0, "Yes": 1}
for col in minimum_standard_cols:
    df[col] = df[col].astype("string").str.strip().map(minimum_standard_mapping)


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
    df[col] = df[col].astype("string").str.strip().map(priority_mapping)


# ============================================================
# CONVERT VISITS TO NUMERIC
# ============================================================

for col in total_visit_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)


# ============================================================
# CONVERT GRADE
# ============================================================

df["Grade"] = pd.to_numeric(df["Grade"], errors="coerce")


# ============================================================
# DATA INFORMATION
# ============================================================

st.success(f"Loaded sheet: **{selected_sheet}**")

with st.expander("📋 Data Preview"):
    st.write(f"Rows: {len(df):,}")
    st.write(f"Columns: {len(df.columns):,}")
    st.dataframe(df.head(10), use_container_width=True, hide_index=True)


# ============================================================
# CALCULATIONS  (unchanged logic)
# ============================================================

table_1 = pd.pivot_table(
    df, index="RtR Staff Name", values=["School Name", "Teacher Name"],
    aggfunc={"School Name": "nunique", "Teacher Name": "count"},
    margins=True, margins_name="Total"
)
school_teacher_summary = table_1.reset_index()

target_base = (
    df.groupby("RtR Staff Name").agg(School_Count=("School Name", "nunique")).reset_index()
)
target_base["Target_Visit"] = target_base["School_Count"] * 2 * 2 * len(total_visit_cols)
Target_Visit = target_base[["RtR Staff Name", "Target_Visit"]].copy()

if len(total_visit_cols) > 0:
    visited = df.groupby("RtR Staff Name")[total_visit_cols].sum().sum(axis=1).reset_index()
    visited.columns = ["RtR Staff Name", "Total_visited"]
else:
    visited = pd.DataFrame(columns=["RtR Staff Name", "Total_visited"])

if len(total_visit_cols) > 0:
    g1_data = df[df["Grade"] == 1]
    if len(g1_data) > 0:
        g1 = g1_data.groupby("RtR Staff Name")[total_visit_cols].sum().sum(axis=1).reset_index()
        g1.columns = ["RtR Staff Name", "Visit Grade_1"]
    else:
        g1 = pd.DataFrame(columns=["RtR Staff Name", "Visit Grade_1"])
else:
    g1 = pd.DataFrame(columns=["RtR Staff Name", "Visit Grade_1"])

if len(total_visit_cols) > 0:
    g2_data = df[df["Grade"] == 2]
    if len(g2_data) > 0:
        g2 = g2_data.groupby("RtR Staff Name")[total_visit_cols].sum().sum(axis=1).reset_index()
        g2.columns = ["RtR Staff Name", "Visit Grade_2"]
    else:
        g2 = pd.DataFrame(columns=["RtR Staff Name", "Visit Grade_2"])
else:
    g2 = pd.DataFrame(columns=["RtR Staff Name", "Visit Grade_2"])

visit_grade = g1.merge(g2, on="RtR Staff Name", how="outer")

diff = Target_Visit.merge(visited, on="RtR Staff Name", how="left")
diff["Total_visited"] = diff["Total_visited"].fillna(0)
diff["Gap of Visit"] = diff["Target_Visit"] - diff["Total_visited"]

Final_Total_Visited = diff.merge(visit_grade, on="RtR Staff Name", how="left").fillna(0)

if len(total_visit_cols) > 0:
    monthly_visit = df[total_visit_cols].sum().reset_index()
    monthly_visit.columns = ["Month", "Total_Visit"]
    monthly_visit["Month"] = monthly_visit["Month"].str.extract(r"_([A-Za-z]+)$")[0]
else:
    monthly_visit = pd.DataFrame(columns=["Month", "Total_Visit"])

if len(minimum_standard_cols) > 0:
    g1_std_data = df[df["Grade"] == 1]
    if len(g1_std_data) > 0:
        min_std_G1 = g1_std_data.groupby("RtR Staff Name")[minimum_standard_cols].sum().sum(axis=1).reset_index(name="Total Standard Meet_Grade-1")
    else:
        min_std_G1 = pd.DataFrame(columns=["RtR Staff Name", "Total Standard Meet_Grade-1"])
else:
    min_std_G1 = pd.DataFrame(columns=["RtR Staff Name", "Total Standard Meet_Grade-1"])

if len(minimum_standard_cols) > 0:
    g2_std_data = df[df["Grade"] == 2]
    if len(g2_std_data) > 0:
        min_std_G2 = g2_std_data.groupby("RtR Staff Name")[minimum_standard_cols].sum().sum(axis=1).reset_index(name="Total Standard Meet_Grade-2")
    else:
        min_std_G2 = pd.DataFrame(columns=["RtR Staff Name", "Total Standard Meet_Grade-2"])
else:
    min_std_G2 = pd.DataFrame(columns=["RtR Staff Name", "Total Standard Meet_Grade-2"])

min_std = min_std_G1.merge(min_std_G2, on="RtR Staff Name", how="outer").fillna(0)

if "Total Standard Meet_Grade-1" not in min_std.columns:
    min_std["Total Standard Meet_Grade-1"] = 0
if "Total Standard Meet_Grade-2" not in min_std.columns:
    min_std["Total Standard Meet_Grade-2"] = 0

min_std["Total Standard Meet"] = (
    min_std["Total Standard Meet_Grade-1"] + min_std["Total Standard Meet_Grade-2"]
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "Home":

    section_header("Dashboard Overview", "Monitor classroom observation performance and visits.")

    total_schools = df["School Name"].nunique()
    total_teachers = df["Teacher Name"].nunique()

    total_visits = int(df[total_visit_cols].sum().sum()) if len(total_visit_cols) > 0 else 0

    if len(minimum_standard_cols) > 0:
        total_standard = int(df[minimum_standard_cols].sum().sum())
        total_possible_standard = int(df[minimum_standard_cols].notna().sum().sum())
        standard_percentage = (total_standard / total_possible_standard * 100) if total_possible_standard > 0 else 0
    else:
        standard_percentage = 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Schools", f"{total_schools:,}")
    with col2:
        st.metric("Total Teachers", f"{total_teachers:,}")
    with col3:
        st.metric("Total Visits", f"{total_visits:,}")
    with col4:
        st.metric("Standards Met", f"{standard_percentage:.1f}%")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.subheader("Monthly Total Visits")

    if len(monthly_visit) > 0:
        fig = styled_line_chart(
            monthly_visit["Month"], monthly_visit["Total_Visit"],
            "Month", "Number of Visits", "Monthly Total Visits"
        )
        st.pyplot(fig, use_container_width=True)
        plt.close(fig)
    else:
        st.info("No monthly visit data available.")


# ============================================================
# SCHOOLS
# ============================================================

elif page == "Schools":

    section_header("School Summary", "Summary of schools and teachers by RtR staff.")

    school_table = (
        df.groupby("RtR Staff Name")
        .agg(Schools=("School Name", "nunique"), Teachers=("Teacher Name", "nunique"))
        .reset_index()
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Total Schools", f"{df['School Name'].nunique():,}")
    with c2:
        st.metric("Total Teachers", f"{df['Teacher Name'].nunique():,}")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    st.subheader("Staff-wise School Summary")
    st.dataframe(school_table, use_container_width=True, hide_index=True)

    st.subheader("School and Teacher Summary")
    st.dataframe(school_teacher_summary, use_container_width=True, hide_index=True)


# ============================================================
# TEACHERS
# ============================================================

elif page == "Teachers":

    section_header("Teacher Summary", "Teacher distribution by RtR staff and school.")

    teacher_table = (
        df.groupby(["RtR Staff Name", "School Name"])
        .agg(Teachers=("Teacher Name", "nunique"))
        .reset_index()
    )

    c1, c2 = st.columns(2)
    with c1:
        st.metric("Unique Teachers", f"{df['Teacher Name'].nunique():,}")
    with c2:
        st.metric("Schools", f"{df['School Name'].nunique():,}")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.dataframe(teacher_table, use_container_width=True, hide_index=True)


# ============================================================
# VISITS
# ============================================================

elif page == "Visits":

    section_header("Visit Monitoring", "Compare target visits with actual visits.")

    total_target = int(Final_Total_Visited["Target_Visit"].sum())
    total_actual = int(Final_Total_Visited["Total_visited"].sum())
    total_gap = total_target - total_actual

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Target Visits", f"{total_target:,}")
    with c2:
        st.metric("Actual Visits", f"{total_actual:,}")
    with c3:
        st.metric("Visit Gap", f"{total_gap:,}", delta=None)

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.subheader("Staff-wise Visit Performance")

    display_visit_table = Final_Total_Visited.copy()
    for col in ["Target_Visit", "Total_visited", "Gap of Visit", "Visit Grade_1", "Visit Grade_2"]:
        if col in display_visit_table.columns:
            display_visit_table[col] = pd.to_numeric(display_visit_table[col], errors="coerce").fillna(0).astype(int)

    st.dataframe(display_visit_table, use_container_width=True, hide_index=True)


# ============================================================
# STANDARDS
# ============================================================

elif page == "Standards":

    section_header("Minimum Standards", "Monitor minimum standard achievement by grade.")

    total_g1 = int(min_std["Total Standard Meet_Grade-1"].sum())
    total_g2 = int(min_std["Total Standard Meet_Grade-2"].sum())
    total_standard_met = total_g1 + total_g2

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Grade 1 Standards", f"{total_g1:,}")
    with c2:
        st.metric("Grade 2 Standards", f"{total_g2:,}")
    with c3:
        st.metric("Total Standards Met", f"{total_standard_met:,}")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.subheader("Staff-wise Minimum Standards")

    display_standard_table = min_std.copy()
    for col in display_standard_table.columns:
        if col != "RtR Staff Name":
            display_standard_table[col] = display_standard_table[col].astype(int)

    st.dataframe(display_standard_table, use_container_width=True, hide_index=True)


# ============================================================
# REPORTS
# ============================================================

elif page == "Reports":

    section_header("Reports", "Filter and explore the classroom observation dataset.")

    col1, col2 = st.columns(2)
    with col1:
        staff_options = ["All"] + sorted(df["RtR Staff Name"].dropna().unique().tolist())
        selected_staff = st.selectbox("RtR Staff", staff_options)
    with col2:
        grade_values = sorted(df["Grade"].dropna().unique().tolist())
        grade_options = ["All"] + grade_values
        selected_grade = st.selectbox("Grade", grade_options)

    filtered_df = df.copy()
    if selected_staff != "All":
        filtered_df = filtered_df[filtered_df["RtR Staff Name"] == selected_staff]
    if selected_grade != "All":
        filtered_df = filtered_df[filtered_df["Grade"] == selected_grade]

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
    st.write(f"Showing **{len(filtered_df):,}** records")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)

    csv_data = filtered_df.to_csv(index=False)
    st.download_button(
        label="⬇️  Download Filtered Report",
        data=csv_data,
        file_name="PIM_Filtered_Report.csv",
        mime="text/csv",
        use_container_width=False
    )
