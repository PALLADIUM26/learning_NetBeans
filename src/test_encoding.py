import sys

sys.stdout.reconfigure(encoding="utf-8")  # Ensure UTF-8 encoding

test_string = "Hello, 😊 Unicode test! বাংলা, हिंदी, 日本語"
print(test_string)
sys.stdout.flush()  # Flush output immediately
