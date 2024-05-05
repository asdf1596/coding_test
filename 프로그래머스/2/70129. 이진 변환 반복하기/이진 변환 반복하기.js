function solution(s) {
    var answer = [];
    let code  = s.split("");
    let try1 = 0;
    let try2 = 0;
    let try3 = 0;
    while(true){
        if(code.length == 1){
            return [try3,try2]
            break;
        }
        try3++;
        for(let a = 0;a<code.length;a++){
            if(code[a] == "0"){
                code[a] = "";
                try2+=1;
            }
        }
        code = code.join("").split("");
        try1 = code.length;
        try1 = try1.toString(2);
        code = try1.split("");
    }
    console.log(code.join(""));
    return answer;
}