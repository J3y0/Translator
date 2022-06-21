# Introduction

This project started when I get bored going to the Internet to look for a word in another language.

I wanted to type a word or a sentence, to automate the search and to have directly the result. All of that should stay in my terminal as I wanted to configure a Dropdown terminal for this program (then I always have it near).

>But how?
# What the code offers

In order to do this, when I want to translate entire sentence, I use the [Deepl API](https://www.deepl.com/fr/docs-api/) which is very easy to use, you just have to create an account *(The free version is enough to make you happy for a lot of time)*.

If I want to translate a word, Deepl wasn't responding to all my needs. Indeed, I wanted to have several definitions of the word, as sometimes words have different meanings. This is why, I put up some work to scrap [Word Reference Website](https://www.wordreference.com/). At the end, I finally have a functionnal translator which lets me select the Deepl or Word Reference experience, the language and returns the translated input.