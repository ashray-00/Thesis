import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

def load_img(name):
    path = "BG_dehazing/{}".format(name)
    im = plt.imread(path)
    return im

def offset_image(coord, name, ax):
    img = get_image(name)
    im = OffsetImage(img, zoom=0.72)
    im.image.axes = ax

    ab = AnnotationBbox(im, (coord, 0),  xybox=(0., -16.), frameon=False,
                        xycoords='data',  boxcoords="offset points", pad=0)

    ax.add_artist(ab)



# image_name = ["Valentine_" + str(d) + ".png" for d in range(193, 204)] 
# df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UCIQUE.csv')
# y1 = df.Blue_green_channels_dehazing_and_red_channel_correction[22:35].values.tolist()
# y2 = df.Color_Balance_and_fusion[22:35].values.tolist()
# y3 = df.Integrated_Color_Model[22:35].values.tolist()
# y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel[22:35].values.tolist()

# image_name = ["Valentine_" + str(d) + ".png" for d in range(193, 204)] 
# df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UIQM.csv')
# y1 = df.Blue_green_channels_dehazing_and_red_channel_correction[22:35].values.tolist()
# y2 = df.Color_Balance_and_fusion[22:35].values.tolist()
# y3 = df.Integrated_Color_Model[22:35].values.tolist()
# y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel[22:35].values.tolist()

# image_name = ["Valentine_" + str(d) + ".png" for d in range(124, 132)] 
# df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UCIQUE.csv')
# y1 = df.Blue_green_channels_dehazing_and_red_channel_correction[10:18].values.tolist()
# y2 = df.Color_Balance_and_fusion[10:18].values.tolist()
# y3 = df.Integrated_Color_Model[10:18].values.tolist()
# y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel[10:18].values.tolist()

image_name = ["Valentine_" + str(d) + ".png" for d in range(124, 132)] 
df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UIQM.csv')
y1 = df.Blue_green_channels_dehazing_and_red_channel_correction[10:18].values.tolist()
y2 = df.Color_Balance_and_fusion[10:18].values.tolist()
y3 = df.Integrated_Color_Model[10:18].values.tolist()
y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel[10:18].values.tolist()

# df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UCIQUE.csv')
# image_name = df.Images.values.tolist()
# y1 = df.Blue_green_channels_dehazing_and_red_channel_correction.values.tolist()
# y2 = df.Color_Balance_and_fusion.values.tolist()
# y3 = df.Integrated_Color_Model.values.tolist()
# y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel.values.tolist()

# df = pd.read_csv('../../Underwater-Image-Enhancements/Metric_Output/UIQM.csv')
# image_name = df.Images.values.tolist()
# y1 = df.Blue_green_channels_dehazing_and_red_channel_correction.values.tolist()
# y2 = df.Color_Balance_and_fusion.values.tolist()
# y3 = df.Integrated_Color_Model.values.tolist()
# y4 = df.Low_Complexity_Enhancement_Based_on_Dark_Channel.values.tolist()

fig, ax = plt.subplots(figsize=(8.2,7.4))
# ax.bar(range(len(image_name)), ran, width=0.5,align="center")
ax.set_xticks(range(1,len(image_name) + 1))
ax.plot(range(1, len(image_name) + 1),
        y1,
        marker = 'o',
        label='Blue-Green channels dehazing and Red channel correction')
ax.plot(range(1, len(image_name) + 1),
        y2,
        marker = 'o',
        label = 'Color Balance and Fusion')
ax.plot(range(1, len(image_name) + 1),
        y3,
        marker = 'o',
        label = 'Integrated Color Model')
ax.plot(range(1, len(image_name) + 1),
        y4,
        marker = 'o',
        label = 'Low Complexity Enhancement based on Dark Channel Prior')
# ax.set_ylabel('UCIQE')
ax.set_ylabel('UIQM')
ax.set_xlabel('Images')
# ax.set_xticks(range(len(image_name)))
# ax.tick_params(axis='x', which='major', pad=26)
# for i, c in enumerate(image_name):
#     offset_image(i, c, ax)
# ax.set(title = "Average Monthly Precipitation\nBoulder, CO",
#        xlabel = "Month",
#        ylabel = "Precipitation\n(inches)")

box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.075),
          fancybox=True, shadow=True, ncol=1)

# plt.savefig('../line_graph_UCIQE.png')
# plt.savefig('../line_graph_UCIQE1.png')
# plt.savefig('../line_graph_UCIQE_1.png')

# plt.savefig('../line_graph_UIQM.png')
# plt.savefig('../line_graph_UIQM1.png')
plt.savefig('../line_graph_UIQM_1.png')
plt.clf()



# ax.set_xticklabels(countries)
# ax.tick_params(axis='x', which='major', pad=26)

# for i, c in enumerate(countries):
#     offset_image(i, c, ax)

# plt.show()
