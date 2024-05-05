function solution(p) {
    p = p.split("");
    for(let a =0;a<p.length-4;a++){
        p[a] = "*";
    }
    return p.join("");
}