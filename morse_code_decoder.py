# Morse Code Translator
# Kenneth Fossum

a = '.-'
b = '-...'
c = '-.-.'
d = '-..'
e = '.'
f = '..-.'
g = '--.'
h = '....'
i = '..'
j = '.---'
k = '-.-'
l = '.-..'
m = '--'
n = '-.'
o = '---'
p = '.--.'
q = '--.-'
r = '.-.'
s = '...'
t = '-'
u = '..-'
v = '...-'
w = '.--'
x = '-..-'
y = '-.--'
z = '--..'
zero = '-----'
one = '.----'
two = '..---'
three = '...--'
four = '....-'
five = '.....'
six = '-....'
seven = '--...'
eight = '---..'
nine = '----.'
morse = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,zero,one,two,three,four,five,six,seven,eight,nine]
morse_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def morse_decoder(code):
    c = 0
    msg = ''
    sentence = code.split('   ') #splits each sentence into an array made of strings of each word
    for word in sentence:
        c =+ 1
        word_str = word.split(' ') #splits each word into an array made of strings of each character
        for char_num in word_str:
            a = 0
            for morse_elem in morse:
                a += 1 #counter for which morse code character you're testing against the given code
                if char_num == morse_elem:
                    msg = msg + morse_char[a-1]
        msg = msg + ' '
    msg = msg[0:len(msg)-1]
    msg = msg.capitalize()
    print('secret msg is ',msg)
    return msg

if __name__ == '__main__':
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    assert morse_decoder("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ...") ==  "0123456789 are digits"
    # print('')
    # print('Confirmed expert coder? Definitely')