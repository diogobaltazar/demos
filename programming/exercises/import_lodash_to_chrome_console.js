fetch('https://cdn.jsdelivr.net/npm/lodash@4.17.4/lodash.min.js')
.then(response => response.text())
.then(text => eval(text))