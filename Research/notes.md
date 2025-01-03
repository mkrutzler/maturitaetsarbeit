# Basics (OStep)
## Introduction (Chapter 7)
Scheduling is not a low level mechanism but a high level policy/disciplines.
We need to make simplifying assumptions of the workload:
1. Each job runs for the same amount of time
2. All jobs arrive at the same time.
3. Once started, each job runs to completion
4. All jobs only use the CPU (no I/O)
5. The run-time of each job is known.
These rules will be eased over time until we get a fully functioning policy.
Of course the more you know the easier it is to schedule.
### Metrics
The fundamental question is: How to we measure the "efficiency" or the "quality" of the scheduler?
You can measure performance or fairness. Here are ways to measure performance:
- turnaround time
  - Calculated as:
    $$T_{turnaround} = T_{completion} - T_{arrival}$$
    For us T_{arrival} = 0, because of simplification 1. (can be neglected later)
- response time: measures the frustration of the user, while looking at the spinning ball
  - Calculated as:
    $$T_{response} = T_{firstrun} - T_{arrival}$$
    - For modern computers, it is essential that this is kept at a minimum
- fairness: first job to finish divided by last job to finish (this is not a performance metric!!)
- does it work dynamically?
### First In, First Out (FIFO) / First Come, First Served (FCFS)
- Most basic scheduling policy
- Given our simplification it works really well and is easy to implement
- However after relaxing assumption 1, it will perform poorly if a huge process gets infront of many small ones
  - This is the so called *convoy effect*
  - It is like if you're at waiting in line to pay and before you have a family of five with two full carts: annoying
### Shortest Job First (SJF)
- The shortest job is run first
  - non-preemptive: runs a process until finish
  - preemptive: can stop and perform a context switch
- If the smaller tasks arrive later (by relaxing assumption 2), then we face the same problem as before. (due to this algorithm can't perform a context switch / is non-preemptive)
### Shortest Time-to-Completion (STCF) / Preemptive Shortest Job First (PSJF)
- This policy requires that rule 3 is ignored.
- This is the preemptive version of SJF.
- It updates, whenever a new job arrives or one is finished
### Round Robin (RR) / time-slicing
- this policy runs each job for a specified "time slice" / "scheduling quantum" (introducing a variable)
- general technique is called "amortization".
- The shorter the time slice, the more responsive the system, however context switching costs CPU time aswell, so you'll need to balance out
- RR is one of the worst policies for turnaround time
- It gives up performance for fairness
### Relaxing Assumptions 4 & 5
#### assumption 4
- If a job waits for I/O than it is in a state called "blocked"
- While a job is waiting for I/O, the CPU can be passed onto somebodye else: "overlapping"
#### assumption 5
- we usually have no idea how long a job will take
- This actually breaks most of our policies, because they all rely on knowing the length of the job (except RR)
- Solution: Multi-Level Feedback Queue (MLFQ) => See next Chapter
## Multi-Level Feedback Queue (Chapter 8)
- One of the most known Policies (Turning Awarded)
- It tries to:
  - optimize turn around time (without knowing the length of the job)
  - minimize response time
### (Basic) Rules of MLFQ
- There are multiple queues and each has their priority level. (higher priority is preferred when switching)
- If multiple jobs are on the same priority than RR (Round Robin) is used
- Priorities can change over time.
- Assume that if a job is resource intensive than it will stay as such. (The history of the job determines the future)
### Changing Priority
- Depending on the CPU time usage, the priority changes
- "allotment": time that a job can spend at a given priority before demotion.
### Priority Boost
- to counter starvation of longer jobs every now and then all of the jobs are put into the priority queue
- also this counters the fact that some programs might start non interactively and than turn into interactive (you know what I mean)
### "Better Accounting" (Anti gaming)
- to prevent people from abusing the allotment method and game the CPU, we need to update rule 4:
- previous:
  a. If a job uses up its allotment while running, its priority is reduced
  b. If a job gives up the CPU before the allotment is up, it stays at the same priority
- new:
  Once a job uses up its time allotment at a given level, its priority is reduced
### Summary of Rules (Copied out of the book)
1. If Priority (A) > Priority (B) => A runs & B doesn't
2. If Priority (A) = Priority (B) => A & B run in RR
3. When a job enters the system, it is placed at the highest priority
4. Once a job uses up its time allotment at a given level, its priority is reduced
5. After some period S, move all the jobs in the system to the topmost queue
### Voo-Doo Constants
These constants heavily change how effective the MLFQ is:
- scheduling quantum (RR)
- amount of queues
- when to priority boost
- allotment (could change in every priority queue)
## Proportional Share (Chapter 9)
- This is a fair scheduler
  - The more/longer jobs run the fairer it becomes
- literally just hold a lottery to determine which programs runs next
- "tickets" represent the share of a resource that a process should recieve = it is like a currency
  - the more tickets you hold, the higher the chance that you have a winning one
  - every time slice a new ticket is picked out as the winning ticket
  - more generally tickets can represent the share of something.
- the tickets are handed out to the user, who than can allocate among their jobs
  - the user can use their "own" tickets which will be converted into the global currency
- ticket transfer can be used to boost a process
  - think server / client => client give server their tickets, so that the server has a higher global share
- ?? in a trusted environment you could also inflate your own tickets to boost you own CPU time
### Advantages of using randomness
- no strange corner-case behaviors
- lightweight
- if the randomizing algorithm is quick than the speed is quick
  - faster algorithms tend to be more like pseudo-random
### Implementation
#### requirements:
- random number generator
- data structure (to track the processes of the system)
- amount of total number of tickets
#### sample code (copied):
```
// counter: used to track if we’ve found the winner yet
int counter = 0;

// winner: call some random number generator to
//         get a value >= 0 and <= (totaltickets - 1)
int winner = getrandom(0, totaltickets);

// current: use this to walk through the list of jobs
node_t *current = head;
while (current) {
    counter = counter + current->tickets;
    if (counter > winner)
        break; // found the winner
    current = current->next;
}
// ’current’ is the winner: schedule it...
```
### Assigning tickets
- Remains open for now
### Stride Scheduling
- it is a deterministic fair-share scheduler
  - while lottery scheduling achieves the proportions with probability (can be off), stride scheduling gets it right each time.
  - PROBLEM: you can't have a new job entering, because it will monopolize the CPU (due to low pass value)
- bit tricky to understand: there is another article about it that I'll later read (under heading Lottery Scheduling)
- how it works:
  - each process has a stride to begin with (the more tickets the smaller the stride)
  - each time the process runs, it's counter (called "pass") get incremented by the value of the stride
    - this is tracking its global progress
  - scheduler schedules according to the pass and the stride
    - pick the lowest pass
#### pseudo-implementation (code copied)
```
current = remove_min(queue); // pick client with min pass
schedule(current); // run for quantum
current->pass += current->stride; // update pass using stride
insert(queue, current); // return current to queue
```
### Sidequest: Linux Completely Fair Scheduler (CFS)
- will talk about it later as well
- every process has a counter called "vruntime"
  - as they run it increases
  - the process with the lowest "vruntime" is next
    - PROBLEM: while waiting / in I/O the process vruntime is not increased: after coming back alive, it'll monopolize the CPU
    - SOLUTION: Once a process wakes up, it will take the lowest amount of vruntime
    - PROBLEM: short sleep will make it less fair for you for you
- the switching is controlled through parameters:
  - sched_latency: dynamic time slice (is calculated), typically 48ms divided by n number of processes
  - sched_latency basicly determines the maximal time frame until each process has run atleast once (if not controlled for minimun time slice)
- There is also a minimal time slice:
  - min_granularity (set to usually 6ms) ensures that each process runs atleast a certain amount of time switching
    - else the context switch would be too expensive
    - with this the scheduler becomes less fair, when only looking at the sched_latency, however it is a good tradeoff
- CFS utilizes the periodic timer interrupt. This means every 1ms it can wake up and determine what to do next
#### Niceness (Priority setting)
- priority setting is done through the "nice" level
  - default: 0 (min: +19, max: -20)
  - the level will be mapped to a "weight" according to a premade table
    - this will keep the proportianility
      meaning: if you have a difference of 5 levels between two jobs, than the ratio of sharing stays the same
  - The time slice is calculated as followed:
    $$timeslice_k = \frac{weight_k}{\sum_{i=0}^{n-1} weight_i} * schedlatency$$
    - here n is the amount of processes
  - new vruntime is also calculated according to the niceness:
    $$vruntime_i = vruntime_i + \frac{weight_0}{weight_i}*runtime_i$$
#### Efficiency of CFS (Red-Black Trees)
- a scheduler has to make decisions as quickly as possible (this should hopefully be scaleable)
- only runnable processes are kept here
  (removed while waiting for I/O)
- efficiency should be logarithmic (what does that mean?)
- how does it even work?
# Computer Scheduling Methods and their Countermeasures
- Started reading it and it didn't really say anything new. I than scanned over it and skipped the rest
## Classification of Policies
### Characteristics
- preemptive vs non-preemptive (already mentionned above)
  - preemptive: if a higher priority exists, than the task can and will be abrupted
  - non-preemptive: opposite of preemptive
- resume vs restart
  - if a preempted job "comes into service again", should we resume where we left off or should we restart the whole thing?
- where does priority come from?
  - job environment (e.g.: running time, I/O)
  - computer system enviroment (dynamic priorities: e.g.: amount of jobs)
  - users environment (assigned by user)
- knowledge of estimated time until finished
  - most of the computers processes don't have a preset time
### Priority Based on running time only
- gives shorter jobs and advantage
#### Shortest Job First (SJF)
- it is assumed that we already know the running time at arrival
- non-preemptive
- rule only reapplied, when a job is finished (could be also giving back the CPU, while waiting for I/O)
- better for shorter running jobs, worse for long ones
#### Preemptive Shortest Job First
- it is assumed that we already know the running time at arrival
- rule reapplied, when a job is finished (+ wait for I/O) or a new job arrives (+ I/O finish)
- preemptive, resume principle
- favors the short jobs even more
- a bit more expensive, because of the context switch
#### Round Robin (RR)
 - running times not known in advance
 - takes both running and arrival time in consideration
 - cannot make the time quantum too small, because context switch will get too expensive
 - ??? What happens if q = 0???
 - for further info read the heading in OStep/Chapter 7
#### Multiple-Level Feedback (FB)
- Do not confuse with the modern MLFQ
- RR but if a task arrives later, it can catch up to the others first
#### Two-Level FB / Limited RR
- work until a fixed amount of quanta, then put into the background (and only run if no one is in queue 1)
#### FB with finite number of levels
- just Two-level FB but with a parameter that tells how many queues exist
- => this gets pretty similar to modern MLFQ
# Lottery/Stride Scheduling
## Lottery and Stride Scheduling: Flexible Proportioal-Share Resource Management
### Abstract
not much to say here
### Introduction
nothing important here either
### 2 - Resource Management Framework

Two basic techniques for tickets:
- ticket transfers => tickets are redistributed amongst clients
- ticket inflation => By manipulating the overall amounts of tickets, you'll change the resource rights
  - currency abstraction => sharing, protecting, naming of resource rights
    - contains the ticket inflation

#### 2.1 - Tickets

Tickets can be distributed with different values (e.g.: 100.- or 20.- bill)
If you seek out tickets, you're active
Tickets give you a right to use resources (you use the resources proportionally to your tickets)
Response time is reverse proportionaly (the more tickets you have, the less response time)

Tickets enable easy comparison between processes and their resources.

THEY ARE NOT CONSUMED! They represent a share of the CPU.

#### 2.2 - Ticket Transfers

Basically what the title already says. They can be redistributed but not created or destroyed. => not suitable for child processes
You can also "boost" other processes: give your tickets to the server, so that it will have more resources and therefore complete your request sooner, while you wait.

Bit advantage over "priority inheritance"?? atleast according to the author


#### 2.3 - Ticket Inflation

This is the "creation" and "destruction" of tickets. => Inflating your own tickets (on a global scale) makes others less "worthy".

to counter this abusive use, we introduce "ticket currencies"

#### 2.4 - Ticket Currencies

Each Parent process can "create" his own currency. The "base tickets" fund these custom currencies. Therefore after inflation the exchange rate changes and not the real value of the tickets.

![Example Sketch](./lottery-scheduling/ticket-currency.png)

you also don't have to be in the same "group" => A could give B1 some of his Currency, which would boost B1.

#### 2.5 - Example Policies

generally not really interesting and repeats some stuff...

you could to a "translation" to priorities by distributing the tickets accordingly:
if priority 1 is run twice as frequent as priority 2 then p1 has 20 tickets and p2 has 10.



### Proportional-Share Mechanisms

Basically the efficient implementation of the philosophy of chapter 2?
the goal is to come as close to actual runtime share as the ticket share (if it makes sense) => it is actually almost impossible
absolute error is the error between the specified and actual allocations
relative error is something I didn't understand (see page 33 middle)

The actual challenge start if we want to implement dynamic environments. It is one thing to manage static tasks and dynamic ones.

randomization can be "exploited" (authors words) => game of chance, however this does need a random number generator or something that sort.
to limit error there is the "multi-winner lottery scheduling", which I have no idea what it is.

also "stride scheduling" is introduced. (it is determenistic)
it computes the interval (also called stride) that each client has to wait?

Now we get to the different policies:

#### Lottery Scheduling

literally just a lottery. the process holding the winning ticket gets the allocation.
accuracy increases with more data (obviously)

(quick) Implementation code: (heavily inspired by page 36)
```cpp
/* Quick Implementation of List-Based Lottery Scheduling Algorithm (not bugtested, just to clear thoughts, heavily inspired after p.36 from "phd-mit-tr667.pdf" */
#include <vector>
#include "client.hpp" /* arbitrary custom client class */

std::vector<client> client_list;
int global_tickets{0};


void client_init(client c, int tickets) {

  /* assign tickets to client and updte global ticket count */
  c.assign_tickets(tickets);
  global_tickets += tickets;

  client_list.push_back(c);
}

void allocate(void) {

  int winner = fast_random() % global_tickets;
  int sum{0};
  int i{0};

  while (sum < winner) {
    c = client_list[i];
    sum += c.tickets;
    i++;
  }

 current = client_list[i-1];
 use_resource(current);

}
```
This method is quite inefficient and you don't really want to use it.
However if you base the algorithm on "balanced binary trees" instead of lists it will become much faster.

This image displays it really well (from page 39 top)

the winner ticket is 25. the right path is chosen and the ticket is adjust accordingly. there are 10 tickets at the left so the "new" winning ticket is 15. 15 is inside 20, so we choose 20. there is no readjusting. after that 15 is larger than 12, meaning 8 is the correct path and process

![Binary Tree](./lottery-scheduling/binary-tree-diagram.png)


There algorithms do not support dynamic operations. it is not difficult to add however, because the single processes do not really change when a newone is added. the only thing that changes is the choosing part (max tickets and stuff).

adding and removing clients is as easy as adding them to the list and adding their tickets to the global max.
As for the binary three variation it is more complex. I think I'll just try to comprehend it for now and not really implement it. I can always come back later.

depending whether the client uses all of the allocation can change it's tickets. For example if you only use a fraction of the time than your tickets can grow and the reverse is true (under a non-preemptive scheduler). This change only persists until he wins again

you can create a "compensate" function and call it right after the allocation

#### Multiwinner lottery scheduling

This is a semi randomized semi deterministic scheduling method.
You basicly hold a large lottery, which will have murrltiple winners. than you have a "superquantum", where everyone gets its CPU time.
You will have a random winner and than a few other winners in a specific offset from the orginal w.
the distribution is uniform and therefore you already have a proportional-share fair system. => WHY????? (page 43)
This can reduce the random error effect, because there are also other clients that will be selected.

The "superquantum" part creates some problems though: which order should the tasks be?

The calculated extra winners mean that the random algroithm has to be used less.
The order of allocations in the superquanta can be either predetermened or randomized. Randomized is much better though, because it means that you won't really have to change anything when you introduce dynamic clients:
if a client joins / leaves, than you just restart the superquanta. if you would do a predetermened permutation of clients, than the first few would get more CPU time, than the ones later.

#### Stride scheduling

Basic Algorithm:
- It is the calculation of "frequency" of allocation
- it is measured in "passes"
- there also "tickets", these are reverse proportional to the strides
- when finding the new client for allocation just look for the lowest pass. than add the stride to the pass for an update
- error should be less than lottery scheduling (idk why tho?)

=> represent in a table

needs adjustments to work dynamically:

basically you have a global ticket and stride variable. you can also save "states" for each client. this will save the difference between the global and the clients pass => if the client rejoins the remainder + the global pass will be taken as the clients pass
if a completely new client appears the stride will be the clients "remainder".
If the global pass gets overall smaller than the remainder should scale appropriatly.


#### hierchical stride scheduling?

Somehow makes sure that the error is not larger than log?
This is important if you have subtasks? basically do the scheduling like a binary tree.

at this point I don't really care about this. I will look at the 2.6 CFS and the ULE. Maybe even some programming? - 2024-10-17

# Time Complexity

# Examples
## Linux 2.6 Fair Scheduler
## Solaris Scheduling
## Ule vs Cfs
