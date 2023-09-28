def averageRuns(runs, matches, notout):
 
    
    out = matches - notout;
 
   
    if (out == 0):
        return -1;
 
    
    avg = runs // out;
 
    return avg;
 

runs = 50000;
matches = 550;
notout = 150;
 
avg = averageRuns(runs, matches, notout);
 
if (avg == -1):
    print("NA");
else:
    print(avg);
 