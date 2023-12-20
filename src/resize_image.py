from PIL import Image
import io


def get_current_image_size(image):
    with io.BytesIO() as buffer:
        image.save(buffer, format='JPEG')
        return len(buffer.getvalue())

def resize_image(image_path, max_size_mb=4):

    image = Image.open(image_path)
    max_size_bytes = max_size_mb * 1024 * 1024

    quality = 95  # Starting quality
    while get_current_image_size(image) > max_size_bytes:
        # Reduce quality or size
        quality -= 5
        if quality <= 65:
            # If quality drops too much, start resizing
            width, height = image.size
            image = image.resize((width - 50, height - 50))

        # Save the image to check its size
        with io.BytesIO() as buffer:
            image.save(buffer, format='JPEG', quality=quality)

        if quality <= 10 or (image.width < 100 and image.height < 100):
            raise Exception("Unable to reduce image size without extreme quality loss.")

    # Final save
    final_buffer = io.BytesIO()
    image.save(final_buffer, format='PNG', quality=quality)
    final_buffer.seek(0)
    return final_buffer