function solution(s, n) {
    var answer = '';
    let try1 = [];
    for(let a = 0;a<s.length;a++){
        if(s[a] == " "){
            try1.push(" ");
            continue;
        }
        try1.push(s[a].charCodeAt(0));
        if(try1[a] >=65 &&try1[a] <= 90){
            if(try1[a]+n >90){
                try1[a]-=26; 
            }
        }else if(try1[a] >=97 &&try1[a] <= 122){
            if(try1[a]+n >122){
                try1[a]-=26; 
            }
        }
        try1[a]+=n;
        try1[a] = String.fromCharCode(try1[a]);
    }
    console.log(try1)
    return try1.join("");
}