process = ["p0", "p1", "p2", "p3", "p4"]
arrivalTime = [1, 2, 3, 4, 5]
burstTIme = [10, 1, 2, 1, 5]
priority = [3, 1, 4, 5,  2]
readyQueue = []



#priority preempt

#p1 (1 - 2)3 - p2 (2-3)1 - p1 (3-11)3 - p3 (11-13)4 - p4 (13-14)5 - p5 (14-19)2
#(also wrong, need to visualize ready queue and keep count of time)
#have a while loop that runs while true, add a job as current job, keep time, have a queue, add other jobs




#priority without preemption

#p1 - p2 - p3 - p4 - p5 (wrong as initial p1 execution takes 10 seconds)
#add arrivals + duration and keep running time to track execution times, or have a job queue

#Round Robin
#each process gets a small unit of cpu time referred to ss a quantum, q.
#if there are n processes in the ready queue and the time quantum is q, then each process gets 2/n of cpu time in chunks of at most q time units at once
#no process waits more than (n-1)q
#performance: if q is large enough, FIFO (lots of time wasted)
#if q is small enough, q must be larhe with respect to context switcj, otherwise overheaad is too high
#example of RR with q = 4

#example
#     duration / arrival
# p1  10  1 
# p2  4   2
# p3  2   3
# p4  3   4
# p5  5   5

#1-3 p1
#3-5 p2
#5-7 p3
#7-9 p1
#9-10 p4
#10-12 p5
#12-14 p2
#14-16 p1
#16-18 p5
#18-20 p1
#20-21 p5
#21-23 p1



# queue = p1 
# tally of how many seconds left per process kept in queue as part of struct
