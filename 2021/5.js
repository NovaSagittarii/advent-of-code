fetch("https://adventofcode.com/2021/day/5/input").then(x=>x.text()).then(data=>{
    // let map = [...new Array(10)].map(x=>[...new Array(10)].map(()=>'.'));
    const dict = {};
    const lines = data.split('\n').filter(x=>x);
    for(const line of lines){
        const [a,b,c,d] = line.replace(' -> ', ',').split(',').map(x=>+x);
        let dx = 0;
        let dy = 0;
        if(a < c) dx = 1;
        else if(a > c) dx = -1;
        if(b < d) dy = 1;
        else if(b > d) dy = -1;
        for(let i = 0; i <= Math.max(Math.abs(a-c),Math.abs(b-d)); i ++){
            let x = a + i * dx;
            let y = b + i * dy;
            let k = x+','+y;
            dict[k] = (dict[k]||0)+1;
            // map[y][x] = dict[k];
        }
    }
    // console.log(map.map(x=>x.join('')).join('\n'));
    console.log(Object.values(dict).filter(x=>x>=2).length);
});