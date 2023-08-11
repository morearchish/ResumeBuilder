
import json
import streamlit as st
class Resume:
    def __init__(self):
        self.name = "Name"
        self.job_title = "Role/Major's"
        self.email = "Email"
        self.link = "www.example.com"
        self.phone = "Ph No"
        self.personal_profile = "A brief personal profile goes here."
        self.address = "City/State"
        self.key_skills = {
            "Web Design": "Assertively exploit wireless initiatives rather than synergistic core competencies.",
            "Interface Design": "Credibly streamline mission-critical value with multifunctional functionalities.",
            "Project Direction": "Proven ability to lead and manage a wide variety of design and development projects in team and independent situations."
        }
        self.technical_skills = ["HTML", "CSS", "JS", "PYTHON", "ML", "AI","RUBY","GOLANG","AWS","Backend","Fontend","Webdev","DATA","EDA","API"]
        self.work_experience = list()
        self.education = list()

    def update_name(self, name):
        self.name = name

    def update_job_title(self, job_title):
        self.job_title = job_title

    def update_email(self, email):
        self.email = email

    def update_link(self, link):
        self.link = link

    def update_phone(self, phone):
        self.phone = phone

    def update_personal_profile(self, personal_profile):
        self.personal_profile = personal_profile

    def update_address(self, address):
        self.address = address

    def update_key_skills(self, key_skills):
        self.key_skills = key_skills

    def update_technical_skills(self, technical_skills):
        self.technical_skills = technical_skills

    def update_work_experience(self, work_experience):
        self.work_experience = work_experience

    def update_education(self, education):
        self.education = education


    def add_education(self, school, qualification, description, date):
        
        self.education.append({
            "school": school,
            "qualification": qualification,
            "description": description,
            "date": date,
        })  


    def display_resume(self):
        st.write("Name:", self.name)
        st.write("Job Title:", self.job_title)
        st.write("Email:", self.email)
        st.write("Link:", self.link)
        st.write("Phone:", self.phone)
        st.write("Personal Profile:", self.personal_profile)
        st.write("Address:", self.address)
        st.write("Key Skills:")
        for skill, description in self.key_skills.items():
            st.write(f"  {skill}: {description}")
        st.write("Technical Skills:", ", ".join(self.technical_skills))
        st.write("Work Experience:")
        # st.text_area("Resume",value=self.work_experience,height=1000)
        for exp in self.work_experience:
            # st.write("abcd")
            st.write(f"  Title: {exp['title']}")
            st.write(f"  Position: {exp['position']}")
            st.write(f"  Duration: {exp['duration']}")
            st.write(f"  Description: {exp['description']}")
        st.write("Education:")
        for edu in self.education:
            st.write(f"  School: {edu['school']}")
            st.write(f"  Qualification: {edu['qualification']}")
            st.write(f"  Description: {edu['description']}")
            st.write(f"  Date: {edu['date']}")
resume = Resume()

# exp_forms=[]
def fill_form():
    st.title("Update Resume")

    resume = Resume()

    name = st.text_input("Name", resume.name)

    job_title = st.text_input("Job Title", resume.job_title)

    email = st.text_input("Email", resume.email)

    link = st.text_input("Link", resume.link)

    phone = st.text_input("Phone", resume.phone)

    personal_profile = st.text_area("Personal Profile", resume.personal_profile)

    address = st.text_input("Address", resume.address)

    st.subheader("Key Skills")
    key_skills = {}
    for i in range(3):
        skill_name = st.text_input(f"Skill {i+1} Name", list(resume.key_skills.keys())[i])
        skill_description = st.text_area(f"Skill {i+1} Description", list(resume.key_skills.values())[i])
        key_skills[skill_name] = skill_description

    # Update Technical Skills
    st.subheader("Technical Skills")
    technical_skills = st.multiselect("Technical Skills", resume.technical_skills)
    

    if 'exp_forms' not in st.session_state:
        st.session_state.exp_forms = []
    if 'edu_forms' not in st.session_state:
        st.session_state.edu_forms = []

    # update experience
    st.subheader("Work Experience")
    count_exp = st.slider('Number of Work Experiences', min_value=1, max_value=10, value=1, step=1)
    for i in range(count_exp):
        with st.form(f"work_exp_form_{i}"):
            title = st.text_input("Title")
            position = st.text_input("Position")
            duration = st.text_input("Duration")
            description = st.text_area("Description")
            but = st.form_submit_button(label=f"Update Experience {i+1}")

            if but:
                st.session_state.exp_forms.append({
                    "title": title,
                    "position": position,
                    "duration": duration,
                    "description": description,
                })

    # Update Education
    st.subheader("Education")
    count_edu = st.slider('Number of Education Entries', min_value=1, max_value=10, value=1, step=1)
    # edu_forms = []
    for i in range(count_edu):
        with st.form(f"education_form_{i}"):
            school = st.text_input("School")
            qualification = st.text_input("Qualification")
            description = st.text_area("Description")
            date = st.text_input("Date")
            but = st.form_submit_button(label=f"Update Education {i+1}")
            if but:
                st.session_state.edu_forms.append({
                    "school": school,
                    "qualification": qualification,
                    "description": description,
                    "date": date,
               })


    # Display the updated resume
    if st.button("Finalize Updates"):
       resume.update_name(name)
       resume.update_job_title(job_title)
       resume.update_email(email)
       resume.update_link(link)
       resume.update_phone(phone)
       resume.update_personal_profile(personal_profile)
       resume.update_address(address)
       resume.update_technical_skills(technical_skills)
       resume.update_key_skills(key_skills)
       resume.update_work_experience(st.session_state.exp_forms) 
       resume.update_education(st.session_state.edu_forms)
    #    st.subheader("Updated Resume")
    #    st.json(resume.__dict__)
       with open("result.json", "w") as json_file:
            json.dump(resume.__dict__, json_file, indent=4)
            

    #    resume.display_resume()
        

if __name__ == "__main__":
    fill_form()

