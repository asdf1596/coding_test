function solution(n) {
    var answer = 0;
    let try1 = [];
    for(let a = 1;a<187;a++){
        if(a%3!=0 && a%10!=3 && !(a>30 && a<40) && !(a>130 && a<=140)){
            try1.push(a);
        }
    }
    console.log(try1);
    return try1[n-1];
}