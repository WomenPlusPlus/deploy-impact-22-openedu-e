# <imports>
import os.path
import time
import uuid
from pprint import pprint

from azure.cognitiveservices.vision.contentmoderator import ContentModeratorClient
from azure.cognitiveservices.vision.contentmoderator.models import (Evaluate, OCR, FoundFaces, # image moderation
        APIErrorException, Body, ImageList, ImageIds, Image, RefreshIndex, MatchResponse, # image lists
        TermList, Terms, TermsData, Screen, # terms lists
        CreateReviewBodyItem ) # create human review for images
from msrest.authentication import CognitiveServicesCredentials


'''
CONTENT MODERATOR 
Prerequisites:
    - A Content Moderator subscription in the Azure portal: https://ms.portal.azure.com
    - pip tool: https://pip.pypa.io/en/stable/installing/
    - Install the SDK from the command line: 
        pip install azure-cognitiveservices-vision-contentmoderator
    - Make sure the terms list file is in your working folder: content_moderator_term_list.txt
How to run:
    - From the command line (from working directory): python content_moderator.py
References:
    - SDK: https://docs.microsoft.com/en-us/python/api/azure-cognitiveservices-vision-contentmoderator/azure.cognitiveservices.vision.contentmoderator?view=azure-python
    - API: https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/api-reference
    - Documentation: https://docs.microsoft.com/en-us/azure/cognitive-services/content-moderator/
This script contains the following tasks:
    - Image moderation
    - Custom images list
    - Custom terms list
    - Create human images review
'''
# Image moderation 
IMAGE_MODERATION = ['https://moderatorsampleimages.blob.core.windows.net/samples/sample2.jpg',
                    'https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png']


# Text moderation
TEXT_MODERATION_FILE = 'content_moderator_text_moderation.txt'


# Image lists for the custom image lists
# Images need to have a minimum of 128 pixels and a maximum file size of 4MB
IMAGE_LIST = {
    "Sports": [ 'https://moderatorsampleimages.blob.core.windows.net/samples/sample4.png',
                'https://moderatorsampleimages.blob.core.windows.net/samples/sample6.png',
                'https://moderatorsampleimages.blob.core.windows.net/samples/sample9.png' ],

    "Swimsuit": [ 'https://moderatorsampleimages.blob.core.windows.net/samples/sample1.jpg',
                  'https://moderatorsampleimages.blob.core.windows.net/samples/sample3.png',
                  'https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png', ]
}
IMAGES_TO_MATCH = [ 'https://moderatorsampleimages.blob.core.windows.net/samples/sample1.jpg',
                    'https://moderatorsampleimages.blob.core.windows.net/samples/sample4.png',
                    'https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png',
                    'https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png' ]

# Terms for the custom terms list
TERM_LIST_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)))
TERMS_LIST_FILE = 'content_moderator_term_list.txt'

# Create a human review for an image URL
image_url_reviews = 'https://moderatorsampleimages.blob.core.windows.net/samples/sample5.png'

# Number of minutes to delay after some operations, to allow server to finish processing, 
# before executing the next task.
LATENCY_DELAY = 0.5

'''
AUTHENTICATE
Create a single client for all samples, except for human reviews. It needs its own client.
'''
# <authentication>
# Set your environment variables with the values of your key and region, "westus" is the default region.
SUBSCRIPTION_KEY = os.environ.get('CONTENT_MODERATOR_SUBSCRIPTION_KEY')
ENDPOINT = os.environ.get('CONTENT_MODERATOR_ENDPOINT', 'https://westus.api.cognitive.microsoft.com')
# </authentication>

# Get region for the human reviews callback endpoint
REGION = os.environ.get('CONTENT_MODERATOR_REGION', 'westus')

# <client>
# Create client 
client = ContentModeratorClient(endpoint=ENDPOINT, credentials=CognitiveServicesCredentials(SUBSCRIPTION_KEY))
# </client>

# Need a special client for the human reviews (due to unique key)
# Need to get key from Content Moderator website,
# go to gear symbol (Settings) --> Credentials --> Ocp-Apim-Subscription-Key
# Set your key and region in your environment variables.
REVIEWS_SUBSCRIPTION_KEY = os.environ.get('CONTENT_MODERATOR_REVIEWS_KEY')

# Where the image for review gets sent to.
call_back_endpoint = 'https://{}.api.cognitive.microsoft.com/contentmoderator/review/v1.0'.format(REGION)
client_reviews = ContentModeratorClient(endpoint= ENDPOINT,
    credentials=CognitiveServicesCredentials(SUBSCRIPTION_KEY))
# The name of the team to assign to the human review job. Add to your environment variables.
# The team name is the Id you used to create your account from the Content Moderator web site. 
# https://{YOUR_REGION}.contentmoderator.cognitive.microsoft.com
team_name = os.environ.get('CONTENT_MODERATOR_TEAM_NAME')
'''
END - Authenticate
'''

print('\n##############################################################################\n')

'''
IMAGE MODERATION
Moderate images, including text and faces.
'''
print('IMAGE MODERATION')
print()
# Image moderation, using image at [0]
print("Evaluate the image '{}' for adult and racy content:".format(os.path.basename(IMAGE_MODERATION[0])))
mod_image = client.image_moderation.evaluate_url_input(content_type="application/json", cache_image=True,
            data_representation="URL", value=IMAGE_MODERATION[0])
assert isinstance(mod_image, Evaluate)
# Format for printing
mod_results = list(mod_image.as_dict().items())
for result in mod_results:
    print(result)

# Moderating text in an image, using image at [0]
print("\nDetect, extract, and moderate text for image {}:".format(os.path.basename(IMAGE_MODERATION[0])))
mod_image = client.image_moderation.ocr_url_input(language="eng", content_type="application/json",
            data_representation="URL", value=IMAGE_MODERATION[0], cache_image=True)
assert isinstance(mod_image, OCR)
# Format for printing
mod_results = list(mod_image.as_dict().items())
for result in mod_results:
    print(result)

# Moderating faces in an image, using image at [1]
print("\nDetect faces and moderate for image {}:".format(os.path.basename(IMAGE_MODERATION[1])))
mod_image = client.image_moderation.find_faces_url_input(content_type="application/json", cache_image=True,
            data_representation="URL", value=IMAGE_MODERATION[1])
assert isinstance(mod_image, FoundFaces)
# Format for printing
mod_results = list(mod_image.as_dict().items())
for result in mod_results:
    print(result)
print()
'''
END - IMAGE MODERATION
'''
print('##############################################################################\n')

# <textModeration>
'''
TEXT MODERATION
Detect, extract, and moderate text from a string in a local file.
'''
print('EVALUATE TEXT')
print()

# Screen the input text: check for profanity, autocorrect text, 
# check for personally identifying information (PII), and classify text.
# The parameter 'text_content' expects a File object, which it can call read() on.
with open(TEXT_MODERATION_FILE, "rb") as text_file:
    screen = client.text_moderation.screen_text(language="eng", text_content_type="text/plain", text_content=text_file, autocorrect=True, pii=True, classify=True)
    assert isinstance(screen, Screen)
    # Format and print
    text_mod_results = list(screen.as_dict().items())
    pprint(text_mod_results)
    print()
'''
END - TEXT MODERATION
'''
# </textModeration>
        
print('\n##############################################################################\n')

'''
CUSTOM IMAGES LIST
This example shows how to manage image lists:
- Create an image list.
- Add images to a list. 
- Get all image IDs.
- Update list details.
- Get list details.
- Refresh the index.
- Match images against the image list.
- Remove an image, refresh, and re-match.
- Delete all images.
- Delete list.
- Get all image list IDs.
'''
print('CUSTOM IMAGES LIST')
print()
# Returns an ImageList object
custom_image_list = client.list_management_image_lists.create(content_type='application/json',
        body={ 'name':'My Custom Images List Name', 'description':'A list of sport and swimsuit images',
               'metadata': { 'good': 'Acceptable', 'not_good': 'Potentially racy' } })
print('Image list created:')
assert isinstance(custom_image_list, ImageList)
# Save the ID of the list
image_list_id = custom_image_list.id 
# Format to print the tuples
image_list = list(custom_image_list.as_dict().items())
for image in image_list:
    print(image)

'''
Add images
Add from the URL dictionary.
'''
print('\nAdding images to list ID {}:'.format(image_list_id))
index = {}  # Keep an index of url ids for later removal
try:
    for label, urls in IMAGE_LIST.items(): # Get list of pairs
        for url in urls:
            print('Adding image {} to list {} with label {}.'.format(os.path.basename(url), image_list_id, label))
            # Returns an Image object
            added_image = client.list_management_image.add_image_url_input( 
                list_id=image_list_id, content_type='application/json',
                data_representation='URL', value=url, label=label )
            if added_image:
                index[url] = added_image.content_id
except APIErrorException as err:
    print('Unable to add image to list: {}'.format(err))
else:
    assert isinstance(added_image, Image)

'''
Get all images ids
'''
print('\nGetting all image IDs for list {}:'.format(image_list_id))
# Returns an ImageIds object
image_ids = client.list_management_image.get_all_image_ids(list_id=image_list_id)
assert isinstance(image_ids, ImageIds)
# Convert ImageIds object to dictionary then list, printing the 'content_ids' key
id_list = list(image_ids.as_dict().items())
print(id_list[1])


'''
Update list details
Changes the name of an existing list.
'''
print('\nUpdating details for list {}:'.format(image_list_id))
# Returns an ImageList object
updated_list = client.list_management_image_lists.update( list_id=image_list_id, content_type='application/json', body={ 'name': 'Swimsuits and sports' })
assert isinstance(updated_list, ImageList)
updated = list(updated_list.as_dict().items())
for item in updated:
    print(item)

'''
Get list details
'''
print('\nGetting details for list {}:'.format(image_list_id))
# Returns an ImageList object
list_details = client.list_management_image_lists.get_details(list_id=image_list_id)
assert isinstance(list_details, ImageList)
for item in list(list_details.as_dict().items()): # Prints id, name, description, metadata
    print(item)

'''
Refresh the index
If changed, an image list must refresh its index for changes to be included in future scans.
'''
print('\nRefreshing the search index for list {}:'.format(image_list_id))
# Returns a RefreshIndex object
refresh_image_index = client.list_management_image_lists.refresh_index_method(list_id=image_list_id)
assert isinstance(refresh_image_index, RefreshIndex)
refreshed = list(refresh_image_index.as_dict().items()) 
# Prints if update was a success
print(refreshed[3])

print('\nWaiting {} minutes to allow server to update index changes...'.format(LATENCY_DELAY))
time.sleep(LATENCY_DELAY * 60)

'''
Match images against the image list
Using the Image Moderation API, compares two lists, looks for exact image matches.
False results have no match details.
'''
for image_url in IMAGES_TO_MATCH:
    print('\nMatching image {} against the images in list {}:'.format(os.path.basename(image_url), image_list_id))
    # Returns a MatchResponse object
    match_result = client.image_moderation.match_url_input(content_type='application/json',
        list_id=image_list_id, data_representation='URL', value=image_url)
    assert isinstance(match_result, MatchResponse)
    # Print information about the match
    print('Is image a match? {}'.format(match_result.is_match))
    print('Complete match details:')
    match_info = list(match_result.as_dict().items()) 
    print(match_info[2])

'''
Delete images
Deletes an image from the list.
'''
image_to_remove = 'https://moderatorsampleimages.blob.core.windows.net/samples/sample16.png'
# Returns a string of the image ID removed
client.list_management_image.delete_image(list_id=image_list_id, image_id=index[image_to_remove])
print('\nRemoved image {} from list {}'.format(os.path.basename(image_to_remove), image_list_id))

'''
Refresh the index (again)
Refreshes the index again after removing an image.
'''
print('\nRefreshing the search index for list {}'.format(image_list_id))
client.list_management_image_lists.refresh_index_method(list_id=image_list_id)

print('Waiting {} minutes to allow server to update index changes...'.format(LATENCY_DELAY))
time.sleep(LATENCY_DELAY * 60)

'''
Re-match
Compares the lists again after the change.
'''
print('\nMatching images to list. The removed image should not match.')
for image_url in IMAGES_TO_MATCH:
    print('\nMatching image {} against the images in list {}'.format(os.path.basename(image_url), image_list_id))
    match_result = client.image_moderation.match_url_input( content_type='application/json',
        list_id=image_list_id, data_representation='URL', value=image_url )
    assert isinstance(match_result, MatchResponse)
    # Print information about the match
    print('Is image a match? {}'.format(match_result.is_match))
    print('Complete match details:')
    match_info = list(match_result.as_dict().items()) 
    print(match_info[2])

'''
Delete all images
Deletes all images from list. Left with an empty list.
'''
# Returns the deletion status, as a string
client.list_management_image.delete_all_images(list_id=image_list_id)
print('\nDeleted all images in the image list {}.'.format(image_list_id))

'''
Delete list
Deletes the list entirely.
'''
# Returns the deletion status, as a string
client.list_management_image_lists.delete(list_id=image_list_id)
print('\nDeleted the image list {}.'.format(image_list_id))

'''
Get all list ids
'''
print('\nVerify that the list {} was deleted:'.format(image_list_id))
# Returns a list[ImageList] object
image_lists = client.list_management_image_lists.get_all_image_lists()
# Checks if our image list is gone.
assert not any(image_list_id == image_list.id for image_list in image_lists)
if image_lists:
    for img_list in image_lists:
        if img_list.id == image_list_id:
            print('Image list:', image_list_id, 'exists.')
        elif img_list.id:    
            print('List in account:', img_list.id)
else:
    print('List', image_list_id, 'has been removed.')
'''
END - CUSTOM IMAGES LIST
'''
print('\n##############################################################################\n')

'''
CUSTOM TERMS LIST
This sample creates a custom terms list, using the List Management API. 
Useful if you want to add/use your own moderation terms to a project.
- Create a terms list.
- Update terms list details.
- Add terms to a list. 
- Get all terms IDs. 
- Refresh the index. 
- Screen the text.
- Remove terms, refresh, and re-screen text.
- Delete all terms. 
- Delete list.
'''
print('CUSTOM TERMS LIST')
print()
'''
Create term list
Creates an empty terms list.
'''
custom_terms_list = client.list_management_term_lists.create(content_type='application/json', 
body={ 'name':'My Custom Terms List Name', 'description':'A list of custom terms.' })

print('Term list created:')
assert isinstance(custom_terms_list, TermList)
# Save an ID of the list
terms_list_id = custom_terms_list.id 
# Format to print as list
terms_list = list(custom_terms_list.as_dict().items())
for term in terms_list:
    print(term)

'''
Update list details
This example adds details about a list.
'''
print('\nUpdating details for list {}:'.format(terms_list_id))
updated_terms_list = client.list_management_term_lists.update(list_id=terms_list_id, content_type="application/json", 
                        body={ "name": "Greetings", "description": "Different ways to greet someone." })
assert isinstance(updated_terms_list, TermList)
updated_list = list(updated_terms_list.as_dict().items())
for term in updated_list:
    print(term)

'''
Add terms
'''
# Do one API call per term added
print('\nAdding terms to list {}...'.format(terms_list_id))
client.list_management_term.add_term(list_id=terms_list_id, term="hello", language="eng")
client.list_management_term.add_term(list_id=terms_list_id, term="wave", language="eng")

'''
Get all terms in list
'''
print("\nGetting all terms in list {}:".format(terms_list_id))
added_terms_list = client.list_management_term.get_all_terms(list_id=terms_list_id, language="eng")
assert isinstance(added_terms_list, Terms)
terms_data = added_terms_list.data
assert isinstance(terms_data, TermsData)
# terms_data.terms returns a list[TermsInList]
for term in terms_data.terms:
    # Get term property from each term in list, or view entire item
    print(term.term, term)

'''
Refresh the index
This is a must when you make changes to the list, in order to scan through it again.
'''
print('\nRefreshing the search index for list {}:'.format(terms_list_id))
refreshed_index = client.list_management_term_lists.refresh_index_method(list_id=terms_list_id, language="eng")
assert isinstance(refreshed_index, RefreshIndex)
# Get status to check if index has been refreshed or not.
print(refreshed_index.status)

print("\nWaiting {} minutes to allow the server time to update the index...".format(LATENCY_DELAY))
time.sleep(LATENCY_DELAY * 60)

'''
Screen text
Searches through a text block to find terms. All terms in a block of screened text are recognized as words within quotes.
'''
print('\nScreening text in the term list:')
with open(os.path.join(TERM_LIST_PATH, TERMS_LIST_FILE), "rb") as text_fd:
    screen = client.text_moderation.screen_text(text_content_type="text/plain", text_content=text_fd,
        language="eng", autocorrect=False, pii=False, list_id=terms_list_id)
    assert isinstance(screen, Screen)
    screened_list = list(screen.as_dict().items())
    for item in screened_list:
        print(item)

'''
Remove terms
'''
term_to_remove = "hello"
print('\nRemoving term "{}" from list {}...'.format(term_to_remove, terms_list_id))
client.list_management_term.delete_term(list_id=terms_list_id, term=term_to_remove, language="eng")

'''
Refresh the index
Refresh again since removing a term changed the list
'''
print("\nRefreshing the search index again for list {}:".format(terms_list_id))
rerefreshed_index = client.list_management_term_lists.refresh_index_method(list_id=terms_list_id, language="eng")
assert isinstance(rerefreshed_index, RefreshIndex)
# Get status to check if index has been refreshed or not.
print(rerefreshed_index.status)

print("\nWaiting {} minutes to allow the server time to update the index...".format(LATENCY_DELAY))
time.sleep(LATENCY_DELAY * 60)

'''
Re-screen text
Notice the 'terms' key is missing the removed term, as expected.
'''
with open(os.path.join(TERM_LIST_PATH, TERMS_LIST_FILE), "rb") as text_fd:
    print('\nScreening text again in the term list:')
    rescreened = client.text_moderation.screen_text(text_content_type="text/plain", text_content=text_fd,
        language="eng", autocorrect=False, pii=False, list_id=terms_list_id)
    assert isinstance(rescreened, Screen)
    rescreened_list =  list(rescreened.as_dict().items())
    for item in rescreened_list:
        print(item)

'''
Delete all terms
This leaves an empty list.
'''
print("\nDelete all terms in the term list {}.".format(terms_list_id))
client.list_management_term.delete_all_terms(list_id=terms_list_id, language="eng")

'''
Delete list
This deletes the list entirely.
'''
client.list_management_term_lists.delete(list_id=terms_list_id)
print("\nDeleted the term list {}.".format(terms_list_id))
'''
END - CUSTOM TERMS LIST
'''
print('\n##############################################################################\n')

'''
CREATE HUMAN IMAGE REVIEWS
These tasks will create a review for humans to moderate on the Content Moderator website.
https://{YOUR_REGION}.contentmoderator.cognitive.microsoft.com
Requires you to moderate an image on website (when prompted), 
then return to the command line to initiate printing of the results of the review.
'''
print("Create review for the image: {}.".format(os.path.basename(image_url_reviews)))
review_item = CreateReviewBodyItem(
    type= "Image",                     # Possible values include: 'Image', 'Text'
    content= image_url_reviews,        # URL for the image we want to review
    content_id= str(uuid.uuid4()),     # Random id
    callback_endpoint= call_back_endpoint, # Endpoint where the review image is sent
    metadata= [{
        # sc is the score, which will return the keys
        # 'a' (for adult) and 'r' (for racy) in the response.
        "key": "sc",
        # If the human reviewer clicks the 'a' and/or 'r' button on the image to be moderated on the website,
        # the response will show 'true'. If neither is clicked, it will be 'false'.
        # The 'True' will be sent to Azure as "str" cast.
        "value": True  
    }]
)

reviews = client_reviews.reviews.create_reviews(
    url_content_type="application/json",
    team_name=team_name,
    create_review_body=[review_item]  # As many review items as you need
)
review_id = reviews[0]  # Ordered list of string of review ID

print("\nGetting review details before human review...\n")
review_details = client_reviews.reviews.get_review(team_name=team_name, review_id=review_id)
for detail in list(review_details.as_dict().items()):
    print(detail)

input("\nPerform manual reviews on the Content Moderator Review Site, then press enter here.")

print("\nGetting review details after human review...")
review_details = client_reviews.reviews.get_review(team_name=team_name, review_id=review_id)

print('\nWait {} minutes for the server to process the request...\n'.format(LATENCY_DELAY))
# Could be shorter, however long it takes to get a 'status:Complete' response in the details.
# If the status comes back as 'Pending', it means the review was not processed yet, so try again.
time.sleep(LATENCY_DELAY * 60)

# Note the 'status' tag (should say 'Complete') and the 'reviewer_result_tags' 
# will say if the image has been marked as adult and/or racy.
for detail in list(review_details.as_dict().items()):
    print(detail)
'''
END - CREATE HUMAN IMAGE REVIEWS
'''
print('\n##############################################################################\n')
print('\n End of Moderation Tests.')