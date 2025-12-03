import streamlit as st, nltk, nltk.stem.wordnet, textblob, re

def prepare_text(text):
  text = re.sub(r"[^A-Za-z0-9]", " ", text)
  text = re.sub(r"\'s", " ", text)
  text = re.sub(r"http\S+", " link ", text)
  text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)

  text_list = text.split()

  lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()
  lemmatized_words = [lemmatizer.lemmatize(word) for word in text_list]
  return " ".join(lemmatized_words)

def analyze_text(text):
  blob = textblob.TextBlob(text)
  sentiment = blob.sentiment[0]

  if sentiment > 0:
    emoji = ":blush:"
    st.success("Happy: {}".format(emoji))
  elif sentiment < 0:
    emoji = ":disappointed:"
    st.warning("Sad: {}".format(emoji))
  else:
    emoji = ":confused:"
    st.info("Confused: {}".format(emoji))
  
  st.success("Polarity score is {}".format(sentiment))

def button_click():
  lemmatized = prepare_text(input_text)
  analyze_text(lemmatized)

st.title("Sentiment Analysis")
input_text = st.text_area(label="Input text to be analyzed here.", height="content")
button = st.button(label="Analyze")

if button: button_click()