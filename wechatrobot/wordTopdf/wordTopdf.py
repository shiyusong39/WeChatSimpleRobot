# -*- coding: UTF-8 -*-
'''
Word 转 PDF
#pip install pywin32
'''

from win32com.client import gencache
from win32com.client import constants, gencache

def word_to_pdf(wordPath, pdfPath):
    """
    word转pdf
    :param wordPath: word文件路径
    :param pdfPath:  生成pdf文件路径
    """
    word = gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(wordPath, ReadOnly=1)
    doc.ExportAsFixedFormat(pdfPath,
                            constants.wdExportFormatPDF,
                            Item=constants.wdExportDocumentWithMarkup,
                            CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
    word.Quit(constants.wdDoNotSaveChanges)

if __name__ == '__main__':
    wordPath='D://20200426.docx'
    pdfPath='D://20200426.pdf'
    word_to_pdf(wordPath,pdfPath)











