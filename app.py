
import streamlit as st
import openai

st.set_page_config(page_title="MyPaedsGPT", layout="centered")

# Load OpenAI API key from .streamlit/secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Clinical Q&A Assistant (Top Section) ---
st.title("Clinical Q&A Assistant")

region = st.selectbox("Choose your guideline region", ["UK", "WHO", "Nigeria", "US", "Australia"])
question = st.text_input("Ask your clinical question:")

def get_clinical_answer(region, question):
    try:
        system_prompt = f"You are a senior paediatric consultant using {region} guidelines. Provide a concise, evidence-based answer."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"

if st.button("Get Answer"):
    if question:
        with st.spinner("Fetching answer..."):
            answer = get_clinical_answer(region, question)
            if answer.startswith("Error:"):
                st.error(answer)
            else:
                st.success("Answer ready:")
                st.write(answer)
    else:
        st.warning("Please enter a question.")

# --- Research & Global Resources Placeholder ---
st.markdown("---")
st.subheader("Research & Global Resources")
st.info("This section will provide access to indexed guidelines, reference materials, topic cards, and search tools.")

# --- Clinic Letter Generator (Third Section) ---
st.markdown("---")
st.header("Clinic Letter Generator")

clinic_type = st.selectbox("Select Clinic Type", [
    "General Paediatrics",
    "Paediatric Cardiology",
    "Paediatric Electrophysiology"
])

hospital_number = st.text_input("Enter Hospital Number")
patient_name = st.text_input("Enter Patient Name")
dob = st.date_input("Enter Date of Birth")
date_seen = st.date_input("Enter Date Seen")
clinical_summary = st.text_area("Clinical Summary / Findings")
impression = st.text_area("Impression / Working Diagnosis")
plan = st.text_area("Management Plan / Follow-up Actions")

sign_off = st.selectbox("Select Professional Role", [
    "Specialty Doctor in Paediatrics",
    "Senior Clinical Fellow, Paediatric Cardiology",
    "ST4 Paediatric Cardiology Trainee",
    "ST5 Paediatric Cardiology Trainee",
    "ST6 Paediatric Cardiology Trainee",
    "ST7 Paediatric Cardiology Trainee",
    "ST8 Paediatric Cardiology Trainee",
    "Locum Paediatric Consultant",
    "Locum Paediatric Consultant with Special Interest in Paediatric Cardiology",
    "Consultant Paediatrician with Special Interest in Paediatric Cardiology",
    "Consultant Paediatric Cardiologist"
])

if st.button("Generate Letter"):
    if all([patient_name, clinical_summary, impression, plan]):
        st.success("Clinic Letter Preview")
        st.markdown("**Patient Name:**")
        st.write(patient_name)
        st.markdown("**Hospital Number:**")
        st.write(hospital_number)
        st.markdown("**Date of Birth:**")
        st.write(dob.strftime('%Y-%m-%d'))
        st.markdown("**Date Seen:**")
        st.write(date_seen.strftime('%Y-%m-%d'))
        st.markdown("---")
        st.markdown("**Clinic Type:**")
        st.write(clinic_type)
        st.markdown("**Clinical Summary:**")
        st.write(clinical_summary)
        st.markdown("**Impression:**")
        st.write(impression)
        st.markdown("**Plan:**")
        st.write(plan)
        st.markdown("---")
        st.markdown("**Yours sincerely,**")
        st.write(sign_off)
    else:
        st.warning("Please fill in all required fields.")
