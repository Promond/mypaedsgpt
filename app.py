import streamlit as st
import openai

st.set_page_config(page_title="MyPaedsGPT", layout="wide")

# Load your OpenAI API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("MyPaedsGPT – Paediatric & Cardiology Assistant")

tab1, tab2 = st.tabs(["📝 Clinic Letter Generator", "🔍 Clinical Q&A"])

# ---- Tab 1: Clinic Letter Generator ----
with tab1:
    st.subheader("Generate GP Letter")

    clinic_type = st.selectbox("Clinic Type", [
        "General Paediatrics",
        "Paediatric Cardiology",
        "Electrophysiology / Pacemaker / ICD"
    ])

    sign_off = st.selectbox("Sign-Off", [
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

    notes = st.text_area("Paste or dictate your consultation notes:", height=250)

    if st.button("Generate Letter"):
        letter = f"""
To: Dr [GP Name]
CC: [Caregiver Name and Address]
Re: [Patient Name], DOB: [Date], NHS No: [NHS Number]
Date of Consultation: [Today’s Date]
Location: {clinic_type} Clinic

Reason for Review:
[Insert summary]

History:
{notes}

Examination Findings:
[Insert findings]

Impression / Diagnosis:
[Insert impression]

Plan:
[Insert plan]

Follow-Up:
[Insert follow-up]

Yours sincerely,

{sign_off}
"""
        st.text_area("Clinic Letter", letter, height=400)
        st.success("Letter generated! You can now copy or save it.")

# ---- Tab 2: Clinical Q&A ----
with tab2:
    st.subheader("Ask Clinical Questions by Region")

    region = st.selectbox("Choose Guideline Source", [
        "UK (NICE / RCPCH)",
        "USA (AAP / NIH / UpToDate)",
        "Australia (RCH Melbourne)",
        "WHO (IMCI / Global)",
        "Nigeria (NPMC / MoH)"
    ])

    question = st.text_area("What would you like to know?", height=150)

    if st.button("Ask MyPaedsGPT"):
        with st.spinner("Fetching response..."):
            prompt = f"You are a paediatric assistant giving an evidence-based answer from {region}. Keep it brief but clear:\n\n{question}"
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            answer = response['choices'][0]['message']['content']
            st.markdown(f"**Answer from {region}:**")
            st.write(answer)
