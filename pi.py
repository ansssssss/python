import time

    pi = 0
    before = time.time()
    for i in range(0,asdf+1):
        new = (-1)**i/(2*i+1)
        pi +=new
    now = time.time()
    runtime = now - before
    print("\n"+str(runtime))
