#M-A-Sc#

 
import face_recognition
import argparse


# Argumente parsen
parser = argparse.ArgumentParser()
parser.add_argument("--sample", required=True, help="Pfad zur Sample-Datei")
parser.add_argument("--template", required=True, help="Pfad zur Template-Datei")
args = parser.parse_args()

# Einlesen der Bilder
sample_image = face_recognition.load_image_file(args.sample)
template_image = face_recognition.load_image_file(args.template)

# Auslesen der biometrischen Merkmale
sample_encoding = face_recognition.face_encodings(sample_image)[0]
template_encoding = face_recognition.face_encodings(template_image)[0]

# Vergleich der Merkmale
results = face_recognition.compare_faces([sample_encoding], template_encoding)

# Ergebnis
if results[0]:
    print("Die Bilder matchen (accept)")
else:
    print("Die Bilder matchen nicht (reject)")
