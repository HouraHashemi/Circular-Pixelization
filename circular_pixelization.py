## remove background

from PIL import Image, ImageDraw, ImageStat, ImageEnhance


class circular_pixelization():

    def is_pixel_bright(self, pixel, brightness_threshold):
        # Calculate the brightness of the pixel using the formula: 0.299*R + 0.587*G + 0.114*B
        brightness = 0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2]
        return brightness > brightness_threshold

    def convert_to_circle_art(self, input_path, output_path, circle_radius, brightness_threshold):
        # Open the image
        img = Image.open(input_path)

        # Create a blank image with the same size as the original, with an alpha channel
        circle_art = Image.new('RGBA', img.size, (255, 255, 255, 0))

        # Create a drawing object
        draw = ImageDraw.Draw(circle_art)

        # Iterate through each pixel and draw a circle if it is not too bright
        for x in range(0, img.width, circle_radius):
            for y in range(0, img.height, circle_radius):
                # Get the color of the pixel in the original image
                pixel_color = img.getpixel((x, y))

                # Check if the pixel is not too bright
                if not self.is_pixel_bright(pixel_color, brightness_threshold):
                    # Draw a circle at the current position with the pixel color
                    draw.ellipse(
                        [(x, y), (x + circle_radius, y + circle_radius)],
                        fill=pixel_color + (255,)  # Set alpha channel to 255 (fully opaque)
                    )

        # Save the circle art image
        circle_art.save(output_path)

if __name__ == "__main__":
    input_image_path = "./images/44.jpg"
    output_image_path = "./results/1.png"
    circle_radius = 8  # Adjust the circle radius according to your preference
    brightness_threshold = 100  # Adjust the brightness threshold according to your preference

    cp = circular_pixelization()
    cp.convert_to_circle_art(input_image_path, output_image_path, circle_radius, brightness_threshold)

    

