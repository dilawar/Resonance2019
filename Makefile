all : switches_in_the_brain.pdf

%.pdf : %.tex
	lualatex --shell-escape $<

switches_in_the_brain.pdf : ./switches_in_the_brain.tex engram.pdf \
    ./fig_model.pdf ./hopfield.pdf \
    ./fig_model_b.pdf \
    ./lisman_bistable.pdf  ./lisman_bistable_small.pdf \
    ./integrator.pdf \
    ./stability_noise.pdf \
    ./strong_bis_naren_and_bhalla_87mm.pdf \
    ./camkii_properties.pdf \
    ./foget_remember.pdf
	latexmk -latex="pdflatex --shell-escape %O %S" $<

