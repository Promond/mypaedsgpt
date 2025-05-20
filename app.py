
import streamlit as st
import datetime

st.set_page_config(page_title="MyPaedsGPT", layout="wide")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("MyPaedsGPT Navigation")
tabs = [
    "📄 Clinic Letter Generator",
    "🩺 Clinical Q&A Assistant",
    "📚 Research & Global Resources",
    "🧠 UpToDate Assistant",
    "🛡️ Safeguarding Tools",
    "🧭 Algorithm Navigator",
    "✍️ Smart Writing & Academic Tools",
    "📊 Presentations & Reviews"
]
selected_tab = st.sidebar.radio("Choose a tool:", tabs)

# -------------------------------
# Tab: Clinic Letter Generator
# -------------------------------
if selected_tab == tabs[0]:
    st.title("📄 Clinic Letter Generator")
    st.text_input("Patient Name")
    st.date_input("Date of Visit", datetime.date.today())
    st.selectbox("Clinic Type", ["General Paediatrics", "Paediatric Cardiology", "Paediatric Electrophysiology"])
    st.selectbox("Professional Sign-Off", [
        "Dr Promise Monday, Specialty Doctor in Paediatrics",
        "Dr Promise Monday, Senior Clinical Fellow, Paediatric Cardiology",
        "Dr Promise Monday, ST4 Paediatric Cardiology Trainee",
        "Dr Promise Monday, ST5 Paediatric Cardiology Trainee",
        "Dr Promise Monday, ST6 Paediatric Cardiology Trainee",
        "Dr Promise Monday, ST7 Paediatric Cardiology Trainee",
        "Dr Promise Monday, ST8 Paediatric Cardiology Trainee",
        "Dr Promise Monday, Locum Paediatric Consultant",
        "Dr Promise Monday, Locum Paediatric Consultant with Special Interest in Paediatric Cardiology",
        "Dr Promise Monday, Consultant Paediatrician with Special Interest in Paediatric Cardiology",
        "Dr Promise Monday, Consultant Paediatric Cardiologist"
    ])
    st.text_area("Clinical Summary / Dictation", height=200)
    st.button("Generate Letter")

# -------------------------------
# Tab: Clinical Q&A Assistant
# -------------------------------
elif selected_tab == tabs[1]:
    st.title("🩺 Clinical Q&A Assistant")
    st.selectbox("Region", ["UK", "WHO", "Nigeria", "USA", "Australia"])
    st.text_area("Ask your question:")
    st.button("Get Answer")

# -------------------------------
# Tab: Research & Global Resources
# -------------------------------
elif selected_tab == tabs[2]:
    st.title("📚 Research & Global Resources")
    st.text_input("Search topic cards or enter a keyword:")
    st.button("Search")

# -------------------------------
# Tab: UpToDate Assistant
# -------------------------------
elif selected_tab == tabs[3]:
    st.title("🧠 UpToDate Assistant")
    st.text_input("Search UpToDate topic:")
    st.text_area("Paste content for summarisation:")
    st.button("Summarise")

# -------------------------------
# Tab: Safeguarding Tools
# -------------------------------
elif selected_tab == tabs[4]:
    st.title("🛡️ Safeguarding Tools")
    st.selectbox("Report Type", ["Child Protection Medical", "Strategy Meeting Summary", "Formal CP Report"])
    st.text_area("Case Details / Clinical History", height=150)
    st.text_area("Examination Findings", height=150)
    st.button("Generate Safeguarding Report")

# -------------------------------
# Tab: Algorithm Navigator
# -------------------------------
elif selected_tab == tabs[5]:
    st.title("🧭 Algorithm Navigator")
    st.selectbox("Region", ["UK", "WHO", "Nigeria", "USA", "Australia"])
    st.text_input("Condition or Symptom:")
    st.button("Generate Algorithm")

# -------------------------------
# Tab: Smart Writing & Academic Tools
# -------------------------------
elif selected_tab == tabs[6]:
    st.title("✍️ Smart Writing & Academic Tools")
    st.selectbox("Select Tool", [
        "Clinical Guideline Generator", "Research Proposal Builder", "Audit Report Writer",
        "Patient Leaflet Creator", "Application Letter Generator", "Journal Critique Generator"
    ])
    st.text_area("Enter prompt or description:")
    st.file_uploader("Upload Data (if applicable)", type=['csv', 'xlsx', 'sav'])
    st.selectbox("Reference Style", ["Harvard", "Vancouver", "APA", "MLA"])
    st.button("Generate Document")

# -------------------------------
# Tab: Presentations & Reviews
# -------------------------------
elif selected_tab == tabs[7]:
    st.title("📊 Presentations & Reviews")
    st.selectbox("Presentation Type", [
        "Clinical Case Presentation", "Journal Club Presentation", "Audit Slide Deck",
        "Morbidity & Mortality Review", "Child Death Review"
    ])
    st.text_area("Describe your case/topic:")
    st.button("Generate Presentation")
