import glob
from shutil import copyfile

emotions = ["anger", "contempt", "disgust", "fear", "happy", "neutral","sadness", "surprise"] #Define emotion order
participants = glob.glob("F:\Emotion-recognition-with-openCV-master\source_emotion\\*.txt") #Returns a list of all folders with participant numbers

for x in participants:
    part = "%s" %x[-4:] #store current participant number
    for sessions in glob.glob("%s\\*" %x): #Store list of sessions for current participant
        for files in glob.glob("%s\\*" %sessions):
            current_session = sessions[-3:]
            file = open(files, 'r')
            
            emotion = int(float(file.readline())) #emotions are encoded as a float, readline as float, then convert to integer.
            sourcefile_emotion = glob.glob("F:\Emotion-recognition-with-openCV-master\source_images\\%s\\%s\\*.png" %(part, current_session))[-1] #get path for last image in sequence, which contains the emotion
            sourcefile_neutral = glob.glob("F:\Emotion-recognition-with-openCV-master\source_images\\%s\\%s\\*.png" %(part, current_session))[0] #do same for neutral image
            
            dest_neut = "F:\Emotion-recognition-with-openCV-master\sorted_set\\neutral\\%s" %sourcefile_neutral[25:] #Generate path to put neutral image
            dest_emot = "F:\Emotion-recognition-with-openCV-master\sorted_set\\%s\\%s" %(emotions[emotion], sourcefile_emotion[25:]) #Do same for emotion containing image
            
            copyfile(sourcefile_neutral, dest_neut) #Copy file
            copyfile(sourcefile_emotion, dest_emot) #Copy file
