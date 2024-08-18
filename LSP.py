#LSP liskoy's subtitution principle

#class Ave:
   # def volar(self):
    #    return "estoy volando"
    
#class Pinguino(Ave):
    #def volar(self):
    #    return "no puedo volar"

#def hacer_volar(ave= Ave):
    #return ave.volar()

#print(hacer_volar(Pinguino())) 

class Ave:
    pass

class Ave_no_voladora(Ave):
    def volar(self):
        return "estoy volando"
    
class Ave_no_volar(Ave):
    pass    