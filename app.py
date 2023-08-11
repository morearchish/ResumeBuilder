
import streamlit as st
from fillaform import *
from generate_resume import generate_resume1
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


def main():

    st.title("Resume Builder")

    st.write("\n")

    col1, col2 = st.columns([1, 3])

    with col1:
        st.write("How do you want to build your resume:")

    with col2:

        options = ["Select", "Fill a form", "From LinkedIn", "From a website", "From previous resume"]
        selected_option = st.selectbox("", options)

    if selected_option == "Fill a form":
        fill_form()
    # elif selected_option == "From LinkedIn":
    #     # LinkedinData()
        
    # elif selected_option == "From a website":
    #     # WebsiteData()
        
    # elif selected_option == "From previous resume":
    #     # ResumeData()
        

    st.write("\n")

    st.write("\nSelect a Template:")

    templates = [
        {"name": "Template 1", "image_url": "Images/1.jpg"},
        {"name": "Template 2", "image_url": "Images/2.jpg"},
        {"name": "Template 3", "image_url": "Images/3.jpg"},
        {"name": "Template 4", "image_url": "Images/4.jpg"},
    ]

    col1, col2 = st.columns(2)

    with col1:
        display_template(templates[0])

    with col2:
        display_template(templates[1])

    st.write("\n")

    with col1:
        display_template(templates[2])

    with col2:
        display_template(templates[3])

    st.write("\n")
    l = []
    for i in templates:
        l.append(i["name"])

    selected_option = st.selectbox("Select an option",l, index=0, key="sdchb")

    if st.button("Generate Resume"):

        select = selected_option.replace(" ","")
        
        pdf_data = generate_resume1(select)
        st.download_button("Download Resume PDF", data=open(pdf_data, 'rb').read(), file_name="resume.pdf")


        # Provide a download link for the generated PDF
        # pdf_bytes = BytesIO(pdf_data)
        # st.download_button("Download Resume PDF", data=pdf_bytes, file_name="resume.pdf", mime='application/pdf')
        # if pdf_file_path is not None:
        #     pdf_bytes = BytesIO(pdf_file)
        #     st.download_button("Download Resume PDF", data=pdf_bytes, file_name="resume.pdf", mime='application/pdf')        else:
        # st.text_area(pdf_file_path.read())
    st.write("\n")

def display_template(template):

    st.write(template["name"])
    st.image(template["image_url"],use_column_width=True)

if __name__ == "__main__":
    main()
