BUILDDIR=build
OUTPUTDIR=output

SRC := $(wildcard src/*.tex)
PDFS := $(patsubst src/%.tex, output/%.pdf, $(SRC))

export TEXINPUTS := .:./include:./build:

all: $(PDFS)

output/%.pdf: src/%.tex
	pdflatex -output-directory build $<
	mv $(BUILDDIR)/*.pdf $@

# Make sure the directories exist.
ifeq ($(wildcard $(BUILDDIR)/),)
$(shell mkdir -p $(BUILDDIR))
endif
ifeq ($(wildcard $(OUTPUTDIR)/),)
$(shell mkdir -p $(OUTPUTDIR))
endif
