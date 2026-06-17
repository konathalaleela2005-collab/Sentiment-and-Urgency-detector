from textblob import TextBlob

message = "I am very angry"

score = TextBlob(message).sentiment.polarity

assert score < 0

print("Test Passed")
