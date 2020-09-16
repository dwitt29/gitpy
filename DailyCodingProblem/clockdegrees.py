
# Daily Coding Problem: Problem #548 [Easy] 

clock = '03:15'

hrs, mins = clock.split( ':' )
mins = int(mins)
hrs = int(hrs)
if hrs > 12: hrs -= 12
deg_per_hr = 360 / 12
deg_per_min = 360 / 60

hrs_in_degrees = int(hrs*deg_per_hr)
mins_in_degrees = int(mins*deg_per_min)

print( abs( hrs_in_degrees - mins_in_degrees) )
