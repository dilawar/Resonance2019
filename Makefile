all : switches_in_the_brain.pdf

switches_in_the_brain.pdf : ./switches_in_the_brain.tex 
	pdflatex --shell-escape $<

zip :
	zip -r ResonanceSubmittion.zip *.pdf *.tex resonance.cls \
	    logo.eps dilawar.jpg
