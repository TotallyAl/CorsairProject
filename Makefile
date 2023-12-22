# Makefile for compiling LaTeX documents

# Set the main file (change 'main.tex' to your actual main file)
MAIN_FILE = report.tex

# List all .tex files (except the main file)
TEX_FILES = $(filter-out $(MAIN_FILE), $(wildcard *.tex))

# Set the output PDF file
OUTPUT_PDF = report.pdf

# Default target: compile the main file
all: $(OUTPUT_PDF)

# Compile the main file
$(OUTPUT_PDF): $(MAIN_FILE) $(TEX_FILES)
	pdflatex $(MAIN_FILE)
	pdflatex $(MAIN_FILE)

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc

# Clean up all generated files
distclean: clean
	rm -f $(OUTPUT_PDF)

# PHONY targets
.PHONY: all clean distclean
