import cv2

img = cv2.imread("assets/solar-system.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(0,255,0))
cv2.putText(img,"Mercury",(60,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Venus",(100,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Earth",(140,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Mars",(180,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Jupiter",(220,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Saturn",(260,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Neptune",(300,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
cv2.putText(img,"Uranus",(320,300),cv2.FONT_HERSHEY_COMPLEX,fontScale=0.7,color=(255,0,0))
