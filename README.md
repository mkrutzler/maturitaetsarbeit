# README
## Main Goal / Concept
Learning about CPU-Scheduling policies. Maybe could even broaden the horizon to general scheduler algorithms.
## Scratchpad (for ideas)
Maybe the the scheduling concepts and apply it to something else that we usually don't overcomplicate. This will be hard though, because we as humans have other variables influence our efficiency than CPUs do (e.g.: deadlines, no I/O, etc.). Deadlines would require an estimate time to finish, which is probably hard to do. Priority adjustment would be with the date approaching. However the efficiency of calculation is less necessary, because we don't count in ms but in minutes.
In addition to that I would have to worry about a user interface. I might just finish all of my theory and start writing the handout, before I decide whether to do this or not.

Another thing that I could do is a C++ implementation of one of the algorithms. Lottery/Stride would be probably the best, because that's where I have most of my material and is (rather) simple compared to something like CFS (just a guess).
## Report 2024-08-25
### What I have done
- General information gathering
- Looking at the basics and overview of approches
- created notes in org
### What I haven't done
- Write / Think about the Handout
- Write Code
### What I am planning to do
- especially theory for now
- dive into lottery / stride scheduling more
  - ??implementation??
- reading through a comparison between the FreeBSD (Ule) and Linux (CFS) scheduler
- bit of datastructure (red-black tree)
- if not enough material:
  - multi CPU
  - adjusting parameters using machine learning (prob won't touch it)
