raw_read = open('text.file', 'r')
text_file = raw_read.read()
alphabet = (
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L',
    'l',
    'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p',
    'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', ' ', '-', '!',
    '?',
    '.', ',', ';', ':', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',)
len_text_file = len(text_file)
len_alphabet = len(alphabet)

print len_text_file
print len_alphabet
gam = []
iterator = 0
e = 0
d = 0
while iterator < len_alphabet:
    if iterator < 52:
        a = alphabet[iterator]
        b = alphabet[iterator + 1]
        iterator += 2
    else:
        a = alphabet[iterator]
        b = alphabet[iterator]
        iterator += 1
    x = 0
    p = 0
    while p < len_text_file:
        if text_file[p] == a or text_file[p] == b:
            x += 1
        p += 1
    gam.append(x)
print gam
pr = gam
(x_a, x_b, x_c, x_d, x_e, x_f, x_g, x_h, x_i, x_j, x_k, x_l, x_m, x_n, x_o, x_p, x_q, x_r, x_s, x_t,
 x_u, x_v, x_w, x_x, x_y, x_z, x_, x_tre, x_zok, x_zpn, x_krp, x_kom, x_kkm, x_dkr, x_0, x_1, x_2, x_3, x_4, x_5, x_6,
 x_7, x_8, x_9) = pr
fl = open('gam_text', 'w')
fl.write(str(gam))
fl.close()
