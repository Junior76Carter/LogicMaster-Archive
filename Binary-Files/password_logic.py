# Simple Logic for Password Matching Pattern
# Developed by Junior Software 76

def check_password(target_password):
    # Simulated list of passwords to check
    wordlist = ["123456", "password", "admin123", "logic76", "010101"]
    
    print(f"[*] Starting analysis for target...")
    
    for attempt in wordlist:
        if attempt == target_password:
            print(f"[+] Match Found: {attempt}")
            return True
        else:
            print(f"[-] Trying: {attempt} ... No match.")
            
    return False

# Example Target
target = "logic76"
check_password(target)
