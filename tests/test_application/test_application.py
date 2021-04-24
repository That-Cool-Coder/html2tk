import html2tk
from time import sleep

html = '''
<html>
<body>
<h1>Happiness Program</h1>
<br>
<p>How would you rate your happiness?</p>
<input id="input" type="range", step="5">
<button id="btn">Submit</button>
<br>
<p id="output"></p>

</body>
</html>
'''

stylesheet = html2tk.Stylesheet(('helvetica', 12), ('helvetica', 20), ('helvetica', 12), ('helvetica', 11))

global app

def test_application():
    global app
    print('') # because pytest doesn't put a newline after their strings

    app = html2tk.Application()
    app.load_html(html=html)
    app.apply_stylesheet(stylesheet)
    app.populate_body()

    app.get_element_by_id('btn').command = callback

    app.mainloop()

def callback():
    app.get_element_by_id('output').text = 'Thinking...'
    app.update()
    sleep(1)

    happiness = app.get_element_by_id('input').value
    if happiness < 10:
        result = 'You are EXTREMELY sad!'
    elif happiness < 25:
        result = 'You are pretty sad'
    elif happiness < 50:
        result = 'You might be a little bit sad, but probably just stressed'
    elif happiness < 75:
        result = 'You have an acceptable level of happiness'
    elif happiness < 90:
        result = 'Wow, you\'re pretty happy'
    else:
       result = 'You are too happy!'
    
    app.get_element_by_id('output').text = result

if __name__ == '__main__':
    test_application()