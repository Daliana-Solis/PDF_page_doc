from fpdf import FPDF
import pandas as pd

#p = portrait, l = landscape
pdf = FPDF(orientation="P", unit="mm", format='A4')

df = pd.read_csv("topics.csv")


"""
.cell(width, height, txt, align, ln, border_size)
Recommended to make width = 0, height the same size as set font, 
ln = *breakline*, begins new cell where the width of the previous cell ends
txt = contains the value of the cell
align = left "L" or "R" right side 
"""

#iterate through CSV, create page for each topic
for index, row in df.iterrows():
    # add page and set font and font size
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)

    #set color on RGB
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'],align='L', ln=1)

    #add line (add x1, y1, x2,y2) start to end coordinates
    pdf.line(10, 21, 200, 21)








pdf.cell(w=0, h=12, txt='Hello', align='L', ln=1, border=1)


pdf.output("output.pdf")