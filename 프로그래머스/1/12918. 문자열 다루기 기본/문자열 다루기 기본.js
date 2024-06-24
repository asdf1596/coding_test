function solution(s) {
    var answer = true;
    if(s.length != 4 && s.length !=6){
        return false;
    }
    for(let a = 0;a<s.length;a++){
        if((isNaN(s[a]))){
            return false;
        }
    }
    return answer;
}