months = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
weekday = {1:"Thursday",2:"Friday",3:"Saturday",4:"Sunday",5:"Monday",6:"Tuesday",0:"Wednesday"}
day,month = [int(x) for x in input().split()]
total = months[month] + day
print(weekday[total%7])