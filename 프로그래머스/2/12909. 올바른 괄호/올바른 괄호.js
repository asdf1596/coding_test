function solution(s){
    var a = 0;
    s.split("");
    if(s[a] == `)`){
        return false;
    }
    for(let b = 0;b<s.length;b++){
        if(b!=0&&a == 0&&s[b] == `)`){
            return false;
        }
        if(s[b] == `(`){
            a+=1;
        }
        else{
            a-=1;
        }
    }
    return ((a) ? false : true);
}