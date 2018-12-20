import cv2, time
from PIL import Image
from check_speed_direction import check2
from face_detection import read_image
first_frame=None
status_list=[None,None]
textfile=open("vertical_record.txt","w")
textfile.close()
textfile=open("horizontal_record.txt","w")
textfile.close()
textfile=open("count.txt","w")
textfile.close()
#times=[]
#df=pandas.DataFrame(columns=["Start","End"])
img_counter=0
#t=0
video=cv2.VideoCapture(0)
count=0
sec = int(round(time.time()))
while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    sec2=int(round(time.time()))

    if first_frame is None:
        first_frame=gray
        continue

    #delta_frame=cv2.absdiff(first_frame,gray)
    #thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)


    #cv2.imshow("Color Frame-ESC to close ",frame)

    key=cv2.waitKey(1)
    #t=t+1

    if key%256 == 27:
      #ESC
      print("closing")
      break

    if img_counter <10 and (sec2-sec)==3:  #SPACE
        img_ctr=str(img_counter)

        img_name="test"+img_ctr+".jpg".format(img_counter)
        sec=sec2
        textfile=open("count.txt","w")
        textfile.write(img_ctr)
        textfile.close()
        cv2.imwrite(img_name,frame)
        imk=Image.open(img_name)
        imk.load()
        imk.show()
        print("written".format(img_name))
        img_counter+=1
        read_image(img_name)
        check2()
video.release()
cv2.destroyAllWindows()
