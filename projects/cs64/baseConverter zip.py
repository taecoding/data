import base64


'''
import base64
data = open('images_a.zip', 'rb').read()
base64.b64encode(data)
'''


filename = 'pretrained_model'
fin = open('encoded.' + filename)
encodedString = fin.read()
decodedString = base64.b64decode(encodedString)
fin.close()

fout = open(filename + '.h5', mode='wb')
fout.write(decodedString)
fout.close()