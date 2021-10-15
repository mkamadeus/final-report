all: generate clean

generate:
	mkdir -p out
	pdflatex -shell-escape -interaction=batchmode main.tex -output-format=pdf 
	biber main.bcf
	pdflatex -shell-escape -interaction=batchmode main.tex -output-format=pdf
	mv main.pdf out/ 
.PHONY: generate

clean:
	rm -rf *.aux *.log *.out *.xml *.toc *.bbl *.bcf *.blg
.PHONY: clean

check:
	lacheck main.tex
.PHONY: check
