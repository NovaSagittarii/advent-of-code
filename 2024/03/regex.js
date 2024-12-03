s.match(/mul\(\d+,\d+\)/g).map(x => x.replace(/[mul()]/g, '').split(',')).map(([x,y])=>x*y).reduce((a,b)=>a+b)

/**
// for part 2
FIND: don't\(\).*?do\(\)
REPLACE: 

FIND: $
REPLACE: \$
*/