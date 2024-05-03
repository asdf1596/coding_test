function solution(x) {
    let i = x.toString().split("");
    console.log(i);
    let y=  0;
    for(let a = 0;a<i.length;a++){
        y+=parseInt(i[a]);
    }
    console.log(y);
    return (x%y) ? false : true;
}