import requests

# @click.command()
# @click.option('--custom', help = "To generate a custom git.io url.")
# @click.option('--randomize', help = "To generate a random git.io url.")

	# curl -X POST https://git.io -F "url=https://github.com/aniketdgp" -F "code=aniket"


def gitioGetter():

	baseURL = 'https://git.io'

	payload = {

		'url': 'https://github.com/aniketdgp',
		'code': 'aniketthestud'

	}

	response = requests.get(baseURL, data = payload).json() #USE GET NOT POST

	print(list(response))







def main():
	# will do stuff
	gitioGetter()

if __name__ == "__main__":
	main()
