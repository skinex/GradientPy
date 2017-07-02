# GradientPy
Program for applying a gradient to an image using libraries: opencv 3.2, pyqt5. Python version 3.6
In this program, there are two options for applying a gradient, namely using standard opencv color maps(like JET, HSV, COOL,RAINBOW ) and custom color maps.
# View application
![alt text](https://github.com/skinex/GradientPy/blob/master/grad.png)
<br/>
# Implementation, custom color maps:
SingleChanell
```python
lst = np.zeros((256, 1, 3), dtype=np.uint8)
for i in range(256):
    for j in range(3):
       lst[i,0,j] = 255-i
       res_img=cv2.LUT(img,lst)
       cv2.imwrite("gradient.jpg", res_img)
       pixmap = QPixmap("gradient.jpg")
       self.ui.label_2.setPixmap(pixmap)
       self.ui.groupBox_2.setVisible(True)
```
MultiChanell
```python
lst1 = np.zeros((256, 1, 3), dtype=np.uint8)
for i in range(256):
    lst1[i,0,0] = 255-i
for i in range(256):
    lst1[i,0,1] = abs(50-i)
for i in range(256):
    lst1[i,0,2] = 255 - (i // 4)
res_img = cv2.LUT(img,lst1)
cv2.imwrite("gradient.jpg", res_img)
pixmap = QPixmap("gradient.jpg")
self.ui.label_2.setPixmap(pixmap)
self.ui.groupBox_2.setVisible(True)
```
# Implementation standart opencv color maps
```python
img = cv2.imread(self.fname)
res_img = cv2.applyColorMap(img,cv2.COLORMAP_JET)
cv2.imwrite("gradient.jpg",res_img)
pixmap = QPixmap("gradient.jpg")
self.ui.label_2.setPixmap(pixmap)
self.ui.groupBox_2.setVisible(True)
```
