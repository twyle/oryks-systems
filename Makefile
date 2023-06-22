gunicorn:
	@cd services/app && gunicorn -b 0.0.0.0:5000 manage:app

initial-tag:
	@git tag -a -m "initial tag" v0.1.0

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

lint:
	@black --line-length 120 services/app
	@isort services/app
	@flake8
	# @pydocstyle  services/app/api
	# @pylint --rcfile=.pylintrc ./services/app/api

build-dev:
	@docker build -f ./services/app/Dockerfile -t oryks-systems-dev:latest ./services/app

run-dev:
	@docker run -p5000:5000 --env-file=./services/app/.env oryks-systems-dev:latest

build-prod:
	@docker build -f ./services/app/Dockerfile.prod -t oryks-systems-prod:latest ./services/app

run-prod:
	@docker run -p5000:5000 --env-file=./services/app/.env oryks-systems-prod:latest

# build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert|bump
