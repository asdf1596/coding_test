function solution(s) {
    var answer = '';
    if(s.length%2==0){
        answer = [s[s.length/2-1],s[s.length/2]].join("");
    }else{
        answer = s[(s.length-1)/2];
    }
    return answer;
}