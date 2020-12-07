((...a) => a.some(_ => _)) ("", '', 0, false, null, NaN, undefined, _.keys({}).length, [].length)
[
    "",
    '',
     0,
     false,
     null,
     NaN,
     undefined,
     _.keys({}).length,
    [].length,
].some(Boolean)