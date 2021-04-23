import html2tk

HTML_FILE_NAME = 'basic.html'

def test_load_from_file():
    html2tk.Application(source_file_path=HTML_FILE_NAME).mainloop()

if __name__ == '__main__':
    test_load_from_file()