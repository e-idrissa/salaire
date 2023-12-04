mesEmployes = []
lowSalary = 0
highSalary = 0

n = int(input("Nombre de nouveaux employes : "))

for i in range(0,n):
    j = str(i+1)
    employe = {
    'name': input("Entrer le nom de votre "+j+"e employe : "),
    'salary': int(input("Entrer son salaire : ")),
    }
    mesEmployes.append(employe)
    if employe["salary"]>highSalary :
        best = employe
        highSalary = employe["salary"]
    elif employe["salary"]>lowSalary & employe["salary"]<best["salary"] :
        low = employe
        lowSalary = employe["salary"]
    
answer = input("Voulez-vous afficher les employes extremes (y/n) : ")
while answer != "y":
    answer = input("Mauvause touche. Voulez-vous afficher les employes extremes (y/n) : ")
if answer=="y":
    print("L'employe au plus gros salaire est : "+best["name"]+"\nSalaire : "+str(best["salary"]))
    print("L'employe au plus maigre salaire est : "+low["name"]+"\nSalaire : "+str(low["salary"]))
elif answer=="n":
    secAnswer = input("Et votre liste des employes (y/n) : ")
    if secAnswer=="y":
        print("Voici votre liste :")
        print(mesEmployes)
    else : print("Good bye :)")
# print(mesEmployes)