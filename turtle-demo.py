import turtle as tu
import pickle, numpy as np

tu.setup(width=1.0,height=1.0)
tu.speed(4)  
tu.width(10)
tu.color('red')

screenx_offset = -tu.window_width()/2
screeny_offset = 0
ncol = 3      # 一行最多存放的汉字数量
nrow = 2      # 一行最多存放的汉字数量

model_file = 'characters.pkl'
read_mode = 'rb'
with open(model_file,read_mode) as f:
    characters = pickle.load(f)
ch_hanzi = '罗老弟你来了'
boxy_offset = 124   # 每个汉字的默认坐标范围为：[0,1024],[-124,900]
x_offset = 1024     # 按行排列每个汉字需要的水平偏移
y_offset = 1024      # 按列排列每个汉字需要的竖直偏移
scale = min(tu.window_width()/(ncol * x_offset), tu.window_height()/(nrow * y_offset))

for i,ch_hz in enumerate(ch_hanzi):
    if ch_hz not in characters:
        print('{} 不是汉字，跳过绘制'.format(ch_hz))
        continue
    # 画实心笔顺
    medians = characters[ch_hz]['medians']
    for median in medians:
        array = np.array(median)
        array[:,0] = (array[:,0] + x_offset*int(i%ncol))*scale + screenx_offset
        array[:,1] = (array[:,1] + boxy_offset - y_offset*int(i//ncol))*scale - screeny_offset
        tu.penup()
        tu.goto(array[0,0],array[0,1])
        tu.pendown()
        for j in range(array.shape[0]):
            tu.goto(array[j,0],array[j,1])
# tu.done()
tu.exitonclick()

