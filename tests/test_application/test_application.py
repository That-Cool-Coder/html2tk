import html2tk

html = '''
<html>
<body>
<h1>Hello world</h1>
<p>This is a paragraph</p>
<p>And things are getting very interesting</p>
<button id="btn">Click me!</button>
<div>
<p id="somediv">I have appeared</p>
</div>
</body>
</html>
'''

stylesheet = html2tk.Stylesheet(('helvetica', 15), ('helvetica', 25), ('helvetica', 15))

def test_application():
    print('') # because pytest doesn't put a newline after their strings

    app = html2tk.Application()
    app.load_html(html=html)
    app.apply_stylesheet(stylesheet)
    app.populate_body()

    div = app.get_element_by_id('somediv')
    div.hide()

    button = app.get_element_by_id('btn')
    button.command = div.unhide

    app.mainloop()

if __name__ == '__main__':
    test_application()