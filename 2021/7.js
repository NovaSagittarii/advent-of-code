fetch("https://adventofcode.com/2021/day/7/input").then(x=>x.text()).then(data=>{
    // data=`16,1,2,0,4,2,7,1,2,14`;
    // const lines = data.split('\n').filter(x=>x);
    const pos = data.split(',').map(x=>+x);
    pos.sort((a,b)=>a-b);
    console.log(pos.map(x => Math.abs(x-pos[~~(pos.length/2)])).reduce((a,b)=>a+b));

    let small = Infinity;
    for(let x = pos[0]; x <= pos[pos.length-1]; x ++){
        small = Math.min(small, pos.map(y => Math.abs(x-y)).map(n => n*(n+1)/2).reduce((a,b)=>a+b));
    }
    console.log(small);
});