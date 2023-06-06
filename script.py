import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lote3.jpg")

#contorno
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = 100

ret,thresh_img = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    #area do contorno
    area = cv2.contourArea(c)
    #segmentando contorno especifico
    if area > 54000 and area < 55000:
        #desenhando contorno
        cv2.drawContours(img, c, -1, (0, 0, 255), 3)
        cv2.putText(img, ("Area: " + str(area)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        hectare = 10000
        #calculo de quantos hectares a area tem
        hectare_por_area = area/hectare
        cv2.putText(img, ("Hectare por area: " + str(hectare_por_area)), (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

        #calculo de sementes de milho por hectare
        taxa_semeadura_milho = 3
        espacamento_milho = 0.45
        sementes_milho_hectare = (hectare / espacamento_milho) * taxa_semeadura_milho * 1.1
        print("Milho:","\n", 
              "Espaçamento: ", espacamento_milho, " metros" ,"\n", 
              "Taxa de semeadura: ", taxa_semeadura_milho, " sementes/metro linear", "\n",
              "Sementes de milho por hectare: ", "{:.1f}".format(sementes_milho_hectare))
        
        #calculo de sementes de feijao por hectare
        peso_semente_feijao = 27.4
        taxa_semeadura_feijao = 12
        espacamento_feijao = 0.45
        taxa_germinacao_feijao = 85
        sementes_feijao_hectare = ((hectare * peso_semente_feijao * taxa_semeadura_feijao) / (espacamento_feijao * taxa_germinacao_feijao)) * 1.1
        print("Feijao:", "\n",
              "Peso de 100g de semente: ", peso_semente_feijao, " gramas" ,"\n",
              "Taxa de semeadura: ", taxa_semeadura_feijao, " sementes/metro linear", "\n",
              "Espaçamento: ", espacamento_feijao, " metros", "\n",
              "Sementes de feijao por hectare: ", "{:.1f}".format(sementes_feijao_hectare), " quilo/hectare")

        #quantos hectares serao usados para milho e feijao
        print("Você possui ", hectare_por_area , " hectares, quantos hectares gostaria de usar para plantar milho?")
        milho = float(input())
        hectare_restante = hectare_por_area - milho
        print("Você possui ", hectare_restante, " hectares restantes, quanto gostaria de usar para plantar feijao?")
        feijao = float(input())

        #calculo de quantas sementes precisara
        semente_milho = sementes_feijao_hectare * milho 
        semente_feijao = sementes_feijao_hectare * feijao
        print("Voce precisará de ", "{:.1f}".format(semente_milho), " sementes de milho e ", "{:.1f}".format(semente_feijao), " quilos de feijao ")
        cv2.putText(img, "Milho: " + str(milho) + " hectares", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        cv2.putText(img, "Sementes: " + str("{:.1f}".format(semente_milho)), (50,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        cv2.putText(img, "Feijao: " + str(feijao) + " hectares", (50,250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
        cv2.putText(img, "Quilos de semente: " + str("{:.1f}".format(semente_feijao)), (50,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

plt.imshow(img)
plt.show()