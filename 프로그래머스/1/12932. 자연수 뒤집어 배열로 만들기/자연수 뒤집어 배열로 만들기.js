function solution(n) {
    var answer = [];
    n = n.toString();
    n = n.split("");
    for(let a= n.length-1;a>=0;a--){
        answer.push(parseInt(n[a]));
    }
    return answer;
}