fetch("https://adventofcode.com/2021/day/6/input").then(x=>x.text()).then(data=>{
    data2=`3,4,3,1,2`;
    const fish = [...new Array(9)].map(x=>0);
    const f = data.split(',').map(x=>+x).map(x => fish[x] ++);
    for(let i = 0; i < 256; i ++){
        let x = fish.shift();
        fish.push(0);
        fish[6] += x;
        fish[8] += x;
        if(i+1 == 80) console.log(fish.reduce((a,b)=>a+b));
    }
    // const lines = data.split('\n').filter(x=>x);
    console.log(fish.reduce((a,b)=>a+b))
});