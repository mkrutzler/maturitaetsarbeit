#!/usr/bin/env sh
pdflatex -synctex=1 -shell-escape -interaction=nonstopmode Thesis.tex
open Thesis.pdf
