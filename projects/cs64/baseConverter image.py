import base64


'''
import base64
data = open('bricks.png', 'rb').read()
base64.b64encode(data)
'''


filename = 'bricks'
fin = open('encoded.' + filename)
encodedString = fin.read()
decodedString = base64.b64decode(encodedString)
fin.close()

fout = open(filename + '.png', mode='wb')
fout.write(decodedString)
fout.close()