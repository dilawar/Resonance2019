all : ./figure_sync_114mm.pdf

%.pdf : %.tex
	lualatex --shell-escape $<
	pdftops -eps $@
	cp figure_sync_114mm.eps ../../../
