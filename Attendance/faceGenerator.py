import cv2
import sqlite3
# Import numpy for matrices calculations
import numpy as np
import database

i = 0
n = "null"
u = "null"
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM RegisteredUsers WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile = row
        #conn.close()
    return profile
