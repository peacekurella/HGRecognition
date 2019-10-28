import os
import shutil
import cv2

source_directory = "/home/prashanth/Desktop/HGRecognition/NUS-Hand-Posture-Dataset-II/NUS Hand Posture dataset-II"
count = 0 

for directory in os.listdir(source_directory):
    for photo in os.listdir(os.path.join(source_directory,directory)):
        if(os.path.splitext(photo)[1]==".jpg"):
            target_directory = "/home/prashanth/Desktop/HGRecognition/GestureData"
            desired_size = 224
            im_pth = os.path.join(os.path.join(source_directory,directory),photo)
            print(im_pth)
            im = cv2.imread(im_pth)
            old_size = im.shape[:2] # old_size is in (height, width) format

            ratio = float(desired_size)/max(old_size)
            new_size = tuple([int(x*ratio) for x in old_size])

            # new_size should be in (width, height) format

            im = cv2.resize(im, (new_size[1], new_size[0]))

            delta_w = desired_size - new_size[1]
            delta_h = desired_size - new_size[0]
            top, bottom = delta_h//2, delta_h-(delta_h//2)
            left, right = delta_w//2, delta_w-(delta_w//2)

            color = [0, 0, 0]
            new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
                value=color)
            
            if(count%7 == 0):
                target_directory = os.path.join(target_directory,"test")
            else:
                target_directory = os.path.join(target_directory,"train")
            
            
            if(photo[0:2]=="BG"):
                if not os.path.exists(os.path.join(target_directory,"BG")):
                    os.makedirs(os.path.join(target_directory,"BG"))
                cv2.imwrite(os.path.join(os.path.join(target_directory,"BG"),photo),new_im)
            else:
                if not os.path.exists(os.path.join(target_directory,photo[0:1].upper())):
                    os.makedirs(os.path.join(target_directory,photo[0:1].upper()))
                cv2.imwrite(os.path.join(os.path.join(target_directory,photo[0:1].upper()),photo),new_im)
            
            count = count + 1
