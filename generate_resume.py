from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from jinja2 import Template
import json
import pdfkit

def read_template(template_filename):
    with open(template_filename, "r", encoding="utf8") as file:
        return file.read()

def replace_placeholders(template_content, data):
    template = Template(template_content)
    return template.render(data)
def convert_html_to_pdf(html_file, pdf_file):
    try:

        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
        options = {
            'page-size': 'A4',
            'encoding': 'UTF-8',
        }

        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file, configuration=config, options=options)
        # pdfkit.from_file(html_file, pdf_file, configuration=config, options=options)
        #  pdfkit.from_file(html_file, pdf_file, options=options)
        # pdfkit.from_file(html_file, False, options=options)
    

        # return pdf_bytes
        print(f"PDF file '{pdf_file}' created successfully.")

    except Exception as e:
        return 
        print(f"Error converting HTML to PDF: {e}")

def generate_resume1(template_filename2):
    template_filename_2 = "./"+template_filename2+"/index.html"
    template_content_2 = read_template(template_filename_2)
    
    with open("./result.json","r") as output:
        candidate_data_2 = json.loads(output.read())
    modified_template_2 = replace_placeholders(template_content_2, candidate_data_2)

    with open("./"+template_filename2+"/"+candidate_data_2["name"]+".html", "w", encoding="utf-8") as output_file:
        output_file.write(modified_template_2)
    # Example usage
    html_file_path = "./"+template_filename2+"/"+candidate_data_2["name"]+".html"
    pdf_file_path = "./"+candidate_data_2["name"]+".pdf" 
    convert_html_to_pdf(html_file_path,pdf_file_path)  
    return pdf_file_path



# def download_pdf(selected_template):
#     # Example usage
#     html_file_path = "path/to/your/input.html"
#     pdf_file_path = "path/to/your/output.pdf"
#     c = canvas.Canvas("generated_resume.pdf", pagesize=letter)
#     c.drawString(72, 720, f"Resume generated based on {selected_template} template...")
#     c.save()
# generate_resume("template4")

