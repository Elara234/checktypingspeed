import time

text = "The quick brown fox jumps over the lazy dog."
print("Type this:\n", text)
input("Press Enter when ready...")
start = time.time()
typed = input("Start typing: ")
end = time.time()

time_taken = end - start
accuracy = sum(1 for i,j in zip(text,typed) if i==j)/len(text)*100
wpm = len(typed.split())/(time_taken/60)

print(f"Time taken: {time_taken:.2f}s")
print(f"Accuracy: {accuracy:.2f}%")
print(f"Typing Speed: {wpm:.2f} WPM")
