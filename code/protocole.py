#frame format

header = '00000000'              #num de sequence sur 256 bits
flag = '01111110'
length = 100                     #nb of Bytes
CRC-16-CCITT = 0x1021            #generator polynomial




#méthode d'encapsulation




def main ():
    perfect_c = canal(p_error = 0, p_loss = 0)
    noisy_c = canal(p_error = 0.05, p_loss = 0.1)
    unstable_c = canal(p_error = 0.1, p_loss = 0.15, max_delay = 300)