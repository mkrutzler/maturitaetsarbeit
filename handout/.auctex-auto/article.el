;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "article"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("titlesec" "") ("titling" "") ("hyperref" "") ("geometry" "margin=1in") ("ulem" "normalem") ("xcolor" "") ("graphicx" "")))
   (TeX-run-style-hooks
    "latex2e"
    "art10"
    "titlesec"
    "titling"
    "hyperref"
    "geometry"
    "ulem"
    "xcolor"
    "graphicx")
   (TeX-add-symbols
    "thesubtitle"
    "currentdate"
    "auinstitution"
    "squiggly"))
 :latex)

