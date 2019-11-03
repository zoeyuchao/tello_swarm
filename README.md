# Tello_Swarm

基于tello的ap模式开发的多无人机控制。

## 1. 安装

```
pip install numpy opencv-python

cd tello_swarm/h264decoder 
mkdir build && cd build 
cmake .. 
make -j 
cp libh264decoder.so ../../
```

## 2. 使用

1. 在跑多机之前一定要先把每一个无人机的ap模式配置成一样的，之后重启飞机；

2. 将所有无人机连接到同一个路由器，并查看每个无人机的 ip 地址；

3. 修改 `tello_mul.py` 中如下代码中的 `tello_ip='your_ip'`

   ```python
   drone1= tello.Tello('', 8888,tello_ip='192.168.43.8')
   ```

4. 打开终端

   ```shell
   python tello_mul.py
   ```

## 3. Tips

1. ap模式下没办法获取多无人机的状态信息和图像信息，这个程序只是多无人机的开环控制
2. 可以引入optitrack做闭环控制




