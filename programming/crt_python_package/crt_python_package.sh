echo "[1 of 2] clearing ~/framework.dataeng/defw previous versions"
# crt src and built package
# creates build and dist (.whl, .tar.gz) folders 
cd ~/demos/programming/exercises/crt_python_package
rm -rf dist/* build/* *.egg-info
python3 setup.py sdist bdist_wheel

echo "[PRE-STEP] Executing fixes to previously found errors:"
# error: Error initializing plugin EntryPoint(name='Windows (alt)', value='keyrings.alt.Windows', group='keyring.backends').
# src: https://bugs.launchpad.net/usd-importer/+bug/1794041
pip3 install --upgrade keyrings.alt

echo "[2 of 3] uploading to PyPi"
# upload package to project
# DEV
# creates framework.dataeng.pkg.egg-info
# python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# PROD

twine upload dist/*

echo "[3 of 3] installing from PyPi. Test by importing 'python_package_exercise' to python3"
# install new package
# python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps defw
# PROD
pip3 install python_package_exercise
cd ~