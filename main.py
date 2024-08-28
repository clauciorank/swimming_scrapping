from process_pdf import ProcessPDF
from detect_line import DetectLines
from text_detection import TextDetection
from text_treat import TreatText
import os
import datetime


def get_creation_time(file_path):
    # Get the creation time of the file
    stat = os.stat(file_path)
    # Convert the creation time to a datetime object
    return datetime.datetime.fromtimestamp(stat.st_ctime)


def list_files_by_creation_date(directory):
    # List all files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sort files by creation time
    files_sorted = sorted(files, key=get_creation_time)

    return files_sorted


if __name__ == '__main__':
    # pdf = ProcessPDF('resultados-estadual-2024.pdf', 'pdf_image')
    #
    # pdf.convert_to_image()
    # pdf.cut_images(378, 2780)
    #
    # image_plot = 'pdf_image/out-0.jpg'
    # for i in range(len(os.listdir('pdf_image'))):
    #     print(f'Processing image {i}')
    #     image = f'pdf_image/out-{i}.jpg'
    #     boxes = DetectLines(image).detect_lines()
    #
    #     text = TextDetection(image, boxes).detect_text()
    #     # append text to a file
    #     with open('output.txt', 'a') as f:
    #         for line in text:
    #             f.write(';'.join(line) + '\n')

    df = TreatText('output.txt').treat_text()

    df_filter = ~df[6].str.contains('REVEZAMENTO') | (df[6].str.contains('REVEZAMENTO') & df[3].notna() & (df[3] != ''))

    # Apply the filter to the DataFrame
    df = df[df_filter]

    problematic_lines = df[(~df[2].str.contains(r'\d')) & (df[2] != '')]

    df.to_csv('output.csv', index=False)
