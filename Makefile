
dev_config:
	bash dev_config.sh

dev: dev_config

build:
	cd guis/browser/client && npm run build
