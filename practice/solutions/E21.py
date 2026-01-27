def solve(data):
    done=[]
    while len(done)<len(data):
        ready=sorted(k for k,v in data.items() if k not in done and set(v)<=set(done))
        if not ready: return 'cycle'
        done.append(ready[0])
    return done
