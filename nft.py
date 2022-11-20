from PIL import Image 
from IPython.display import display
import random
import json
import os

 
# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%
face = ["light", "chocolate"]
face_weights = [50, 50] 
ears = ["no child", "one child", "two child", "three child"]
ears_weights = [40, 30, 20, 10]
eyes = ["low income", "medium income", "high income", "extra income", "not clear"]
eyes_weights = [70, 10, 5 , 1 , 14] 
hair = ['under 18', '18-22', '22-25', '25-30', '30-35', '35-45', '45-55',
 '55-65',
 'retired',
 'retired with self-care ability',
 'retired without self-care ability',
 'dont want to disclose']
hair_weights = [10 , 10 , 10 , 10 ,10, 10, 10 ,10 ,10, 7 , 1 , 2]
mouth = ['high school', 'college', 'master', 'MBA', 'Ph.D', 'not to disclose']
mouth_weights = [10, 10,50, 10,15, 5]
nose = ['no_criminal_record', 'with_criminal_record']
nose_weights = [90, 10]
logo = ['logo']
logo_weights = [100]

print(nose_weights)



#Classify traits
logo_files = {"logo" : "logo"}

face_files = {
    "light": "face1",
    "chocolate": "face2"
}
ears_files = {
    "no child": "ears1",
    "one child": "ears2",
    "two child": "ears3",
    "three child": "ears4"
}
eyes_files = {
    "low income": "eyes1",
    "medium income": "eyes2",
    "high income": "eyes3",
    "extra income": "eyes4",
    "not clear": "eyes5"     
}
hair_files = {
    "under 18": "hair1",
    "18-22": "hair2",
    "22-25": "hair3",
    "25-30": "hair4",
    "30-35": "hair5",
    "35-45": "hair6",
    "45-55": "hair7",
    "55-65": "hair8",
    "retired": "hair9",
    "retired with self-care ability": "hair10",
    "retired without self-care ability": "hair11",
    "dont want to disclose": "hair12"
}
mouth_files = {
    "high school": "m1",
    "college": "m2",
    "master": "m3",
    "MBA": "m4",
    "Ph.D": "m5",
    "not to disclose": "m6"
}
nose_files = {
    "no_criminal_record": "n1",
    "with_criminal_record": "n2"   
}


## Generate Traits
TOTAL_IMAGES = 100 # Number of random unique images we want to generate
all_images = [] 
# A recursive function to generate unique image combinations
def create_new_image():
    new_image = {} #
    # For each trait category, select a random trait based on the weightings
    new_image ["Face"] = random.choices(face, face_weights)[0]
    new_image ["Ears"] = random.choices(ears, ears_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    new_image ["logo"] = random.choices(logo,logo_weights)[0]
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)



# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)
print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
print(all_images)


# Get Trait Counts
face_count = {}
for item in face:
    face_count[item] = 0
ears_count = {}
for item in ears:
    ears_count[item] = 0
eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
hair_count = {}
for item in hair:
    hair_count[item] = 0
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
nose_count = {}
for item in nose:
    nose_count[item] = 0
for image in all_images:
    face_count[image["Face"]] += 1
    ears_count[image["Ears"]] += 1
    eyes_count[image["Eyes"]] += 1
    hair_count[image["Hair"]] += 1
    mouth_count[image["Mouth"]] += 1
    nose_count[image["Nose"]] += 1
print(face_count)
print(ears_count)
print(eyes_count)
print(hair_count)
print(mouth_count)
print(nose_count)


#### Generate Images
os.mkdir(f'./images_3')
for item in all_images:
    im1 = Image.open(f'./scripts/face_parts/face/{face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./scripts/face_parts/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./scripts/face_parts/ears/{ears_files[item["Ears"]]}.png').convert('RGBA')
    im4 = Image.open(f'./scripts/face_parts/hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im5 = Image.open(f'./scripts/face_parts/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im6 = Image.open(f'./scripts/face_parts/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
    im7 = Image.open(f'./scripts/face_parts/logo/{logo_files[item["logo"]]}.png').convert('RGBA')
    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    #Convert to RGB
    rgb_im = com6.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images_3/" + file_name)


​
