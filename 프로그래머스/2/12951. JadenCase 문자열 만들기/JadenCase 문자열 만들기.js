function solution(s) {
    var answer = '';
    s=  s.split(" ");
    let try1 = [];
    for(let a = 0;a<s.length;a++){
        try1 = s[a].split("");
        for(let b = 0;b<try1.length;b++){
            if(b == 0){
                try1[b] = try1[b].toUpperCase();
            }
            if(b>=1){
                try1[b] = try1[b].toLowerCase();
            }
        }
        s[a] = try1.join("");
    }
    return s.join(" ");
}