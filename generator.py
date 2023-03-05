

import sys
import getopt
from random_html import *
import random
from random_pdf import *
import string
from imageio import *
import numpy
from PIL import Image
import io
import os

def generate_png(filename, extension):

	if random.randrange(0,5) == 1:
		filename+= "."+str(extension)

	thingoof = "donottouch.png"
	imarray = numpy.random.rand(100,100,3) * 255
	im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
	im.save(thingoof)
	os.system("cp ./donottouch.png "+str(filename))

	return 0


def write_file(filename, content, extension):
	if content == None or content == "":
		print("Invalid content")
		assert 1==2
	if random.randrange(0,5) == 1:
		if extension == "" or extension == None:
			fh = open(filename, "wb")
		else:

			fh = open(filename+"."+str(extension), "wb+")
	else:
		fh = open(filename, "wb")
	if isinstance(content, bytes):

		fh.write(content)
	elif isinstance(content, str):
		fh.write(str.encode(content))
	else:
		print("Invalid type : "+str(type(content)))
		print("Content: "+str(content))
		print("str(type(content)) == "+str(type(content)))
		print("type(content) == \"str\"  : "+str(type(content) == "str"))
		exit(1)
	fh.close()
	return


def write_file_always_ext(filename, content, extension):
	
	fh = open(filename+"."+str(extension), "wb+")
	
	fh.write(bytes(content, encoding='utf-8'))
	fh.close()
	return


def random_binary(nbytes):
	output_string = ""
	for _ in range(nbytes):
		output_string+=chr(random.randrange(0,256))
	return output_string


def random_string(length):
	return ''.join([random.choice(list(string.ascii_lowercase)) for _ in range(length)])


def image_to_byte_array(image:Image):
	imgByteArr = io.BytesIO()
	image.save(imgByteArr, format=image.format)
	imgByteArr = imgByteArr.getvalue()
	return imgByteArr

def generate_random_file(filename, ftype):
	if ftype == "html":
		result = Output(RandomHtml())
		write_file(filename, result, "html")
		return 0

	if ftype == "binary":
		result = random_binary(500)
		write_file(filename, result, "")
		return 0

	if ftype == "pdf":
		result = generate_pdf()
		write_file(filename, result, "pdf")
		return 0

	if ftype == "text":
		length = random.randrange(1, 1000)
		result = random_string(length)
		print("Text result: "+str(result))
		write_file(filename, result, "txt")
		return 0
		#return result

	if ftype == "png":
		result = generate_png(filename, "png")
		#print("filename: "+str(filename))
		#print(result)
		#print("result.format : "+str(result.format))
		#write_file(filename, image_to_byte_array(result), "png")
		return 0



	



	return 1

'''
def random_string(length):
	return ''.join([random.choice(list(string.ascii_lowercase)) for _ in range(length)])
'''


def get_random_string(min_len, max_len):
	return random_string(random.randrange(min_len, max_len))

def generate_files(number_of_files, output_directory, mime_types):

	for _ in range(number_of_files):
		cur_type = random.choice(mime_types)
		
		filename = output_directory+str(get_random_string(1,3))

		generate_random_file(filename, cur_type)





if __name__=="__main__":


	supported_mime_types = ["html", "binary", "pdf", "text", "png"]

	outdir = sys.argv[1]
	if outdir[-1] != "/":
		outdir += "/"
	num_files = 100
	generate_files(num_files, outdir, supported_mime_types)

	#print(generate_random_file("sampletext", "html"))
	#generate_random_file("./tests/oofthing", "png")


	#generate_random_file("./tests/oofthing2", "gif")
	# Handle command line arguments:





