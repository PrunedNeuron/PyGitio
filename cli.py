# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 18:32:14 2018
@author: https://git.io/ayush

"""

import requests
import click
import pyperclip


def getBaseURL():
    return 'https://git.io'


def gitioGetter(GitHubURL, customString):

    payload = {

        'url': GitHubURL,
        'code': customString

    }

    if(customString == ''):
        del payload['code']

    response = requests.post(getBaseURL(), data = payload)
    return response


def copyToClipBoard(textData):
    pyperclip.copy(textData)


@click.command(help = 'pygitio <GitHubURL> <CustomText>')
@click.argument('url')
@click.argument('custom', required=False)
def main(url = '', custom = ''):

    ''' 
    
        Custom git.io shortener. 
        COMMAND: pygitio <GitHubURL> <CustomText>

    '''

    customString = custom
    userURL = url

    if custom is not None:
        desiredURL = getBaseURL() + '/' + customString
    else:
        desiredURL = 'UNUSED'

    while(True):
        serverResponse = gitioGetter(userURL, customString)
        if(serverResponse.status_code == 422):
            # this means the customString is not available!
            click.secho('\nSorry, %s is not available. Enter a different custom string: ' % (custom), fg = 'red', nl = False)
            customString = input()
        elif(custom is None and serverResponse.status_code == 201):
            copyToClipBoard(serverResponse.headers['Location'])
            click.secho('\nYour URL has been shortened and has been copied to your clipboard. ', fg = 'green')
            click.secho('\nView your git.io URL in action here: %s' % (serverResponse.headers['Location']), fg = 'green')
            break
        elif(serverResponse.status_code == 201 and serverResponse.headers['Location'] == desiredURL):
            # This means the URL was successfully created
            copyToClipBoard(serverResponse.headers['Location'])
            click.secho('Your custom URL has been created and has been copied to your clipboard. ', fg = 'green')
            click.secho('\nView your git.io URL in action here: %s' % (serverResponse.headers['Location']), fg = 'green')
            break
        else:
            copyToClipBoard(serverResponse.headers['Location'])
            click.secho("\nThat URL already has a shortened link ( %s ), cannot shorten again. Existing link has been copied to your clipboard." % (serverResponse.headers['Location']), fg = 'cyan')
            break


if __name__ == '__main__':
    main()