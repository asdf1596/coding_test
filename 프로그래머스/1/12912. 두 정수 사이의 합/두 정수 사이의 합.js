function solution(a, b) {
    var answer = 0;
    if(a>b){
        answer = b;
        b = a;
        a = answer;
        answer = 0;
    }
    for(let c = a;c<b+1;c++){
        answer+=c;
    }
    return answer;
}