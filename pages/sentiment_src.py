import streamlit as st


st.header('Balibad\'s Basic Sentiment Analyzer App')
st.subheader('This python code is implemented for Streamlit')
st.code('''
        import streamlit as st
        import nltk.classify.util
        from nltk.classify import NaiveBayesClassifier
        from nltk.corpus import names

        # Define features (words) and their corresponding labels (positive/negative)
        def word_features(words):
            return dict([(word, True) for word in words])

        positive_words = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'poor', 'difficult']

        positive_features = [(word_features(pos_word.split()), 'positive') for pos_word in positive_words]
        negative_features = [(word_features(neg_word.split()), 'negative') for neg_word in negative_words]

        # Combine positive and negative features
        train_set = positive_features + negative_features

        # Train the Naive Bayes classifier
        classifier = NaiveBayesClassifier.train(train_set)

        # Define messages for positive and negative sentiments
        sentiment_messages = {
            'positive': "You seem to be feeling positive! Keep up the good vibes!",
            'negative': "It looks like you're feeling down. Remember, tomorrow is a new day!"
        }

        # Define the Streamlit app
        def main():
            st.title("Balibad's Sentiment Analyzer 🐶")
            sentence = st.text_input('Tell me what you feel today:')
            if st.button('Say it'):
                if sentence:
                    # Classify the sentence
                    sentiment = classifier.classify(word_features(sentence.split()))
                    st.write(f"{sentiment_messages.get(sentiment, 'Unknown')}")

        # Run the Streamlit app
        if __name__ == '__main__':
            main()
    ''')
