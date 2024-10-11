import csv  
    
# field names  
fields = ['Name', 'Age']  
    
# data rows of csv file  
rows = [ ['Nikhil', '18'],  
         ['Sanchit', '19'],  
         ['Aditya', '18'],  
         ['Sagar', '20'],  
         ['Prateek', '21'],  
         ['Sahil', '19']]  
    
# name of csv file  
filename = #enter file name
    
# writing to csv file  
with open('#enter file name', 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 