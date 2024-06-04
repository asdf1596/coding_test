function solution(s, skip, index) {
    var answer = '';
    let try1 = [];
    let try2 = s.split("");
    skip = skip.split("");
    for(let a = 97;a<123;a++){
        if(skip.indexOf(String.fromCharCode(a)) == -1){
            try1.push(String.fromCharCode(a));
        }
    }
    for(let a = 0;a<try2.length;a++){
        let b = try1.indexOf(try2[a])+index;
        if(b>=26-skip.length) b%=26-skip.length;
        answer+=try1[b];
    }
    console.log(try1);
    return answer;
}