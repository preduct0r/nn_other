from pdf2image import convert_from_path
from pathlib import Path
def convert_pdf_to_images_pdf2image(pdf_path, output_folder, image_format='png', dpi=300, ii=0):
    """
    Converts each page of a PDF to an image file (PNG or JPEG).

    Args:
        pdf_path (str): The path to the PDF file.
        output_folder (str): The folder where a_images will be saved.
        image_format (str): The desired image format ('png' or 'jpeg').
        dpi (int): Dots per inch, affecting the resolution of the output image.
    """
    try:
        # Convert PDF to a list of PIL Image objects
        # You can specify DPI for resolution, e.g., dpi=300 for higher quality
        images = convert_from_path(pdf_path, dpi=dpi)

        for i, image in enumerate(images):
            # Construct the output file name
            if image_format.lower() == 'jpeg' or image_format.lower() == 'jpg':
                file_extension = 'jpg'
                save_format = 'JPEG'
            else:
                file_extension = 'png'
                save_format = 'PNG'
            
            output_path = f"{output_folder}/{ii}_page_{i + 1}.{file_extension}"
            
            # Save the image
            image.save(output_path, save_format)
            print(f"Saved: {output_path}")

        print(f"Successfully converted PDF to {image_format.upper()} images in '{output_folder}'")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure poppler is installed and in your PATH if you are on Windows.")
        print("You can download poppler for Windows from: https://github.com/oschwartz10612/poppler-windows/releases")


if __name__ == "__main__":
    import os
    base_output_dir = "/home/den/Documents/Nornikel/vllm/benchmark/jpg"
    input_pdf_folder = Path("/home/den/Documents/Nornikel/vllm/benchmark/original")

    if not os.path.exists(base_output_dir):
        os.makedirs(base_output_dir)
        print(f"Created base output directory: {base_output_dir}")

    for ii, pdf_file_path_obj in enumerate(input_pdf_folder.glob("*.pdf")):
        pdf_file_stem = pdf_file_path_obj.stem
        current_pdf_output_folder = Path(base_output_dir)
        
        if not os.path.exists(current_pdf_output_folder):
            os.makedirs(current_pdf_output_folder)
            print(f"Created output directory for {pdf_file_path_obj.name}: {current_pdf_output_folder}")

        my_pdf_file_str = str(pdf_file_path_obj)
        
        print(f"\nProcessing {my_pdf_file_str}...")
        
        # # Convert to PNG
        # print(f"Converting to PNG (output: {current_pdf_output_folder})...")
        # convert_pdf_to_images_pdf2image(my_pdf_file_str, str(current_pdf_output_folder), image_format='png', dpi=200, ii=ii)
        
        # Convert to JPEG
        print(f"Converting to JPEG (output: {current_pdf_output_folder})...")
        convert_pdf_to_images_pdf2image(my_pdf_file_str, str(current_pdf_output_folder), image_format='jpeg', dpi=200, ii=ii)

    print(f"\nAll PDF processing finished. Check subfolders in '{base_output_dir}'.")
