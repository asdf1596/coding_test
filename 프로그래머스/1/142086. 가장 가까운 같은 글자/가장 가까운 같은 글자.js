function solution(s) {
    var answer = [];
    let try1 = s.split("");
    let try2 = "";
    for(let a = 0;a<s.length;a++){
        answer.push(-1);
        for(let b = a-1;b>=0;b--){
            if(try1[a] == try1[b]){
                answer[a] = (a-b);
                break;
            }
        }
        if(answer[a] == 0) answer[a] = -1;
    }
    return answer;
}