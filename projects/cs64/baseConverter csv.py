import base64

'''
csv_df = df.to_csv(index=False)
import base64
base64.b64encode(csv_df.encode('utf-8'))
'''

'''
import base64
data = open('small_portfolio.csv', 'rb').read()
base64.b64encode(data)
'''


filename = 'small_portfolio'
fin = open('encoded.' + filename)
encodedString = fin.read()
decodedString = base64.b64decode(encodedString)
fin.close()

fout = open(filename + '.csv', mode='w')
print(decodedString.decode('utf-8'), file=fout)
fout.close()