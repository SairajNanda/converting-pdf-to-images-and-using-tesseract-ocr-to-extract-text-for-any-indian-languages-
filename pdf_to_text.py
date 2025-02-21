from pdf2image import convert_from_path


def convert_pdf(pdf_path,save_directory,res=400):
    pages = convert_from_path(pdf_path,res)

    name_with_extension = pdf_path.rsplit('/')[-1]
    name = name_with_extension.rsplit('.')[0]

    for idx,page in enumerate(pages):
        page.save(f'{save_directory}/{name}_{idx}.png','PNG')

convert_pdf('/home/speech/Desktop/bodo2.pdf', '/home/speech/Desktop/bodo_scraped/bodopdf2image')



# sudo apt install tesseract-ocr
# sudo apt-get install tesseract-ocr*
# tesseract ~/path/image.png - -l ben
