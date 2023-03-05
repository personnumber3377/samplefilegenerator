import random
from fpdf import FPDF

class PDF(FPDF):
	#self.pdf_w=210
	#self.pdf_h=297
	def lines(self):
		self.set_line_width(1.0)
		#random.randrange(0,self.pdf_w)
		pdf_w=210
		pdf_h=297

		#random.randrange(0,self.pdf_h)
		self.line(random.randrange(0,pdf_w),random.randrange(0,pdf_h),random.randrange(0,pdf_w),random.randrange(0,pdf_h))
	pass # nothing happens when it is executed.

def generate_pdf():







	#pdf = PDF()

	pdf=PDF(orientation='L')



	pdf.add_page()
	max_lines = 100
	min_lines = 0
	for _ in range(random.randrange(min_lines,max_lines)):

		pdf.lines()


	result = pdf.output(dest='S').encode('latin-1')

	return result

if __name__=="__main__":

	print(generate_pdf())

