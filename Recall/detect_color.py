from __future__ import division
from cv_bridge import CvBridge
import cv2
import numpy as np
import math
import logging
@nrp.MapVariable("red_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("blue_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("violet_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("violet_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_left",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("green_right",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("brown_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("brown_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("black_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("black_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("indigo_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("indigo_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("cyan_left", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("cyan_right", initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("red",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("blue",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("black",initial_value = 0,scope = nrp.GLOBAL)
@nrp.MapVariable("green",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("violet",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("yellow",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("brown",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("cyan",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapVariable("indigo",initial_value = 0, scope = nrp.GLOBAL)
@nrp.MapRobotSubscriber("Camera", Topic("/husky/husky/camera", sensor_msgs.msg.Image))
@nrp.Robot2Neuron()
def detect_color (t,Camera,red_left,red_right,blue_left,blue_right,green_left,green_right,brown_left,brown_right,black_left,black_right,violet_left,violet_right,yellow_left,yellow_right,cyan_left,cyan_right,indigo_left,indigo_right,red,blue,black,green,violet,yellow,cyan,indigo,brown):
        
        bridge = CvBridge()
        image = Camera.value
        cv_image = bridge.imgmsg_to_cv2(image,"bgr8")
        hsv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
        
        def detectcolorred(cv_image,hsv_image):
            lower_red = np.array([0, 30, 30])
            upper_red = np.array([0, 255, 255])
            mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
            image_size= (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                red_left.value = cv2.countNonZero(mask_red[:, :half])
                red_right.value = cv2.countNonZero(mask_red[:, half:])
                red_left.value = 2 * (red_left.value / image_size)
                red_right.value = 2 * (red_right.value / image_size)
                red.value = red_left.value + red_right.value
                #clientLogger.info("Red left e Red right", red_left.value, red_right.value)
                return red
                
        
        def detectcolorgreen(cv_image,hsv_image):
            lower_green = np.array([50, 30, 30])
            upper_green = np.array([70, 255, 255])
            # Create a mask where every non red pixel will be a Zero.
            mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                # Get the number of red pixels in the image.
                green_left.value = cv2.countNonZero(mask_green[:, :half])
                green_right.value = cv2.countNonZero(mask_green[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                green_left.value = 2 * (green_left.value / image_size)
                green_right.value = 2 * (green_right.value / image_size)
                green.value = green_left.value + green_right.value
                #clientLogger.info("Green left e Green right", green_left.value, green_right.value)
                return green
        
        def detectcolorblue(cv_image,hsv_image):
            lower_blue = np.array([115, 100, 20])
            upper_blue = np.array([125, 255, 255])
            #Create a mask where every non red pixel will be a Zero.
            mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                # Get the number of red pixels in the image.
                blue_left.value = cv2.countNonZero(mask_blue[:, :half])
                blue_right.value = cv2.countNonZero(mask_blue[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                blue_left.value = 2 * (blue_left.value / image_size)
                blue_right.value = 2 * (blue_right.value / image_size)
                blue.value = blue_left.value + blue_right.value
                #clientLogger.info("Blue left e blue right", blue_left.value, blue_right.value)
                return blue
            
        def detectcolorbrown(cv_image,hsv_image):
            lower_brown = np.array([10,100, 20])
            upper_brown = np.array([20, 255, 200])
            # Create a mask where every non red pixel will be a Zero.
            mask_brown = cv2.inRange(hsv_image, lower_brown, upper_brown)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                # Get the number of red pixels in the image.
                brown_left.value = cv2.countNonZero(mask_brown[:, :half])
                brown_right.value = cv2.countNonZero(mask_brown[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                brown_left.value = 2 * (brown_left.value / image_size)
                brown_right.value = 2 * (brown_right.value / image_size)
                brown.value = brown_left.value + brown_right.value
                return brown
        
        def detectcolorblack(cv_image,hsv_image):
            lower_black = np.array([0,0,0])
            upper_black = np.array([0,0,0])
            # Create a mask where every non red pixel will be a Zero.
            mask_black = cv2.inRange(hsv_image, lower_black, upper_black)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                # Get the number of red pixels in the image.
                black_left.value = cv2.countNonZero(mask_black[:, :half])
                black_right.value = cv2.countNonZero(mask_black[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                black_left.value = 2 * (black_left.value / image_size)
                black_right.value = 2 * (black_right.value / image_size)
                black.value = black_left.value + black_right.value
                #clientLogger.info("Black left e Black right", black_left.value, black_right.value)
                return black
                
        def detectcolorpurple(cv_image,hsv_image):
            lower_violet = np.array([150, 200, 20])
            upper_violet = np.array([165, 255, 255])
            #Create a mask where every non red pixel will be a Zero.
            mask_violet = cv2.inRange(hsv_image, lower_violet, upper_violet)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                #Get the number of red pixels in the image.
                violet_left.value = cv2.countNonZero(mask_violet[:, :half])
                violet_right.value = cv2.countNonZero(mask_violet[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                violet_left.value = 2 * (violet_left.value / image_size)
                violet_right.value = 2 * (violet_right.value / image_size)
                violet.value = violet_left.value + violet_right.value
                return violet
        
        def detectcoloryellow(cv_image,hsv_image):
            lower_yellow = np.array([25, 50, 50])
            upper_yellow = np.array([35, 255, 255])
            #Create a mask where every non red pixel will be a Zero.
            mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                #Get the number of red pixels in the image.
                yellow_left.value = cv2.countNonZero(mask_yellow[:, :half])
                yellow_right.value = cv2.countNonZero(mask_yellow[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                yellow_left.value = 2 * (yellow_left.value / image_size)
                yellow_right.value = 2 * (yellow_right.value / image_size)
                yellow.value = yellow_left.value + yellow_right.value
                return yellow
         
        def detectcolorcyan(cv_image,hsv_image):
            lower_cyan = np.array([85, 100, 30])
            upper_cyan = np.array([90, 255, 255])
            #Create a mask where every non red pixel will be a Zero.
            mask_cyan = cv2.inRange(hsv_image, lower_cyan, upper_cyan)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                #Get the number of red pixels in the image.
                cyan_left.value = cv2.countNonZero(mask_cyan[:, :half])
                cyan_right.value = cv2.countNonZero(mask_cyan[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                cyan_left.value = 2 * (cyan_left.value / image_size)
                cyan_right.value = 2 * (cyan_right.value / image_size)
                cyan.value = cyan_left.value + cyan_right.value
                #clientLogger.info("Cyan left & Cyan right", turquoise_left.value, turquoise_right.value)
                return cyan
        
        def detectcolorindigo(cv_image,hsv_image):
            lower_indigo = np.array([135, 200, 20])
            upper_indigo = np.array([145, 255, 255])
            #Create a mask where every non red pixel will be a Zero.
            mask_indigo = cv2.inRange(hsv_image, lower_indigo, upper_indigo)
            image_size = (cv_image.shape[0] * cv_image.shape[1])
            if (image_size > 0):
                half = cv_image.shape[1] // 2
                #Get the number of red pixels in the image.
                indigo_left.value = cv2.countNonZero(mask_indigo[:, :half])
                indigo_right.value = cv2.countNonZero(mask_indigo[:, half:])
                # We have to mutiply the rate by two since it is for an half image only.
                indigo_left.value = 2 * (indigo_left.value / image_size)
                indigo_right.value = 2 * (indigo_right.value / image_size)
                indigo.value = indigo_left.value + indigo_right.value
                return indigo
        
        yellow = detectcoloryellow(cv_image,hsv_image)
        blue = detectcolorblue(cv_image,hsv_image)
        red = detectcolorred(cv_image,hsv_image)
        black = detectcolorblack(cv_image,hsv_image)
        green = detectcolorgreen(cv_image,hsv_image)
        cyan = detectcolorcyan(cv_image,hsv_image)
        violet = detectcolorpurple(cv_image,hsv_image)
        brown = detectcolorbrown(cv_image,hsv_image)
        indigo = detectcolorindigo(cv_image,hsv_image)