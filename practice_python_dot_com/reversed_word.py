# Data Science, Machine Learning, Data Structure

#Solution
def reverseWord(w):
    return ' '.join(w.split()[::-1])


def reverseChar(w):
    return w[::-1]

# print reverseChar("A Beautiful Mind")
# print reverseWord("A Beautiful Mind")

#Solution
# print " ".join(reversed("A Beautiful Mind"))

#Solution
# x = "A Beautiful Mind".split()
# x.reverse()
# print x

#Solution
def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0, word)
  return " ".join(result)

print reverse_v1("Bangladesh World clock")


