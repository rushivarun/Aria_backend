from flask import Flask
from flask import jsonify
from rake_nltk import Rake
from azure.cognitiveservices.search.imagesearch import ImageSearchAPI
from msrest.authentication import CognitiveServicesCredentials
import nltk


nltk.download('stopwords')
nltk.download('punkt')


def keyword_ext(my_text):
    r = Rake()
    r.extract_keywords_from_text(my_text)
    key_list = r.get_ranked_phrases()
    return key_list

subscription_key = "6c492807720245c09691b16f4826e3c3"


def FetchImage(search_term):

	client = ImageSearchAPI(CognitiveServicesCredentials(subscription_key))

	image_results = client.images.search(query=search_term)

	if image_results.value:
	    first_image_result = image_results.value[0]
	    #print("Total number of images returned: {}".format(len(image_results.value)))
	    #print("First image thumbnail url: 				{}".format(first_image_result.thumbnail_url))
	    #print("First image content url: {}".format(first_image_result.content_url))
	    return {'image_url': first_image_result.content_url, 'search_word': search_term, 'friendly': image_results.value[0].additional_properties['isFamilyFriendly'] }

	else:
	    print("No image results returned!")