import streamlit as bel

bel.title('Hello, world')
bel.header('this is header')
bel.subheader('this is subheader')
bel.markdown('this is markdown')
bel.code("print('this is code')", language='python')
bel.latex('''(a+b)^2 = (a^2 + 2ab + b^2''')

# button
if bel.button('click me'):
    bel.write(' You Cilck the Button')
else:
    bel.write(' Pleaes Cilck the Button')

data = bel.text_input('Please enter data')
if bel.button('Submit'):
    bel.write(F"Your data is'{data}")

# slider

score = bel.slider(
    "Plases enter your score",
    min_value=0,
    max_value=100,
    value=10)
bel.write(F"Your score is {score}")
