#Ejercisio 146: 

def new_game():
    respuestas=[]
    respuestas_correctas=0
    pregunta_num=0
    
    for key in preguntas:
        print("----------------------------------------------------")
        print(key)
        for i in opciones[pregunta_num]:
            print(i)
        
        respuesta=input("Ingresa(A, B, C o D)").upper()
        respuestas.append(respuesta)
        
        respuestas_correctas+= check_answer(preguntas.get(key),respuesta)
            
        pregunta_num+=1
    
    display_score(respuestas_correctas, respuestas)
    
#----------------------------------------------------
def check_answer(respuesta_correcta, respuesta):
    
    if respuesta_correcta ==respuesta:
        print("Correcto")
        return 1
    else:
        print("Incorrecto")
        return 0
    
#----------------------------------------------------
def display_score(respuestas_correctas, respuestas):
    print("----------------------------------------------------")
    print("Resultado")
    print("----------------------------------------------------")
    
    print("Respuestas correctas: ", end=" ")
    for i in preguntas:
        print(preguntas.get(i), end=" ")
    print()
    
    print("Tus respuestas: ",end=" ")
    for i in respuestas:
        print(i, end=" ")
    print()
    puntaje= int((respuestas_correctas/len(preguntas))*100)
    print("Puntaje: " + str(puntaje)+ "%")    
#----------------------------------------------------
def play_again():
    respuesta=input("Quieres jugar de nuevo? (SI o NO): ").upper()
    
    if respuesta == "SI":
        return True
    else:
        return False
#----------------------------------------------------

preguntas={
    "Que idioma se habla en Brasil?: ": "A",
    "Cual es el oceano mas grande del mundo":"B",
    "Cual es la estrella mas cercana a la tierra?":"C",
    "Cual es el segundo pais mas grande del mundo?":"A"
}

opciones= [["A, Portugues","B, Español","C, Brasilero", "D, Ingles"],
           ["A, Atlantico","B, Pacifico","C, Artico", "D, Indio"],
           ["A, La luna","B, Alfa Centauri A","C, El sol", "D, ninguno"],
           ["A, Canada","B, Rusia","C, EE.UU", "D, China"]
]

new_game()

while play_again():
    new_game()
    
print("Adios")