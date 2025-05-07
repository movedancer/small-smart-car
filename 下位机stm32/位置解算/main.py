import numpy as np
import math
from math import pi
from matplotlib import pyplot as plt
# 车轮半径
r_a = 1
r_b = 1

# 中轴长度
axis_len = 5

# 车轮速度
s_a = np.linspace(0, 20, 20)
s_b = np.linspace(0,15,20)

# 时间 
t = np.linspace(0,10,20)

# 以a轮起始值为原点

# 位置
location = [(axis_len/2, 0.)]

# 车体偏转角度 初始为90°
angle: float = 90.

# 计算偏转角
def deflection_angle(v1: float, v2: float, t: float):
    w = (v2 - v1) / axis_len
    theta = w * t
    return theta

def delta_dist(v1: float, v2: float, delta_angle: float):
    r = (axis_len * v1) / abs(v2 -v1) + axis_len / 2
    dist = ((math.sin(abs(delta_angle) / 2)) * r) * 2
    delta_x = math.cos((((angle + (delta_angle / 2)) % 360)/360) * 2 * pi) * dist
    delta_y = math.sin((((angle + (delta_angle / 2)) % 360)/360) * 2 * pi) * dist
    
    return (delta_x, delta_y) 



last_t = t[0]
for (sa, sb, t) in zip(s_a, s_b, t):
    delta_t = t - last_t
    if(t <= 0):
        last_t = 0
        continue
    if(sa == sb):
        (_x, _y) = location[len(location) - 1]
        (x_, y_) = (_x + delta_t * sa * math.cos(((angle % 360) / 360) * 2 * pi), _y + delta_t * sa * math.sin(((angle % 360) / 360) * 2 * pi))
        location.append((x_, y_))
        last_t = t
    else:
        delta_angle = deflection_angle(sa, sb, delta_t)
        (_x, _y) = location[len(location) - 1]
        (tmp1, tmp2) = delta_dist(sa, sb, delta_angle)
        (x_, y_) = (_x + tmp1, _y + tmp2)
        location.append((x_, y_))
        last_t = t
        angle = angle + delta_angle

# 解包坐标点列表
x, y = zip(*location)

# 绘制坐标点
plt.scatter(x, y)

# 可选：添加标题和轴标签
plt.title('Coordinate Points')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# 显示网格
plt.grid(True)

# 显示图表
plt.show()






