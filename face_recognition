#M-A-Sc


import cv2

# Bildpfad
image_path = "example_image.jpg"

# Lade Bild
image = cv2.imread(image_path)

# Zeige Originalbild an und warte auf Tastendruck
cv2.imshow("Originalbild", image)
cv2.waitKey(0)

# Konvertiere das Bild in Graustufen
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialisiere den Gesichtserkennungs-Algorithmus
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Gesichtserkennung auf dem Graustufenbild durchführen
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

# Zeichne Rechteck um das erkannte Gesicht
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)    

# Zeige das Bild mit Gesichtserkennung an
cv2.imshow("Gesichtserkennung", image)

# Speichere die detektierten Gesichtsregionen als Bilddateien
for i, (x, y, w, h) in enumerate(faces):
    face_image = image[y:y+h, x:x+w]
    cv2.imwrite(f"face_{i}.jpg", face_image)    

# Warte auf Tastendruck zum Schließen
cv2.waitKey(0)

# Schließe das Fenster
cv2.destroyAllWindows()
