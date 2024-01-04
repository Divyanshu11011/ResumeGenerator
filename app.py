import streamlit as st
import openai
from fpdf import FPDF

# Streamlit app
def main():
    st.title("Resume Generator")

    # User inputs
    openai_api_key = st.sidebar.text_input('OpenAI API Key')
    name = st.text_input("Enter your name")
    contact_info = st.text_input("Enter your contact info")
    skills = st.text_input("Enter your skills (comma-separated)")
    projects = st.text_input("Enter your projects (comma-separated)")
    achievements = st.text_input("Enter your achievements (comma-separated)")
    work_experience = st.text_input("Enter your work experience (comma-separated)")

    if st.button("Generate Resume"):
        # Set up OpenAI API
        openai.api_key = openai_api_key

        # Prepare prompt for OpenAI API
        prompt = f"Generate a professional resume for a person named {name} with contact info {contact_info}, skills in {skills}, projects {projects}, achievements {achievements}, and work experience in {work_experience}."

        # Call OpenAI API
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=500)

        # Display result
        resume_text = response.choices[0].text.strip()
        st.text_area("Your Resume:", value=resume_text, height=200, max_chars=None)

        # Save as text file
        with open('resume.txt', 'w', encoding='utf-8') as f:
            f.write(resume_text)

        # Convert text file to PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        with open('resume.txt', 'r', encoding='utf-8') as f:
            for line in f:
                pdf.cell(200, 10, txt = line, ln = True)
        pdf.output("resume.pdf")

        st.success('Resume has been saved as a PDF file named "resume.pdf" in the current directory.')

if __name__ == '__main__':
    main()
