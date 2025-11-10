#add 0 after five 1s
def hdlc_stuffing(bitstream):
    return bitstream.replace("11111", "111110")

#remove the 0 after five 1s
def hdlc_destuffing(bitstream):
    return bitstream.replace("111110", "11111")
    

#---- for testing ----
#def main():                    

#    flux_original = "011111101111101111110111110"
#    flux_restauré = hdlc_destuffing(hdlc_stuffing(flux_original))
#    assert flux_restauré == flux_original  

#if __name__ == "__main__":
#    main()