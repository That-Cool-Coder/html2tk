import html2tk

def test_read_string_data():
    content = '''
    <html>
    <head>

    </head>

    <body>
        <p>Hello world</p>
    </body>
    </html>
'''
    html2tk.Application(raw_html=content)

if __name__ == '__main__':
    test_read_string_data()