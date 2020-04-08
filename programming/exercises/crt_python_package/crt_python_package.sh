python3 -m pip install --user --upgrade setuptools wheel

cd python_package
python3 setup.py sdist bdist_wheel

python3 -m pip install --user --upgrade twine

# deploy to DEV (PyPi)
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pytho_package_diogo
cd ..

# test with
# python
# >>> import pythonpkg