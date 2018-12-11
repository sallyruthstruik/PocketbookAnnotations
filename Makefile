
dev_config:
	bash dev_config.sh

dev: dev_config

build:
	cd guis/browser/client && npm run-script build

release_config:
	git checkout -- guis/browser/client/src/config.js

release: release_config build
