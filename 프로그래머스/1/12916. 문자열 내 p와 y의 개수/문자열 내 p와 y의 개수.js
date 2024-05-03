function solution(s){
    var answer = true;
    let i = 0;
    let y = s.split("");
    for(let a=0;a<y.length;a++){
        if(y[a]=="p" || y[a]=="P"){
            i++;
        }else if(y[a] == "Y" || y[a] == "y"){
            i--;
        }
    }
    if(i == 0){
        return true;
    }
    return false;
}