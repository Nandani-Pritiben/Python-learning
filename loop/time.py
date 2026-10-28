import time
waight_time=1
attempt=0
max_attempt=5

while attempt<max_attempt:
    attempt+=1
    waight_time*=2
    print(f'attempt: {attempt},waight_time: {waight_time}')
    time.sleep(waight_time)
