import html2tk
from time import sleep

html = '''
<html>
<body>
<h1>Happiness Program</h1>
<br>

<p>What is your name?</p>
<input id="name">
<br>

<p>How would you rate your happiness?</p>
<input id="happiness" type="range" increment="20" value="48">
<br>

<p>Is what you just said true?</p>
<select id="select">
<option value="yes">yes</option>
<option value="no">no</option>
</select>
<br>

<button id="btn">Submit</button>
<br>

<p id="output"></p>

</body>
</html>
'''

stylesheet = html2tk.Stylesheet(('helvetica', 12), ('helvetica', 20), ('helvetica', 12), ('helvetica', 10))

global app

def test_application():
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
    app.get_element_by_id('output').text = 'Thinking...'
    app.update()
    sleep(1)

    happiness = app.get_element_by_id('happiness').value
    if app.get_element_by_id('select').value == 'no':
        happiness = 100 - happiness

    result = app.get_element_by_id('name').value.capitalize() + ', '
    if happiness < 10:
        result += 'you are EXTREMELY sad!'
    elif happiness < 25:
        result += 'you are pretty sad'
    elif happiness < 50:
        result += 'you might be a little bit sad, but you\'re probably just stressed'
    elif happiness < 75:
        result += 'you have an acceptable level of happiness'
    elif happiness < 90:
        result += 'you\'re pretty happy'
    else:
       result += 'you are too happy!'
    
    app.get_element_by_id('output').text = result

if __name__ == '__main__':
    test_application()