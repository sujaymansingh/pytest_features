test:
	@poetry run python -m pytest -v calculator tests


format:
	@poetry run black calculator tests


watch-git-show:
	@watch -c git show --color=always
