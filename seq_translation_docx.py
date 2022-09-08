#This code was modified based on the code provided by Vincent Vanburen in MPHY625 Spring 2020
import glob

import re

import docx
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Inches, Cm

directory = "/Users/YYY/Desktop/Python/Seq/"

files = sorted(glob.glob(directory+"*.seq")) 
#strings in python may be concatenated with the plus sign. Adding *.seq will just retrieve filenames that end with .seq

#tab = open("seq_translation.txt","w")

tab = docx.Document()

sections = tab.sections
for section in sections:
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)

gencode = {
      'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
      'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
      'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
      'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
      'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
      'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
      'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
      'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
      'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
      'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
      'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
      'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
      'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
      'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}

basepairs = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}


def translate_frameshifted( sequence ):
      translate = ''.join([gencode.get(sequence[3*i:3*i+3],'X') for i in range(len(sequence)//3)])
      return translate

def reverse_complement( sequence ):
      reversed_sequence = (sequence[::-1])
      rc = ''.join([basepairs.get(reversed_sequence[i], 'X') for i in range(len(sequence))])
      return rc

for record in files:

	f = open(record, "r")

	header = ""

	sequence = ""

	line = f.readline()						

	while (line):

		line = line.strip("\n")


		if re.match(r'>.*', line):

			header = re.sub(r'>','', line)

		else:

			sequence = sequence + line


		line = f.readline()

	tab.add_paragraph (">"+header+"\n"+sequence+"\n"+"\n"
			"+1"+"\n"+translate_frameshifted(sequence[0:])+"\n"+   
			"+2"+"\n"+translate_frameshifted(sequence[1:])+"\n"+   
			"+3"+"\n"+translate_frameshifted(sequence[2:])+"\n"+   
			"-1"+"\n"+translate_frameshifted(reverse_complement(sequence))+"\n"+ 
			"-2"+"\n"+translate_frameshifted(reverse_complement(sequence[:len(sequence)-1]))+"\n"+  
			"-3"+"\n"+translate_frameshifted(reverse_complement(sequence[:len(sequence)-2]))+"\n"+"\n"
			)
	style = tab.styles['Normal']
	font = style.font
	font.name = 'Courier'
	font.size = Pt(10)
		
	f.close() 

tab.save("seq_translated.docx")

"""
when encounter:
from exceptions import PendingDeprecationWarning
ModuleNotFoundError: No module named 'exceptions'

run:
pip install python-docx
"""

