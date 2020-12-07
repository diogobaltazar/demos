# clean nulls 
ds = (
  ds
  .select('a', 'b', 'c')
  .filter(
    f.reduce(lambda x, y: x & y, [F.col(_).isNotNull() for _ in ['a', 'b', 'c']])
  )
)