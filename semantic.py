
import spacy

#first example - comparing words

nlp = spacy.load("en_core_web_md")

#Well en_core_web_md seems to have some of it's priorities right...
tokens = nlp("happiness money instagram status power health purpose family")

for token1 in tokens:   
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#The output of this is interesting. The fact that the similarity of a cat is similar with an apple and a banana shows that the fact 
#that the monkey is associated with a banana does not affect the similarity of a cat with a banana, even though the cat and the monkey 
#are similar. 



#second example - comparing sentences

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

