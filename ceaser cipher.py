  # Encode and Decode

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z"]

def encode(msg, key):
    encode_msg = ""
    for each_ch in msg:
        if each_ch not in letters:
            encode_ch = each_ch
        else:
            ch_index = letters.index(each_ch)
            encode_ch_index = ch_index + key
            if encode_ch_index > 25:
                encode_ch_index -= len(letters)
            encode_ch = letters[encode_ch_index]
        
        encode_msg += encode_ch

    return encode_msg.capitalize()


def decode(msg,key):
    decode_msg = ""
    for each_ch in msg:
        if each_ch not in letters:
            decode_ch = each_ch
        else:
            ch_index = letters.index(each_ch)
            decode_ch_index = ch_index - key
            decode_ch = letters[decode_ch_index]
        
        decode_msg += decode_ch

    return decode_msg.capitalize()



# Main Program
print("Which option you wanna choose? 1. Encode, 2.Decode: ")
user_choice = input("1 or 2?- ")
if user_choice == "1":
    user_msg = input("Enter your msg you wanna encode: ").lower()
    key = int(input("Enter the secret key: "))
    encode_msg = encode(user_msg, key)
    print(encode_msg)

else:
    user_msg = input("Enter your msg you wanna decode: ").lower()
    key = int(input("Enter the secret key: "))
    decode_msg = decode(user_msg, key)
    print(decode_msg)
