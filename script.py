import cv2
from cvzone.HandTrackingModule import HandDetector

# Inicia a WebCam
webcam = cv2.VideoCapture(0)

# Inicia o rastreador de mõos
detector = HandDetector(detectionCon=0.7, maxHands=2)

while True:
    # Lê a imagem da webcam
    success, img = webcam.read()
    if not success:
        print("Erro ao ler a imagem")
        continue

    # Detecta as mãos no quadro
    hands, imgs = detector.findHands(img)

    # Mostra o quadro com as marcações
    cv2.imshow("Quadro", imgs)

    # Encerra a aplicação quando qualquer tecla é presisonada
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libera a câmera e fecha as janelas
webcam.release()
cv2.destroyAllWindows()