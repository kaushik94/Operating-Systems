CSWITCH_TIME = 0.0
FTIME = 2.0

def takeinput():
        N = input()
        jobs = []
        for i in xrange(N):
                jobid, atime, etime = map(float, raw_input().split())
                jobs.append((atime, etime, 0.0, jobid))
        roundrobin(jobs)

def roundrobin(jobs):
        arrival_sorted = sorted(jobs)
        timenow = 0
        donejobs = []
        while len(arrival_sorted):
                print arrival_sorted
                visit = arrival_sorted.pop(0)
                atime, etime, waiting, jobid = visit        
                if etime <= FTIME:
                        etime = 0
                        waiting = timenow-atime
                        timenow += etime + CSWITCH_TIME
                else:
                        etime -= FTIME
                        waiting = timenow-atime
                        timenow += FTIME + CSWITCH_TIME
                if etime <= 0:
                        donejobs.append((atime, etime, waiting, jobid))
                else:
                        arrival_sorted.append((0, etime, waiting, jobid))
                
        print donejobs        
def solve():
        takeinput() 
solve()
