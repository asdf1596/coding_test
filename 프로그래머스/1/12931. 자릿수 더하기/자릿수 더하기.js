function solution(n)
{
    var answer = 0;
    n = n.toString();
    n = n.split("");
    for(let a=0;a<n.length;a++){
        answer+=parseInt(n[a]);
    }
    return answer;
}