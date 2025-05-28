# 7. Print Unique Words Ignoring Stop Words (Using Set)
# Given list: ['python', 'code', 'loop', 'if', 'python', 'else', 'if'].
# Print unique words excluding stop words:
# {'if', 'else'}.
 # Expected Output: Unique non-stop words: {'python', 'code', 'loop'}
 
a = ['python', 'code', 'loop', 'if', 'python', 'else', 'if']
stop_words = {'if', 'else'}
 
unique_words = set()
for word in a:
    if word not in stop_words:
        unique_words.add(word)
print(f"Unique non-stop words: {unique_words}")

 