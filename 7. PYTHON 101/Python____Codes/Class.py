class employee:
    company="Goggle"
    level=11
    def upgradelevel(a):
        a.level=a.level+1
        
class freelance:
    company="UpWork"

class WebDeveloperAndDesigner(freelance,employee):
    name="Alvi"

e=employee()
f=freelance() 
p=WebDeveloperAndDesigner()   
print(p.company)
print(p.level)
p.upgradelevel()
print(p.level)
