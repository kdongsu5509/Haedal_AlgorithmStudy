for x in range(10) :
        for i in range(len(progresses)) :
            if (progresses[i] < 100) :
                progresses[i] += speeds[i]
                result[i] += 1