lista_angajati=[] #lista in care retinem toate informatiile despre angajati
                  #fiecare element al listei reprezinta setul complet de informatii despre fiecare angajat

    # d['average_age'] = $avg
    # d['best_paid_job'] = $best_paid
    # d['best_paid_employee'] = $best_paid_employee
    # d['no_employees'] = $no_employees
    # d['top_3_jobs'] = [$job1,$job2, $job3]
    # d['seniors'] = $no_seniors
    # d['middle'] = $no_middle
    # d['juniors'] = $no_juniors'



def functie (f):
    d = {}
    lista_angajati = f.readlines()
    #print(lista_angajati)
    lista_date_angajati = []
    for i in lista_angajati:
        date_angajat = i.split('\t')
        # In lista date_angajat avem:
        # pozitia 0 - nume
        # pozitia 1 - varsta
        # pozitia 2 - ocupatie
        # pozitia 3 - salariu
        # pozitia 4 - vechime


        date_angajat[1] = int(date_angajat[1])    #convertire varsta din string in int
        date_angajat[3] = int(date_angajat[3])    #convertire salariu din string in int
        date_angajat[4] = int(date_angajat[4])    #convertire vechime din string in int
        lista_date_angajati.append(date_angajat) #lista de liste date_angajat. Fiecare element al acestei liste va fi reprezentat de lista cu datele unui singur angajat



    ############################ CALCULARE VARSTA MEDIE ##################################
    suma = 0
    for i in lista_date_angajati:
        suma += i[1]
    avg = suma/ len(lista_date_angajati)
    d['average_age'] = avg  # adaugam in dictionar average_age



    ############################ CALCULARE best_paid_job ##################################
    salariu = set() # in acest set vom retine toate valorile pentru salariu
    for i in lista_date_angajati:
        salariu.add(i[3])

    best_paid = max(salariu)
    #print('Salariul maxim este: '+ str(best_paid))
    d['best_paid_job'] = best_paid  #adaugam in dictionar best_paid_job



    ############################ CALCULARE best_paid_employee ##################################
    for i in lista_date_angajati:
        if(i[3] == best_paid):
            best_paid_employee = i[0]
    #print('Cel mai mare salariu il are: '+ str(best_paid_employee))
    d['best_paid_employee'] = best_paid_employee



    ############################ CALCULARE NUMAR DE ANGAJATI ##################################
    no_employees = len(lista_date_angajati)
    #print(str(no_employees) + ' angajati in firma')
    d['no_employees'] = no_employees



    ############################ CALCULARE TO 3 JOBS ##################################
    # facem un dictionar JOBS in care punem perechile JOB - Nr angajati pe acea pozitie

    jobs = {} #perechi job- nr de aparitii
    for i in lista_date_angajati:
        if i[2] not in jobs:
            jobs.update({i[2]: 1})
        else:
            jobs[i[2]] = jobs[i[2]] + 1
    #print(jobs)
    job_sortat = []
    for w in sorted(jobs, key=jobs.get, reverse=True):
        job_sortat.append(w)
    # print("\n")
    # print(job_sortat)

    top_3_jobs = []
    top_3_jobs = job_sortat[0:3]
    d['top_3_jobs'] = top_3_jobs
    # print(top_3_jobs)





    ############################ CALCULARE NUMAR DE SENIORI, MIDDLE SI JUNIORS ##################################
    no_seniors = 0
    no_middle = 0
    no_juniors = 0
    for i in lista_date_angajati:
        if (i[4] > 5):
            no_seniors += 1
        elif(i[4] >3):
            no_middle += 1
        else:
            no_juniors += 1

    # print(str(no_seniors) + ' seniori in firma')
    # print(str(no_middle) + ' middle in firma')
    # print(str(no_juniors) + ' juniors in firma')

    d['seniors'] = no_seniors
    d['middle'] = no_middle
    d['juniors'] = no_juniors



    print(d)
    return d







with open('test_file', mode='r', encoding='utf-8') as file:
    functie(file)
