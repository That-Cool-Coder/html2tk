import html2tk
from time import sleep

html = '''
<html>
<head>
<title>Style test</title>
</head>

<body>

<h1 id="heading">Style Testing Program</h1>
<br>
<button id="btn">Clicky!</button>
<br>
<div id="toShow" hidden>
<p>I am shown!</p>
</div>

</body>
</html>
'''

stylesheet = html2tk.Stylesheet(
    heading={'color' : 'red', 'font_size' : 13},
    div={'color' : 'blue'},
    button={'color' : 'grey50'},)

def test_style():
    global app
    print('') # because pytest doesn't put a newline after their strings

    app = html2tk.Application()
    app.maximise()
    app.load_html(html=html)
    app.apply_stylesheet(stylesheet)
    app.populate_body()

    app.get_element_by_id('btn').command = callback

    app.mainloop()

def callback():
    div = app.get_element_by_id('toShow')
    div.style.background_color = 'red'
    if div.hidden:
        div.show()
    else:
        div.hide()

if __name__ == '__main__':
    test_style()