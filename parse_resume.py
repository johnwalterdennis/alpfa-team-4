from PyPDF2 import PdfReader

def parse_resume(filepath):
    with open(filepath, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    ##for page in range(len(reader.pages)):
        #     text += reader.pages[page_num].extract_text()
        # return text