function solution(n) {
    var answer = n;
    let try1 = 0;
    let try2 = n.toString(2).split("");
    let try3 = 0;
    for(let a = 0;a<try2.length;a++){
        if(try2[a] == "1"){
            try1++;
        }
    }
    while(true){
        try3 = 0;
        answer++;
        try2 = answer.toString(2).split("");
        for(let a = 0;a<try2.length;a++){
            if(try2[a] == "1"){
                try3++;
            }
        }
        if(try3 == try1) break;
    }
    return answer;
}