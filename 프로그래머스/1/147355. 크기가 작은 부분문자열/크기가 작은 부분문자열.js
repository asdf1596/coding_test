function solution(t, p) {
    var answer = 0;
    let try1 = [];
    for(let a = 0;a<t.length-p.length+1;a++){
        try1.push(parseInt(t.slice(a,a+p.length)));
        if(try1[a] <= parseInt(p)) answer++;
        console.log(try1[a]);
    }
    return answer;
}