import numpy as np
import cv2
import os

def carregaNomesASeremLidos(txt):
    nomesCadastrados = []
    pFile = open(txt, "r")
    for line in pFile:
        nomesCadastrados.append(line.rstrip())
    return nomesCadastrados

def criaPastaComNomes(listaNomes):
    for nome in listaNomes:
        try:
            print("criou " + nome)
            os.mkdir("./data/"+nome)
        except OSError:
            print("Não foi possível criar o diretório ou o mesmo já existe.")

def salvaFacesDetectadas(nome):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0) #inicia captura da câmera

    counterFrames = 0
    while(counterFrames < 120): #quando chegar ao milésimo frame, para
        print(counterFrames)
        ret, img = cap.read()

        #frame não pode ser obtido? entao sair
        if(ret == False):
            cap.release()
            return

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #se nenhuma face for achada, continue
        if not np.any(faces):
            continue

        #achou uma face? recorte ela (crop)
        for (x, y, w, h) in faces:
            rostoImg = img[y:y+h, x:x+w]

        #imagens muito pequenas são desconsideradas
        larg, alt, _ = rostoImg.shape
        if(larg * alt <= 20 * 20):
            continue

        #salva imagem na pasta
        rostoImg = cv2.resize(rostoImg, (255, 255))
        cv2.imwrite( nome + "/" + str(counterFrames)+".png", rostoImg)
        counterFrames += 1
            
    cap.release()

#função principal da aplicação

nomesCadastrados = carregaNomesASeremLidos("input.txt")
criaPastaComNomes(nomesCadastrados)

for nome in nomesCadastrados:
    print("Analisando: " + nome)
    salvaFacesDetectadas(nome)