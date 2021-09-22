import PyPDF3


def pdf_read_pages(path):
    '''
        Getting pdf page numbers
        :param path:
        :return page number:
    '''
    try:
        with open(path, 'rb') as my_pdf:
            reader = PyPDF3.PdfFileReader(my_pdf)
            print(reader.numPages)
    except FileNotFoundError:
        print('File not found')


# combining pdfs
def pdf_combiner(pdf_list):
    '''
        combines pdfs
        :param pdf_list - takes in multiple file paths for pdfs:
        :return nothing, combines pdf:
    '''
    merger = PyPDF3.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')

# water marking
def watermarking_pdf(path, watermark_path):
    '''
        watermarking pdfs
        :param path => file path:
        :param watermark_path => watermark path:
        :return nothing, writes a new file with watermark:
    '''
    template = PyPDF3.PdfFileReader(open(path, 'rb'))
    watermark = PyPDF3.PdfFileReader(open(watermark_path, 'rb'))
    output = PyPDF3.PdfFileWriter()

    for i in range(template.getNumPages()):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked.pdf', 'wb') as file:
            output.write(file)