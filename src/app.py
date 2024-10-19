import argparse

def main():
    parser = argparse.ArgumentParser(description="Print the greeting type.")
    parser.add_argument('-n', '--greeting_type', type=str, choices=['morning', 'evening', 'afternoon'], required=True, help="Type of greeting")
    
    args = parser.parse_args()
    
    print(f"Received greeting type: {args.greeting_type}")

if __name__ == "__main__":
    main()
