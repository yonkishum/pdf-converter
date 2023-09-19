from fpdf import FPDF
import os

pdf = FPDF()
pdf.set_auto_page_break(0)

img_list = [x for x in os.listdir('input_images')]

for img in sorted(img_list):
    pdf.add_page()
    image = "input_images/" + img
    pdf.image(image)
    
pdf.output("document_converted.pdf", "F")
print("completed")