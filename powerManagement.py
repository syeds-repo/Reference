import logging
import time
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.DEBUG)
logging.warning('Starting the application')


def string_reverse(str):

    rstr = ''
    index = len(str)
    while index > 0:
        rstr += str[ index - 1 ]
        index = index - 1
    return rstr
'''
loop=0
while loop < 100:
    str = 'macbookair'
    logging.info('Iteration : {}'.format(loop))
    logging.info('Reverse String: {}'.format(string_reverse(str)))
    time.sleep(5)
    loop = loop + 1 
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<power>')
def hello_name(power):
    return "Frequency Set to {}!".format(power)

if __name__ == '__main__':
    print ('Starting the application')
    app.run(host='0.0.0.0')
