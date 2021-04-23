import html2tk

html = '''
<html>
<body>
<h1>Hello world</h1>
<p>This is a paragraph</p>
<p>And things are getting <i>very</i> interesting</p>
</body>
</html>
'''

stylesheet = html2tk.Stylesheet(('helvetica', 17), ('helvetica', 25))

def test_application():
    app = html2tk.Application()
    app.load_html(html=html)
    app.apply_stylesheet(stylesheet)
    app.populate_body()
    app.mainloop()

if __name__ == '__main__':
    test_application()