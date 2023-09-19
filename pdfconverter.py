# importing fpdf
from fpdf import FPDF # pip install fpdf
# importing os
import os

# creating a FPDF object
pdf = FPDF()
# setting auto pages to break after a image
pdf.set_auto_page_break(0)

# listing all the files in a single array
img_list = [x for x in os.listdir('input_images')]

# looping and sorting the images
for img in sorted(img_list):
    # creating a page
    pdf.add_page()
    # fetching the image
    image = "input_images/" + img
    # adding the image into the pdf object
    pdf.image(image)

# creating the pdf file in the output
pdf.output("document_converted.pdf", "F")
# printing in the console, all tasks completed
print("completed")
