# Report 2024-10-20: First Draft (Probekapitel):

## Did:
- Theory
- +- Skeleton of pdf, except not sure about "Metrics"
- Provisional Basics and Advanced Policies:
  - theory finished => just write the text and implement it


## TODO:
- Move the Metrics Part: Introduce time complexity?
  - Also reread the performance part of the phd-667.pdf
- !!! go into performance (with graphics?) for each policy !!!
- Fix cApiTaL LetTeRs... and spelling in pdf
- CFS and Solaris scheduler, maybe explain some differences or parts of code
- Implement Comments in Handout/article.tex file
  - labeled as "% TODO:"


## COMPLETE LIST OF UNCHECKED TODOS IN ARTICLE.TEX (find them as "% TODO:"):
### Section Introduction 
* Explain why a CPU can only do one operation at the time

### Section Metrics 
* Move to a different location or split up
* Mention these metrics later on (once implemented performance statistics)

### Basics 
* Overall Define Terms better
* Implementation of Basic Policies in Python
* Dive a bit into Sotring algorithms for the FIFO and etc. (has to also do with time complexity so if than make an input there as well
* (STCF): Rewrite some of the text: weird perspective
* (STCF): Completely redesign the code: more in RR style
* (RR): Why would one want to do really little time slices => explain

### MLFQ 
* Make a connection to previous queues
* Create an example with I/O wait and programs finishing early
* Explain changing queues (goes in the same "define terms better" category)