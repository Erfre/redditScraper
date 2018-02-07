test = ['.jpg', '.png', '/a/', '/gallery/']

links_to_test_against = ['https://imgur.com/q26gWVs','https://i.redd.it/mxyp4grf30sz.jpg', 'https://i.imgur.com/OJcP8d7.jpg']
for link in links_to_test_against:
    print(link)
    for tests in test:
        if link.find(tests) != -1: #this means the string dont find the value
            print('not found')

        else:
            print(link.find(tests))