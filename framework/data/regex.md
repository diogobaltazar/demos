df = pd.DataFrame(data = {
    'a': [1, 2, 3, 4],
    'b': ['Raw value', 'raw value', 'raw Value', 'Raw Value']
})
df[df.parameter_type.str.match(r'(R|r)aw (V|v)alue') == False]
