all: generate clean

generate:
	latexmk -synctex=1 -interaction=nonstopmode -file-line-error -pdf main.tex
.PHONY: generate

clean:
	rm -rf *.aux *.log *.out *.xml *.toc *.bbl *.bcf *.blg
.PHONY: clean

check:
	lacheck main.tex
.PHONY: check

lint:
	chktex main.tex
.PHONY: lint
