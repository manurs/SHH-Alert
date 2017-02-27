import time

def getYesterday():
  day = int(time.strftime("%d"))
  month = time.strftime("%b")
  year = int(time.strftime("%Y"))

  if day!=1:
    return day-1, month, year
  
  #El dia uno no va hacia atrás
  else:
    list_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    list_num_m = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    pos_m = int(time.strftime("%m"))-1 #index by 0, no 1
    
    if pos_m==0: #Caso especial, nos vamos al año anterior
      pos_m=12
      year=year-1
    
    month = list_month[pos_m-1]
    day = list_num_m[pos_m-1]
    
    if day==-1:
      #Febrero tiene miga
      if y%4==0 and y%100!=0 or y%400==0:
        day=29 #Bisiesto
      else:
        day=28
    
    return day, month, year
