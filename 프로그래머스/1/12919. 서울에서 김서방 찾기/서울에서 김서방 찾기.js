function solution(seoul) {
    var answer = '';
    for(let a = 0;a<seoul.length;a++){
        if(seoul[a] == "Kim"){
            answer = '김서방은 '+a.toString()+'에 있다'
        }
    }
    return answer;
}