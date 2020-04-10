# crt src and built package
# creates build and dist (.whl, .tar.gz) folders 
cd simplepypkg
rm -rf dist/* build/* *.egg-info
python3 setup.py sdist bdist_wheel


# upload package to project
# DEV
# creates framework.dataeng.pkg.egg-info
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# PROD
twine upload dist/*

# install new package
# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps simplepypkg
# PROD
pip3 uninstall --yes simplepypkg2
pip3 install simplepypkg2

cd ..