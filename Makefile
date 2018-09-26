all : switches_in_the_brain.pdf
	
figures : 
	cd figures && make

switches_in_the_brain.pdf : ./switches_in_the_brain.tex figures
	latexmk -silent -pdf $<
