function sn(s){
    const x = parseInt(s).toString(5).split('').map(x=>+x).reverse()
    console.log(x);
    for(let i = 0; i < x.length; i ++){
        if(x[i]>2){
            x[i] -= 5;
            if(i+1 >= x.length) x.push(0);
            x[i+1] += 1;
        }
    }
    const m = {
        "-2":"=", "-1":"-",
    }
    return x.reverse().map(k => m[k] || k).join("");
}
sn("4890")
sn("28061203326175")