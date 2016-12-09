# example: make deploy version=1-0-0

deploy:
	npm run build
	appcfg.py --application=slept-well-app --version=$(version) update_queues .
	appcfg.py --application=slept-well-app --version=$(version) update_indexes .
	appcfg.py --application=slept-well-app --version=$(version) update .

update_queues:
	appcfg.py --application=slept-well-app --version=$(version) update_queues .

update_indexes:
	appcfg.py --application=slept-well-app --version=$(version) update_indexes .
