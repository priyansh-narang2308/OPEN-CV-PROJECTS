# GUI Application Pencil Sketch from Photo

# Using streamlit,numpy,opencv and Pil(imaging library)

import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2 as cv


def convert_to_watercolorsketch(img):
    img_1 = cv.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.8)
    img_water_color = cv.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return img_water_color


def covert_to_pencil_sketch(img):
    img_pencil_sketch, pencil_color_sketch = cv.pencilSketch(
        img, sigma_s=50, sigma_r=0.07, shade_factor=0.0835
    )
    return img_pencil_sketch


def load_image(imag):
    img = Image.open(imag)
    return img


def main():

    st.title("CONVERT IMAGE TO SKETCH")
    st.write(
        "Application to convert your normal image to a WATER COLOR SKETCH or PENCIL SKETCH"
    )
    st.subheader("Please Upload The Image")

    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        opt = st.selectbox("How to convert the Image", ["Water Color", "Pencil Sketch"])

        if opt == "Water Color":
            image = Image.open(image_file)
            final_sketch = convert_to_watercolorsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_image(image_file), width=250)

            with col2:
                st.header("Water Color Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()  # In memory Buffer
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolorsketch.png",
                    mime="image/png",
                )

        if opt == "Pencil Sketch":
            image = Image.open(image_file)
            final_sketch = covert_to_pencil_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)

            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(load_image(image_file), width=250)

            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                img = im_pil
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name=".png",
                    mime="image/png",  # Format of the file
                )


if __name__ == "__main__":
    main()


# python -m streamlit run image_conversion.py to run it in an local host
