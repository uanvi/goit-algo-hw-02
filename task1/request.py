import queue
import uuid

# create quue
request_queue = queue.Queue()

def generate_request():
    """Generate request, add to queue"""
    request_id = uuid.uuid4()
    
    request_queue.put(request_id)
    print(f"Generated request: {request_id}")

def process_request():
    """Process request, remove from queue"""
    if not request_queue.empty():
        request_id = request_queue.get()
        print(f"Processed request: {request_id}")
    else:
        print("Queue is empty. No requests to process.")

def main():
    try:
        while True:
            user_input = input("Press 'g' to generate a request, 'p' to process a request, or 'q' to quit: ")
            if user_input.lower() == 'g':
                generate_request()
            elif user_input.lower() == 'p':
                process_request()
            elif user_input.lower() == 'q':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please enter 'g', 'p', or 'q'.")
            
    except KeyboardInterrupt:
        print("\nInterrupted")

if __name__ == "__main__":
    main()
