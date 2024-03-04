from multiprocessing import Process, Queue
from Queue import Empty
from random import choice as rndchoice
import time

def worker(id, todo_q, start_q, finish_q):
    """multiprocessing worker"""
    msg = None
    while (msg!='DONE'):
        try:
            msg = todo_q.get_nowait()    # Poll non-blocking on todo_q
            if (msg!='DONE'):
                start_q.put((id, msg))   # Let the controller know work started
                time.sleep(0.05)
                if (rndchoice(range(3))==1):
                    # Die a fraction of the time before finishing
                    print "DEATH to worker %s who had task=%s" % (id, msg)
                    break
                finish_q.put((id, msg))  # Acknowledge work finished
        except Empty:
            pass
    return

if __name__ == '__main__':
    NUM_WORKERS = 5
    WORK_ID = set(['A','B','C','D','E']) # Work to be done, you will need to
                                    #    name work items so they are unique
    WORK_DONE = set([])             # Work that has been done
    ASSIGNMENTS = dict()            # Who was assigned a task
    workers = dict()
    todo_q = Queue()
    start_q = Queue()
    finish_q = Queue()

    print "Starting %s tasks" % len(WORK_ID)
    # Add work
    for work in WORK_ID:
        todo_q.put(work)

    # spawn workers
    for ii in xrange(NUM_WORKERS):
        p = Process(target=worker, args=(ii, todo_q, start_q, finish_q))
        workers[ii] = p
        p.start()

    finished = False
    while True:
        try:
            start_ack = start_q.get_nowait()  # Poll for work started
            ## Check for race condition between start_ack and finished_ack
            if not ASSIGNMENTS.get(start_ack[0], False):
                ASSIGNMENTS[start_ack[0]] = start_ack   # Track the assignment
                print "ASSIGNED worker=%s task=%s" % (start_ack[0], 
                    start_ack[1])
                WORK_ID.remove(start_ack[1])      # Account for started tasks
            else:
                # Race condition. Never overwrite existing assignments
                # Wait until the ASSIGNMENT is cleared
                start_q.put(start_ack)
        except Empty:
            pass

        try:
            finished_ack = finish_q.get_nowait()  # Poll for work finished
            # Check for race condition between start_ack and finished_ack
            if (ASSIGNMENTS[finished_ack[0]][1]==finished_ack[1]):
                # Clean up after the finished task
                print "REMOVED worker=%s task=%s" % (finished_ack[0], 
                    finished_ack[1])
                del ASSIGNMENTS[finished_ack[0]]
                WORK_DONE.add(finished_ack[1])
            else:
                # Race condition. Never overwrite existing assignments
                # It was received out of order... wait for the 'start_ack'
                finish_q.put(finished_ack)
            finished_ack = None
        except Empty:
            pass

        # Look for any dead workers, and put their work back on the todo_q
        if not finished:
            for id, p in workers.items():
                status = p.is_alive()
                if not status:
                    print "    WORKER %s FAILED!" % id
                    # Add to the work again...
                    todo_q.put(ASSIGNMENTS[id][1])
                    WORK_ID.add(ASSIGNMENTS[id][1])
                    del ASSIGNMENTS[id]      # Worker is dead now
                    del workers[id]
                    ii += 1
                    print "Spawning worker number", ii
                    # Respawn a worker to replace the one that died
                    p = Process(target=worker, args=(ii, todo_q, start_q, 
                        finish_q))
                    workers[ii] = p
                    p.start()
        else:
            for id, p in workers.items():
                p.join()
                del workers[id]
            break

        if (WORK_ID==set([])) and (ASSIGNMENTS.keys()==list()):
            finished = True
            [todo_q.put('DONE') for x in xrange(NUM_WORKERS)]
        else:
            pass
    print "We finished %s tasks" % len(WORK_DONE)