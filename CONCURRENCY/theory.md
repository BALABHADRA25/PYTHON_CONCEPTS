Concurrency - refers to the ability of a program to manage multiple task at once, improving performance ad responsivness.

In python, thread and asynchronous tasks facilitate concurrency on a single processor,
while multiprocessing allows for true parallelism by utilizing multiple CPU cores.

Concurrency - simultaneous occurence
In python the things that are occuring simultaneously are called by different names:
- thread
- task
- process

The way thread, task and processes takes turn differ.

preemptive mutitasking
========================
In multi-thread approach, the operating system actually know about each thread and can interrupt
it any time and start running a different thread.
This mechanism is also true for process.
Here the operating system can preempt your thread or process to make the switch.

cooperative mutitasking
=======================
Asynchronous task uses cooperative mutitasking.
The task must cooperate each other by announcing when they are ready to be switched out without operating system involvement.

process
=========
A process can be thought of as almost a completely different program.
Each process run in its own python interpreter.


asyncio---one cpu core---cooperative---The task decide when to give up the control.

threading---one cpu core--preemptive---The operating system decides when to switch tasks external to python

multiprocessing---many cpu core---preemptive---The processes run all at the same time in different processor.

Concurrency can make big difference in two types of problem
- I/O Bound -- program spends most of the time waiting 
- CPU Bound -- program spend most of the time doing CPU operation.





