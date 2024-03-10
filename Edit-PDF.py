"""
Program : PDF Separate and Merge Application. This app can merge two files,
          extract a page from file and split file into separate pages. The
          user must enter the absolute path of the file.

Author one name: Badr Eldeen Khaled Khareeb
Author one ID: 20230086

Author two: Samir Sherif Shokry Abd elhady
Author two ID: 20230178

Author three: Mohamed Bakry Mohamed yassin
Author three ID: 20230325

Version: 3.0

Date: 29/2/2024
"""

# Call the PyPDF2 library that we will need to build this application
import PyPDF2


def merger_pdf(f_pdf, s_pdf):
    try:
        # open the pdf
        pdf1 = open(f_pdf, 'rb')
        pdf2 = open(s_pdf, 'rb')

        # Create PDF reader
        reader1 = PyPDF2.PdfReader(pdf1)
        reader2 = PyPDF2.PdfReader(pdf2)

        # Create PDF writer
        writer = PyPDF2.PdfWriter()

        # Merge pages from first PDF
        for page in range(len(reader1.pages)):
            writer.add_page(reader1.pages[page])

        # Merge pages from second PDF
        for page in range(len(reader2.pages)):
            writer.add_page(reader2.pages[page])

        # Write the merged PDF
        merged = open('merged.pdf', 'wb')
        writer.write(merged)
        print("The files have been merged successfully\n")

        # Close PDF
        merged.close()
        pdf1.close()
        pdf2.close()
        main()

    except FileNotFoundError:
        print("This file doesn't exist\n")
        main()

def extract_page(PDF):
    try:
        # open the PDF
        pdf = open(PDF, 'rb')

        # Create PDF reader
        reader = PyPDF2.PdfReader(pdf)

        # Create PDF writer
        writer = PyPDF2.PdfWriter()

        # check if input (page number) is valid or not
        while True:
            page_num = input('Enter page number: ')
            if page_num.isdigit() and 0 < int(page_num) <= len(reader.pages):
                page_num = int(page_num)
                break
            else:
                print("This page doesn't exist\n")

        # Add selected page to writer
        page = reader.pages[page_num - 1]
        writer.add_page(page)

        # Write the extracted page to a new file
        new_pdf = open(f"{PDF}-{page_num}.pdf", 'wb')
        writer.write(new_pdf)
        print("The page has been extracted successfully\n")

        # Close PDF
        new_pdf.close()
        pdf.close()
        main()

    except FileNotFoundError:
        print("This file doesn't exist\n")
        main()


def split_pdf(PDF):
    try:
        # open the PDF
        pdf = open(PDF, 'rb')

        # Create PDF reader
        reader = PyPDF2.PdfReader(pdf)

        # Create a separate PDF file for each page
        for page_num in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_num])
            new_pdf = open(f"{PDF}-{page_num + 1}.pdf", 'wb')
            writer.write(new_pdf)
            new_pdf.close()  # Close pdf per page

        print("Done\n")
        # Close the file
        pdf.close()

        main()

    except FileNotFoundError:
        print("This file doesn't exist\n")
        main()


def main():
    print("""Menu
A) Merge two files 
B) Extract a page from file 
C) Split file into separate pages 
D) Exit
""")

    while True:
        choice = input("Enter your choice (A, B, C, or D): ").upper()

        if choice == "A":
            pdf1 = input("Enter the absolute path of the first file: ")
            pdf2 = input("Enter the absolute path of the second file: ")
            merger_pdf(pdf1, pdf2)

        elif choice == "B":
            pdf = input("Enter the file absolute path: ")
            extract_page(pdf)

        elif choice == "C":
            pdf = input("Enter the file absolute path: ")
            split_pdf(pdf)

        elif choice == "D":
            exit()

        else:
            print("Invalid choice.\nPlease", end=" ")


main()
