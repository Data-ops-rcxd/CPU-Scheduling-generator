import xlsxwriter
import random, time

## Number of process:
n = 15


pburst = dict()
parrvl = dict()
wtprom = 0
tatprom = 0

for i in range(n):
    pburst[i] = random.randrange(1000,2000,1)
    parrvl[i] = i

def fcfs(pburst, parrvl):
    wt = dict()
    tat = dict()
    gc = 0
    for i in range(n):
        if parrvl[i] == 0:
            gc += pburst[i]
            wt[i] = 0
            tat[i] = pburst[i]
            worksheet.write('A'+ str(jum+i+2),i+1)
            worksheet.write('B'+ str(jum+i+2),pburst[i])
            worksheet.write('C'+ str(jum+i+2),parrvl[i])
            worksheet.write('D'+ str(jum+i+2),wt[i])
            worksheet.write('E'+ str(jum+i+2),tat[i])
            
        else:
            gc =+ pburst[i]
            wt[i] = pburst[i-1] - parrvl[i]
            tat[i] = pburst[i] + wt[i]
            worksheet.write('A'+ str(jum+i+2),i+1)
            worksheet.write('B'+ str(jum+i+2),pburst[i])
            worksheet.write('C'+ str(jum+i+2),parrvl[i])
            worksheet.write('D'+ str(jum+i+2),wt[i])
            worksheet.write('E'+ str(jum+i+2),tat[i])

    promwt = sum(wt.values())/len(wt)
    promtat = sum(tat.values())/len(tat)

    worksheet.write('F'+ str(jum+i+2),promwt)
    worksheet.write('G'+ str(jum+i+2),promtat)

    #Tiempo de espera es = Burst time del anterior - Arrival time
    #Turn around time = Burst time propio + tiempo de espera
    return promwt, promtat

workbook = xlsxwriter.Workbook("Gant chart.xlsx")
worksheet = workbook.add_worksheet("FCFS")
worksheet.write('A1','Process')
worksheet.write('B1','Burst Time')
worksheet.write('C1','Arrival Time')
worksheet.write('D1','Waiting Time')
worksheet.write('E1','Turnaround Time')
worksheet.write('F1','Waiting Avg')
worksheet.write('G1','Turnaround Avg')
worksheet.write('H1','FCFS length time')

jum = 0

inicio = time.time()
for index in range(10000):
    wtprom, tatprom = fcfs(pburst, parrvl)
    jum = jum + n
duracion = time.time() - inicio

worksheet.write('H2', duracion)

workbook.close()

print('Duración del FCFS:', duracion)
print('Waiting Time promedio FCFS:', wtprom)
print('Turn Around Time promedio FCFS:', tatprom)

#En el caso de estar en desorden se puede usar parrvl = sorted(parrvl.items(), key=operator.itemgetter(1))
# o key=lambda item: item[1]
