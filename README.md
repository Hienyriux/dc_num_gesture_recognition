# dc_num_gesture_recognition
Project of Nanjing University's Data Communication course in 2019 spring

本程序用于识别从1到5的数字手势   
基于Android和opencv-python开发   
由于是"数据通信"课的项目, 本程序并没有在手机端完成拍照和识别的全过程, 而是在手机端拍照后, 将照片上传至电脑端进行识别, 电脑端再将结果发送给手机端   
识别的判据是手指个数, 步骤为:  
1. 提取H通道(HSV颜色空间)图像
2. 中值滤波(去椒盐噪声)
3. 肤色分割(二值化)
4. 形态学运算(开操作, 即open)
5. 提取轮廓, 并选择最大轮廓
6. 计算轮廓点的矩和质心
7. 求轮廓点到质心距离的极大值点, 并做一些简单的筛选工作
8. 最后剩下的极大值点个数即为手指个数

### 运行提示: 请保证照相背景为白色; 电脑端请安装opencv-python

### 运行截图
***初始界面***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png)  
***识别1***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture1.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture1.png)  
***识别2***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture2.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture2.png)  
***识别3***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture3.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture3.png)  
***识别4***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture4.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture4.png)  
***识别5***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture5.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture5.png)  
***识别6, 失败***  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/gesture6.png)  
![https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture.png](https://github.com/Hienyriux/hienyriux_pics/blob/master/app_gesture6.png)  
