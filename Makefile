all : switches_in_the_brain.pdf

switches_in_the_brain.pdf : ./switches_in_the_brain.tex 
	pdflatex --shell-escape $<
