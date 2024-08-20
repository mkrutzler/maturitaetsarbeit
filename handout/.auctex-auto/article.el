;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "article"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("titlesec" "") ("titling" "") ("hyperref" "") ("geometry" "margin=1in") ("ulem" "normalem") ("xcolor" "") ("graphicx" "")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
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

