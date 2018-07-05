all : switches_in_the_brain.pdf

switches_in_the_brain.pdf : ./switches_in_the_brain.tex engram.pdf ./fig_model.pdf ./hopfield.pdf ./fig_model_b.pdf ./lisman_bistable.pdf ./foget_remember.pdf
	latexmk -latex="pdflatex --shell-escape %O %S" $<

%.pdf : %.tex
	lualatex --shell-escape $<
