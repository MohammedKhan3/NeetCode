def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    sum=0
    for i,e in enumerate(queries):
        queriesLeft = len(queries)-(i+1)
        sum+= e*queriesLeft
    return sum
