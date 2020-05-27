import model as mo
import view as vi

custlist=[]
page=-1

view = vi.viewer()
model = mo.model()
while True:
    choice = view.hello()
    if choice=="I":
        custlist, page = model.inputI(custlist, page)
    elif choice=="C":
        custlist, page = view.inputC(custlist, page)
    elif choice == 'P':
        custlist, page = view.inputP(custlist, page)
    elif choice == 'N':
        custlist, page = view.inputN(custlist, page)
    elif choice=='D':
        custlist, page = model.inputD(custlist, page)
    elif choice=="U": 
        custlist, page = model.inputU(custlist, page)
    elif choice=="S":
        view.search()
    elif choice=="Q":
        model.write(custlist)
    elif choice=="FU":
        model.fupdate(custlist)
    else:
        break
