import os
from PIL import Image, ImageDraw, ImageFont

# Define colors (Note: These are placeholders as ASCII colors don't apply to images)
YELLOW = (255, 255, 0)  # RGB for yellow
BROWN = (139, 69, 19)  # RGB for brown
BLACK = (0, 0, 0)  # RGB for text
DARK_GRAY = (50, 50, 50)  # RGB for dark gray background


def garden(sub_stage=0):
    base_frame = [
        "                  ",
        "                  ",
        "                  ",
        "                  ",
        "~~~~~~~~~~~~~~~~",
        "################",
        "################",
        "################",
        "################",
        "################"
    ]

    if sub_stage < 4:
        base_frame[sub_stage] = "                 (q*)".center(18)  # Center the art within the line
    elif sub_stage == 4:
        base_frame[4] = "~~~~~~(q*)~~~~~~"
    elif sub_stage == 5:
        base_frame[5] = "######(q*)######"
    elif sub_stage == 6:
        base_frame[6] = "######(q*)######"
    elif sub_stage == 7:
        base_frame[7] = "######(q*)######"

    return "\n".join(base_frame)


def save_frame_as_image(frame_number, text, output_folder='frames'):
    os.makedirs(output_folder, exist_ok=True)

    # Create a blank image with white background
    img = Image.new('RGB', (118, 180), color=DARK_GRAY)
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Draw the text on the image with appropriate colors
    y_offset = 20
    for line in text.split('\n'):
        color = BROWN if "####" in line or "~~~~" in line else BLACK
        if "(q*)" in line:
            color = YELLOW
        d.text((10, y_offset), line, fill=color, font=font)
        y_offset += 15

    img_path = os.path.join(output_folder, f'frame_{frame_number:02d}.png')
    img.save(img_path)
    print(f'Saved {img_path}')


def create_frames():
    for i in range(8):
        frame_text = garden(i)
        save_frame_as_image(i, frame_text)

    images = []
    frame_files = os.listdir("frames")
    for frame in frame_files:
        img = Image.open(f"frames/{frame}")
        images.append(img)

    images[0].save("strawberry.gif",
                   save_all=True,
                   append_images=images[1:],
                   duration=200,
                   loop=0)
    print("GIF created")

create_frames()
