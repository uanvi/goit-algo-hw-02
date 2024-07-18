from collections import deque

def is_palindrome(s):
    """check if string is palindrome """
    # normalize string 
    s = s.lower().replace(' ', '')

    # add to dequeue
    char_deque = deque(s)

    # compare
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True


def main():
    try:
        while True:
            user_input = input("Enter string to check: ")
            
            if is_palindrome(user_input):
                print(f"String '{user_input}' is palindrome.")
            else:
                print(f"String '{user_input}' is not palindrome.")
                
    except KeyboardInterrupt:
        print("\nInterrupted")

if __name__ == "__main__":
    main()