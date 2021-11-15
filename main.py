import random

responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.',
             'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.',
             'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.',
             'Better not ell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
             'Don\'t count on it.', 'My reply is no.', 'My sources say no.',
             'Outlook not so good.', 'Very doubtful.'
             ]


user_input = ''

while user_input != '-1':

    user_input = input('What do you want to ask the 8ball? (-1 to quit): ')
    if user_input[-1] != '?':
        print('Please end your response with a question mark')
        continue

    print(responses[random.randint(0, len(responses)-1)])


print('8ball going to sleep. Program finished.')