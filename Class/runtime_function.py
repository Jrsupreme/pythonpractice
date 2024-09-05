#calculate uptime
#substract the down time to the total time 
#total uptime should be in percentage
#return the result as a vaiable rounded to two decimal places

def runtime(total_hours, down_hours):
    uptime = ((total_hours - down_hours)/total_hours) * 100
    return round(uptime, 2)

runtime(200, 20)

print(uptime)