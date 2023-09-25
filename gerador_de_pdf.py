# Install de biblioteca externa (fdpf) com pip install
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World')
pdf.output('Arquivos/exemplo.pdf')