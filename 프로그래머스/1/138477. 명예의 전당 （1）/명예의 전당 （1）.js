function solution(k, score) {
    var answer = [];
    let try1 = [];
    let try2 = 0;
    let try3 = 0;
    for(let a = 0;a<score.length;a++){
        if(!try1.length){
            try1.push(score[0]);
        }else{
            try2=try1[try1.length-1];
            if(try1.length==k){
                for(let b = 0;b<try1.length;b++){
                    if(score[a] >= try1[b]){
                        try1.splice(b,0,score[a]);
                        try1.length = k;
                        break;
                    }
                }
            }else{
                try3 = try1.length;
                for(let b = 0;b<try1.length;b++){
                    if(score[a] >= try1[b]){
                        try1.splice(b,0,score[a]);
                        break;
                    }
                }
                if(try1.length == try3) try1.push(score[a]);
            }
        }
        answer.push(try1[try1.length-1]);
    }
    return answer;
}