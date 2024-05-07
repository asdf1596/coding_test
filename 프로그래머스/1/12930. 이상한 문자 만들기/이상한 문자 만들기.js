function solution(s) {
    var answer = '';
    let try1 = s.split(" ");
    let try2 = [];
    for(let a = 0;a<try1.length;a++){
        try2 = try1[a].split("");
        for(let b = 0;b<try2.length;b++){
            if(b%2==0 || b==0){
                try2[b] = try2[b].toUpperCase();
            }else{
                try2[b] = try2[b].toLowerCase();
            }
        }
        try1[a] = try2.join("");
    }
    answer = try1.join(" ");
    return answer;
}