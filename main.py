import matplotlib.pyplot as plt
from matplotlib import font_manager

font_path = "fonts/EISHStest2.ttf"
font_prop = font_manager.FontProperties(fname=font_path)

plt.figure(figsize=(4,2))

# Stack glyphs manually
plt.text(0.1, 0.5, "\uE101", fontproperties=font_prop, fontsize=64)
plt.text(0.1, 0.5, "\uE102", fontproperties=font_prop, fontsize=64)
plt.text(0.2, 0.5, "\uE100", fontproperties=font_prop, fontsize=64)  # smaller top mark

plt.axis('off')
plt.show()
