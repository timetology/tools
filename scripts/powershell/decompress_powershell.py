import base64
import zlib 
import argparse 


def decode_command(cmd):
    
    try:
        # base64 decode the command
        p1 = base64.b64decode(cmd)
        # Decompress with no header or trailer 
        p2 = zlib.decompress(p1, -15)
        return p2
    except TypeError:
        return "Command was not a Base64 encoded string. "
    except zlib.error:
        print "Warning! The command was not compressed. Returning decoded string.\n\n"
        return p1 

def main():
    parser = argparse.ArgumentParser(description='Decompress PowerShell Encoded Command.')
    parser.add_argument('command', help='Base64 encoded command to process.')
    args = parser.parse_args()

    print decode_command(args.command)
    

if __name__ == "__main__":
    main()
