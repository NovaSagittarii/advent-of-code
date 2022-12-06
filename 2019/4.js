function validate(num){
    const str = ""+num;
    if(!/([0-9])\1/.test(str.replace(/([0-9])\1{2,}/g, ''))) return false;
    if(str.split('').sort((a,b)=>a-b).join('') != str) return false;
    return true;
}
function solve(lo, hi){
    let sum = 0;
    for(let i = lo; i <= hi; i ++) sum += validate(i);
    console.log(sum);
    return sum;
}
solve(171309, 643603);