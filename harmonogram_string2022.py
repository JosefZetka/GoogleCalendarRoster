import pandas as pd
from zaznam import Zaznam, Record, casy, in_case, datetime_str_adding
file = pd.ExcelFile("D:\\programming\\Google Calendar Roster\\Google Calendar 2020-20201205T184646Z-001\\Google Calendar 2020\\Harm_Disp_2022.xls")
vysledek = {}
k = 1
import pdb
for sname in file.sheet_names:
    try:
        sh = pd.read_excel(io =file,sheet_name=sname,header = 1, index_col=[0,1],skiprows=0)
        
        for d in range(1,len(sh.columns)):
            print("d je {0} a len(sh.columns)={1}".format(d,len(sh.columns)))
            print("sh[d][1] = {0}".format(sh[d][1]))
            print("sh[d][2] = {0}".format(sh[d][2]))
            k+=1
            if pd.isna(sh[d][1]) == True:                            
                if pd.isna(sh[d][2]) == True:                   
                    print("sh[d][1] = {0}".format(sh[d][1]))
                    print("sh[d][2] = {0}".format(sh[1][2]))
                else:
                    vysledek.update({k:Zaznam(sname,d,sh[d][2])})
                    print("sh[d][1] = {0}".format(sh[d][1]))
                    print("sh[d][2] = {0}".format(sh[1][2]))
            else:    
                if pd.isna(sh[d][2]) == True:
                    vysledek.update({k:Zaznam(sname,d,sh[d][1])})
                    print("sh[d][1] = {0}".format(sh[d][1]))
                    print("sh[d][2] = {0}".format(sh[1][2]))
                else:
                    vysledek.update({k:Zaznam(sname,d,sh[d][2])})
                    print("sh[d][1] = {0}".format(sh[d][1]))
                    print("sh[d][2] = {0}".format(sh[1][2]))
            print("sh[d][1] = {0}".format(sh[d][1]))
            print("sh[d][2] = {0}".format(sh[1][2]))
    except:
        
        print(sname + " = problem ")
f = open("demofile1.txt", "w")
gf = open("googlecalendar2022.csv","w")
gf.writelines("Subject,Start Date,Start Time,End Date,End Time\n")
for k in vysledek.keys():
    #breakpoint() JE NUTNE NEZAPOMENOUT ZMENIT v Zaznam in_case rok resp. nazev listu bude I.22 nebo I.23 nebo I.24
    f.writelines(str(k) + " : " + str(vysledek[k].mesic) + " , " +  str(vysledek[k].den) + " , " + str(vysledek[k].smena +"\n"))
    #f.write("Woops! I have deleted the content!")
    subject = vysledek[k].smena
    startdate = str(in_case(vysledek[k].mesic)) +"/"+ ("{:0>2d}".format(vysledek[k].den))+"/" + (str(2022))
    starttime = str(casy(vysledek[k].smena)[0])
    end_datetime_str = datetime_str_adding(startdate,starttime)
    gf.writelines(subject + "," + startdate + "," + starttime + "," + end_datetime_str +  "\n")

            

f.close()
gf.close()




