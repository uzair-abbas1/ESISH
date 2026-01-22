
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Path to your font file
font_path = 'ESISHTest1.ttf'

# Load the font
prop = fm.FontProperties(fname=font_path)

# Create a figure
fig, ax = plt.subplots(figsize=(10, 4))

# Display text using your custom font
message = "Hello World!\nABCDEFGHIJKLMNOPQRSTUVWXYZ\nabcdefghijklmnopqrstuvwxyz"
ax.text(0.5, 0.5, message, fontproperties=prop, fontsize=24,
        ha='center', va='center')

# Remove axes
ax.axis('off')

# Show the result
plt.tight_layout()
plt.show()
