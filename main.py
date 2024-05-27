from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

#generates master pages
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row['Topic'], align='C', ln=1)
    line_spacing = 10
    y_value = 29
    for line in range(26):
        pdf.line(x1=10, y1=y_value, x2=200, y2=y_value)
        y_value = y_value + line_spacing
# sets footer for master page
    pdf.ln(250)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

# set up extra pages
    for i in range(row['Pages'] - 1):
        pdf.add_page()
        y_value_extra_page = 10
        for line in range(28):
            pdf.line(x1=10, y1=y_value_extra_page, x2=200, y2=y_value_extra_page)
            y_value_extra_page = y_value_extra_page + line_spacing
# sets footer for extra pages
        pdf.ln(274)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output('output.pdf')