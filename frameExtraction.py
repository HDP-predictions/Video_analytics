import cv2
import os
import csv
import pandas as pd
from datetime import timedelta


# In[2]:

pathExcel = '/part4/fps10Videos/'
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
data = pd.read_excel(pathExcel+'video_tags (13).xlsx')


# In[3]:


data


# In[4]:


data=data.astype(str)


# In[5]:


data.dtypes


# In[ ]:


pathPatting = '/part4/fps15Videos/data/patting/'
pathFeeding = '/part4/fps15Videos/data/feeding/'
pathDiaperChange = '/part4/fps15Videos/data/diaper_change/'
path = ''


#Count for frames
frameCount = 0
#labelFrameCount = 0

uhidIdx = 0
videoIdx = 1
totalDuration = 2
clipStartFrom = 3
clipEndAt = 4
#clipDuration = 6
label = 6
count = 1

#Set path for frames
#pathPatting = './train/patting/'
#pathFeeding = './train/feeding/'
#pathDiaperChange = './train/diaper change/'
#path = ''

#Count for frames
frameCount = 0
#labelFrameCount = 0

#For every row in excel sheet
for row in range(len(data)):
    try:
         if((data.iloc[row,label] =='Diaper_change') or (data.iloc[row,label] =='Feeding') or (data.iloc[row,label] =='Patting')) :
           #Read videos from excel sheet
           cap = cv2.VideoCapture('/part4/fps15Videos/motinagar/'+str(data.iloc[row,videoIdx]))
           #fps = cap.get(cv2.CAP_PROP_FPS)
           fps = 15

           #Frames to be extracted
           framesToExtract = 120

           #Total Frame count in video
           length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
           #cap.set(cv2.cv.CV_CAP_PROP_FPS, 15)
           print('(',count,') ',length, 'Frames in ', data.iloc[row,videoIdx], 'video with label ', data.iloc[row,label])

           ####calculate start video frame count############
           videoFrameStartTime = data.iloc[row,clipStartFrom]
           print(data.iloc[row,label],' clip starts from ', videoFrameStartTime)
           startString = videoFrameStartTime.split('.')

           beforeDecStrStart = (startString[0])
           afterDecStrStart = (startString[1])
           beforeDecStart = int(startString[0])
           if(len(startString[1]) < 2):
               afterDecStart = 10*int(startString[1])
           else:
               afterDecStart = int(startString[1])
           print(beforeDecStart, afterDecStart)

           FrameStartTime = (beforeDecStart*60 + afterDecStart) * fps;
           print('start frame: ', FrameStartTime)

           ####calculate end video frame count############
           videoFrameEndTime = data.iloc[row,clipEndAt]
           print(data.iloc[row,label],' clip End at ', videoFrameEndTime)

           endString = videoFrameEndTime.split('.')

           beforeDecStrEnd = (endString[0])
           afterDecStrEnd = (endString[1])
           beforeDecEnd = int(endString[0])

           if(len(endString[1]) < 2):
               afterDecEnd = 10*int(endString[1])
           else:
               afterDecEnd = int(endString[1])


           FrameEndTime = (beforeDecEnd*60 + afterDecEnd) * fps;
           print('oiginal end frame: ', FrameEndTime)

           frameDuration = FrameEndTime - FrameStartTime
           print(frameDuration)

           #If frame count is more than required frame then set them accordingly


           #Set frame paths
           print('new end frame: ', FrameEndTime)
           if(data.iloc[row, label] == 'Patting'):
               path = pathPatting
           elif(data.iloc[row, label] == 'Diaper_change'):
               path = pathDiaperChange
           elif(data.iloc[row, label] == 'Feeding'):
               path = pathFeeding


           print(path)

           #Extract frames and store them in correspondig paths
           c = 0
           temp = 0
           while( temp < length ):
               ret, frame = cap.read()

               if ((ret == False) ):
                  break
               if(( temp >= FrameStartTime and temp <= FrameEndTime and c < 120)):
                  cv2.imwrite(os.path.join(path, str(data['UHID'].iloc[row])+"_"+str(frameDuration)+"_"+str(c)+"_"+str(data['Video (Title)'].iloc[row])+"_"+str(data['Label'].iloc[row])+"_"+str(frameCount) + '.jpg'), cv2.resize(frame,(720,480), interpolation = cv2.INTER_AREA))
                  frameCount+=1
                  c+=1

               temp+=1

           print('Total frames extracted in this label: ', c)
           print('Total frameCount: ', frameCount)
           row+=1
           count+=1
    except:
        continue

data = pd.read_excel(pathExcel+'video_tags (13).xlsx', sheet_name='KR-video_procedures')


#For every row in excel sheet
for row in range(len(data)):
    try:
         if((data.iloc[row,label] =='Diaper_change') or (data.iloc[row,label] =='Feeding') or (data.iloc[row,label] =='Patting')) :
           #Read videos from excel sheet
           cap = cv2.VideoCapture('/part4/fps15Videos/kalawati/'+str(data.iloc[row,videoIdx]))
           #fps = cap.get(cv2.CAP_PROP_FPS)
           fps = 15

           #Frames to be extracted
           framesToExtract = 120

           #Total Frame count in video
           length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
           #cap.set(cv2.cv.CV_CAP_PROP_FPS, 15)
           print('(',count,') ',length, 'Frames in ', data.iloc[row,videoIdx], 'video with label ', data.iloc[row,label])

           ####calculate start video frame count############
           videoFrameStartTime = data.iloc[row,clipStartFrom]
           print(data.iloc[row,label],' clip starts from ', videoFrameStartTime)
           startString = videoFrameStartTime.split('.')

           beforeDecStrStart = (startString[0])
           afterDecStrStart = (startString[1])
           beforeDecStart = int(startString[0])
           if(len(startString[1]) < 2):
               afterDecStart = 10*int(startString[1])
           else:
               afterDecStart = int(startString[1])
           print(beforeDecStart, afterDecStart)

           FrameStartTime = (beforeDecStart*60 + afterDecStart) * fps;
           print('start frame: ', FrameStartTime)

           ####calculate end video frame count############
           videoFrameEndTime = data.iloc[row,clipEndAt]
           print(data.iloc[row,label],' clip End at ', videoFrameEndTime)

           endString = videoFrameEndTime.split('.')

           beforeDecStrEnd = (endString[0])
           afterDecStrEnd = (endString[1])
           beforeDecEnd = int(endString[0])

           if(len(endString[1]) < 2):
               afterDecEnd = 10*int(endString[1])
           else:
               afterDecEnd = int(endString[1])


           FrameEndTime = (beforeDecEnd*60 + afterDecEnd) * fps;
           print('oiginal end frame: ', FrameEndTime)

           frameDuration = FrameEndTime - FrameStartTime
           print(frameDuration)

           #If frame count is more than required frame then set them accordingly


           #Set frame paths
           print('new end frame: ', FrameEndTime)
           if(data.iloc[row, label] == 'Patting'):
               path = pathPatting
           elif(data.iloc[row, label] == 'Diaper_change'):
               path = pathDiaperChange
           elif(data.iloc[row, label] == 'Feeding'):
               path = pathFeeding


           print(path)

           #Extract frames and store them in correspondig paths
           c = 0
           temp = 0
           while( temp < length ):
               ret, frame = cap.read()

               if ((ret == False) ):
                  break
               if(( temp >= FrameStartTime and temp <= FrameEndTime and c < 120)):
                  cv2.imwrite(os.path.join(path, str(data['UHID'].iloc[row])+"_"+str(frameDuration)+"_"+str(c)+"_"+str(data['Video (Title)'].iloc[row])+"_"+str(data['Label'].iloc[row])+"_"+str(frameCount) + '.jpg'), cv2.resize(frame,(720,480), interpolation = cv2.INTER_AREA))
                  frameCount+=1
                  c+=1

               temp+=1

           print('Total frames extracted in this label: ', c)
           print('Total frameCount: ', frameCount)
           row+=1
           count+=1
    except:
        continue

