# Makefile for compiling LaTeX documents

# Set the main file (change 'main.tex' to your actual main file)
MAIN_FILE = report.tex

# List all .tex files (except the main file)
TEX_FILES = $(filter-out $(MAIN_FILE), $(wildcard *.tex))

# Set the output PDF file
OUTPUT_PDF = report.pdf

DATA_DIR = ./data
SCRIPTS_DIR = ./scripts

DATA_CSV = $(wildcard $(DATA_DIR)/*.csv)
SCRIPTS = $(wildcard $(SCRIPTS_DIR)/*.py)
DATA_PDF = $(patsubst $(DATA_DIR)/%.csv, $(DATA_DIR)/%.pdf, $(DATA_CSV))
EXTRA_PDF = $(DATA_DIR)/combined_vel_accel.pdf
PICTURES_DIR = ./pics 
PICTURES = $(wildcard $(PICTURES_DIR)/*.png)

# Default target: compile the main file
all: print_vars $(OUTPUT_PDF)

graphs: $(DATA_PDF) $(SCRIPTS)

print_vars:
	$(info DATA_CSV: $(DATA_CSV))
	$(info DATA_PDF: $(DATA_PDF))
	$(info SCRIPTS: $(SCRIPTS))

# General rule for converting CSVs into PDF
%.pdf: %.csv $(SCRIPTS)
	$(SCRIPTS_DIR)/plot.py $< $@

# Special rule for displacement_angle_amortisseur.pdf
$(DATA_DIR)/displacement_angle_amortisseur.pdf: $(DATA_DIR)/displacement_angle_amortisseur.csv $(SCRIPTS)
	$(SCRIPTS_DIR)/plot_displacement.py $(DATA_DIR)/displacement_angle_amortisseur.csv $(DATA_DIR)/displacement_angle_amortisseur.pdf

$(DATA_DIR)/combined_vel_accel.pdf: $(DATA_CSV) $(SCRIPTS)
	$(SCRIPTS_DIR)/plot_combined_accel_vel.py $(DATA_DIR)/velocity_axeAmortisseur.csv $(DATA_DIR)/amortisseur_axeAmortisseur.csv combined_vel_accel.pdf

# Compile the main file
$(OUTPUT_PDF): $(MAIN_FILE) $(DATA_PDF) $(EXTRA_PDF) $(PICTURES)
	pdflatex $(MAIN_FILE)
	pdflatex $(MAIN_FILE)

# Clean up auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc

# Clean up all generated files
distclean: clean
	rm -f $(OUTPUT_PDF)

# PHONY targets
.PHONY: print_vars clean distclean
