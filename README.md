# Recompile article

All figures have already been generated. They are in PDF format. To recompile
the paper:

    $ pdflatex switches_in_the_brain.tex 


# Regenerating everything again

This is not recommended. Please write to dilawars@ncbs.res.in if you need
something changed in figures.

If you are feeling bold, then you can do the following:

    $ make -B

To generate pdf your need to install `gnuplot`, latest texlive and `latexmk`. On
ubuntu machine:

    $ sudo apt install latexmk gnuplot
