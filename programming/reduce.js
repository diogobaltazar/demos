_ = require('lodash')

res = _.reduce(
    [
        {a: 'a', b: 'b'},
        {a: 'c', b: 'd'}
    ],
    (acc, val) => acc = acc.concat(`${val.a} - ${val.b}`),
    []
)

console.log(res)