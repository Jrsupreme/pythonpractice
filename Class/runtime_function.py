#calculate uptime
#substract the down time to the total time 
#total uptime should be in percentage
#return the result as a vaiable rounded to two decimal places

def runtime(total_hours, down_hours):
    uptime = ((total_hours - down_hours)/total_hours) * 100 #basic percentage math formula
    return round(uptime, 2) #round method takes the first argument and round's it up to the number of decimal places specified in second argument

print(runtime(213, 37))



