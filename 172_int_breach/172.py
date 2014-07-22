import hashlib
import uuid
import fileinput

def hash_text(input_text):
    return hashlib.sha1(input_text).hexdigest()

def salt_hash_text(input_text):
    return hash_text(str(uuid.uuid4()) + input_text)

def main():
    for line in fileinput.input():
        print line.strip(), ": ", salt_hash_text(line)

if __name__ == '__main__': main()
