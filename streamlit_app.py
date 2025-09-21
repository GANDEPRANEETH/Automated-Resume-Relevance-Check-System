import streamlit as st
import requests

st.title("Resume Relevance Checker")

job_title = st.text_input("Job Title")
job_description = st.text_area("Job Description")
job_skills = st.text_input("Job Skills (comma separated)")

resume_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=['pdf', 'docx'])

if st.button("Evaluate"):
    if not all([job_title, job_description, job_skills, resume_file]):
        st.warning("Please fill all fields and upload a resume.")
    else:
        files = {
            "resume": (resume_file.name, resume_file.getvalue(), resume_file.type)
        }
        data = {
            "title": job_title,
            "skills": job_skills,
            "description": job_description
        }

        response = requests.post("http://localhost:8000/evaluate/", data=data, files=files)

        if response.ok:
            result = response.json()
            st.success("Evaluation complete!")
            st.write(f"Score: {result.get('score')}")
            st.write(f"Verdict: {result.get('verdict')}")
            st.write(f"Feedback: {result.get('feedback')}")
        else:
            st.error("Failed to evaluate resume.")
