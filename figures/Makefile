FIGS := engram.pdf \
    ./fig_model.pdf \
    ./hopfield.pdf \
    ./fig_model_b.pdf \
    ./lisman_bistable.pdf \
    ./lisman_bistable_small.pdf \
    ./integrator.pdf \
    ./stability_noise.pdf \
    ./strong_bis_naren_and_bhalla_87mm.pdf \
    ./camkii_properties.pdf \
    ./bistable_multistabe_synapse.pdf \
    ./camkii_pp1_switch_level1_detail.pdf \
    ./foget_remember.pdf \
    ./camkii_subunit_exchage.pdf \
    ./self_phospho.pdf \

all : $(FIGS)

camkii_properties.pdf: integrator.pdf \
    camkii_pp1_switch_level1_detail.pdf \
    camkii_subunit_exchage.pdf

%.pdf : %.tex
	lualatex --shell-escape $<
	cp $@ ..

.PRECIOUS: %.pdf %.ps
