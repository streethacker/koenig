help:
	@echo 'Makefile for koenig                    '
	@echo '                                         '
	@echo 'Usage:                                   '
	@echo '    make develop    make a develop env   '
	@echo '    make install    install as a package '

requirements:
	pip install -i http://pypi.douban.com/simple -r requirements.txt

develop: requirements
	python setup.py develop
	@echo
	@echo "Install finished"

install: requirements
	python setup.py install --record install.record
	@echo
	@echo "Install finished"
