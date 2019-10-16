PHOTOS = 2

def family_tree(generations):
    number_of_photos = 0

    for generation in range(1, generations + 1):

        if generation is 1:
            number_of_photos = PHOTOS
        else:
            number_of_photos = number_of_photos * 2 + PHOTOS
    
    print("Number of generations: " + str(generations))
    print("The total number of photos will be: " + str(number_of_photos))

if __name__ == '__main__':
    family_tree(5)