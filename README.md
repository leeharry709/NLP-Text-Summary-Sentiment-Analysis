# NLP-Text-Summary-Sentiment-Analysis

## Introduction
Text summarization is a fundamental task in natural language processing (NLP), aimed at condensing the content of a given text while preserving its most important information. In this report, we discuss a text summarization application built using the PEGASUS model, a state-of-the-art transformer-based architecture for abstractive summarization. The application also leverages additional NLP tools such as keyword extraction and sentiment analysis to provide a comprehensive summary.

## Application Overview
The text summarization application is designed to interactively summarize input text provided by the user. It utilizes the `transformers` library to load a pre-trained PEGASUS model and tokenizer. The application is built using Streamlit, a Python library for creating web applications with minimal code.

## PEGASUS Model 
<p align='center'>
  <img src='https://production-media.paperswithcode.com/methods/f8b904da-2aaa-4b73-85cd-a8adfacce042.png' width='75%'>
</p>
PEGASUS is a pre-trained transformer model developed by Google AI for text summarization, built on top of the BART (Bidirectional Autoregressive Transformers) architecture. PEGASUS uses a masked language modeling (MLM) objective to pre-train, which involves randomly masking some of the words in a sentence and then predicting the missing words. What is unique with the output of PEGASUS is that the model generates a completely new summary whereas other models use sentences within the input text to generate a summary.

## Application Components
The application consists of the following components:

1. **Model Loading**: The PEGASUS model and tokenizer are loaded using the Hugging Face transformers library.

2. **Summarization Function**: The core of the application is the summarize_text function, which takes the user's input text as input and performs the following tasks:

   - Tokenizes the input text.
   - Generates a summary using the PEGASUS model.
   - Extracts keywords from the input text.
   - Calculates sentiment polarity and subjectivity.

3. **User Interaction**: Users can input the text they want to summarize through the chat interface provided by Streamlit. The application allows for interactive communication with the summarization model.

4. **Output Display**: The application displays the following information as output:

   - The generated summary.
   - The top 10 keywords extracted from the input text.
   - Sentiment analysis results, including polarity and subjectivity scores.

<p align='center'>
  <img src='https://github.com/leeharry709/NLP-Text-Summary-Sentiment-Analysis/blob/main/Screenshot%202023-08-18%20215116.png?raw=true' width='65%'>
</p>

The image shows the summary, keywords, and sentiment of the introductory paragraph of the Google AI blog post: [PEGASUS: A State-of-the-Art Model for Abstractive Text Summarization](https://ai.googleblog.com/2020/06/pegasus-state-of-art-model-for.html).

## Summarization and Analysis

Once the user provides input, the application proceeds to perform summarization and analysis tasks:

- It tokenizes the input text, generates a summary using PEGASUS, and displays the summary.
- It extracts the top 10 keywords from the input text and displays them.
- It calculates sentiment analysis scores, including polarity and subjectivity, and displays them.

## Conclusion

The text summarization application built with PEGASUS provides an efficient and user-friendly way to summarize text while also offering additional insights through keyword extraction and sentiment analysis. This application can be a valuable tool for users who want to quickly understand the essence of a given text and gain insights into its sentiment and key topics.

Further improvements and customization options can be explored, such as fine-tuning the summarization model for domain-specific tasks or enhancing the user interface for a more engaging user experience.

## Real-World Application
Text summarization, sentiment, and keyword extraction are all very essential to everyday life already. All three methods of NLP are used in search engines to show users before they click on the link what they are expecting in the website. The keywords can help users find what they are looking for without typing out the exact phrases or title of the webpage, the summarization can tell them briefly what the page is about before fully clicking on them (and inadvertantly avoiding spam or malware sites), and the sentiment can filter out search results that are too polarizing and opinionated. Optimization of NLP will allow users to live more efficient and productive lives.
