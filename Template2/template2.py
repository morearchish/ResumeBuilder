def replace_placeholders(template, data):
    template = template.replace("<placeholder_name>", data["name"])
    template = template.replace("<placeholder_job_title>", data["job_title"])
    template = template.replace("<placeholder_email>", data["email"])
    template = template.replace("<placeholder_website>", data["website"])
    template = template.replace("<placeholder_phone>", data["phone"])
    template = template.replace("<placeholder_personal_profile>", data["personal_profile"])

    # Handle multiple job experiences
    work_experience_html = ""
    for job in data["work_experience"]:
        job_html = f"""
            <article>
                <h2>{job['job_title']}</h2>
                <p class="subDetails">{job['duration']}</p>
                <p>{job['description']}</p>
            </article>
        """
        work_experience_html += job_html

    template = template.replace("<placeholder_work_experience>", work_experience_html)

    # Replace key skills placeholders
    key_skills_html = ""
    for skill in data["key_skills"]:
        skill_html = f"<li>{skill}</li>"
        key_skills_html += skill_html

    template = template.replace("<placeholder_key_skills>", key_skills_html)

    # Replace education placeholders
    education_html = ""
    for edu in data["education"]:
        edu_html = f"""
            <article>
                <h2>{edu['school']}</h2>
                <p class="subDetails">{edu['qualification']}</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ultricies massa et erat luctus
                    hendrerit. Curabitur non consequat enim.</p>
            </article>
        """
        education_html += edu_html

    template = template.replace("<placeholder_education>", education_html)

    return template


if __name__ == "__main__":
    # Sample data for one candidate with multiple job experiences
    candidate_data = {
        "name": "John Doe",
        "job_title": "Software Engineer",
        "email": "john.doe@example.com",
        "website": "www.johndoe.com",
        "phone": "1234567890",
        "personal_profile": "A brief personal profile goes here.",
        "work_experience": [
            {
                "job_title": "Software Engineer",
                "duration": "Jan 2018 - Present",
                "description": "Worked on various projects.",
            },
            {
                "job_title": "Intern",
                "duration": "Jun 2017 - Dec 2017",
                "description": "Assisted senior engineers.",
            },
        ],
        "key_skills": ["Python", "JavaScript", "HTML/CSS", "Database Management"],
        "education": [
            {"school": "University of XYZ", "qualification": "Bachelor of Science in Computer Science"},
            {"school": "ABC College", "qualification": "High School Diploma"},
        ],
    }

    # Read the HTML template
    with open("./template2/index.html", "r") as file:
        template = file.read()

    # Replace all placeholders with the candidate's data
    modified_template = replace_placeholders(template, candidate_data)

    # Save the modified template to a new file
    with open("./template2/john_doe_resume.html", "w") as output_file:
        output_file.write(modified_template)
