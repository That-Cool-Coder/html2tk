import html2tk

HTML_FILE_NAME = 'basic.html'

def test_load_from_file():
    html2tk.Application(source_file_name=HTML_FILE_NAME)

if __name__ == '__main__':
    test_load_from_file()