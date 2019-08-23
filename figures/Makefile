EPSES := engram.eps \
    ./fig_model.eps \
    ./hopfield.eps \
    ./fig_model_b.eps \
    ./lisman_bistable.eps \
    ./lisman_bistable_small.eps \
    ./integrator.eps \
    ./stability_noise.eps \
    ./strong_bis_naren_and_bhalla_87mm.eps \
    ./camkii_properties.eps \
    ./bistable_multistabe_synapse.eps \
    ./foget_remember.eps \

all : $(EPSES)

camkii_properties.eps: integrator.eps

%.pdf : %.tex
	lualatex --shell-escape $<

%.eps : %.pdf
	pdftops -eps $<
	cp $@ ..

